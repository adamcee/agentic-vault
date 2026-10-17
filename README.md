# The Agentic Vault

**Project memory for long-running work with AI.**

AI models forget everything between chats. On a project that lasts weeks or months, the AI suggests ideas you rejected last week, contradicts decisions you made last month, and needs the project re-explained in every new session.

The Agentic Vault is a folder of markdown files and a few rules that fix this. Your decisions, research, and plans live in the folder, and every AI session reads it first instead of starting from zero.

Over time the vault becomes your project's [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base), sometimes called an [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)): the decisions, evidence, terms, and plans that define the project, and the links between them. Because it's plain markdown, you own it. It works in Obsidian or any editor, tracks changes with git, and is easy for coding agents and other AI tools to search.

## How It Works

1. **Plain markdown files.** Everything is a text file you can read and edit yourself, in any editor.
2. **One master file.** `AGENTS.md` holds the project's goals, hard constraints, current phase, and standing decisions. Every AI session reads it first.
3. **Decision records.** Each major decision gets a short document recording what was chosen, what was rejected, and why.
4. **The agent maintains the vault.** Built-in rules tell the agent to log each session, update the plan after each decision, check old decisions against new evidence, and fix broken links. That busywork moves off your plate, so you can spend your time on decisions and use the agent freely, without having to manage it.
5. **Writing discipline.** Vault documents put the main point first and cut AI filler. That makes them faster for you to read and act on, and lets the AI load more of the project at once.

## What It Lets You Do

- **Build a knowledge base you own.** The vault grows into a linked map of your project in plain files that no vendor controls.

- **Stop and restart sessions freely.** Each session records where it left off. The next one picks up from there, even after weeks away.
- **Use several AI tools on one project.** Claude Code, Codex, Gemini CLI, Cursor, and chat apps all read the same master file, `AGENTS.md`.
- **Keep settled questions settled.** Decisions and rejected alternatives are written down, so the AI stops reopening them.
- **Tie decisions to evidence.** Claims link to the research behind them. When new evidence arrives, you can find the decisions it affects.
- **Plan in one place and build in another.** Coding agents in separate code repos can read the vault for constraints and decisions.
- **Keep non-code work in the same system.** Strategy, research, and business planning sit next to the technical docs.

## Repository Structure

```text
/
├── template/   ← The vault template. Copy this to start a project.
├── examples/   ← Three filled-in example vaults: software, business, and creative.
└── website/    ← Source for the documentation site (see website/README.md to run it).
```

The vault used to build this project is published separately at [agentic-vault-meta](https://github.com/adamcee/agentic-vault-meta).

## Setup

**Recommended setup:** open the vault in [Obsidian](https://obsidian.md/) and connect a desktop AI app that supports MCP (Model Context Protocol), such as Claude Desktop or the Codex app. You chat with the AI however you like, and every chat can read and write the vault, while you view and edit the same files in Obsidian. Back the vault up to a private GitHub repository for history and off-site copies. [Obsidian Setup](website/docs/installation/obsidian-setup.md) walks through it and lists the plugins that help the AI.

The tiers below cover other ways to work. You can move up a tier later.

### Tier 1: Web chat (Claude.ai, Gemini, ChatGPT)

1. Copy the `template/` folder.
2. Open `AGENTS.md` in a text editor and fill in the bracketed sections.
3. Paste the contents of `AGENTS.md` as the first message of each new chat.

### Tier 2: AI IDE (Cursor, Windsurf, Roo Code)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md`.
3. Open `my-new-project` in your IDE. Cursor and Windsurf read `AGENTS.md`, and the included `.cursorrules` and `.windsurfrules` point to it as a fallback.

### Tier 3: CLI agents (Claude Code, Codex, Gemini CLI)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md` and `architecture/CONSTITUTION.md`.
3. Run `claude`, `codex`, or `gemini` from the project folder. Codex reads `AGENTS.md` directly; `CLAUDE.md` and `GEMINI.md` import it.

## Setup Wizard

To have the AI fill in the template, paste `template/SETUP_WIZARD.md` into your AI tool and answer its four questions. It fills in `AGENTS.md` and `architecture/CONSTITUTION.md`, or prints them for you to paste if it has no file access.

## Design & Goals

The methodology came out of months of heavy AI use on a real project, and each protocol was added to fix a specific, recurring failure. [Design & Goals](website/docs/methodology/design-and-goals.md) covers the failures, the protocols, and what worked.
