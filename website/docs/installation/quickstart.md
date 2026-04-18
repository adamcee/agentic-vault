# Quickstart Guide

This guide will walk you through the manual setup of the Agentic Vault.

## Step 1: Scaffold the Vault
If you are using a terminal, run the included script to scaffold your new project:
```bash
./scripts/init-vault.sh my-new-project
```
*(If you are not using a terminal, you can simply copy the `template/` folder and rename it to your project name).*

## Step 2: Configure SYSTEM.md
Open `SYSTEM.md` in your new project directory and replace all bracketed placeholders (like `[Project Name]`) with your actual project details.

## Step 3: Configure Invariants
Open `architecture/CONSTITUTION.md` and define the absolute hard constraints for your project.

## Step 4: Interact with your AI
Ensure your AI (Claude Code, Cursor, Gemini CLI) has access to the root of your project. The included `.cursorrules`, `CLAUDE.md`, and `GEMINI.md` files will automatically force the AI to read your `SYSTEM.md` at the start of every session!