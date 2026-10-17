---
doctype: ADR
id: ADR-T001
domain: technical
status: superseded
date: 2026-08-31
tags: [client-platform, mobile, react-native]
constitution-clause: null
supersedes: null
superseded-by: "[[decisions/technical/ADR-T002-responsive-web-pwa]]"
---
# ADR-T001: React Native App for Managers and Staff

> **Superseded 2026-09-10** by [[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]] after a second interview round confirmed that managers schedule on a computer.
>
> **Weakened 2026-09-04.** Four of five managers in interview round 1 build the schedule on a laptop or back-office PC, not a phone ([[research/manager-interview-synthesis]] [emerging]). Flagged for human review.

## Context
Brigade needs a client that managers use to build weekly schedules and staff use to see shifts. The co-founder expected managers to build schedules on their phones between other tasks during service [unsourced].

## Decision
Build one React Native app for iOS and Android, with a manager view and a staff view in the same app.

## Alternatives Considered
- **Responsive web app.** It is cheaper to build, but web push notifications on phones looked unreliable.
- **Two native apps (Swift and Kotlin).** They give the best phone experience, but a solo developer cannot maintain two codebases.

## Consequences
- One codebase covers both phone platforms.
- Every staff member must install an app from an app store before seeing a single shift.
- App-store review adds days to every release.
