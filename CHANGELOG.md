# Changelog

## Unreleased

Multi-agent handover detection — family 8 (team registry + publish/
subscribe messaging). The first family whose handover signature spans
*multiple files* — every confirmed real example splits the publish half
and the subscribe half across separate files, so this runs as a
repo-wide pass (`_detect_pubsub_messaging`), not a per-file detector like
every other family.

### Added

- **MetaGPT (Python)** — `Environment.publish_message(message)` (a
  distribution method) paired with `Role._watch(actions)` /
  `Role.set_addresses(addresses)` (per-agent subscription filters),
  confirmed split across 3 files (`team.py`, `environment/base_env.py`,
  `roles/role.py`). Re-scan after fix: 0 → 2 agents / 1 handover.
- **open-agent-sdk-typescript (JS/TS)** — a `TeamCreateTool`/
  `SendMessageTool` tool-definition pair, identified by their literal
  `name: 'TeamCreate'`/`name: 'SendMessage'` values, confirmed split
  across 2 files (`team-tools.ts`, `send-message.ts`). Re-scan after fix:
  3 → 5 agents / 2 → 3 handovers (additive on top of family 7, already
  detected in the same repo).

No regressions — AI-integration counts unchanged across a 10-repo
regression sweep; no false positives on repos without this pattern.

---

Multi-agent handover detection — family 4 (protocol/server). The first
family with no in-process call chain at all — a client object calling a
remotely, independently-deployed agent/workflow over a network boundary.

### Added

- **AP2's `*Client(name=..., base_url=...)` shape** — any constructor
  ending in `Client` carrying both a `name=` and a `base_url=` keyword.
  Re-scan after fix, AP2's real `remote_agents.py`:
  `credentials_provider_client` → `credentials_provider`,
  `merchant_agent_client` → `merchant_agent`. Full-app re-scan: 0 → 12
  agents / 9 handovers (family 2's `sub_agents=[...]` and family 4's
  remote clients co-occurring in the same app, exactly as documented
  during evidence-gathering).
- **llama_deploy's `.run_workflow(workflow_name, ...)` shape** — a
  bespoke REST protocol, not A2A, confirming this family is a genuine
  architectural pattern independent of any specific wire protocol.

No regressions — AI-integration counts unchanged across an 11-repo
regression sweep.

---

Multi-agent handover detection — families 3 and 7 (recursive
self-delegation, and named subagent registry). Grouped together since
family 7 is family 3's static-declaration cousin: a predefined registry
of subagents vs. a dynamically depth-tracked spawn tree.

### Added

- **Family 3 — recursive self-delegation.** A tool function (literally
  named `delegate_task`/`delegate_agent`/`spawn_agent`/`spawn_subagent`)
  that recursively spawns a child instance of the same agent. Requires a
  depth-cap signal (`max_spawn_depth`/`MAX_DEPTH`/`max_depth`/
  `child_depth`) present somewhere in the file to corroborate — the depth
  cap, not the call name alone, is this family's structural signature, so
  a function that happens to share one of these names without any
  depth-tracking nearby is not matched. Re-scan after fix, Hermes's real
  `tools/delegate_tool.py`: 0 → 2 agents / 1 handover (correctly matching
  the tool's own self-referential registration,
  `handler=lambda args, **kw: delegate_task(...)`).
- **Family 7 — named subagent registry**, in both languages. Python:
  `ClaudeAgentOptions(agents={"code-reviewer": AgentDefinition(...)})` —
  a dict keyed by name, distinguished from family 2's same-named
  `agents=` keyword by value type (family 2 requires a List, this
  requires a Dict). Re-scan after fix, the real Claude Agent SDK
  `examples/agents.py`: 0 → 5 agents / 4 handovers. JS/TS: `const
  BUILTIN_AGENTS: Record<string, AgentDefinition> = { Explore: {...},
  Plan: {...} }` — uses proper brace-balance matching
  (`_js_balanced_brace_span`), not a character window, since an early
  draft of this detector spilled past the object's closing brace into
  unrelated code in the same file and produced false positives (caught
  before landing). Re-scan after fix, the real
  `open-agent-sdk-typescript/src/tools/agent-tool.ts`: 0 → 3 agents / 2
  handovers.

