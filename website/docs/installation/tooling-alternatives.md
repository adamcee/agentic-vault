# Tooling Alternatives

While we recommend [Obsidian](https://obsidian.md/) for managing your Agentic Vault due to its excellent Markdown support, local-first architecture, and robust plugin ecosystem (like `obsidian-roamlinks` and MCP integration), you have many great alternatives depending on your workflow and operating system.

## 🪟 Windows Options

If you are on Windows and looking for local-first alternatives:

1. **Notepad++**: A very lightweight, fast text editor. It won't have graph views or automatic wikilink resolution natively, but it's great for quickly editing `SYSTEM.md` or adding plain text notes.
2. **VS Code**: Microsoft's free code editor has fantastic Markdown support. With extensions like *Markdown All in One* and *Foam*, you can replicate almost all of Obsidian's features, including wikilinks and graph views.
3. **Zettlr**: An open-source Markdown editor specifically designed for personal knowledge management, researchers, and writers. It supports cross-linking and is a strong, privacy-focused alternative.

## 🌐 General & Cross-Platform Alternatives

1. **Logseq**: An open-source, privacy-first alternative to Obsidian. It is an outliner at its core but has excellent local file management, wikilinks (`[[like this]]`), and graph views. 
2. **Cursor / Windsurf / Roo Code**: If you are a developer, your AI-native IDE is already a great vault manager. Use global search to navigate your docs, and use the IDE's built-in Markdown preview to read your architecture decisions.
3. **Neovim / Emacs**: For CLI power users, plugins like *Telekasten* (Neovim) or *Org-roam* (Emacs) offer incredibly powerful vault-management features right in your terminal.

## ☁️ Web-Based Alternatives

If you don't want to install software and prefer a cloud-synced solution (Note: this makes it harder for local CLI agents like `claude` or `gemini` to read your files automatically):

1. **GitHub/GitLab Web Interface**: Simply upload your vault to a private repository and edit the Markdown files directly in your browser. GitHub natively renders Markdown beautifully.
2. **Notion**: You can copy your `SYSTEM.md` constraints into Notion and use it to track your project. Be aware that exporting back to Markdown for an agent to read can be clunky.
3. **Google Docs**: Not recommended for the actual vault structure due to lack of Markdown and folder nesting, but can be used for drafting initial ideas before pasting them into your IDE.

## The Core Rule: Plain Text

Regardless of the tool you choose, the Agentic Vault relies on **plain text files (Markdown)**. As long as your tool can read, edit, and save `.md` files in a folder structure, it can be used to manage your vault!