"""
X-Verba Governance Verification Engine

Compares a Governance Baseline against the current scan's `results` dict and
reports whether governance improved, stayed stable, or regressed.

This module performs **no scanning** — `compare()` is a pure function of two
already-computed `results`-shaped dicts (as produced by `ScanEngine.scan()`
and persisted by `baseline.BaselineStore`). It has zero imports from the
detection layer.

All severity/threshold decisions are fixed, documented constants below.
"""
from typing import Any, Dict, List, Optional, Set, Tuple

from models import DeltaDirection, MetricDelta, Severity, VerificationResult

# ── Severity constants (Section 2.4 of the governance baselines plan) ───────

GAMMA_VALUE_DROP_SEVERITY = Severity.HIGH
GAMMA_STATUS_DOWNGRADE_SEVERITY = Severity.CRITICAL
GAMMA_STATUS_UPGRADE_SEVERITY = Severity.INFO

COVERAGE_SEVERITY = Severity.MEDIUM
COVERAGE_CRITICAL_DROP_SEVERITY = Severity.CRITICAL

GOVERNANCE_STATUS_DOWNGRADE_SEVERITY = Severity.CRITICAL
GOVERNANCE_STATUS_UPGRADE_SEVERITY = Severity.INFO

DECISION_CRITICAL_INCREASE_SEVERITY = Severity.HIGH
DECISION_TOTAL_CHANGE_SEVERITY = Severity.INFO

AI_PROVIDER_NEW_SEVERITY = Severity.MEDIUM
AI_PROVIDER_REMOVED_SEVERITY = Severity.INFO

AGENT_NEW_SEVERITY = Severity.MEDIUM
AGENT_REMOVED_SEVERITY = Severity.INFO
HANDOVER_NEW_UNGOVERNED_SEVERITY = Severity.HIGH
HANDOVER_NEW_GOVERNED_SEVERITY = Severity.MEDIUM
HANDOVER_REMOVED_SEVERITY = Severity.INFO

TOP_DECISIONS_CHANGED_SEVERITY = Severity.INFO

CRITICAL_FINDINGS_INCREASE_SEVERITY = Severity.CRITICAL
CRITICAL_FINDINGS_DECREASE_SEVERITY = Severity.INFO

# Ordering for governance status / gamma status escalation checks.
# Unknown statuses (e.g. future additions) rank as BELOW_THRESHOLD.
STATUS_RANK = {
    "NO_AI_INTEGRATIONS": 0,
    "NO_GOVERNABLE_DECISION_POINTS": 0,
    "BELOW_THRESHOLD": 1,
    "PARTIAL_COVERAGE": 2,
    "ABOVE_THRESHOLD": 3,
}


def _status_rank(status: Optional[str]) -> int:
    return STATUS_RANK.get(status, STATUS_RANK["BELOW_THRESHOLD"])