No regressions — AI-integration counts unchanged across a 10-repo
regression sweep spanning both languages.

---

Multi-agent handover detection — family 5 (agent-as-tool). A sub-agent
wrapped inside a tool definition, handed to a supervisor — the handover
is invisible at the supervisor's declaration site, only visible by
tracing into the tool's body. Three independent wrapping syntaxes, all
detected:

### Added

- **OpenAI Agents SDK's built-in method** — `Agent(tools=[spanish_agent
  .as_tool(tool_name=..., tool_description=...), ...])`. Re-scan after
  fix, the real `agents_as_tools.py` example: 0 → 3 agents / 3 handovers
  (`orchestrator_agent` → `spanish_agent`/`french_agent`/`italian_agent`).
- **Pydantic AI's decorator form** — `@triage_agent.tool` applied to a
  function whose body calls a *different* agent's `.run(`/`.invoke(`.
  Re-scan after fix, the real `medical_agent_delegation.py` example:
  `triage_agent` → `specialist_agent`/`senior_doctor_agent`.
- **LangChain.js's manual-wrap form, and the engine's first JS/TS
  handover detection** (previously Python-AST-only) — `const
  scheduleEvent = tool(async (...) => { await calendarAgent.invoke(...)
  }, {...})` then `createAgent({ tools: [scheduleEvent] })`. Pattern-based
  (windowed character-distance matching, not balanced-brace parsing,
  consistent with how JS/TS detection works elsewhere in this engine).
  Re-scan after fix, the real `subagents-personal-assistant.ts` example:
  0 → 2 agents / 2 handovers; a 3rd, correctly generalised find on
  `router-knowledge-base.ts` in the same directory — a compiled
  `workflow` object (not literally named "...Agent") wrapped as a tool
  the same way, picked up by the same `.invoke(` pattern match.

No regressions — AI-integration counts unchanged across the full
regression sweep (8 repos spanning both languages).

## 0.4.7

Multi-agent handover detection — family 6 (constructor-keyword handoff
list). Reuses the same AST shape as family 2's list-composition (a
constructor keyword whose value is a list) since `handoffs=` is
structurally identical, just a different semantic label — no new
detection mechanism needed, only a new keyword and one extra method for
the post-construction mutation form.

### Added

- **`Agent(handoffs=[...])`, both confirmed sub-variants.** OpenAI Agents
  SDK's wrapper-object form — `handoffs=[handoff(agent=faq_agent,
  on_handoff=..., tool_name_override=...), ...]` — and Swarms' flat-list
  form — `handoffs=[agent1, agent2]` (no wrapper call). `_literal_or_name`
  now resolves an `agent=` keyword on an inline call, recursively, to
  find the real target through the `handoff(...)` wrapper.
- **`faq_agent.handoffs.append(handoff(agent=triage_agent, ...))`** — the
  post-construction mutation form, detected as a separate pattern (an
  `.append()` call on a `.handoffs` attribute).
- Re-scan after fix, `openai-agents-python`'s real customer-service
  example: 0 → 3 agents / 4 handovers (all 4 edges of the
  triage/faq/seat-booking graph, including both directions of the
  `.handoffs.append()` mutations).

### Known limitation (not fixed in this release)

- `on_handoff=` presence/absence at a given edge is a documented
  governance-relevant signal (a real callback that runs before/during the
  handoff) but isn't yet recognised as a Pre-Node by `_assess_pre_node_strength`
  — all family 6 handovers currently report as ungoverned regardless of
  whether `on_handoff=` is present. Confirmed on the same
  `openai-agents-python` example (the `seat_booking_agent` handoff has
  `on_handoff=on_seat_booking_handoff` but still reports ungoverned).
  Scheduled as a follow-up refinement, not a detection gap.

## 0.4.6

Multi-agent handover detection — families 1 and 2. `agent_inventory`
(Agents Detected / Handovers / Chains / Clusters) reported 0 on every real
multi-agent repo scanned this session because `AgentHandoverAnalyser` only
recognised one shape (`agent_a.run(x)` -> variable -> `agent_b.run(var)`,
same function body). Real frameworks build multi-agent systems two other
ways just as commonly: declaring a graph of edges, or passing a flat list
of agents into a constructor. Both are now detected, verified empirically
by re-scanning real repos before/after.

### Added

- **Family 1 — graph/builder edges.** Detects
  `StateGraph().add_node(...).add_edge(a, b)` (LangGraph),
  `WorkflowBuilder().add_edge(a, b)` (Microsoft Agent Framework),
  `pipeline.connect(sender, receiver)` (Haystack), and `DiGraphBuilder`
  (AutoGen) — both the fluent-chained form and the assign-then-call form
  (`workflow = StateGraph(...); workflow.add_edge(a, b)`). Each `add_edge`/
  `connect` call becomes a handover edge between the two node labels.
  Re-scan after fix: `TradingAgents` (a real LangGraph trading-debate
  pipeline) 0 → 12 agents / 7 handovers / 4 chains / 5 clusters;
  `azure-trust-agents` (Microsoft Agent Framework) 0 → 4 agents / 12
  handovers.
- **Family 2 — list-composition.** Detects `agents=[...]` (CrewAI),
  `participants=[...]` (AutoGen), `sub_agents=[...]` (Google ADK),
  `members=[...]` (Semantic Kernel, OpenClaw's own team model) — any
  constructor keyword from this set whose value is a list, including one
  level of same-file variable indirection (`agent_list = [a, b];
  Crew(agents=agent_list)`). Re-scan after fix: a Google ADK sample
  (`root_agent = Agent(sub_agents=[weather_agent])`) 0 → 2 agents / 1
  handover; `ClawTeam-OpenClaw`'s own team model (`TeamConfig(members=
  [leader])`) 0 → 2 agents / 1 handover.

### Fixed — file-walker

- **`SKIP_FILENAMES` (setup.py, conftest.py, setup.cfg) matched by bare
  filename anywhere in the tree, not just at the repo root.** A module
  that happens to share one of these names deeper in the tree — e.g.
  `tradingagents/graph/setup.py`, the actual LangGraph workflow
  construction file, the single most relevant file in that repo for this
  exact feature — was being skipped as if it were build tooling. Now only
  applied to files at the scanned repo's own root.

### Known limitations (not fixed in this release)

- List-composition detection does not trace a constructor keyword's value
  through a function call — `agents, handoffs = get_agents()` followed by
  `HandoffOrchestration(members=agents, ...)` is not detected, since the
  actual list literal lives inside `get_agents()`'s return statement, one
  function away. Same limitation class as the dict-unpacking case below.
  Confirmed on Semantic Kernel's own `step4_handoff.py` example.
- Constructor keywords built via `**kwargs` dict-unpacking are not
  detected — `Crew(*args, **crew_params)` where `crew_params["agents"]`
  is assigned earlier gives no literal `agents=` keyword in the AST for
  this detector to see. Confirmed on `CrewAI-Studio`'s real `my_crew.py`.
  Both of these would need interprocedural/dataflow tracing, a
  meaningfully larger feature than this release's scope.
- JS/TS support, family 1's `add_conditional_edges` variant and Mastra's
  `.step()`/`.then()` chain form, families 3-9, and the IaC-declared
  variant (AWS Bedrock Agents' `agent_collaborators=` in a CDK stack) are
  not yet implemented — scheduled for follow-up releases per the
  implementation order in `.claude/skills/agent-handover-detection`.

## 0.4.5

File-walker fixes. All four were found by reading `_collect_files()` and
its supporting constants against real repos, then verified empirically by
re-scanning before/after each change.

### Fixed

- **`.test-d.ts` (vitest/tsd type-testing convention) wasn't recognised as
  a test file.** `TEST_FILE_RE` required a literal `.` immediately after
  `test`/`spec`, so `.test.ts` matched but `.test-d.ts` (hyphen instead of
  dot) did not. On a real scan (`vercel/ai`), **126 of 128 candidate
  governance nodes (98.4%) traced back to a single type-test file** with
  no real application logic — the scan's entire headline result (128
  critical findings, Gamma 0.08) was almost completely noise from this one
  misclassification. Likely the highest-impact single bug fixed across
  this round of work.
- **`--focus` resolved relative paths against the CLI process's working
  directory, not the scanned repository.** `--focus packages/core/src`
  silently returned 0 files scanned unless run from inside the target
  repo. Now resolved relative to the repo path being scanned.
- **`SKIP_DIRS` pruned directories named `examples`/`samples`/`docs`/etc.
  even when an explicit `--focus` target lived inside one of them** —
  `--focus examples/src/multi-agent` returned 0 files even with the path
  bug above fixed, because the walker pruned `examples/` before the focus
  filter ever ran. Now a normally-skipped directory is still walked into
  if it's required to reach an explicit focus target (the target itself,
  or one of its ancestors); once inside the focus subtree, normal
  skip-dir rules resume as expected. Re-scan after both `--focus` fixes
  (`langchainjs`, `--focus examples/src/multi-agent`): 0 → 5 files.
- **No exclusion for minified/bundled JS shipped inside a source tree.**
  A CLI tool's own bundled web UI (a 4,210-line minified Angular build
  artifact) was scanned as real source and showed up in the scan's top
  influential decisions by PageRank — pure noise from a vendored,
  built artifact. Added a filename heuristic for `*.min.js` and
  webpack/esbuild-style content-hashed chunk filenames
  (`main-3CUQG2IN.js`, `chunk-NALL4A3P.js`). Confirmed via re-scan
  (`google/adk-python`): the bundle no longer appears anywhere in the
  contract.

## 0.4.4

### Added — governance theatre detection

- New detector for a specific TS/JS anti-pattern: an agent-action
  framework's `validate()` function that unconditionally returns `true`
  regardless of its input (a bare `=> true` arrow, or a body whose
  parameters are all underscore-prefixed/unused) — present and callable,
  but never actually checking anything. Scoped to require a corroborating
  agent-action-framework signal (`handler:`, `iagentruntime`,
  `@elizaos/core`, `similes:`) in the same file, so it doesn't fire on
  unrelated `validate()` functions elsewhere in a codebase. Confirmed on
  elizaOS-pattern plugins (49 findings on a real plugin set during
  development); 0 false positives confirmed on every non-agent-framework
  TS/JS repo scanned this session.

### AI-provider detection

AI-provider detection release. Scanned 35+ real repositories across every
major current agent framework/SDK (LangChain v1, OpenAI Agents SDK, Google
ADK, Anthropic's Claude Agent SDK in both Python and JS/TS, AWS Strands,
AWS's JS Bedrock SDK, LlamaIndex's agent/workflow submodule, Agency Swarm)
and found the same class of bug nine times: each framework's own current
top-level import was simply absent from the provider-detection tables,
causing affected scans to report **zero AI integrations** — not a missing
inventory section, the entire scan finding nothing to evaluate. Every fix
below was verified empirically by re-scanning the real repository
before/after the change.

### Fixed — AI-provider import detection (9 confirmed gaps)

- **Modern LangChain (v1.x)** — `langchain.chat_models` (the new
  provider-agnostic `init_chat_model` factory) and `langchain.agents` (the
  new unified `create_agent` constructor) were missing; only the legacy
  `langchain_openai`/`AgentExecutor` surface was recognised. Confirmed
  100% false negative on `chat-langchain`, a real production RAG agent.
  Re-scan after fix: 0 → 7 AI integrations.
- **OpenAI Agents SDK** — its package is literally named `agents`, too
  generic to safelist outright (would false-positive on any unrelated
  local module of the same name). Added as a *guarded* import: only
  recognised when the file also contains `Agent(`, `Runner.run(`, or
  `handoff(` — the same precaution already used for generic method names.
  Re-scan after fix: 0 → 8 AI integrations.
- **Google ADK and the newer `google.genai` SDK** — distinct from
  `google.generativeai`, which was already recognised. Confirmed on a
  real multi-agent payments app (Google's AP2). Re-scan after fix
  (bypassing an unrelated pre-existing `SKIP_DIRS` bug that excludes any
  `samples/` directory — see Known Issues): 0 → 15 AI integrations.
- **Anthropic's Claude Agent SDK — Python and JS/TS, two separate fixes.**
  The Python package is `claude_agent_sdk`; the JS/TS package is the
  differently-named `@anthropic-ai/claude-agent-sdk`. Both were missing —
  fixing one does not fix the other, even for the same vendor's own SDK.
  Re-scan after fix: SDK examples 0 → 102; a real desktop app built on the
  JS/TS package, 0 → 6.
- **AWS Strands Agents** (`strands` package) — distinct from
  `bedrock_agentcore` (a separate AWS runtime/deployment SDK, already
  recognised via `boto3`). Confirmed on a real Bedrock chat app where the
  actual agent-construction file was invisible despite the app's overall
  AI-integration count looking nonzero (from unrelated `boto3` calls
  elsewhere) — a reminder that a nonzero count can still hide a 100% miss
  on the framework that actually matters. Re-scan after fix: the specific
  file now appears in the contract.
- **AWS SDK for JavaScript v3's Bedrock clients** — distinct from Python's
  `boto3`, already recognised. Confirmed on a real, fully-functional
  Electron desktop app. Re-scan after fix: 0 → 34 AI integrations.
- **LlamaIndex's agent/workflow submodule** — `llama_index.llms` was
  already recognised, but `llama_index.core.agent`/`llama_index.core.workflow`
  were not; import matching is by full dotted path, not top-level package,
  so partial recognition of one submodule doesn't extend to another.
  Re-scan after fix: 1 → 61 AI integrations.
- **Agency Swarm** (`agency_swarm` package) — confirmed on a real
  multi-agent assistant app. Re-scan after fix: 15 → 90 AI integrations.

### Known issues (not fixed in this release)

- `SKIP_DIRS` unconditionally excludes `examples/` and `samples/` (among
  others), even when those directories contain the only relevant source
  in a repo, and even when explicitly passed via `--focus`. Confirmed on
  `langchainjs` and `google-agentic-commerce/AP2`. Scheduled for a
  follow-up release alongside the other file-walker bugs (`--focus`
  cwd-resolution, no minified-bundle exclusion, `.test-d.ts` not matching
  the test-file regex).
- Raw-HTTP AI-provider calls (no SDK import, no distinctive method name —
  just a provider hostname inside a generic `fetch`/`httpx`/custom-wrapper
  call) remain undetected. Confirmed on 3 independent codebases, including
  20 provider files in a single repo (`promptfoo`). Needs a different
  detection strategy (hostname/path matching) and is scheduled separately.
- Multi-agent handover detection (`agent_inventory` reporting 0 agents/
  handovers on real multi-agent repos) is a separate, larger body of work
  — 9 confirmed handover shapes across the frameworks above, not yet
  implemented.

## 0.4.3

Detection-accuracy release. Every fix below was found by reading the engine
source against an independent audit, then verified empirically by re-scanning
real repositories (`gogcli`, `ECC`, `minGPT`, a Gemini/LangGraph quickstart)
before and after each change — not just patched and assumed correct.

### Fixed — false positives

- **`has_recovery` counted logging-only exception handlers as real recovery.**
  `except Exception as e: logger.error(e)` was reported as a genuine recovery
  path in Python, JS/TS, *and* Go (a third instance neither source audit
  caught) — meaning errors that were actually swallowed silently still
  counted as "handled." Terminal-state counts dropped 92-100% on real repos
  after this fix alone.
- **Terminal-state detection fired on files with no AI integration at all.**
  A pure utility file's exception handling was flagged the same as AI-adjacent
  code. Now scoped to AI-adjacent files only, matching the same rule already
  used for irreversible-action detection.
- **`subprocess.run`/`subprocess.call` were flagged as critical regardless of
  the actual command** — `git fetch`, `pytest`, `uv run test` were treated
  identically to `rm -rf`. Fixed to check command content — and a second bug
  was found and fixed in the same pass: the original proposed fix (and our
  first implementation of it) only matched shell-string-style commands
  (`"rm -rf /path"`), silently missing the more common Python list-style
  calls (`["rm", "-rf", "/path"]`) — which would have traded a false positive
  for a false negative on the exact case it was meant to catch.
- **`_has_dynamic_prompt()` and `_identify_provider()` flagged unrelated
  code as AI/prompt issues.** A 20-line window checked for any keyword or
  template signal anywhere in the block, with no requirement that they
  co-occur — a variable named `query_domains` 15 lines from an unrelated
  f-string could trigger a false AI-lifecycle finding. Also, generic method
  names (`.chat(`, `.query(`, `.predict(`) were matched as AI calls on *any*
  object, not just recognized AI clients — a `db.query()` call could be
  misidentified as an AI integration. Both fixed: the window now requires a
  prompt keyword and a template signal on the *same* line, and generic method
  names require a recognized AI import as the call's root object.

### Fixed — scoring accuracy

- **Gamma's denominator included every decision point detected, not just
  consequential ones** — null checks, simple loops, and ternaries with no
  downstream consequence inflated the count (and therefore the apparent
  precision) of the score. Now filtered to decision points that actually
  lead to a consequence, in both `GammaVariantsBuilder` and the sibling
  `GovernanceMetricsBuilder.compute_coverage()` (a second instance of the
  same bug, not previously identified). This changes the displayed Gamma
  value on existing scans — sometimes up, sometimes down, depending on
  whether a repo's apparent governance was concentrated in real enforcement
  or in the null-check noise being removed.
- **The Pre-Node "governed" threshold (0.5) let a guard with no hard block
  count as governed** — `if result: db.commit()` passed with no `raise` or
  `return` anywhere in the guard body, purely from scope overlap. Raised to
  0.7, and consolidated four separate hardcoded `0.5` literals (which would
  have drifted out of sync with each other) into one shared constant.
- **Gamma was displayed with up to 17 digits of floating-point noise**
  (`0.10540059347181009`) in the terminal, JSON, and YAML output. Now
  rounded to 2 decimal places at the single source all three formats read
  from, plus a separate stray `.4f` (4 decimals) in the terminal printer
  that would have stayed wrong even after the source-level fix.

### Fixed — Drift Class labeling

- **Two of the engine's highest-confidence, most-frequently-triggered DC
  labels didn't match their own canonical definitions.** "Unsanitized user
  input into an AI prompt" was labeled `DC-E5` (Dominance Forcing — coercive
  rhetorical structure, an unrelated phenomenon); corrected to `DC-E3`
  (Signal Corruption). "Dynamic prompt assembly" was labeled `DC-L2`
  (Performative Capture — DAN-style outputs that enact change); this gap has
  no reliable structural signature for any specific Drift Class, so it now
  gets none rather than a guessed label.
- **`DC-E14` (Substrate Contamination) was applied to every ungated
  irreversible action**, regardless of whether it matched the class's actual
  definition (a dormant/conditional trigger activating after deployment —
  the Knight Capital pattern). Now requires a real dormant-trigger guard;
  verified against both a positive case (fires correctly) and a negative
  case (stays silent) with a synthetic repro.
- **The cross-file/speculative proximity fallback for DC labeling was
  removed.** Previously, a gap with no same-file confirmed match would
  borrow the nearest unrelated match from anywhere else in the scan —
  producing DC labels with no real connection to the gap they were attached
  to. Most governance gaps are generic Pre-Node gaps that don't exhibit any
  specific Drift Class mechanism; leaving them unlabeled is the honest
  result, not a regression. Verified empirically: zero gaps received a
  forced label across four real repos after this change, where every one of
  them would have received some label before it.
- **Confidence levels added to structural DC findings** — previously every
  finding from `_match_dc_patterns()` displayed as undifferentiated
  "STRUCTURAL" regardless of actual confidence. High-temperature-based
  findings are now SPECULATIVE, missing-human-review aggregates are MEDIUM,
  matching the confidence vocabulary already used for Legion matches.
- **`_DC_NAME_FALLBACK` had 6 of 8 names wrong** relative to the canonical
  taxonomy (e.g. `DC-E14` labeled "Unsanctioned Dependency" instead of
  "Substrate Contamination"). Corrected; was dead code in practice (upstream
  fallback chains already resolved correct names first) but a landmine
  worth removing regardless.

### Fixed — crashes

- **`x-verba forensics`, `x-verba prompt`, and `x-verba compile` all crashed
  immediately** with `ModuleNotFoundError`, instead of showing their
  intended "not yet implemented" message — three more instances of the
  same missing-relative-import bug fixed elsewhere in `0.4.2`. Also fixed a
  related rough edge: `compile` printed a confusing "Compilation failed"
  line directly underneath its own "Not yet implemented" panel.

### Verified against

- `gogcli` (Go, no AI integrations), `ECC` (mixed JS/TS/Python, 3,251 files),
  `karpathy/minGPT`, a Gemini/LangGraph quickstart — full before/after
  comparison on every numeric fix.
- Purpose-built synthetic repros for the cases no real repo happened to
  trigger: the subprocess git-fetch-vs-rm-rf distinction, the dormant-trigger
  DC-E14 positive/negative cases, and the dynamic-prompt false-positive shape.

## 0.4.2

Bug-fix release. `x-verba qa` and `x-verba scan --compare` were both broken
in every published version up to and including `0.4.1` — neither command
could actually run.

### Fixed

- **`x-verba qa` crashed immediately** with
  `ModuleNotFoundError: No module named 'qa_engine'` — `cli.py`'s `qa`
  command imported it as `from qa_engine import ...` instead of
  `from .qa_engine import ...`. The same bug also existed in
  `scan --compare`'s import of the same module.
- **`x-verba scan --format yaml --compare ...` crashed** with
  `NameError: formatter is not defined` — the `--compare` branch reused a
  `formatter` variable that was only ever assigned when `--format` was
  `text` or `json`, never when it was `yaml` or `md`.
- **Removed the `npm install -g x-verba` line from the README** — there is
  no published npm package (`npm view x-verba` returns 404). Also corrected
  the Python version floor in the install instructions from `3.9+` to
  `3.10+`, matching `pyproject.toml`'s actual `requires-python`.

### Verified against

- `karpathy/minGPT` — `scan --save-baseline`, `scan --compare`,
  `scan --format yaml --compare`, and standalone `qa` all run end to end.

## 0.4.1

Bug-fix release. No new detection logic, no scoring changes — every fix below
is in the scan/report/packaging layer, found by running the CLI against real
public repositories rather than fixtures.

### Fixed

- **Structural Gamma was `null` on any repo with no AI integrations under the
  default `ai-app` profile.** The scanner short-circuited before Passes 3-16
  ever ran, returning `governance_status: NO_AI_INTEGRATIONS` and
  `total_decision_points: 0` even when the repo had thousands of real
  decision points. The `ai-app` profile now only filters which findings are
  flagged as AI-adjacent — it no longer skips structural analysis. A non-AI
  Go CLI tool (`gogcli`, 581 files) now correctly reports
  `structural_gamma: 0.105 (BELOW_THRESHOLD)` and 16,858 decision points
  instead of `null`/`0`.
- **`x-verba scan` never generated the governance contract by default.**
  Only the text scorecard was written unless `--format yaml` was passed
  explicitly. The contract — the actual artifact developers act on — is now
  always written alongside the scorecard.
- **The governance contract's default output path ignored the scanned
  repo's path.** `--format yaml` without `--output` wrote to
  `<current-directory>/.verba/governance.yaml` instead of
  `<scanned-repo>/.verba/governance.yaml`, silently landing files outside
  the repo being scanned.
- **The package failed to import at all** due to two broken import
  statements in `engine.py` (`from graph import ...` instead of
  `from .graph import ...`) and a casing typo (`pagerank_DAMPING` vs.
  `PAGERANK_DAMPING`).
- **`xverba.bat` crashed on every real scan** with
  `ImportError: attempted relative import with no known parent package` —
  it `cd`'d into the `x_verba` package directory and ran `python -m cli`,
  breaking the package's own relative imports. It now runs
  `py -m x_verba.cli` from the repo root, and resolves its own location via
  `%~dp0` instead of a hardcoded path, so it works regardless of where the
  repo is cloned.
- **Console output garbled or crashed on Windows** — em-dashes and
  box-drawing characters rendered as `�` (and in one case raised
  `UnicodeEncodeError`) because stdout/stderr weren't using UTF-8 on
  Windows' legacy console code page. Both streams are now reconfigured to
  UTF-8 at CLI startup.
- **Every scan printed an unattributable `SyntaxWarning: <unknown>:80`** —
  `ast.parse()` was never told which file it was parsing, so warnings about
  *the scanned repo's own* code (not x-verba's) couldn't be traced back to
  a real file. Parsing now passes the real filename through, and these
  warnings are suppressed from the terminal entirely — x-verba reports
  structural governance gaps, not third-party lint issues.

### Verified against

- `gogcli` (Go, 581 files, no AI integrations)
- `karpathy/minGPT` (Python, real model/training code)
- `affaan-m/ECC` (mixed JS/TS/Python, 3,251 files, 8,483 decision points)
