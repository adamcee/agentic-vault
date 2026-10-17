# Obsidian Setup

The recommended setup pairs [Obsidian](https://obsidian.md/) with a desktop AI app that supports the Model Context Protocol (MCP), such as Claude Desktop or the Codex app. You chat with the AI the way you like, and in every chat it can read and write the vault, while you browse and edit the same files in Obsidian.

## New to Obsidian or MCP?

Copy this prompt into your AI app, replacing the bracketed path, and it will set things up with you step by step.

```text
Help me set up Obsidian for my Agentic Vault, the folder at [path to my vault
folder], following https://adamcee.github.io/agentic-vault/installation/obsidian-setup/.
I'm new to Obsidian and MCP. Please:
1. Ask what computer I use and which AI app I use (Claude Desktop, the Codex
   app, or another app that supports MCP).
2. Walk me through installing Obsidian and opening my folder as a vault.
3. Walk me through installing the plugins listed on that page, starting with
   Local REST API with MCP and Omnisearch. Explain each in one sentence.
4. Help me connect my AI app to the vault's MCP server. Tell me exactly which
   settings screen or config file to open and what to enter. If you can edit
   the config file yourself, do it and show me what you changed.
5. Help me back the vault up to a private GitHub repository with the Git
   plugin, explaining each step in plain words.
6. Test the setup: start a chat and confirm you can read AGENTS.md.
Go one step at a time and wait for me to confirm before moving on.
```

## How the Pieces Fit

- **The vault** is a folder of markdown files on your computer.
- **Obsidian** opens that folder as a vault. You read, edit, link, and search notes there, and see the graph of how they connect.
- **An MCP server** runs alongside Obsidian and gives AI apps access to the vault's files and search.
- **Your AI app** (Claude Desktop, the Codex app, or any MCP-capable tool) connects to that server. Every chat can read `AGENTS.md`, search notes, and create or update files.
- **CLI agents** (Claude Code, Codex CLI, Gemini CLI) can skip MCP and work on the files directly from a terminal in the vault folder.
- **GitHub** holds a private copy of the vault as a git repository, for backup and history.

Because everything is plain files, you and the AI always see the same vault. An edit you make in Obsidian is there for the AI's next read, and a file the AI writes shows up in Obsidian right away.

## Setup Steps

1. Install Obsidian and open your vault folder with **Open folder as vault**.
2. Install the community plugins below. At minimum, install **Local REST API with MCP** and **Omnisearch**.
3. Add the vault's MCP server to your AI app's MCP settings, using the connection details the plugin shows.
4. Back the vault up to GitHub (next section).
5. Start a chat and ask the AI to read `AGENTS.md`. It should report the current phase and last session.

## Back Up to GitHub

Keep the vault in a private GitHub repository. The vault folder is already a git repository if you created it with `init-vault.sh`.

1. Create a private repository on GitHub and add it as the vault's remote (`git remote add origin <url>`).
2. Install the **Git** plugin in Obsidian and turn on scheduled commit and push.

You get an off-site backup, a full history of every change you or the AI made, and a way to undo any AI edit. Coding agents working in other repositories, or in the cloud, can also clone the vault to read its decisions.

## Plugins That Help the AI

| Plugin | Type | Why it helps |
|---|---|---|
| **Local REST API with MCP** | Community | Runs an MCP server for the vault, so desktop AI apps can read, search, and write notes. |
| **Omnisearch** | Community | Fast full-text search with an HTTP API that agents can query when they don't know a note's exact name. |
| **Bases** | Core | Turns decision-record frontmatter into queryable tables (see `decisions/_BASES_SCHEMA.md`). |
| **Properties** | Core | Shows and edits YAML frontmatter, such as decision status and evidence maturity tags. |
| **Backlinks** and **Outgoing links** | Core | Show what links to a note and what it links to, which is how reweaves find affected decisions. |
| **Graph view** | Core | Shows the whole vault as a map, making orphaned notes and clusters easy to spot. |
| **Git** | Community | Commits and pushes the vault to GitHub on a schedule, so every AI edit is backed up and can be reviewed or undone. |
| **Find orphaned files and broken links** | Community | Lists notes nothing links to and links that point nowhere, for vault maintenance sessions. |
| **Linter** | Community | Keeps frontmatter and formatting consistent across files written by different AI sessions. |
| **Templater** | Community | Inserts templates for new decision records, research docs, and idea notes. |

## Optional Plugins

| Plugin | Why you might want it |
|---|---|
| **Smart Connections** | Semantic search that finds related notes by meaning, not just matching words. |
| **Dataview** | Custom queries over frontmatter, such as every `[emerging]` research doc. |
| **Agent Client** or **Copilot** | Run Claude Code or Codex in a panel inside Obsidian. |

## Without Obsidian

Obsidian is recommended, not required. Any editor that saves markdown works, and CLI agents need only the files ([Tooling Alternatives](tooling-alternatives.md)).
