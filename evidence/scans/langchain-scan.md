# X-Verba Governance Report
*Generated 2026-04-03T07:11:44.936480+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\langchain`  
**Identity Key:** `langchain-203bbb36`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **1698 files** and found **296 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **236** |
| High findings | 296 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.0 (below threshold) |

---

## Governance gaps

### 🟡 HIGH — `libs\core\langchain_core\language_models\base.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\language_models\chat_models.py:1185`

No checkpoint exists before the AI call at libs\core\langchain_core\language_models\chat_models.py:1185. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\core\langchain_core\language_models\chat_models.py:1185`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\language_models\chat_models.py:454`

No checkpoint exists before the AI call at libs\core\langchain_core\language_models\chat_models.py:454. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\core\langchain_core\language_models\chat_models.py:454`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\language_models\llms.py:791`

No checkpoint exists before the AI call at libs\core\langchain_core\language_models\llms.py:791. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\core\langchain_core\language_models\llms.py:791`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\language_models\llms.py:433`

No checkpoint exists before the AI call at libs\core\langchain_core\language_models\llms.py:433. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\core\langchain_core\language_models\llms.py:433`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\language_models\llms.py:380`

No checkpoint exists before the AI call at libs\core\langchain_core\language_models\llms.py:380. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\core\langchain_core\language_models\llms.py:380`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\model_laboratory.py:79`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\model_laboratory.py:79. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\model_laboratory.py:79`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\model_laboratory.py:97`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\model_laboratory.py:97. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\model_laboratory.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:658`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:658. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:658`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:771`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:771. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:771`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:906`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:1204`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:1204. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:1204`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:1749`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:1749. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:1749`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:1780`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:1780. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:1780`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent.py:960`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent.py:960. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent.py:960`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\initialize.py:110`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\conversational_retrieval\openai_functions.py:78`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent_toolkits\conversational_retrieval\openai_functions.py:78. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent_toolkits\conversational_retrieval\openai_functions.py:78`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:103`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:103. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:103`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:110`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:217`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:217. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:217`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:224`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\chat\base.py:162`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\conversational\base.py:163`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\conversational_chat\base.py:170`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\mrkl\base.py:147`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:78`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:78. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:78`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:94`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:250`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:595`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:595. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:595`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:596`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:596. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:596`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:752`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:752. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:752`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:753`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:753. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:753`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:360`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:360. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:360`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:493`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_assistant\base.py:493. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_assistant\base.py:493`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\agents\structured_chat\base.py:147`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\example_generator.py:22`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\example_generator.py:22. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\example_generator.py:22`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\llm.py:117`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\llm.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm.py:117`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\llm.py:345`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\llm.py:345. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm.py:345`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\llm.py:129`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\llm.py:129. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm.py:129`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\llm.py:241`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\llm.py:241. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm.py:241`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:93`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:268`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:78`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:270`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\loading.py:322`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\loading.py:322. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:322`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\loading.py:326`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\loading.py:326. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\loading.py:326`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\mapreduce.py:61`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\mapreduce.py:61. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\mapreduce.py:61`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\mapreduce.py:112`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\mapreduce.py:112. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\mapreduce.py:112`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\moderation.py:74`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\moderation.py:75`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\sequential.py:173`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\api\base.py:284`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\api\base.py:306`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\api\base.py:372`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\api\base.py:372. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\api\base.py:372`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\api\base.py:374`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\api\base.py:374. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\api\base.py:374`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\combine_documents\reduce.py:321`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\combine_documents\reduce.py:321. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\combine_documents\reduce.py:321`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\combine_documents\refine.py:164`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\combine_documents\refine.py:164. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\combine_documents\refine.py:164`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\combine_documents\refine.py:169`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\combine_documents\refine.py:169. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\combine_documents\refine.py:169`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\combine_documents\stuff.py:266`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\combine_documents\stuff.py:266. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\combine_documents\stuff.py:266`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:228`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\constitutional_ai\base.py:228. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:228`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:229`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\constitutional_ai\base.py:229. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:229`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:255`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\constitutional_ai\base.py:255. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:255`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:271`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\constitutional_ai\base.py:271. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:271`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:290`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\constitutional_ai\base.py:290. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:290`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:483`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:483. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:483`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:567`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:567. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:567`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:177`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:177. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:177`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:135`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:135. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:135`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:154`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:154. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:154`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\flare\base.py:147`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\flare\base.py:147. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\flare\base.py:147`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\flare\base.py:278`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\flare\base.py:217`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\flare\base.py:217. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\flare\base.py:217`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\hyde\base.py:81`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\hyde\base.py:81. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\hyde\base.py:81`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\hyde\base.py:96`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\hyde\base.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\hyde\base.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_checker\base.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_checker\base.py:37`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_checker\base.py:42`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_checker\base.py:47`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_math\base.py:275`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\llm_math\base.py:314`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\llm_math\base.py:314. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_math\base.py:314`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_math\base.py:187`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_summarization_checker\base.py:40`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_summarization_checker\base.py:46`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_summarization_checker\base.py:52`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\llm_summarization_checker\base.py:58`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\natbot\base.py:121`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\natbot\base.py:121. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\natbot\base.py:121`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\base.py:134`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\citation_fuzzy_match.py:164`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\citation_fuzzy_match.py:164. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\citation_fuzzy_match.py:164`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:100`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\extraction.py:100. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:100`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:184`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\extraction.py:184. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:184`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\openapi.py:403`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\qa_with_structure.py:104`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\qa_with_structure.py:104. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\qa_with_structure.py:104`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:103`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\tagging.py:103. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:103`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:183`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\openai_functions\tagging.py:183. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:183`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_generation\base.py:99`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_generation\base.py:99. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_generation\base.py:99`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_generation\base.py:122`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_generation\base.py:122. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_generation\base.py:122`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:68`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\base.py:68. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:68`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:69`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\base.py:69. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:69`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:167`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\base.py:167. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:167`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:54`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:54. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:54`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:73`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:73. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:73`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:98`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:98. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:98`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:100`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:100. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:100`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:153`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:153`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:155`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:155. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:155`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\query_constructor\base.py:323`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:55`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:55`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:84`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:84`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:124`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:124. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:124`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:132`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:132. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:132`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:205`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:205. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:205`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\question_answering\chain.py:213`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\question_answering\chain.py:213. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:213`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\question_answering\chain.py:158`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:80`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\retrieval_qa\base.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:80`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:154`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\retrieval_qa\base.py:154. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:154`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\router\llm_router.py:137`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\router\llm_router.py:163`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\router\llm_router.py:163. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\router\llm_router.py:163`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\router\multi_prompt.py:182`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\router\multi_prompt.py:182. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\router\multi_prompt.py:182`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\summarize\chain.py:44`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\summarize\chain.py:44. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:44`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\summarize\chain.py:84`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\summarize\chain.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:84`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\summarize\chain.py:91`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\summarize\chain.py:91. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:91`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\summarize\chain.py:183`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\summarize\chain.py:183. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:183`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\chains\summarize\chain.py:185`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\chains\summarize\chain.py:185. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:185`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chains\summarize\chain.py:146`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:383`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:388`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:393`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:403`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:413`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:433`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\chat_models\base.py:471`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\base.py:214`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\base.py:218`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\base.py:226`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\base.py:226. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\base.py:226`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\base.py:234`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\base.py:234. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\base.py:234`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\cache.py:261`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\cache.py:261. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\cache.py:261`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\cache.py:256`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\cache.py:256. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\cache.py:256`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\cache.py:261`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\cache.py:261. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\cache.py:261`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\cache.py:279`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\cache.py:279. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\cache.py:279`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\embeddings\cache.py:284`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\embeddings\cache.py:284. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\embeddings\cache.py:284`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\evaluation\loading.py:168`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\evaluation\agents\trajectory_eval_chain.py:249`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\evaluation\agents\trajectory_eval_chain.py:298`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\evaluation\agents\trajectory_eval_chain.py:298. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\evaluation\agents\trajectory_eval_chain.py:298`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\evaluation\embedding_distance\base.py:72`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\indexes\vectorstore.py:137`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\indexes\vectorstore.py:67`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:421`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:462`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\indexes\_sql_record_manager.py:462. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:462`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:510`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\indexes\_sql_record_manager.py:510. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:510`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\buffer.py:62`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\buffer.py:62. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\buffer.py:62`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\buffer.py:72`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\buffer.py:72. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\buffer.py:72`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:77`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\chat_memory.py:100`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\chat_memory.py:100. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:100`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:77`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\chat_memory.py:100`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\chat_memory.py:100. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:100`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\chat_memory.py:91`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\chat_memory.py:91. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:91`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\chat_memory.py:104`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\chat_memory.py:104. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\chat_memory.py:104`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:609`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:609. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:609`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:513`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:513. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:513`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:532`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:532. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:532`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:592`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:592. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:592`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:609`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:609. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:609`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:598`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\entity.py:598. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\entity.py:598`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary.py:56`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary.py:56. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary.py:56`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary.py:57`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary.py:57. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary.py:57`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary.py:79`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary.py:79. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary.py:79`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary.py:160`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary.py:124`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary.py:124. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary.py:124`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary_buffer.py:69`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary_buffer.py:69. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary_buffer.py:69`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\summary_buffer.py:121`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\memory\summary_buffer.py:121. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\memory\summary_buffer.py:121`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\fix.py:81`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\fix.py:81. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\fix.py:81`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\fix.py:88`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\fix.py:88. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\fix.py:88`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\fix.py:97`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\fix.py:97. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\fix.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\retry.py:117`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\retry.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\retry.py:117`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\retry.py:122`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\retry.py:122. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\retry.py:122`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\retry.py:245`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\retry.py:245. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\retry.py:245`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\output_parsers\retry.py:251`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\output_parsers\retry.py:251. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\output_parsers\retry.py:251`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\multi_query.py:179`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\multi_query.py:179. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\multi_query.py:179`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\multi_query.py:199`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\multi_query.py:199. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\multi_query.py:199`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\re_phraser.py:76`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\re_phraser.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\re_phraser.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\document_compressors\chain_extract.py:78`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\document_compressors\chain_extract.py:78. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\document_compressors\chain_extract.py:78`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\document_compressors\cohere_rerank.py:59`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\self_query\base.py:316`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\self_query\base.py:316. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\self_query\base.py:316`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\retrievers\self_query\base.py:332`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\retrievers\self_query\base.py:332. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\retrievers\self_query\base.py:332`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:947`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:947. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:947`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:961`

