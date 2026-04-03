# X-Verba Governance Report
*Generated 2026-04-03T07:43:29.034738+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\crewAI`  
**Identity Key:** `crewAI-484622e0`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **779 files** and found **128 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **161** |
| High findings | 126 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.0 (below threshold) |

---

## Governance gaps

### 🔴 CRITICAL — `lib\crewai\src\crewai\crew.py:1683`

No checkpoint exists before the AI call at lib\crewai\src\crewai\crew.py:1683. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\crew.py:1683`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\__init__.py:175`

No checkpoint exists before the AI call at lib\crewai\src\crewai\__init__.py:175. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\__init__.py:175`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\__init__.py:175`

No checkpoint exists before the AI call at lib\crewai\src\crewai\__init__.py:175. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\__init__.py:175`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\agent\core.py:1383`

No checkpoint exists before the AI call at lib\crewai\src\crewai\agent\core.py:1383. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\agent\core.py:1383`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:200`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:200. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:214`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:214. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:288`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:288. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:288`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:298`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:298. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:298`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:312`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:312. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:312`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:361`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:361. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:361`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:164`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:164. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:164`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:165`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:165. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:165`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:354`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:354. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:354`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:397`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:397. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:397`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\memory_tui.py:375`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\memory_tui.py:375. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\memory_tui.py:375`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\shared\token_manager.py:40`

No checkpoint exists before the AI call at lib\crewai\src\crewai\cli\shared\token_manager.py:40. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\cli\shared\token_manager.py:40`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\experimental\agent_executor.py:232`

No checkpoint exists before the AI call at lib\crewai\src\crewai\experimental\agent_executor.py:232. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\experimental\agent_executor.py:232`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:191`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:191. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:191`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:199`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:199. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:199`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:766`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:766. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:766`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:909`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:909. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:909`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:942`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:942. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:942`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1295`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1295. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1295`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1459`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1459. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1459`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:788`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:788. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:788`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1317`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1317. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1317`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\azure\completion.py:915`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\azure\completion.py:915. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\azure\completion.py:915`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\azure\completion.py:716`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\azure\completion.py:716. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\azure\completion.py:716`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\azure\completion.py:982`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\azure\completion.py:982. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\azure\completion.py:982`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\azure\completion.py:956`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\azure\completion.py:956. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\azure\completion.py:956`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:309`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\bedrock\completion.py:309. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:309`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:2122`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\bedrock\completion.py:2122. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:2122`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1155`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\gemini\completion.py:1155. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1155`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1114`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\gemini\completion.py:1114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1114`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1234`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\gemini\completion.py:1234. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1234`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1193`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\gemini\completion.py:1193. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1193`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:248`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:248. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:248`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:256`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:256. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:256`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1865`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1865. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1865`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1603`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1603. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1603`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:2163`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:2163. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:2163`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1579`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1579. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1579`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1828`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1828. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1828`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1986`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1986. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1986`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:2107`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:2107. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:2107`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1962`

No checkpoint exists before the AI call at lib\crewai\src\crewai\llms\providers\openai\completion.py:1962. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\llms\providers\openai\completion.py:1962`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:321`

No checkpoint exists before the AI call at lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:321. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:321`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai\src\crewai\rag\chromadb\client.py:459`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai\src\crewai\rag\chromadb\client.py:522`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\rag\embeddings\providers\aws\bedrock.py:26`

No checkpoint exists before the AI call at lib\crewai\src\crewai\rag\embeddings\providers\aws\bedrock.py:26. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\rag\embeddings\providers\aws\bedrock.py:26`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\rag\qdrant\client.py:374`

No checkpoint exists before the AI call at lib\crewai\src\crewai\rag\qdrant\client.py:374. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\rag\qdrant\client.py:374`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\rag\qdrant\client.py:427`

No checkpoint exists before the AI call at lib\crewai\src\crewai\rag\qdrant\client.py:427. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai\src\crewai\rag\qdrant\client.py:427`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai\src\crewai\security\security_config.py:52`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai\src\crewai\utilities\internal_instructor.py:148`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\anthropic.py:54`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\anthropic.py:54. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\anthropic.py:54`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\anthropic.py:68`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:230`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\bedrock.py:230. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:230`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:165`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\bedrock.py:165. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:165`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\openai.py:317`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\openai.py:317. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:317`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\openai.py:385`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\openai.py:385. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:385`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\openai.py:170`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\openai.py:170. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:170`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:184`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\openai.py:594`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\openai.py:594. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:594`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\uploaders\openai.py:662`

No checkpoint exists before the AI call at lib\crewai-files\src\crewai_files\uploaders\openai.py:662. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-files\src\crewai_files\uploaders\openai.py:662`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\adapters\lancedb_adapter.py:18`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\adapters\lancedb_adapter.py:18. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\adapters\lancedb_adapter.py:18`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\adapters\rag_adapter.py:31`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\adapters\rag_adapter.py:31. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\adapters\rag_adapter.py:31`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:109`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:121`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:121. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:121`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:171`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:171. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:171`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:422`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:422. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:422`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\bedrock\knowledge_base\retriever_tool.py:207`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\s3\reader_tool.py:33`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\aws\s3\writer_tool.py:34`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\core.py:176`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\core.py:176. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\core.py:176`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\csv_loader.py:63`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\csv_loader.py:63. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\csv_loader.py:63`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\directory_loader.py:86`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\directory_loader.py:86. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\directory_loader.py:86`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\docs_site_loader.py:115`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\docs_site_loader.py:115. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\docs_site_loader.py:115`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:82`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:82. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:82`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\github_loader.py:111`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\json_loader.py:56`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\json_loader.py:56. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\json_loader.py:56`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\mdx_loader.py:60`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\mdx_loader.py:60. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\mdx_loader.py:60`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:63`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\pdf_loader.py:126`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:62`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:21`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:30`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:30. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:30`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\webpage_loader.py:55`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\webpage_loader.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\webpage_loader.py:55`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\xml_loader.py:62`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\rag\loaders\xml_loader.py:62. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\xml_loader.py:62`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\youtube_channel_loader.py:147`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\rag\loaders\youtube_video_loader.py:102`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:89`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:89. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:89`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\contextualai_query_tool\contextual_query_tool.py:99`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\contextualai_query_tool\contextual_query_tool.py:99. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\contextualai_query_tool\contextual_query_tool.py:99`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:52`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:52. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:52`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:59`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:59. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:59`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\databricks_query_tool\databricks_query_tool.py:63`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\databricks_query_tool\databricks_query_tool.py:67`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\databricks_query_tool\databricks_query_tool.py:68`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:125`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:127`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\qdrant_vector_search_tool\qdrant_search_tool.py:122`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\qdrant_vector_search_tool\qdrant_search_tool.py:122. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\qdrant_vector_search_tool\qdrant_search_tool.py:122`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\rag\rag_tool.py:263`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\rag\rag_tool.py:263. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\rag\rag_tool.py:263`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\weaviate_tool\vector_search.py:129`

No checkpoint exists before the AI call at lib\crewai-tools\src\crewai_tools\tools\weaviate_tool\vector_search.py:129. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\crewai-tools\src\crewai_tools\tools\weaviate_tool\vector_search.py:129`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:377`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:377. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:377`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:824`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:824. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:824`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:872`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:872. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:872`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:1484`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:1484. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:1484`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:1598`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:1598. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:1598`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:837`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:837. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:837`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:71`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\cli.py:71. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\cli.py:71`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:172`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\docs_check.py:172. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\docs_check.py:172`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:185`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\docs_check.py:185. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\docs_check.py:185`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:230`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\docs_check.py:230. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\docs_check.py:230`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:270`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\docs_check.py:270. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\docs_check.py:270`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:306`

No checkpoint exists before the AI call at lib\devtools\src\crewai_devtools\docs_check.py:306. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `lib\devtools\src\crewai_devtools\docs_check.py:306`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\__init__.py:63`

