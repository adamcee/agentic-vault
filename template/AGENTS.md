# AGENTS.md — [Project Name] Master Context
*Single source of truth for every AI agent working in this vault. Load this file first in every session. Updated: [YYYY-MM-DD].*

`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and `.windsurfrules` are short pointers to this file. They hold only tool-specific notes. Project content goes here, never in a pointer file.

## Last Session Checkpoint

On [YYYY-MM-DD], [one or two sentences: what the last session did and which files it changed].

Full log: [[session-history]].

---

## Session Start Protocol

Run these steps at the start of every session. Agents with skills can run them as the `vault-start` skill.

1. **Read this file in full**, then your tool's pointer file if it adds notes.
2. **Find what changed since the last session.** Take the date of the last `## YYYY-MM-DD` heading in [[session-history]], then list files changed since that date:
   - **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`
   - **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
   - **No shell:** ask the user what changed.
3. **Ask the session type**, such as planning, research, decision, writing, coding, or vault maintenance.
4. **Load the files listed for that type** under Task-Specific Context Loading.
5. **Confirm readiness** in a few sentences: what changed and what you loaded.

At the end of any session that changed the vault, run the Post-Task Completion Gate.

---

## Hard Constraints — Never Violate Without an ADR

- **`journal/` is human-only.** Never write to `journal/`. It is the owner's personal record.
- **Terse by default.** Vault documents follow the Writing Discipline section below. A document that fails the tightening checklist is not done.
- **Wikilink discipline.** When editing a vault document, link each reference to its canonical vault location with a `[[wikilink]]`.
- **Action items go to the ledger only.** Route new action items to `prototype/implementation-plan.md`.
- **No orphan checkboxes.** Task checkboxes (`- [ ]`) appear only in the implementation plan and in protocol checklists, never as standalone lists elsewhere.
- **Drafts ingestion gate.** AI-generated content lands in `drafts/` first. Nothing moves from `drafts/` into the vault without passing the tightening checklist.
- **Append-only logs.** Add to `session-history.md` by appending. Never rewrite it.

[Add your project's hard constraints here, or keep them in `architecture/CONSTITUTION.md`.]

---

## Session Interaction Style

Share useful advice, risks, and alternatives even when not asked, kept short and separate from the main task. Skip filler, apologies, and narration of tool use.

---

## Writing Discipline

Write for the human owner first and the next AI session second, following the four principles of ISO 24495-1 plain language: readers get what they need, find it easily, understand it, and can act on it. The full rules are in [[vault-guide/style-guides/ai-writing-discipline-core]].

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

## What [Project Name] Is

[One or two paragraphs: what the project is, who it's for, and what it's trying to achieve.]

---

## Current Phase

[The current two-to-six-week milestone: what you're working on and what "done" looks like.]

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
- **`prototype/`** (or `src/`): `implementation-plan.md` (the ledger), specs, and work in progress.
- **`drafts/`**: staging area for AI-generated content.
- **`vault-guide/`**: how the vault works, plus style guides.
- **`journal/`**: human-only notes. Read-only for AI.
- **`session-history.md`**: one line per session, append-only.

---

## Tools & Stack

[List the tools this project uses: software stack, design tools, spreadsheets, or whatever applies.]

| Area | Tool |
|---|---|
| [e.g., Frontend] | [e.g., React] |
| [e.g., Data] | [e.g., PostgreSQL] |

**Common commands:** [Shell commands you run often, if any.]

---

## Agentic Boundaries

- **Always:** Apply the tightening checklist to any vault document you write or edit. Use `[[wikilinks]]`.
- **Ask first:** [Changes that need a human yes, e.g., new dependencies, schema changes, spending money.]
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

[Customize for your project.]
- **Planning:** `prototype/implementation-plan.md`, relevant decisions.
- **Decision:** `decisions/` index and `architecture/CONSTITUTION.md`. Check for an existing or rejected decision before proposing a new one.
- **Research:** `research/` and the decisions it may affect.
- **Strategy:** `strategy/` and relevant PDRs.
- **Vault maintenance:** `vault-guide/`.

---

## Standing Decisions (Do Not Relitigate Without a New Decision Record)

[Bullet list of locked decisions, each linked to its ADR or PDR.]

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
