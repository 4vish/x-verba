# Changelog

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
