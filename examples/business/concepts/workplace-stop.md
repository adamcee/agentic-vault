---
id: workplace-stop
date: 2026-09-02
status: active
tags: [concept, operations]
---
# Workplace Stop

A workplace stop is a booked block of time when the van parks at one host workplace and services several riders' bikes in a row. It is the core unit of service under [[decisions/product/PDR-P001-workplace-commuter-focus|PDR-P001]].

- **Host.** A named contact at the site gives written permission for the van to park and work ([[architecture/CONSTITUTION]] P3).
- **Slots.** Riders at that site claim 40-minute slots in the booking tool ([[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]).
- **Day-before text.** Each booked rider gets a text the day before asking what is wrong with the bike, so the founder loads the right parts.
- **Handover.** Riders leave the bike at the van and collect it before going home.

A stop with fewer than three booked slots by noon the day before is moved or merged with another stop.
