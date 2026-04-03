# X-Verba Governance Report
*Generated 2026-04-03T08:08:15.594813+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\x-verba\dify`  
**Identity Key:** `dify-151a5a12`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **5357 files** and found **786 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **767** |
| High findings | 764 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.01 (below threshold) |

---

## Governance gaps

### 🔴 CRITICAL — `api\commands\plugin.py:473`

No checkpoint exists before the AI call at api\commands\plugin.py:473. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\commands\plugin.py:473`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\commands\plugin.py:473`

No checkpoint exists before the AI call at api\commands\plugin.py:473. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\commands\plugin.py:473`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\apikey.py:94`

No checkpoint exists before the AI call at api\controllers\console\apikey.py:94. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\apikey.py:94`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\app\completion.py:101`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\app\completion.py:180`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\conversation.py:357`

No checkpoint exists before the AI call at api\controllers\console\app\conversation.py:357. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\conversation.py:357`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\conversation.py:481`

No checkpoint exists before the AI call at api\controllers\console\app\conversation.py:481. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\conversation.py:481`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:72`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:72. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:72`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:101`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:101. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:101`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:133`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:133. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:133`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:184`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:184. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:184`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:193`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:193. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:193`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\generator.py:202`

No checkpoint exists before the AI call at api\controllers\console\app\generator.py:202. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\generator.py:202`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\app\mcp_server.py:146`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\mcp_server.py:81`

No checkpoint exists before the AI call at api\controllers\console\app\mcp_server.py:81. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\mcp_server.py:81`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\app\site.py:133`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:344`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:344. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:344`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:384`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:384. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:384`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:422`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:422. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:422`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:460`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:460. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:460`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:498`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:498. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:712`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:712. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:712`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:1340`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:1192`

No checkpoint exists before the AI call at api\controllers\console\app\workflow.py:1192. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow.py:1192`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow_run.py:272`

No checkpoint exists before the AI call at api\controllers\console\app\workflow_run.py:272. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow_run.py:272`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow_trigger.py:70`

No checkpoint exists before the AI call at api\controllers\console\app\workflow_trigger.py:70. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\app\workflow_trigger.py:70`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\auth\forgot_password.py:160`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets.py:824`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets.py:824. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets.py:824`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets.py:744`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets.py:744. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets.py:744`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets_document.py:733`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets_document.py:733. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets_document.py:733`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets_document.py:679`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets_document.py:679. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets_document.py:679`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets_document.py:335`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets_document.py:335. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets_document.py:335`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets_document.py:815`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets_document.py:815. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets_document.py:815`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets_document.py:849`

No checkpoint exists before the AI call at api\controllers\console\datasets\datasets_document.py:849. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\datasets_document.py:849`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:35`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:35. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:35`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:48`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:48. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:48`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:90`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:90`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_datasets.py:87`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_datasets.py:59`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_datasets.py:59. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_datasets.py:59`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:48`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:48. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:48`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:75`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:75. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:145`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:145. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:145`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:165`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:165. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:165`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:533`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:533. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:533`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:579`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:579. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:579`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:596`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:596. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:596`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:625`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:625. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:625`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:650`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:810`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:810. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:810`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:830`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:830. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:830`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:850`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:850. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:850`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:871`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:871. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:871`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:900`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:900. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:900`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:919`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:919. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:919`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:939`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:939. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:939`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:967`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:967. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:967`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:970`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:993`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1014`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1014. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1014`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1031`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1031. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1031`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:210`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:210. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:210`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:248`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:248. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:248`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:283`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:283. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:283`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:318`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:318. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:318`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:351`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:351. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:680`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:709`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:709. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:709`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:752`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:752. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:752`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:955`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:955. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:955`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:467`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:467. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:467`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:500`

No checkpoint exists before the AI call at api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:500. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:500`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\completion.py:101`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\completion.py:174`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\message.py:148`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\trial.py:190`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\trial.py:263`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\trial.py:442`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\explore\workflow.py:64`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\console\workspace\account.py:410`

No checkpoint exists before the AI call at api\controllers\console\workspace\account.py:410. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\console\workspace\account.py:410`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\workspace\account.py:616`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\console\workspace\members.py:323`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\mcp\mcp.py:83`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\mcp\mcp.py:87`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\mcp\mcp.py:194`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\app\completion.py:115`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\app\completion.py:210`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\app\workflow.py:174`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\app\workflow.py:234`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\dataset\document.py:636`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\service_api\dataset\document.py:764`

No checkpoint exists before the AI call at api\controllers\service_api\dataset\document.py:764. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\service_api\dataset\document.py:764`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\service_api\dataset\document.py:799`

No checkpoint exists before the AI call at api\controllers\service_api\dataset\document.py:799. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\service_api\dataset\document.py:799`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:79`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:123`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:189`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:191`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:133`

No checkpoint exists before the AI call at api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:133. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:133`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\trigger\webhook.py:60`

No checkpoint exists before the AI call at api\controllers\trigger\webhook.py:60. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\trigger\webhook.py:60`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\controllers\trigger\webhook.py:131`

No checkpoint exists before the AI call at api\controllers\trigger\webhook.py:131. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\controllers\trigger\webhook.py:131`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\web\completion.py:98`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\web\completion.py:181`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\web\forgot_password.py:135`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\web\message.py:197`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\controllers\web\workflow.py:71`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\indexing_runner.py:379`

No checkpoint exists before the AI call at api\core\indexing_runner.py:379. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\indexing_runner.py:538`

No checkpoint exists before the AI call at api\core\indexing_runner.py:538. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\indexing_runner.py:538`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\indexing_runner.py:614`

No checkpoint exists before the AI call at api\core\indexing_runner.py:614. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\indexing_runner.py:614`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\base_app_runner.py:542`

No checkpoint exists before the AI call at api\core\app\apps\base_app_runner.py:542. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\base_app_runner.py:542`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\message_based_app_generator.py:84`

No checkpoint exists before the AI call at api\core\app\apps\message_based_app_generator.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\message_based_app_generator.py:84`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\app_generator.py:685`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\app_generator.py:685. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\app_generator.py:685`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\app_runner.py:281`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\app_runner.py:281. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\app_runner.py:281`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\app_runner.py:320`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\app_runner.py:320. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\app_runner.py:320`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:627`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:627. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:627`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:218`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:218. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:218`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:627`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:627. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:627`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:706`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:706. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:706`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:895`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:895. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:895`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:346`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:351`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:352`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:652`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:652. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:652`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:655`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:655. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:655`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1037`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1037. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1037`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1038`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1038. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1038`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048`

No checkpoint exists before the AI call at api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\agent_chat\app_runner.py:104`

No checkpoint exists before the AI call at api\core\app\apps\agent_chat\app_runner.py:104. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\agent_chat\app_runner.py:104`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\chat\app_runner.py:114`

No checkpoint exists before the AI call at api\core\app\apps\chat\app_runner.py:114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\chat\app_runner.py:114`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\common\workflow_response_converter.py:506`

No checkpoint exists before the AI call at api\core\app\apps\common\workflow_response_converter.py:506. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\common\workflow_response_converter.py:506`

AI output flows to 'user-facing response' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_config_manager.py:29`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_config_manager.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_config_manager.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:131`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:375`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:477`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_generator.py:120`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_generator.py:120. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:120`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_generator.py:235`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_generator.py:235. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:235`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:380`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:472`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_generator.py:651`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_generator.py:651. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:651`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_generator.py:235`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_generator.py:235. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_generator.py:235`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_runner.py:164`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_runner.py:164. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_runner.py:164`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_runner.py:141`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_runner.py:141. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_runner.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_runner.py:141`

No checkpoint exists before the AI call at api\core\app\apps\pipeline\pipeline_runner.py:141. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\pipeline\pipeline_runner.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\workflow\app_generator.py:637`

No checkpoint exists before the AI call at api\core\app\apps\workflow\app_generator.py:637. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\workflow\app_generator.py:637`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\workflow\generate_task_pipeline.py:274`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\apps\workflow\generate_task_pipeline.py:645`

No checkpoint exists before the AI call at api\core\app\apps\workflow\generate_task_pipeline.py:645. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\apps\workflow\generate_task_pipeline.py:645`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\workflow\generate_task_pipeline.py:270`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\app\apps\workflow\generate_task_pipeline.py:275`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:125`

No checkpoint exists before the AI call at api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:125. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:125`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:513`

No checkpoint exists before the AI call at api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:513. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:513`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\app\task_pipeline\message_cycle_manager.py:139`

No checkpoint exists before the AI call at api\core\app\task_pipeline\message_cycle_manager.py:139. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\app\task_pipeline\message_cycle_manager.py:139`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\datasource\datasource_manager.py:349`

No checkpoint exists before the AI call at api\core\datasource\datasource_manager.py:349. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\datasource\datasource_manager.py:349`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\external_data_tool\external_data_fetch.py:87`

No checkpoint exists before the AI call at api\core\external_data_tool\external_data_fetch.py:87. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\external_data_tool\external_data_fetch.py:87`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\external_data_tool\factory.py:37`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\llm_generator\llm_generator.py:457`

No checkpoint exists before the AI call at api\core\llm_generator\llm_generator.py:457. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\llm_generator\llm_generator.py:457`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\mcp\server\streamable_http.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\ops\base_trace_instance.py:60`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\ops_trace_manager.py:767`

No checkpoint exists before the AI call at api\core\ops\ops_trace_manager.py:767. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\ops_trace_manager.py:767`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210`

No checkpoint exists before the AI call at api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210`

No checkpoint exists before the AI call at api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\langfuse_trace\langfuse_trace.py:76`

No checkpoint exists before the AI call at api\core\ops\langfuse_trace\langfuse_trace.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\langfuse_trace\langfuse_trace.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\langfuse_trace\langfuse_trace.py:76`

No checkpoint exists before the AI call at api\core\ops\langfuse_trace\langfuse_trace.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\langfuse_trace\langfuse_trace.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\langsmith_trace\langsmith_trace.py:64`

No checkpoint exists before the AI call at api\core\ops\langsmith_trace\langsmith_trace.py:64. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\langsmith_trace\langsmith_trace.py:64`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\langsmith_trace\langsmith_trace.py:64`

No checkpoint exists before the AI call at api\core\ops\langsmith_trace\langsmith_trace.py:64. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\langsmith_trace\langsmith_trace.py:64`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\mlflow_trace\mlflow_trace.py:105`

No checkpoint exists before the AI call at api\core\ops\mlflow_trace\mlflow_trace.py:105. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\mlflow_trace\mlflow_trace.py:105`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\mlflow_trace\mlflow_trace.py:105`

No checkpoint exists before the AI call at api\core\ops\mlflow_trace\mlflow_trace.py:105. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\mlflow_trace\mlflow_trace.py:105`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\opik_trace\opik_trace.py:112`

No checkpoint exists before the AI call at api\core\ops\opik_trace\opik_trace.py:112. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\opik_trace\opik_trace.py:112`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\opik_trace\opik_trace.py:112`

No checkpoint exists before the AI call at api\core\ops\opik_trace\opik_trace.py:112. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\opik_trace\opik_trace.py:112`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\ops\tencent_trace\tencent_trace.py:245`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\weave_trace\weave_trace.py:96`

