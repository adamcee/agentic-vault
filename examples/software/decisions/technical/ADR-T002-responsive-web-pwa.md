---
doctype: ADR
id: ADR-T002
domain: technical
status: accepted
date: 2026-09-10
tags: [client-platform, web, pwa, sms]
constitution-clause: P1
supersedes: "[[decisions/technical/ADR-T001-react-native-manager-app]]"
superseded-by: null
---
# ADR-T002: Responsive Web App With SMS Alerts

## Context
[[decisions/technical/ADR-T001-react-native-manager-app|ADR-T001]] assumed managers schedule from their phones. Eight of nine interviewed managers build the weekly schedule on a laptop or back-office PC, usually in one sitting ([[research/manager-interview-synthesis]] [supported]).

Staff need much less: they view shifts and request swaps from a phone. All nine managers said their staff would resist installing another app for work ([[research/manager-interview-synthesis]] [supported]).

## What Changed
Interview round 1 weakened ADR-T001 on 2026-09-04. Round 2 repeated the finding with four more managers, so the team replaced the decision instead of patching it.

## Decision
Build one responsive web app. Managers get a desktop-first scheduling grid, and staff get a phone layout that installs from the browser as a PWA (progressive web app). An SMS (text message) carries every shift change and a login link, so staff never need a password.

## Alternatives Considered
- **Keep React Native.** It optimizes for a device managers do not schedule on, and it forces every staff member to install an app.
- **Native iOS app first.** Staff at every interviewed restaurant carry a mix of Android phones and iPhones ([[research/manager-interview-synthesis]] [supported]).
- **Email instead of SMS.** Seven of nine managers said kitchen staff rarely read email ([[research/manager-interview-synthesis]] [supported]).

## Consequences
- One codebase ships without app-store review.
- Web push on phones is less reliable than native push, so SMS carries every time-sensitive alert, and each message costs money.
- The decision adds constitution clause P1 to [[architecture/CONSTITUTION]].
- A reweave on 2026-10-06 strengthened this choice: all six pilot schedules were built in a desktop browser ([[research/pilot-usage-weeks-1-2]] [emerging]).
