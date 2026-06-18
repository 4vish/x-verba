"""
X-Verba Domain Models

Dataclasses and enums shared across engine.py, graph/, and writer.py:
governance drift state, enriched consequences, agent/decision graphs,
inventories, governance coverage, tendency indicators, and Gamma variants.

Extracted from engine.py (TASK-001, TASK-006, TASK-007, TASK-008) as part of
the v0.4.0 architectural refactor. No behaviour changes — definitions are
unchanged from their original engine.py location.
"""
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Optional, List, Dict


# ── TASK-001: Enhanced data models ────────────────────────────────────────────

class TendencyState(Enum):
    """Governance drift state, classified by TendencyAnalyzer (Pass 14)."""
    STABLE = "stable"
    EMERGING = "emerging"
    AMPLIFYING = "amplifying"
    CRITICAL = "critical"
    FAILURE = "failure"


# Scoring tables for EnhancedConsequence.criticality (Regeneration Handover, Part 4).
BUSINESS_IMPACT_SCORES = {"low": 0.2, "medium": 0.5, "high": 0.8, "critical": 1.0}

BLAST_RADIUS_SCORES = {
    "single_user": 0.1, "team": 0.3, "department": 0.5,
    "customer": 0.7, "organization": 0.85, "public": 1.0,
}

# reversible: "true" | "partial" | "false" (string, not bool — partial states exist)
REVERSIBILITY_SCORES = {"true": 0.1, "partial": 0.3, "false": 1.0}


@dataclass
class EnhancedConsequence:
    """
    A consequence (Pass 2) enriched with business-relevant attributes:
    blast radius, business impact, governance status, and a computed
    criticality score used to prioritise findings and build the
    DecisionGraph (Pass 11).
    """
    location: str
    decision_location: str
    consequence_type: str
    reversible: str  # "true" | "partial" | "false"
    blast_radius: str  # single_user|team|department|customer|organization|public
    business_impact: str  # low|medium|high|critical
    governed: bool
    governance_type: Optional[str]
    governance_strength: float
    drift_class: Optional[str] = None

    @property
    def criticality(self) -> float:
        """
        Criticality = business_impact x blast_radius x irreversibility x (1 + governance_gap)

        governance_gap is 0.0 if governed (Pre-Node strength >= 0.5), else
        1.0 — doubling the score for ungoverned consequences.
        Reference: Regeneration Handover, Part 4.
        """
        impact = BUSINESS_IMPACT_SCORES.get(self.business_impact, 0.5)
        radius = BLAST_RADIUS_SCORES.get(self.blast_radius, 0.5)
        irreversibility = REVERSIBILITY_SCORES.get(self.reversible, 0.3)
        governance_gap = 0.0 if self.governed else 1.0
        return impact * radius * irreversibility * (1 + governance_gap)

    def to_dict(self) -> dict:
        """JSON-serialisable representation, including the computed criticality."""
        d = asdict(self)
        d["criticality"] = self.criticality
        return d


@dataclass
class AgentNode:
    """A unique agent identified from agent-to-agent handovers (Pass 4)."""
    name: str
    framework: str  # crewai|autogen|langchain|langgraph|unknown
    location: str  # file:line of first occurrence
    methods: List[str] = field(default_factory=list)
    governed: bool = False
    governance_type: Optional[str] = None
    governance_strength: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AgentEdge:
    """A single agent-to-agent handover (Pass 4), as a graph edge."""
    from_agent: str
    to_agent: str
    data_variable: str
    location: str  # file:line
    pre_node_exists: bool
    pre_node_strength: float
    drift_class: Optional[str] = None  # e.g. "DC-E13" if ungoverned

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AgentGraph:
    """
    Topology of agent-to-agent handovers within a scan.

    `chains` are maximal linear sequences of handovers (A -> B -> C);
    `clusters` are connected components of the handover graph.
    """
    nodes: List[AgentNode] = field(default_factory=list)
    edges: List[AgentEdge] = field(default_factory=list)
    chains: List[List[str]] = field(default_factory=list)
    clusters: List[List[str]] = field(default_factory=list)

    @property
    def ungoverned_edges(self) -> List[AgentEdge]:
        return [e for e in self.edges if not e.pre_node_exists]

    @property
    def chain_risk(self) -> Dict[int, float]:
        """Propagation risk per chain: ratio of ungoverned edges within it."""
        risks = {}
        for idx, chain in enumerate(self.chains):
            chain_edges = [
                e for e in self.edges
                if e.from_agent in chain and e.to_agent in chain
            ]
            if chain_edges:
                ungoverned = sum(1 for e in chain_edges if not e.pre_node_exists)
                risks[idx] = ungoverned / len(chain_edges)
        return risks

    def to_dict(self) -> dict:
        return {
            "nodes": [n.to_dict() for n in self.nodes],
            "edges": [e.to_dict() for e in self.edges],
            "chains": self.chains,
            "clusters": self.clusters,
        }