No checkpoint exists before the AI call at api\core\ops\weave_trace\weave_trace.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\weave_trace\weave_trace.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\ops\weave_trace\weave_trace.py:96`

No checkpoint exists before the AI call at api\core\ops\weave_trace\weave_trace.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\ops\weave_trace\weave_trace.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:854`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:854. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:854`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:878`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:878. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:878`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:243`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:243. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:243`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:857`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:857. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:857`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:882`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:882. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:882`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\retrieval_service.py:577`

No checkpoint exists before the AI call at api\core\rag\datasource\retrieval_service.py:577. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\retrieval_service.py:577`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\chroma\chroma_vector.py:101`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\chroma\chroma_vector.py:101. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\chroma\chroma_vector.py:101`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\chroma\chroma_vector.py:107`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\chroma\chroma_vector.py:107. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\chroma\chroma_vector.py:107`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:253`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:253. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:253`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:269`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:269. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:269`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:243`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:243. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:243`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:157`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:200`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\milvus\milvus_vector.py:200. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:200`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:179`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\milvus\milvus_vector.py:179. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:179`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:101`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\myscale\myscale_vector.py:101. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:101`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:112`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\myscale\myscale_vector.py:112. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:112`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:153`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\myscale\myscale_vector.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:153`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\rag\datasource\vdb\opensearch\opensearch_vector.py:55`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tencent\tencent_vector.py:202`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\tencent\tencent_vector.py:202. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\tencent\tencent_vector.py:202`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\upstash\upstash_vector.py:76`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\upstash\upstash_vector.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\upstash\upstash_vector.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\upstash\upstash_vector.py:97`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\upstash\upstash_vector.py:97. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\upstash\upstash_vector.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:352`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:352. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:352`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:399`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:399. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:399`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:445`

No checkpoint exists before the AI call at api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:445. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:445`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\rag\embedding\cached_embedding.py:195`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\embedding\cached_embedding.py:34`

No checkpoint exists before the AI call at api\core\rag\embedding\cached_embedding.py:34. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\embedding\cached_embedding.py:34`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\embedding\cached_embedding.py:89`

No checkpoint exists before the AI call at api\core\rag\embedding\cached_embedding.py:89. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\embedding\cached_embedding.py:89`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:66`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:66. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\index_processor.py:66`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\rag\index_processor\index_processor.py:70`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:121`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:121. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\index_processor.py:121`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:157`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:157. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:196`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:196. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:206`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:206. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:107`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:107. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\index_processor.py:107`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\index_processor.py:153`

No checkpoint exists before the AI call at api\core\rag\index_processor\index_processor.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\paragraph_index_processor.py:316`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\paragraph_index_processor.py:316. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\paragraph_index_processor.py:101`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\paragraph_index_processor.py:101. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\paragraph_index_processor.py:101`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\paragraph_index_processor.py:213`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\paragraph_index_processor.py:213. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\paragraph_index_processor.py:213`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\paragraph_index_processor.py:228`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\paragraph_index_processor.py:228. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\paragraph_index_processor.py:228`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\paragraph_index_processor.py:310`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\paragraph_index_processor.py:310. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:118`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:118. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:267`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:289`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:289. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:289`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:407`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:407. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:297`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:297. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:297`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:398`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:398. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:81`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:81. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:81`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:157`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\parent_child_index_processor.py:157. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\parent_child_index_processor.py:157`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\qa_index_processor.py:218`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\qa_index_processor.py:218. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\qa_index_processor.py:266`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\qa_index_processor.py:266. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\qa_index_processor.py:266`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\qa_index_processor.py:79`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\qa_index_processor.py:79. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\qa_index_processor.py:273`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\qa_index_processor.py:273. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\qa_index_processor.py:273`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\qa_index_processor.py:162`

No checkpoint exists before the AI call at api\core\rag\index_processor\processor\qa_index_processor.py:162. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\index_processor\processor\qa_index_processor.py:162`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:281`

No checkpoint exists before the AI call at api\core\rag\retrieval\dataset_retrieval.py:281. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\retrieval\dataset_retrieval.py:281`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:282`

No checkpoint exists before the AI call at api\core\rag\retrieval\dataset_retrieval.py:282. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\retrieval\dataset_retrieval.py:282`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:976`

No checkpoint exists before the AI call at api\core\rag\retrieval\dataset_retrieval.py:976. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\retrieval\dataset_retrieval.py:976`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:1828`

No checkpoint exists before the AI call at api\core\rag\retrieval\dataset_retrieval.py:1828. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\retrieval\dataset_retrieval.py:1828`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:1841`

No checkpoint exists before the AI call at api\core\rag\retrieval\dataset_retrieval.py:1841. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\retrieval\dataset_retrieval.py:1841`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:80`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:80`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:42`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:42. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:42`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:80`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:80`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:24`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:24. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:24`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:37`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:37. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:37`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:55`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🔴 CRITICAL — `api\core\rag\summary_index\summary_index.py:76`

No checkpoint exists before the AI call at api\core\rag\summary_index\summary_index.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\rag\summary_index\summary_index.py:76`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_file_manager.py:170`

No checkpoint exists before the AI call at api\core\tools\tool_file_manager.py:170. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_file_manager.py:170`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_file_manager.py:194`

No checkpoint exists before the AI call at api\core\tools\tool_file_manager.py:194. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_file_manager.py:194`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_file_manager.py:214`

No checkpoint exists before the AI call at api\core\tools\tool_file_manager.py:214. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_file_manager.py:214`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_file_manager.py:238`

No checkpoint exists before the AI call at api\core\tools\tool_file_manager.py:238. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_file_manager.py:238`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:1037`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:1037. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1037`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:1039`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:1039. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1039`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:1034`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:1034. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1034`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:1041`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:1041. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1041`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:688`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:688. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:688`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:1045`

No checkpoint exists before the AI call at api\core\tools\tool_manager.py:1045. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1045`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\tools\tool_manager.py:1050`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\builtin_tool\tool.py:105`

No checkpoint exists before the AI call at api\core\tools\builtin_tool\tool.py:105. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\builtin_tool\tool.py:105`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\utils\dataset_retriever\dataset_multi_retriever_tool.py:92`

No checkpoint exists before the AI call at api\core\tools\utils\dataset_retriever\dataset_multi_retriever_tool.py:92. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\utils\dataset_retriever\dataset_multi_retriever_tool.py:92`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\workflow_as_tool\provider.py:100`

No checkpoint exists before the AI call at api\core\tools\workflow_as_tool\provider.py:100. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\workflow_as_tool\provider.py:100`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\workflow_as_tool\provider.py:221`

No checkpoint exists before the AI call at api\core\tools\workflow_as_tool\provider.py:221. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\workflow_as_tool\provider.py:221`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\core\tools\workflow_as_tool\tool.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\tools\workflow_as_tool\tool.py:315`

No checkpoint exists before the AI call at api\core\tools\workflow_as_tool\tool.py:315. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\tools\workflow_as_tool\tool.py:315`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\workflow\system_variables.py:131`

No checkpoint exists before the AI call at api\core\workflow\system_variables.py:131. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\workflow\system_variables.py:131`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\workflow\nodes\trigger_webhook\node.py:151`

No checkpoint exists before the AI call at api\core\workflow\nodes\trigger_webhook\node.py:151. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\workflow\nodes\trigger_webhook\node.py:151`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\core\workflow\nodes\trigger_webhook\node.py:164`

No checkpoint exists before the AI call at api\core\workflow\nodes\trigger_webhook\node.py:164. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\core\workflow\nodes\trigger_webhook\node.py:164`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\events\event_handlers\create_site_record_when_app_created.py:21`

No checkpoint exists before the AI call at api\events\event_handlers\create_site_record_when_app_created.py:21. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\events\event_handlers\create_site_record_when_app_created.py:21`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\extensions\storage\aws_s3_storage.py:23`

No checkpoint exists before the AI call at api\extensions\storage\aws_s3_storage.py:23. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\extensions\storage\aws_s3_storage.py:23`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\extensions\storage\aws_s3_storage.py:29`

No checkpoint exists before the AI call at api\extensions\storage\aws_s3_storage.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\extensions\storage\aws_s3_storage.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\extensions\storage\oracle_oci_storage.py:17`

No checkpoint exists before the AI call at api\extensions\storage\oracle_oci_storage.py:17. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\extensions\storage\oracle_oci_storage.py:17`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\libs\archive_storage.py:65`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\libs\archive_storage.py:215`

No checkpoint exists before the AI call at api\libs\archive_storage.py:215. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\libs\archive_storage.py:215`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\libs\rsa.py:14`

No checkpoint exists before the AI call at api\libs\rsa.py:14. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\libs\rsa.py:14`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\models\workflow.py:495`

No checkpoint exists before the AI call at api\models\workflow.py:495. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\models\workflow.py:495`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\models\workflow.py:654`

No checkpoint exists before the AI call at api\models\workflow.py:654. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\models\workflow.py:654`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:117`

No checkpoint exists before the AI call at api\schedule\clean_workflow_runlogs_precise.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\clean_workflow_runlogs_precise.py:117`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:139`

No checkpoint exists before the AI call at api\schedule\clean_workflow_runlogs_precise.py:139. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\clean_workflow_runlogs_precise.py:139`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:144`

No checkpoint exists before the AI call at api\schedule\clean_workflow_runlogs_precise.py:144. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\clean_workflow_runlogs_precise.py:144`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:148`

No checkpoint exists before the AI call at api\schedule\clean_workflow_runlogs_precise.py:148. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\clean_workflow_runlogs_precise.py:148`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:135`

No checkpoint exists before the AI call at api\schedule\clean_workflow_runlogs_precise.py:135. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\clean_workflow_runlogs_precise.py:135`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\schedule\trigger_provider_refresh_task.py:45`

No checkpoint exists before the AI call at api\schedule\trigger_provider_refresh_task.py:45. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\schedule\trigger_provider_refresh_task.py:45`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:327`

No checkpoint exists before the AI call at api\services\account_service.py:327. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:327`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:507`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:540`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:578`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:685`

No checkpoint exists before the AI call at api\services\account_service.py:685. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:685`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:700`

No checkpoint exists before the AI call at api\services\account_service.py:700. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:700`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:716`

No checkpoint exists before the AI call at api\services\account_service.py:716. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:716`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:732`

No checkpoint exists before the AI call at api\services\account_service.py:732. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:732`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:785`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1512`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:1238`

No checkpoint exists before the AI call at api\services\account_service.py:1238. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:1238`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1107`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1136`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1229`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1255`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1273`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1324`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1165`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1219`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1288`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1336`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:1073`

No checkpoint exists before the AI call at api\services\account_service.py:1073. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:1073`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:1123`

