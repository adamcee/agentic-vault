---
id: pilot-usage-weeks-1-2
date: 2026-10-06
status: Active
tags: [research, pilot, usage-data, shift-swaps, sms]
evidence-maturity: emerging
source: Brigade audit log and SMS send log from two pilot restaurants, 2026-09-21 to 2026-10-04
---
# Pilot Usage Data, Weeks 1 and 2

Managers approved 57 of 59 swap requests in the first two pilot weeks, with a median wait of 7 minutes, and both denials were cross-role swaps. Two restaurants over two weeks is one small sample, so the evidence is `emerging`.

## Pilot Setup
- **Restaurant A:** one location, 40 seats, 18 staff, one manager.
- **Restaurant B:** two locations, 31 staff, two managers who share scheduling.
- **Period:** 2026-09-21 to 2026-10-04, two weekly schedules per location and six in total.
- **Data:** the audit log required by clause S2 of [[architecture/CONSTITUTION]] and the SMS send log. This round included no interviews.

## Findings

| Metric | Restaurant A | Restaurant B | Total |
|---|---|---|---|
| Weekly schedules published in Brigade | 2 of 2 | 4 of 4 | 6 of 6 |
| Schedules built in a desktop browser | 2 | 4 | 6 |
| Staff who opened at least one shift link | 17 of 18 | 28 of 31 | 45 of 49 |
| Staff who installed the PWA | 6 | 9 | 15 |
| Swap requests | 22 | 37 | 59 |
| Same-role swap requests | 19 | 32 | 51 |
| Swaps approved | 21 | 36 | 57 |
| Median minutes to a manager's decision | 5 | 9 | 7 |
| SMS messages sent | 214 | 389 | 603 |

All 51 same-role swaps were approved. Of the eight cross-role swaps, managers approved six and denied two.

At Restaurant A, a manager denied a server's request to take a bartender shift because the server lacks bar certification. At Restaurant B, a manager denied a line cook's request to cover a prep shift because it would have put him into overtime.

Three same-role swaps at Restaurant B waited more than three hours because the deciding manager was off shift. In two of them, staff texted the manager directly to ask.

## Interpretations
- We read this to mean same-role swaps that add no overtime could be approved automatically without losing the check managers care about. Fifty-nine swaps at two restaurants cannot settle that, so the next step is to ask the pilot managers.
- Only 15 of 49 staff installed the PWA, yet 45 opened shift links, so SMS links are the main way staff reach Brigade.

## Reweave Triggers
- [[decisions/product/PDR-P002-manager-approval-for-swaps]]: **weakened**. Managers approved nearly every swap within minutes, and approval caught problems only in cross-role swaps. Flagged for human review; not yet superseded.
- [[decisions/technical/ADR-T002-responsive-web-pwa]]: **strengthened**. Every schedule was built on a desktop, and staff rely on SMS links more than the installed PWA.
- [[decisions/product/PDR-P001-flat-fee-per-location]]: no change. The pilot is free, so it says nothing about willingness to pay.
- [[ideas/auto-approve-same-role-swaps]]: opened from this data.
- Action items went to Phase 2 of [[prototype/implementation-plan]].
