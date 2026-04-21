# The Agentic Vault

**A shared brain for you and your AI.**

Whether you are designing a new product, architecting software, or world-building a novel, AI is an incredible thought partner. But it has a fatal flaw: **Amnesia**. 

If you use Claude, Gemini, Cursor, or ChatGPT for complex projects, you have experienced "Context Rot":
- The AI forgets the core values of your product you established yesterday.
- It suggests ideas you already rejected last week.
- It loses the thread of *why* you are building something, forcing you to start from scratch in every new chat.

The **Agentic Vault** solves this. It is an AI-native project knowledge base. It provides a structured framework of folders, rules, and protocols that act as a persistent, long-term memory for your AI.

---

## 🗂️ Repository Structure

This repository contains the entire Agentic Vault ecosystem. 

```text
/
├── template/                  ← The pristine, reusable vault template.
├── example/                   ← A populated example (BrewTrack app) showing ADRs in action.
├── website/                   ← The MkDocs documentation hub source code.
└── project_vault/             ← The meta-vault we used to build this project!
```

**If you just want to use the template:** Copy the `template/` directory or run `./template/scripts/init-vault.sh my-new-project`.

---

## 🚀 Installation & Setup

This vault is designed to degrade gracefully. Whether you are a non-technical founder or a senior systems architect, you can use this framework.

### Tier 1: The Web App User (Non-Technical)
*You use Claude.ai, Gemini Advanced, or ChatGPT in your browser.*
1. Download or clone this repository and copy the `template/` folder.
2. Open `SYSTEM.md` in any text editor and fill out the `[Replace this section...]` brackets.
3. **The Workflow:** Whenever you start a new chat, copy the contents of your filled-out `SYSTEM.md` and paste it as your very first message.

### Tier 2: The IDE Prosumer (Cursor, Windsurf, Roo Code)
*You use an AI-native IDE.*
1. Run `./template/scripts/init-vault.sh my-new-project` to scaffold the vault.
2. Open `my-new-project` in your IDE.
3. The included `.cursorrules` and `.windsurfrules` files are already configured to force the AI to read your `SYSTEM.md` before taking action.
4. **The Workflow:** Just start chatting in your IDE. The context is automatically injected.

### Tier 3: The CLI Power User (Claude Code, Gemini CLI)
*You operate directly in the terminal.*
1. Run `./template/scripts/init-vault.sh my-new-project` to scaffold the vault.
2. Fill out `SYSTEM.md` and `architecture/CONSTITUTION.md`.
3. The included `CLAUDE.md` and `GEMINI.md` files act as pointers, forcing your CLI agents to read the SSOT.
4. **The Workflow:** Navigate to the folder in your terminal. Run `claude` or `gemini`. The agent will automatically load the vault topology, parse your standing decisions, and execute tasks against your constraints.

---

## 🪄 The AI Setup Wizard (Recommended)

Don't want to fill out the boilerplate yourself? Let your AI do it.

1. Open `template/SETUP_WIZARD.md`.
2. Copy the entire prompt.
3. Paste it into your AI of choice (Claude, Gemini, Cursor) while in your new project directory.
4. The AI will ask you a few questions about your project and autonomously populate `SYSTEM.md`, `AGENTS.md`, and `CONSTITUTION.md` for you!

---

## Design & Goals

AI models are powerful thought partners that forget between sessions. On projects that last longer than a single chat, this amnesia causes decisions to be relitigated and rejected ideas to resurface. The Agentic Vault solves this by treating the project folder as the single source of truth—complete with standing decisions, research traceability, and strict writing discipline.

For a comprehensive dive into the philosophy, protocols, and field tests that shaped this methodology, read the full [Design & Goals](website/docs/methodology/design-and-goals.md) document.
