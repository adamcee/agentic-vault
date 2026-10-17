# The Agentic Vault

**Project memory for long-running work with AI.**

AI models forget everything between chats. On a project that lasts weeks or months, the AI suggests ideas you already rejected, contradicts decisions you already made, and needs the project re-explained in every session.

The Agentic Vault is a folder of markdown files and a few rules that fix this. Your decisions, research, and plans live in the folder, and every AI session reads it first.

Over time the vault becomes your project's [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base), sometimes called an [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)): the decisions, evidence, terms, and plans that define the project, and the links between them. Because it's plain markdown, you own it. It works in Obsidian or any editor, tracks changes with git, and is easy for coding agents and other AI tools to search.

## How It Works

1. **Plain markdown files.** Everything is a text file you can read and edit yourself, in any editor.
2. **One master file.** `AGENTS.md` holds the project's goals, hard constraints, current phase, and standing decisions. Every session reads it first.
3. **Decision records.** Each major decision gets a short document recording what was chosen, what was rejected, and why. The AI checks these before proposing changes.
4. **The agent maintains the vault.** Built-in rules tell the agent to log each session, update the plan after each decision, check old decisions against new evidence, and fix broken links. That busywork moves off your plate, so you can spend your time on decisions and use the agent freely, without having to manage it.
5. **Writing discipline.** Vault documents put the main point first and cut AI filler. That makes them faster for you to read and act on, and lets the AI load more of the project at once.

## What It Lets You Do

- Build a knowledge base you own, in plain files that no vendor controls.
- Stop and restart sessions without re-explaining the project.
- Use Claude, Gemini, Cursor, and chat apps on the same project without their instructions drifting apart.
- Keep rejected ideas from coming back.
- Find and recheck the decisions that new evidence affects.
- Point coding agents in separate repos at the vault for constraints and decisions.

Start with the [Quickstart](installation/quickstart.md), or browse the [example vaults](examples/README.md): a web app, a small business, and an indie game.
