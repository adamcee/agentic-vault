# Tooling Alternatives

**Recommendation:** use [Obsidian](https://obsidian.md/) if you can ([Obsidian Setup](obsidian-setup.md)). If you can't or would rather not, pick a desktop editor from the list below that shows backlinks, such as Zettlr, Logseq, or VS Code with Foam.

The vault is plain markdown, so any editor that saves `.md` files works. What you lose outside Obsidian is mostly **backlinks**, the panel that shows every note linking to the one you're reading, and the graph view of the whole vault.

Backlinks are how you see that a new research doc touches an old decision. Your AI can still find links by searching the files, but you lose that view.

## Desktop Editors

All of these run on Windows, Mac, and Linux and keep your vault as local files that CLI agents can read.

| Editor | Wikilinks | Backlinks | Graph view | Notes |
|---|---|---|---|---|
| **Zettlr** | Yes | Yes, in the Related Files panel | Yes | A markdown editor for researchers and writers. |
| **Logseq** | Yes | Yes, as Linked References | Yes | An outliner; it works best with notes written as bullet lists. |
| **VS Code with Foam** | Yes | Yes | Yes | Add the *Foam* extension (and optionally *Markdown All in One*). |
| **Neovim** | Yes, with a plugin | Yes, with *obsidian.nvim* or *Telekasten* | No | For people who already live in the terminal. |
| **Cursor, Windsurf, or Roo Code** | No | No, unless you add a VS Code extension such as Foam | No | Fine if you already use an AI IDE; search and markdown preview cover the basics. |

## Web-Based Tools

**We don't recommend web-based tools for the vault.** Local CLI agents can't read the files directly, links and frontmatter don't survive export cleanly, and you no longer own plain files.

- **GitHub or GitLab in the browser** works for editing files in a private repository, and GitHub renders markdown. It has no backlinks.
- **Google Docs** has no markdown or folder structure, so keep it for early drafts at most.

### Using Notion Instead

The method's principles still work in Notion: one master page, decision records, research tied to decisions, and session logs. Notion's `@` mentions give you backlinks. If you already live in Notion, give this prompt to your AI:

```text
I want to apply the Agentic Vault method (https://adamcee.github.io/agentic-vault/)
in Notion instead of a folder of markdown files. Use the template at
https://github.com/adamcee/agentic-vault/tree/main/template as the model and
help me build the Notion version:
1. A top-level page for my project, with a child page "AGENTS" holding what
   AGENTS.md holds: project summary, current phase, hard constraints, standing
   decisions, and the session protocols.
2. A "Decisions" database with properties for ID, type (ADR or PDR), status
   (proposed, accepted, superseded, rejected), date, supersedes, and
   superseded-by.
3. Databases for research (with an evidence-maturity property), ideas (with a
   resolved-by property), concepts, and drafts.
4. A "Session History" page where each session adds one line, and an
   "Implementation Plan" page for action items.
5. Use @ mentions wherever the template uses [[wikilinks]], so backlinks work.
If you can access my Notion workspace (for example through a Notion MCP
connector), create these yourself and tell me what you made. Otherwise give me
step-by-step instructions. Then interview me about my project and fill in the
AGENTS page.
```
