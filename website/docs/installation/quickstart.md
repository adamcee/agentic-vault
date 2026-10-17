# Quickstart

## 1. Create the Vault

From the repository root, run:

```bash
./template/scripts/init-vault.sh my-new-project
```

The script copies the template and makes an initial git commit. Without a terminal, copy the `template/` folder and rename it.

## 2. Fill In SYSTEM.md

Open `SYSTEM.md` and replace the bracketed placeholders, such as `[Project Name]`, with your project's details. The [Setup Wizard](wizard.md) can do this for you.

## 3. Set Hard Constraints

Open `architecture/CONSTITUTION.md` and list the rules your project must never break.

## 4. Start a Session

Open the project folder in your AI tool, where `CLAUDE.md`, `GEMINI.md`, and `.cursorrules` tell the AI to read `SYSTEM.md` at the start of each session. In a web chat, paste `SYSTEM.md` as your first message.
