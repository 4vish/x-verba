"""PageRank over a DecisionGraph (TASK-009). Reference: Regeneration Handover, Part 9."""
from typing import Dict

from models import DecisionGraph

# PageRank defaults (Regeneration Handover, Part 9).
PAGERANK_DAMPING = 0.85
PAGERANK_ITERATIONS = 20


def pagerank(
    decision_graph: DecisionGraph,
    damping: float = PAGERANK_DAMPING, iterations: int = PAGERANK_ITERATIONS,
) -> Dict[str, float]:
    """
    Rank decision nodes by influence in the consequence network.

    Edges run from a decision node to a consequence location; an edge's
    target counts toward a node's PageRank only when that location is
    itself a decision node id (i.e. a decision whose location is also
    the site of a downstream consequence). Reference: Regeneration
    Handover, Part 9.
    """
    node_ids = list(decision_graph.nodes.keys())
    if not node_ids:
        return {}

    out_degree: Dict[str, int] = {}
    for edge in decision_graph.edges:
        out_degree[edge.from_node] = out_degree.get(edge.from_node, 0) + 1

    scores = {node_id: 1.0 / len(node_ids) for node_id in node_ids}

    for _ in range(iterations):
        new_scores = {}
        for node_id in node_ids:
            rank = (1 - damping) / len(node_ids)
            incoming_edges = [e for e in decision_graph.edges if e.to_consequence == node_id]
            for edge in incoming_edges:
                from_node = edge.from_node
                degree = out_degree.get(from_node, 0)
                if degree > 0 and from_node in scores:
                    rank += (damping * scores[from_node]) / degree
            new_scores[node_id] = rank
        scores = new_scores

    return dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
