# X-Verba Governance Report
*Generated 2026-04-03T08:29:19.604393+00:00 by Super Semantics*

**Repository:** `C:\Users\OEM\lerobot`  
**Identity Key:** `lerobot-2776bcfa`  
**Context Profile:** `ai-app`

---

## What we found

X-Verba scanned **332 files** and found **172 AI integration points**.

| Metric | Value |
| --- | --- |
| Critical findings | **155** |
| High findings | 172 |
| Governance coverage | 0% |
| Structural Gamma proxy | 0.0 (below threshold) |

---

## Governance gaps

### 🔴 CRITICAL — `src\lerobot\async_inference\policy_server.py:324`

No checkpoint exists before the AI call at src\lerobot\async_inference\policy_server.py:324. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\async_inference\policy_server.py:324`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:177`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:177. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:177`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:175`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:175. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:175`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:177`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:177. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:177`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:220`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:220. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:220`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:367`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:629`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:180`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:180. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:180`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\cameras\realsense\camera_realsense.py:235`

No checkpoint exists before the AI call at src\lerobot\cameras\realsense\camera_realsense.py:235. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:235`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\cameras\realsense\camera_realsense.py:629`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\datasets\pipeline_features.py:94`

No checkpoint exists before the AI call at src\lerobot\datasets\pipeline_features.py:94. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\datasets\pipeline_features.py:94`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:288`

No checkpoint exists before the AI call at src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:288. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:288`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:292`

No checkpoint exists before the AI call at src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:292. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:292`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:431`

No checkpoint exists before the AI call at src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:431. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:431`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi_gemma.py:261`

No checkpoint exists before the AI call at src\lerobot\policies\pi_gemma.py:261. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi_gemma.py:261`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi_gemma.py:315`

No checkpoint exists before the AI call at src\lerobot\policies\pi_gemma.py:315. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi_gemma.py:315`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi_gemma.py:145`

No checkpoint exists before the AI call at src\lerobot\policies\pi_gemma.py:145. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi_gemma.py:145`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi_gemma.py:146`

No checkpoint exists before the AI call at src\lerobot\policies\pi_gemma.py:146. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi_gemma.py:146`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\pi_gemma.py:250`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pretrained.py:229`

No checkpoint exists before the AI call at src\lerobot\policies\pretrained.py:229. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pretrained.py:229`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\act\modeling_act.py:110`

No checkpoint exists before the AI call at src\lerobot\policies\act\modeling_act.py:110. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\act\modeling_act.py:110`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\act\modeling_act.py:117`

No checkpoint exists before the AI call at src\lerobot\policies\act\modeling_act.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\act\modeling_act.py:117`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\diffusion\modeling_diffusion.py:98`

No checkpoint exists before the AI call at src\lerobot\policies\diffusion\modeling_diffusion.py:98. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\diffusion\modeling_diffusion.py:98`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\diffusion\modeling_diffusion.py:135`

No checkpoint exists before the AI call at src\lerobot\policies\diffusion\modeling_diffusion.py:135. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\diffusion\modeling_diffusion.py:135`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\groot_n1.py:84`

No checkpoint exists before the AI call at src\lerobot\policies\groot\groot_n1.py:84. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\groot_n1.py:84`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\groot_n1.py:85`

No checkpoint exists before the AI call at src\lerobot\policies\groot\groot_n1.py:85. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\groot_n1.py:85`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\groot_n1.py:132`

No checkpoint exists before the AI call at src\lerobot\policies\groot\groot_n1.py:132. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\groot_n1.py:132`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\groot_n1.py:163`

No checkpoint exists before the AI call at src\lerobot\policies\groot\groot_n1.py:163. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\groot_n1.py:163`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\modeling_groot.py:291`

