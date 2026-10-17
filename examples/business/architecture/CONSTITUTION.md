---
id: CONSTITUTION
date: 2026-08-31
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Business Invariants

*What Curbside Cycles must never do. Breaking an invariant requires a new decision record that supersedes the clause; "it would be easier" is not a reason.*

## Part I — Service & Pricing Invariants

- **P1 — One Van Until Demand Is Proven:** The business runs one van and no fixed premises. A lease, a second vehicle, or a hire waits until the van runs at 80% or more of its [[concepts/van-day|van-day]] capacity for eight weeks in a row.
- **P2 — Quote Before Work:** Every job gets a price before the founder touches the bike. Work beyond the quote needs the rider's yes by text or in person.
- **P3 — Host Permission for Every Stop:** A [[concepts/workplace-stop|workplace stop]] happens only with written permission from a named contact at the host site. The van never parks and works on a site without it.
- **P4 — Labor Floor:** Every price, including membership, must earn at least $60 per hour of van time after parts cost. A price that falls below the floor needs a decision record.

## Part II — Tools & Operations Invariants

- **S1 — One Customer List:** Customer records live only in the booking tool ([[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]). The spreadsheet holds visits, money, and parts, never contact details.

## Part III — Violation Protocol

Breaking an invariant for a real reason takes three steps:
1. Stop, and don't act on the break.
2. Draft an ADR for `decisions/technical/` or a PDR for `decisions/product/` that:
   - Names the CONSTITUTION clause it supersedes.
   - States the reason in full.
   - Lists the alternatives considered.
   - States the consequences.
3. Review the draft in chat and act only after the founder approves the record ([[vault-guide/decision-propagation-protocol]]).
