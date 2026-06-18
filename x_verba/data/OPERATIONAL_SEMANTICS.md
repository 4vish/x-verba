# X-Verba Legion Detection — Operational Semantics

**Version:** 1.0  
**Applies to:** x-verba v0.4.0-mvp1  
**Status:** Normative — independent implementations should produce byte-identical Legion sets for identical input.

---

## 1. Overview

Legion detection transforms raw scan primitives (AST nodes, CFG branches, call-graph edges) into typed, deduplicated, confidence-scored drift pattern hypotheses called **Legions**.

The pipeline has four layers:

```
Scan Primitives (AST / CFG / Call Graph)
      │
      ▼  Layer 2: Evidence Extraction
  EvidenceNode[]  ← _extract_evidence_nodes(primitives)
      │
      ▼  Layer 3: Deterministic Extraction Algorithm
  Legion[]        ← LegionMatcher.match(primitives)
      │
      ▼  Layer 4: Lifecycle Management
  Legion[]        ← _dedup_legions(legions)  [dedup by canonical_hash]
      │
      ▼  Output
  list[dict]      ← [l.to_dict() for l in legions]
                     → results["legion_matches"]
```

---

## 2. Legion Schema

Defined in `models.py` as the `Legion` dataclass.

### 2.1 Field Reference

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Equals `canonical_hash` — the deduplication key |
| `dc_code` | `str` | Primary Drift Class, e.g. `"DC-E13"` |
| `dc_name` | `str` | Human-readable DC name |
| `legion_code` | `str` | Legion within the DC, e.g. `"L1"` |
| `legion_name` | `str` | Human-readable Legion name |
| `description` | `str` | What the pattern means in plain English |
| `detection_method` | `str` | `"structural_pattern"` or `"keyword_heuristic"` |
| `confidence_float` | `float` | `0.9` (HIGH), `0.6` (MEDIUM), `0.3` (SPECULATIVE) |
| `confidence` | `str` | `"HIGH"`, `"MEDIUM"`, or `"SPECULATIVE"` |
| `evidence_type` | `str` | `"call_graph"`, `"cfg_node"`, or `"code_pattern"` |
| `file_path` | `str` | Source file where pattern was detected |
| `line_number` | `int` | Line number within that file |
| `location` | `str` | `"{file_path}:{line_number}"` (legacy compat) |
| `code_context` | `str` | Evidence snippet — matched text or surrounding lines |
| `observability_level` | `str` | `"STRUCTURAL"` or `"BEHAVIOURAL"` |
| `canonical_hash` | `str` | SHA256[:16] — deterministic deduplication key |
| `version` | `str` | Schema version, currently `"1.0"` |
| `tier` | `str` | DC tier (`A`/`B`/`C`/`D`) from taxonomy |
| `primary_so` | `str` | Recommended Stabilising Operator |
| `false_positive_conditions` | `list[str]` | When this pattern may not indicate actual drift |
| `false_negative_conditions` | `list[str]` | When this pattern may be absent despite drift |
| `created_at` | `str` | ISO 8601 UTC timestamp of first detection |
| `last_updated` | `str` | ISO 8601 UTC timestamp of last confidence update |

### 2.2 Confidence Tiers

Three tiers, each with a canonical float value:

| Label | Float | Detection method | Meaning |
|---|---|---|---|
| `HIGH` | `0.9` | `structural_pattern` | Directly computed from structural analysis — ungated agent handover, confidence-gate-without-correctness-check. Treat as a confirmed finding pending human review. |
| `MEDIUM` | `0.6` | `structural_pattern` | Reasonably specific pattern match — chained AI calls. Likely correct; worth investigating. |
| `SPECULATIVE` | `0.3` | `keyword_heuristic` | Keyword match derived from Legion name keywords. No verified structural signature. Flag for human review before acting on. |

**Rule:** Confidence only ever increases through `_update_legion_confidence()`. A HIGH detection cannot be downgraded to SPECULATIVE by a later pass.

### 2.3 Detection Method → Evidence Type Mapping

| `detection_method` | `matched_pattern` | `evidence_type` |
|---|---|---|
| `structural_pattern` | `agent_handover_no_prenode` | `call_graph` |
| `structural_pattern` | `chained_ai_calls` | `call_graph` |
| `structural_pattern` | `cluster_governance_gap` | `call_graph` |
| `structural_pattern` | `confidence_gate_no_correctness_check` | `cfg_node` |
| `keyword_heuristic` | any keyword | `code_pattern` |

### 2.4 Observability Level

- `STRUCTURAL` — the pattern is visible in static code structure (call graph, CFG). Independent implementations should always detect it.
- `BEHAVIOURAL` — the pattern depends on keyword matching against runtime-adjacent concepts (variable names, comment patterns). Detection is probabilistic and environment-sensitive.

