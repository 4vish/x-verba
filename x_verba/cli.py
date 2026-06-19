"""
X-Verba CLI entry point — v0.4.0
Find the governance gaps in your AI code before your users do.
"""
import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

BANNER = """
 ██╗  ██╗      ██╗   ██╗███████╗██████╗ ██████╗  █████╗
 ╚██╗██╔╝      ██║   ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
  ╚███╔╝ █████╗██║   ██║█████╗  ██████╔╝██████╔╝███████║
  ██╔██╗ ╚════╝╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██╗██╔══██║
 ██╔╝ ██╗       ╚████╔╝ ███████╗██║  ██║██████╔╝██║  ██║
 ╚═╝  ╚═╝        ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝

 Governance Infrastructure for the AI Era
 by Super Semantics — supersemantics.org
"""


@click.group()
@click.version_option(version="0.4.0", prog_name="x-verba")
def main():
    """
    X-Verba — Find the governance gaps in your AI code before your users do.

    AI writes code. AI runs code. X-Verba governs it.

    Five modes:

    \b
      scan      Scan any repo → governance scorecard + report
      qa        Check code against a baseline → governance regression report
      forensics [coming soon] Reverse engineer failures → DC decomposition
      prompt    [coming soon] Generate governed prompt for AI coding tools
      compile   [coming soon] Compile approved schema → executable bundle
    """
    pass


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--format", "output_format",
    type=click.Choice(["text", "json", "yaml", "md"], case_sensitive=False),
    default="text",
    help="Output format. text = governance scorecard, json = full results, yaml/md = governance contract",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file path. Default: .verba/governance-report.txt (or .json)",
)
@click.option(
    "--identity-key", "-k",
    type=str,
    default=None,
    help="Identity Key for this system. Scopes governance events across the full lifecycle.",
)
@click.option(
    "--context-profile", "-p",
    type=click.Choice(["ai-app", "system-utility", "general"], case_sensitive=False),
    default="ai-app",
    help=(
        "Context profile. "
        "ai-app = AI-adjacent only (default). "
        "system-utility = suppress file op false positives. "
        "general = scan everything."
    ),
)
@click.option(
    "--strict-ai-only",
    is_flag=True,
    default=False,
    help="Exit code 1 if no AI integrations found. Use in CI on repos that must use AI.",
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    default=False,
    help="Show detailed scan progress and skipped files.",
)
@click.option(
    "--save-baseline",
    is_flag=True,
    default=False,
    help=(
        "Save this scan as the governance baseline (.verba/governance-baseline.json) "
        "for future 'x-verba scan --compare' runs."
    ),
)
@click.option(
    "--compare",
    "compare_path",
    type=click.Path(),
    default=None,
    help=(
        "Compare this scan against a governance baseline JSON file and report "
        "regressions. Typical usage: --compare .verba/governance-baseline.json"
    ),
)
@click.option(
    "--focus",
    "focus_paths",
    multiple=True,
    type=click.Path(),
    default=None,
    help=(
        "Restrict scan to files under these paths (repeatable). "
        "Use for large monorepos to scan only entry point directories. "
        "Example: --focus backend/api/routes/ --focus backend/workers/"
    ),
)
def scan(
    path, output_format, output, identity_key, context_profile, strict_ai_only,
    verbose, save_baseline, compare_path, focus_paths,
):
    """
    Scan any repo and generate a governance scorecard.

    PATH is the directory to scan. Defaults to current directory.

    \b
    Supported languages (MVP1):
      Python, JavaScript/TypeScript (inc. React/JSX/TSX), Go, Rust, C#

    What this does:

    \b
      1. Reads your code — finds every AI call, decision point,
         and existing constraint (AST for Python, pattern for JS/TS/Go/Rust/C#)
      2. Maps findings to the VERBA governance taxonomy
      3. Builds agent/decision graphs and runs PageRank + critical-path analysis
      4. Computes governance metrics: coverage, tendency, gamma variants
      5. Identifies governance gaps and drift class detections

    Context profiles control what gets flagged:

    \b
      ai-app        — only flag issues in AI-integrated files (default)
      system-utility — suppress file op false positives for tools/compilers
      general        — flag everything regardless of AI presence

    Examples:

    \b
      x-verba scan .
      x-verba scan ./my-repo --format json
      x-verba scan ./my-repo --context-profile general
      x-verba scan ./my-repo --strict-ai-only
      x-verba scan ./my-repo --identity-key my-system-v1.0
      x-verba scan ./my-repo -o report.txt
      x-verba scan . --save-baseline
      x-verba scan . --compare .verba/governance-baseline.json
      x-verba scan . --compare .verba/governance-history/scan-001.json
    """
    from .engine import ScanEngine, OutputFormatter

    console.print()
    subtitle = f"Governance scorecard  |  profile: {context_profile}"
    if focus_paths:
        subtitle += f"  |  focus: {', '.join(focus_paths)}"
    console.print(Panel(
        Text("X-Verba Scan", style="bold"),
        subtitle=subtitle,
        border_style="dim",
    ))
    console.print()

    engine = ScanEngine(verbose=verbose, context_profile=context_profile)
    results = engine.scan(path, identity_key=identity_key, focus_paths=list(focus_paths) if focus_paths else None)

    if strict_ai_only and results.get("summary", {}).get("ai_integrations_detected", 0) == 0:
        console.print(
            "[bold red]--strict-ai-only: No AI integrations detected. "
            "Expected AI usage in this repo.[/bold red]"
        )
        raise SystemExit(1)

    if output_format in ("yaml", "md"):
        from .writer import OutputWriter
        writer = OutputWriter(results, output_format)
        output_path = writer.write(output or None)
        _print_terminal_summary(results, output_path)
    else:
        formatter = OutputFormatter()
        report = formatter.format_report(results, fmt=output_format)

        output_path = output
        if not output_path:
            ext = "json" if output_format == "json" else "txt"
            verba_dir = Path(path) / ".verba"
            verba_dir.mkdir(parents=True, exist_ok=True)
            output_path = str(verba_dir / f"governance-report.{ext}")

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(report, encoding="utf-8")

        _print_terminal_summary(results, output_path)

    if save_baseline:
        from .baseline import BaselineStore
        store = BaselineStore(Path(path))
        baseline_file = store.save(results)
        store.archive(results)
        console.print(f"[dim]Baseline saved:[/dim] {baseline_file}")
        console.print()

    if compare_path is not None:
        from .baseline import BaselineStore, BaselineNotFoundError
        from qa_engine import GovernanceVerificationEngine
        from .writer import OutputWriter
        store = BaselineStore(Path(path))
        target = Path(compare_path) if compare_path else None
        try:
            baseline = store.load(target)
        except BaselineNotFoundError as e:
            console.print(f"[bold red]Error:[/bold red] {e}")
            raise SystemExit(1)
        current = formatter.format_report(results, fmt="json")
        import json as _json
        current_dict = _json.loads(current)
        verification = GovernanceVerificationEngine().compare(baseline, current_dict)
        verification_dict = verification.to_dict()
        verif_fmt = "json" if output_format == "json" else "yaml"
        verif_writer = OutputWriter(verification_dict, verif_fmt)
        verif_path = verif_writer.write_verification(verification_dict)
        _print_verification_summary(verification_dict, verif_path)
        if not verification.passed:
            raise SystemExit(1)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--schema", "-s",
    type=click.Path(exists=True),
    required=True,
    help="Path to the approved governance schema (YAML or JSON)",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the regression report",
)
@click.option(
    "--fail-on-critical",
    is_flag=True,
    default=True,
    help="Exit with non-zero status if critical governance regressions found (default: true)",
)
def qa(path, schema, output_format, fail_on_critical):
    """
    Check code against an approved governance baseline.

    Scans PATH and compares it against the governance baseline at SCHEMA
    (a .verba/governance-baseline.json file saved by 'x-verba scan --save-baseline').
    Flags every governance regression — new ungated AI calls, missing Pre-Nodes,
    removed Invariants — before they ship.

    Equivalent to: x-verba scan PATH --compare SCHEMA

    Designed to run in CI/CD pipelines on every commit.

    Examples:

    \b
      x-verba qa . --schema .verba/governance-baseline.json
      x-verba qa . --schema .verba/governance-baseline.json --format json
    """
    import json as _json
    from .engine import ScanEngine, OutputFormatter
    from qa_engine import GovernanceVerificationEngine
    from .writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba QA", style="bold"),
        subtitle="Governance regression check",
        border_style="dim",
    ))
    console.print()

    scan_results = ScanEngine().scan(path)
    current = OutputFormatter._json_safe(scan_results)

    with open(schema, encoding="utf-8") as f:
        if schema.lower().endswith((".yaml", ".yml")):
            import yaml as _yaml
            baseline = _yaml.safe_load(f)
        else:
            baseline = _json.load(f)

    verification = GovernanceVerificationEngine().compare(baseline, current)
    verification_dict = verification.to_dict()

    writer = OutputWriter(verification_dict, output_format)
    output_path = writer.write_verification(verification_dict)
    _print_qa_summary(verification_dict, output_path)

    if fail_on_critical and verification_dict.get("has_critical_regressions"):
        raise SystemExit(1)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--identity-key", "-k",
    type=str,
    default=None,
    help="Identity Key to trace across the full governance chain",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the forensic report",
)
def forensics(path, identity_key, output_format):
    """
    [coming v0.2] Reverse engineer governance failures — DC decomposition.

    Examples:

    \b
      x-verba forensics ./legacy-repo
      x-verba forensics ./repo --identity-key my-system-v1.0
    """
    from forensics_engine import ForensicsEngine
    from .writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Forensics", style="bold"),
        subtitle="Reverse engineering governance failures",
        border_style="dim",
    ))
    console.print()

    engine = ForensicsEngine()
    results = engine.analyse(path, identity_key=identity_key)

    if results.get("status") == "not_implemented":
        return

    writer = OutputWriter(results, output_format)
    output_path = writer.write(None)
    _print_forensics_summary(results, output_path)