An irreversible action (external_api) at line 63 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\a2a\config.py:179`

An irreversible action (email_send) at line 179 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\a2a\task_helpers.py:288`

An irreversible action (email_send) at line 288 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\a2a\updates\polling\handler.py:29`

An irreversible action (email_send) at line 29 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\a2a\updates\push_notifications\handler.py:24`

An irreversible action (email_send) at line 24 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\a2a\updates\streaming\handler.py:261`

An irreversible action (email_send) at line 261 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\agent\core.py:1227`

An irreversible action (system_command) at line 1227 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\agent\core.py:1233`

An irreversible action (system_command) at line 1233 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\cli.py:64`

An irreversible action (system_command) at line 64 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\cli.py:71`

An irreversible action (system_command) at line 71 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\evaluate_crew.py:20`

An irreversible action (system_command) at line 20 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\evaluate_crew.py:25`

An irreversible action (system_command) at line 25 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\kickoff_flow.py:13`

An irreversible action (system_command) at line 13 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\kickoff_flow.py:18`

An irreversible action (system_command) at line 18 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\plot_flow.py:13`

An irreversible action (system_command) at line 13 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\plot_flow.py:18`

An irreversible action (system_command) at line 18 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\replay_from_task.py:16`

An irreversible action (system_command) at line 16 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\replay_from_task.py:20`

An irreversible action (system_command) at line 20 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\reset_memories_command.py:101`

