# The Agentic Vault

**A domain-agnostic, AI-native knowledge base template designed to stop context loss and hallucination in LLM coding and planning sessions.**

If you are using Claude Code, Gemini CLI, Cursor, or even just copying and pasting into a web app, you have experienced **Context Rot**:
- The AI forgets standing decisions made last week.
- It relitigates rejected architectural patterns.
- It hallucinates dependencies because it lost the thread of what you are actually building.

The **Agentic Vault** solves this. It treats your project documentation as a high-leverage state machine for multi-agent LLM parsing. 

## Core Philosophy
1. **The `SYSTEM.md` Primacy:** One Single Source of Truth (SSOT). Every AI tool you use is forced to read this first.
2. **Decision Records (ADRs/PDRs):** We don't just record *what* we built; we record *why* we chose it, and what we rejected.
3. **Research Traceability:** Empirical claims link back to local research documents, not the AI's training data.
4. **Writing Discipline:** Strict adherence to BLUF (Bottom Line Up Front) and the "Paragraph Ban." We write for machine parseability.

---

## 🚀 Installation & Setup

This vault is designed to degrade gracefully. Whether you are a non-technical founder or a senior systems architect, you can use this framework.

### Tier 1: The Web App User (Non-Technical)
*You use Claude.ai, Gemini Advanced, or ChatGPT in your browser.*
1. Download or clone this repository.
2. Open `SYSTEM.md` in any text editor and fill out the `[Replace this section...]` brackets.
3. **The Workflow:** Whenever you start a new chat, copy the contents of your filled-out `SYSTEM.md` and paste it as your very first message.

### Tier 2: The IDE Prosumer (Cursor, Windsurf, Roo Code)
*You use an AI-native IDE.*
1. Run `./scripts/init-vault.sh my-new-project` to scaffold the vault.
2. Open `my-new-project` in your IDE.
3. The included `.cursorrules` and `.windsurfrules` files are already configured to force the AI to read your `SYSTEM.md` before taking action.
4. **The Workflow:** Just start chatting in your IDE. The context is automatically injected.

### Tier 3: The CLI Power User (Claude Code, Gemini CLI)
*You operate directly in the terminal.*
1. Run `./scripts/init-vault.sh my-new-project` to scaffold the vault.
2. Fill out `SYSTEM.md` and `architecture/CONSTITUTION.md`.
3. The included `CLAUDE.md` and `GEMINI.md` files act as pointers, forcing your CLI agents to read the SSOT.
4. **The Workflow:** Navigate to the folder in your terminal. Run `claude` or `gemini`. The agent will automatically load the vault topology, parse your standing decisions, and execute tasks against your constraints.

---

## 🪄 The AI Setup Wizard (Recommended)

Don't want to fill out the boilerplate yourself? Let your AI do it.

1. Open `SETUP_WIZARD.md`.
2. Copy the entire prompt.
3. Paste it into your AI of choice (Claude, Gemini, Cursor) while in this directory.
4. The AI will ask you a few questions about your project and autonomously populate `SYSTEM.md`, `AGENTS.md`, and `CONSTITUTION.md` for you!

---

## Directory Structure

```text
/
├── SYSTEM.md                  ← Start here. The Master Context.
├── AGENTS.md                  ← The navigation map and stack reference.
├── CLAUDE.md / GEMINI.md      ← Agent-specific pointers.
├── architecture/              
│   └── CONSTITUTION.md        ← Project invariants and hard constraints.
├── decisions/                 ← Architecture and Product Decision Records.
├── strategy/                  ← Personas, business models, goals.
├── concepts/                  ← Atomic definitions (what something is).
├── ideas/                     ← Raw proposals (what something could be).
├── research/                  ← Evidence and external findings.
├── prototype/ (or src/)       ← Your actual implementation code and plans.
├── drafts/                    ← Staging area for AI-generated text.
└── vault-guide/               ← Rules for maintaining the vault itself.
```