No checkpoint exists before the AI call at src\lerobot\policies\groot\modeling_groot.py:291. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\modeling_groot.py:291`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\processor_groot.py:210`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:257`

No checkpoint exists before the AI call at src\lerobot\policies\groot\action_head\flow_matching_action_head.py:257. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:257`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:343`

No checkpoint exists before the AI call at src\lerobot\policies\groot\action_head\flow_matching_action_head.py:343. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:343`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:398`

No checkpoint exists before the AI call at src\lerobot\policies\groot\action_head\flow_matching_action_head.py:398. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:398`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:26`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:26. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:26`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:73`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:73. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:73`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:78`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:80`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:82`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:40`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:42`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:87`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:123`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:123. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:123`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:163`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:163. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:163`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:188`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:188. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:188`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:227`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:227. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:227`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:247`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:247. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:247`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:418`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:418. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:418`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:380`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:380. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:380`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:404`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:404. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:404`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:411`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:411. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:411`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:26`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:26. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:26`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:47`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:47. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:47`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:279`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:279. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:279`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:363`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:363. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:363`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:108`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:108. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:108`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:116`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:124`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:126`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:34`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:34. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:34`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:400`

No checkpoint exists before the AI call at src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:400. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:400`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:201`

No checkpoint exists before the AI call at src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:201. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:201`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:227`

No checkpoint exists before the AI call at src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:227. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:227`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:176`

No checkpoint exists before the AI call at src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:176. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:176`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0\modeling_pi0.py:261`

No checkpoint exists before the AI call at src\lerobot\policies\pi0\modeling_pi0.py:261. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0\modeling_pi0.py:261`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0\modeling_pi0.py:267`

No checkpoint exists before the AI call at src\lerobot\policies\pi0\modeling_pi0.py:267. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0\modeling_pi0.py:267`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0\modeling_pi0.py:1014`

No checkpoint exists before the AI call at src\lerobot\policies\pi0\modeling_pi0.py:1014. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0\modeling_pi0.py:1014`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0\modeling_pi0.py:1253`

No checkpoint exists before the AI call at src\lerobot\policies\pi0\modeling_pi0.py:1253. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0\modeling_pi0.py:1253`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi05\modeling_pi05.py:258`

No checkpoint exists before the AI call at src\lerobot\policies\pi05\modeling_pi05.py:258. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi05\modeling_pi05.py:258`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi05\modeling_pi05.py:264`

No checkpoint exists before the AI call at src\lerobot\policies\pi05\modeling_pi05.py:264. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi05\modeling_pi05.py:264`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi05\modeling_pi05.py:985`

No checkpoint exists before the AI call at src\lerobot\policies\pi05\modeling_pi05.py:985. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi05\modeling_pi05.py:985`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi05\modeling_pi05.py:1224`

No checkpoint exists before the AI call at src\lerobot\policies\pi05\modeling_pi05.py:1224. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi05\modeling_pi05.py:1224`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:837`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:842`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:915`

No checkpoint exists before the AI call at src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:915. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:915`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:1275`

No checkpoint exists before the AI call at src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:1275. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:1275`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sac\modeling_sac.py:942`

No checkpoint exists before the AI call at src\lerobot\policies\sac\modeling_sac.py:942. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sac\modeling_sac.py:942`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:117`

No checkpoint exists before the AI call at src\lerobot\policies\sac\reward_model\modeling_classifier.py:117. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:117`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:243`

No checkpoint exists before the AI call at src\lerobot\policies\sac\reward_model\modeling_classifier.py:243. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:243`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:279`

No checkpoint exists before the AI call at src\lerobot\policies\sac\reward_model\modeling_classifier.py:279. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:279`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:283`

No checkpoint exists before the AI call at src\lerobot\policies\sac\reward_model\modeling_classifier.py:283. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sac\reward_model\modeling_classifier.py:283`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sarm\processor_sarm.py:95`

No checkpoint exists before the AI call at src\lerobot\policies\sarm\processor_sarm.py:95. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sarm\processor_sarm.py:95`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\sarm\processor_sarm.py:96`

