# X-Verba — Empirical Findings Summary
*Scanned by Super Semantics — supersemantics.org*
*Reproduce any result: pip install x-verba*
*github.com/4vish/x-verba*

---

## The Pattern

10 repos scanned. 10 repos scored Γ = 0.0 (or 0.01).
1 intentionally governed baseline scored Γ = 1.0.
The tool is calibrated. The results are real. Anyone can verify them.

| Repo | Owner | Files | AI Calls | Critical | Γ |
|------|-------|-------|----------|----------|---|
| **Governed baseline** | Super Semantics | 1 | 2 | 0 | **1.0** |
| LangChain | LangChain AI | 1,698 | 296 | 236 | 0.0 |
| AutoGen | Microsoft | 763 | 70 | 64 | 0.0 |
| Semantic Kernel | Microsoft | 2,584 | 251 | 193 | 0.0 |
| CrewAI | CrewAI Inc | 779 | 128 | 161 | 0.0 |
| OpenAI SDK | OpenAI | 1,054 | 8 | 14 | 0.0 |
| Anthropic SDK | Anthropic | 554 | 9 | 8 | 0.0 |
| Dify | LangGenius | 5,357 | 786 | 767 | 0.01 |
| LeRobot | HuggingFace | 332 | 172 | 155 | 0.0 |
| Weaviate Verba | Weaviate | 243 | 18 | 21 | 0.0 |
| SAFi | jnamaya | 117 | 31 | 41 | 0.0 |

**Reproduce it yourself:**
```bash
pip install x-verba
git clone https://github.com/langchain-ai/langchain.git
python -m x_verba.cli scan ./langchain
```

---

## What Γ = 0.0 means

Structural Gamma = Governed Decision Points / Total Decision Points.

Every AI call is a decision point. It is governed when a mandatory
checkpoint fires immediately before it — validating input, checking
conditions, and blocking execution if they are not met.

Γ = 0.0 — zero decision points are governed.
Γ = 1.0 — every decision point has a checkpoint.
Threshold for sufficiency: Γ ≥ 0.9.

---

## Finding-by-finding breakdown

---

### 1. LangChain — LangChain AI — 112k stars
**Γ = 0.0 | 1,698 files | 296 AI calls | 236 critical**

**Finding 1** — `chat_models.py:1185` CRITICAL
AI call fires with no checkpoint before it. Any input reaches the
model unfiltered. Output flows to the next AI call with no validation.
No governance record exists at any point in the chain.

**Finding 2** — `llms.py:791` CRITICAL
AI output flows directly to next AI call. One corrupted output seeds
the next automatically. DC-E13 Propagating Corruption — the same
pattern that produced cascading failures in the Flash Crash.

**Finding 3** — `base.py:97` HIGH
Every AI output reaches its destination automatically. No human
review. No authorisation gate. No audit trail. 296 times.

**What this means:** Every application built on LangChain inherits
Γ = 0.0 as its starting point. Governance must be added manually
by every developer, every time. None of it is structural.

---

### 2. AutoGen — Microsoft — 54k stars
**Γ = 0.0 | 763 files | 70 AI calls | 64 critical**

**Finding 1** — `agbench/linter/cli.py:66` CRITICAL
AI call fires with no checkpoint. Output flows directly to
user-facing response. No sanitisation. No review. No record.

**Finding 2** — `agbench/linter/coders/oai_coder.py:26` CRITICAL
AI call in a code generation context with no eligibility condition.
Generated code reaches downstream processing unchecked.

**Finding 3** — `autogen_agentchat/teams/_group_chat/_chat_agent_container.py:91` CRITICAL
Agent group chat fires AI calls with no Pre-Node. Multiple agents
chained together, none governed at the decision point level.

**What this means:** Microsoft's multi-agent framework has no
structural governance at any agent-to-agent handoff point.
Every agent transition is ungoverned.

---

### 3. Semantic Kernel — Microsoft — 24k stars
**Γ = 0.0 | 2,584 files | 251 AI calls | 193 critical**

