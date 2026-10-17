---
doctype: PDR
id: PDR-P002
domain: product
status: accepted
date: 2026-09-10
tags: [shift-swaps, approvals, reweave-weakened]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P002: Every Shift Swap Needs Manager Approval

> **Weakened 2026-10-06.** In the first two pilot weeks, managers approved 57 of 59 swap requests with a median wait of 7 minutes, and both denials were cross-role swaps ([[research/pilot-usage-weeks-1-2]] [emerging]). The data points toward auto-approving same-role swaps that add no overtime. Flagged for human review; follow-up tasks are in Phase 2 of [[prototype/implementation-plan]], and the proposal is [[ideas/auto-approve-same-role-swaps]].

## Context
Staff trade shifts every week, today mostly through group texts. Eight of nine interviewed managers said they want to approve every swap, because an unchecked swap can put an untrained person on a station or push someone into overtime ([[research/manager-interview-synthesis]] [supported]).

## Decision
Every [[concepts/shift-swap]] needs a manager's approval before it changes the schedule. Both staff members get an SMS when the manager decides.

## Alternatives Considered
- **Auto-approve every swap.** Staff wait less, but managers in both interview rounds refused it.
- **Auto-approve same-role swaps that add no overtime.** Deferred until real swap data exists.
- **No tracking, as with group texts.** Staff keep full freedom, but the schedule stops matching who shows up.

## Consequences
- Each swap waits for a manager, which slows swaps when the manager is off shift.
- Every swap decision lands in the audit log required by clause S2 of [[architecture/CONSTITUTION]].
- The overtime check depends on the manager's judgment, not on Brigade.