An irreversible action (system_command) at line 101 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\run_crew.py:61`

An irreversible action (system_command) at line 61 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\run_crew.py:63`

An irreversible action (system_command) at line 63 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\train_crew.py:22`

An irreversible action (system_command) at line 22 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\train_crew.py:27`

An irreversible action (system_command) at line 27 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\authentication\main.py:101`

An irreversible action (external_api) at line 101 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\tools\main.py:83`

An irreversible action (database_write) at line 83 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\tools\main.py:71`

An irreversible action (system_command) at line 71 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\cli\triggers\main.py:129`

An irreversible action (system_command) at line 129 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\events\listeners\tracing\utils.py:230`

An irreversible action (system_command) at line 230 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\flow\persistence\sqlite.py:296`

An irreversible action (database_delete) at line 296 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\mcp\transports\stdio.py:51`

An irreversible action (system_command) at line 51 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\encoding_flow.py:420`

An irreversible action (database_write) at line 420 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\unified_memory.py:795`

An irreversible action (database_delete) at line 795 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\storage\kickoff_task_outputs_storage.py:219`

An irreversible action (database_delete) at line 219 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\storage\kickoff_task_outputs_storage.py:62`

An irreversible action (database_write) at line 62 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\storage\lancedb_storage.py:128`

An irreversible action (database_write) at line 128 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:685`

An irreversible action (file_system) at line 685 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai\src\crewai\rag\chromadb\types.py:42`

An irreversible action (database_write) at line 42 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-files\src\crewai_files\cache\cleanup.py:99`

An irreversible action (database_delete) at line 99 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:27`

An irreversible action (file_system) at line 27 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\arxiv_paper_tool\arxiv_paper_tool.py:85`

An irreversible action (external_api) at line 85 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\code_interpreter_tool\code_interpreter_tool.py:286`

An irreversible action (system_command) at line 286 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\code_interpreter_tool\code_interpreter_tool.py:294`

An irreversible action (system_command) at line 294 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\generate_crewai_automation_tool\generate_crewai_automation_tool.py:52`

An irreversible action (external_api) at line 52 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\invoke_crewai_automation_tool\invoke_crewai_automation_tool.py:128`

An irreversible action (external_api) at line 128 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\nl2sql\nl2sql_tool.py:88`

An irreversible action (database_write) at line 88 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\parallel_tools\parallel_search_tool.py:104`

An irreversible action (external_api) at line 104 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\patronus_eval_tool\patronus_eval_tool.py:146`

An irreversible action (external_api) at line 146 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\patronus_eval_tool\patronus_predefined_criteria_eval_tool.py:95`

An irreversible action (external_api) at line 95 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\serper_dev_tool\serper_dev_tool.py:257`

An irreversible action (external_api) at line 257 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\serper_scrape_website_tool\serper_scrape_website_tool.py:59`

An irreversible action (external_api) at line 59 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\singlestore_search_tool\singlestore_search_tool.py:149`

An irreversible action (database_write) at line 149 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\crewai-tools\src\crewai_tools\tools\snowflake_search_tool\snowflake_search_tool.py:154`

An irreversible action (system_command) at line 154 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:115`

An irreversible action (database_write) at line 115 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:44`

An irreversible action (system_command) at line 44 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\cli.py:42`

An irreversible action (system_command) at line 42 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `lib\devtools\src\crewai_devtools\docs_check.py:156`

