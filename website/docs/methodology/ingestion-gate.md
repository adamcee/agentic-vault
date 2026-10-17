# The Ingestion Gate

AI-generated content lands in `drafts/` first and enters the vault only after passing a checklist.

## Why It Exists

An audit found that about forty percent of the vault's writing-discipline violations came from AI reports admitted without tightening. The reports were often useful, but they carried hedges, meta-commentary, and padded paragraphs.

Future sessions then read that prose as the project's voice and wrote more like it.

## The Rule

All AI-generated content (research reports, competitive analyses, syntheses, from any model) lands in `drafts/` first. Nothing moves into the vault until it passes:

1. **The [writing discipline checklist](writing-discipline.md).**
2. **A slop-word pass.** Remove the usual tells: *delve, testament, tapestry, synergy, robust, landscape, leverage*. These words are fine elsewhere. In vault documents they signal unreviewed AI output.
3. **Meta-commentary removal.** Delete *"This section will cover,"* *"As previously discussed,"* *"It is worth noting,"* and *"The following table shows."*
4. **Paragraph compression.** No paragraph in a strategy or architecture doc exceeds two sentences.

## Promote With a Link-Aware Move

Move an approved draft with a tool that rewrites links, such as Obsidian's move command or an MCP move. A plain `mv`, or copying the file and deleting the draft, leaves every link pointing at `drafts/`. If that happens, fix the links and run the link checker.

## Fix Errors, Don't Annotate Them

When tightening a draft, remove what's wrong instead of flagging it and keeping it.

- Correct factual mistakes.
- Remove invented claims.
- Rewrite misframed sections.
- Save the unmodified original as `_source-<name>.md` in the same directory, for citation.

A document that says *"warning: this section is wrong"* belongs on a to-do list, not in the vault.

## Why It's Worth the Effort

Asking an AI for a research report and pasting eight pages of plausible prose into the vault feels productive, but every later session that reads the file pays for it. The gate moves that cost to one review up front.