No checkpoint exists before the AI call at api\services\account_service.py:1123. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:1123`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1152`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\account_service.py:1177`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\account_service.py:1196`

No checkpoint exists before the AI call at api\services\account_service.py:1196. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\account_service.py:1196`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:695`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:697`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:55`

No checkpoint exists before the AI call at api\services\annotation_service.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:55`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:98`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:155`

No checkpoint exists before the AI call at api\services\annotation_service.py:155. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:155`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:197`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:227`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:245`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:261`

No checkpoint exists before the AI call at api\services\annotation_service.py:261. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:261`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:269`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:284`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:303`

No checkpoint exists before the AI call at api\services\annotation_service.py:303. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:303`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:311`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:328`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:341`

No checkpoint exists before the AI call at api\services\annotation_service.py:341. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:341`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:364`

No checkpoint exists before the AI call at api\services\annotation_service.py:364. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:364`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:377`

No checkpoint exists before the AI call at api\services\annotation_service.py:377. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:377`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:402`

No checkpoint exists before the AI call at api\services\annotation_service.py:402. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:402`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:526`

No checkpoint exists before the AI call at api\services\annotation_service.py:526. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:526`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:534`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:554`

No checkpoint exists before the AI call at api\services\annotation_service.py:554. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:554`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:574`

No checkpoint exists before the AI call at api\services\annotation_service.py:574. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:574`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:597`

No checkpoint exists before the AI call at api\services\annotation_service.py:597. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:597`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:605`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:634`

No checkpoint exists before the AI call at api\services\annotation_service.py:634. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:634`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:643`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:682`

No checkpoint exists before the AI call at api\services\annotation_service.py:682. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\annotation_service.py:682`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:692`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:69`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:205`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\annotation_service.py:351`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_dsl_service.py:627`

No checkpoint exists before the AI call at api\services\app_dsl_service.py:627. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_dsl_service.py:627`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\app_dsl_service.py:655`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\app_dsl_service.py:289`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\app_generate_service.py:120`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:129`

No checkpoint exists before the AI call at api\services\app_generate_service.py:129. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:129`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:138`

No checkpoint exists before the AI call at api\services\app_generate_service.py:138. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:138`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:169`

No checkpoint exists before the AI call at api\services\app_generate_service.py:169. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:169`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:183`

No checkpoint exists before the AI call at api\services\app_generate_service.py:183. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:183`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:234`

No checkpoint exists before the AI call at api\services\app_generate_service.py:234. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:234`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:219`

No checkpoint exists before the AI call at api\services\app_generate_service.py:219. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:219`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\app_generate_service.py:185`

No checkpoint exists before the AI call at api\services\app_generate_service.py:185. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\app_generate_service.py:185`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\billing_service.py:386`

No checkpoint exists before the AI call at api\services\billing_service.py:386. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\billing_service.py:386`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:350`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:350. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:350`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:66`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:66. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:66`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:106`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:106. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:106`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:150`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:150. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:150`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:190`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:190. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:190`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:326`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:326. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:326`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:440`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:440. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:440`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:415`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:415. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:415`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:125`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:125. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:125`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:166`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:166. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:166`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:299`

No checkpoint exists before the AI call at api\services\clear_free_plan_tenant_expired_logs.py:299. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\clear_free_plan_tenant_expired_logs.py:299`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\conversation_service.py:152`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:606`

No checkpoint exists before the AI call at api\services\dataset_service.py:606. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:606`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:606`

No checkpoint exists before the AI call at api\services\dataset_service.py:606. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:606`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3131`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:640`

No checkpoint exists before the AI call at api\services\dataset_service.py:640. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:640`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:641`

No checkpoint exists before the AI call at api\services\dataset_service.py:641. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:641`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3730`

No checkpoint exists before the AI call at api\services\dataset_service.py:3730. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3730`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:337`

No checkpoint exists before the AI call at api\services\dataset_service.py:337. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:337`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3415`

No checkpoint exists before the AI call at api\services\dataset_service.py:3415. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3415`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:2523`

No checkpoint exists before the AI call at api\services\dataset_service.py:2523. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:2523`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3236`

No checkpoint exists before the AI call at api\services\dataset_service.py:3236. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3236`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3378`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3482`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3812`

No checkpoint exists before the AI call at api\services\dataset_service.py:3812. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3812`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:228`

No checkpoint exists before the AI call at api\services\dataset_service.py:228. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:228`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:347`

No checkpoint exists before the AI call at api\services\dataset_service.py:347. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:347`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:470`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:599`

No checkpoint exists before the AI call at api\services\dataset_service.py:599. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:599`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:634`

No checkpoint exists before the AI call at api\services\dataset_service.py:634. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:634`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:1629`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:1694`

No checkpoint exists before the AI call at api\services\dataset_service.py:1694. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:1694`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:2521`

No checkpoint exists before the AI call at api\services\dataset_service.py:2521. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:2521`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:2653`

No checkpoint exists before the AI call at api\services\dataset_service.py:2653. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:2653`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3378`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3482`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3564`

No checkpoint exists before the AI call at api\services\dataset_service.py:3564. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3564`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3657`

No checkpoint exists before the AI call at api\services\dataset_service.py:3657. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3657`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3900`

No checkpoint exists before the AI call at api\services\dataset_service.py:3900. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3900`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3938`

No checkpoint exists before the AI call at api\services\dataset_service.py:3938. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3938`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:118`

No checkpoint exists before the AI call at api\services\dataset_service.py:118. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:304`

No checkpoint exists before the AI call at api\services\dataset_service.py:304. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:304`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:313`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:545`

No checkpoint exists before the AI call at api\services\dataset_service.py:545. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:545`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:1400`

No checkpoint exists before the AI call at api\services\dataset_service.py:1400. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:1400`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:1444`

No checkpoint exists before the AI call at api\services\dataset_service.py:1444. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:1444`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:1768`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3201`

No checkpoint exists before the AI call at api\services\dataset_service.py:3201. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3201`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3513`

No checkpoint exists before the AI call at api\services\dataset_service.py:3513. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3513`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3634`

No checkpoint exists before the AI call at api\services\dataset_service.py:3634. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3634`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3732`

No checkpoint exists before the AI call at api\services\dataset_service.py:3732. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3732`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:4037`

No checkpoint exists before the AI call at api\services\dataset_service.py:4037. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:4037`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:4073`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:1179`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:1858`

No checkpoint exists before the AI call at api\services\dataset_service.py:1858. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:1858`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3147`

No checkpoint exists before the AI call at api\services\dataset_service.py:3147. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3147`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3225`

No checkpoint exists before the AI call at api\services\dataset_service.py:3225. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3225`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3513`

No checkpoint exists before the AI call at api\services\dataset_service.py:3513. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3513`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3545`

No checkpoint exists before the AI call at api\services\dataset_service.py:3545. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3545`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3585`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3612`

No checkpoint exists before the AI call at api\services\dataset_service.py:3612. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3612`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3984`

No checkpoint exists before the AI call at api\services\dataset_service.py:3984. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3984`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:4010`

No checkpoint exists before the AI call at api\services\dataset_service.py:4010. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:4010`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:1142`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:2579`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3373`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:3477`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3493`

No checkpoint exists before the AI call at api\services\dataset_service.py:3493. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3493`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3545`

No checkpoint exists before the AI call at api\services\dataset_service.py:3545. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3545`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:186`

No checkpoint exists before the AI call at api\services\dataset_service.py:186. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:186`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:2016`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:2028`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:2599`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:3395`

No checkpoint exists before the AI call at api\services\dataset_service.py:3395. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\dataset_service.py:3395`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:2083`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\dataset_service.py:1164`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:557`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:557. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:557`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:628`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:628. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:628`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:388`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:388. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:388`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\datasource_provider_service.py:464`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:711`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:711. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:711`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:884`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:884. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:884`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:991`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:991. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:991`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:56`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:56. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:56`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:238`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:238. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:238`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:280`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:280. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:280`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\datasource_provider_service.py:293`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:319`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:319. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:319`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:370`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:370. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:370`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:432`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:432. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:432`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:927`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:927. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:927`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:114`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:114`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\datasource_provider_service.py:255`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:359`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:359. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:359`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:452`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:452. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:452`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:494`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:494. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:494`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:723`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:723. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:723`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:178`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:178. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:178`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\datasource_provider_service.py:504`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:637`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:637. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:637`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\datasource_provider_service.py:936`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:118`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:118. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:565`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:565. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:565`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:518`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:518. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:518`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:579`

No checkpoint exists before the AI call at api\services\datasource_provider_service.py:579. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\datasource_provider_service.py:579`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\end_user_service.py:29`

No checkpoint exists before the AI call at api\services\end_user_service.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\end_user_service.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\end_user_service.py:141`

No checkpoint exists before the AI call at api\services\end_user_service.py:141. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\end_user_service.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\end_user_service.py:61`

No checkpoint exists before the AI call at api\services\end_user_service.py:61. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\end_user_service.py:61`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\file_service.py:181`

No checkpoint exists before the AI call at api\services\file_service.py:181. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\file_service.py:203`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\file_service.py:234`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\file_service.py:250`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\knowledge_service.py:19`

No checkpoint exists before the AI call at api\services\knowledge_service.py:19. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\knowledge_service.py:19`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\message_service.py:316`

No checkpoint exists before the AI call at api\services\message_service.py:316. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\message_service.py:316`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:61`

No checkpoint exists before the AI call at api\services\summary_index_service.py:61. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:61`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\summary_index_service.py:177`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:651`

No checkpoint exists before the AI call at api\services\summary_index_service.py:651. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:651`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:756`

No checkpoint exists before the AI call at api\services\summary_index_service.py:756. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:756`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:795`

No checkpoint exists before the AI call at api\services\summary_index_service.py:795. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:795`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:835`

No checkpoint exists before the AI call at api\services\summary_index_service.py:835. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:835`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:898`

No checkpoint exists before the AI call at api\services\summary_index_service.py:898. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:898`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:975`

No checkpoint exists before the AI call at api\services\summary_index_service.py:975. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:975`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1226`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1226. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1226`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:97`

No checkpoint exists before the AI call at api\services\summary_index_service.py:97. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:539`

No checkpoint exists before the AI call at api\services\summary_index_service.py:539. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:539`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:591`

No checkpoint exists before the AI call at api\services\summary_index_service.py:591. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:591`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1173`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1173. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1173`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1199`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1199. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1199`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1253`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1253. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1253`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1300`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1300. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1300`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:627`

No checkpoint exists before the AI call at api\services\summary_index_service.py:627. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:627`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:923`

No checkpoint exists before the AI call at api\services\summary_index_service.py:923. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:923`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1065`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1065. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1065`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:698`

No checkpoint exists before the AI call at api\services\summary_index_service.py:698. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:698`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:1034`

No checkpoint exists before the AI call at api\services\summary_index_service.py:1034. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:1034`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\summary_index_service.py:1150`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:297`

No checkpoint exists before the AI call at api\services\summary_index_service.py:297. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:297`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:311`

