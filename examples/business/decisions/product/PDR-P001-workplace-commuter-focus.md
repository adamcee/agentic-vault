---
doctype: PDR
id: PDR-P001
domain: product
status: accepted
date: 2026-09-02
tags: [market, customers, workplace-stops]
constitution-clause: P3
supersedes: null
superseded-by: null
---
# PDR-P001: Target Daily Commuters at Their Workplace

## Context
One van can serve only a few riders a day, so the first customer group decides whether the business works. Local shops take two to seven days to return a bike in September, which leaves a daily commuter without transport ([[research/local-price-scan]] [emerging]).

## Decision
Curbside Cycles serves riders who commute by bike most days, and it serves them at their workplace during work hours. The van books a [[concepts/workplace-stop|workplace stop]] at one host site and works through several bikes in a row.

## Alternatives Considered
- **Home visits on evenings and weekends.** Riders like them, but one bike per stop means more driving and fewer jobs per [[concepts/van-day|van day]].
- **Recreational and road riders.** Their demand peaks on spring weekends, and owners of expensive bikes tend to stay loyal to one shop.
- **Fleet contracts with delivery or bike-share operators.** These pay steadily, but one van cannot meet a fleet's turnaround promises.

## Consequences
- Every stop needs a host contact and written permission ([[architecture/CONSTITUTION]] P3).
- Work happens on weekdays, which leaves weekends open for home visits at a higher price.
- Winter demand is untested and is the main risk to this choice.

> **Reweave 2026-09-14 (strengthened):** 31 of 41 survey respondents said they would use repair done at work ([[research/commuter-survey-2026-09]] [emerging]).
>
> **Reweave 2026-10-05 (strengthened):** 37 of 52 pilot visits took place at workplace stops. Workplace demand now appears in both the survey and the pilot ([[research/commuter-survey-2026-09]], [[research/pilot-month-results]] [supported]).