No checkpoint exists before the AI call at libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:961. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:961`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1005`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1005. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1005`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1010`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1010. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1010`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1020`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1020. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1020`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1025`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1025. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1025`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1183`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1183. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1183`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1926`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1926. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1926`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:2058`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:2058. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:2058`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:2061`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:2061. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:2061`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1182`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1182. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1182`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1188`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1188. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1188`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1187`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1187. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1187`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1488`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1488. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1488`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1054`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\chat_models.py:1054. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\chat_models.py:1054`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:91`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\llms.py:291`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\llms.py:291. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:291`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\llms.py:327`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\llms.py:327. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:327`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\llms.py:367`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\llms.py:367. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:367`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\llms.py:412`

No checkpoint exists before the AI call at libs\partners\anthropic\langchain_anthropic\llms.py:412. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\anthropic\langchain_anthropic\llms.py:412`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\chroma\langchain_chroma\vectorstores.py:477`

No checkpoint exists before the AI call at libs\partners\chroma\langchain_chroma\vectorstores.py:477. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\chroma\langchain_chroma\vectorstores.py:477`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\deepseek\langchain_deepseek\chat_models.py:250`

No checkpoint exists before the AI call at libs\partners\deepseek\langchain_deepseek\chat_models.py:250. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\deepseek\langchain_deepseek\chat_models.py:250`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\deepseek\langchain_deepseek\chat_models.py:254`

No checkpoint exists before the AI call at libs\partners\deepseek\langchain_deepseek\chat_models.py:254. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\deepseek\langchain_deepseek\chat_models.py:254`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\fireworks\langchain_fireworks\embeddings.py:92`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:792`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:792. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:792`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1003`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1003. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1003`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:733`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:733. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:733`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:748`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:748. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:748`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:839`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:839. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:839`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:906`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:906. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:906`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:589`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:772`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:772. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:772`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:788`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:788. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:788`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1008`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1008. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1008`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:688`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:688. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:688`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:151`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:279`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:279. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:279`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:400`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:400. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:400`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:402`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:402. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:402`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:332`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:332. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:332`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:388`