---

## 3. EvidenceNode Schema

Defined in `models.py` as the `EvidenceNode` dataclass.

```
EvidenceNode
  ├── type: "ast_pattern" | "cfg_node" | "call_edge" | "keyword_match"
  ├── source: descriptor (AST node type, CFG block label, call signature)
  ├── payload: dict — pattern-specific data extracted from code
  ├── confidence: float 0.0–1.0
  ├── file_path: str
  ├── line_number: int
  └── canonical_hash: SHA256[:16] of (type, source, file_path, line_number)
```

EvidenceNodes are **intermediate representations** — they are extracted from scan primitives and used internally by the extraction algorithm but do not appear in `results["legion_matches"]`. They are produced by `_extract_evidence_nodes(primitives)` and can be used by `_update_legion_confidence()` when new evidence arrives.

### 3.1 Primitive → EvidenceNode Mapping

| Primitive source | EvidenceNode.type | confidence |
|---|---|---|
| `decision_points` (conditionals, loops, try/except) | `cfg_node` | `0.7` |
| `agent_handovers` (ungoverned) | `call_edge` | `0.9` |
| `agent_handovers` (governed) | `call_edge` | `0.3` |
| `ai_integrations` | `ast_pattern` | `0.8` |

---

## 4. Evidence Graph Layer

### 4.1 Conceptual Model

```
Source Code
    │
    ├─ ASTAnalyser (Python)       ─→ ai_integrations[]
    ├─ DecisionPointAnalyser      ─→ decision_points[]
    ├─ AgentHandoverAnalyser      ─→ agent_handovers[]
    └─ ConsequenceClassifier      ─→ consequences[]
    
         └──── All ──────────────→  primitives dict
                                         │
                          _extract_evidence_nodes(primitives)
                                         │
                                  EvidenceNode[]
                                         │
                          LegionMatcher.match(primitives)
                          (uses primitives directly, EvidenceNodes
                           available for lifecycle updates)
                                         │
                                    Legion[]
```

### 4.2 Evidence → Legion Transformation

Each heuristic in `LegionMatcher` maps a specific primitive pattern to a `Legion` instance via `_build_match()`:

```
Heuristic                  Evidence Source         → Legion Confidence
─────────────────────────────────────────────────────────────────────
_match_agent_handovers     agent_handovers (Pass4) → HIGH   (structural)
_match_cluster_gaps        cluster_governance_gaps → HIGH   (structural)
_match_confidence_gates    decision_points (CFG)   → HIGH   (structural)
_match_chained_ai_calls    ai_integrations (count) → MEDIUM (structural)
_match_validation_unused   decision_points (calls) → SPECULATIVE (keyword)
_match_keyword_legions     all snippets            → SPECULATIVE (keyword)
```

---

## 5. Deterministic Extraction Algorithm

### 5.1 Specification

```python
def legion_extraction_algorithm(primitives, dc_classes_complete, legion_patterns):
    """
    Given identical (primitives, dc_classes_complete, legion_patterns),
    this algorithm always produces the same set of Legion instances,
    as determined by their canonical_hashes.

    Guarantees:
    1. DETERMINISM:  Same code → same Legions (by canonical_hash). Always.
    2. STABILITY:    Output order is consistent — sorted by canonical_hash
                     after deduplication.
    3. INDEPENDENCE: An independent implementation given the same inputs
                     and the same canonical_hash function should produce
                     a set of canonical_hashes that is a subset/superset
                     of this implementation's output (differences only
                     from heuristic coverage, not non-determinism).
    4. VERSIONED:    All Legions carry version="1.0". Schema changes
                     increment this field.
    """

    # Step 1: Run heuristics in fixed order (stable input order within each)
    legions = []
    legions += _match_confidence_gates(primitives)    # HIGH (structural)
    legions += _match_validation_unused(primitives)   # SPECULATIVE
    legions += _match_agent_handovers(primitives)     # HIGH (structural)
    legions += _match_chained_ai_calls(primitives)    # MEDIUM (structural)
    legions += _match_cluster_gaps(primitives)        # HIGH (structural)
    legions += _match_keyword_legions(primitives,     # SPECULATIVE
                   already_matched=legions)

    # Step 2: Sort by canonical_hash — CRITICAL for stable deduplication
    legions.sort(key=lambda l: l.canonical_hash)

    # Step 3: Deduplicate — same canonical_hash → keep highest confidence
    legions = _dedup_legions(legions)

    # Step 4: Convert to backward-compatible dicts
    return [l.to_dict() for l in legions]
```

### 5.2 Canonical Hash Function

