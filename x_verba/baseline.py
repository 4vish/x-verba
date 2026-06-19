"""
X-Verba Governance Baseline Storage

Stores and retrieves Governance Baselines under `.verba/`:

    .verba/
        governance-baseline.json       — the approved governance state
        governance-history/
            scan-001.json
            scan-002.json
            ...

The baseline is a full scan `results` dict (the same JSON produced by
`OutputFormatter.format_report(results, fmt="json")`), serialized via
`OutputFormatter._json_safe` so that `models.py` dataclasses and graph
node/edge data round-trip as plain JSON. No re-scanning happens here —
this module only persists and retrieves scan results.
"""
import json
from pathlib import Path
from typing import Optional

from .engine import OutputFormatter

BASELINE_FILENAME = "governance-baseline.json"
HISTORY_DIRNAME = "governance-history"


class BaselineNotFoundError(Exception):
    """Raised when a governance baseline file does not exist."""


class BaselineStore:
    """Save, load, and archive governance baselines under `<repo>/.verba/`."""

    def __init__(self, repo_path: Path):
        self.verba_dir = Path(repo_path) / ".verba"
        self.baseline_path = self.verba_dir / BASELINE_FILENAME
        self.history_dir = self.verba_dir / HISTORY_DIRNAME

    def save(self, results: dict) -> Path:
        """Write `results` to governance-baseline.json, becoming the approved governance state."""
        self.verba_dir.mkdir(parents=True, exist_ok=True)
        payload = OutputFormatter._json_safe(results)
        self.baseline_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return self.baseline_path

    def load(self, path: Optional[Path] = None) -> dict:
        """Load a governance baseline from `path`, or governance-baseline.json by default."""
        target = Path(path) if path else self.baseline_path
        if not target.exists():
            raise BaselineNotFoundError(
                f"No governance baseline found at {target}. "
                f"Run 'x-verba scan . --save-baseline' first."
            )
        with open(target, encoding="utf-8") as f:
            return json.load(f)

    def archive(self, results: dict) -> Path:
        """Append `results` to governance-history/ as the next sequential scan-NNN.json."""
        self.history_dir.mkdir(parents=True, exist_ok=True)
        existing = sorted(self.history_dir.glob("scan-*.json"))
        next_num = len(existing) + 1
        archive_path = self.history_dir / f"scan-{next_num:03d}.json"
        payload = OutputFormatter._json_safe(results)
        archive_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return archive_path

