# Implementation Plan
*Updated: 2026-10-09*

The vault ledger. AI sessions route every new action item here.

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
- [ ] Add "copy last week" to the scheduling grid ([[ideas/copy-last-week]]).
- [ ] Prototype auto-approval for same-role swaps that add no overtime, behind a per-location setting (reweave 2026-10-06, [[ideas/auto-approve-same-role-swaps]]).
- [ ] Ask all three pilot managers whether they would turn auto-approval on (reweave 2026-10-06).
- [ ] Decide on [[decisions/product/PDR-P002-manager-approval-for-swaps|PDR-P002]]: if the managers agree, write PDR-P003 to supersede it; if not, record why it stands (reweave 2026-10-06).
- [ ] Send the backup manager an SMS when a swap waits more than one hour (reweave 2026-10-06).
- [ ] Track SMS messages per location per week against the fee in [[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]].
- [ ] Tighten [[drafts/ai-report-sms-provider-comparison]] through the ingestion gate, then choose an SMS provider.

## Phase 3: First Paying Locations (Next)
- [ ] Add billing per [[concepts/location]] ([[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]]).
- [ ] Test the $49 price with five owners outside the pilot, which would close the `[unsourced]` flag in PDR-P001.
