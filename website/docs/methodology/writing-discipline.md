# AI Writing Discipline

Vault documents are written for you first and the next AI session second. Cutting AI filler makes a document faster for you to read, check, and act on, and it lets the AI load more of the project at once.

## Plain Language (ISO 24495-1)

The rules build on ISO 24495-1:2023, the international plain language standard. A document meets it when its readers can:

- **Get what they need** (relevant).
- **Find it easily** (findable).
- **Understand it** (understandable).
- **Use it** to act or decide (usable).

## The Rules

- **Main point first (BLUF).** The first sentence of a document or section states the decision or finding. No introductions.
- **Two-sentence paragraphs.** If a thought needs more, use a bulleted list with bold lead-ins.
- **Active voice.** Omit needless words.
- **No meta-commentary.** Cut "This section covers," "As previously discussed," "It is worth noting," and "The following table shows."
- **No preamble before a table or list** that explains itself.
- **Complete sentences.** Short sentences are good. Fragments are not.
- **Plain words.** "Uses," not "utilizes." "Different," not "inverted."
- **Define terms on first use.** Spell out abbreviations and explain terms of art the first time they appear.
- **Descriptive headings.** A heading says what the section contains ("Pricing Is Per Visit"), not a label ("Discussion").
- **No reification.** If two things differ, describe the difference in a sentence. Don't capitalize it, give it a header, or call it a principle.
- **No stacked synonyms.** Pick the most precise adjective and use it once.
- **One em-dash per paragraph, at most.**
- **ADRs and PDRs stay short.** They record context, decision, and consequences. Implementation specs and multi-line code go elsewhere.

## The Tightening Checklist

Every document an AI writes or substantially edits must pass this checklist before the task is done. The full version lives in the template's `AGENTS.md`.

1. The first sentence states the core claim.
2. No paragraph exceeds two sentences.
3. No narrative preamble before a self-explanatory table or list.
4. No stacked near-synonymous adjectives.
5. No meta-commentary in the body.
6. ADRs and PDRs contain no implementation specs or multi-line code blocks.
7. Executive summaries run 12 lines or fewer.
8. No reified observations.
9. No sentence fragments.
10. No more than one em-dash per paragraph.

See [The Ingestion Gate](ingestion-gate.md) for how the checklist applies to AI-generated drafts.
