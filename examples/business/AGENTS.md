# AGENTS.md — Curbside Cycles Master Context
*Single source of truth for every AI agent working in this vault. Load this file first in every session. Updated: 2026-10-09.*

`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and `.windsurfrules` are short pointers to this file that hold only tool-specific notes. Project content goes here, never in a pointer file.

Each protocol below is a short checklist. Its canonical page in `vault-guide/` holds the full rules; if the two differ, the page wins and this file gets corrected.

## Last Session Checkpoint

On 2026-10-09, the session saved an AI-written memo on membership tiers to [[drafts/membership-tier-options]] for tightening, added launch tasks for [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]] to [[prototype/implementation-plan]], and opened [[ideas/apartment-building-weekend-stops]]. It stopped mid-review of a second-visit price for members and left [[drafts/2026-10-09-resume-membership-tiers]] for the next session.

Full log: [[session-history]].

---

## Session Start Protocol

Run these steps at the start of every session, and again if you realize mid-session that you skipped them. Agents with skills run them as the `vault-start` skill; every step is a tool call, not a memory of a past session.

1. **Read this file in full**, then your tool's pointer file if it adds notes.
2. **Find what changed since the last session.** Take the date of the last `## YYYY-MM-DD` heading in [[session-history]] (`grep '^## ' session-history.md | tail -1`), then list files changed since that date:
   - **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`. The `00:00` makes the cutoff the start of that day, so the last session's own changes show up.
   - **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
   - **No shell:** search for the date prefix over MCP, or ask the user what changed.
   - Flag root-level files, new decision records, and new files in `drafts/`.
3. **Ask the session type**, such as pricing, pilot, research, planning, decision, writing, or vault maintenance.
4. **Load the files listed for that type** under Task-Specific Context Loading.
5. **Confirm readiness** in a few sentences: what changed, what you loaded, and anything odd about the vault's state.

At the end of any session that changed the vault, run the Post-Task Completion Gate.

---

## Hard Constraints — Never Violate Without a Decision Record

- **`journal/` is human-only.** Never write to `journal/`. It is the owner's personal record.
- **Terse by default.** Vault documents follow the Writing Discipline section below. A document that fails the tightening checklist is not done.
- **Wikilink discipline.** When editing a vault document, link each reference to its canonical vault location with a `[[wikilink]]` ([[vault-guide/wikilink-discipline]]).
- **The ledger is the AI's; the task list is the human's.** AI sessions route new action items to `prototype/implementation-plan.md`. The founder curates `prototype/human-task-list.md`; AI never writes to it.
- **No orphan checkboxes.** Task checkboxes (`- [ ]`) appear only in the two task files and in protocol checklists, never as standalone lists elsewhere.
- **Decisions are reviewed before they are written.** Draft an ADR or PDR in chat, expect two to four rounds, and write the file only after the founder approves ([[vault-guide/decision-propagation-protocol]]).
- **Drafts ingestion gate.** AI-generated content lands in `drafts/` first and moves into the vault only after passing the promotion checklist ([[vault-guide/ingestion-gate]]).
- **No cruft.** When admitting AI content, fix or remove what's wrong instead of flagging it. Keep the untouched original as `_source-<name>.md` beside the clean doc.
- **Append-only logs.** Add to `session-history.md` and the weekly log by appending, never by rewriting ([[vault-guide/session-logs]]).
- **Stay in phase.** Don't start work outside the current phase.
- **No customer personal data in the vault.** Research docs use counts, not names. Names, phone numbers, and card details stay in the booking tool.

Business invariants (one van, quote before work, host permission, labor floor) live in [[architecture/CONSTITUTION]].

---

## Session Interaction Style

- **Suggest freely.** Share useful advice, risks, and alternatives even when not asked, kept short and separate from the main task. Skip filler, apologies, and narration of tool use.
- **Research may widen; decisions wait.** When one source leads to another, follow it. Capture framing in concept notes and drafts, and send decision candidates to the ledger instead of drafting them mid-research.

---

## Writing Discipline

Write for the human owner first and the next AI session second, following the four principles of ISO 24495-1 plain language: readers get what they need, find it easily, understand it, and can act on it. The full rules are in [[vault-guide/style-guides/ai-writing-discipline-core]]; research docs follow [[vault-guide/style-guides/research-paper-discipline]].

**Tightening Checklist.** Every document an AI agent writes or substantially edits must pass this checklist before the task is complete.
1. The first sentence states the core claim (BLUF).
2. No paragraph exceeds 2 sentences (research docs may use single-thought paragraphs).
3. No narrative preamble before a self-explanatory table or list.
4. No stacked near-synonymous adjectives.
5. No meta-commentary in the body ("This section covers...").
6. ADRs and PDRs contain no step-by-step procedures, full price sheets, or multi-line code blocks.
7. Biographies run 2 lines or fewer; executive summaries 12 lines or fewer.
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

Every top-level folder has a `README.md` listing its files. Folders named `archive/` hold retired docs and are exempt from tightening and scans.

- **`architecture/`**: `CONSTITUTION.md` (business invariants).
- **`decisions/`**
  - `technical/`: ADRs for tools, equipment, and operations setup.
  - `product/`: PDRs for services, pricing, and market choices.
  - `rejected/`: decisions considered and declined. Never revive one without a new record.
  - `_BASES_SCHEMA.md`: frontmatter schema, status meanings, tags, and search recipes.
- **`strategy/`**: goals, audience, and what success looks like.
- **`concepts/`**: definitions of key terms. A concept note says *what something is*.
- **`ideas/`**: raw proposals awaiting evaluation. Each has a `resolved-by` field.
- **`research/`**: the founder's own evidence, such as the commuter survey, pilot results, and price scan.
- **`prototype/`**
  - `implementation-plan.md`: the AI ledger and the phase plan.
  - `human-task-list.md`: the founder's working list. AI never writes here.
  - `implementation-logs/`: weekly append-only logs (`YYYY-Www.md`).
- **`drafts/`**: staging area for AI-generated content and hand-over notes (`YYYY-MM-DD-resume-<topic>.md`).
- **`prompts/`**: reusable prompts, such as the customer-interview synthesis prompt.
- **`vault-guide/`**: canonical protocol pages and style guides.
- **`journal/`**: human-only notes. Read-only for AI.
- **`session-history.md`**: one line per session, append-only.
- **`.link-check-ignore`**: intentional links to notes that don't exist yet.

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

**Vault scripts** (Python 3, in `.claude/skills/`; each page in `vault-guide/` gives a manual fallback):
- `vault-links/vault-link-check.py`: finds broken wikilinks.
- `vault-maintenance/vault-lint.py`: checks session logs and file size at session close.
- `vault-maintenance/vault-review-scan.py`: flags writing-discipline and reweave gaps.

---

## Agentic Boundaries

- **Always:** Apply the tightening checklist to any vault document you write or edit. Use `[[wikilinks]]`.
- **Ask first:** Price changes, any spending, new tool subscriptions, and anything sent to a host workplace or landlord.
- **Never:** Put customer contact or payment details in the vault, write to `journal/` or `human-task-list.md`, write a decision record before the founder approves it, or change a standing decision without a new record.

---

## Vault Access Tools

Use the best tool your environment offers:

1. **Filesystem tools** (read, grep, glob, edit): the default for CLI agents.
2. **Obsidian CLI**, if installed: `search`, `backlinks`, `orphans`, `unresolved`, `move`.
3. **Obsidian MCP** (desktop apps): read, search, create, append, move.
4. **Copy and paste** (web chat): the user pastes files in and copies your output back.

Move or rename notes with a tool that rewrites links (Obsidian `move` or MCP move). Plain `mv` leaves every link pointing at the old path.

---

## Task-Specific Context Loading

- **Planning:** `prototype/implementation-plan.md`, [[strategy/business-goals]], and the decisions the task touches.
- **Pricing:** [[decisions/product/PDR-P004-membership-plus-per-visit]], [[research/local-price-scan]], [[research/pilot-month-results]], and Part I of [[architecture/CONSTITUTION]].
- **Pilot:** [[research/pilot-month-results]], [[concepts/van-day]], [[concepts/workplace-stop]], and the current phase in `prototype/implementation-plan.md`.
- **Decision:** `decisions/` index and `architecture/CONSTITUTION.md`. Check for an existing or rejected decision before proposing a new one.
- **Research:** `research/`, the decisions it may affect, and [[vault-guide/research-paper-workflow]]. Interview notes go through [[prompts/customer-interview-synthesis]].
- **Strategy:** `strategy/` and relevant PDRs.
- **Vault maintenance:** [[vault-guide/vault-design-philosophy]], the style guide, the relevant `vault-guide/` page, and the README of any folder you change.
- **Anything else:** [[vault-guide/vault-design-philosophy]] and the README of the most relevant folder.

---

## Standing Decisions (Do Not Relitigate Without a New Decision Record)

- **Customers are daily commuters, served at their workplace** in scheduled [[concepts/workplace-stop|workplace stops]]: [[decisions/product/PDR-P001-workplace-commuter-focus|PDR-P001]].
- **Pricing is a monthly membership plus per-visit prices for non-members:** [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]], which superseded per-visit-only pricing in [[decisions/product/PDR-P002-per-visit-pricing|PDR-P002]].
- **Bookings go through a hosted online booking tool,** not phone and spreadsheet: [[decisions/technical/ADR-T001-online-booking-tool|ADR-T001]].

**Rejected, do not revive without a new record:**
- **A storefront workshop lease** before the van is consistently full: [[decisions/rejected/PDR-P003-storefront-workshop-lease|PDR-P003]].

---

## Decision Records

Check `decisions/technical/`, `decisions/product/`, and `decisions/rejected/` before proposing any change, and search frontmatter instead of reading every file (`grep -rl "status: rejected" decisions/`). The schema and status meanings are in [[decisions/_BASES_SCHEMA]].

---

## Decision Propagation Protocol

**Trigger:** Any new decision (ADR, PDR, tool adoption, change in direction). Canonical page: [[vault-guide/decision-propagation-protocol]].
**Rule:** The task isn't complete until every item is done or marked N/A.

- [ ] List three alternatives with one-line tradeoffs, draft the record in chat, and write it only after the founder approves.
- [ ] Update `prototype/implementation-plan.md`.
- [ ] Update `architecture/CONSTITUTION.md` if the decision touches a hard constraint.
- [ ] Mark any superseded record `superseded-by` and link the new one. An amended record stays `accepted`.
- [ ] Update this file if the decision changes Standing Decisions, Vault Structure, or Task-Specific Context Loading.
- [ ] Log the decision in this week's implementation log.

---

## Reweave Protocol

**Trigger:** New information arrives (survey results, pilot numbers, a competitor change, a change in direction). Canonical page: [[vault-guide/reweave-protocol]].
**Rule:** The task isn't complete until every item is done.

- [ ] **Find affected docs.** Ask of each decision, strategy, or design doc: *"If this were written today, would its conclusions change?"*
- [ ] **Classify the impact:** strengthened (add a link), weakened (write a dated note into the affected doc and flag the founder), or invalidated (never change it silently; flag the founder and propose a superseding record).
- [ ] **Add `## Reweave Triggers`** to the new document, listing affected files with `[[wikilinks]]` and one-line impacts. If nothing is affected, write `No existing docs affected.`
- [ ] **Backfill on touch.** A research doc you read in full or edit that lacks `## Reweave Triggers` gets one before the task closes.
- [ ] **Route action items** to the implementation plan and log the reweave in this week's implementation log.

