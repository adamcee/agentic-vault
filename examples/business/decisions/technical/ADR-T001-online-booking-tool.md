---
doctype: ADR
id: ADR-T001
domain: technical
status: accepted
date: 2026-09-04
tags: [booking, tools, operations]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T001: Use a Hosted Online Booking Tool

## Context
The founder works with greasy hands and cannot answer the phone mid-repair. Each [[concepts/workplace-stop|workplace stop]] also needs a block of time slots that riders at one site can claim before the van arrives.

## Decision
Curbside Cycles takes bookings through a hosted online booking tool at $30 a month. It holds the customer list, per-stop slots, reminders, and a card on file; the spreadsheet keeps the money and the visit log.

## Alternatives Considered
- **Phone and spreadsheet.** It costs nothing, but every missed call during a repair is a lost booking, and slot clashes need manual fixing.
- **Hiring a part-time scheduler.** It adds a wage before the business pays the founder one.

## Consequences
- The monthly fee is a fixed cost from day one.
- Customer records live in one place ([[architecture/CONSTITUTION]] S1).
- Commuters were assumed to prefer booking online over calling [unsourced].

> **Reweave 2026-10-05 (strengthened):** 44 of 52 pilot visits were booked through the tool rather than by phone or text ([[research/pilot-month-results]] [emerging]).