@dataclass
class DecisionNode:
    """A decision point (Pass 1), as a node in the DecisionGraph."""
    id: str  # location (file:line)
    decision_type: str  # conditional_branch|ternary|loop|try_except|agent_invocation|function_call
    condition: str
    pre_node_strength: float
    governed: bool
    criticality: float = 0.5  # placeholder; updated from consequence edges

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DecisionEdge:
    """An edge from a decision point to one of its downstream consequences."""
    from_node: str  # decision location
    to_consequence: str  # consequence location
    consequence_type: str
    criticality: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DecisionGraph:
    """Decision points (nodes) mapped to their downstream consequences (edges)."""
    nodes: Dict[str, DecisionNode] = field(default_factory=dict)
    edges: List[DecisionEdge] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "nodes": {loc: n.to_dict() for loc, n in self.nodes.items()},
            "edges": [e.to_dict() for e in self.edges],
        }


@dataclass
class AIInventory:
    """Aggregated view of all detected AI integrations (Pass 1)."""
    total: int
    by_provider: Dict[str, int] = field(default_factory=dict)
    governed: int = 0
    ungoverned: int = 0
    high_risk_patterns: int = 0  # temperature > 0.7 AND user_input_in_prompt AND dynamic_prompt

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AgentInventory:
    """Aggregated view of agents, handovers, chains, and clusters (Pass 4-5, 11)."""
    total_agents: int
    total_handovers: int
    governed_handovers: int
    ungoverned_handovers: int
    total_chains: int
    fully_governed_chains: int
    partially_governed_chains: int
    ungoverned_chains: int
    total_clusters: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DecisionInventory:
    """Aggregated view of decision points by consequence type and criticality band."""
    total: int
    by_consequence_type: Dict[str, int] = field(default_factory=dict)
    by_criticality: Dict[str, int] = field(default_factory=dict)
    critical_total: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


# ── TASK-006: Governance coverage model ───────────────────────────────────────

@dataclass
class GovernanceCoverage:
    """
    Governance coverage broken down by decision type, consequence type,
    criticality, and checkpoint type. All percentages are 0-100.
    """
    overall_percent: float
    by_decision_type: Dict[str, float] = field(default_factory=dict)
    by_consequence_type: Dict[str, float] = field(default_factory=dict)
    critical_coverage: float = 0.0
    by_checkpoint_type: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


# ── TASK-007: Tendency indicators ─────────────────────────────────────────────

@dataclass
class TendencyIndicators:
    """
    Governance drift indicators and the resulting TendencyState
    classification. Reference: Regeneration Handover, Part 10.
    """
    ungoverned_decision_density: float
    critical_ungoverned_ratio: float
    ungoverned_handover_ratio: float
    high_centrality_ungoverned: int
    dependency_bridges_ungoverned: int
    silent_failure_density: int
    score: float
    state: TendencyState
    t_amplification_active: bool
    pre_node_proximity: str

    def to_dict(self) -> dict:
        d = asdict(self)
        d["state"] = self.state.value
        return d


# ── TASK-008: Gamma variants ──────────────────────────────────────────────────

@dataclass
class GammaValue:
    """A single Gamma ratio with its coverage status and supporting counts."""
    value: float
    status: str  # ABOVE_THRESHOLD | PARTIAL_COVERAGE | BELOW_THRESHOLD
    governed: int = 0
    total: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class GammaVariants:
    """All Structural Gamma variants for a scan. Reference: Regeneration Handover, Part 11."""
    overall: GammaValue
    by_decision_type: Dict[str, GammaValue] = field(default_factory=dict)
    by_consequence_type: Dict[str, GammaValue] = field(default_factory=dict)
    critical: GammaValue = None
    agent_handover: GammaValue = None
    agent_chain: GammaValue = None
    cluster: GammaValue = None

    def to_dict(self) -> dict:
        return asdict(self)


