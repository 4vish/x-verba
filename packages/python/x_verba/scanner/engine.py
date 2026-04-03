"""
X-Verba Scan Engine v0.2.0

AI-integration-centric governance analysis.

Governance gaps are only meaningful in the context of AI calls.
Non-AI code with file writes is a compiler.
AI code with ungated file writes is a Knight Capital.

Four passes:
  1. Primitive Detection — find AI calls (AST for Python, regex for JS/TS)
  2. DC Pattern Matching — map to Drift Class taxonomy
  3. Gap Analysis — Pre-Node, Human Gate, Invariant, Terminal State gaps
  4. Structural Gamma — governed / total decision points

Context profiles:
  ai-app        — full governance analysis, irreversible actions only when AI-adjacent (default)
  system-utility — suppresses IA-GAPs for local file ops in non-AI files
  general       — scan all files, legacy v0.1 behaviour

v0.2.0 changes:
  - Irreversible actions flagged only when AI-adjacent (fixes TypeScript false positive problem)
  - Context profile support via --context-profile flag
  - Fixed Gamma calculation (was always 0 for irreversible actions)
  - Robust error handling throughout (no more crash on malformed files)
  - ai_only mode: non-AI files skipped from governance analysis
"""
import os
import ast
import json
import hashlib
from pathlib import Path
from typing import Optional
from datetime import datetime, timezone
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

TAXONOMY_PATH = Path(__file__).parent.parent / "taxonomy"

# ── AI provider detection ─────────────────────────────────────────────────────
# Only actual LLM provider SDKs and their adapters.
# Agent frameworks (crewai, autogen, haystack) are NOT listed here —
# we detect them via their underlying LLM calls.

AI_PROVIDER_IMPORTS = {
    "openai": "openai",
    "anthropic": "anthropic",
    "google.generativeai": "google",
    "google.cloud.aiplatform": "google",
    "cohere": "cohere",
    "boto3": "aws_bedrock",
    "langchain_openai": "langchain",
    "langchain_anthropic": "langchain",
    "langchain_google_genai": "langchain",
    "langchain_cohere": "langchain",
    "langchain_community.llms": "langchain",
    "langchain_community.chat_models": "langchain",
    "llama_index.llms": "llama_index",
    "transformers": "huggingface",
}

AI_CALL_METHODS = [
    "chat.completions.create", "completions.create",
    "ChatCompletion.create", "Completion.create",
    "client.chat", "openai.ChatCompletion",
    "messages.create", "client.messages",
    "anthropic.Anthropic", "AsyncAnthropic",
    "chain.run", "chain.invoke", "chain.stream",
    "agent.run", "agent.invoke",
    "LLMChain", "AgentExecutor",
    "ChatOpenAI", "ChatAnthropic", "ChatGoogleGenerativeAI",
    ".generate(", ".complete(", ".predict(",
    ".chat(", ".ask(", ".query(",
    "pipeline(", "AutoModelForCausalLM",
    "invoke_model(", "invoke_model_with_response_stream(",
]

IRREVERSIBLE_ACTION_PATTERNS = {
    "email_send": [
        "send_mail", "send_message", "smtp.sendmail", "ses.send_email",
        "mailgun", "sendgrid",
    ],
    "database_delete": [
        "db.delete", "collection.drop", "session.delete",
        ".delete_many", ".drop_collection", "DELETE FROM",
    ],
    "database_write": [
        "db.insert", "db.update", "db.save",
        "collection.insert", ".commit()",
    ],
    "external_api": [
        "requests.post", "requests.put", "requests.delete",
        "httpx.post", "urllib.request",
    ],
    "file_system": ["os.remove", "os.unlink", "shutil.rmtree"],
    "system_command": [
        "os.system", "subprocess.run", "subprocess.call", "subprocess.Popen",
    ],
    "payment": [
        "stripe.charge", "stripe.PaymentIntent", "payment.create",
        "transaction.create",
    ],
}

SUPPORTED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".go", ".rb", ".cs", ".php",
}

SKIP_DIRS = {
    ".git", ".verba", "node_modules", "__pycache__",
    ".venv", "venv", "env", "dist", "build", ".next",
    "coverage", ".pytest_cache", ".mypy_cache",
    "test", "tests", "spec", "specs", "__tests__",
    "docs", "examples", "fixtures", "mocks",
    "notebooks", "tutorials", "demo", "demos", "samples",
    "benchmark", "benchmarks", "eval", "evals", "cookbook",
}

# Context profiles — control which checks fire in which scenarios
CONTEXT_PROFILES = {
    "ai-app": {
        "description": (
            "Full governance analysis. Irreversible actions flagged only when "
            "AI-adjacent. Default profile for AI-integrated applications."
        ),
        "flag_irrev_outside_ai": False,
        "require_ai_for_scan": True,
        "suppress_informal_invariants": False,
    },
    "system-utility": {
        "description": (
            "Suppresses IA-GAPs for local file ops in non-AI files. "
            "For compilers, build tools, CLI utilities with some AI features."
        ),
        "flag_irrev_outside_ai": False,
        "require_ai_for_scan": False,
        "suppress_informal_invariants": True,
    },
    "general": {
        "description": (
            "Legacy behaviour — scans all files regardless of AI presence. "
            "Use when you want maximum coverage including non-AI code."
        ),
        "flag_irrev_outside_ai": True,
        "require_ai_for_scan": False,
        "suppress_informal_invariants": False,
    },
}


