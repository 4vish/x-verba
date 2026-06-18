"""
X-Verba Decision Graph Algorithms

Pure functions operating on `models.DecisionGraph`: PageRank-based decision
importance, critical path, reachability, and propagation-risk ranking.

Extracted from engine.py's DecisionGraphAnalyzer (TASK-009 to TASK-012) as
part of the v0.4.0 architectural refactor. No behaviour changes.
"""
from .pagerank import pagerank, PAGERANK_DAMPING, PAGERANK_ITERATIONS
from .critical_path import critical_path, reachability_from
from .propagation import propagation_potential, PROPAGATION_UNGOVERNED_WEIGHT

__all__ = [
    "pagerank",
    "PAGERANK_DAMPING",
    "PAGERANK_ITERATIONS",
    "critical_path",
    "reachability_from",
    "propagation_potential",
    "PROPAGATION_UNGOVERNED_WEIGHT",
]
