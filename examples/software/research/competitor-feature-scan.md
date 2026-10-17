---
id: competitor-feature-scan
date: 2026-09-17
status: Active
tags: [research, competitors, pricing, ingestion-gate]
evidence-maturity: emerging
source: Co-founder's trial notes on five generic scheduling apps, 2026-09-11 to 2026-09-15
---
# Competitor Feature Scan

All five generic scheduling apps the co-founder trialed are built phone-first for managers, and four charge per active employee. None let her build a test week as fast as her own spreadsheet.

## Method
The co-founder ran free trials of five generic shift-scheduling apps, labeled App 1 to App 5, and built the same 18-person test week in each. An AI session wrote a report from her notes on 2026-09-16, and it passed the ingestion gate on 2026-09-17 after checking against those notes.

The untouched original is [[research/_source-competitor-feature-scan]]. The gate removed two claims the notes do not support: a figure for how often restaurants switch apps, and a label calling App 3 the market leader.

## Findings

| Feature | App 1 | App 2 | App 3 | App 4 | App 5 |
|---|---|---|---|---|---|
| Pricing basis | Per employee | Per employee | Per employee | Location tiers | Per employee |
| Desktop scheduling grid | Limited | None | Full | Limited | None |
| Minutes to build the test week | 52 | 70 | 38 | 61 | 66 |
| Staff must install an app | Yes | Yes | No | Yes | Yes |
| Swap approval | Manager | Manager | Manager, optional auto-approve for same role | Manager | Manager |
| Payroll or tip features bundled | Yes | No | Yes | Yes | No |

Her spreadsheet baseline for the same week was 25 minutes.

## Interpretations
- We read the build times to mean a fast desktop grid is the clearest product gap, since even the best app took half again as long as a spreadsheet.
- Bundled payroll and tip features make three apps heavier to set up, and Brigade's constitution keeps it out of pay entirely.

## Reweave Triggers
- [[decisions/technical/ADR-T002-responsive-web-pwa]]: **strengthened**. Four of five apps make staff install an app, which interviewed managers said staff resist.
- [[decisions/product/PDR-P001-flat-fee-per-location]]: **strengthened**. Four of five apps charge per employee, so flat pricing per location stands out.
- [[decisions/product/PDR-P002-manager-approval-for-swaps]]: no change. App 3's optional same-role auto-approval is worth revisiting if pilot data questions approval.
- [[ideas/tip-pooling-calculator]]: informs review. Three apps bundle pay features, which conflicts with clause P3 of [[architecture/CONSTITUTION]].
