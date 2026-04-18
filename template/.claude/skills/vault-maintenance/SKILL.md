---
name: vault-maintenance
description: "Audits the health and integrity of the vault. Checks for broken wikilinks, orphaned notes, and dead ends. Trigger when tasked with 'vault maintenance', 'checking links', or 'cleaning up the vault'."
---

# Vault Maintenance Skill

This skill guides the AI agent through a vault audit.

## 🛠️ Tooling & Fallbacks

**Primary Tool (Obsidian CLI):**
If the project uses Obsidian and the CLI is installed (e.g. `/Applications/Obsidian.app/Contents/MacOS/obsidian`), use it for robust graph queries.
- Broken links: `obsidian unresolved`
- Orphans: `obsidian orphans`

**Fallback Tool (Native Search):**
If the Obsidian CLI is not available, you MUST degrade gracefully and use native filesystem tools (`grep_search`, `glob`):
- **Broken Links:** Use `grep_search` for the regex `\[\[(.*?)\]\]` to find all wikilinks. Cross-reference the extracted filenames against the actual files using `glob`.
- **Orphans:** Use `glob` to list all `.md` files. For each file, use `grep_search` to see if its name appears inside `[[ ]]` in any other file. (This is computationally heavy, so only do it if the vault is small or the user specifically asks).

## 📋 Maintenance Operations

### 1. Unresolved (Broken) Links
Find all wikilinks that point to non-existent files.
*Action:* Fix typos, point to the nearest relevant index/README, or ask the user if the file should be created.

### 2. Orphaned Notes
Find files that have *no incoming links*.
*Action:* Find a logical parent document (e.g., `SYSTEM.md` or a `README.md`) and weave a `[[wikilink]]` to the orphaned note.

### 3. Dead End Notes
Find files that have *no outgoing links*.
*Action:* Insert relevant `[[wikilinks]]` pointing to other vault notes (concepts, ADRs, strategy).