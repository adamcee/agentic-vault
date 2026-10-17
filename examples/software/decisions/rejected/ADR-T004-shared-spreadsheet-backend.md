---
doctype: ADR
id: ADR-T004
domain: technical
status: rejected
date: 2026-09-17
tags: [backend, spreadsheet, pilot]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T004: Shared Spreadsheet as the Schedule Backend (Rejected)

## Context
The co-founder proposed running the pilot on a shared spreadsheet, because both pilot restaurants already keep their schedule in one. Brigade would read and write the sheet through its API and add SMS alerts and a staff phone view on top, which promised a pilot in days instead of weeks.

## Decision
Rejected. Brigade keeps schedule data in PostgreSQL as set by [[decisions/technical/ADR-T003-django-and-postgresql|ADR-T003]].

## Reasons for Rejection
- **No per-person permissions.** Anyone with edit access can change every shift, including other staff members' shifts.
- **No reliable change events.** SMS alerts need to know exactly which shift changed, and polling a sheet for differences misses or repeats edits.
- **No transactions.** Restaurant B has two managers who edit the same week, and a sheet cannot enforce the no-overlap rule between their edits.
- **No audit trail.** A sheet's version history does not meet constitution clause S2 in [[architecture/CONSTITUTION]].

## Alternatives Considered
- **One-time spreadsheet import at onboarding.** Accepted as a plan task: owners keep their staff list and recurring shifts without retyping them.

## Consequences
- The pilot start moves to 2026-09-21, about a week later than the spreadsheet route promised.
- Future sessions should not reopen this option to save build time.
