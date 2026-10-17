# Quickstart

## 1. Create the Vault

From the repository root, run:

```bash
./template/scripts/init-vault.sh my-new-project
```

The script copies the template and makes an initial git commit. Without a terminal, copy the `template/` folder and rename it.

## 2. Fill In AGENTS.md

Open `AGENTS.md` and replace the bracketed placeholders, such as `[Project Name]`, with your project's details. The [Setup Wizard](wizard.md) can do this for you.

## 3. Set Hard Constraints

Open `architecture/CONSTITUTION.md` and list the rules your project must never break.

## 4. Connect Your AI

The recommended setup is Obsidian plus a desktop AI app with MCP, backed up to GitHub. See [Obsidian Setup](obsidian-setup.md).

## 5. Start a Session

Open the project folder in your AI tool: Codex, Cursor, and Windsurf read `AGENTS.md` directly, and `CLAUDE.md` and `GEMINI.md` import it. In a web chat, paste `AGENTS.md` as your first message.