# ── VERBA Phase 2: governance primitive models ───────────────────────────────
#
# Promoted from raw dict literals in engine.py. No behaviour change — each
# to_dict() reproduces the exact dict shape engine.py built by hand. These
# give the scanner typed governance objects (VSL-readiness groundwork)
# without changing any rendered output.

@dataclass
class PreNode:
    """A detected Pre-Node (checkpoint) guarding a decision point, with its
    strength (0.0-1.0) and the line of code that triggered detection."""
    type: str
    strength: float
    evidence_line: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TerminalState:
    """A state from which no automated transition is permitted — e.g. an
    except block that swallows an exception with no recovery action."""
    id: str
    type: str
    location: str
    severity: str
    plain_english: str
    consequence: str
    recommended_action: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Invariant:
    """An informal governance check (assertion, validation, auth check)
    detected in code — a candidate for formalisation as a VERBA Invariant."""
    location: str
    type: str
    pattern: str
    line_content: str
    near_ai_call: bool

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class GovernanceGap:
    """
    A detected governance gap (missing Pre-Node, missing human gate,
    ungated irreversible action, informal invariant, or ungoverned decision
    point). The five gap subtypes share a common core but each carries a
    few type-specific fields — those live in `extra` so to_dict() reproduces
    each subtype's exact historical dict shape with no spurious keys.
    """
    id: str
    type: str
    location: str
    severity: str
    plain_english: str
    what_is_missing: str
    consequence: str
    verba_term: str
    recommended_action: str
    policy: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        core = asdict(self)
        extra = core.pop("extra")
        return {**core, **extra}


# ── VERBA Phase 2: governance verification models ────────────────────────────

class Severity(Enum):
    """Severity of a governance metric delta between baseline and current scan."""
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DeltaDirection(Enum):
    """Direction of change for a governance metric between baseline and current scan."""
    IMPROVED = "improved"
    STABLE = "stable"
    REGRESSED = "regressed"
    NEW = "new"
    REMOVED = "removed"


@dataclass
class MetricDelta:
    """A single before/after comparison between a governance baseline and
    the current scan, e.g. Structural Gamma 0.83 -> 0.92."""
    metric: str
    baseline_value: Any
    current_value: Any
    direction: DeltaDirection
    severity: Severity
    description: str

    def to_dict(self) -> dict:
        d = asdict(self)
        d["direction"] = self.direction.value
        d["severity"] = self.severity.value
        return d


@dataclass
class VerificationResult:
    """
    Result of comparing a governance baseline against the current scan —
    "has governance improved, degraded, or remained stable?"
    """
    deltas: List[MetricDelta]
    overall_status: str  # IMPROVED | STABLE | REGRESSED
    passed: bool
    has_critical_regressions: bool

    def to_dict(self) -> dict:
        delta_dicts = [d.to_dict() for d in self.deltas]
        regressions = [
            {
                "metric": d["metric"],
                "severity": d["severity"],
                "location": d["metric"],
                "description": d["description"],
                "baseline_value": d["baseline_value"],
                "current_value": d["current_value"],
            }
            for d in delta_dicts
            if d["direction"] in ("regressed", "new") and d["severity"] in ("high", "critical")
        ]
        improvements = [d for d in delta_dicts if d["direction"] in ("improved", "removed")]
        return {
            "deltas": delta_dicts,
            "overall_status": self.overall_status,
            "passed": self.passed,
            "has_critical_regressions": self.has_critical_regressions,
            "regressions": regressions,
            "improvements": improvements,
        }


# ── Legion operational semantics models ──────────────────────────────────────
#
# Formalises the Legion detection layer as a typed data model.
# EvidenceNode is the intermediate representation between AST/CFG primitives
# and a Legion instance. Legion is the unit of drift detection — one matched
# pattern hypothesis, with a canonical_hash that guarantees deterministic
# deduplication across scan passes.