No checkpoint exists before the AI call at api\services\summary_index_service.py:311. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:311`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:475`

No checkpoint exists before the AI call at api\services\summary_index_service.py:475. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:475`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\summary_index_service.py:488`

No checkpoint exists before the AI call at api\services\summary_index_service.py:488. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\summary_index_service.py:488`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\vector_service.py:64`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\vector_service.py:64`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\webapp_auth_service.py:75`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:280`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:280. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:280`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:302`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:302. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:302`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:258`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:258. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:258`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:492`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:492. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:492`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:502`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:502. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:502`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:544`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:544. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:544`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:592`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:592. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:592`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:226`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:226. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:226`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:330`

No checkpoint exists before the AI call at api\services\workflow_draft_variable_service.py:330. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\workflow_draft_variable_service.py:330`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\workflow_service.py:1510`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_auto_upgrade_service.py:12`

No checkpoint exists before the AI call at api\services\plugin\plugin_auto_upgrade_service.py:12. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_auto_upgrade_service.py:12`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_auto_upgrade_service.py:28`

No checkpoint exists before the AI call at api\services\plugin\plugin_auto_upgrade_service.py:28. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_auto_upgrade_service.py:28`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_auto_upgrade_service.py:56`

No checkpoint exists before the AI call at api\services\plugin\plugin_auto_upgrade_service.py:56. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_auto_upgrade_service.py:56`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:59`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:59. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:59`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:228`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:228. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:228`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:242`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:242. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:242`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:265`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:265. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:265`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:273`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:273. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:273`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:141`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:141. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:141`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_migration.py:116`

No checkpoint exists before the AI call at api\services\plugin\plugin_migration.py:116. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_migration.py:116`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_parameter_service.py:60`

No checkpoint exists before the AI call at api\services\plugin\plugin_parameter_service.py:60. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_parameter_service.py:60`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_parameter_service.py:70`

No checkpoint exists before the AI call at api\services\plugin\plugin_parameter_service.py:70. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_parameter_service.py:70`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_permission_service.py:11`

No checkpoint exists before the AI call at api\services\plugin\plugin_permission_service.py:11. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_permission_service.py:11`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\plugin\plugin_permission_service.py:21`

No checkpoint exists before the AI call at api\services\plugin\plugin_permission_service.py:21. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\plugin\plugin_permission_service.py:21`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_generate_service.py:94`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_generate_service.py:94. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_generate_service.py:94`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_generate_service.py:100`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:1153`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:1153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:1153`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:115`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:115. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:115`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:123`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:123. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:123`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:138`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:138. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:138`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:149`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:149. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:149`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:438`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:1190`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:1218`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:114`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:114`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:117`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:117`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:118`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:118. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:118`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:122`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:122. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:122`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:137`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:137. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:137`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:148`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:148. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:148`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:435`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline.py:435. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:435`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline.py:438`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:656`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:656. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:656`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:939`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:269`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:415`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:420`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:420. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:420`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:583`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:583. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:583`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:584`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:584. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:584`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:240`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:240. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:240`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:720`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:720. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:720`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:594`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:595`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:611`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:685`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:685. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:685`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:924`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:924. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:924`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:931`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:302`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:323`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:323. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:323`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:460`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_dsl_service.py:460. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:460`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_transform_service.py:55`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_transform_service.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:55`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:81`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_transform_service.py:268`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_transform_service.py:268. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:268`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:45`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:49`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_transform_service.py:218`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_transform_service.py:218. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:218`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_transform_service.py:219`

No checkpoint exists before the AI call at api\services\rag_pipeline\rag_pipeline_transform_service.py:219. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\rag_pipeline_transform_service.py:219`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:22`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:22. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:22`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:26`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:26. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:26`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:18`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:18. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:18`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:22`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:22. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:22`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:16`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:16. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:16`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:20`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:20. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:20`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:21`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:21. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:21`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:29`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:24`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:24. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:24`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:32`

No checkpoint exists before the AI call at api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:247`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:50`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:50. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:50`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:156`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:156. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:156`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:384`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:384. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:384`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:414`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:414. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:414`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:419`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:437`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:437. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:437`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:451`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:451. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:451`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:476`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:476. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:476`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:498`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:498. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:498`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:659`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:704`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:704. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:704`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:313`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:313. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:313`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:234`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:593`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:593. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:593`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:606`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:606. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:606`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:627`

No checkpoint exists before the AI call at api\services\tools\builtin_tools_manage_service.py:627. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\builtin_tools_manage_service.py:627`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\tools\mcp_tools_manage_service.py:288`

No checkpoint exists before the AI call at api\services\tools\mcp_tools_manage_service.py:288. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\tools\mcp_tools_manage_service.py:288`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:356`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:356. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:356`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:408`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:408. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:408`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:483`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:483. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:483`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:561`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:561. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:561`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:587`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:587. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:587`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:611`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:611. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:611`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:645`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:645. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:645`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:701`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:701. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:701`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:737`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:737. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:737`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:757`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:757. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:757`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:774`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:774. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:774`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:249`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:249. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:249`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:323`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:323. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:323`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:326`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:326. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:326`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:73`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:73. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:73`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:82`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:82. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:82`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:155`

No checkpoint exists before the AI call at api\services\trigger\trigger_provider_service.py:155. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:155`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:168`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\trigger\trigger_provider_service.py:260`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\webhook_service.py:96`

No checkpoint exists before the AI call at api\services\trigger\webhook_service.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\webhook_service.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\webhook_service.py:923`

No checkpoint exists before the AI call at api\services\trigger\webhook_service.py:923. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\webhook_service.py:923`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\services\trigger\webhook_service.py:114`

No checkpoint exists before the AI call at api\services\trigger\webhook_service.py:114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\services\trigger\webhook_service.py:114`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\trigger\webhook_service.py:103`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\services\trigger\webhook_service.py:138`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\add_document_to_index_task.py:33`

No checkpoint exists before the AI call at api\tasks\add_document_to_index_task.py:33. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\add_document_to_index_task.py:33`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\add_document_to_index_task.py:107`

No checkpoint exists before the AI call at api\tasks\add_document_to_index_task.py:107. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\add_document_to_index_task.py:107`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\add_document_to_index_task.py:112`

No checkpoint exists before the AI call at api\tasks\add_document_to_index_task.py:112. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\add_document_to_index_task.py:112`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\add_document_to_index_task.py:49`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\async_workflow_tasks.py:160`

No checkpoint exists before the AI call at api\tasks\async_workflow_tasks.py:160. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\async_workflow_tasks.py:160`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\async_workflow_tasks.py:160`

No checkpoint exists before the AI call at api\tasks\async_workflow_tasks.py:160. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\async_workflow_tasks.py:160`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\batch_clean_document_task.py:96`

No checkpoint exists before the AI call at api\tasks\batch_clean_document_task.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\batch_clean_document_task.py:96`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\batch_clean_document_task.py:76`

No checkpoint exists before the AI call at api\tasks\batch_clean_document_task.py:76. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\batch_clean_document_task.py:76`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\batch_create_segment_to_index_task.py:142`

No checkpoint exists before the AI call at api\tasks\batch_create_segment_to_index_task.py:142. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\batch_create_segment_to_index_task.py:142`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\batch_create_segment_to_index_task.py:144`

No checkpoint exists before the AI call at api\tasks\batch_create_segment_to_index_task.py:144. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\batch_create_segment_to_index_task.py:144`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:153`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:153`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:154`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:154. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:154`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:155`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:155. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:155`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:157`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:157. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:157`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:158`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:158. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:158`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:161`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:161. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:161`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:162`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:162. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:162`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:177`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:177. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:177`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_dataset_task.py:115`

No checkpoint exists before the AI call at api\tasks\clean_dataset_task.py:115. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_dataset_task.py:115`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_document_task.py:127`

No checkpoint exists before the AI call at api\tasks\clean_document_task.py:127. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_document_task.py:127`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_document_task.py:35`

No checkpoint exists before the AI call at api\tasks\clean_document_task.py:35. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_document_task.py:35`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_document_task.py:66`

No checkpoint exists before the AI call at api\tasks\clean_document_task.py:66. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_document_task.py:66`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_document_task.py:97`

No checkpoint exists before the AI call at api\tasks\clean_document_task.py:97. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_document_task.py:97`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\clean_notion_document_task.py:29`

No checkpoint exists before the AI call at api\tasks\clean_notion_document_task.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\clean_notion_document_task.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\clean_notion_document_task.py:44`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\create_segment_to_index_task.py:30`

No checkpoint exists before the AI call at api\tasks\create_segment_to_index_task.py:30. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\create_segment_to_index_task.py:30`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\create_segment_to_index_task.py:42`

No checkpoint exists before the AI call at api\tasks\create_segment_to_index_task.py:42. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\create_segment_to_index_task.py:42`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\create_segment_to_index_task.py:84`

No checkpoint exists before the AI call at api\tasks\create_segment_to_index_task.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\create_segment_to_index_task.py:84`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:29`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:37`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:49`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:49. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:49`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:95`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:95. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:95`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:108`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:108. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:108`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:84`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:84`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:89`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:89. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:89`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:176`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:176. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:176`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:58`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:58. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:58`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:181`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:181. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:181`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:120`

No checkpoint exists before the AI call at api\tasks\deal_dataset_index_update_task.py:120. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_index_update_task.py:120`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:32`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:52`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:52. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:52`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:107`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:107. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:107`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:85`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:85. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:85`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:90`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:90`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:175`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:175. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:175`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:61`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:61. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:61`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:180`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:180. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:180`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:119`

No checkpoint exists before the AI call at api\tasks\deal_dataset_vector_index_task.py:119. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\deal_dataset_vector_index_task.py:119`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_account_task.py:17`

No checkpoint exists before the AI call at api\tasks\delete_account_task.py:17. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_account_task.py:17`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:32`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:36`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:36. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:36`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:40`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:40. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:40`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:44`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:44. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:44`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:46`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:46. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:46`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:50`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:50. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:50`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_conversation_task.py:52`

No checkpoint exists before the AI call at api\tasks\delete_conversation_task.py:52. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_conversation_task.py:52`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_segment_from_index_task.py:32`

