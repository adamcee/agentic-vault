# The Agentic Vault

**A markdown vault that gives AI sessions persistent project memory.**

AI tools forget everything between sessions, so they reopen settled decisions, suggest options you already rejected, and lose track of what you're building. This vault holds your decisions, research, and plans in plain files that every AI session reads first.

## How It Works

1. **`SYSTEM.md` is the single source of truth.** Every AI tool reads it before acting.
2. **Decision records (ADRs and PDRs)** record what you chose, what you rejected, and why.
3. **Research traceability.** Empirical claims link to research docs in the vault, not to the AI's memory.
4. **Writing discipline.** Documents put the main point first and keep paragraphs to two sentences, so an AI can read more of the vault in less context.

## Setup

### Tier 1: Web chat (Claude.ai, Gemini, ChatGPT)

1. Open `SYSTEM.md` in a text editor and fill in the bracketed sections.
2. Paste the contents of `SYSTEM.md` as the first message of each new chat.

### Tier 2: AI IDE (Cursor, Windsurf, Roo Code)

1. Run `./scripts/init-vault.sh my-new-project`.
2. Fill in `SYSTEM.md`.
3. Open `my-new-project` in your IDE. `.cursorrules` and `.windsurfrules` tell the AI to read `SYSTEM.md` before acting.

### Tier 3: CLI agents (Claude Code, Gemini CLI)

1. Run `./scripts/init-vault.sh my-new-project`.
2. Fill in `SYSTEM.md` and `architecture/CONSTITUTION.md`.
3. Run `claude` or `gemini` from the project folder. `CLAUDE.md` and `GEMINI.md` point the agent to `SYSTEM.md` at session start.

## Setup Wizard

Paste the prompt in `SETUP_WIZARD.md` into your AI tool from this directory and answer its four questions. It fills in `SYSTEM.md`, `AGENTS.md`, and `architecture/CONSTITUTION.md`, or prints them for you to paste if it has no file access.

## Directory Structure

```text
/
├── SYSTEM.md                  ← Start here. Master context.
├── AGENTS.md                  ← Directory map and stack reference.
├── CLAUDE.md / GEMINI.md      ← Pointers to SYSTEM.md for each tool.
├── architecture/
│   └── CONSTITUTION.md        ← Hard constraints.
├── decisions/                 ← Architecture and product decision records.
├── strategy/                  ← Goals, users, business model.
├── concepts/                  ← Definitions (what something is).
├── ideas/                     ← Raw proposals (what something could be).
├── research/                  ← Evidence and external findings.
├── prototype/ (or src/)       ← Implementation plan and code.
├── drafts/                    ← Staging area for AI-generated text.
└── vault-guide/               ← Rules for maintaining the vault.
```
