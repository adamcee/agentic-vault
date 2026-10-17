---
id: CONSTITUTION
date: YYYY-MM-DD
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Project Invariants

*What the project must never do. Breaking an invariant requires a new ADR that supersedes the clause; "it would be easier" is not a reason.*

## Part I — Product & Domain Invariants

[Add your product constraints here. Example:]
- **P1 — No Dark Patterns:** The UX must never use forced continuity or disguised ads.

## Part II — Stack Invariants

[Add your technical stack constraints here. Example:]
- **S1 — TypeScript Only:** No plain JavaScript in the `src/` directory.

## Part III — Violation Protocol

If there is a genuine reason to break an invariant:
1. Stop. Do not implement the violation.
2. Create an ADR in `/decisions/technical/` or `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the ADR reviewed before implementing.