---

## Post-Task Completion Gate

Before marking any substantive task complete:

| Did the task… | Then… |
|---|---|
| Produce a new research doc? | Run the Reweave Protocol. |
| Read a primary source? | Make sure the source has its own doc in `research/`, not only an interpretation. |
| Touch a research doc with no `## Reweave Triggers`? | Add the section (backfill on touch). |
| Touch a decision record? | Add citation links for any claims you can verify. |
| Make a decision? | Run the Decision Propagation Protocol. |
| Generate action items? | Route them to `prototype/implementation-plan.md`, never `human-task-list.md`. |
| Change Hard Constraints, Standing Decisions, or Vault Structure? | Update this file. |
| Write or edit any vault doc? | Run the tightening checklist. |
| Create or edit `[[wikilinks]]`? | Run `vault-link-check.py` on the affected files. Fix each broken target, link the nearest real note, or add an intended forward link to `.link-check-ignore`. |
| Add a script or config to a skill folder? | Document it in that skill's `SKILL.md`. |
| Change the vault at all? | Append a section to this week's `prototype/implementation-logs/YYYY-Www.md` and one line under today's `## YYYY-MM-DD` heading in [[session-history]], each with a single append. Update Last Session Checkpoint above, then run `vault-lint.py`. |

If no row applies, no integration pass is needed.

