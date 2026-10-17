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
10. **Pilot plan with reweave tasks:** [prototype/implementation-plan.md](prototype/implementation-plan.md) marks the tasks that research added.
11. **Session history:** [session-history.md](session-history.md) logs ten sessions from 2026-08-31 to 2026-10-09.
