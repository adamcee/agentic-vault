# The Agentic Vault

**A markdown vault that gives AI sessions persistent project memory.**

AI tools forget everything between sessions, so they reopen settled decisions, suggest options you already rejected, and lose track of what you're building. This vault holds your decisions, research, and plans in plain files that every AI session reads first.

Over time it becomes your project's [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base) (or [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science))): plain markdown you own, read, and edit, tracked with git and searchable by any AI tool.

## How It Works

1. **Plain markdown files.** You can read and edit everything yourself, in Obsidian or any editor.
2. **`AGENTS.md` is the single source of truth.** Every AI tool reads it before acting.
3. **Decision records (ADRs and PDRs)** record what you chose, what you rejected, and why.
4. **Research traceability.** Empirical claims link to research docs in the vault, not to the AI's memory.
5. **The agent maintains the vault.** Protocols in `AGENTS.md` tell the agent to log sessions, propagate decisions, recheck decisions against new evidence, and fix links, so you don't have to.
6. **Writing discipline.** Documents put the main point first and cut AI filler, so they're quick for you to read and use, and the AI can load more of the vault at once.

## Setup

### Tier 1: Web chat (Claude.ai, Gemini, ChatGPT)

1. Open `AGENTS.md` in a text editor and fill in the bracketed sections.
2. Paste the contents of `AGENTS.md` as the first message of each new chat.

### Tier 2: AI IDE (Cursor, Windsurf, Roo Code)

1. Run `./scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md`.
3. Open `my-new-project` in your IDE. Cursor and Windsurf read `AGENTS.md`, and the included `.cursorrules` and `.windsurfrules` point to it as a fallback.

### Tier 3: CLI agents (Claude Code, Gemini CLI)

1. Run `./scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md` and `architecture/CONSTITUTION.md`.
3. Run `claude`, `gemini`, or `codex` from the project folder. Codex reads `AGENTS.md` directly; `CLAUDE.md` and `GEMINI.md` import it.

## Setup Wizard

Paste the prompt in `SETUP_WIZARD.md` into your AI tool from this directory and answer its four questions. It fills in `AGENTS.md` and `architecture/CONSTITUTION.md`, or prints them for you to paste if it has no file access.

## Directory Structure

```text
/
├── AGENTS.md                  ← Start here. Master context and protocol checklists.
├── CLAUDE.md / GEMINI.md      ← Pointers to AGENTS.md for each tool.
├── session-history.md         ← One line per session, append-only.
├── architecture/
│   └── CONSTITUTION.md        ← Hard constraints.
├── decisions/                 ← Decision records: technical/, product/, rejected/.
├── strategy/                  ← Goals, audience, positioning.
├── concepts/                  ← Definitions (what something is).
├── ideas/                     ← Raw proposals (what something could be).
├── research/                  ← Evidence and source summaries.
├── prototype/                 ← AI ledger, human task list, weekly logs, specs.
├── drafts/                    ← Staging area for AI-generated text.
├── prompts/                   ← Reusable prompts and research briefs.
├── vault-guide/               ← Protocol pages and style guides.
├── journal/                   ← Your notes. AI never writes here.
└── .claude/skills/            ← Session start, link checks, lint, and review scripts.
```
