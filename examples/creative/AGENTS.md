# AGENTS.md — Low Tide Master Context
*Single source of truth for every AI agent working in this vault. Load this file first in every session. Updated: 2026-10-09.*

`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and `.windsurfrules` are short pointers to this file. They hold only tool-specific notes. Project content goes here, never in a pointer file.

## Last Session Checkpoint

On 2026-10-09, the session generated an AI comparison of four unnamed games in the genre from the team's play notes and left it in [[drafts/genre-comparison]] awaiting tightening. It also added a tightening task to [[prototype/implementation-plan]].

Full log: [[session-history]].

---

## Session Start Protocol

Run these steps at the start of every session. Agents with skills can run them as the `vault-start` skill.

1. **Read this file in full**, then your tool's pointer file if it adds notes.
2. **Find what changed since the last session.** Take the date of the last `## YYYY-MM-DD` heading in [[session-history]], then list files changed since that date:
   - **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`
   - **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
   - **No shell:** ask the user what changed.
3. **Ask the session type**, such as planning, research, decision, script writing, building in Godot, or vault maintenance.
4. **Load the files listed for that type** under Task-Specific Context Loading.
5. **Confirm readiness** in a few sentences: what changed and what you loaded.

At the end of any session that changed the vault, run the Post-Task Completion Gate.

---

## Hard Constraints — Never Violate Without an ADR

- **`journal/` is human-only.** Never write to `journal/`. It is the owner's personal record.
- **Terse by default.** Vault documents follow the Writing Discipline section below. A document that fails the tightening checklist is not done.
- **Wikilink discipline.** When editing a vault document, link each reference to its canonical vault location with a `[[wikilink]]`.
- **Action items go to the ledger only.** Route new action items to `prototype/implementation-plan.md`, the production plan.
- **No orphan checkboxes.** Task checkboxes (`- [ ]`) appear only in the implementation plan and in protocol checklists, never as standalone lists elsewhere.
- **Drafts ingestion gate.** AI-generated content lands in `drafts/` first. Nothing moves from `drafts/` into the vault without passing the tightening checklist.
- **Append-only logs.** Add to `session-history.md` by appending. Never rewrite it.

- **Project invariants live in [[architecture/CONSTITUTION]].** In short: two-person scope (P1), no lost progress (P2), offline single-player (P3), Godot with GDScript only (S1), and everything in version control (S2).

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
6. ADRs and PDRs contain no implementation specs or multi-line code blocks.
7. Executive summaries run 12 lines or fewer.
8. No reified observations (abstract differences named, capitalized, or declared as principles).
9. No sentence fragments. Every sentence has a subject and a verb.
10. No more than one em-dash per paragraph.

---

## What Low Tide Is

Low Tide is a short narrative puzzle game for PC, about two to three hours long. Ines returns to her late father's tidal island to recover his lost logbook, and each puzzle must be solved during one [[concepts/tide-window]] before the sea returns.

Two people make it: Mara (writer-designer) and Teo (artist-programmer). The goal is a finished game for adults who play story-driven games in an evening or two ([[strategy/goals-and-audience]]).

---

## Current Phase

**Vertical slice, a six-week milestone that started on 2026-09-28.** The slice is the linear act 1 plus the first half of act 2, with final art for 6 backgrounds.

Done means at least 7 of 8 playtesters in round 3 finish the slice without outside help. Round 2 reached 6 of 8, and the open question is whether hints or a clearer tide-chart clue closes the gap ([[decisions/product/PDR-P003-no-hint-system|PDR-P003]]).

---

## Vault Structure

- **`architecture/`**: `CONSTITUTION.md` (hard constraints) and design docs.
- **`decisions/`**
  - `technical/`: ADRs for tools, stack, and system design.
  - `product/`: PDRs for product, business, and creative choices.
  - `rejected/`: decisions considered and declined.
  - `_BASES_SCHEMA.md`: frontmatter schema for decision records.
- **`strategy/`**: goals, audience, and positioning.
- **`concepts/`**: definitions of key terms. A concept note says *what something is*.
- **`ideas/`**: raw proposals awaiting evaluation. Each has a `resolved-by` field.
- **`research/`**: evidence, such as interviews, tests, market data, and source summaries.
- **`prototype/`**: `implementation-plan.md`, the production plan and the vault's ledger. The Godot project lives in its own repository.
- **`drafts/`**: staging area for AI-generated content.
- **`vault-guide/`**: how the vault works, plus style guides.
- **`journal/`**: human-only notes. Read-only for AI.
- **`session-history.md`**: one line per session, append-only.

---

## Tools & Stack

| Area | Tool |
|---|---|
| Engine and code | Godot 4, GDScript ([[decisions/technical/ADR-T001-godot-engine]]) |
| Background painting | Krita |
| Script and dialogue | Plain-text script files, imported into Godot |
| Scope and time tracking | A shared spreadsheet |
| Version control | Git with Git LFS for art |
| Playtests | Mara's notes and Teo's screen recordings |

**Common commands:** The team runs no regular shell commands, and builds run from the Godot editor.

---

## Agentic Boundaries

- **Always:** Apply the tightening checklist to any vault document you write or edit. Use `[[wikilinks]]`.
- **Ask first:** Adding a Godot plugin, changing a scene's palette, cutting or adding scenes, and spending money.
- **Never:** Commit secrets, write to `journal/`, or change a standing decision without a new decision record.

---

## Vault Access Tools

Use the best tool your environment offers:

1. **Filesystem tools** (read, grep, glob, edit): the default for CLI agents.
2. **Obsidian CLI**, if installed: `search`, `backlinks`, `orphans`, `unresolved`.
3. **Obsidian MCP** (desktop apps): read, search, create, append.
4. **Copy and paste** (web chat): the user pastes files in and copies your output back.

---

## Task-Specific Context Loading

- **Planning:** `prototype/implementation-plan.md`, relevant decisions.
- **Decision:** `decisions/` index and `architecture/CONSTITUTION.md`. Check for an existing or rejected decision before proposing a new one.
- **Research:** `research/` and the decisions it may affect.
- **Script writing:** [[decisions/product/PDR-P005-linear-story-local-choices|PDR-P005]], [[concepts/local-choice]], and the latest playtest notes.
- **Puzzle design:** [[decisions/product/PDR-P003-no-hint-system|PDR-P003]], [[concepts/tide-window]], and [[research/playtest-round-2]].
- **Strategy:** `strategy/` and relevant PDRs.
- **Vault maintenance:** `vault-guide/`.

---

## Standing Decisions (Do Not Relitigate Without a New Decision Record)

- **Engine:** Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-engine|ADR-T001]]).
- **Art style:** hand-painted 2D backgrounds with a 16-colour palette per scene ([[decisions/product/PDR-P002-hand-painted-limited-palette|PDR-P002]]).
- **Story:** linear, one ending, small local choices ([[decisions/product/PDR-P005-linear-story-local-choices|PDR-P005]]). It superseded the branching story in [[decisions/product/PDR-P001-branching-three-endings|PDR-P001]].
- **Hints:** none ([[decisions/product/PDR-P003-no-hint-system|PDR-P003]]). Weakened on 2026-10-05 and under review until playtest round 3.
- **Rejected:** online co-op ([[decisions/rejected/PDR-P004-online-co-op|PDR-P004]]).

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

**Trigger:** New information arrives (research, test results, competitor news, a change in direction).
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

Tags: `[established]`, `[supported]`, `[emerging]`, `[theoretical]`. Never write a research doc from memory; it must come from actual source material.