**Finding 1** — `kernel.py:512` CRITICAL
The core kernel itself fires AI calls with no Pre-Node. This is
the foundation every Semantic Kernel application is built on.
Every application inherits this structural gap.

**Finding 2** — `azure_ai/agent_thread_actions.py:842` CRITICAL
Azure AI agent fires with no checkpoint. Enterprise Azure
deployments built on Semantic Kernel are affected at the base.

**Finding 3** — `bedrock/bedrock_agent_base.py:72` CRITICAL
AWS Bedrock agent base class — no checkpoint. Every Bedrock
agent built on this class inherits Γ = 0.0 structurally.

**What this means:** Microsoft has two major AI frameworks.
Both score Γ = 0.0. The gap is structural across the entire
Microsoft AI product line.

---

### 4. CrewAI — CrewAI Inc — 44k stars
**Γ = 0.0 | 779 files | 128 AI calls | 161 critical**

**Finding 1** — `crew.py:1683` CRITICAL
The core crew orchestrator fires AI calls with no checkpoint.
Every crew, every agent, every task inherits this gap.

**Finding 2** — `__init__.py:175` CRITICAL
AI call in the package initialisation itself. Fires when the
package is imported. No conditions. No gate. No record.

**Finding 3** — `agent/core.py:1383` CRITICAL
Individual agent core fires with no Pre-Node. Output flows
to user-facing response automatically. 161 critical gaps total.

**What this means:** CrewAI's role-playing agent architecture
has no governance at any decision point. Every role, every
task, every output is structurally ungoverned.

---

### 5. OpenAI Python SDK — OpenAI — 25k stars
**Γ = 0.0 | 1,054 files | 8 AI calls | 14 critical**

**Finding 1** — `lib/_realtime.py:43` CRITICAL
Realtime AI call with no Pre-Node. User input flows directly
into the realtime stream with no sanitisation checkpoint.

**Finding 2** — `lib/_realtime.py:80` CRITICAL
Second realtime call. No checkpoint between calls.
Output of first may seed the second without validation.

**Finding 3** — `lib/_realtime.py:38` CRITICAL
Four ungoverned realtime calls in the same file, in sequence.
No validation between any of them.

**What this means:** OpenAI's own SDK — the package millions
of developers import — has no structural governance before
its own API calls.

---

### 6. Anthropic Python SDK — Anthropic
**Γ = 0.0 | 554 files | 9 AI calls | 8 critical**

Anthropic publishes more AI safety research than any company
in the world. Their own SDK has no structural governance before
their own API calls.

**Finding 1** — `anthropic/_client.py:384` CRITICAL
Core client fires AI call with no checkpoint. Every application
built on the Anthropic SDK inherits this structural gap.

**Finding 2** — `anthropic/_client.py:388` CRITICAL
Second call four lines later. No validation between them.
Both reach downstream processing automatically.

**Finding 3** — `lib/aws/_auth.py:24` CRITICAL
AWS authentication layer fires with no checkpoint.
Infrastructure-level AI call with no Pre-Node.

**What this means:** Constitutional AI governs the model.
Nothing governs the code that calls it.

---

### 7. Dify — LangGenius — 129k stars
**Γ = 0.01 | 5,357 files | 786 AI calls | 767 critical**

The largest repo scanned. 786 AI calls. 767 critical findings.
Γ = 0.01 — one decision point governed out of 786.

**Finding 1** — `api/commands/plugin.py:473` CRITICAL
Plugin command fires AI call with no checkpoint. Output flows
to downstream processing. Same location flagged twice —
two separate ungoverned calls at the same line.

**Finding 2** — `api/controllers/console/apikey.py:94` CRITICAL
AI call output flows directly to a database write with no human
review. Ungated irreversible action triggered by AI output.

**Finding 3** — `api/controllers/console/app/completion.py:101` HIGH
AI output flows to next AI call with no validation.
Then again at line 180. Chained ungoverned calls throughout.

