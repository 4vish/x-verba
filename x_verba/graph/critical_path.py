"""Critical path and reachability over a DecisionGraph (TASK-010/011)."""
from typing import Dict, List

from models import DecisionGraph


def critical_path(decision_graph: DecisionGraph) -> List[str]:
    """
    Find the path of decisions whose cumulative criticality (own node
    criticality plus outgoing edge criticalities) is highest — the
    sequence most worth governing first. Reference: Regeneration
    Handover, Part 8.
    """
    nodes = decision_graph.nodes
    edges = decision_graph.edges
    if not nodes:
        return []

    def dfs_criticality(node_id: str, visited: set):
        if node_id in visited:
            return 0.0, []
        visited = visited | {node_id}

        node = nodes.get(node_id)
        base_criticality = node.criticality if node else 0.0
        outgoing = [e for e in edges if e.from_node == node_id]

        best_extra, best_path = 0.0, []
        for edge in outgoing:
            target = edge.to_consequence
            downstream_crit, downstream_path = (
                dfs_criticality(target, visited) if target in nodes else (0.0, [])
            )
            total = edge.criticality + downstream_crit
            if total >= best_extra:
                best_extra, best_path = total, downstream_path

        return base_criticality + best_extra, [node_id] + best_path

    targets = {e.to_consequence for e in edges}
    entry_nodes = [n for n in nodes if n not in targets] or list(nodes.keys())

    best_crit, best_path = -1.0, []
    for entry in entry_nodes:
        crit, path = dfs_criticality(entry, set())
        if crit > best_crit:
            best_crit, best_path = crit, path

    return best_path


def reachability_from(
    decision_graph: DecisionGraph, start_node: str, max_depth: int = 5,
) -> Dict[str, List[str]]:
    """
    Find every node/consequence reachable from `start_node`, with the
    path taken to reach it. Cycles are avoided by excluding nodes
    already on the current path; traversal stops at `max_depth` hops.
    """
    edges = decision_graph.edges
    results: Dict[str, List[str]] = {}

    def dfs(node_id: str, path: List[str], depth: int):
        if depth > max_depth or node_id in path:
            return
        path = path + [node_id]
        results[node_id] = path
        for edge in (e for e in edges if e.from_node == node_id):
            dfs(edge.to_consequence, path, depth + 1)

    dfs(start_node, [], 0)
    return results
