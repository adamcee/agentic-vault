---
id: manager-interview-synthesis
date: 2026-09-10
status: Active
tags: [research, interviews, managers, staff]
evidence-maturity: supported
source: Co-founder's notes from nine manager interviews in two rounds, 2026-09-01 to 2026-09-09
---
# Manager Interview Synthesis

Managers build the weekly schedule on a laptop or back-office PC in one sitting, and staff only need to see shifts and trade them from a phone. Both interview rounds found this, so the evidence is `supported`.

## Method
- **Round 1 (2026-09-01 to 2026-09-03):** five managers at independent restaurants with one to three locations and 12 to 45 staff. Each 45-minute call walked through how they built last week's schedule.
- **Round 2 (2026-09-07 to 2026-09-09):** four more managers with the same script, including the manager of pilot Restaurant A and one of the two managers at pilot Restaurant B.
- **Maturity:** `emerging` after round 1 on 2026-09-04. It was raised to `supported` on 2026-09-10 because round 2 repeated every finding below.

## Findings

| Finding | Round 1 (n=5) | Round 2 (n=4) | Total |
|---|---|---|---|
| Builds the schedule on a laptop or back-office PC | 4 | 4 | 8 of 9 |
| Builds it in one sitting of one to two hours a week | 4 | 3 | 7 of 9 |
| Says staff mainly need to see shifts and request swaps | 5 | 4 | 9 of 9 |
| Says staff would resist installing another app for work | 5 | 4 | 9 of 9 |
| Reports staff carrying a mix of Android phones and iPhones | 5 | 4 | 9 of 9 |
| Says kitchen staff rarely read email | 4 | 3 | 7 of 9 |
| Named per-seat billing as a reason to leave or avoid an app | 3 | 3 | 6 of 9 |
| Wants to approve every swap | 4 | 4 | 8 of 9 |

One round 1 manager put it plainly: "I do the schedule Sunday night at the office desk, with last week's sales report open next to it."

The one manager who schedules on a phone runs a single 12-person cafe and builds the week in about 20 minutes.

## Interpretations
- We read the laptop finding to mean the manager grid should be desktop-first and the phone layout should serve staff.
- The wish to approve every swap is a stated preference. Pilot usage should show whether managers act on it or approve by reflex.

## Reweave Triggers
- [[decisions/technical/ADR-T001-react-native-manager-app]]: **weakened** on 2026-09-04 by round 1, then **invalidated** on 2026-09-10 by round 2. Superseded by ADR-T002.
- [[decisions/technical/ADR-T002-responsive-web-pwa]]: new decision built on this evidence.
- [[decisions/product/PDR-P001-flat-fee-per-location]]: **strengthened**. Per-seat complaints support flat pricing per location.
- [[decisions/product/PDR-P002-manager-approval-for-swaps]]: new decision built on the swap-approval finding.
- [[strategy/goals-and-audience]]: **strengthened**. The interviews confirm the split between managers on a laptop and staff on a phone.