@main.command()
@click.option(
    "--description", "-d",
    type=str,
    default=None,
    help="Plain language description of what you want to build",
)
@click.option(
    "--from-repo",
    type=click.Path(exists=True),
    default=None,
    help="Infer governance requirements from an existing partial codebase",
)
@click.option(
    "--domain",
    type=click.Choice([
        "healthcare", "finance", "legal", "infrastructure",
        "education", "ecommerce", "general",
    ], case_sensitive=False),
    default="general",
    help="Domain context for governance requirement inference",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["txt", "md", "json"], case_sensitive=False),
    default="md",
    help="Output format for the governed prompt",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file. Default: .verba/governed-prompt.[format]",
)
def prompt(description, from_repo, domain, output_format, output):
    """
    [coming v0.2] Generate a governance-informed prompt for AI coding tools.

    Examples:

    \b
      x-verba prompt -d "patient triage API using GPT-4" --domain healthcare
      x-verba prompt --from-repo ./partial-codebase --domain finance
    """
    from prompt_engine import PromptEngine

    console.print()
    console.print(Panel(
        Text("X-Verba Prompt", style="bold"),
        subtitle="Generating governance-informed prompt",
        border_style="dim",
    ))
    console.print()

    if not description and not from_repo:
        console.print("[red]Error:[/red] Provide either --description or --from-repo")
        raise SystemExit(1)

    engine = PromptEngine()
    results = engine.generate(
        description=description,
        from_repo=from_repo,
        domain=domain,
    )