No checkpoint exists before the AI call at libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:388. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:388`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\chat_models.py:946`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\chat_models.py:966`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\chat_models.py:968`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\chat_models.py:949`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\llms.py:356`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\ollama\langchain_ollama\llms.py:373`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\azure.py:690`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\azure.py:690. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\azure.py:690`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\azure.py:700`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\azure.py:700. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\azure.py:700`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\azure.py:709`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\azure.py:709. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\azure.py:709`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:4593`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:4593. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:4593`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1018`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1018. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1018`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1090`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:4851`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:4851. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:4851`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1068`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1396`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1396. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1396`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1460`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1460. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1460`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1655`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1655. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1655`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:4241`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:4241. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:4241`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1085`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1719`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1719. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1719`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1063`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\chat_models\base.py:1540`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\chat_models\base.py:1540. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\chat_models\base.py:1540`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\embeddings\azure.py:210`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\embeddings\azure.py:210. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\azure.py:210`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\embeddings\azure.py:222`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\embeddings\azure.py:222. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\azure.py:222`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\base.py:389`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\base.py:509`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\base.py:448`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\embeddings\base.py:432`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\llms\azure.py:179`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\llms\azure.py:179. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\llms\azure.py:179`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\llms\azure.py:191`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\llms\azure.py:191. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\llms\azure.py:191`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\llms\base.py:334`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\llms\base.py:334. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\llms\base.py:334`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\llms\base.py:337`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\llms\base.py:337. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\llms\base.py:337`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:433`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\middleware\openai_moderation.py:433. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:433`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:437`

