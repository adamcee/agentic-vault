---
id: style-core-001
date: YYYY-MM-DD
status: Active
tags: [style-guide, writing-discipline, core]
---
# AI Writing Discipline: Core Architecture

## BLUF
All architectural, strategic, and decision-based vault documents must adhere to strict operational brevity to optimize multi-agent LLM parsing.

## Architecture
- **Active Voice:** Use active voice exclusively. Omit needless words.
- **BLUF (Bottom Line Up Front):** The core decision or insight must be the first sentence. Zero introductions.
- **The Paragraph Ban:** Limit standard paragraphs to a maximum of two sentences. If a thought requires more, use a bulleted list with bolded lead-in terms.
- **AI Silence:**
  - Absolutely no throat-clearing ("I have analyzed...").
  - Extends to document body text. Banned phrases: "This section covers," "As previously discussed," "It is worth noting," "The following table shows."
- **Table/List Preamble Ban:**
  - If a table or list is self-explanatory, do not precede it with a narrative paragraph.
- **Grammatical Completeness:**
  - Write complete, grammatically correct sentences. Short sentences are good. Fragments are not.
- **Prefer Simpler Language:**
  - Use the plainest word that carries the meaning. "Different" over "inverted."
- **No Reification:**
  - Do not name abstract observations. If two things differ, describe the difference. Do not capitalize it or declare it a principle.
- **Semantic Deduplication:**
  - Never stack near-synonymous adjectives ("continuous, formative, real-time, embedded"). Pick the most precise term; use it once.
- **ADR/PDR Scope Boundary:**
  - ADRs and PDRs record Context, Decision, and Consequences. They do not contain implementation specs, code examples, or step-by-step workflows.