No checkpoint exists before the AI call at api\tasks\delete_segment_from_index_task.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_segment_from_index_task.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_segment_from_index_task.py:37`

No checkpoint exists before the AI call at api\tasks\delete_segment_from_index_task.py:37. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_segment_from_index_task.py:37`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_segment_from_index_task.py:64`

No checkpoint exists before the AI call at api\tasks\delete_segment_from_index_task.py:64. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_segment_from_index_task.py:64`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\delete_segment_from_index_task.py:80`

No checkpoint exists before the AI call at api\tasks\delete_segment_from_index_task.py:80. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\delete_segment_from_index_task.py:80`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\disable_segments_from_index_task.py:30`

No checkpoint exists before the AI call at api\tasks\disable_segments_from_index_task.py:30. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\disable_segments_from_index_task.py:30`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\disable_segments_from_index_task.py:35`

No checkpoint exists before the AI call at api\tasks\disable_segments_from_index_task.py:35. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\disable_segments_from_index_task.py:35`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\disable_segments_from_index_task.py:62`

No checkpoint exists before the AI call at api\tasks\disable_segments_from_index_task.py:62. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\disable_segments_from_index_task.py:62`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\disable_segments_from_index_task.py:90`

No checkpoint exists before the AI call at api\tasks\disable_segments_from_index_task.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\disable_segments_from_index_task.py:90`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\disable_segment_from_index_task.py:27`

No checkpoint exists before the AI call at api\tasks\disable_segment_from_index_task.py:27. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\disable_segment_from_index_task.py:27`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:35`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:35. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:35`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:45`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:45. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:45`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:123`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:123. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:123`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:90`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:90`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:115`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:115. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:115`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:143`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:143. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:143`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_sync_task.py:153`

No checkpoint exists before the AI call at api\tasks\document_indexing_sync_task.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_sync_task.py:153`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_task.py:60`

No checkpoint exists before the AI call at api\tasks\document_indexing_task.py:60. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_task.py:60`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_task.py:96`

No checkpoint exists before the AI call at api\tasks\document_indexing_task.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_task.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_task.py:125`

No checkpoint exists before the AI call at api\tasks\document_indexing_task.py:125. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_task.py:125`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\document_indexing_task.py:83`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_task.py:138`

No checkpoint exists before the AI call at api\tasks\document_indexing_task.py:138. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_task.py:138`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_update_task.py:31`

No checkpoint exists before the AI call at api\tasks\document_indexing_update_task.py:31. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_update_task.py:31`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_update_task.py:40`

No checkpoint exists before the AI call at api\tasks\document_indexing_update_task.py:40. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\document_indexing_update_task.py:40`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\duplicate_document_indexing_task.py:85`

No checkpoint exists before the AI call at api\tasks\duplicate_document_indexing_task.py:85. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\duplicate_document_indexing_task.py:85`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\enable_segments_to_index_task.py:33`

No checkpoint exists before the AI call at api\tasks\enable_segments_to_index_task.py:33. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\enable_segments_to_index_task.py:33`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\enable_segments_to_index_task.py:38`

No checkpoint exists before the AI call at api\tasks\enable_segments_to_index_task.py:38. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\enable_segments_to_index_task.py:38`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\enable_segments_to_index_task.py:126`

No checkpoint exists before the AI call at api\tasks\enable_segments_to_index_task.py:126. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\enable_segments_to_index_task.py:126`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\enable_segment_to_index_task.py:32`

No checkpoint exists before the AI call at api\tasks\enable_segment_to_index_task.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\enable_segment_to_index_task.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\generate_summary_index_task.py:88`

No checkpoint exists before the AI call at api\tasks\generate_summary_index_task.py:88. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\generate_summary_index_task.py:88`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\generate_summary_index_task.py:42`

No checkpoint exists before the AI call at api\tasks\generate_summary_index_task.py:42. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\generate_summary_index_task.py:42`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\generate_summary_index_task.py:47`

No checkpoint exists before the AI call at api\tasks\generate_summary_index_task.py:47. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\generate_summary_index_task.py:47`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\generate_summary_index_task.py:111`

No checkpoint exists before the AI call at api\tasks\generate_summary_index_task.py:111. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\generate_summary_index_task.py:111`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\recover_document_indexing_task.py:27`

No checkpoint exists before the AI call at api\tasks\recover_document_indexing_task.py:27. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\recover_document_indexing_task.py:27`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:50`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:50. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:50`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:262`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:262. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:262`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:262`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:262. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:262`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:249`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:249. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:249`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:88`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:88. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:88`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\regenerate_summary_index_task.py:219`

No checkpoint exists before the AI call at api\tasks\regenerate_summary_index_task.py:219. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\regenerate_summary_index_task.py:219`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:102`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:114`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:114. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:114`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:126`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:126. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:126`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:139`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:139. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:139`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:144`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:144. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:144`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:156`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:156. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:156`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:168`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:168. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:168`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:180`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:180. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:180`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:192`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:192. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:192`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:206`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:206. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:206`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:218`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:218. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:218`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:258`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:258. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:258`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:270`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:270. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:270`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:309`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:309. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:309`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:312`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:312. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:312`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:332`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:332. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:332`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:333`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:333. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:333`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:336`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:336. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:336`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:337`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:337. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:337`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:340`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:340. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:340`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:341`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:341. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:341`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:342`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:342. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:342`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:354`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:354. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:354`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:368`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:368. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:368`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:380`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:380. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:380`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:392`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:392. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:392`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:548`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:548. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:548`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:560`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:560. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:560`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:574`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:574. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:574`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:588`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:588. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:588`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:600`

No checkpoint exists before the AI call at api\tasks\remove_app_and_related_data_task.py:600. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_app_and_related_data_task.py:600`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_document_from_index_task.py:29`

No checkpoint exists before the AI call at api\tasks\remove_document_from_index_task.py:29. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_document_from_index_task.py:29`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\remove_document_from_index_task.py:71`

No checkpoint exists before the AI call at api\tasks\remove_document_from_index_task.py:71. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\remove_document_from_index_task.py:71`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:106`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:106. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:106`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:106`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:106. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:106`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:35`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:35. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:35`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:39`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:39. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:39`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:43`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:43. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:43`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\retry_document_indexing_task.py:77`

No checkpoint exists before the AI call at api\tasks\retry_document_indexing_task.py:77. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:77`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\retry_document_indexing_task.py:62`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\sync_website_document_indexing_task.py:32`

No checkpoint exists before the AI call at api\tasks\sync_website_document_indexing_task.py:32. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\sync_website_document_indexing_task.py:32`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\sync_website_document_indexing_task.py:61`

No checkpoint exists before the AI call at api\tasks\sync_website_document_indexing_task.py:61. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\sync_website_document_indexing_task.py:61`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\sync_website_document_indexing_task.py:49`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\trigger_subscription_refresh_tasks.py:25`

No checkpoint exists before the AI call at api\tasks\trigger_subscription_refresh_tasks.py:25. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\trigger_subscription_refresh_tasks.py:25`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\batch_import_annotations_task.py:38`

No checkpoint exists before the AI call at api\tasks\annotation\batch_import_annotations_task.py:38. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\batch_import_annotations_task.py:38`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\batch_import_annotations_task.py:57`

No checkpoint exists before the AI call at api\tasks\annotation\batch_import_annotations_task.py:57. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\batch_import_annotations_task.py:57`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\disable_annotation_reply_task.py:27`

No checkpoint exists before the AI call at api\tasks\annotation\disable_annotation_reply_task.py:27. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\disable_annotation_reply_task.py:27`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\disable_annotation_reply_task.py:34`

No checkpoint exists before the AI call at api\tasks\annotation\disable_annotation_reply_task.py:34. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\disable_annotation_reply_task.py:34`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\enable_annotation_reply_task.py:39`

No checkpoint exists before the AI call at api\tasks\annotation\enable_annotation_reply_task.py:39. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\enable_annotation_reply_task.py:39`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\annotation\enable_annotation_reply_task.py:55`

No checkpoint exists before the AI call at api\tasks\annotation\enable_annotation_reply_task.py:55. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\annotation\enable_annotation_reply_task.py:55`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:121`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:121. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:121`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:125`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:130`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:134`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:188`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\rag_pipeline_run_task.py:188. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:188`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:188`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\rag_pipeline_run_task.py:188. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:188`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:102`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\rag_pipeline_run_task.py:102. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:102`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:135`

No checkpoint exists before the AI call at api\tasks\rag_pipeline\rag_pipeline_run_task.py:135. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:135`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:139`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:144`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:148`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `scripts\stress-test\setup_all.py:140`

No checkpoint exists before the AI call at scripts\stress-test\setup_all.py:140. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `scripts\stress-test\setup_all.py:140`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `scripts\stress-test\setup_all.py:140`

No checkpoint exists before the AI call at scripts\stress-test\setup_all.py:140. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `scripts\stress-test\setup_all.py:140`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `api\commands\plugin.py:71`

An irreversible action (database_write) at line 71 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\commands\storage.py:757`

An irreversible action (database_write) at line 757 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\commands\vector.py:44`

An irreversible action (database_write) at line 44 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\configs\packaging\__init__.py:11`

An irreversible action (database_write) at line 11 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\admin.py:220`

An irreversible action (database_delete) at line 220 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\wraps.py:186`

An irreversible action (database_write) at line 186 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\app\model_config.py:170`

An irreversible action (database_write) at line 170 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\app\site.py:107`

An irreversible action (database_write) at line 107 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow.py:1069`

An irreversible action (database_write) at line 1069 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\app\workflow_draft_variable.py:244`

An irreversible action (database_write) at line 244 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\auth\oauth.py:151`

An irreversible action (database_write) at line 151 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets.py:867`

An irreversible action (database_delete) at line 867 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\datasets\datasets.py:830`

An irreversible action (database_write) at line 830 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\explore\installed_app.py:187`

An irreversible action (database_delete) at line 187 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\explore\installed_app.py:170`

An irreversible action (database_write) at line 170 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\workspace\account.py:237`

An irreversible action (database_write) at line 237 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\console\workspace\workspace.py:251`

An irreversible action (database_write) at line 251 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\controllers\web\passport.py:76`

An irreversible action (database_write) at line 76 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\indexing_runner.py:154`

An irreversible action (database_delete) at line 154 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\indexing_runner.py:67`

An irreversible action (database_write) at line 67 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\provider_manager.py:332`

An irreversible action (database_write) at line 332 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\apps\base_app_runner.py:435`

An irreversible action (database_write) at line 435 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\apps\advanced_chat\app_generator.py:205`

An irreversible action (database_write) at line 205 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\apps\pipeline\pipeline_generator.py:119`

An irreversible action (database_write) at line 119 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\apps\workflow\app_generator.py:198`

An irreversible action (database_write) at line 198 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\llm\quota.py:93`

An irreversible action (database_write) at line 93 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\app\task_pipeline\message_cycle_manager.py:148`

An irreversible action (database_write) at line 148 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\datasource\datasource_file_manager.py:100`

An irreversible action (database_write) at line 100 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\entities\provider_configuration.py:657`

An irreversible action (database_delete) at line 657 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\entities\provider_configuration.py:511`

An irreversible action (database_write) at line 511 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\helper\marketplace.py:29`

An irreversible action (external_api) at line 29 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\ops\ops_trace_manager.py:566`

An irreversible action (database_write) at line 566 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\ops\aliyun_trace\data_exporter\traceclient.py:55`

An irreversible action (database_write) at line 55 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\ops\tencent_trace\client.py:83`

An irreversible action (database_write) at line 83 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\keyword\jieba\jieba.py:130`

An irreversible action (database_delete) at line 130 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\keyword\jieba\jieba.py:131`

An irreversible action (database_write) at line 131 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\alibabacloud_mysql\alibabacloud_mysql_vector.py:194`

