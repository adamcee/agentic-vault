# AGENTS.md — Curbside Cycles Master Context
*Single source of truth for every AI agent working in this vault. Load this file first in every session. Updated: 2026-10-09.*

`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and `.windsurfrules` are short pointers to this file. They hold only tool-specific notes. Project content goes here, never in a pointer file.

## Last Session Checkpoint

On 2026-10-09, the session saved an AI-written memo on membership tiers to [[drafts/membership-tier-options]] for tightening, added launch tasks for [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]] to [[prototype/implementation-plan]], and opened [[ideas/apartment-building-weekend-stops]].

Full log: [[session-history]].

---

## Session Start Protocol

Run these steps at the start of every session. Agents with skills can run them as the `vault-start` skill.

1. **Read this file in full**, then your tool's pointer file if it adds notes.
2. **Find what changed since the last session.** Take the date of the last `## YYYY-MM-DD` heading in [[session-history]], then list files changed since that date:
   - **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`
   - **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
   - **No shell:** ask the user what changed.
3. **Ask the session type**, such as planning, research, pricing, decision, writing, or vault maintenance.
4. **Load the files listed for that type** under Task-Specific Context Loading.
5. **Confirm readiness** in a few sentences: what changed and what you loaded.

At the end of any session that changed the vault, run the Post-Task Completion Gate.

---

## Hard Constraints — Never Violate Without a Decision Record

- **`journal/` is human-only.** Never write to `journal/`. It is the owner's personal record.
- **Terse by default.** Vault documents follow the Writing Discipline section below. A document that fails the tightening checklist is not done.
- **Wikilink discipline.** When editing a vault document, link each reference to its canonical vault location with a `[[wikilink]]`.
- **Action items go to the ledger only.** Route new action items to `prototype/implementation-plan.md`.
- **No orphan checkboxes.** Task checkboxes (`- [ ]`) appear only in the implementation plan and in protocol checklists, never as standalone lists elsewhere.
- **Drafts ingestion gate.** AI-generated content lands in `drafts/` first. Nothing moves from `drafts/` into the vault without passing the tightening checklist.
- **Append-only logs.** Add to `session-history.md` by appending. Never rewrite it.
- **No customer personal data in the vault.** Research docs use counts, not names. Names, phone numbers, and card details stay in the booking tool.

Business invariants (one van, quote before work, host permission, labor floor) live in [[architecture/CONSTITUTION]].

---

## Session Interaction Style

Share useful advice, risks, and alternatives even when not asked, kept short and separate from the main task. Skip filler, apologies, and narration of tool use.

---

## Writing Discipline

Write for a reader with no context, following the four principles of ISO 24495-1 plain language: readers get what they need, find it easily, understand it, and can act on it. The full rules are in [[vault-guide/style-guides/ai-writing-discipline-core]].

**Tightening Checklist.** Every document an AI agent writes or substantially edits must pass this checklist before the task is complete.
1. The first sentence states the core claim (BLUF).
2. No paragraph exceeds 2 sentences (research exception: single-thought paragraphs permitted).
3. No narrative preamble before a self-explanatory table or list.
4. No stacked near-synonymous adjectives.
5. No meta-commentary in the body ("This section covers...").
6. ADRs and PDRs contain no step-by-step procedures or full price sheets.
7. Executive summaries run 12 lines or fewer.
8. No reified observations (abstract differences named, capitalized, or declared as principles).
9. No sentence fragments. Every sentence has a subject and a verb.
10. No more than one em-dash per paragraph.

---

## What Curbside Cycles Is

Curbside Cycles is a one-person mobile bike-repair van serving one mid-size city. The founder, a former bike-shop mechanic, brings the van to riders so they never lose their bike to a shop's multi-day queue.

The business targets daily bike commuters and serves them at their workplace during work hours ([[decisions/product/PDR-P001-workplace-commuter-focus|PDR-P001]]). The open question for 2026 is whether one van can pay the founder a full-time wage; the targets are in [[strategy/business-goals]].

---

## Current Phase

Phase 3 of [[prototype/implementation-plan]]: launch the monthly membership from [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]], running 2026-10-07 to 2026-11-15. The phase is done when the membership is on sale in the booking tool, offered to every pilot repeat customer and host workplace, and at least 15 riders have joined.

---

## Vault Structure

- **`architecture/`**: `CONSTITUTION.md` (business invariants).
- **`decisions/`**
  - `technical/`: ADRs for tools, equipment, and operations setup.
  - `product/`: PDRs for services, pricing, and market choices.
  - `rejected/`: decisions considered and declined.
  - `_BASES_SCHEMA.md`: frontmatter schema for decision records.
- **`strategy/`**: goals, audience, and what success looks like.
- **`concepts/`**: definitions of key terms. A concept note says *what something is*.
- **`ideas/`**: raw proposals awaiting evaluation. Each has a `resolved-by` field.
- **`research/`**: the founder's own evidence, such as the commuter survey, pilot results, and price scan.
- **`prototype/`**: `implementation-plan.md`, the pilot plan and task ledger.
- **`drafts/`**: staging area for AI-generated content.
- **`vault-guide/`**: how the vault works, plus style guides.
- **`journal/`**: human-only notes. Read-only for AI.
- **`session-history.md`**: one line per session, append-only.

---

## Tools & Stack

| Area | Tool |
|---|---|
| Booking | Hosted online booking tool with per-stop time slots ([[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]]) |
| Bookkeeping | Spreadsheet: visit log, parts, revenue, van costs |
| Payments | Card payment terminal paired with the founder's phone |
| Vehicle | Cargo van with workstand, bench, air compressor, and portable power station |
| Messaging | Phone and text, for day-before reminders and host contacts |

**Weekly routines:** Every Friday, export the week's bookings into the spreadsheet visit log and reconcile card-terminal payouts against it.

---

## Agentic Boundaries

- **Always:** Apply the tightening checklist to any vault document you write or edit. Use `[[wikilinks]]`.
- **Ask first:** Price changes, any spending, new tool subscriptions, and anything sent to a host workplace or landlord.
- **Never:** Put customer contact or payment details in the vault, write to `journal/`, or change a standing decision without a new decision record.

---

## Vault Access Tools

Use the best tool your environment offers:

1. **Filesystem tools** (read, grep, glob, edit): the default for CLI agents.
2. **Obsidian CLI**, if installed: `search`, `backlinks`, `orphans`, `unresolved`.
3. **Obsidian MCP** (desktop apps): read, search, create, append.
4. **Copy and paste** (web chat): the user pastes files in and copies your output back.

---

## Task-Specific Context Loading

- **Planning:** `prototype/implementation-plan.md`, [[strategy/business-goals]], and the decisions the task touches.
- **Pricing:** [[decisions/product/PDR-P004-membership-plus-per-visit]], [[research/local-price-scan]], [[research/pilot-month-results]], and Part I of [[architecture/CONSTITUTION]].
- **Decision:** `decisions/` index and `architecture/CONSTITUTION.md`. Check for an existing or rejected decision before proposing a new one.
- **Research:** `research/` and the decisions it may affect.
- **Strategy:** `strategy/` and relevant PDRs.
- **Vault maintenance:** `vault-guide/`.

---

## Standing Decisions (Do Not Relitigate Without a New Decision Record)

- **Customers are daily commuters, served at their workplace** in scheduled [[concepts/workplace-stop|workplace stops]]: [[decisions/product/PDR-P001-workplace-commuter-focus|PDR-P001]].
- **Pricing is a monthly membership plus per-visit prices for non-members:** [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]], which superseded per-visit-only pricing in [[decisions/product/PDR-P002-per-visit-pricing|PDR-P002]].
- **Bookings go through a hosted online booking tool,** not phone and spreadsheet: [[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]].
- **No storefront workshop lease** until the van is consistently full: [[decisions/rejected/PDR-P003-storefront-workshop-lease|PDR-P003]] (rejected).

---

## Decision Records

Check `decisions/technical/`, `decisions/product/`, and `decisions/rejected/` before proposing any change, and search frontmatter instead of reading every file (`grep -rl "status: accepted" decisions/`). The schema is in [[decisions/_BASES_SCHEMA]].

---

## Decision Propagation Protocol

**Trigger:** Any new decision (ADR, PDR, tool adoption, change in direction).
**Rule:** The task isn't complete until every item is done or marked N/A.

- [ ] Write the ADR or PDR in `decisions/technical/` or `decisions/product/`.
- [ ] Update `prototype/implementation-plan.md`.
- [ ] Update `architecture/CONSTITUTION.md` if the decision touches a hard constraint.
- [ ] Mark any superseded record `superseded-by` and link the new one.
- [ ] Update this file if the decision changes Standing Decisions, Vault Structure, or Task-Specific Context Loading.

---

## Reweave Protocol

**Trigger:** New information arrives (survey results, pilot numbers, a competitor change, a change in direction).
**Rule:** The task isn't complete until every item is done.

- [ ] **Find affected docs.** Ask of each decision, strategy, or design doc: *"If this were written today, would its conclusions change?"*
- [ ] **Classify the impact:** strengthened (add a link), weakened (add a note and flag for the human), or invalidated (flag for the human and propose a superseding record).
- [ ] **Add `## Reweave Triggers`** to the new document, listing affected files with `[[wikilinks]]` and one-line impacts. If nothing is affected, write `No existing docs affected.`
- [ ] **Route action items** to the implementation plan.

---

## Post-Task Completion Gate

Before marking any substantive task complete:

| Did the task… | Then… |
|---|---|
| Produce a new research doc? | Run the Reweave Protocol. |
| Make a decision? | Run the Decision Propagation Protocol. |
| Generate action items? | Route them to `prototype/implementation-plan.md`. |
| Write or edit any vault doc? | Run the tightening checklist. |
| Create or edit `[[wikilinks]]`? | Confirm every target exists. |
| Change the vault at all? | Append one line under today's `## YYYY-MM-DD` heading in [[session-history]] and update Last Session Checkpoint above. |

---

## Research Traceability

Every empirical claim in a decision, strategy, or design doc links to the vault research doc that supports it: `claim text ([[research/source-doc]] [maturity-tag])`. Flag unsupported claims `[unsourced]`.

Tags: `[established]`, `[supported]`, `[emerging]`, `[theoretical]`. Never write a research doc from memory; it must come from source material such as survey responses, the visit log, or call notes.