@main.command()
@click.argument("schema", type=click.Path(exists=True))
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output path for compiled bundle. Default: .verba/bundle.vsl",
)
@click.option(
    "--validate-only",
    is_flag=True,
    default=False,
    help="Validate the schema without compiling",
)
def compile(schema, output, validate_only):
    """
    [coming v0.2] Compile an approved governance schema into an executable bundle.

    Examples:

    \b
      x-verba compile .verba/governance.yaml
      x-verba compile .verba/governance.yaml --validate-only
    """
    from compile_engine import CompileEngine

    console.print()
    console.print(Panel(
        Text("X-Verba Compile", style="bold"),
        subtitle="Compiling governance schema to executable bundle",
        border_style="dim",
    ))
    console.print()

    engine = CompileEngine()

    if validate_only:
        results = engine.validate(schema)
        _print_validation_summary(results)
    else:
        results = engine.compile(schema, output)
        _print_compile_summary(results)


# ── Terminal output helpers ───────────────────────────────────────────────────

def _tendency_explanation(tendency: dict) -> str:
    """One-sentence explanation of what is driving the tendency state."""
    state = tendency.get("state", "")
    if state == "stable":
        return ""
    reasons = []
    if tendency.get("critical_ungoverned_ratio", 0) > 0.3:
        reasons.append("ungoverned critical decisions")
    if tendency.get("t_amplification_active"):
        reasons.append("T-Amplification active on high-centrality decisions")
    if tendency.get("ungoverned_decision_density", 0) > 0.5:
        reasons.append("high ungoverned decision density")
    if not reasons:
        reasons.append("weak Pre-Node coverage across decision points")
    return f"Tendency driven primarily by: {', '.join(reasons)}."