An irreversible action (database_delete) at line 194 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\alibabacloud_mysql\alibabacloud_mysql_vector.py:96`

An irreversible action (database_write) at line 96 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\clickzetta\clickzetta_vector.py:754`

An irreversible action (database_delete) at line 754 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\clickzetta\clickzetta_vector.py:174`

An irreversible action (database_write) at line 174 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\hologres\hologres_vector.py:163`

An irreversible action (database_delete) at line 163 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\iris\iris_vector.py:244`

An irreversible action (database_delete) at line 244 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\iris\iris_vector.py:150`

An irreversible action (database_write) at line 150 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\milvus\milvus_vector.py:191`

An irreversible action (database_delete) at line 191 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\myscale\myscale_vector.py:108`

An irreversible action (database_delete) at line 108 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\opengauss\opengauss.py:169`

An irreversible action (database_delete) at line 169 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\opengauss\opengauss.py:101`

An irreversible action (database_write) at line 101 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\oracle\oraclevector.py:218`

An irreversible action (database_delete) at line 218 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\oracle\oraclevector.py:185`

An irreversible action (database_write) at line 185 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pgvector\pgvector.py:157`

An irreversible action (database_delete) at line 157 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pgvector\pgvector.py:107`

An irreversible action (database_write) at line 107 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pgvecto_rs\pgvecto_rs.py:149`

An irreversible action (database_delete) at line 149 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pgvecto_rs\pgvecto_rs.py:60`

An irreversible action (database_write) at line 60 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pyvastbase\vastbase_vector.py:143`

An irreversible action (database_delete) at line 143 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\pyvastbase\vastbase_vector.py:94`

An irreversible action (database_write) at line 94 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\relyt\relyt_vector.py:107`

An irreversible action (database_write) at line 107 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tencent\tencent_vector.py:302`

An irreversible action (database_delete) at line 302 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_on_qdrant_vector.py:437`

An irreversible action (database_write) at line 437 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_on_qdrant_vector.py:505`

An irreversible action (external_api) at line 505 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_service.py:190`

An irreversible action (database_write) at line 190 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\tidb_vector\tidb_vector.py:118`

An irreversible action (database_write) at line 118 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\vikingdb\vikingdb_vector.py:208`

An irreversible action (database_delete) at line 208 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:339`

An irreversible action (database_delete) at line 339 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\embedding\cached_embedding.py:99`

An irreversible action (database_write) at line 99 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\extractor\notion_extractor.py:355`

An irreversible action (database_write) at line 355 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\extractor\notion_extractor.py:104`

An irreversible action (external_api) at line 104 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\extractor\pdf_extractor.py:176`

An irreversible action (database_write) at line 176 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\extractor\word_extractor.py:159`

An irreversible action (database_write) at line 159 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\index_processor\processor\parent_child_index_processor.py:204`

An irreversible action (database_write) at line 204 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\rag\retrieval\dataset_retrieval.py:980`

An irreversible action (database_write) at line 980 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\repositories\sqlalchemy_workflow_node_execution_repository.py:56`

An irreversible action (database_write) at line 56 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\tools\tool_engine.py:366`

An irreversible action (database_write) at line 366 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\tools\tool_file_manager.py:112`

An irreversible action (database_write) at line 112 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\tools\tool_manager.py:320`

An irreversible action (database_write) at line 320 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\tools\workflow_as_tool\provider.py:219`

An irreversible action (database_write) at line 219 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\core\workflow\node_factory.py:207`

An irreversible action (database_write) at line 207 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\create_installed_app_when_app_created.py:16`

An irreversible action (database_write) at line 16 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\create_site_record_when_app_created.py:27`

An irreversible action (database_write) at line 27 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\sync_workflow_schedule_when_app_published.py:62`

An irreversible action (database_write) at line 62 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\update_app_dataset_join_when_app_model_config_updated.py:43`

An irreversible action (database_write) at line 43 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\update_app_dataset_join_when_app_published_workflow_updated.py:43`

An irreversible action (database_write) at line 43 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\update_app_triggers_when_app_published_workflow_updated.py:57`

An irreversible action (database_delete) at line 57 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\events\event_handlers\update_app_triggers_when_app_published_workflow_updated.py:82`

An irreversible action (database_write) at line 82 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\extensions\ext_mail.py:58`

An irreversible action (email_send) at line 58 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\extensions\ext_otel.py:60`

An irreversible action (database_write) at line 60 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\extensions\ext_sentry.py:44`

An irreversible action (database_write) at line 44 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\extensions\logstore\aliyun_logstore_pg.py:86`

An irreversible action (database_write) at line 86 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\libs\smtp.py:50`

An irreversible action (email_send) at line 50 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\models\model.py:467`

An irreversible action (database_write) at line 467 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\models\workflow.py:1258`

An irreversible action (database_write) at line 1258 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\clean_embedding_cache_task.py:33`

An irreversible action (database_delete) at line 33 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\clean_embedding_cache_task.py:36`

An irreversible action (database_write) at line 36 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\clean_unused_datasets_task.py:148`

An irreversible action (database_write) at line 148 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\clean_workflow_runlogs_precise.py:51`

An irreversible action (database_write) at line 51 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\create_tidb_serverless_task.py:64`

An irreversible action (database_write) at line 64 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\mail_clean_document_notify_task.py:96`

An irreversible action (database_write) at line 96 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\trigger_provider_refresh_task.py:62`

An irreversible action (database_write) at line 62 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\update_api_token_last_used_task.py:85`

An irreversible action (database_write) at line 85 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\schedule\workflow_schedule_task.py:27`

An irreversible action (database_write) at line 27 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\account_service.py:429`

An irreversible action (database_delete) at line 429 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\account_service.py:173`

An irreversible action (database_write) at line 173 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:316`

An irreversible action (database_delete) at line 316 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\annotation_service.py:96`

An irreversible action (database_write) at line 96 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\app_dsl_service.py:474`

An irreversible action (database_write) at line 474 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\app_service.py:371`

An irreversible action (database_delete) at line 371 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\app_service.py:170`

An irreversible action (database_write) at line 170 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\clear_free_plan_tenant_expired_logs.py:155`

An irreversible action (database_write) at line 155 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\conversation_service.py:198`

An irreversible action (database_delete) at line 198 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\conversation_service.py:133`

An irreversible action (database_write) at line 133 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\credit_pool_service.py:26`

An irreversible action (database_write) at line 26 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\dataset_service.py:293`

An irreversible action (database_write) at line 293 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:996`

An irreversible action (database_delete) at line 996 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\datasource_provider_service.py:61`

An irreversible action (database_write) at line 61 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\file_service.py:265`

An irreversible action (database_delete) at line 265 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\file_service.py:115`

An irreversible action (database_write) at line 115 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\file_service.py:363`

An irreversible action (file_system) at line 363 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\human_input_service.py:219`

An irreversible action (database_write) at line 219 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\ops_service.py:273`

An irreversible action (database_delete) at line 273 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\ops_service.py:208`

An irreversible action (database_write) at line 208 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\webapp_auth_service.py:112`

An irreversible action (database_write) at line 112 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:362`

An irreversible action (database_delete) at line 362 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\workflow_draft_variable_service.py:116`

An irreversible action (database_write) at line 116 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\workflow_service.py:1523`

An irreversible action (database_delete) at line 1523 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\workflow_service.py:100`

An irreversible action (database_write) at line 100 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\pipeline_generate_service.py:117`

An irreversible action (database_write) at line 117 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:205`

An irreversible action (database_delete) at line 205 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline.py:104`

An irreversible action (database_write) at line 104 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\rag_pipeline\rag_pipeline_dsl_service.py:342`

An irreversible action (database_write) at line 342 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\retention\conversation\messages_clean_service.py:365`

An irreversible action (database_write) at line 365 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\retention\workflow_run\archive_paid_plan_workflow_run.py:194`

An irreversible action (database_write) at line 194 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\retention\workflow_run\clear_free_plan_expired_workflow_run_logs.py:216`

An irreversible action (database_write) at line 216 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:395`

An irreversible action (database_delete) at line 395 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\tools\builtin_tools_manage_service.py:55`

An irreversible action (database_write) at line 55 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\tools\workflow_tools_manage_service.py:89`

An irreversible action (database_write) at line 89 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\trigger\schedule_service.py:128`

An irreversible action (database_delete) at line 128 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:386`

An irreversible action (database_delete) at line 386 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\trigger\trigger_provider_service.py:70`

An irreversible action (database_write) at line 70 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\trigger\webhook_service.py:937`

An irreversible action (database_delete) at line 937 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\trigger\webhook_service.py:932`

An irreversible action (database_write) at line 932 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\services\workflow\workflow_converter.py:103`

An irreversible action (database_write) at line 103 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\async_workflow_tasks.py:127`

An irreversible action (database_write) at line 127 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_index_update_task.py:52`

An irreversible action (database_write) at line 52 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\deal_dataset_vector_index_task.py:55`

An irreversible action (database_write) at line 55 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\delete_segment_from_index_task.py:81`

An irreversible action (database_write) at line 81 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\disable_segments_from_index_task.py:101`

An irreversible action (database_write) at line 101 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\disable_segment_from_index_task.py:85`

An irreversible action (database_write) at line 85 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\document_indexing_task.py:90`

An irreversible action (database_write) at line 90 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\duplicate_document_indexing_task.py:120`

An irreversible action (database_write) at line 120 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\human_input_timeout_tasks.py:60`

An irreversible action (database_write) at line 60 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\mail_human_input_delivery_task.py:121`

An irreversible action (database_write) at line 121 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:453`

An irreversible action (database_delete) at line 453 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\remove_app_and_related_data_task.py:326`

An irreversible action (database_write) at line 326 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\remove_document_from_index_task.py:79`

