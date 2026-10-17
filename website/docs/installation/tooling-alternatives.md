# Tooling Alternatives

The vault is a folder of markdown files, so any editor that reads and saves `.md` files works. We recommend [Obsidian](https://obsidian.md/) for its wikilinks, graph view, local files, and MCP integration.

## Windows

1. **Notepad++.** A fast, lightweight editor. It has no graph view or wikilink support, but it's fine for editing `SYSTEM.md` and plain notes.
2. **VS Code.** With the *Markdown All in One* and *Foam* extensions, it supports wikilinks and a graph view.
3. **Zettlr.** An open-source markdown editor for researchers and writers, with cross-linking.

## Cross-Platform

1. **Logseq.** An open-source outliner that stores local files and supports wikilinks (`[[like this]]`) and a graph view.
2. **Cursor, Windsurf, or Roo Code.** If you already use an AI IDE, its search and markdown preview are enough to manage the vault.
3. **Neovim or Emacs.** *Telekasten* (Neovim) and *Org-roam* (Emacs) add linked-note features in the terminal.

## Web-Based

Cloud tools make it harder for local CLI agents like `claude` or `gemini` to read your files.

1. **GitHub or GitLab.** Put the vault in a private repository and edit files in the browser, which renders markdown.
2. **Notion.** You can keep `SYSTEM.md` content in Notion, but exporting back to markdown for an agent is awkward.
3. **Google Docs.** It has no markdown or folder nesting, so it doesn't suit the vault itself. Use it for early drafts only.
