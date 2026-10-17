# Quickstart

## New to GitHub or the Command Line?

Let your AI do the setup with you. Copy this prompt into the AI app you use (Claude, ChatGPT, Gemini, or another), and it will either run the steps itself or walk you through them one at a time.

```text
I want to set up an "Agentic Vault": a folder of markdown files that gives you,
my AI assistant, a memory of my project between chats. The template is the
template/ folder at https://github.com/adamcee/agentic-vault, and the guide is
at https://adamcee.github.io/agentic-vault/.

I'm not familiar with GitHub, git, or the command line. Please:
1. Ask me what computer I use (Mac, Windows, or Linux) and which AI apps I have.
2. If you can run commands on my computer, do each setup step yourself and tell
   me in one sentence what it does before you run it. If you can't, walk me
   through one step at a time and wait for me to confirm each one.
3. Get the template onto my computer (download the ZIP if I don't have git),
   copy the template/ folder, and rename it after my project.
4. Interview me about my project, then fill in AGENTS.md and
   architecture/CONSTITUTION.md.
5. Offer to set up a private GitHub backup, explaining what GitHub is in plain
   words.
6. Show me how to start a new chat that reads AGENTS.md first.
Use plain language and don't skip steps.
```

If you're comfortable with a terminal, follow the steps below.

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