---

## Research Traceability

Every empirical claim in a decision, strategy, or design doc links to the vault research doc that supports it: `claim text ([[research/source-doc]] [maturity-tag])`. Canonical page: [[vault-guide/research-traceability]].

- **Unsourced claims** are flagged `[unsourced]`. Never write a research doc from memory; it must come from source material such as survey responses, the visit log, or call notes.
- **Findings vs. inferences:** a finding gets a plain link; an inference says so.
- **Primary over secondary:** link the primary source's doc when it exists; mark secondary-only citations.
- **Maturity tags:** `[established]`, `[supported]`, `[emerging]`, `[theoretical]`, also in the research doc's frontmatter as `evidence-maturity`. AI syntheses are tagged `secondary`.

---

## Vault Maintenance

- **Plan triage** when the ledger passes about 200 open items, after a major change in direction, or quarterly ([[vault-guide/implementation-plan-triage]]).
- **Vault review** quarterly or after a long gap ([[vault-guide/vault-review-protocol]]). Findings go to the ledger, never to a standalone report.

---

## Operational Gotchas

- **Auto-commit hides edits from `git status`.** If the Git plugin commits on a schedule, confirm an edit landed with `git log --oneline -3`.
- **Stray daily notes.** Obsidian sometimes creates `YYYY-MM-DD.md` at the vault root. Empty ones can be deleted; never touch `journal/`.
- **Broken links stay at zero.** Once `vault-link-check.py` reports zero, any new result is a regression to fix in the same session.
- **Large MCP writes can hang.** Write a short stub, then append in chunks of about 10KB.
- **Search lags new files.** Read files created this session by path instead of searching for them.
- **Truncated reads.** Some tools cut off long files. Never build an edit from text you didn't see in full, and keep this file under about 40KB.
- **Skills live outside Obsidian.** `.claude/skills/` isn't indexed by Obsidian, so scripts run only from a terminal-capable agent.

---

## Session History

The full history is in [[session-history]], one line per session under its date, and weekly detail is in `prototype/implementation-logs/`. Both are append-only, so never add session entries to this file.
