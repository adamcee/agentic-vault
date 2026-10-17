# The Agentic Vault

**Project memory for long-running work with AI.**

AI models forget everything between chats. On a project that lasts weeks or months, the AI suggests ideas you already rejected, contradicts decisions you already made, and needs the project re-explained in every session.

The Agentic Vault is a folder of markdown files and a few rules that fix this. Your decisions, research, and plans live in the folder, and every AI session reads it first.

## How It Works

1. **One master file.** `AGENTS.md` holds the project's goals, hard constraints, current phase, and standing decisions. Every session reads it first.
2. **Decision records.** Each major decision gets a short document recording what was chosen, what was rejected, and why. The AI checks these before proposing changes.
3. **Writing discipline.** Vault documents put the main point first and cut filler, so an AI can load more of the project in less context.

## What It Lets You Do

- Stop and restart sessions without re-explaining the project.
- Use Claude, Gemini, Cursor, and chat apps on the same project without their instructions drifting apart.
- Keep rejected ideas from coming back.
- Find and recheck the decisions that new evidence affects.
- Point coding agents in separate repos at the vault for constraints and decisions.

Start with the [Quickstart](installation/quickstart.md), or browse the [example vaults](examples/README.md): a web app, a small business, and an indie game.