No checkpoint exists before the AI call at src\lerobot\policies\sarm\processor_sarm.py:96. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\sarm\processor_sarm.py:96`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:87`

No checkpoint exists before the AI call at src\lerobot\policies\smolvla\smolvlm_with_expert.py:87. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:87`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:104`

No checkpoint exists before the AI call at src\lerobot\policies\smolvla\smolvlm_with_expert.py:104. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:104`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:78`

No checkpoint exists before the AI call at src\lerobot\policies\smolvla\smolvlm_with_expert.py:78. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:78`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:85`

No checkpoint exists before the AI call at src\lerobot\policies\smolvla\smolvlm_with_expert.py:85. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:85`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:86`

No checkpoint exists before the AI call at src\lerobot\policies\smolvla\smolvlm_with_expert.py:86. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\smolvla\smolvlm_with_expert.py:86`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\tdmpc\modeling_tdmpc.py:153`

No checkpoint exists before the AI call at src\lerobot\policies\tdmpc\modeling_tdmpc.py:153. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\tdmpc\modeling_tdmpc.py:153`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\vqbet\modeling_vqbet.py:151`

No checkpoint exists before the AI call at src\lerobot\policies\vqbet\modeling_vqbet.py:151. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\vqbet\modeling_vqbet.py:151`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:89`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:89. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:89`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:314`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:314. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:314`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:978`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:978. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:978`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:316`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:316. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:316`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:337`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:337. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:337`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:1223`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:1223. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:1223`

AI output flows to 'next AI call' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:2015`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:2015. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:2015`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:1387`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:1387. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:1387`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\modeling_wall_x.py:1479`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\modeling_wall_x.py:1479. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\modeling_wall_x.py:1479`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\utils.py:262`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\utils.py:262. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\utils.py:262`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:42`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:42. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:42`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:51`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:51. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:51`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:57`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:57. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:57`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:398`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:398. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:398`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1172`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1172. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1172`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1815`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1815. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1815`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1816`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1816. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1816`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1320`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1320. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1320`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2615`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2615. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2615`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:893`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:893. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:893`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1235`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1361`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1361. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1361`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1406`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1406. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1406`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2417`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2417. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2417`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2516`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2667`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2667. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2667`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2734`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2734. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2734`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2030`

No checkpoint exists before the AI call at src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2030. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2030`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\configuration_florence2.py:20`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\configuration_florence2.py:20. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\configuration_florence2.py:20`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:56`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:56. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:56`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:60`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:60. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:60`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2361`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2361. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2361`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2440`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2440. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2440`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2590`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2590. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2590`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2591`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2591. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2591`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1657`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1657. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1657`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1944`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1944. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1944`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2068`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2068. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2068`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2202`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2202. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2202`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2715`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2715. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2715`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:912`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:912. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:912`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1822`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1830`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1830. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1830`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:2043`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:2043. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:2043`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1603`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1603. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1603`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1606`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1606. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1606`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1842`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1842. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1842`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_florence2.py:1849`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_florence2.py:1849. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_florence2.py:1849`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\policies\xvla\modeling_xvla.py:398`

No checkpoint exists before the AI call at src\lerobot\policies\xvla\modeling_xvla.py:398. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\policies\xvla\modeling_xvla.py:398`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\processor\hil_processor.py:591`

No checkpoint exists before the AI call at src\lerobot\processor\hil_processor.py:591. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\processor\hil_processor.py:591`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\processor\migrate_policy_normalization.py:651`

No checkpoint exists before the AI call at src\lerobot\processor\migrate_policy_normalization.py:651. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\processor\migrate_policy_normalization.py:651`