No checkpoint exists before the AI call at libs\partners\openai\langchain_openai\middleware\openai_moderation.py:437. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:437`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openrouter\langchain_openrouter\chat_models.py:472`

No checkpoint exists before the AI call at libs\partners\openrouter\langchain_openrouter\chat_models.py:472. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openrouter\langchain_openrouter\chat_models.py:472`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openrouter\langchain_openrouter\chat_models.py:509`

No checkpoint exists before the AI call at libs\partners\openrouter\langchain_openrouter\chat_models.py:509. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openrouter\langchain_openrouter\chat_models.py:509`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openrouter\langchain_openrouter\chat_models.py:491`

No checkpoint exists before the AI call at libs\partners\openrouter\langchain_openrouter\chat_models.py:491. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openrouter\langchain_openrouter\chat_models.py:491`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\openrouter\langchain_openrouter\chat_models.py:595`

No checkpoint exists before the AI call at libs\partners\openrouter\langchain_openrouter\chat_models.py:595. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\openrouter\langchain_openrouter\chat_models.py:595`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\perplexity\langchain_perplexity\chat_models.py:424`

No checkpoint exists before the AI call at libs\partners\perplexity\langchain_perplexity\chat_models.py:424. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\perplexity\langchain_perplexity\chat_models.py:424`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\perplexity\langchain_perplexity\chat_models.py:600`

