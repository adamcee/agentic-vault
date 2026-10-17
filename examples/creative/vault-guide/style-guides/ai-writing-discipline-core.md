---
id: style-core-001
date: 2026-04-06
status: Active
tags: [style-guide, writing-discipline, core]
---
# AI Writing Discipline: Core Architecture

## BLUF
Vault documents are written for the human owner first and the next AI session second. They follow ISO 24495-1 plain language and the rules below.

## Plain Language (ISO 24495-1:2023)
A document is in plain language when its readers can:
- **Get what they need** (relevant). Write for the reader's task and cut what doesn't serve it.
- **Find it easily** (findable). Put the main point first and use headings that say what each section contains.
- **Understand it** (understandable). Use familiar words, short sentences, and define terms on first use.
- **Use it** (usable). The reader can act on the document without asking for clarification.

## Rules
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
- **Define Terms on First Use:**
  - Spell out an abbreviation or define a term of art the first time it appears in a document.
- **Descriptive Headings:**
  - A heading says what the section contains ("Pricing Is Per Visit"), not a vague label ("Discussion").
- **Prefer Simpler Language:**
  - Use the plainest word that carries the meaning. "Different" over "inverted."
- **No Reification:**
  - Do not name abstract observations. If two things differ, describe the difference. Do not capitalize it or declare it a principle.
- **Semantic Deduplication:**
  - Never stack near-synonymous adjectives ("continuous, formative, real-time, embedded"). Pick the most precise term; use it once.
- **ADR/PDR Scope Boundary:**
  - ADRs and PDRs record Context, Decision, and Consequences. They do not contain implementation specs, code examples, or step-by-step workflows.