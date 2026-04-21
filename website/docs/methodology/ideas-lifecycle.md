# The Ideas Lifecycle

Not every idea is ready for an ADR. Most aren't. Without somewhere to put the raw ones, they live in chat logs and die there.

## The Problem

Project ideas arrive faster than you can evaluate them. A decision record is the wrong container for *"what if we tried X?"* — it demands context, alternatives, and consequences before anyone knows if the idea is worth that effort. Chat messages are the wrong container because they disappear.

The result, without a protocol: good ideas get lost, and the same half-formed ideas resurface every few weeks because nobody wrote down the last round of thinking.

## The `ideas/` Directory

Raw ideas go in `ideas/`. An idea note is lighter than a decision record — just a name, a date, a few sentences, and a `resolved-by` field that starts empty.

```yaml
---
id: short-kebab-case-name
date: YYYY-MM-DD
status: idea
tags: [relevant, tags]
resolved-by: null
---
```

## The Four Resolutions

Ideas don't stay in `ideas/` forever. Each one eventually resolves to one of:

- **Promoted to decision** — the idea matured enough for an ADR or PDR. `resolved-by: "[[decisions/technical/ADR-T0XX]]"`.
- **Rejected** — evaluated and declined. A full rejection ADR is optional for lightweight cases. `resolved-by: "rejected — [brief reason]"`.
- **Absorbed** — the idea got folded into another document. `resolved-by: "absorbed into [[path/to/doc]]"`.
- **Still open** — the note stays as-is.

## Why This Is Separate from Drafts and Concepts

Three directories handle three different states. They are not the same thing:

- **`ideas/`** — *"What if we built X?"* Propositions awaiting evaluation.
- **`concepts/`** — *"What is X?"* Definitions and link hubs for existing terms.
- **`drafts/`** — AI-generated content awaiting tightening before vault admission.

## The Common Failure Mode

Without this directory, AI sessions end up proposing the same idea every two weeks because there's no record of the previous round of thinking. The `ideas/` directory is the shortest-form memory in the vault. It costs almost nothing to maintain and prevents the single most common form of relitigation.
