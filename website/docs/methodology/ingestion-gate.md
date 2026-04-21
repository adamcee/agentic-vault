# The Ingestion Gate

AI-generated content does not go directly into the vault. It lands in `drafts/` first, where it passes a checklist before admission.

## Why the Gate Exists

This protocol was added after an audit found that roughly forty percent of writing-discipline violations in the vault originated from AI-generated reports that had been admitted without tightening. The reports were often factually useful, but they carried the usual AI prose patterns: hedge-phrases, meta-commentary, reified observations, paragraph bloat.

Once in the vault, that prose became the corpus that future AI sessions read as the project's voice. The rot compounded.

## The Rule

All AI-generated content (research reports, competitive analyses, synthesis docs — regardless of which model produced it) lands in `drafts/` first. Nothing moves from `drafts/` into the vault without passing:

1. **The [writing discipline checklist](writing-discipline.md)** — BLUF, paragraph ban, no meta-commentary, no reification.
2. **An AI slop purge.** Find-and-replace for the standard tells: *delve, testament, tapestry, synergy, robust, landscape, leverage*. These words are not banned in prose generally; they are banned in vault documents because they are markers of unexamined AI output.
3. **Meta-commentary removal.** *"This section will cover,"* *"As previously discussed,"* *"It is worth noting,"* *"The following table shows"* — delete on sight.
4. **Paragraph compression.** No paragraph exceeds two sentences in strategy or architecture docs.

## The No-Cruft Principle

When tightening an AI-generated draft, strip what's wrong — don't flag it with a warning and keep it. The vault must be accurate, not a museum of errors.

- Correct factual mistakes.
- Remove hallucinated claims.
- Rewrite misframed sections.
- Archive the unmodified original as `_source-<name>.md` in the same directory for citation traceability.

A document that says *"warning: this section is wrong"* is not a vault document. It's a todo.

## The Common Failure Mode

The easiest thing in the world is to ask an AI for a research report, get back eight pages of plausible prose, and paste it into the vault. It feels productive. What it actually does is install a future attention-drain into every session that reads that file. The ingestion gate is the cost you pay once, up front, so you don't pay it forever.
