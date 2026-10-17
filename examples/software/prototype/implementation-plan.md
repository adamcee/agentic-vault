---
id: implementation-plan
date: 2026-10-09
status: Active
tags: [ledger, planning]
---
# Implementation Plan
*Updated: 2026-10-09*

The AI ledger: every new action item lands here, and the owner moves items to [[prototype/human-task-list]] during weekly review. Item format: `- [ ] **Title**: what, and how you'll know it's done (session type)`, with `[~]` for work in progress.

## Now
- [ ] **Ask the pilot managers about auto-approval**: ask all three pilot managers whether they would turn on auto-approval for same-role swaps that add no overtime; done when all three have answered and the answers are in a research doc (research). From the 2026-10-06 reweave.
- [ ] **Copy last week**: add "copy last week" to the scheduling grid ([[ideas/copy-last-week]]); done when a manager can start a new week from the previous one and edit only the changes (coding).

## For the Owner: Keep, Drop, or Decide
- [ ] **Backup-manager SMS**: send the backup manager an SMS when a swap waits more than one hour; done when the alert fires in the pilot (coding). From the 2026-10-06 reweave. Auto-approval would remove most of these waits, so keep this, drop it, or hold it until PDR-P002 is settled.

## Decisions Owed
- [ ] **Swap approval under PDR-P002**: decide on [[decisions/product/PDR-P002-manager-approval-for-swaps|PDR-P002]]. If the managers agree, draft PDR-P003 in chat to supersede it; if not, record why it stands. Done when the owner approves a record (decision). Waits on the manager answers in Now; from the 2026-10-06 reweave.
- [ ] **SMS provider**: choose a provider after the comparison passes the gate, listing three alternatives and drafting the ADR in chat; done when the owner approves the record (decision).

## Drafts Awaiting Promotion
- [ ] **SMS provider comparison**: tighten [[drafts/ai-report-sms-provider-comparison]] through the ingestion gate, starting from [[drafts/2026-10-09-resume-sms-provider-choice]]; done when a clean doc is in `research/` with its `_source-` original beside it, or the draft is deleted (research).

## Vault Maintenance
- [ ] **First quarterly review**: run [[vault-guide/vault-review-protocol]] and [[vault-guide/implementation-plan-triage]] after the pilot ends; done when every unfixed finding is a task under Vault Maintenance (vault maintenance).

## Phase 1: Foundations (Done, 2026-08-31 to 2026-09-20)
- [x] Interview five managers about how they build schedules today (round 1).
- [x] Interview four more managers, including both pilot restaurants (round 2).
- [x] Stop the React Native setup and archive the spike branch (reweave 2026-09-10, [[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]]).
- [x] Set up the Django project on PostgreSQL ([[decisions/technical/ADR-T003-django-and-postgresql|ADR-T003]]).
- [x] Build the desktop scheduling grid for managers.
- [x] Build the staff phone view with SMS login links ([[decisions/technical/ADR-T002-responsive-web-pwa|ADR-T002]]).
- [x] Add swap requests with manager approval ([[decisions/product/PDR-P002-manager-approval-for-swaps|PDR-P002]]).
- [x] Add the audit log for published shifts (clause S2 of [[architecture/CONSTITUTION]]).
- [x] Add a one-time spreadsheet import for onboarding ([[decisions/rejected/ADR-T004-shared-spreadsheet-backend|ADR-T004]]).

## Phase 2: Two-Restaurant Pilot (Current, 2026-09-21 to 2026-10-30)
- [x] Launch the pilot at Restaurant A and Restaurant B (2026-09-21).
- [x] Export two weeks of audit and SMS logs and write [[research/pilot-usage-weeks-1-2]].
- [ ] **Auto-approval prototype**: prototype auto-approval for same-role swaps that add no overtime, behind a per-location setting ([[ideas/auto-approve-same-role-swaps]]); done when a pilot manager can switch it on for one location (coding). From the 2026-10-06 reweave.
- [ ] **SMS volume per location**: track SMS messages per location per week against the fee in [[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]]; done when a weekly count exists for every pilot location (research).

## Phase 3: First Paying Locations (Next)
- [ ] **Billing per location**: add billing per [[concepts/location]] ([[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]]); done when a test owner can pay for one location (coding).
- [ ] **Price test**: test the $49 price with five owners outside the pilot; done when the results close the `[unsourced]` flag in PDR-P001 (research).
