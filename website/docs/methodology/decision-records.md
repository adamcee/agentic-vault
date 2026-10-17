# Decision Records (ADRs & PDRs)

Decision records capture what you chose, what you rejected, and why. They live in `decisions/`: Architecture Decision Records (ADRs) for technical choices and Product Decision Records (PDRs) for product choices.

## Why AI Needs Them

A fresh AI session has no record of past decisions, so it reopens them. If you rejected MongoDB three weeks ago, today's session may suggest it again.

An ADR stating "MongoDB was rejected because of X" stops this. The AI reads the record and works within it.

## Keeping Records Current

Two protocols keep decisions accurate over time:

1. **Decision Propagation.** When a decision is made, the AI pushes it into the implementation plan and `CONSTITUTION.md`.
2. **[Reweave](reweave-protocol.md).** When new information arrives, the AI checks whether it strengthens, weakens, or invalidates existing decisions.
