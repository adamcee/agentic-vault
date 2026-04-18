---
name: prompt-architect
description: "Design, draft, and audit LLM prompts and system instructions for any purpose. Use this skill whenever the user says 'write a prompt', 'system prompt for', 'improve this prompt', or asks you to create instructions that an LLM will consume."
---

# Prompt Architect

Build structured, high-signal LLM prompts that work. 

## Core workflow

### Phase 1 — Clarify purpose and target
Establish the target model (Claude, Gemini, GPT), execution context, success criteria, and failure modes to prevent.

### Phase 2 — Structure with RCCF
- **Role:** The persona and expertise level.
- **Context:** The minimum background that changes the output decision.
- **Constraints:** Hard boundaries and negative instructions (falsifiable).
- **Format:** The exact output structure (XML, JSON, Markdown).

### Phase 3 — Apply the hierarchy
1. **Clarity and directness:** No passive voice.
2. **Examples:** 1-3 "golden" examples.
3. **Chain of thought:** `<thinking>` tags or step-by-step instructions.
4. **Structured space:** XML tags to separate instructions from context from input.

### Phase 4 — Audit for context budget
- Delete any token that doesn't change the output.
- Ensure constraints are falsifiable.
- Remove meta-commentary ("This prompt is designed to...").