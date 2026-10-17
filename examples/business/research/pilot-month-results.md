---
id: pilot-month-results
date: 2026-10-05
status: active
tags: [pilot, pricing, demand, primary-research]
evidence-maturity: emerging
sample: 52 visits, 38 customers, 4 host workplaces
---
# Pilot Month Results, 2026-09-07 to 2026-10-04

Repeat customers rebooked every three to four weeks and compared each visit's price with shop prices, while host workplaces asked for a monthly plan. The data comes from the spreadsheet visit log and the booking tool for one four-week pilot, so the findings are `[emerging]`.

## Volume and Revenue
| Measure | Result |
|---|---|
| [[concepts/van-day|Van days]] worked | 15 of 16 planned (one lost to rain) |
| Host workplaces | 4 |
| Visits | 52, of which 37 at [[concepts/workplace-stop|workplace stops]] |
| Customers | 38 |
| Visits per van day | 3.5, against a capacity of 6 |
| Revenue, including parts | $3,640, or $243 per van day |
| Booked through the online tool | 44 of 52 |

## Findings
- **Repeat riders book monthly.** Of the 23 customers whose first visit fell in the first ten days, 14 booked again. The gaps ran from 20 to 27 days, with a median of 24.
- **Riders price-shop each visit.** On 11 of 52 visits the rider compared the price with a shop's, and 7 of those 11 were second visits. Four repeat riders asked whether regulars got a lower rate.
- **Hosts want a monthly plan.** Three of four host contacts asked for one without being prompted. One asked whether the employer could pay for staff memberships as a perk.
- **One-off jobs still matter.** The 15 visits away from workplace stops were home visits and one-time repairs, and none of those riders rebooked.
- **The van ran under capacity.** At 3.5 visits per van day, the pilot used 58% of capacity, well short of the 80% test in [[architecture/CONSTITUTION]] P1.

## Limits
Four weeks shows only one rebooking cycle, so the 24-day interval needs a second month to confirm. September weather was mild, and October may be slower.

## Reweave Triggers
- [[decisions/product/PDR-P002-per-visit-pricing|PDR-P002]]: weakened. Monthly rebooking, price-shopping, and host requests all point to a membership. Flagged for the founder with a superseding PDR proposed.
- [[decisions/product/PDR-P001-workplace-commuter-focus|PDR-P001]]: strengthened. 37 of 52 visits were at workplace stops, which agrees with the survey.
- [[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]: strengthened. 44 of 52 visits were booked online.
- [[strategy/business-goals]]: weakened. Revenue per van day ran at $243 against a $350 target.
- [[ideas/monthly-membership]]: ready for a decision.
- [[prototype/implementation-plan]]: added membership tasks and a second-month interval check.
