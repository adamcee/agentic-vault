---
id: quartz-for-example-site
date: 2026-04-17
status: idea
tags: [website, documentation, quartz, mkdocs, user-experience]
resolved-by: null
---
# Idea: Use Quartz for the Example Vault Site

## Context
Currently, we have initialized MkDocs Material to serve as both the documentation hub (linear installation guides, methodology) and the host for the interactive `example/` BrewTrack vault (using the `mkdocs-roamlinks-plugin` to hack in wikilink support).

## The Proposal
Split the web presence into two tools optimized for their specific jobs:
1. **MkDocs Material** for the primary landing page, methodology explanations, and tiered installation guides (linear, professional, highly legible).
2. **Quartz** specifically to host and render the `example/` vault. 

## Rationale
The core value proposition of the Agentic Vault is managing context as a linked graph of markdown files rather than linear wikis. 

MkDocs cannot visually demonstrate this value. It is built for books and chapters. Quartz is built specifically for Obsidian vaults. 

If we use Quartz for the example site, users will experience the "Aha!" moment:
- They will see the interactive **Graph View** connecting ADRs to Strategy.
- They will see the **Backlinks** panel on every page, proving how the Reweave Protocol surfaces connections.
- They will get **Hover Previews** for wikilinks, demonstrating frictionless context gathering.
- It natively supports Obsidian callouts (`> [!info]`), tags, and frontmatter without hacky Python regex plugins.

## Trade-offs
- **Maintenance Overhead:** We would have to maintain two separate web projects and build pipelines. One uses Python (MkDocs) and one uses Node.js/Go (Quartz).
- **Fragmented UX:** The user experience is split between a Material theme (docs) and a Quartz theme (example vault). 

## Next Steps
Evaluate whether the visual impact of the Quartz Graph View is worth the overhead of managing a second build tool before implementing.