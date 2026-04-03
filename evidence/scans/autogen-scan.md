# X-Verba Governance Report
*Generated 2026-04-03T07:27:18.798990+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\autogen`  
**Identity Key:** `autogen-012d2d8e`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **763 files** and found **70 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **64** |
| High findings | 70 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.0 (below threshold) |

---

## Governance gaps

### 🔴 CRITICAL — `python\packages\agbench\src\agbench\linter\cli.py:66`

No checkpoint exists before the AI call at python\packages\agbench\src\agbench\linter\cli.py:66. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\agbench\src\agbench\linter\cli.py:66`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:26`

No checkpoint exists before the AI call at python\packages\agbench\src\agbench\linter\coders\oai_coder.py:26. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:26`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:54`

No checkpoint exists before the AI call at python\packages\agbench\src\agbench\linter\coders\oai_coder.py:54. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:54`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:159`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_chat_agent_container.py:91`

No checkpoint exists before the AI call at python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_chat_agent_container.py:91. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_chat_agent_container.py:91`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:139`

No checkpoint exists before the AI call at python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:139. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:139`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:141`

No checkpoint exists before the AI call at python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:141. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:882`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:882. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:882`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_agent.py:648`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_agent.py:648. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_agent.py:648`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:76`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:81`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:81. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:81`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:614`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:614. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:614`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:608`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:608. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:608`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:610`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:610. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:610`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:538`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:273`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:531`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:531. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:531`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:275`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:275. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:275`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\_string_similarity_map.py:109`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\_string_similarity_map.py:109. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\_string_similarity_map.py:109`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\apprentice.py:192`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\apprentice.py:192. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\apprentice.py:192`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:370`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\memory\redis\_redis_memory.py:220`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\memory\redis\_redis_memory.py:220. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\memory\redis\_redis_memory.py:220`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:104`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:1372`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:293`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:293. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:293`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:349`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:349. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:349`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:677`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:677. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:677`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:260`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:271`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:271. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:271`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:897`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:897. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:897`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:212`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:212. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:212`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:215`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:215. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:215`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:602`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:820`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:217`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:217. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:217`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:393`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:393. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:393`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:397`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:397. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:397`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:493`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:493. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:493`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:496`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:496. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:496`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:635`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:635. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:635`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:743`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:743. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:743`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:176`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:176. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:176`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:444`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:444. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:444`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:233`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:233. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:233`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:128`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:128. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:128`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:134`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:134. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:134`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:96`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:256`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:256. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:256`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1090`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1090. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1090`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1118`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1118. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:544`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:684`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:684. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:684`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:694`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:694. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:694`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:258`

No checkpoint exists before the AI call at python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:258. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:258`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:547`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\tools\azure\_ai_search.py:173`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\tools\azure\_ai_search.py:183`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-ext\src\autogen_ext\tools\azure\_ai_search.py:203`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\database\schema_manager.py:541`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\database\schema_manager.py:541. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\database\schema_manager.py:541`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\database\schema_manager.py:66`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\gallery\builder.py:410`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\gallery\builder.py:410. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\gallery\builder.py:410`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:28`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:28. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:28`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:31`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:31. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:31`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:71`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:71. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:71`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:63`

No checkpoint exists before the AI call at python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:63. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:63`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `python\packages\agbench\src\agbench\run_cmd.py:467`

An irreversible action (system_command) at line 467 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_base_group_chat.py:534`

An irreversible action (email_send) at line 534 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_magentic_one\_magentic_one_orchestrator.py:266`

An irreversible action (email_send) at line 266 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-core\src\autogen_core\tool_agent\_caller_loop.py:50`

An irreversible action (email_send) at line 50 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:187`

An irreversible action (external_api) at line 187 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:226`

An irreversible action (file_system) at line 226 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\code_executors\docker_jupyter\_jupyter_server.py:167`

An irreversible action (email_send) at line 167 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-ext\src\autogen_ext\code_executors\docker_jupyter\_jupyter_server.py:110`

An irreversible action (database_delete) at line 110 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `python\packages\autogen-studio\autogenstudio\web\managers\connection.py:76`

An irreversible action (email_send) at line 76 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\agbench\src\agbench\linter\cli.py:66`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\agbench\src\agbench\linter\cli.py:66`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:26`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:54`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\agbench\src\agbench\linter\coders\oai_coder.py:54`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_chat_agent_container.py:91`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:139`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:139`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:141`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\ui\_console.py:141`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:882`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_agent.py:648`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:81`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:614`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:608`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:610`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:531`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:531`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:275`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\openai\_openai_assistant_agent.py:533`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\_string_similarity_map.py:109`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\_string_similarity_map.py:109`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\apprentice.py:192`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\apprentice.py:192`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\experimental\task_centric_memory\utils\teachability.py:74`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\chromadb\_chromadb.py:323`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\mem0\_mem0.py:387`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\redis\_redis_memory.py:220`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\memory\redis\_redis_memory.py:220`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:293`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:349`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:677`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:271`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:271`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:897`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:212`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:212`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:215`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:215`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:217`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\anthropic\_anthropic_client.py:217`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:393`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:397`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:493`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\azure\_azure_ai_client.py:496`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:635`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:635`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:743`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\ollama\_ollama_client.py:743`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:176`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:444`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:233`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_message_transform.py:233`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:128`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:128`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:134`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:134`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:96`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:256`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1090`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:1118`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:684`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:694`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-ext\src\autogen_ext\models\openai\_openai_client.py:258`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\database\schema_manager.py:541`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\database\schema_manager.py:541`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\gallery\builder.py:410`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:28`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:28`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:31`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\gallery\tools\generate_image.py:31`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:71`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:71`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:63`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `python\packages\autogen-studio\autogenstudio\validation\component_test_service.py:63`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `70 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\agbench\src\agbench\run_cmd.py:467`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_base_group_chat.py:534`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-agentchat\src\autogen_agentchat\teams\_group_chat\_magentic_one\_magentic_one_orchestrator.py:266`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-core\src\autogen_core\tool_agent\_caller_loop.py:50`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:187`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-ext\src\autogen_ext\agents\azure\_azure_ai_agent.py:226`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-ext\src\autogen_ext\code_executors\docker_jupyter\_jupyter_server.py:167`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-ext\src\autogen_ext\code_executors\docker_jupyter\_jupyter_server.py:110`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `python\packages\autogen-studio\autogenstudio\web\managers\connection.py:76`

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