def _get(d: dict, *path, default=None):
    """Safely walk a chain of dict keys, returning `default` if any step is missing."""
    cur = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def _tuples_to_lists(value):
    """Recursively convert tuples to lists so YAML never emits !!python/tuple tags."""
    if isinstance(value, dict):
        return {k: _tuples_to_lists(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_tuples_to_lists(v) for v in value]
    return value


class GovernanceVerificationEngine:
    """Compares a governance baseline against the current scan results."""

    def compare(self, baseline: dict, current: dict) -> VerificationResult:
        current = _tuples_to_lists(current)
        deltas: List[MetricDelta] = []

        deltas.append(self._compare_gamma(baseline, current))
        deltas.append(self._compare_coverage(baseline, current))
        deltas.append(self._compare_governance_status(baseline, current))
        deltas.extend(self._compare_decision_inventory(baseline, current))
        deltas.extend(self._compare_ai_providers(baseline, current))
        deltas.extend(self._compare_agent_inventory(baseline, current))
        top_decisions_delta = self._compare_top_decisions(baseline, current)
        if top_decisions_delta is not None:
            deltas.append(top_decisions_delta)
        deltas.append(self._compare_critical_findings(baseline, current))

        return self._build_result(deltas)

    # ── Per-metric comparisons ───────────────────────────────────────────────

    def _compare_gamma(self, baseline: dict, current: dict) -> MetricDelta:
        b = _get(baseline, "summary", "gamma_variants", "overall", default={}) or {}
        c = _get(current, "summary", "gamma_variants", "overall", default={}) or {}
        b_value, b_status = b.get("value"), b.get("status")
        c_value, c_status = c.get("value"), c.get("status")

        if _status_rank(c_status) < _status_rank(b_status):
            return MetricDelta(
                metric="structural_gamma",
                baseline_value=b, current_value=c,
                direction=DeltaDirection.REGRESSED,
                severity=GAMMA_STATUS_DOWNGRADE_SEVERITY,
                description=f"Structural Gamma status downgraded: {b_status} -> {c_status}",
            )
        if _status_rank(c_status) > _status_rank(b_status):
            return MetricDelta(
                metric="structural_gamma",
                baseline_value=b, current_value=c,
                direction=DeltaDirection.IMPROVED,
                severity=GAMMA_STATUS_UPGRADE_SEVERITY,
                description=f"Structural Gamma status improved: {b_status} -> {c_status}",
            )
        if isinstance(b_value, (int, float)) and isinstance(c_value, (int, float)):
            if c_value > b_value:
                return MetricDelta(
                    metric="structural_gamma",
                    baseline_value=b, current_value=c,
                    direction=DeltaDirection.IMPROVED,
                    severity=Severity.INFO,
                    description=f"Structural Gamma improved: {b_value:.2f} -> {c_value:.2f}",
                )
            if c_value < b_value:
                return MetricDelta(
                    metric="structural_gamma",
                    baseline_value=b, current_value=c,
                    direction=DeltaDirection.REGRESSED,
                    severity=GAMMA_VALUE_DROP_SEVERITY,
                    description=f"Structural Gamma dropped: {b_value:.2f} -> {c_value:.2f}",
                )
        return MetricDelta(
            metric="structural_gamma",
            baseline_value=b, current_value=c,
            direction=DeltaDirection.STABLE,
            severity=Severity.INFO,
            description="Structural Gamma unchanged",
        )

    def _compare_coverage(self, baseline: dict, current: dict) -> MetricDelta:
        b_overall = _get(baseline, "summary", "coverage", "overall", default=0) or 0
        c_overall = _get(current, "summary", "coverage", "overall", default=0) or 0
        b_critical = _get(baseline, "summary", "coverage", "critical", default=0) or 0
        c_critical = _get(current, "summary", "coverage", "critical", default=0) or 0

        if c_critical < b_critical:
            return MetricDelta(
                metric="governance_coverage_critical",
                baseline_value=b_critical, current_value=c_critical,
                direction=DeltaDirection.REGRESSED,
                severity=COVERAGE_CRITICAL_DROP_SEVERITY,
                description=f"Critical governance coverage dropped: {b_critical:.1f}% -> {c_critical:.1f}%",
            )
        if c_overall > b_overall:
            return MetricDelta(
                metric="governance_coverage",
                baseline_value=b_overall, current_value=c_overall,
                direction=DeltaDirection.IMPROVED,
                severity=Severity.INFO,
                description=f"Governance coverage improved: {b_overall:.1f}% -> {c_overall:.1f}%",
            )
        if c_overall < b_overall:
            return MetricDelta(
                metric="governance_coverage",
                baseline_value=b_overall, current_value=c_overall,
                direction=DeltaDirection.REGRESSED,
                severity=COVERAGE_SEVERITY,
                description=f"Governance coverage dropped: {b_overall:.1f}% -> {c_overall:.1f}%",
            )
        return MetricDelta(
            metric="governance_coverage",
            baseline_value=b_overall, current_value=c_overall,
            direction=DeltaDirection.STABLE,
            severity=Severity.INFO,
            description="Governance coverage unchanged",
        )

    def _compare_governance_status(self, baseline: dict, current: dict) -> MetricDelta:
        b_status = _get(baseline, "summary", "governance_status")
        c_status = _get(current, "summary", "governance_status")

        if _status_rank(c_status) < _status_rank(b_status):
            return MetricDelta(
                metric="governance_status",
                baseline_value=b_status, current_value=c_status,
                direction=DeltaDirection.REGRESSED,
                severity=GOVERNANCE_STATUS_DOWNGRADE_SEVERITY,
                description=f"Governance status downgraded: {b_status} -> {c_status}",
            )
        if _status_rank(c_status) > _status_rank(b_status):
            return MetricDelta(
                metric="governance_status",
                baseline_value=b_status, current_value=c_status,
                direction=DeltaDirection.IMPROVED,
                severity=GOVERNANCE_STATUS_UPGRADE_SEVERITY,
                description=f"Governance status improved: {b_status} -> {c_status}",
            )
        return MetricDelta(
            metric="governance_status",
            baseline_value=b_status, current_value=c_status,
            direction=DeltaDirection.STABLE,
            severity=Severity.INFO,
            description="Governance status unchanged",
        )

    def _compare_decision_inventory(self, baseline: dict, current: dict) -> List[MetricDelta]:
        b_total = _get(baseline, "summary", "decision_inventory", "total", default=0) or 0
        c_total = _get(current, "summary", "decision_inventory", "total", default=0) or 0
        b_critical = _get(baseline, "summary", "decision_inventory", "critical", default=0) or 0
        c_critical = _get(current, "summary", "decision_inventory", "critical", default=0) or 0

        deltas: List[MetricDelta] = []
        if c_critical > b_critical:
            deltas.append(MetricDelta(
                metric="decision_inventory_critical",
                baseline_value=b_critical, current_value=c_critical,
                direction=DeltaDirection.REGRESSED,
                severity=DECISION_CRITICAL_INCREASE_SEVERITY,
                description=f"New critical decision points introduced: {b_critical} -> {c_critical}",
            ))
        elif c_total != b_total:
            deltas.append(MetricDelta(
                metric="decision_inventory_total",
                baseline_value=b_total, current_value=c_total,
                direction=DeltaDirection.STABLE,
                severity=DECISION_TOTAL_CHANGE_SEVERITY,
                description=f"Decision points changed: {b_total} -> {c_total}",
            ))
        return deltas

    def _compare_ai_providers(self, baseline: dict, current: dict) -> List[MetricDelta]:
        b_providers: Set[str] = set(_get(baseline, "summary", "ai_inventory", "by_provider", default={}) or {})
        c_providers: Set[str] = set(_get(current, "summary", "ai_inventory", "by_provider", default={}) or {})

        deltas: List[MetricDelta] = []
        for provider in sorted(c_providers - b_providers):
            deltas.append(MetricDelta(
                metric=f"ai_provider:{provider}",
                baseline_value=None, current_value=provider,
                direction=DeltaDirection.NEW,
                severity=AI_PROVIDER_NEW_SEVERITY,
                description=f"New AI provider detected: {provider}",
            ))
        for provider in sorted(b_providers - c_providers):
            deltas.append(MetricDelta(
                metric=f"ai_provider:{provider}",
                baseline_value=provider, current_value=None,
                direction=DeltaDirection.REMOVED,
                severity=AI_PROVIDER_REMOVED_SEVERITY,
                description=f"AI provider removed: {provider}",
            ))
        return deltas

    def _compare_agent_inventory(self, baseline: dict, current: dict) -> List[MetricDelta]:
        b_nodes = _get(baseline, "graphs", "agent_graph", "nodes", default=[]) or []
        c_nodes = _get(current, "graphs", "agent_graph", "nodes", default=[]) or []
        b_edges = _get(baseline, "graphs", "agent_graph", "edges", default=[]) or []
        c_edges = _get(current, "graphs", "agent_graph", "edges", default=[]) or []

        b_agent_names = {n.get("name") for n in b_nodes}
        c_agent_names = {n.get("name") for n in c_nodes}

        deltas: List[MetricDelta] = []
        for name in sorted(c_agent_names - b_agent_names):
            deltas.append(MetricDelta(
                metric=f"agent:{name}",
                baseline_value=None, current_value=name,
                direction=DeltaDirection.NEW,
                severity=AGENT_NEW_SEVERITY,
                description=f"New agent detected: {name}",
            ))
        for name in sorted(b_agent_names - c_agent_names):
            deltas.append(MetricDelta(
                metric=f"agent:{name}",
                baseline_value=name, current_value=None,
                direction=DeltaDirection.REMOVED,
                severity=AGENT_REMOVED_SEVERITY,
                description=f"Agent removed: {name}",
            ))

        def edge_key(e: dict) -> Tuple[Any, Any, Any]:
            return (e.get("from_agent"), e.get("to_agent"), e.get("data_variable"))

        b_edges_by_key = {edge_key(e): e for e in b_edges}
        c_edges_by_key = {edge_key(e): e for e in c_edges}

        for key in sorted(set(c_edges_by_key) - set(b_edges_by_key), key=str):
            edge = c_edges_by_key[key]
            from_agent, to_agent, data_variable = key
            if edge.get("pre_node_exists"):
                severity = HANDOVER_NEW_GOVERNED_SEVERITY
                description = f"New governed handover: {from_agent} -> {to_agent} ({data_variable})"
            else:
                severity = HANDOVER_NEW_UNGOVERNED_SEVERITY
                description = f"New ungoverned handover: {from_agent} -> {to_agent} ({data_variable})"
            deltas.append(MetricDelta(
                metric=f"agent_handover:{from_agent}->{to_agent}:{data_variable}",
                baseline_value=None, current_value=edge,
                direction=DeltaDirection.NEW,
                severity=severity,
                description=description,
            ))
        for key in sorted(set(b_edges_by_key) - set(c_edges_by_key), key=str):
            edge = b_edges_by_key[key]
            from_agent, to_agent, data_variable = key
            deltas.append(MetricDelta(
                metric=f"agent_handover:{from_agent}->{to_agent}:{data_variable}",
                baseline_value=edge, current_value=None,
                direction=DeltaDirection.REMOVED,
                severity=HANDOVER_REMOVED_SEVERITY,
                description=f"Handover removed: {from_agent} -> {to_agent} ({data_variable})",
            ))
        return deltas

    def _compare_top_decisions(self, baseline: dict, current: dict) -> Optional[MetricDelta]:
        b_top = _get(baseline, "summary", "top_decisions", default={}) or {}
        c_top = _get(current, "summary", "top_decisions", default={}) or {}
        if b_top == c_top:
            return None
        return MetricDelta(
            metric="top_decisions",
            baseline_value=b_top, current_value=c_top,
            direction=DeltaDirection.STABLE,
            severity=TOP_DECISIONS_CHANGED_SEVERITY,
            description="Critical/most-influential decision points changed",
        )

    def _compare_critical_findings(self, baseline: dict, current: dict) -> MetricDelta:
        b_critical = _get(baseline, "summary", "critical", default=0) or 0
        c_critical = _get(current, "summary", "critical", default=0) or 0

        if c_critical > b_critical:
            return MetricDelta(
                metric="critical_findings",
                baseline_value=b_critical, current_value=c_critical,
                direction=DeltaDirection.REGRESSED,
                severity=CRITICAL_FINDINGS_INCREASE_SEVERITY,
                description=f"Critical governance findings increased: {b_critical} -> {c_critical}",
            )
        if c_critical < b_critical:
            return MetricDelta(
                metric="critical_findings",
                baseline_value=b_critical, current_value=c_critical,
                direction=DeltaDirection.IMPROVED,
                severity=CRITICAL_FINDINGS_DECREASE_SEVERITY,
                description=f"Critical governance findings decreased: {b_critical} -> {c_critical}",
            )
        return MetricDelta(
            metric="critical_findings",
            baseline_value=b_critical, current_value=c_critical,
            direction=DeltaDirection.STABLE,
            severity=Severity.INFO,
            description="Critical governance findings unchanged",
        )

    # ── DC-aware QA recommendations ──────────────────────────────────────────

    def dc_qa_recommendations(self, legion_matches: list) -> list:
        """Generate QA test recommendations from Legion match findings.

        HIGH/MEDIUM confidence matches → specific named test cases.
        SPECULATIVE matches → generic manual review note.
        Returns a list of recommendation dicts for inclusion in the QA report.
        """
        return _dc_qa_recommendations(legion_matches)

    # ── Aggregation ───────────────────────────────────────────────────────────

    def _build_result(self, deltas: List[MetricDelta]) -> VerificationResult:
        has_critical_regressions = any(
            d.severity == Severity.CRITICAL and d.direction == DeltaDirection.REGRESSED
            for d in deltas
        )
        has_regressions = any(
            d.severity in (Severity.HIGH, Severity.CRITICAL)
            and d.direction in (DeltaDirection.REGRESSED, DeltaDirection.NEW)
            for d in deltas
        )
        has_improvements = any(
            d.direction in (DeltaDirection.IMPROVED, DeltaDirection.REMOVED)
            for d in deltas
        )

        if has_regressions:
            overall_status = "REGRESSED"
        elif has_improvements:
            overall_status = "IMPROVED"
        else:
            overall_status = "STABLE"

        return VerificationResult(
            deltas=deltas,
            overall_status=overall_status,
            passed=not has_critical_regressions,
            has_critical_regressions=has_critical_regressions,
        )


# ── DC-to-QA test mapping ─────────────────────────────────────────────────────

_DC_QA_TESTS: Dict[str, List[Dict[str, str]]] = {
    "DC-E13": [
        {
            "test": "test_ungated_agent_handover",
            "description": "Verify agent handover is blocked without a validated Pre-Node.",
            "approach": "Mock the receiving agent; inject corrupted/malformed output from the sending agent. Assert the handover is rejected or quarantined.",
        },
        {
            "test": "test_chained_ai_calls_propagate_errors",
            "description": "Verify chained AI calls do not silently propagate errors across the chain.",
            "approach": "Force the first AI call to return an error payload. Assert the second call receives no input or raises before proceeding.",
        },
    ],
    "DC-I11": [
        {
            "test": "test_confidence_gate_without_correctness_check",
            "description": "Verify confidence score threshold gate is paired with a correctness check.",
            "approach": "Submit input that produces a high-confidence but factually incorrect response. Assert the downstream action is blocked or flagged for review.",
        },
        {
            "test": "test_shadow_compliance_validation_unused",
            "description": "Verify that validation results are consumed and not silently discarded.",
            "approach": "Introduce a validation function that returns False. Assert the caller branches on the result rather than proceeding unconditionally.",
        },
    ],
    "DC-E1": [
        {
            "test": "test_boundary_condition_amount_zero",
            "description": "Verify AI-driven action handles amount=0 safely.",
            "approach": "Pass amount=0. Assert no divide-by-zero, no silent no-op, and the response is deterministic.",
        },
        {
            "test": "test_boundary_condition_amount_negative",
            "description": "Verify AI-driven action rejects or handles amount=-1.",
            "approach": "Pass amount=-1. Assert an explicit error is raised rather than a silent incorrect result.",
        },
        {
            "test": "test_boundary_condition_amount_overflow",
            "description": "Verify AI-driven action handles amount > MAX safely.",
            "approach": "Pass amount=MAX+1. Assert overflow is caught before the action executes.",
        },
    ],
}

_SPECULATIVE_NOTE = (
    "SPECULATIVE match — manual review required. "
    "Confirm whether this pattern represents a real governance gap before writing tests."
)


def _dc_qa_recommendations(legion_matches: list) -> list:
    """Map Legion match findings to concrete QA test recommendations.

    HIGH/MEDIUM confidence → specific named test cases from _DC_QA_TESTS.
    SPECULATIVE → generic manual review note.
    Unknown DC codes → generic structural test suggestion.
    """
    recommendations = []
    seen: set = set()

    for match in legion_matches:
        dc_code = match.get("dc_code", "")
        confidence = match.get("confidence", "SPECULATIVE")
        location = match.get("location", "")
        legion_name = match.get("legion_name", match.get("legion_code", ""))

        key = (dc_code, confidence)
        if key in seen:
            continue
        seen.add(key)

        if confidence == "SPECULATIVE":
            recommendations.append({
                "dc_code": dc_code,
                "legion": legion_name,
                "location": location,
                "confidence": "SPECULATIVE",
                "note": _SPECULATIVE_NOTE,
                "tests": [],
            })
            continue

        tests = _DC_QA_TESTS.get(dc_code)
        if tests:
            recommendations.append({
                "dc_code": dc_code,
                "legion": legion_name,
                "location": location,
                "confidence": confidence,
                "tests": tests,
            })
        else:
            recommendations.append({
                "dc_code": dc_code,
                "legion": legion_name,
                "location": location,
                "confidence": confidence,
                "tests": [
                    {
                        "test": f"test_{dc_code.lower().replace('-', '_')}_governance",
                        "description": f"Verify governance gate for {dc_code} ({legion_name}).",
                        "approach": "Inject a scenario that would trigger ungoverned drift. Assert the Pre-Node blocks or flags the action.",
                    }
                ],
            })

    return recommendations
