# The Ideas Lifecycle

Raw ideas go in `ideas/` as short notes until they are promoted, rejected, or absorbed. Most ideas aren't ready for a decision record, and without a place to put them they get lost in chat logs.

## The Problem

A decision record is the wrong place for *"what if we tried X?"* It asks for context, alternatives, and consequences before anyone knows whether the idea is worth that effort. A chat message is the wrong place because it disappears.

Without a home for raw ideas, good ones get lost and weak ones come back every few weeks.

## The `ideas/` Directory

An idea note holds a name, a date, a few sentences, and a `resolved-by` field that starts empty.

```yaml
---
id: short-kebab-case-name
date: YYYY-MM-DD
status: idea
tags: [relevant, tags]
resolved-by: null
---
```

## Resolutions

Each idea ends in one of four states:

- **Promoted.** It became an ADR or PDR. `resolved-by: "[[decisions/technical/ADR-T0XX]]"`.
- **Rejected.** It was evaluated and declined. A full rejection ADR is optional for small cases. `resolved-by: "rejected — [brief reason]"`.
- **Absorbed.** It was folded into another document. `resolved-by: "absorbed into [[path/to/doc]]"`.
- **Open.** The note stays as is.

## Ideas, Concepts, and Drafts

- **`ideas/`** holds proposals: *"What if we built X?"*
- **`concepts/`** holds definitions of existing terms: *"What is X?"*
- **`drafts/`** holds AI-generated content waiting to be tightened before it enters the vault.

The `ideas/` folder costs little to maintain and stops the AI from proposing the same idea every two weeks.