**What this means:** 129k stars. Used in production worldwide.
767 critical governance gaps. Γ = 0.01.

---

### 8. LeRobot — HuggingFace — Physical Robotics
**Γ = 0.0 | 332 files | 172 AI calls | 155 critical**

This is not a chat application. This is AI governing physical robots.
Real actuators. Real-world consequences. Γ = 0.0.

**Finding 1** — `async_inference/policy_server.py:324` CRITICAL
The policy server — the component deciding what physical actions
a robot takes — fires with no Pre-Node. Robot actions are
determined by ungoverned AI output.

**Finding 2** — `cameras/realsense/camera_realsense.py:177` CRITICAL
Camera input feeds directly into AI processing with no checkpoint.
Physical sensor data reaches AI with no validation.

**Finding 3** — `cameras/realsense/camera_realsense.py:175` CRITICAL
Two ungoverned calls at lines 175 and 177. Real-world sensor
data, real-world robot actions, zero governance at any decision
point.

**What this means:** The governance gap is not theoretical when
the output controls a physical robot.

---

### 9. Weaviate Verba RAG — Weaviate
**Γ = 0.0 | 243 files | 18 AI calls | 21 critical**

**Finding 1** — `goldenverba/verba_manager.py:743` CRITICAL
Core RAG manager fires AI call with no checkpoint. Retrieved
documents flow directly into the AI prompt with no source
validation. DC-E3 Signal Corruption risk.

**Finding 2** — `components/managers.py:535` CRITICAL
Component manager fires with no Pre-Node. Output flows to
downstream processing automatically.

**Finding 3** — `components/managers.py:368` HIGH
AI output flows directly to a database write with no human
review. Retrieved content to AI to database — no checkpoint
anywhere in that chain.

**What this means:** RAG systems are uniquely vulnerable.
External documents feed into AI calls. AI output writes to
databases. No governance at any point means corrupted
retrieval corrupts everything downstream.

---

### 10. SAFi — "Open-source runtime governance engine"
**Γ = 0.0 | 117 files | 31 AI calls | 41 critical**

SAFi explicitly claims to be a governance engine. It scored Γ = 0.0.
This is not a criticism of SAFi's intent. It is a structural finding.

**Finding 1** — `safi_app/tts.py:51` CRITICAL
TTS endpoint receives user text, passes it to SAFi constructor
with no Pre-Node checkpoint. SAFi's WillGate fires inside the
call — not before it. Governance at the Node, not the Pre-Node.

**Finding 2** — `safi_app/api/conversations.py:279` CRITICAL
Conversation API fires AI call with no Pre-Node. Output flows
to user-facing response automatically.

**Finding 3** — `safi_app/core/orchestrator.py:131` CRITICAL
The core orchestrator fires at line 131 with no checkpoint.
Then again at line 137. Two ungoverned calls in the core.

**What this means:** SAFi governs at the Node — it evaluates
outputs after the AI call. VERBA governs at the Pre-Node —
before the call fires. SAFi has the right idea in the wrong place.

This is empirical evidence that pre-commitment governance
does not yet exist anywhere — including in systems explicitly
designed for governance.

---

## The conclusion

1,776 AI integration points scanned across 10 repos.
1,673 critical or high severity governance gaps detected.
Structural Gamma across all repos: 0.0 (or 0.01).

The entire AI framework ecosystem governs by reaction.
Callbacks, tracing, monitoring, output evaluation — all fire
after the AI call has already committed.

VERBA governs by prevention. The Pre-Node fires before
commitment — at the saddle point where governance has
maximum leverage and minimum cost.

X-Verba detects the absence of that checkpoint.
Structurally. From the code. Reproducibly. On any machine.

The gap is real. The tool finds it. The evidence is public.

---

*Super Semantics — Governance proven, not claimed.*
*supersemantics.org | github.com/4vish/x-verba*
*pip install x-verba*
