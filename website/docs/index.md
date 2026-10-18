# The Agentic Vault

**Project memory for long-running work with AI.**

AI models forget everything between chats. On a project that lasts weeks or months, the AI suggests ideas you already rejected, contradicts decisions you already made, and needs the project re-explained in every session.

The Agentic Vault is a folder of markdown files and a few rules that fix this. Your decisions, research, and plans live in the folder, and every AI session reads it first.

## See It in Action

Two example vaults show the method on fictional projects. Each repo holds the vault's actual files, which you can clone and open in Obsidian like your own; each website shows the same files with graph view, backlinks, and search, so you can explore without installing anything.

!!! example "Night Post: an indie RPG, six months in"
    A three-person team making an adventure game about a night courier. Decisions that changed after playtests, market and accessibility research, a world bible, and the agents' session logs.

    [Explore the site](https://adamcee.github.io/night-post-vault/){ .md-button .md-button--primary } [View the repo](https://github.com/adamcee/night-post-vault){ .md-button }

!!! example "Curbside Cycles: a small business, five weeks in"
    A one-person bike-repair van. A survey, a pilot month that changed the pricing, and a rejected storefront lease, with no software involved.

    [Explore the site](https://adamcee.github.io/curbside-cycles-vault/){ .md-button .md-button--primary } [View the repo](https://github.com/adamcee/curbside-cycles-vault){ .md-button }

The websites exist only to make the examples easy to browse; your own vault doesn't need one. If you want, you can publish all or part of yours the same way.

## Every Session Starts Up to Speed

The `vault-start` skill is what makes this work day to day. At the start of every conversation, the agent runs it: it reads `AGENTS.md`, finds what changed since the last session, asks what kind of work you're doing, and loads the files that work needs.

That holds whether you're chatting with an assistant or running an autonomous agent with no one watching. Claude Code runs the skill because `CLAUDE.md` tells it to, you can also type `/vault-start`, and agents without skills follow the same steps from the Session Start Protocol in `AGENTS.md`.

## How It Works

1. **Plain markdown files.** Everything is a text file you can read and edit yourself, in any editor.
2. **One master file.** `AGENTS.md` holds the project's goals, hard constraints, current phase, and standing decisions. Every session reads it first.
3. **Decision records.** Each major decision gets a short document recording what was chosen, what was rejected, and why. You can write one yourself or have the AI draft it, and every later session reads it before proposing changes.
4. **The agent maintains the vault.** Built-in rules tell the agent to log each session, update the plan after each decision, check old decisions against new evidence, and fix broken links. That busywork moves off your plate, so you can focus on the decisions and work with the agent however suits you.
5. **Writing discipline.** Vault documents put the main point first and cut AI filler. That makes them faster for you to read and act on, and lets the AI load more of the project at once.

## What It Lets You Do

Over time the vault becomes your project's [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base), sometimes called an [ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)): the decisions, evidence, terms, and plans that define the project, and the links between them. It's plain markdown you own, so it works in Obsidian or any editor and tracks changes with git.

- **Stop and restart sessions** without re-explaining the project.
- **Use any kind of AI agent.** Coding agents, agents that draft marketing copy, research assistants, and personal assistants can all read the same vault and work from the same decisions.
- **Use several AI tools on one project.** Claude, Codex, Gemini, Cursor, and chat apps read the same master file, so their instructions don't drift apart.
- **Keep rejected ideas from coming back,** and find the decisions that new evidence affects.

## Built From Real Work, Shaped to Yours

The rules weren't designed up front. They were added one at a time during months of AI-assisted work on a real project, each to fix a problem that kept recurring ([Design & Goals](methodology/design-and-goals.md)).

Your vault can grow the same way. When you spot a problem or a better way of working, tell your AI to add a rule: it goes in `AGENTS.md` or a page in `vault-guide/`, and every later session follows it.

Start with the [Quickstart](installation/quickstart.md), which includes a prompt your AI can use to set everything up with you.
