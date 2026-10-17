# The Agentic Vault

**Project memory for long-running work with AI.**

AI models forget everything between chats. On a project that lasts weeks or months, the AI suggests ideas you rejected last week, contradicts decisions you made last month, and needs the project re-explained in every new session.

The Agentic Vault is a folder of markdown files and a few rules that fix this. Your decisions, research, and plans live in the folder, and every AI session reads it first instead of starting from zero.

## What It Lets You Do

- **Stop and restart sessions freely.** Each session records where it left off. The next one picks up from there, even after weeks away.
- **Use several AI tools on one project.** Claude Code, Gemini CLI, Cursor, and chat apps all read the same master file.
- **Keep settled questions settled.** Decisions and rejected alternatives are written down, so the AI stops reopening them.
- **Tie decisions to evidence.** Claims link to the research behind them. When new evidence arrives, you can find the decisions it affects.
- **Plan in one place and build in another.** Coding agents in separate code repos can read the vault for constraints and decisions.
- **Keep non-code work in the same system.** Strategy, research, and business planning sit next to the technical docs.

## Repository Structure

```text
/
├── template/   ← The vault template. Copy this to start a project.
├── example/    ← A filled-in example vault (BrewTrack, a coffee-shop loyalty app).
└── website/    ← Source for the documentation site.
```

The vault used to build this project is published separately at [agentic-vault-meta](https://github.com/adamcee/agentic-vault-meta).

## Setup

Pick the tier that matches how you use AI. You can move up a tier later.

### Tier 1: Web chat (Claude.ai, Gemini, ChatGPT)

1. Copy the `template/` folder.
2. Open `SYSTEM.md` in a text editor and fill in the bracketed sections.
3. Paste the contents of `SYSTEM.md` as the first message of each new chat.

### Tier 2: AI IDE (Cursor, Windsurf, Roo Code)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `SYSTEM.md`.
3. Open `my-new-project` in your IDE. The included `.cursorrules` and `.windsurfrules` tell the AI to read `SYSTEM.md` before acting.

### Tier 3: CLI agents (Claude Code, Gemini CLI)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `SYSTEM.md` and `architecture/CONSTITUTION.md`.
3. Run `claude` or `gemini` from the project folder. `CLAUDE.md` and `GEMINI.md` point the agent to `SYSTEM.md` at session start.

## Setup Wizard

To have the AI fill in the template, paste `template/SETUP_WIZARD.md` into your AI tool and answer its four questions. It fills in `SYSTEM.md`, `AGENTS.md`, and `architecture/CONSTITUTION.md`, or prints them for you to paste if it has no file access.

## Design & Goals

The methodology came out of months of heavy AI use on a real project, and each protocol was added to fix a specific, recurring failure. [Design & Goals](website/docs/methodology/design-and-goals.md) covers the failures, the protocols, and what worked.