An irreversible action (system_command) at line 156 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\crew.py:1683`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\crew.py:1683`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\__init__.py:175`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\agent\core.py:1383`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:200`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:200`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:214`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:214`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:288`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:288`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:288`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:298`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:298`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:298`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:312`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:312`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:361`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:361`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:164`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:165`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:354`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:354`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:397`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:397`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\memory_tui.py:375`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\cli\shared\token_manager.py:40`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\experimental\agent_executor.py:232`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:191`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:199`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:766`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:766`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:909`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:909`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:942`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:942`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1221`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1295`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1295`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1426`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1459`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1459`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:788`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:788`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:792`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1624`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1317`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1317`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\anthropic\completion.py:1321`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\azure\completion.py:915`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\azure\completion.py:716`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\azure\completion.py:982`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\azure\completion.py:956`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:309`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\bedrock\completion.py:2122`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1155`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1234`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\gemini\completion.py:1193`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:248`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:256`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1865`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1603`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:2163`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:2163`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1579`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1828`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1986`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:2107`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\llms\providers\openai\completion.py:1962`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:321`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\rag\embeddings\providers\aws\bedrock.py:26`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\rag\qdrant\client.py:374`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\rag\qdrant\client.py:374`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai\src\crewai\rag\qdrant\client.py:427`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai\src\crewai\rag\qdrant\client.py:427`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\anthropic.py:54`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:230`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:230`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\bedrock.py:165`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:317`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:317`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:385`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:385`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:170`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:594`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:594`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:662`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-files\src\crewai_files\uploaders\openai.py:662`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\adapters\lancedb_adapter.py:18`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\adapters\rag_adapter.py:31`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\agents\invoke_agent_tool.py:126`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:121`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:121`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:171`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_session_manager.py:171`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:422`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:422`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\aws\bedrock\browser\browser_toolkit.py:444`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\core.py:176`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\core.py:176`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\core.py:176`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\csv_loader.py:63`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\csv_loader.py:63`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\directory_loader.py:86`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\directory_loader.py:86`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\docs_site_loader.py:115`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\docs_site_loader.py:115`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:82`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:82`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\json_loader.py:56`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\mdx_loader.py:60`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\mysql_loader.py:95`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\postgres_loader.py:94`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:30`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\text_loader.py:30`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\webpage_loader.py:55`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\webpage_loader.py:55`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\xml_loader.py:62`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:89`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\ai_mind_tool\ai_mind_tool.py:89`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\contextualai_query_tool\contextual_query_tool.py:99`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\contextualai_query_tool\contextual_query_tool.py:99`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:52`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\dalle_tool\dalle_tool.py:59`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:301`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\mongodb_vector_search_tool\vector_search.py:305`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\qdrant_vector_search_tool\qdrant_search_tool.py:122`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\rag\rag_tool.py:263`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\rag\rag_tool.py:263`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\weaviate_tool\vector_search.py:129`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:377`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:377`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:824`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:824`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:872`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:872`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:1484`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:1484`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:1598`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:837`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:837`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:71`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:172`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:172`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:185`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:185`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:230`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:230`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:270`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:270`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:306`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:306`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `128 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\__init__.py:63`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\a2a\config.py:179`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\a2a\task_helpers.py:288`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\a2a\updates\polling\handler.py:29`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\a2a\updates\push_notifications\handler.py:24`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\a2a\updates\streaming\handler.py:261`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\agent\core.py:1227`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\agent\core.py:1233`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\cli.py:64`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\cli.py:71`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\evaluate_crew.py:20`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\evaluate_crew.py:25`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\kickoff_flow.py:13`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\kickoff_flow.py:18`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\plot_flow.py:13`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\plot_flow.py:18`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\replay_from_task.py:16`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\replay_from_task.py:20`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\reset_memories_command.py:101`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\run_crew.py:61`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\run_crew.py:63`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\train_crew.py:22`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\train_crew.py:27`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\authentication\main.py:101`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\tools\main.py:83`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\tools\main.py:71`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\cli\triggers\main.py:129`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\events\listeners\tracing\utils.py:230`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\flow\persistence\sqlite.py:296`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\mcp\transports\stdio.py:51`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\encoding_flow.py:420`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\unified_memory.py:795`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\storage\kickoff_task_outputs_storage.py:219`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\storage\kickoff_task_outputs_storage.py:62`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\storage\lancedb_storage.py:128`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\memory\storage\qdrant_edge_storage.py:685`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai\src\crewai\rag\chromadb\types.py:42`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-files\src\crewai_files\cache\cleanup.py:99`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\rag\loaders\docx_loader.py:27`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\arxiv_paper_tool\arxiv_paper_tool.py:85`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\code_interpreter_tool\code_interpreter_tool.py:286`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\code_interpreter_tool\code_interpreter_tool.py:294`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\generate_crewai_automation_tool\generate_crewai_automation_tool.py:52`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\invoke_crewai_automation_tool\invoke_crewai_automation_tool.py:128`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\nl2sql\nl2sql_tool.py:88`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\parallel_tools\parallel_search_tool.py:104`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\patronus_eval_tool\patronus_eval_tool.py:146`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\patronus_eval_tool\patronus_predefined_criteria_eval_tool.py:95`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\serper_dev_tool\serper_dev_tool.py:257`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\serper_scrape_website_tool\serper_scrape_website_tool.py:59`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\singlestore_search_tool\singlestore_search_tool.py:149`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\crewai-tools\src\crewai_tools\tools\snowflake_search_tool\snowflake_search_tool.py:154`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:115`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:44`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\devtools\src\crewai_devtools\cli.py:42`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `lib\devtools\src\crewai_devtools\docs_check.py:156`

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