No checkpoint exists before the AI call at libs\partners\perplexity\langchain_perplexity\chat_models.py:600. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\perplexity\langchain_perplexity\chat_models.py:600`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\perplexity\langchain_perplexity\chat_models.py:513`

No checkpoint exists before the AI call at libs\partners\perplexity\langchain_perplexity\chat_models.py:513. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\perplexity\langchain_perplexity\chat_models.py:513`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\perplexity\langchain_perplexity\chat_models.py:657`

No checkpoint exists before the AI call at libs\partners\perplexity\langchain_perplexity\chat_models.py:657. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\perplexity\langchain_perplexity\chat_models.py:657`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\qdrant\langchain_qdrant\fastembed_sparse.py:80`

No checkpoint exists before the AI call at libs\partners\qdrant\langchain_qdrant\fastembed_sparse.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\fastembed_sparse.py:80`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\qdrant.py:671`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\qdrant\langchain_qdrant\qdrant.py:826`

No checkpoint exists before the AI call at libs\partners\qdrant\langchain_qdrant\qdrant.py:826. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\qdrant.py:826`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\qdrant\langchain_qdrant\qdrant.py:584`

No checkpoint exists before the AI call at libs\partners\qdrant\langchain_qdrant\qdrant.py:584. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\qdrant.py:584`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\qdrant\langchain_qdrant\qdrant.py:592`

No checkpoint exists before the AI call at libs\partners\qdrant\langchain_qdrant\qdrant.py:592. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\qdrant.py:592`

AI output flows to 'external API call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\partners\qdrant\langchain_qdrant\qdrant.py:605`

No checkpoint exists before the AI call at libs\partners\qdrant\langchain_qdrant\qdrant.py:605. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\partners\qdrant\langchain_qdrant\qdrant.py:605`

AI output flows to 'external API call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\xai\langchain_xai\chat_models.py:518`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\xai\langchain_xai\chat_models.py:524`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\xai\langchain_xai\chat_models.py:515`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `libs\partners\xai\langchain_xai\chat_models.py:521`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\integration_tests\chat_models.py:1543`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\integration_tests\chat_models.py:1543. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\integration_tests\chat_models.py:1543`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:71`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:71. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:71`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:935`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:935. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:935`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:982`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:982. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:982`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1097`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1097. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1097`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1119`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1119. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1119`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:961`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:961. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:961`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146`

No checkpoint exists before the AI call at libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\text-splitters\langchain_text_splitters\spacy.py:46`

No checkpoint exists before the AI call at libs\text-splitters\langchain_text_splitters\spacy.py:46. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `libs\text-splitters\langchain_text_splitters\spacy.py:46`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\indexing\api.py:248`

An irreversible action (database_delete) at line 248 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\core\langchain_core\runnables\configurable.py:360`

An irreversible action (database_write) at line 360 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\core\scripts\check_version.py:4`

An irreversible action (database_write) at line 4 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\hub.py:61`

An irreversible action (database_write) at line 61 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:22`

An irreversible action (external_api) at line 22 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:23`

An irreversible action (external_api) at line 23 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:19`

An irreversible action (external_api) at line 19 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:333`

An irreversible action (database_write) at line 333 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\memory\entity.py:437`

An irreversible action (database_delete) at line 437 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\runnables\hub.py:10`

An irreversible action (database_write) at line 10 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\tools\gmail\send_message.py:13`

An irreversible action (email_send) at line 13 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\tools\office365\send_message.py:13`

An irreversible action (email_send) at line 13 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain\langchain_classic\tools\slack\send_message.py:13`

An irreversible action (email_send) at line 13 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\langchain\agents\middleware\file_search.py:281`

An irreversible action (system_command) at line 281 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\langchain\agents\middleware\file_search.py:216`

An irreversible action (system_command) at line 216 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\langchain\agents\middleware\shell_tool.py:139`

