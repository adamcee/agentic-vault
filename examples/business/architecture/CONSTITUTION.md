---
id: CONSTITUTION
date: 2026-08-31
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Business Invariants

*This document defines what Curbside Cycles is and is not allowed to do. These constraints are non-negotiable. Violating any invariant requires a new decision record that explicitly supersedes the relevant clause. "It would be easier" is not sufficient justification.*

## Part I — Service & Pricing Invariants

- **P1 — One Van Until Demand Is Proven:** The business runs one van and no fixed premises. A lease, a second vehicle, or a hire waits until the van runs at 80% or more of its [[concepts/van-day|van-day]] capacity for eight weeks in a row.
- **P2 — Quote Before Work:** Every job gets a price before the founder touches the bike. Work beyond the quote needs the rider's yes by text or in person.
- **P3 — Host Permission for Every Stop:** A [[concepts/workplace-stop|workplace stop]] happens only with written permission from a named contact at the host site. The van never parks and works on a site without it.
- **P4 — Labor Floor:** Every price, including membership, must earn at least $60 per hour of van time after parts cost. A price that falls below the floor needs a decision record.

## Part II — Tools & Operations Invariants

- **S1 — One Customer List:** Customer records live only in the booking tool ([[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]). The spreadsheet holds visits, money, and parts, never contact details.

## Part III — Violation Protocol

If there is a genuine reason to violate any invariant in this document:
1. Stop. Do not act on the violation.
2. Create an ADR in `/decisions/technical/` or a PDR in `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the record reviewed by the founder before acting.