AI output flows to 'database write' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\processor\tokenizer_processor.py:388`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\processor\tokenizer_processor.py:111`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🟡 HIGH — `src\lerobot\processor\tokenizer_processor.py:379`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:470`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:470. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:470`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:471`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:471. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:471`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:421`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:421. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:421`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:429`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:429. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:429`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:438`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:438. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:438`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:449`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:449. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:449`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:460`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:460. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:460`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:470`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:470. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:470`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:471`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:471. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:471`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:509`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:509. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:509`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:510`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:510. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:510`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:413`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:413. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:413`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:415`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:415. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:415`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:421`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:421. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:421`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:429`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:429. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:429`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:438`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:438. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:438`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:449`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:449. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:449`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:460`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:460. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:460`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:509`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:509. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:509`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:510`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:510. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:510`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:413`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:413. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:413`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\rl\gym_manipulator.py:415`

No checkpoint exists before the AI call at src\lerobot\rl\gym_manipulator.py:415. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\rl\gym_manipulator.py:415`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\scripts\lerobot_record.py:502`

No checkpoint exists before the AI call at src\lerobot\scripts\lerobot_record.py:502. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\scripts\lerobot_record.py:502`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\scripts\lerobot_record.py:509`

No checkpoint exists before the AI call at src\lerobot\scripts\lerobot_record.py:509. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\scripts\lerobot_record.py:509`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\scripts\lerobot_train_tokenizer.py:311`

No checkpoint exists before the AI call at src\lerobot\scripts\lerobot_train_tokenizer.py:311. The AI receives input and produces output with nothing checking whether it should — or what it can return.

**What is missing:** A mandatory checkpoint immediately before this AI call.

**Consequence if not addressed:** Any input reaches this AI call unfiltered. Any output proceeds to its destination unchecked. No governance record exists.

*VERBA term: Pre-Node gap*

### 🟡 HIGH — `src\lerobot\scripts\lerobot_train_tokenizer.py:311`

AI output flows to 'downstream processing' with no human review detected.

**What is missing:** Human authorisation gate for critical severity outputs.

**Consequence if not addressed:** Every AI output reaches its destination automatically.

*VERBA term: Human-Authorised Transition missing*

### 🔴 CRITICAL — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:318`

