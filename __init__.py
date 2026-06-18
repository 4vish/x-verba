"""X-VERBA v0.4.0 — Governance Intelligence Platform"""

__version__ = "0.4.0"

from engine import (
    ScanEngine,
    OutputFormatter,
    TendencyState,
)

from writer import (
    OutputWriter,
)

from cli import (
    main,
)

__all__ = [
    "ScanEngine",
    "OutputFormatter",
    "TendencyState",
    "OutputWriter",
    "main",
]