An irreversible action (database_write) at line 79 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:119`

An irreversible action (database_write) at line 119 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `api\tasks\rag_pipeline\rag_pipeline_run_task.py:159`

An irreversible action (database_write) at line 159 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `scripts\stress-test\setup_all.py:26`

An irreversible action (system_command) at line 26 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `web\public\vs\language\typescript\tsWorker.js:3324`

An irreversible action (database_write) at line 3324 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\commands\plugin.py:473`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\apikey.py:94`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\apikey.py:94`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\app\conversation.py:357`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\conversation.py:357`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\app\conversation.py:481`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\conversation.py:481`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:72`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:101`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:133`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\app\generator.py:184`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:184`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\app\generator.py:193`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:193`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\generator.py:202`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\mcp_server.py:81`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:344`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:384`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:422`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:460`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:712`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow.py:1192`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\app\workflow_run.py:272`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow_run.py:272`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\app\workflow_trigger.py:70`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\datasets\datasets.py:824`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets.py:824`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets.py:744`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets_document.py:733`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets_document.py:679`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets_document.py:335`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets_document.py:815`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\datasets_document.py:849`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:72`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:80`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:109`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:35`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:48`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:90`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline.py:90`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_datasets.py:59`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:48`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_import.py:145`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:165`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:533`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:579`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:596`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:625`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:810`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:830`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:850`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:871`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:900`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:919`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:939`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:967`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1014`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:1031`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:210`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:210`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:248`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:283`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:318`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:709`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:752`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:955`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:467`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\datasets\rag_pipeline\rag_pipeline_workflow.py:500`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\controllers\console\workspace\account.py:410`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\console\workspace\account.py:410`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\service_api\dataset\document.py:764`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\service_api\dataset\document.py:799`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\service_api\dataset\rag_pipeline\rag_pipeline_workflow.py:133`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\trigger\webhook.py:60`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\controllers\trigger\webhook.py:131`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\indexing_runner.py:538`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\indexing_runner.py:614`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\base_app_runner.py:542`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\message_based_app_generator.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\app_generator.py:685`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\app_runner.py:281`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\app\apps\advanced_chat\app_runner.py:320`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\app_runner.py:320`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:627`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:218`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:706`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:895`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:652`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:652`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:655`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:655`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1037`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1039`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1043`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1048`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\advanced_chat\generate_task_pipeline.py:1038`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\app\apps\agent_chat\app_runner.py:104`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\agent_chat\app_runner.py:104`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\app\apps\chat\app_runner.py:114`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\chat\app_runner.py:114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\common\workflow_response_converter.py:506`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_config_manager.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_generator.py:120`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_generator.py:235`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_generator.py:651`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_runner.py:164`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\pipeline\pipeline_runner.py:141`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\workflow\app_generator.py:637`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\apps\workflow\generate_task_pipeline.py:645`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:125`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:125`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\task_pipeline\easy_ui_based_generate_task_pipeline.py:513`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\app\task_pipeline\message_cycle_manager.py:139`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\app\task_pipeline\message_cycle_manager.py:139`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\datasource\datasource_manager.py:349`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\datasource\datasource_manager.py:349`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\external_data_tool\external_data_fetch.py:87`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\llm_generator\llm_generator.py:457`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\ops_trace_manager.py:767`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\arize_phoenix_trace\arize_phoenix_trace.py:210`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\langfuse_trace\langfuse_trace.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\langsmith_trace\langsmith_trace.py:64`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\ops\mlflow_trace\mlflow_trace.py:105`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\mlflow_trace\mlflow_trace.py:105`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\opik_trace\opik_trace.py:112`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\ops\weave_trace\weave_trace.py:96`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\ops\weave_trace\weave_trace.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:854`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:878`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:243`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:243`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:857`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:882`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\retrieval_service.py:577`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:201`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:257`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\analyticdb\analyticdb_vector_openapi.py:294`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\chroma\chroma_vector.py:101`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\chroma\chroma_vector.py:107`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:232`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:253`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:253`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:269`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:269`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:243`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\couchbase\couchbase_vector.py:243`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\milvus\milvus_vector.py:200`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\milvus\milvus_vector.py:200`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\milvus\milvus_vector.py:179`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\milvus\milvus_vector.py:179`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:101`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:101`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:101`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:112`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:112`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:112`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:153`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:153`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\tencent\tencent_vector.py:202`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\upstash\upstash_vector.py:76`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\upstash\upstash_vector.py:76`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\upstash\upstash_vector.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\datasource\vdb\upstash\upstash_vector.py:97`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\upstash\upstash_vector.py:97`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:352`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:399`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:445`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:445`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\embedding\cached_embedding.py:34`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\embedding\cached_embedding.py:89`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:66`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:66`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:66`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:121`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:157`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\index_processor.py:107`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\paragraph_index_processor.py:101`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\index_processor\processor\paragraph_index_processor.py:213`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\paragraph_index_processor.py:213`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\paragraph_index_processor.py:228`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:118`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:289`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:297`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:81`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:157`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\index_processor\processor\qa_index_processor.py:218`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\qa_index_processor.py:266`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\qa_index_processor.py:273`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\index_processor\processor\qa_index_processor.py:162`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:281`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:281`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:282`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:282`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:976`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:1828`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:1841`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\summary_index\summary_index.py:80`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\summary_index\summary_index.py:42`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\summary_index\summary_index.py:24`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\summary_index\summary_index.py:37`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\rag\summary_index\summary_index.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_file_manager.py:170`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_file_manager.py:194`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_file_manager.py:214`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_file_manager.py:238`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:1037`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:1039`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:1034`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:1041`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:688`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\core\tools\tool_manager.py:1045`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\tool_manager.py:1045`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\builtin_tool\tool.py:105`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\utils\dataset_retriever\dataset_multi_retriever_tool.py:92`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\workflow_as_tool\provider.py:100`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\workflow_as_tool\provider.py:221`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\tools\workflow_as_tool\tool.py:315`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\workflow\system_variables.py:131`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\workflow\nodes\trigger_webhook\node.py:151`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\workflow\nodes\trigger_webhook\node.py:151`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\core\workflow\nodes\trigger_webhook\node.py:164`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\core\workflow\nodes\trigger_webhook\node.py:164`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\events\event_handlers\create_site_record_when_app_created.py:21`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\extensions\storage\aws_s3_storage.py:23`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\extensions\storage\aws_s3_storage.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\extensions\storage\oracle_oci_storage.py:17`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\libs\archive_storage.py:215`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\libs\archive_storage.py:215`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\libs\rsa.py:14`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\models\workflow.py:495`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\models\workflow.py:654`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:117`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:139`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:144`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:148`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:135`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\schedule\trigger_provider_refresh_task.py:45`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:327`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:685`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:700`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:716`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:732`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:1238`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:1073`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:1123`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\account_service.py:1196`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:55`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\annotation_service.py:155`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:155`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\annotation_service.py:261`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:261`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\annotation_service.py:303`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:303`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:341`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:364`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:377`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:402`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\annotation_service.py:526`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:526`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:554`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\annotation_service.py:574`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:574`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\annotation_service.py:597`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:597`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:634`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\annotation_service.py:682`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_dsl_service.py:627`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\app_generate_service.py:129`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:129`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:138`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:169`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:183`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:234`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:219`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\app_generate_service.py:185`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\billing_service.py:386`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:350`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:350`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:66`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:66`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:106`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:106`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:150`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:150`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:150`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:190`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:190`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:326`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:326`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:440`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:415`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:415`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:125`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:125`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:125`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:166`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:166`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:166`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:299`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:299`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:606`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:640`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:641`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3730`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3730`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3730`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:337`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3415`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3415`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:2523`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3236`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3236`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3812`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:228`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:228`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:347`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:599`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:634`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:1694`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:2521`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:2653`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:2653`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3564`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3564`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3657`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3900`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3900`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3900`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3938`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3938`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3938`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:118`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:304`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:304`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:545`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:1400`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:1444`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3201`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3513`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3513`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3634`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3732`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3732`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3732`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:4037`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:1858`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3147`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3147`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3147`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\dataset_service.py:3225`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3225`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3545`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3612`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3984`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:4010`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\dataset_service.py:3493`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3493`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:186`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\dataset_service.py:3395`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:557`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:557`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:628`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:628`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:388`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:711`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:711`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\datasource_provider_service.py:884`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:884`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:991`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:56`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:56`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:238`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:280`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:319`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\datasource_provider_service.py:370`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:370`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:432`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:927`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\datasource_provider_service.py:359`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:359`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\datasource_provider_service.py:452`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:452`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:452`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:494`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:494`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:723`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:178`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:637`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:637`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:118`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\datasource_provider_service.py:565`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:565`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:518`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\datasource_provider_service.py:579`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\end_user_service.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\end_user_service.py:141`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\end_user_service.py:61`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\knowledge_service.py:19`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\message_service.py:316`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:61`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:651`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:651`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:756`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:795`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:835`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:898`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:975`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1226`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:97`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:97`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:539`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:591`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:591`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1173`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1199`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1253`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1300`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:627`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:923`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:1065`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1065`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:698`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\summary_index_service.py:698`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:698`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\summary_index_service.py:1034`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:1034`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:297`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:311`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:475`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\summary_index_service.py:488`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:280`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:302`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:258`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:258`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:492`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:502`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:544`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:592`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:592`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:226`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:330`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\workflow_draft_variable_service.py:330`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_auto_upgrade_service.py:12`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_auto_upgrade_service.py:28`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_auto_upgrade_service.py:56`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:59`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:59`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:228`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:228`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:242`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:265`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:273`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:141`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:116`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_migration.py:116`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_parameter_service.py:60`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_parameter_service.py:70`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_permission_service.py:11`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\plugin\plugin_permission_service.py:21`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_generate_service.py:94`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:1153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:115`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:123`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:138`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:149`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:118`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:122`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:137`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:148`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:435`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:656`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:420`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:583`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:584`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:240`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:720`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:685`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:924`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:924`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:323`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:460`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_transform_service.py:55`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_transform_service.py:268`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_transform_service.py:218`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\rag_pipeline_transform_service.py:219`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:22`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\built_in\built_in_retrieval.py:26`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:18`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:22`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\customized\customized_retrieval.py:51`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:16`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:20`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\database\database_retrieval.py:52`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:21`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:24`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\rag_pipeline\pipeline_template\remote\remote_retrieval.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:50`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:50`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:156`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:384`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:414`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:437`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:437`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:451`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:451`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:476`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:498`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:498`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:704`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:313`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:593`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:606`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\builtin_tools_manage_service.py:627`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\tools\mcp_tools_manage_service.py:288`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:356`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:356`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:408`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:408`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:483`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:483`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:561`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:561`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:587`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:587`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:611`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:611`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:611`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:645`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:701`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:737`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:757`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:774`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:249`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:249`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:323`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:326`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:73`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:82`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:155`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\trigger_provider_service.py:155`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\webhook_service.py:96`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\webhook_service.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\webhook_service.py:923`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\services\trigger\webhook_service.py:114`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\services\trigger\webhook_service.py:114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:33`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:33`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:107`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:107`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:112`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\add_document_to_index_task.py:112`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\async_workflow_tasks.py:160`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\batch_clean_document_task.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\batch_clean_document_task.py:76`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\batch_clean_document_task.py:76`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\batch_create_segment_to_index_task.py:142`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\batch_create_segment_to_index_task.py:142`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\batch_create_segment_to_index_task.py:144`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\batch_create_segment_to_index_task.py:144`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:154`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:155`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:157`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:158`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:161`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:162`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:177`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:115`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:115`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_dataset_task.py:115`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_document_task.py:127`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\clean_document_task.py:35`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_document_task.py:35`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\clean_document_task.py:66`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_document_task.py:66`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\clean_document_task.py:97`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_document_task.py:97`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\clean_notion_document_task.py:29`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\clean_notion_document_task.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:30`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:30`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:42`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:42`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:84`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\create_segment_to_index_task.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:29`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:49`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:95`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:95`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:108`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:84`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:89`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:89`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:176`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:176`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:58`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:181`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:181`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_index_update_task.py:120`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:32`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:52`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:107`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:85`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:85`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:90`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:90`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:175`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:175`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:61`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:180`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:180`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:119`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_account_task.py:17`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:32`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:36`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:36`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:40`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:40`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:44`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:44`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:46`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:50`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_conversation_task.py:52`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_segment_from_index_task.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_segment_from_index_task.py:37`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_segment_from_index_task.py:64`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\delete_segment_from_index_task.py:80`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\delete_segment_from_index_task.py:80`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:30`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:30`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:35`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:35`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:62`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:90`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\disable_segments_from_index_task.py:90`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\disable_segment_from_index_task.py:27`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\disable_segment_from_index_task.py:27`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:35`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:35`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:45`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:45`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:123`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:123`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:123`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:90`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:115`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:115`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:115`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:143`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:143`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:153`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_sync_task.py:153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_task.py:60`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_task.py:60`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_task.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_task.py:125`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_task.py:125`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_task.py:138`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_update_task.py:31`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_update_task.py:31`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\document_indexing_update_task.py:40`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\document_indexing_update_task.py:40`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\duplicate_document_indexing_task.py:85`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\duplicate_document_indexing_task.py:85`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:33`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:33`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:38`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:38`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:126`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\enable_segments_to_index_task.py:126`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\enable_segment_to_index_task.py:32`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\enable_segment_to_index_task.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:88`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:88`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:42`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:42`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:47`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:47`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:111`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\generate_summary_index_task.py:111`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\recover_document_indexing_task.py:27`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\recover_document_indexing_task.py:27`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:50`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:50`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:50`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:262`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:262`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:249`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:88`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:88`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:88`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\regenerate_summary_index_task.py:219`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:114`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:114`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:126`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:139`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:144`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:156`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:168`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:180`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:192`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:206`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:218`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:258`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:270`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:309`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:312`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:332`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:332`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:332`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:333`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:333`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:333`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:336`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:336`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:336`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:337`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:337`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:337`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:340`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:340`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:340`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:341`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:341`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:341`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:342`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:342`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:342`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:354`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:354`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:368`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:368`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:380`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:392`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:548`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:560`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:574`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:588`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_app_and_related_data_task.py:600`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\remove_document_from_index_task.py:29`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_document_from_index_task.py:29`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\remove_document_from_index_task.py:71`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:106`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:35`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:35`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:39`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:39`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:43`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:43`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:77`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\retry_document_indexing_task.py:77`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\sync_website_document_indexing_task.py:32`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\sync_website_document_indexing_task.py:32`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\sync_website_document_indexing_task.py:61`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\sync_website_document_indexing_task.py:61`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\trigger_subscription_refresh_tasks.py:25`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\annotation\batch_import_annotations_task.py:38`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\annotation\batch_import_annotations_task.py:38`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\batch_import_annotations_task.py:38`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `api\tasks\annotation\batch_import_annotations_task.py:57`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\batch_import_annotations_task.py:57`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\annotation\disable_annotation_reply_task.py:27`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\disable_annotation_reply_task.py:27`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\annotation\disable_annotation_reply_task.py:34`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\disable_annotation_reply_task.py:34`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\annotation\enable_annotation_reply_task.py:39`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\enable_annotation_reply_task.py:39`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\annotation\enable_annotation_reply_task.py:55`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\annotation\enable_annotation_reply_task.py:55`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:174`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:90`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:121`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:121`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\rag_pipeline_run_task.py:188`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\rag_pipeline_run_task.py:102`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `api\tasks\rag_pipeline\rag_pipeline_run_task.py:135`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `api\tasks\rag_pipeline\rag_pipeline_run_task.py:135`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `scripts\stress-test\setup_all.py:140`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `scripts\stress-test\setup_all.py:140`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `786 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\commands\plugin.py:71`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\commands\storage.py:757`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\commands\vector.py:44`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\configs\packaging\__init__.py:11`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\admin.py:220`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\wraps.py:186`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\app\model_config.py:170`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\app\site.py:107`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\app\workflow.py:1069`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\app\workflow_draft_variable.py:244`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\auth\oauth.py:151`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\datasets\datasets.py:867`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\datasets\datasets.py:830`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\explore\installed_app.py:187`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\explore\installed_app.py:170`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\workspace\account.py:237`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\console\workspace\workspace.py:251`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\controllers\web\passport.py:76`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\indexing_runner.py:154`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\indexing_runner.py:67`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\provider_manager.py:332`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\apps\base_app_runner.py:435`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\apps\advanced_chat\app_generator.py:205`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\apps\pipeline\pipeline_generator.py:119`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\apps\workflow\app_generator.py:198`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\llm\quota.py:93`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\app\task_pipeline\message_cycle_manager.py:148`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\datasource\datasource_file_manager.py:100`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\entities\provider_configuration.py:657`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\entities\provider_configuration.py:511`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\helper\marketplace.py:29`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\ops\ops_trace_manager.py:566`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\ops\aliyun_trace\data_exporter\traceclient.py:55`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\ops\tencent_trace\client.py:83`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\keyword\jieba\jieba.py:130`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\keyword\jieba\jieba.py:131`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\alibabacloud_mysql\alibabacloud_mysql_vector.py:194`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\alibabacloud_mysql\alibabacloud_mysql_vector.py:96`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\clickzetta\clickzetta_vector.py:754`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\clickzetta\clickzetta_vector.py:174`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\hologres\hologres_vector.py:163`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\iris\iris_vector.py:244`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\iris\iris_vector.py:150`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\milvus\milvus_vector.py:191`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\myscale\myscale_vector.py:108`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\opengauss\opengauss.py:169`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\opengauss\opengauss.py:101`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\oracle\oraclevector.py:218`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\oracle\oraclevector.py:185`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pgvector\pgvector.py:157`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pgvector\pgvector.py:107`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pgvecto_rs\pgvecto_rs.py:149`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pgvecto_rs\pgvecto_rs.py:60`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pyvastbase\vastbase_vector.py:143`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\pyvastbase\vastbase_vector.py:94`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\relyt\relyt_vector.py:107`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\tencent\tencent_vector.py:302`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_on_qdrant_vector.py:437`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_on_qdrant_vector.py:505`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\tidb_on_qdrant\tidb_service.py:190`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\tidb_vector\tidb_vector.py:118`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\vikingdb\vikingdb_vector.py:208`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\datasource\vdb\weaviate\weaviate_vector.py:339`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\embedding\cached_embedding.py:99`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\extractor\notion_extractor.py:355`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\extractor\notion_extractor.py:104`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\extractor\pdf_extractor.py:176`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\extractor\word_extractor.py:159`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\index_processor\processor\parent_child_index_processor.py:204`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\rag\retrieval\dataset_retrieval.py:980`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\repositories\sqlalchemy_workflow_node_execution_repository.py:56`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\tools\tool_engine.py:366`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\tools\tool_file_manager.py:112`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\tools\tool_manager.py:320`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\tools\workflow_as_tool\provider.py:219`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\core\workflow\node_factory.py:207`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\create_installed_app_when_app_created.py:16`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\create_site_record_when_app_created.py:27`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\sync_workflow_schedule_when_app_published.py:62`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\update_app_dataset_join_when_app_model_config_updated.py:43`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\update_app_dataset_join_when_app_published_workflow_updated.py:43`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\update_app_triggers_when_app_published_workflow_updated.py:57`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\events\event_handlers\update_app_triggers_when_app_published_workflow_updated.py:82`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\extensions\ext_mail.py:58`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\extensions\ext_otel.py:60`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\extensions\ext_sentry.py:44`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\extensions\logstore\aliyun_logstore_pg.py:86`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\libs\smtp.py:50`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\models\model.py:467`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\models\workflow.py:1258`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\clean_embedding_cache_task.py:33`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\clean_embedding_cache_task.py:36`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\clean_unused_datasets_task.py:148`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\clean_workflow_runlogs_precise.py:51`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\create_tidb_serverless_task.py:64`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\mail_clean_document_notify_task.py:96`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\trigger_provider_refresh_task.py:62`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\update_api_token_last_used_task.py:85`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\schedule\workflow_schedule_task.py:27`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\account_service.py:429`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\account_service.py:173`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\annotation_service.py:316`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\annotation_service.py:96`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\app_dsl_service.py:474`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\app_service.py:371`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\app_service.py:170`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\clear_free_plan_tenant_expired_logs.py:155`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\conversation_service.py:198`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\conversation_service.py:133`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\credit_pool_service.py:26`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\dataset_service.py:293`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\datasource_provider_service.py:996`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\datasource_provider_service.py:61`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\file_service.py:265`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\file_service.py:115`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\file_service.py:363`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\human_input_service.py:219`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\ops_service.py:273`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\ops_service.py:208`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\webapp_auth_service.py:112`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\workflow_draft_variable_service.py:362`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\workflow_draft_variable_service.py:116`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\workflow_service.py:1523`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\workflow_service.py:100`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\rag_pipeline\pipeline_generate_service.py:117`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:205`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\rag_pipeline\rag_pipeline.py:104`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\rag_pipeline\rag_pipeline_dsl_service.py:342`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\retention\conversation\messages_clean_service.py:365`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\retention\workflow_run\archive_paid_plan_workflow_run.py:194`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\retention\workflow_run\clear_free_plan_expired_workflow_run_logs.py:216`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\tools\builtin_tools_manage_service.py:395`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\tools\builtin_tools_manage_service.py:55`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\tools\workflow_tools_manage_service.py:89`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\trigger\schedule_service.py:128`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\trigger\trigger_provider_service.py:386`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\trigger\trigger_provider_service.py:70`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\trigger\webhook_service.py:937`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\trigger\webhook_service.py:932`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\services\workflow\workflow_converter.py:103`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\async_workflow_tasks.py:127`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\deal_dataset_index_update_task.py:52`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\deal_dataset_vector_index_task.py:55`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\delete_segment_from_index_task.py:81`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\disable_segments_from_index_task.py:101`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\disable_segment_from_index_task.py:85`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\document_indexing_task.py:90`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\duplicate_document_indexing_task.py:120`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\human_input_timeout_tasks.py:60`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\mail_human_input_delivery_task.py:121`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\remove_app_and_related_data_task.py:453`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\remove_app_and_related_data_task.py:326`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\remove_document_from_index_task.py:79`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\rag_pipeline\priority_rag_pipeline_run_task.py:119`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `api\tasks\rag_pipeline\rag_pipeline_run_task.py:159`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `scripts\stress-test\setup_all.py:26`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `web\public\vs\language\typescript\tsWorker.js:3324`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

---

## Governance score

**Structural Gamma proxy:** 0.01

Only 1% of decision points are governed. The system is structurally ungoverned. The Drift Node is the global energy minimum.

> Structural proxy only — not runtime Gamma. Measures whether governance mechanisms are structurally present.

---

## Next steps

1. Fill in the null fields in `.verba/governance.yaml`
2. Complete the test stubs in `.verba/test_case_matrix.yaml`
3. Open in Verba Studio for AI-assisted policy authoring
4. Add `x-verba qa . --schema .verba/governance.yaml` to your CI/CD pipeline (coming v0.2)

*Generated by X-Verba — https://github.com/4vish/x-verba*