An irreversible action (system_command) at line 318 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:321`

An irreversible action (system_command) at line 321 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `src\lerobot\policies\vqbet\vqbet_utils.py:560`

An irreversible action (database_write) at line 560 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `src\lerobot\scripts\lerobot_info.py:43`

An irreversible action (system_command) at line 43 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

### 🔴 CRITICAL — `src\lerobot\scripts\lerobot_train_tokenizer.py:584`

An irreversible action (database_write) at line 584 in an AI-adjacent file has no authorisation gate. Once executed, it cannot be undone.

**What is missing:** An eligibility condition confirming authorisation before execution.

**Consequence if not addressed:** This action executes automatically. No human approval. No record. No way to stop it once triggered. Knight Capital lost $440M from exactly this pattern.

*VERBA term: Eligibility Condition missing*

---

## Failure mode candidates

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\async_inference\policy_server.py:324`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:177`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:175`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:220`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:220`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:220`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:180`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:180`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:235`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\cameras\realsense\camera_realsense.py:235`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\datasets\pipeline_features.py:94`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:288`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:288`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:292`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:292`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:431`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:261`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:315`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:145`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:145`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:146`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi_gemma.py:146`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pretrained.py:229`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\act\modeling_act.py:110`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\act\modeling_act.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\diffusion\modeling_diffusion.py:98`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\diffusion\modeling_diffusion.py:135`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:84`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:84`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:85`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:85`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:132`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:132`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\groot_n1.py:163`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\modeling_groot.py:291`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:257`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:343`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\action_head\flow_matching_action_head.py:398`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:26`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:73`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\configuration_eagle2_5_vl.py:73`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:123`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:429`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:163`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:188`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:227`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:247`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:418`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:380`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:404`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\image_processing_eagle2_5_vl_fast.py:411`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:26`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:47`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:279`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:363`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:108`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\modeling_eagle2_5_vl.py:108`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:34`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\groot\eagle2_hg_model\processing_eagle2_5_vl.py:400`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:201`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:227`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\multi_task_dit\modeling_multi_task_dit.py:176`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0\modeling_pi0.py:261`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0\modeling_pi0.py:267`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\pi0\modeling_pi0.py:1014`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0\modeling_pi0.py:1014`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0\modeling_pi0.py:1253`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi05\modeling_pi05.py:258`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi05\modeling_pi05.py:264`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\pi05\modeling_pi05.py:985`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi05\modeling_pi05.py:985`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi05\modeling_pi05.py:1224`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:915`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:915`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\pi0_fast\modeling_pi0_fast.py:1275`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sac\modeling_sac.py:942`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:117`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:243`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:279`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:279`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:283`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sac\reward_model\modeling_classifier.py:283`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sarm\processor_sarm.py:95`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\sarm\processor_sarm.py:96`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:87`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:87`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:104`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:104`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:78`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:78`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:85`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:85`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:86`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\smolvla\smolvlm_with_expert.py:86`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\tdmpc\modeling_tdmpc.py:153`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\vqbet\modeling_vqbet.py:151`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:89`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:314`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:978`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:316`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:337`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:337`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E5 Dominance Forcing (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:1223`

Forceful or manipulative inputs that try to override your system's rules through the structure of the request rather than its content.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:1223`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:2015`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:2015`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:1387`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\modeling_wall_x.py:1479`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\utils.py:262`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\configuration_qwen2_5_vl.py:241`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:42`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:51`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:57`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:398`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1172`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1815`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1816`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1320`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2615`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:893`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1361`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:1406`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2417`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2667`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2734`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\wall_x\qwen_model\qwen2_5_vl_moe.py:2030`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\configuration_florence2.py:20`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:56`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:60`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2361`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2440`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2590`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2591`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1657`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1944`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2068`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2202`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2715`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:912`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1830`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:2043`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1603`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1606`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1842`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_florence2.py:1849`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\policies\xvla\modeling_xvla.py:398`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\processor\hil_processor.py:591`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\processor\migrate_policy_normalization.py:651`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\processor\migrate_policy_normalization.py:651`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:470`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:471`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:421`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:429`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:438`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:449`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:460`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:509`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:510`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:413`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\rl\gym_manipulator.py:415`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\scripts\lerobot_record.py:502`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\scripts\lerobot_record.py:509`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-L2 Performative Capture (Tier A)

**Location:** `src\lerobot\scripts\lerobot_train_tokenizer.py:311`

Your system is induced to perform harmful actions by framing them as fiction, roleplay, or hypothetical scenarios.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-I11 Evaluative Decoupling (Tier A)

**Location:** `src\lerobot\scripts\lerobot_train_tokenizer.py:311`

Your system is performing well on the metrics you are measuring while systematically violating the intent those metrics were designed to capture. Goodhart's Law.

**Recommended operator:** SO-5 Coherence Enforcement

### DC-E13 Propagating Corruption (Tier B)

**Location:** `172 AI calls detected`

A single bad output becomes the seed for more bad outputs â€” the corruption spreads through your system automatically after the first incident.

**Recommended operator:** SO-4 Attractor Disruption

### DC-S3 Emergent Misalignment (Tier B)

**Location:** `cluster-level`

Each part of your system behaves correctly in isolation but together they produce outcomes nobody intended and nobody is governing.

**Recommended operator:** SO-3 Distributional Rebalancing

### DC-E14 Substrate Contamination (Tier C)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:318`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `src\lerobot\data_processing\sarm_annotations\subtask_annotation.py:321`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `src\lerobot\policies\vqbet\vqbet_utils.py:560`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `src\lerobot\scripts\lerobot_info.py:43`

Dormant or legacy code that sits quietly in your system until a specific trigger activates it â€” the Knight Capital failure mode.

**Recommended operator:** SO-1 Boundary Enforcement

### DC-E14 Substrate Contamination (Tier C)

**Location:** `src\lerobot\scripts\lerobot_train_tokenizer.py:584`

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