def _print_terminal_summary(results, output_path):
    """Print clean terminal summary of scan results."""
    console.print()

    stats = results.get("summary", {})
    status = stats.get("governance_status", "")
    files = stats.get("files_scanned", 0)
    ai_count = stats.get("ai_integrations_detected", 0)
    profile = stats.get("context_profile", "ai-app")
    decision_pts = stats.get("decision_points_detected", 0)

    if status == "NO_AI_INTEGRATIONS":
        console.print(f"[dim]Files scanned:[/dim] {files}")
        console.print(f"[dim]Context profile:[/dim] {profile}")
        console.print()
        console.print("[yellow]No AI integrations detected.[/yellow]")
        console.print(f"[dim]{stats.get('note', '')}[/dim]")
        console.print()
        console.print(f"[dim]Report:[/dim] {output_path}")
        console.print()
        return

    lang_cov = stats.get("language_coverage", {})
    lang_frac = lang_cov.get("decision_analysed_fraction", 0)
    gamma = stats.get("gamma_variants", {}).get("overall", {})
    gamma_val = gamma.get("value")
    gamma_status = gamma.get("status", "")
    tendency = stats.get("tendency", {})
    tendency_state = tendency.get("state", "unknown")

    critical = stats.get("critical", 0)
    high = stats.get("high", 0)
    medium = stats.get("medium", 0)

    console.print(f"[dim]Files scanned:[/dim]          {files}")
    console.print(f"[dim]AI integrations:[/dim]        {ai_count}")
    console.print(f"[dim]Candidate Gov. Nodes:[/dim]   {ai_count}  [dim](X-Verba inferences — confirm in contract)[/dim]")
    console.print(f"[dim]Decision points:[/dim]        {decision_pts}")
    console.print(f"[dim]Context profile:[/dim]        {profile}")
    console.print(f"[dim]Language coverage:[/dim]      {lang_frac:.0%}")
    gamma_str = f"{gamma_val:.4f}" if gamma_val is not None else "N/A"
    console.print(f"[dim]Structural Gamma:[/dim]       {gamma_str}  [dim]({gamma_status})[/dim]")
    if gamma_val is not None:
        gamma_pct = int(round(gamma_val * 100))
        console.print(f"[dim]  {gamma_pct}% of governance-relevant decision points have an observable governance checkpoint.[/dim]")

    if tendency_state == "failure":
        console.print(f"[bold red]Tendency:[/bold red]               {tendency_state.upper()}")
    elif tendency_state == "stable":
        console.print(f"[green]Tendency:[/green]               {tendency_state.upper()}")
    else:
        console.print(f"[dim]Tendency:[/dim]               {tendency_state.upper()}")
    tendency_reason = _tendency_explanation(tendency)
    if tendency_reason:
        console.print(f"[dim]  {tendency_reason}[/dim]")
    console.print()

    if critical > 0:
        console.print(
            f"[bold red]CRITICAL: {critical}[/bold red]  "
            f"[yellow]HIGH: {high}[/yellow]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )
    elif high > 0:
        console.print(
            f"[green]No critical findings[/green]  "
            f"[yellow]HIGH: {high}[/yellow]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )
    else:
        console.print(
            f"[green]No critical or high findings[/green]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )
    console.print()

    # R1 + R5: show DC-I11 aggregate in a separate structural/informational section
    dc_i11 = stats.get("dc_i11_aggregate")
    if dc_i11:
        count = dc_i11.get("aggregate_count", 0)
        rep = dc_i11.get("aggregate_locations", [])
        console.print("[bold]Structural findings[/bold] [dim](informational)[/dim]")
        console.print(
            f"  [yellow]~[/yellow]  DC-I11 Evaluative Decoupling — "
            f"[dim]{count} AI call {'site' if count == 1 else 'sites'} without a governance checkpoint.[/dim]"
        )
        console.print(
            "[dim]     Implement a governance layer at API entry points, "
            "not per-call-site.[/dim]"
        )
        if rep:
            console.print(f"[dim]     Examples: {', '.join(rep[:3])}"
                          + (f" (+{count - 3} more)" if count > 3 else "") + "[/dim]")
        console.print()

    top = stats.get("top_decisions", {}).get("most_influential", [])[:3]
    if top:
        console.print("[bold]Top influential decisions:[/bold]")
        for loc, score in top:
            console.print(f"  [yellow]>[/yellow]  {loc}  [dim](PageRank: {score:.6f})[/dim]")
        console.print()

    console.print(f"[dim]Report:[/dim] {output_path}")
    console.print()


def _print_verification_summary(verification, output_path):
    """Print a governance verification summary (for --compare and qa)."""
    status = verification.get("overall_status", "UNKNOWN")
    regressions = verification.get("regressions", [])
    improvements = verification.get("improvements", [])

    color_map = {"IMPROVED": "green", "STABLE": "dim", "REGRESSED": "bold red"}
    color = color_map.get(status, "dim")
    console.print(f"[{color}]Governance verification: {status}[/{color}]")
    console.print()

    if regressions:
        console.print(f"[bold red]Regressions: {len(regressions)}[/bold red]")
        for r in regressions[:5]:
            console.print(f"  [red]x[/red]  {r.get('metric', '')}")
            console.print(f"     {r.get('description', '')}")
        console.print()

    if improvements:
        console.print(f"[green]Improvements: {len(improvements)}[/green]")
        for d in improvements[:5]:
            console.print(f"  [green]v[/green]  {d.get('metric', '')}: {d.get('description', '')}")
        console.print()

    if not regressions and not improvements:
        console.print("[dim]No governance changes detected.[/dim]")
        console.print()

    console.print(f"[dim]Verification report:[/dim] {output_path}")
    console.print()


def _print_qa_summary(results, output_path):
    """Print QA regression summary."""
    regressions = results.get("regressions", [])
    critical = [r for r in regressions if r.get("severity") == "critical"]
    high = [r for r in regressions if r.get("severity") == "high"]

    if not regressions:
        console.print("[green]Governance check passed.[/green]")
        console.print("[dim]No governance regressions detected.[/dim]")
    else:
        console.print(
            f"[bold red]Governance regressions detected: {len(regressions)}[/bold red]"
        )
        console.print(
            f"[red]Critical: {len(critical)}[/red]  "
            f"[yellow]High: {len(high)}[/yellow]"
        )
        console.print()
        for r in critical[:3]:
            console.print(f"  [red]✗[/red]  {r.get('location', 'unknown')}")
            console.print(f"     {r.get('description', '')}")
            console.print()

    console.print(f"[dim]Full report:[/dim] {output_path}")
    console.print()


def _print_forensics_summary(results, output_path):
    """Print forensics decomposition summary."""
    dc_classes = results.get("dc_classes_detected", [])
    gamma = results.get("structural_gamma", {})

    console.print(f"[dim]Drift Classes detected:[/dim] {len(dc_classes)}")
    console.print(
        f"[dim]Structural Gamma proxy:[/dim] "
        f"{gamma.get('proxy_value', 'N/A')}"
    )
    console.print()

    if dc_classes:
        console.print("[bold]DC decomposition:[/bold]")
        for dc in dc_classes[:5]:
            console.print(
                f"  {dc.get('code', '')}  {dc.get('name', '')}  "
                f"[dim]Tier {dc.get('tier', '?')}[/dim]"
            )
            console.print(f"     {dc.get('plain_english', '')[:80]}")
            so = dc.get("primary_so", "")
            if so:
                console.print(f"     [dim]→ Recommended: {so}[/dim]")
            console.print()

    console.print(f"[dim]Full forensic report:[/dim] {output_path}")
    console.print()


def _print_validation_summary(results):
    valid = results.get("valid", False)
    issues = results.get("issues", [])

    if valid:
        console.print("[green]Schema validation passed.[/green]")
        console.print("[dim]Schema is complete and ready to compile.[/dim]")
    else:
        console.print(
            f"[bold red]Schema validation failed: {len(issues)} issues[/bold red]"
        )
        for issue in issues[:5]:
            console.print(f"  [red]✗[/red]  {issue}")
    console.print()


def _print_compile_summary(results):
    success = results.get("success", False)
    output_path = results.get("output_path", "")
    version = results.get("version_hash", "")

    if success:
        console.print("[green]Compilation successful.[/green]")
        console.print(f"[dim]Bundle:[/dim] {output_path}")
        console.print(f"[dim]Version:[/dim] {version}")
        console.print("\n[dim]Deploy this bundle with the VERBA Runtime.[/dim]")
        console.print("[dim]The Priming Engine will load it and begin monitoring.[/dim]")
    else:
        console.print("[bold red]Compilation failed.[/bold red]")
        for error in results.get("errors", [])[:5]:
            console.print(f"  [red]✗[/red]  {error}")
    console.print()


if __name__ == "__main__":
    main()