```python
def _compute_canonical_hash(file_path, line_number, dc_code, legion_code, matched_pattern):
    """
    SHA256-based deterministic identifier.

    Input normalization:
      - matched_pattern: None → "" (empty string)
      - All inputs are UTF-8 encoded before hashing
      - No locale-specific transforms (sort order, case folding)

    Output: first 16 hex characters of the SHA256 digest.
    """
    key = f"{dc_code}:{legion_code}:{file_path}:{line_number}:{matched_pattern or ''}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]
```

**Stability contract:** The key format `"DC:LEGION:FILE:LINE:PATTERN"` is frozen at schema version `1.0`. Changes to this format require a version bump to `"1.1"` and a migration utility.

### 5.3 Determinism Guarantee

> **Given identical source files and identical configuration (LEGION_DETECTION_PATTERNS.json and dc_classes_complete.json), Legion extraction is deterministic: the same set of canonical_hashes is produced on every run, in every environment, by every conforming implementation.**

This guarantee holds because:
- Heuristic order is fixed (not data-structure-dependent)
- The canonical hash is a pure function of (dc_code, legion_code, file_path, line_number, matched_pattern)
- The pre-dedup sort uses `canonical_hash` as the key — no tie-breaking by insertion order
- All string comparisons use literal equality (no locale collation)

---

## 6. Lifecycle Management

### 6.1 Deduplication

```python
def _dedup_legions(legions: list[Legion]) -> list[Legion]:
    """
    Deduplication rule:
      - Two Legions with the same canonical_hash are the same finding
      - When duplicates exist, keep the one with the highest confidence_float
      - Input order (post-sort) is otherwise preserved

    This ensures that if _match_agent_handovers (HIGH) and
    _match_keyword_legions (SPECULATIVE) both detect the same pattern
    at the same location, only the HIGH-confidence instance appears
    in the output.
    """
```

### 6.2 Confidence Updates

```python
def _update_legion_confidence(legion: Legion, new_evidence: list[EvidenceNode]) -> None:
    """
    Called when a retrace or incremental scan surfaces new evidence
    for an already-detected Legion.

    Rules:
    - Confidence is monotonically non-decreasing (never lowered)
    - new_evidence confidence → max(new_evidence[i].confidence)
    - If max(new_evidence) <= legion.confidence_float: no-op
    - legion.last_updated is set to UTC now on any change
    - Label (HIGH/MEDIUM/SPECULATIVE) is derived from confidence_float:
        >= 0.8 → HIGH
        >= 0.5 → MEDIUM
        <  0.5 → SPECULATIVE
    """
```

### 6.3 Versioning

Every `Legion` instance carries `version = "1.0"`. This field identifies the schema version used when the Legion was created. Consumers should:
- Reject Legions with unknown version strings
- Apply migration logic for Legions with version `< current`
- Treat `version = None` or missing as `"0.9"` (pre-schema Legions from earlier scan passes)

---

## 7. Output Contract

`results["legion_matches"]` is a `list[dict]`. Each dict is produced by `Legion.to_dict()` and contains:

**Legacy keys** (present since v0.2.0 — do not remove):
```
dc_code, dc_name, tier, legion_code, legion_name, location,
confidence, evidence, matched_pattern, heuristic_description, primary_so
```

**New schema keys** (added in v0.4.0):
```
id, description, detection_method, confidence_float, evidence_type,
file_path, line_number, observability_level, canonical_hash, version,
false_positive_conditions, false_negative_conditions, created_at, last_updated
```

Consumers that only read legacy keys continue to work without modification. New consumers should read `canonical_hash` for deduplication and `confidence_float` for numeric comparisons.

---

## 8. False Positive and False Negative Conditions

Each Legion entry in `LEGION_DETECTION_PATTERNS.json` may carry:

- `false_positive_conditions`: list of strings describing code patterns where this Legion fires but drift is not actually present (e.g. "confidence gate followed by a correctness check outside the detection window")
- `false_negative_conditions`: list of strings describing situations where drift is present but the Legion does not fire (e.g. "confidence score passed as a function argument rather than checked inline")

These are surfaced in `Legion.false_positive_conditions` and `Legion.false_negative_conditions` and are intended to guide human reviewers when evaluating SPECULATIVE matches.

---

## 9. Test Coverage

The following tests verify the operational semantics described in this document:

| Test | What it verifies |
|---|---|
| `TestLegionSchema::test_legion_schema_serializable` | `Legion.to_dict()` contains all legacy + new keys; JSON-serializable |
| `TestLegionSchema::test_evidence_extraction_deterministic` | Same primitives → same EvidenceNode canonical_hashes |
| `TestLegionSchema::test_legion_canonical_hash_deterministic` | `_compute_canonical_hash` is a pure function; different inputs → different hashes |
| `TestLegionSchema::test_dedup_keeps_highest_confidence` | `_dedup_legions` keeps highest confidence_float; different hashes → both kept |

Run: `python -m pytest test_matrix.py::TestLegionSchema -v`