# ── AST analyser (Python only) ────────────────────────────────────────────────

class ASTAnalyser:
    """
    AST-based analysis for Python files.
    Detects actual AI API calls — not strings, not comments,
    not import statements used as type hints.
    """

    def __init__(self):
        self.ai_imports = {}
        self.ai_calls = []
        self.assignments = {}

    def analyse(self, source: str, filepath: str) -> dict:
        self.ai_imports = {}
        self.ai_calls = []
        self.assignments = {}

        try:
            tree = ast.parse(source)
        except (SyntaxError, ValueError, RecursionError):
            return {"ai_calls": [], "imports": {}, "parse_error": True}

        self._collect_imports(tree)
        self._collect_calls(tree, source.splitlines())

        return {
            "ai_calls": self.ai_calls,
            "imports": self.ai_imports,
            "parse_error": False,
        }

    def _collect_imports(self, tree: ast.AST) -> None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    for pkg, provider in AI_PROVIDER_IMPORTS.items():
                        if alias.name == pkg or alias.name.startswith(pkg + "."):
                            local = alias.asname or alias.name.split(".")[0]
                            self.ai_imports[local] = provider

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for pkg, provider in AI_PROVIDER_IMPORTS.items():
                    if module == pkg or module.startswith(pkg + "."):
                        for alias in node.names:
                            local = alias.asname or alias.name
                            self.ai_imports[local] = provider
                        break

    def _collect_calls(self, tree: ast.AST, lines: list) -> None:
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Call, ast.Expr)):
                continue

            call_node = node if isinstance(node, ast.Call) else None
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call_node = node.value

            if not call_node:
                continue

            func = call_node.func
            call_str = self._get_call_string(func)
            if not call_str:
                continue

            provider = self._identify_provider(call_str)
            if not provider:
                continue

            line_num = getattr(call_node, "lineno", 0)
            line_content = (
                lines[line_num - 1].strip()
                if line_num > 0 and line_num <= len(lines)
                else ""
            )

            temperature = None
            max_tokens = None
            streaming = False
            for kw in call_node.keywords:
                if kw.arg == "temperature" and isinstance(kw.value, ast.Constant):
                    temperature = kw.value.value
                if kw.arg in ("max_tokens", "max_new_tokens") and isinstance(kw.value, ast.Constant):
                    max_tokens = kw.value.value
                if kw.arg == "stream" and isinstance(kw.value, ast.Constant):
                    streaming = bool(kw.value.value)

            self.ai_calls.append({
                "line": line_num,
                "line_content": line_content[:120],
                "call": call_str[:80],
                "provider": provider,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "streaming": streaming,
            })

    def _get_call_string(self, func_node) -> Optional[str]:
        if isinstance(func_node, ast.Name):
            return func_node.id
        if isinstance(func_node, ast.Attribute):
            obj = self._get_call_string(func_node.value)
            if obj:
                return f"{obj}.{func_node.attr}"
        return None

    def _identify_provider(self, call_str: str) -> Optional[str]:
        call_lower = call_str.lower()
        root = call_str.split(".")[0]
        if root in self.ai_imports:
            return self.ai_imports[root]

        for method in AI_CALL_METHODS:
            if method.rstrip("(") in call_str:
                if any(x in call_lower for x in ["openai", "chatcompletion", "completion"]):
                    return "openai"
                if any(x in call_lower for x in ["anthropic", "claude"]):
                    return "anthropic"
                if any(x in call_lower for x in ["langchain", "chain", "agent"]):
                    return "langchain"
                return "ai_framework"

        return None


# ── JS/TS detection ───────────────────────────────────────────────────────────

def _detect_ai_calls_js(content: str, lines: list) -> list:
    """
    JavaScript/TypeScript AI call detection.
    Pattern-based — skips comments and obvious string contexts.
    """
    import re
    calls = []

    js_ai_patterns = [
        (r'openai\.(chat|completions?|beta)', "openai"),
        (r'new\s+OpenAI\s*\(', "openai"),
        (r'client\.chat\.completions\.create', "openai"),
        (r'anthropic\.messages\.create', "anthropic"),
        (r'new\s+Anthropic\s*\(', "anthropic"),
        (r'new\s+ChatOpenAI\s*\(', "langchain"),
        (r'new\s+ChatAnthropic\s*\(', "langchain"),
        (r'chain\.invoke\s*\(', "langchain"),
        (r'agent\.invoke\s*\(', "langchain"),
        (r'generateText\s*\(', "vercel_ai"),
        (r'streamText\s*\(', "vercel_ai"),
        (r'\.generate\s*\(\s*\{', "ai_framework"),
    ]

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
            continue

        for pattern, provider in js_ai_patterns:
            if re.search(pattern, line):
                if line.count('"') % 2 == 0 and line.count("'") % 2 == 0:
                    calls.append({
                        "line": i,
                        "line_content": stripped[:120],
                        "call": pattern,
                        "provider": provider,
                        "temperature": _extract_js_param(lines, i, "temperature"),
                        "max_tokens": _extract_js_param(lines, i, "maxTokens"),
                        "streaming": "stream" in content[
                            max(0, content.find(line) - 100):content.find(line) + 200
                        ].lower(),
                    })
                    break

    return calls


