# AI Writing Discipline

Vault documents are written for a reader with no context: the next AI session. Short, direct prose lets that session load more of the project and find the main point fast.

## The Rules

- **Main point first (BLUF).** The first sentence of a document or section states the decision or finding. No introductions.
- **Two-sentence paragraphs.** If a thought needs more, use a bulleted list with bold lead-ins.
- **Active voice.** Omit needless words.
- **No meta-commentary.** Cut "This section covers," "As previously discussed," "It is worth noting," and "The following table shows."
- **No preamble before a table or list** that explains itself.
- **Complete sentences.** Short sentences are good. Fragments are not.
- **Plain words.** "Uses," not "utilizes." "Different," not "inverted."
- **No reification.** If two things differ, describe the difference in a sentence. Don't capitalize it, give it a header, or call it a principle.
- **No stacked synonyms.** Pick the most precise adjective and use it once.
- **One em-dash per paragraph, at most.**
- **ADRs and PDRs stay short.** They record context, decision, and consequences. Implementation specs and multi-line code go elsewhere.

## The Tightening Checklist

Every document an AI writes or substantially edits must pass this checklist before the task is done. The full version lives in the template's `SYSTEM.md`.

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
