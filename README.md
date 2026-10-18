# The Agentic Vault

**The Agentic Vault is a project knowledge base that you and your AI agents share, built on plain markdown files, Obsidian, and git.**

Every AI session reads the vault first, so your agents remember the decisions you've made, the evidence behind them, and what's already done. Without it, AI models forget everything between chats: they suggest ideas you already rejected and need the project re-explained every time.

The vault is built for your agents to manage. They keep it current on their own, and guardrails let them contribute and make decisions safely: hard constraints they can't break, your approval before any decision is written, a staging area for their drafts, and logs they can only add to.

Over time the vault becomes your project's [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base), sometimes called an [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)): the decisions, evidence, terms, and plans that define the project, and the links between them. It's plain markdown that you own, so it works in Obsidian or any editor, tracks changes with git, and is easy for any AI agent to search.

**Get started:** the [Quickstart](website/docs/installation/quickstart.md) includes a prompt your AI can use to set everything up with you, even if you've never used GitHub or a terminal.

## See It in Action

Two example vaults show the method on fictional projects. Each repo holds the vault's actual files, which you can clone and open in Obsidian like your own; each website shows the same files with graph view, backlinks, and search, so you can explore without installing anything.

| Example | Explore | Files |
|---|---|---|
| **Night Post**: an indie RPG, six months in, with playtests, market research, and a world bible | [Website](https://adamcee.github.io/night-post-vault/) | [Repo](https://github.com/adamcee/night-post-vault) |
| **Curbside Cycles**: a one-person bike-repair business, five weeks in, with a survey and a pricing pilot | [Website](https://adamcee.github.io/curbside-cycles-vault/) | [Repo](https://github.com/adamcee/curbside-cycles-vault) |

The websites exist only to make the examples easy to browse; your own vault doesn't need one, though you can publish all or part of it the same way.

## Every Session Starts Up to Speed

The `vault-start` skill is what makes this work day to day. At the start of every conversation, the agent runs it: it reads `AGENTS.md`, finds what changed since the last session, asks what kind of work you're doing, and loads the files that work needs.

That holds whether you're chatting with an assistant or running an autonomous agent with no one watching. Claude Code runs the skill because `CLAUDE.md` tells it to, you can also type `/vault-start`, and agents without skills follow the same steps from the Session Start Protocol in `AGENTS.md`.

## How It Works

1. **Plain markdown files.** Everything is a text file you can read and edit yourself, in any editor.
2. **One master file.** `AGENTS.md` holds the project's goals, hard constraints, current phase, and standing decisions. Every AI session reads it first.
3. **Decision records.** Each major decision gets a short document recording what was chosen, what was rejected, and why. You can write one yourself or have the AI draft it, and every later session reads it before proposing changes.
4. **Agents manage the vault.** Built-in rules tell the agent to log each session, update the plan after each decision, check old decisions against new evidence, and fix broken links. That busywork moves off your plate, so you can focus on the decisions and work with the agent however suits you.
5. **Guardrails.** Agents work within limits you set: hard constraints in `AGENTS.md` and `CONSTITUTION.md`, an approval step before any decision record is written, `drafts/` for unreviewed AI writing, append-only logs, and a `journal/` folder agents never touch.
6. **Writing discipline.** Vault documents put the main point first and cut AI filler. That makes them faster for you to read and act on, and lets the AI load more of the project at once.

## What It Lets You Do

- **Build a knowledge base you own.** The vault grows into a linked map of your project in plain files that no vendor controls.
- **Stop and restart sessions freely.** Each session records where it left off. The next one picks up from there, even after weeks away.
- **Use any kind of AI agent.** Coding agents, agents that draft marketing copy, research assistants, and personal assistants can all work from the same vault.
- **Use several AI tools on one project.** Claude Code, Codex, Antigravity CLI, Cursor, and chat apps all read the same master file, `AGENTS.md`.
- **Keep settled questions settled.** Decisions and rejected alternatives are written down, so the AI stops reopening them.
- **Tie decisions to evidence.** Claims link to the research behind them. When new evidence arrives, you can find the decisions it affects.
- **Plan in one place and build in another.** Coding agents in separate code repos can read the vault for constraints and decisions.
- **Keep non-code work in the same system.** Strategy, research, and business planning sit next to the technical docs.

## Repository Structure

```text
/
├── template/   ← The vault template. Copy this to start a project.
├── scripts/    ← sync-examples.py keeps the example vault repos in step with the template.
└── website/    ← Source for the documentation site (see website/README.md to run it).
```

The example vaults live in their own repos (see above). The vault used to build this project is published at [agentic-vault-meta](https://github.com/adamcee/agentic-vault-meta).

## Setup

**Recommended setup:** [Obsidian](https://obsidian.md/) plus a desktop AI app that supports MCP (Model Context Protocol), such as Claude Desktop or the Codex app, backed up to a private GitHub repository. You chat with the AI however you like and every chat can read and write the vault, while you view and edit the same files in Obsidian.

[Obsidian Setup](website/docs/installation/obsidian-setup.md) walks through it and lists the plugins that help the AI.

**New to GitHub or the command line?** The [Quickstart](website/docs/installation/quickstart.md) has a prompt you can give your AI so it does the setup with you.

The tiers below cover other ways to work. You can move up a tier later.

### Tier 1: Web chat (Claude.ai, Gemini, ChatGPT)

1. Copy the `template/` folder.
2. Open `AGENTS.md` in a text editor and fill in the bracketed sections.
3. Paste the contents of `AGENTS.md` as the first message of each new chat.

### Tier 2: AI IDE (Cursor, Windsurf, Roo Code)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md`.
3. Open `my-new-project` in your IDE. Cursor reads `AGENTS.md` directly, and the included `.windsurfrules` points Windsurf to it.

### Tier 3: CLI agents (Claude Code, Codex, Antigravity CLI)

1. Run `./template/scripts/init-vault.sh my-new-project`.
2. Fill in `AGENTS.md` and `architecture/CONSTITUTION.md`.
3. Run `claude`, `codex`, or `agy` (Antigravity CLI, which replaced Gemini CLI for individual accounts) from the project folder. Codex and Antigravity read `AGENTS.md` directly; `CLAUDE.md` imports it for Claude Code.

## Setup Wizard

To have the AI fill in the template, paste `template/SETUP_WIZARD.md` into your AI tool and answer its four questions. It fills in `AGENTS.md` and `architecture/CONSTITUTION.md`, or prints them for you to paste if it has no file access.

## Built From Real Work, Shaped to Yours

The rules weren't designed up front. They were added one at a time during months of AI-assisted work on a real project, each to fix a problem that kept recurring ([Design & Goals](website/docs/methodology/design-and-goals.md)).

Your vault can grow the same way. When you spot a problem or a better way of working, tell your AI to add a rule: it goes in `AGENTS.md` or a page in `vault-guide/`, and every later session follows it.
