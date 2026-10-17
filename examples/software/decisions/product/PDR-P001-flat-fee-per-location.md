---
doctype: PDR
id: PDR-P001
domain: product
status: accepted
date: 2026-08-31
tags: [pricing, billing]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P001: Flat Monthly Fee per Location, Unlimited Staff

> **Strengthened 2026-09-10 and 2026-09-17.** Reweaves added the interview and competitor evidence cited in Context.

## Context
Small restaurants hire seasonally and lose staff often. Six of nine interviewed managers named per-seat billing as a reason they left or avoided a scheduling app ([[research/manager-interview-synthesis]] [supported]).

Four of the five generic scheduling apps the co-founder trialed charge per active employee ([[research/competitor-feature-scan]] [emerging]). Flat pricing is a difference an owner sees on the first page.

## Decision
Charge $49 per month for each [[concepts/location]], with unlimited staff accounts. The pilot is free.

## Alternatives Considered
- **Per seat, about $3 per employee per month.** Revenue grows with larger restaurants, but owners hesitate to add part-timers, who then miss shift alerts.
- **Tiers by staff count.** Bills are predictable, but owners near a tier edge hesitate to add staff in the same way.
- **Free app with paid SMS.** Owners pay only for what they use, but revenue is too small to fund development.

## Consequences
- A 60-person location pays the same as a 15-person one, so SMS cost per location must stay well under the fee.
- We assume owners will pay $49 per location without a sales call [unsourced]. The free pilot cannot test this, so a pricing test is a Phase 3 task in [[prototype/implementation-plan]].
- Billing counts locations, so the definition in [[concepts/location]] is binding.
