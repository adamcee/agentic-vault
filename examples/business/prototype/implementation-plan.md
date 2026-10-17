---
id: implementation-plan
date: 2026-09-03
updated: 2026-10-09
status: active
tags: [ledger, plan]
---
# Implementation Plan
*Updated: 2026-10-09*

Every new action item lands in this ledger, and the founder moves items to [[prototype/human-task-list]] during the Friday review. Items use the format `- [ ] **Title**: what, and how you'll know it's done (session type)`, with `[~]` for in progress.

## Now
- [ ] **Confirm recurring billing**: check that the booking tool can bill members monthly; done when a test member is billed, or a new ADR is drafted in chat if it can't (planning). *(reweave: [[research/pilot-month-results]])*
- [ ] **Offer the membership to repeat riders**: offer it to the 14 pilot repeat customers once billing works; done when each has a yes, a no, or no reply after a week (pilot).
- [ ] **Ask hosts about employer-paid memberships**: ask the three hosts who requested a plan; done when their answers are summarized with [[prompts/customer-interview-synthesis]] and saved to `drafts/` (research).
- [ ] **Resume the membership-tier work**: pick up from [[drafts/2026-10-09-resume-membership-tiers]]; done when the tier memo is promoted or deleted and the hand-over note is removed (planning).

## For the Owner: Keep, Drop, or Decide
- [ ] **Premium tier in the tier memo**: the draft's $75 tier with two services a month earns about $56 per hour of van time, below the labor floor in [[architecture/CONSTITUTION]] P4; keep it for the second-visit review or drop it (pricing).
- [ ] **Apartment-building weekend stops**: [[ideas/apartment-building-weekend-stops]] waits on the membership launch; keep it open, drop it, or schedule a test stop for Phase 4 (planning).

## Decisions Owed
- [~] **PDR-P005, second-visit price for members**: a member who books every 24 days needs more than one service a month ([[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]]). Round 1 of the chat draft ran on 2026-10-09 and nothing is written to disk; done when the founder approves the record or drops the question (decision).

## Drafts Awaiting Promotion
- [ ] **Tighten the membership tier memo**: run [[drafts/membership-tier-options]] through the promotion checklist and remove its unsourced claims before anyone uses it; done when it moves to `research/` or is deleted (writing).

## Vault Maintenance
- [ ] **Source or cut the seasonality claim**: [[decisions/rejected/PDR-P003-storefront-workshop-lease|PDR-P003]] says spring brings most walk-in repair volume, flagged `[unsourced]`; done when it links a research doc or the line is cut (research).
- [x] Backfilled the `[unsourced]` online-booking claim in [[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]] with [[research/pilot-month-results]] (2026-10-05).

## Phase 1: Set Up the Van and the Basics (Done, 2026-08-31 to 2026-09-06)
- [x] Fit the van with a workstand, bench, compressor, and power station.
- [x] Add commercial use to the van insurance.
- [x] Set up the booking tool with per-stop slots ([[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]).
- [x] Pair the card terminal with the founder's phone and test a payment.
- [x] Print the per-visit price sheet ([[decisions/product/PDR-P002-per-visit-pricing|PDR-P002]]).
- [x] Sign written permission with four host workplaces ([[architecture/CONSTITUTION]] P3).

## Phase 2: Pilot Month (Done, 2026-09-07 to 2026-10-04)
- [x] Work 16 [[concepts/van-day|van days]] across the four hosts.
- [x] Log every visit in the spreadsheet: host, job, price, parts, minutes.
- [x] Run the commuter survey in two office-park bike rooms ([[research/commuter-survey-2026-09]]).
- [x] Log each pilot customer's rebooking interval. *(reweave: [[research/commuter-survey-2026-09]])*
- [x] Price two rented bench days for overhaul jobs ([[decisions/rejected/PDR-P003-storefront-workshop-lease|PDR-P003]]).
- [x] Write up the pilot results ([[research/pilot-month-results]]).

## Phase 3: Membership Launch (Current, 2026-10-07 to 2026-11-15)
Four open Phase 3 items sit under Now and Drafts Awaiting Promotion above.
- [x] Write the membership PDR ([[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]]). *(reweave: [[research/pilot-month-results]])*
- [x] Update the price sheet: non-member commuter service rises to $60.
- [ ] **Track a second month of intervals**: log October rebooking intervals; done when the 24-day median is confirmed or replaced (pilot). *(reweave: [[research/pilot-month-results]])*
- [ ] **Recheck revenue per van day**: compare October and early November against [[strategy/business-goals]] on 2026-11-15; done when the result is logged and any gap is flagged to the founder (planning). *(reweave: [[research/pilot-month-results]])*

## Phase 4: Full-Time Decision (Next, by 2026-12-15)
- [ ] **Sign two more hosts**: get written permission from two more host workplaces; done when six hosts are signed (planning).
- [ ] **Review eight weeks of revenue**: compare revenue per van day with the targets in [[strategy/business-goals]]; done when the comparison is a research doc (research).
- [ ] **Decide on full time**: decide whether the van supports the founder full time; done when the founder approves a PDR (decision).
