# Example Vault: Curbside Cycles

Curbside Cycles is a fictional mobile bike-repair van serving one mid-size city, run by a former bike-shop mechanic who wants to know whether one van can pay a full-time wage. This vault picks up five weeks in, on 2026-10-09, after the founder has chosen a market, run a one-month pilot, rejected a storefront lease, and replaced per-visit pricing with a monthly membership.

No software is being built, so most records are product decisions (PDRs) about services, pricing, and market, with one tool decision (ADR).

## Tour

1. **Master file:** [AGENTS.md](AGENTS.md) holds the project, current phase, constraints, tools, standing decisions, and the last session checkpoint.
2. **Business invariants:** [architecture/CONSTITUTION.md](architecture/CONSTITUTION.md) lists the rules no session may break without a decision record.
3. **Superseded decision:** [PDR-P002](decisions/product/PDR-P002-per-visit-pricing.md) shows per-visit pricing, its dated reweave notes, and the pointer to [PDR-P004](decisions/product/PDR-P004-membership-plus-per-visit.md), which replaced it.
4. **Rejected decision:** [PDR-P003](decisions/rejected/PDR-P003-storefront-workshop-lease.md) records why the founder declined a storefront workshop lease.
5. **A reweave:** [research/pilot-month-results.md](research/pilot-month-results.md) ends with Reweave Triggers that weakened PDR-P002 and the business goals and strengthened two other records.
6. **Research with maturity tags:** [research/commuter-survey-2026-09.md](research/commuter-survey-2026-09.md) is a 41-person survey tagged `emerging`, and [PDR-P001](decisions/product/PDR-P001-workplace-commuter-focus.md) shows a claim upgraded to `[supported]` once the pilot agreed with it.
7. **Ideas in each state:** [promoted](ideas/monthly-membership.md), [rejected](ideas/e-bike-battery-service.md), [absorbed](ideas/pre-visit-text-checklist.md), and [open](ideas/apartment-building-weekend-stops.md).
8. **Draft awaiting tightening:** [drafts/membership-tier-options.md](drafts/membership-tier-options.md) is AI prose held at the ingestion gate.
9. **Admitted doc with its original:** [research/local-price-scan.md](research/local-price-scan.md) passed the gate, and [research/_source-local-price-scan.md](research/_source-local-price-scan.md) is the untouched AI original.
10. **Ledger vs. the founder's list:** [prototype/implementation-plan.md](prototype/implementation-plan.md) is the AI ledger, with Now, For the Owner, Decisions Owed, Drafts Awaiting Promotion, and Vault Maintenance above the phases, and reweave tasks marked. [prototype/human-task-list.md](prototype/human-task-list.md) is the founder's own short list, pulled from the ledger on Fridays; AI never writes to it.
11. **Session logs:** [session-history.md](session-history.md) logs ten sessions from 2026-08-31 to 2026-10-09, one `(agent, session type)` line each.
12. **Weekly logs:** [prototype/implementation-logs/](prototype/implementation-logs/README.md) holds one file per week with sessions, starting at vault creation in [2026-W36](prototype/implementation-logs/2026-W36.md). Weeks 37, 39, and 40 have no file because the founder was out working pilot van days and no session ran.
13. **Hand-over note:** [drafts/2026-10-09-resume-membership-tiers.md](drafts/2026-10-09-resume-membership-tiers.md) is what the last session left when it stopped mid-task.
14. **Decision owed, not yet written:** PDR-P005, a second-visit price for members, sits under Decisions Owed in the ledger after one round of review in chat. No file exists until the founder approves it.
15. **Unsourced claim backfilled:** [ADR-T001](decisions/technical/ADR-T001-online-booking-tool.md) once flagged "commuters prefer booking online" as `[unsourced]`; the pilot reweave replaced the flag with a link to the pilot results. The remaining `[unsourced]` claim in PDR-P003 is a Vault Maintenance task.
16. **Reusable prompt:** [prompts/customer-interview-synthesis.md](prompts/customer-interview-synthesis.md) turns conversation notes into a research draft with counts and no names.