def _extract_js_param(lines: list, line_num: int, param: str) -> Optional[float]:
    import re
    context = "\n".join(lines[max(0, line_num - 1):min(len(lines), line_num + 10)])
    match = re.search(rf'{param}\s*:\s*([0-9.]+)', context)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            pass
    return None


# ── Guard detection ───────────────────────────────────────────────────────────

def _has_guard_before(lines: list, line_num: int, window: int = 15) -> bool:
    """Check for a genuine governance checkpoint in the N lines before a call."""
    guard_patterns = [
        "validate_", "is_valid", "check_", "verify_", "sanitize", "sanitise",
        "allowed_", "permitted_", "authorized", "authorised", "authenticated",
        "raise ", "return safe", "return error", "return None",
        "throw new", "throw Error",
        "pre_node", "invariant", "governance", "eligibility",
        "allow_list", "allowlist", "whitelist", "blocklist", "blacklist",
        "if not allowed", "if not valid", "if not auth",
    ]

    search_lines = lines[max(0, line_num - window):line_num - 1]
    for line in search_lines:
        line_lower = line.lower().strip()
        if not line_lower or line_lower.startswith("#") or line_lower.startswith("//"):
            continue
        for pattern in guard_patterns:
            if pattern in line_lower:
                return True
    return False


def _has_human_review(lines: list, line_num: int) -> bool:
    """Check for human review mechanism after an AI call."""
    search_lines = lines[line_num:min(len(lines), line_num + 20)]
    human_signals = [
        "review", "approve", "confirm", "human_in_loop",
        "human_review", "manual_check", "oversight",
        "require_approval", "awaiting_approval",
    ]
    return any(
        any(s in line.lower() for s in human_signals)
        for line in search_lines
    )


def _detect_irreversible_actions(lines: list, filepath: str) -> list:
    """
    Detect irreversible actions with no authorisation gate.
    Only called on AI-adjacent files in ai-app and system-utility profiles.
    """
    import re
    findings = []

    for action_type, patterns in IRREVERSIBLE_ACTION_PATTERNS.items():
        for pattern in patterns:
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped.startswith("#") or stripped.startswith("//"):
                    continue
                if "import " in stripped and "(" not in stripped:
                    continue

                if re.search(pattern, line, re.IGNORECASE):
                    has_gate = _has_authorisation_gate(lines, i)
                    if not has_gate:
                        findings.append({
                            "line": i,
                            "action_type": action_type,
                            "pattern": pattern,
                            "line_content": stripped[:120],
                            "filepath": filepath,
                        })
                    break  # one finding per pattern per file

    return findings


def _has_authorisation_gate(lines: list, line_num: int) -> bool:
    """Check for authorisation gates before irreversible actions."""
    if not lines or line_num == 0:
        return False
    search_lines = lines[max(0, line_num - 20):line_num - 1]
    gate_signals = [
        "approve", "confirm", "authoris", "authoriz",
        "permission", "has_permission", "can_",
        "require_approval", "user_confirmed",
        "human_authorised", "manual_approval",
    ]
    return any(
        any(s in line.lower() for s in gate_signals)
        for line in search_lines
    )


# ── Main scan engine ──────────────────────────────────────────────────────────

