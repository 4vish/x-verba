# Changelog

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
