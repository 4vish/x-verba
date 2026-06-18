"""Propagation-risk ranking over a DecisionGraph (TASK-012). Reference: Regeneration Handover, Part 9."""
from typing import Dict, List

from models import DecisionGraph
from .critical_path import reachability_from

# Each ungoverned node on a propagation path multiplies the path's risk by
# (1 + ungoverned_count * PROPAGATION_UNGOVERNED_WEIGHT).
PROPAGATION_UNGOVERNED_WEIGHT = 0.5


def propagation_potential(
    decision_graph: DecisionGraph, ungoverned_decision: str, max_depth: int = 5,
) -> Dict[str, List[str]]:
    """
    For an ungoverned decision, find every downstream consequence/decision
    reachable from it, ranked by propagation risk (highest first): the
    sum of reachable-node criticalities, amplified by how many of those
    nodes are themselves ungoverned. Reference: Regeneration Handover,
    Part 9.
    """
    reachable = reachability_from(decision_graph, ungoverned_decision, max_depth)

    ranked = sorted(
        reachable.items(),
        key=lambda item: _propagation_risk_score(item[1], decision_graph),
        reverse=True,
    )
    return dict(ranked)


def _propagation_risk_score(path: List[str], decision_graph: DecisionGraph) -> float:
    risk = 0.0
    ungoverned_count = 0
    for node_id in path:
        node = decision_graph.nodes.get(node_id)
        if node is not None:
            risk += node.criticality
            if not node.governed:
                ungoverned_count += 1
    return risk * (1 + ungoverned_count * PROPAGATION_UNGOVERNED_WEIGHT)