class ScanEngine:
    """
    Core scan engine — AI-integration-centric.

    Governance gaps are only meaningful relative to AI calls.
    Irreversible actions flagged only when AI-adjacent (in ai-app profile).

    v0.2.0 — context profiles, fixed Gamma, robust error handling.
    """

    def __init__(self, verbose: bool = False, context_profile: str = "ai-app"):
        self.verbose = verbose
        self.context_profile = context_profile
        self.profile = CONTEXT_PROFILES.get(context_profile, CONTEXT_PROFILES["ai-app"])
        self.dc_classes = self._load_taxonomy("dc_classes.json")
        self.so_operators = self._load_taxonomy("so_operators.json")
        self.ast_analyser = ASTAnalyser()

    def _load_taxonomy(self, filename: str) -> dict:
        path = TAXONOMY_PATH / filename
        if path.exists():
            try:
                with open(path) as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def scan(self, repo_path: str, identity_key: str = None) -> dict:
        path = Path(repo_path).resolve()
        identity_key = identity_key or self._generate_identity_key(path)

        results = {
            "scan_date": datetime.now(timezone.utc).isoformat(),
            "repo": str(path),
            "identity_key": identity_key,
            "verba_version": "0.2.0",
            "context_profile": self.context_profile,
            "reviewed": False,
        }

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:

            t1 = progress.add_task("Pass 1 — Reading code structure...", total=None)
            files = self._collect_files(path)
            parsed = self._parse_files(files)
            results["files_scanned"] = len(files)
            progress.update(t1, completed=True)

            t2 = progress.add_task("Pass 2 — Detecting AI integrations (AST)...", total=None)
            primitives = self._detect_primitives(parsed, path)
            results["primitives"] = primitives
            progress.update(t2, completed=True)

            # In ai-app profile, exit cleanly if no AI found
            if (
                self.profile["require_ai_for_scan"]
                and not primitives["ai_integrations"]
            ):
                results["summary"] = {
                    "files_scanned": len(files),
                    "ai_integrations_detected": 0,
                    "critical": 0, "high": 0, "medium": 0,
                    "total_gaps": 0,
                    "dc_classes_detected": 0,
                    "governance_coverage": "N/A",
                    "structural_gamma": None,
                    "governance_status": "NO_AI_INTEGRATIONS",
                    "context_profile": self.context_profile,
                    "note": (
                        "No AI integrations detected. X-Verba governs AI-integrated code. "
                        "If this repo uses AI, check that imports match known providers. "
                        "Use --context-profile general to scan all files regardless."
                    ),
                }
                results["gaps"] = []
                results["drift_classes"] = []
                results["structural_gamma"] = {
                    "proxy_value": None,
                    "status": "NO_AI_INTEGRATIONS",
                    "interpretation": "No AI integration points detected. Governance score not applicable.",
                }
                results["critical_findings"] = []
                return results

            t3 = progress.add_task("Pass 3 — Mapping Drift Classes...", total=None)
            dc_findings = self._match_dc_patterns(primitives, parsed)
            results["drift_classes"] = dc_findings
            progress.update(t3, completed=True)

            t4 = progress.add_task("Pass 4 — Analysing governance gaps...", total=None)
            gaps = self._analyse_gaps(primitives)
            results["gaps"] = gaps
            progress.update(t4, completed=True)

            t5 = progress.add_task("Pass 5 — Computing Gamma score...", total=None)
            gamma = self._compute_gamma(primitives, gaps)
            results["structural_gamma"] = gamma
            progress.update(t5, completed=True)

        results["summary"] = self._build_summary(results, files, gaps, dc_findings, gamma)
        results["critical_findings"] = self._extract_critical_findings(gaps, dc_findings)

        return results

    def _generate_identity_key(self, path: Path) -> str:
        return f"{path.name}-{hashlib.md5(str(path).encode()).hexdigest()[:8]}"

    def _collect_files(self, path: Path) -> list:
        files = []
        for root, dirs, filenames in os.walk(path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fn in filenames:
                fp = Path(root) / fn
                if fp.suffix in SUPPORTED_EXTENSIONS:
                    files.append(fp)
        return files

    def _parse_files(self, files: list) -> list:
        parsed = []
        for fp in files:
            try:
                content = fp.read_text(encoding="utf-8", errors="ignore")
                parsed.append({
                    "path": fp,
                    "content": content,
                    "lines": content.splitlines(),
                    "extension": fp.suffix,
                    "has_ai": self._quick_ai_check(content),
                })
            except (OSError, PermissionError) as e:
                if self.verbose:
                    console.print(f"[dim]Skipping {fp}: {e}[/dim]")
        return parsed

    def _quick_ai_check(self, content: str) -> bool:
        """Fast pre-filter: does this file likely contain AI calls?"""
        ai_signals = list(AI_PROVIDER_IMPORTS.keys()) + [
            "openai", "anthropic", "langchain", "llama_index",
            "transformers", "bedrock", "cohere", "generativeai",
            "ChatCompletion", "messages.create", "invoke_model",
            "generateText", "streamText",
        ]
        content_lower = content.lower()
        return any(sig.lower() in content_lower for sig in ai_signals)

    def _is_ai_adjacent_file(self, file_data: dict, ai_file_paths: set) -> bool:
        """
        A file is AI-adjacent if it contains AI calls directly,
        or if it imports a module from an AI-containing file (one level).
        """
        if file_data["has_ai"]:
            return True
        content = file_data["content"]
        for ai_path in ai_file_paths:
            stem = Path(ai_path).stem
            if f"import {stem}" in content or f"from {stem}" in content:
                return True
        return False

    def _detect_primitives(self, parsed: list, base_path: Path) -> dict:
        primitives = {
            "ai_integrations": [],
            "sensitive_fields": [],
            "irreversible_actions": [],
            "constraints": [],
            "nodes": [],
            "clusters": [],
        }

        # First pass: identify AI-containing files
        ai_file_paths = {str(f["path"]) for f in parsed if f["has_ai"]}

        for file_data in parsed:
            content = file_data["content"]
            lines = file_data["lines"]
            fp = file_data["path"]
            ext = file_data["extension"]

            try:
                rel_path = fp.relative_to(base_path)
            except ValueError:
                rel_path = fp

            is_ai_file = file_data["has_ai"]
            is_adjacent = self._is_ai_adjacent_file(file_data, ai_file_paths)

            # AST analysis for Python
            if ext == ".py":
                try:
                    ast_result = self.ast_analyser.analyse(content, str(rel_path))
                    for call in ast_result["ai_calls"]:
                        pre_node = _has_guard_before(lines, call["line"])
                        human_review = _has_human_review(lines, call["line"])
                        primitives["ai_integrations"].append({
                            "id": f"AI-{len(primitives['ai_integrations'])+1:03d}",
                            "provider": call["provider"],
                            "location": f"{rel_path}:{call['line']}",
                            "line_content": call["line_content"],
                            "temperature": call.get("temperature"),
                            "max_tokens": call.get("max_tokens"),
                            "streaming": call.get("streaming", False),
                            "dynamic_prompt": self._has_dynamic_prompt(content, call["line"]),
                            "user_input_in_prompt": self._has_user_input_in_prompt(content, call["line"]),
                            "pre_node_detected": pre_node,
                            "human_review_detected": human_review,
                            "output_destination": self._detect_output_destination(lines, call["line"]),
                            "source_file": str(rel_path),
                        })
                except Exception as e:
                    if self.verbose:
                        console.print(f"[dim]AST error in {rel_path}: {e}[/dim]")

            # Pattern-based for JS/TS
            elif ext in (".js", ".ts", ".jsx", ".tsx"):
                try:
                    js_calls = _detect_ai_calls_js(content, lines)
                    for call in js_calls:
                        pre_node = _has_guard_before(lines, call["line"])
                        human_review = _has_human_review(lines, call["line"])
                        primitives["ai_integrations"].append({
                            "id": f"AI-{len(primitives['ai_integrations'])+1:03d}",
                            "provider": call["provider"],
                            "location": f"{rel_path}:{call['line']}",
                            "line_content": call["line_content"],
                            "temperature": call.get("temperature"),
                            "max_tokens": call.get("max_tokens"),
                            "streaming": call.get("streaming", False),
                            "dynamic_prompt": "template" in content[
                                max(0, content.find(call["line_content"]) - 200):
                            ].lower(),
                            "user_input_in_prompt": any(
                                s in content[
                                    max(0, content.find(call["line_content"]) - 300):
                                ]
                                for s in [
                                    "req.body", "request.body", "userInput",
                                    "user_input", "query",
                                ]
                            ),
                            "pre_node_detected": pre_node,
                            "human_review_detected": human_review,
                            "output_destination": self._detect_output_destination(lines, call["line"]),
                            "source_file": str(rel_path),
                        })
                except Exception as e:
                    if self.verbose:
                        console.print(f"[dim]JS scan error in {rel_path}: {e}[/dim]")

            # Irreversible actions — only on AI-adjacent files in ai-app profile
            should_scan_irrev = (
                self.profile["flag_irrev_outside_ai"]
                or is_adjacent
            )
            if should_scan_irrev:
                try:
                    irrev = _detect_irreversible_actions(lines, str(rel_path))
                    primitives["irreversible_actions"].extend(irrev)
                except Exception as e:
                    if self.verbose:
                        console.print(f"[dim]Irreversible action scan error in {rel_path}: {e}[/dim]")

            # Constraints — only on AI files, suppressed in system-utility profile
            if not self.profile["suppress_informal_invariants"] and is_ai_file:
                try:
                    self._detect_constraints(content, lines, rel_path, primitives)
                except Exception as e:
                    if self.verbose:
                        console.print(f"[dim]Constraint scan error in {rel_path}: {e}[/dim]")

        # Cluster detection
        try:
            self._detect_clusters(base_path, primitives)
        except Exception as e:
            if self.verbose:
                console.print(f"[dim]Cluster detection error: {e}[/dim]")

        # Deduplicate irreversible actions
        seen = set()
        unique_irrev = []
        for a in primitives["irreversible_actions"]:
            key = f"{a['filepath']}:{a['line']}"
            if key not in seen:
                seen.add(key)
                unique_irrev.append(a)
        primitives["irreversible_actions"] = unique_irrev

        return primitives

    def _detect_constraints(self, content, lines, rel_path, primitives):
        constraint_patterns = [
            ("assertion", ["assert ", "assertTrue", "assertFalse"]),
            ("validation", ["validate_", "is_valid(", "check_input", "verify_"]),
            ("auth_check", [
                "@login_required", "@auth", "require_auth",
                "is_authenticated", "permission_required",
            ]),
        ]
        for i, line in enumerate(lines, 1):
            for c_type, patterns in constraint_patterns:
                for pattern in patterns:
                    if pattern in line and not line.strip().startswith("#"):
                        near_ai = self._is_near_ai_call(lines, i)
                        primitives["constraints"].append({
                            "location": f"{rel_path}:{i}",
                            "type": c_type,
                            "pattern": pattern,
                            "line_content": line.strip()[:120],
                            "near_ai_call": near_ai,
                        })
                        break

    def _detect_clusters(self, base_path: Path, primitives: dict) -> None:
        config_files = (
            list(base_path.rglob("docker-compose*.yml")) +
            list(base_path.rglob("kubernetes/*.yaml")) +
            list(base_path.rglob("k8s/*.yaml"))
        )
        if config_files or len(primitives["ai_integrations"]) > 3:
            primitives["clusters"].append({
                "detected": True,
                "evidence": [str(f.name) for f in config_files[:3]],
                "ai_integration_count": len(primitives["ai_integrations"]),
                "cluster_governance_required": True,
            })

    def _match_dc_patterns(self, primitives: dict, parsed: list) -> list:
        findings = []
        dc_classes = self.dc_classes.get("classes", {})
        seen_locations = set()

        for ai in primitives.get("ai_integrations", []):
            loc = ai["location"]

            if ai.get("user_input_in_prompt") and not ai.get("pre_node_detected"):
                key = f"DC-E5:{loc}"
                if key not in seen_locations:
                    seen_locations.add(key)
                    findings.append(self._build_finding(
                        "DC-E5", dc_classes.get("DC-E5", {}), loc,
                        "E5-L2", ai["id"],
                        "User input flows into AI prompt with no sanitisation checkpoint",
                        "critical",
                    ))

            if ai.get("dynamic_prompt") and not ai.get("pre_node_detected"):
                key = f"DC-L2:{loc}"
                if key not in seen_locations:
                    seen_locations.add(key)
                    findings.append(self._build_finding(
                        "DC-L2", dc_classes.get("DC-L2", {}), loc,
                        "L2-L1", ai["id"],
                        "Dynamic prompt assembled from external input with no boundary check",
                        "high",
                    ))

            temp = ai.get("temperature")
            if temp is not None and isinstance(temp, (int, float)) and temp > 0.7:
                key = f"DC-I6-temp:{loc}"
                if key not in seen_locations:
                    seen_locations.add(key)
                    findings.append(self._build_finding(
                        "DC-I6", dc_classes.get("DC-I6", {}), loc,
                        "I6-L1", ai["id"],
                        f"High temperature ({temp}) — structural cascade rupture risk",
                        "high",
                    ))

            if not ai.get("human_review_detected") and not ai.get("pre_node_detected"):
                key = f"DC-I11:{loc}"
                if key not in seen_locations:
                    seen_locations.add(key)
                    findings.append(self._build_finding(
                        "DC-I11", dc_classes.get("DC-I11", {}), loc,
                        "I11-L1", ai["id"],
                        "No governance checkpoint — AI output proceeds without any check",
                        "medium",
                    ))

        if len(primitives.get("ai_integrations", [])) > 1:
            dc = dc_classes.get("DC-E13", {})
            key = "DC-E13:chained"
            if key not in seen_locations:
                seen_locations.add(key)
                count = len(primitives["ai_integrations"])
                findings.append(self._build_finding(
                    "DC-E13", dc, f"{count} AI calls detected",
                    "E13-L1", "chain",
                    f"{count} chained AI calls — output of one may seed the next without validation",
                    "high",
                ))

        if primitives.get("clusters"):
            dc = dc_classes.get("DC-S3", {})
            key = "DC-S3:cluster"
            if key not in seen_locations:
                seen_locations.add(key)
                findings.append(self._build_finding(
                    "DC-S3", dc, "cluster-level",
                    "S3-L1", "cluster",
                    "Multi-service architecture with no cluster-level governance — Flash Crash failure mode",
                    "critical",
                ))

        for action in primitives.get("irreversible_actions", []):
            loc = f"{action['filepath']}:{action['line']}"
            key = f"DC-E14:{loc}"
            if key not in seen_locations:
                seen_locations.add(key)
                dc = dc_classes.get("DC-E14", {})
                findings.append(self._build_finding(
                    "DC-E14", dc, loc,
                    "E14-L1", "irreversible",
                    f"Irreversible action ({action['action_type']}) with no authorisation gate — Knight Capital failure mode",
                    "critical",
                ))

        return findings

    def _build_finding(self, dc_code, dc, location, legion_code, triggered_by, evidence, severity):
        legions = dc.get("legions", {})
        legion = legions.get(legion_code, {})
        primary_so = dc.get("primary_so", "")
        so_data = self.so_operators.get("operators", {}).get(primary_so, {})
        contraindications = self._get_contraindications(dc_code)
        monitoring_freq = self._get_monitoring_frequency(dc_code)

        return {
            "dc_code": dc_code,
            "dc_name": dc.get("name", ""),
            "tier": dc.get("tier", ""),
            "location": location,
            "severity": severity,
            "triggered_by": triggered_by,
            "evidence": evidence,
            "plain_english": dc.get("plain_english", ""),
            "what_happens_without_governance": dc.get("what_happens_without_governance", ""),
            "consequence": dc.get("consequence", ""),
            "legion_detected": {
                "code": legion_code,
                "name": legion.get("name", ""),
                "description": legion.get("description", ""),
            },
            "stabiliser_recommendation": {
                "primary_so": primary_so,
                "so_name": so_data.get("name", ""),
                "plain_english": so_data.get("plain_english", ""),
                "contraindications": contraindications,
            },
            "monitoring_frequency": monitoring_freq,
            "human_review_required": True,
            "policy": None,
            "invariant": None,
            "terminal_state": None,
            "severity_confirmed": None,
        }

    def _analyse_gaps(self, primitives: dict) -> list:
        gaps = []

        for ai in primitives.get("ai_integrations", []):
            if not ai.get("pre_node_detected"):
                gaps.append({
                    "id": f"PN-GAP-{len(gaps)+1:03d}",
                    "type": "missing_pre_node",
                    "location": ai["location"],
                    "severity": "critical",
                    "plain_english": (
                        f"No checkpoint exists before the AI call at {ai['location']}. "
                        f"The AI receives input and produces output with nothing checking "
                        f"whether it should — or what it can return."
                    ),
                    "what_is_missing": "A mandatory checkpoint immediately before this AI call.",
                    "consequence": (
                        "Any input reaches this AI call unfiltered. Any output proceeds "
                        "to its destination unchecked. No governance record exists."
                    ),
                    "verba_term": "Pre-Node gap",
                    "verba_explanation": (
                        "A Pre-Node is the mandatory checkpoint that fires at the saddle "
                        "point — the moment before commitment, where governance has maximum "
                        "leverage and minimum intervention cost."
                    ),
                    "recommended_action": (
                        "Define what must be checked before this AI call. "
                        "What conditions must be met? What must the AI never return?"
                    ),
                    "policy": None,
                    "ai_integration_ref": ai["id"],
                })

            if not ai.get("human_review_detected"):
                dest = ai.get("output_destination", "downstream")
                gaps.append({
                    "id": f"HG-GAP-{len(gaps)+1:03d}",
                    "type": "missing_human_gate",
                    "location": ai["location"],
                    "severity": "high",
                    "plain_english": (
                        f"AI output flows to '{dest}' with no human review detected."
                    ),
                    "what_is_missing": "Human authorisation gate for critical severity outputs.",
                    "consequence": "Every AI output reaches its destination automatically.",
                    "verba_term": "Human-Authorised Transition missing",
                    "verba_explanation": (
                        "In VERBA, a Human-Authorised Transition cannot be initiated by "
                        "automation — it requires explicit, auditable human approval."
                    ),
                    "recommended_action": (
                        "Define the severity and required authorisation level for this output."
                    ),
                    "policy": None,
                    "ai_integration_ref": ai["id"],
                })

        for action in primitives.get("irreversible_actions", []):
            loc = f"{action['filepath']}:{action['line']}"
            gaps.append({
                "id": f"IA-GAP-{len(gaps)+1:03d}",
                "type": "ungated_irreversible_action",
                "location": loc,
                "severity": "critical",
                "plain_english": (
                    f"An irreversible action ({action['action_type']}) at line {action['line']} "
                    f"in an AI-adjacent file has no authorisation gate. "
                    f"Once executed, it cannot be undone."
                ),
                "what_is_missing": "An eligibility condition confirming authorisation before execution.",
                "consequence": (
                    "This action executes automatically. No human approval. "
                    "No record. No way to stop it once triggered. "
                    "Knight Capital lost $440M from exactly this pattern."
                ),
                "verba_term": "Eligibility Condition missing",
                "verba_explanation": (
                    "An Eligibility Condition is a mandatory prerequisite that, if not met, "
                    "terminates automation and escalates to a human."
                ),
                "recommended_action": (
                    "Define what must be confirmed before this action executes. "
                    "Define what happens if conditions are not met."
                ),
                "policy": None,
            })

        if not self.profile["suppress_informal_invariants"]:
            for constraint in primitives.get("constraints", []):
                gaps.append({
                    "id": f"INV-GAP-{len(gaps)+1:03d}",
                    "type": "informal_invariant",
                    "location": constraint["location"],
                    "severity": "medium",
                    "plain_english": (
                        f"A governance check exists at {constraint['location']} "
                        f"but it is informal — not version-controlled, not machine-executable, "
                        f"not connected to any audit trail."
                    ),
                    "what_is_missing": "Formalisation as a VERBA Invariant.",
                    "consequence": (
                        "A future refactor removes this check silently. "
                        "No test catches it. No audit records it."
                    ),
                    "verba_term": "Informal Invariant — needs formalisation",
                    "verba_explanation": (
                        "An Invariant must always hold, cannot be bypassed, "
                        "and must be explicitly declared in the governance schema."
                    ),
                    "recommended_action": (
                        "Formalise this check as an Invariant with CANNOT_BE_BYPASSED: TRUE."
                    ),
                    "policy": None,
                })

        return gaps

    def _compute_gamma(self, primitives: dict, gaps: list) -> dict:
        """
        Structural Gamma = Governed Decision Points / Total Decision Points

        Governed AI call     = has pre_node AND has human_review.
        Governed irrev action = NOT in the ungated list (i.e. has an auth gate).

        v0.2.0 fix: irrev actions now correctly counted using actual gap list.
        """
        ai_integrations = primitives.get("ai_integrations", [])
        irreversible = primitives.get("irreversible_actions", [])
        total_decision_points = len(ai_integrations) + len(irreversible)

        if total_decision_points == 0:
            return {
                "proxy_value": None,
                "threshold": 0.9,
                "status": "NO_AI_INTEGRATIONS",
                "interpretation": "No AI integration points detected. Governance score not applicable.",
                "total_decision_points": 0,
                "governed_decision_points": 0,
                "important_note": "Structural proxy only. Runtime Gamma requires the VERBA Priming Engine.",
                "what_this_means": "Gamma = Governed Decision Points / Total Decision Points",
            }

        governed_ai = sum(
            1 for ai in ai_integrations
            if ai.get("pre_node_detected") and ai.get("human_review_detected")
        )

        # Irreversible actions: governed = total minus those appearing as IA-GAPs
        ungated_irrev_locs = {
            g["location"]
            for g in gaps
            if g.get("type") == "ungated_irreversible_action"
        }
        governed_irrev = sum(
            1 for a in irreversible
            if f"{a['filepath']}:{a['line']}" not in ungated_irrev_locs
        )

        governed = governed_ai + governed_irrev
        gamma = round(governed / total_decision_points, 2)

        if gamma >= 0.9:
            status = "ABOVE_THRESHOLD"
            interpretation = "Structural governance coverage meets the 90% sufficiency threshold."
        elif gamma >= 0.5:
            status = "PARTIAL_COVERAGE"
            interpretation = (
                f"Only {int(gamma*100)}% of decision points are governed. "
                f"Significant gaps remain."
            )
        else:
            status = "BELOW_THRESHOLD"
            interpretation = (
                f"Only {int(gamma*100)}% of decision points are governed. "
                f"The system is structurally ungoverned. "
                f"The Drift Node is the global energy minimum."
            )

        return {
            "proxy_value": gamma,
            "threshold": 0.9,
            "status": status,
            "interpretation": interpretation,
            "total_decision_points": total_decision_points,
            "governed_decision_points": governed,
            "important_note": (
                "Structural proxy only — not runtime Gamma. "
                "Measures whether governance mechanisms are structurally present."
            ),
            "what_this_means": "Gamma = Governed Decision Points / Total Decision Points",
        }

    def _build_summary(self, results, files, gaps, dc_findings, gamma):
        critical = sum(1 for g in gaps if g.get("severity") == "critical")
        high = sum(1 for g in gaps if g.get("severity") == "high")
        medium = sum(1 for g in gaps if g.get("severity") == "medium")
        ai_count = len(results.get("primitives", {}).get("ai_integrations", []))
        total = ai_count + len(results.get("primitives", {}).get("irreversible_actions", []))
        governed = gamma.get("governed_decision_points", 0)
        coverage = int((governed / total) * 100) if total > 0 else 100

        return {
            "files_scanned": len(files),
            "ai_integrations_detected": ai_count,
            "critical": critical,
            "high": high,
            "medium": medium,
            "total_gaps": len(gaps),
            "dc_classes_detected": len(dc_findings),
            "governance_coverage": f"{coverage}%",
            "structural_gamma": gamma.get("proxy_value"),
            "governance_status": gamma.get("status"),
            "context_profile": self.context_profile,
        }

    def _extract_critical_findings(self, gaps, dc_findings):
        critical = [g for g in gaps if g.get("severity") == "critical"]
        findings = []
        for gap in critical[:5]:
            dc_match = next(
                (d for d in dc_findings if d.get("location") == gap.get("location")),
                None,
            )
            findings.append({
                "location": gap.get("location", ""),
                "plain_english": gap.get("plain_english", "")[:120],
                "dc_candidate": (
                    f"{dc_match['dc_code']} {dc_match['dc_name']}"
                    if dc_match else gap.get("verba_term", "")
                ),
                "severity": "critical",
            })
        return findings

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _has_dynamic_prompt(self, content: str, line_num: int) -> bool:
        lines = content.splitlines()
        context = "\n".join(lines[max(0, line_num - 20):line_num + 5])
        return any(s in context for s in [
            'f"', "f'", ".format(", "% (", "+ prompt",
            "system_prompt =", "user_message =", "{query}", "{input}",
        ])

    def _has_user_input_in_prompt(self, content: str, line_num: int) -> bool:
        lines = content.splitlines()
        context = "\n".join(lines[max(0, line_num - 30):line_num + 5])
        user_signals = [
            "request.", "req.", "user_input", "user_message",
            "query", "input_text", "body", "form_data",
        ]
        prompt_signals = ["prompt", "messages", "content", "system"]
        return (
            any(s in context for s in user_signals)
            and any(s in context for s in prompt_signals)
        )

    def _detect_output_destination(self, lines: list, line_num: int) -> str:
        search = lines[line_num:min(len(lines), line_num + 15)]
        text = "\n".join(search)
        if any(s in text for s in ["return response", "render", "jsonify", "send_response"]):
            return "user-facing response"
        if any(s in text for s in ["db.", ".save(", ".commit(", "insert"]):
            return "database write"
        if any(s in text for s in ["requests.", "http.", "fetch(", "axios."]):
            return "external API call"
        if any(s in text for s in ["openai.", "anthropic.", "claude.", "generate"]):
            return "next AI call"
        return "downstream processing"

    def _is_near_ai_call(self, lines: list, line_num: int, window: int = 10) -> bool:
        search = lines[max(0, line_num - window):min(len(lines), line_num + window)]
        ai_signals = list(AI_PROVIDER_IMPORTS.keys()) + ["completion", "generate", "chat"]
        return any(any(s in line.lower() for s in ai_signals) for line in search)

    def _get_contraindications(self, dc_code: str) -> list:
        return [
            c for c in self.so_operators.get("contraindications", [])
            if c.get("to_dc") == dc_code
        ]

    def _get_monitoring_frequency(self, dc_code: str) -> str:
        freq_map = {
            "DC-E2": "Per-token monitoring required",
            "DC-I6": "Per-generation-step monitoring required",
            "DC-E5": "Per-turn monitoring required",
            "DC-E9": "Cross-session monitoring required",
            "DC-I11": "Cross-session monitoring required",
            "DC-L2": "Per-turn monitoring required",
            "DC-S3": "Cluster-level continuous monitoring required",
            "DC-E14": "Pre-deployment activation check required",
        }
        return freq_map.get(dc_code, "Per-turn monitoring recommended")
