---
id: bases-schema
date: 2026-08-31
tags: [decisions, schema]
---
# Decision Records Schema

Frontmatter for every ADR and PDR, used by Obsidian Bases and by plain text search.

## Frontmatter

Copy this into every new decision record:

```yaml
---
doctype: ADR  # or PDR
id: ADR-T001  # PDR-P001 for product decisions
domain: technical  # or product
status: accepted  # proposed, accepted, superseded, rejected, deprecated
date: YYYY-MM-DD
tags: [kebab-case, topics]
constitution-clause: null  # e.g. S1 or P3, if the record touches a CONSTITUTION clause
supersedes: null  # "[[decisions/...]]"
superseded-by: null
---
```

## Status Meanings

- **proposed**: drafted in chat, not yet approved. Records aren't written to disk in this state unless the owner asks.
- **accepted**: in force. A record amended with a dated note stays `accepted`.
- **superseded**: fully replaced by a newer record named in `superseded-by`.
- **rejected**: evaluated and declined; lives in `decisions/rejected/`.
- **deprecated**: no longer relevant, with nothing replacing it.

## Naming

`ADR-T001-short-title.md` and `PDR-P001-short-title.md`, numbered in the order they're written. Rejected records keep their number and move to `rejected/`.

## Tags

Keep a short, shared tag list so searches work. Add new tags here before using them:

- approvals: who must sign off on a change, such as swap approval.
- backend: server-side framework and data storage.
- billing: what Brigade charges and the unit it counts.
- client-platform: the app staff and managers run, web or native.
- database: datastore choice and database-level rules.
- django: the Django framework.
- mobile: phone apps and phone-first design.
- pilot: anything shaped by the two-restaurant pilot.
- postgresql: PostgreSQL as datastore and job queue.
- pricing: price levels and pricing models.
- pwa: the installable staff web view.
- react-native: the superseded React Native plan.
- reweave-weakened: a record that new evidence weakened and that awaits a human decision.
- shift-swaps: staff trading or handing off shifts.
- sms: text-message alerts and login links.
- spreadsheet: spreadsheets as a backend or import source.
- web: the responsive web app.

## Search Recipes

- Accepted decisions: `grep -rl "status: accepted" decisions/`
- Everything rejected: `grep -rl "status: rejected" decisions/`
- Records touching a constitution clause: `grep -rl "constitution-clause: S1" decisions/`
- Records that replaced others: `grep -rL "supersedes: null" decisions/`
