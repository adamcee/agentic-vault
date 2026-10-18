# Decision Records (ADRs & PDRs)

Decision records capture what you chose, what you rejected, and why. They live in `decisions/`: Architecture Decision Records (ADRs) for technical choices and Product Decision Records (PDRs) for product choices.

## Why AI Needs Them

A fresh AI session has no record of past decisions, so it reopens them. If you rejected MongoDB three weeks ago, today's session may suggest it again.

An ADR stating "MongoDB was rejected because of X" stops this. The AI reads the record and works within it.

## Who Writes Them

You and the AI both write decision records. Write one yourself whenever you make a call, or have the AI draft it; it's the same file either way.

## Review Before Writing

When the AI drafts a record, it does so in chat first: the AI lists three alternatives with one-line tradeoffs, drafts the record, and revises it with you, usually over two to four rounds. It writes the file only after you approve.

## Status

An accepted record that gets amended with a dated note stays `accepted`. A record is `superseded` only when a newer one replaces it entirely, and rejected options move to `decisions/rejected/`.

## Keeping Records Current

Two protocols keep decisions accurate over time:

1. **Decision Propagation.** When a decision is made, the AI pushes it into the implementation plan and `CONSTITUTION.md`.
2. **[Reweave](reweave-protocol.md).** When new information arrives, the AI checks whether it strengthens, weakens, or invalidates existing decisions.