An irreversible action (system_command) at line 139 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\langchain\agents\middleware\todo.py:112`

An irreversible action (system_command) at line 112 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\langchain\agents\middleware\_execution.py:34`

An irreversible action (system_command) at line 34 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\langchain_v1\scripts\check_version.py:5`

An irreversible action (database_write) at line 5 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\langchain_anthropic\middleware\anthropic_tools.py:1018`

An irreversible action (file_system) at line 1018 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\partners\anthropic\scripts\check_version.py:5`

An irreversible action (database_write) at line 5 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\integration_tests\chat_models.py:737`

An irreversible action (database_write) at line 737 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:868`

An irreversible action (database_write) at line 868 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\core\langchain_core\language_models\chat_models.py:1185`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\core\langchain_core\language_models\chat_models.py:454`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\core\langchain_core\language_models\chat_models.py:454`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\core\langchain_core\language_models\llms.py:791`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\core\langchain_core\language_models\llms.py:433`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\core\langchain_core\language_models\llms.py:380`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\model_laboratory.py:79`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\model_laboratory.py:97`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\model_laboratory.py:97`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:658`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:771`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:1204`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:1749`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:1780`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:960`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent.py:960`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\conversational_retrieval\openai_functions.py:78`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:103`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:103`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:217`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\vectorstore\base.py:217`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:78`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:595`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:596`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:752`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:753`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:360`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_assistant\base.py:493`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:83`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:92`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\agents\openai_functions_agent\agent_token_buffer_memory.py:91`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\example_generator.py:22`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\llm.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\llm.py:345`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\llm.py:129`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\llm.py:241`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\loading.py:322`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\loading.py:326`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\mapreduce.py:61`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\mapreduce.py:61`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\mapreduce.py:112`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\api\base.py:372`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\api\base.py:374`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\combine_documents\reduce.py:321`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\combine_documents\refine.py:164`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\combine_documents\refine.py:169`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\combine_documents\stuff.py:266`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:228`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:229`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:255`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:255`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:271`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:271`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\constitutional_ai\base.py:290`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:483`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:567`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:567`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\conversational_retrieval\base.py:177`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:135`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:135`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\elasticsearch_database\base.py:154`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\flare\base.py:147`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\flare\base.py:147`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\flare\base.py:217`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\flare\base.py:217`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\hyde\base.py:81`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\hyde\base.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\llm_math\base.py:314`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\natbot\base.py:121`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\citation_fuzzy_match.py:164`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:100`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\extraction.py:184`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\qa_with_structure.py:104`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:103`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\openai_functions\tagging.py:183`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_generation\base.py:99`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_generation\base.py:122`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:68`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:69`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\base.py:167`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:54`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:73`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:98`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:100`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\qa_with_sources\loading.py:155`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:55`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:124`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:132`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:205`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\question_answering\chain.py:213`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:80`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\retrieval_qa\base.py:154`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\router\llm_router.py:163`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\router\multi_prompt.py:182`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\router\multi_prompt.py:182`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\summarize\chain.py:44`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\summarize\chain.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\summarize\chain.py:91`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\summarize\chain.py:183`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\chains\summarize\chain.py:185`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\base.py:226`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\base.py:234`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\cache.py:261`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\cache.py:256`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\cache.py:279`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\embeddings\cache.py:284`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\evaluation\agents\trajectory_eval_chain.py:298`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:462`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:510`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\buffer.py:62`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\buffer.py:72`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\chat_memory.py:100`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\chat_memory.py:91`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\chat_memory.py:104`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:609`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:513`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:532`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:592`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:598`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary.py:56`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary.py:57`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary.py:79`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary.py:124`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary_buffer.py:69`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\memory\summary_buffer.py:121`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\fix.py:81`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\fix.py:88`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\fix.py:97`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\retry.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\retry.py:122`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\retry.py:245`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\output_parsers\retry.py:251`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\multi_query.py:179`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\multi_query.py:199`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\re_phraser.py:76`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\re_phraser.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\document_compressors\chain_extract.py:78`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\document_compressors\chain_extract.py:78`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\self_query\base.py:316`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\retrievers\self_query\base.py:332`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:947`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\langchain\langchain_classic\smith\evaluation\runner_utils.py:961`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1005`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1010`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1020`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1025`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1183`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1926`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:2058`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:2061`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1182`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1188`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1187`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1488`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\chat_models.py:1054`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:291`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:327`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:367`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:367`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:412`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\anthropic\langchain_anthropic\llms.py:412`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `libs\partners\chroma\langchain_chroma\vectorstores.py:477`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\chroma\langchain_chroma\vectorstores.py:477`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\deepseek\langchain_deepseek\chat_models.py:250`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\deepseek\langchain_deepseek\chat_models.py:254`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:792`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1003`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:733`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:748`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:839`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:906`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:772`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:788`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:1008`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:688`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\chat_models\huggingface.py:688`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:279`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:400`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:402`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:332`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\huggingface\langchain_huggingface\llms\huggingface_pipeline.py:388`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\azure.py:690`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\azure.py:700`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\azure.py:709`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:4593`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1018`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:4851`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1396`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1460`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1655`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:4241`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1719`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\chat_models\base.py:1540`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\embeddings\azure.py:210`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\embeddings\azure.py:222`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\llms\azure.py:179`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\llms\azure.py:191`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\llms\base.py:334`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\llms\base.py:337`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:433`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openai\langchain_openai\middleware\openai_moderation.py:437`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openrouter\langchain_openrouter\chat_models.py:472`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\partners\openrouter\langchain_openrouter\chat_models.py:509`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openrouter\langchain_openrouter\chat_models.py:509`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openrouter\langchain_openrouter\chat_models.py:491`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\openrouter\langchain_openrouter\chat_models.py:595`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\perplexity\langchain_perplexity\chat_models.py:424`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\perplexity\langchain_perplexity\chat_models.py:600`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\perplexity\langchain_perplexity\chat_models.py:513`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\perplexity\langchain_perplexity\chat_models.py:657`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\qdrant\langchain_qdrant\fastembed_sparse.py:80`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\qdrant\langchain_qdrant\qdrant.py:826`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\qdrant\langchain_qdrant\qdrant.py:584`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\qdrant\langchain_qdrant\qdrant.py:592`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\partners\qdrant\langchain_qdrant\qdrant.py:605`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\integration_tests\chat_models.py:1543`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:71`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:935`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:982`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1097`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1097`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1119`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1119`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:1146`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:961`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `libs\text-splitters\langchain_text_splitters\spacy.py:46`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `296 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\core\langchain_core\indexing\api.py:248`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\core\langchain_core\runnables\configurable.py:360`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\core\scripts\check_version.py:4`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\hub.py:61`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:22`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:23`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\agents\agent_toolkits\openapi\planner_prompt.py:19`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\indexes\_sql_record_manager.py:333`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\memory\entity.py:437`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\runnables\hub.py:10`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\tools\gmail\send_message.py:13`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\tools\office365\send_message.py:13`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain\langchain_classic\tools\slack\send_message.py:13`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\langchain\agents\middleware\file_search.py:281`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\langchain\agents\middleware\file_search.py:216`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\langchain\agents\middleware\shell_tool.py:139`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\langchain\agents\middleware\todo.py:112`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\langchain\agents\middleware\_execution.py:34`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\langchain_v1\scripts\check_version.py:5`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\partners\anthropic\langchain_anthropic\middleware\anthropic_tools.py:1018`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\partners\anthropic\scripts\check_version.py:5`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\standard-tests\langchain_tests\integration_tests\chat_models.py:737`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `libs\standard-tests\langchain_tests\unit_tests\chat_models.py:868`

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