@dataclass
class EvidenceNode:
    """Intermediate representation between AST/CFG primitives and Legion detection.

    Each EvidenceNode captures one piece of structural or keyword evidence
    from code analysis before it is aggregated into a Legion. The
    canonical_hash guarantees that the same evidence at the same location
    always produces the same identifier, enabling stable deduplication.
    """
    type: str               # "ast_pattern" | "cfg_node" | "call_edge" | "keyword_match"
    source: str             # descriptor: AST node type, CFG block label, call signature
    payload: Dict[str, Any] # pattern-specific data extracted from code
    confidence: float       # raw evidence strength 0.0–1.0
    file_path: str
    line_number: int
    canonical_hash: str = ""  # SHA256[:16] of (type, source, file_path, line_number)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Legion:
    """A detected drift pattern instance.

    Represents the hypothesis that a specific Drift Class failure mode is
    structurally present in the codebase at a given location. Each Legion
    is produced by one of three detection methods:

      - structural_pattern: derived directly from the AST/call-graph
        (Pass 4 agent handovers, Pass 2 decision points, chained AI calls)
      - keyword_heuristic: derived from keyword matching against code snippets
        (SPECULATIVE tier only — requires human confirmation)

    The canonical_hash field is a deterministic SHA256-based identifier
    computed from (dc_code, legion_code, file_path, line_number, matched_pattern).
    Two Legion instances with the same canonical_hash represent the same
    structural finding and are deduplicated by _dedup_legions().
    """
    id: str                      # == canonical_hash (first 16 hex chars)
    dc_code: str                 # primary Drift Class, e.g. "DC-E13"
    dc_name: str
    legion_code: str             # Legion within the DC, e.g. "L1"
    legion_name: str
    description: str             # human-readable description of the pattern
    detection_method: str        # "structural_pattern" | "keyword_heuristic"
    confidence_float: float      # 0.9 = HIGH, 0.6 = MEDIUM, 0.3 = SPECULATIVE
    confidence: str              # "HIGH" | "MEDIUM" | "SPECULATIVE" (label)
    evidence_type: str           # "code_pattern" | "call_graph" | "cfg_node"
    file_path: str
    line_number: int
    location: str                # "{file_path}:{line_number}" (legacy compat)
    code_context: str            # evidence snippet (matched text or surrounding lines)
    observability_level: str     # "STRUCTURAL" | "BEHAVIOURAL"
    canonical_hash: str          # SHA256[:16] — deduplication key
    version: str = "1.0"         # schema version for forward compatibility
    tier: str = ""               # DC tier (A/B/C/D) from taxonomy
    primary_so: str = ""         # recommended Stabilising Operator
    heuristic_description: str = ""
    matched_pattern: str = ""
    false_positive_conditions: List[str] = field(default_factory=list)
    false_negative_conditions: List[str] = field(default_factory=list)
    created_at: str = ""         # ISO timestamp of first detection
    last_updated: str = ""       # ISO timestamp of last confidence update

    def __hash__(self) -> int:
        return hash(self.canonical_hash)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Legion) and self.canonical_hash == other.canonical_hash

    def to_dict(self) -> dict:
        """Backward-compatible dict.

        Preserves all keys that existing consumers (writer.py, qa_engine.py,
        _enrich_gaps_with_drift_exposure) already read, and appends the new
        schema fields. No consumer changes required.
        """
        return {
            # ── Legacy keys (shape unchanged) ─────────────────────────────
            "dc_code": self.dc_code,
            "dc_name": self.dc_name,
            "tier": self.tier,
            "legion_code": self.legion_code,
            "legion_name": self.legion_name,
            "location": self.location,
            "confidence": self.confidence,
            "evidence": self.code_context,
            "matched_pattern": self.matched_pattern,
            "heuristic_description": self.heuristic_description,
            "primary_so": self.primary_so,
            # ── New schema fields ─────────────────────────────────────────
            "id": self.id,
            "description": self.description,
            "detection_method": self.detection_method,
            "confidence_float": self.confidence_float,
            "evidence_type": self.evidence_type,
            "file_path": self.file_path,
            "line_number": self.line_number,
            "observability_level": self.observability_level,
            "canonical_hash": self.canonical_hash,
            "version": self.version,
            "false_positive_conditions": self.false_positive_conditions,
            "false_negative_conditions": self.false_negative_conditions,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
        }
