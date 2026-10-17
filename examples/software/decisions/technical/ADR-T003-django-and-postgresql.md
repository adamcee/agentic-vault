---
doctype: ADR
id: ADR-T003
domain: technical
status: accepted
date: 2026-09-15
tags: [backend, database, postgresql, django]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T003: Django on PostgreSQL, With PostgreSQL as the Only Datastore

## Context
[[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]] made Brigade a server-rendered web app, so it needs a server framework and a datastore. Schedule data is relational: locations have staff, staff hold roles, shifts belong to a week and a role, and a [[concepts/shift-swap]] links two people to one shift.

Two rules need database transactions. No one may be booked on overlapping shifts, and every change to a published shift must write an audit row (constitution clause S2).

## Decision
Use Django on PostgreSQL. PostgreSQL is the only datastore, and background jobs such as SMS sends run from a queue table in PostgreSQL instead of a separate broker.

## Alternatives Considered
- **SQLite.** It is the simplest to run, but our host offers managed backups and point-in-time recovery only for PostgreSQL, and SQLite cannot enforce the no-overlap rule as a database constraint.
- **A hosted backend service with a document store.** This was the implied plan under [[decisions/technical/ADR-T001-react-native-manager-app|ADR-T001]], and it handles questions like "who is free and qualified for Friday close" poorly.
- **A separate job broker.** It adds a second datastore to run and back up for a job volume that a queue table handles at pilot scale.

## Consequences
- PostgreSQL rejects double-booked shifts even if application code has a bug.
- One service needs backups and monitoring.
- The decision adds constitution clause S1 to [[architecture/CONSTITUTION]].
- The queue table needs review if SMS volume grows far past pilot levels.
