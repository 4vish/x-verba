# X-Verba Governance Report
*Generated 2026-04-03T08:32:45.100240+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\Verba`  
**Identity Key:** `Verba-a47a7b56`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **243 files** and found **18 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **21** |
| High findings | 18 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.0 (below threshold) |

---

## Governance gaps

### 🔴 CRITICAL — `goldenverba\verba_manager.py:743`

No checkpoint exists before the AI call at goldenverba\verba_manager.py:743. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\verba_manager.py:743`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:473`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:860`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:881`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:368`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:458`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\managers.py:535`

No checkpoint exists before the AI call at goldenverba\components\managers.py:535. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\components\managers.py:535`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\managers.py:543`

No checkpoint exists before the AI call at goldenverba\components\managers.py:543. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\components\managers.py:543`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:567`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:596`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:622`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\managers.py:793`

No checkpoint exists before the AI call at goldenverba\components\managers.py:793. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\components\managers.py:793`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\managers.py:802`

No checkpoint exists before the AI call at goldenverba\components\managers.py:802. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\components\managers.py:802`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:819`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:843`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\components\managers.py:657`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\generation\GeminiGenerator.py:70`

No checkpoint exists before the AI call at goldenverba\components\generation\GeminiGenerator.py:70. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `goldenverba\components\generation\GeminiGenerator.py:70`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `goldenverba\server\api.py:215`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `goldenverba\components\managers.py:484`

An irreversible action (database_delete) at line 484 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\514-cff62b6f7919676e.js:1`

An irreversible action (database_write) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\789-e4deefde6e1de3c8.js:1`

An irreversible action (database_write) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\864-15201e63d2e174b9.js:1`

An irreversible action (database_write) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\949-4b7f5a091d97fe2c.js:1`

An irreversible action (database_write) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-235aaff141d9263e.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-25ed1cb73822cf4e.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-345642b96638188b.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-5e9b74ed5a1be60e.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-63c3d501186e1569.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-8184afaea67792bd.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-e15dc604b4004fa4.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-f09784266b0febdd.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-f3aef3f90382cf14.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `goldenverba\server\frontend\out\_next\static\chunks\app\page-f7e98beb8ba64d62.js:1`

An irreversible action (database_delete) at line 1 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\verba_manager.py:743`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\components\managers.py:535`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\components\managers.py:543`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\components\managers.py:793`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\components\managers.py:802`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `goldenverba\components\generation\GeminiGenerator.py:70`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `18 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\components\managers.py:484`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\514-cff62b6f7919676e.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\789-e4deefde6e1de3c8.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\864-15201e63d2e174b9.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\949-4b7f5a091d97fe2c.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-235aaff141d9263e.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-25ed1cb73822cf4e.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-345642b96638188b.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-5e9b74ed5a1be60e.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-63c3d501186e1569.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-8184afaea67792bd.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-e15dc604b4004fa4.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-f09784266b0febdd.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-f3aef3f90382cf14.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `goldenverba\server\frontend\out\_next\static\chunks\app\page-f7e98beb8ba64d62.js:1`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

---

## Governance score

**Structural Gamma proxy:** 0.0

Only 0% of decision points are governed. The system is structurally ungoverned. The Drift Node is the global energy minimum.

> Structural proxy only — not runtime Gamma. Measures whether governance mechanisms are structurally present.

---

## Next steps

1. Fill in the null fields in `.verba/governance.yaml`
2. Complete the test stubs in `.verba/test_case_matrix.yaml`
3. Open in Verba Studio for AI-assisted policy authoring
4. Add `x-verba qa . --schema .verba/governance.yaml` to your CI/CD pipeline (coming v0.2)

*Generated by X-Verba — https://github.com/4vish/x-verba*