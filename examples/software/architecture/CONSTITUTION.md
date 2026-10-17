---
id: CONSTITUTION
date: 2026-09-15
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Brigade Invariants

*What Brigade must never do. Breaking an invariant requires a new ADR that supersedes the clause; "it would be easier" is not a reason.*

## Part I — Product & Domain Invariants

- **P1 — Staff Need Only a Phone Browser:** Staff see shifts and request swaps from any phone browser, with no app-store install and no password. Added 2026-09-10 by [[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]].
- **P2 — Phone Numbers Serve Scheduling Only:** Staff phone numbers receive shift alerts and login links and nothing else. Brigade never sends marketing texts and never shares a number.
- **P3 — Brigade Does Not Calculate Pay:** Brigade shows scheduled hours but never computes wages, overtime pay, or tips. Pay stays in the owner's payroll tool.

## Part II — Stack Invariants

- **S1 — PostgreSQL Is the Only Datastore:** No second database, cache store, or spreadsheet holds schedule data. Added 2026-09-15 by [[decisions/technical/ADR-T003-django-and-postgresql|ADR-T003]].
- **S2 — Changes to Published Shifts Are Logged:** Every change to a published shift writes an append-only audit row naming who changed what and when. Managers need this record when a staff member disputes a change.

## Part III — Violation Protocol

If there is a genuine reason to break an invariant:
1. Stop. Do not implement the violation.
2. Create an ADR in `/decisions/technical/` or `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the ADR reviewed before implementing.
