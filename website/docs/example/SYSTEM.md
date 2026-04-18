# [[SYSTEM]].md — BrewTrack Master Context
*Load this file first in every AI session. Updated: 2026-04-17*

## 🔖 Last session checkpoint
On 2026-04-17, decided to move forward with React Native for the mobile app (ADR-T001) and established the gamified points system (PDR-P001).

*See `journal/` for daily notes or `prototype/implementation-logs/` for full session histories.*

---

## How This File Gets Loaded

- **Claude Code:** reads via `CLAUDE.md` pointer
- **Gemini CLI:** reads via `GEMINI.md` pointer
- **Cursor / Windsurf:** reads via `.cursorrules` / `.windsurfrules` pointers
- **Claude Desktop / Cowork:** reads via Obsidian MCP

Regardless of access method: read this file before any substantive session. Do not rely on the project prompt or memory for details — the vault is the source of truth.

### ✅ Session-Start: Find New / Modified Docs
At the start of any session, check for files modified since the last session date:
- **MCP:** `obsidian_global_search(query=".", useRegex=true, modified_since="2026-04-17")`
- **CLI:** `git log -1 --before="2026-04-17" --format=%H` then `git diff`

---

## ⚠️ Hard Constraints — Never Violate Without an ADR

- **journal/ is human-only** — never write to `journal/` for any reason. Human owner's personal daily record. Read-only for AI.
- **Terse by default** — vault documents follow the Paragraph Ban, BLUF discipline, and the 7-point tightening checklist (see Writing Discipline section). 
- **Wikilink discipline** — when editing any vault document, use `[[wikilinks]]` to connect references to their canonical vault location. Every claim that rests on a research doc, ADR, or strategy section should link to it.
- **Action items route to the vault ledger only.** AI sessions route new action items to `prototype/implementation-plan.md` (or equivalent task tracker). 
- **No orphan checkboxes.** `- [ ]` task checkboxes for tracking completion appear only in canonical task lists, never scattered across standard documents.
- **Drafts ingestion gate.** All AI-generated content lands in `drafts/` first — never directly into the vault. No document moves from `drafts/` into the vault without passing the tightening checklist.

---

## Session Interaction Style

**Proactive suggestions encouraged.** During conversations, proactively share advice, ideas, design patterns, or potential pitfalls. Keep suggestions concise and clearly separated from the main task. Focus on technical rationale. Avoid conversational filler, apologies, and mechanical tool-use narration (e.g., "I will now call...").

---

## Writing Discipline & Multi-Agent Interoperability

All vault documents are treated as high-leverage state machines for multi-agent LLM parsing. 

**Tightening Checklist:** Every document written or substantially edited by an AI agent must pass this checklist before the task is marked complete:
1. First sentence is BLUF (Bottom Line Up Front — core claim).
2. No paragraph exceeds 2 sentences (research exception: single-thought paragraphs permitted).
3. No narrative preamble before a self-explanatory table or list.
4. No stacked near-synonymous adjectives.
5. No meta-commentary in document body ("This section covers...").
6. ADRs/PDRs contain no implementation specs or multi-line code blocks.
7. Executive summaries ≤ 12 lines.
8. No reified observations (abstract differences named, capitalized, or declared as principles).
9. No sentence fragments. Every sentence has a subject and a verb.
10. No em-dash clusters (max one per paragraph).

---

## What BrewTrack Is

BrewTrack is a mobile loyalty application designed for independent local coffee shops. It allows small cafes to compete with massive corporate rewards programs (like Starbucks) by offering a white-labeled, beautifully designed digital punch card. 

The primary domain focuses on low-friction transactions at the point of sale (QR code scanning) and gamified retention mechanics that encourage repeat business.

---

## Current Phase

**Phase 1: Proof of Concept App**
Building the initial React Native mobile app and the Python/FastAPI backend. Focusing entirely on the QR code generation and the basic points tallying for a single cafe.

---

## Vault Topology & Stack Reference

See **`AGENTS.md`** for the directory structure, stack reference, and agentic boundaries.

---

## Task-Specific Context Loading

- **Coding session:** Load `AGENTS.md`, `architecture/CONSTITUTION.md`, active spec from `prototype/specs/`, relevant ADRs.
- **Architecture decision:** Load `decisions/technical/` index, `architecture/CONSTITUTION.md`.
- **Strategy/Research:** Load `strategy/`, `research/` folders as relevant.
- **Vault maintenance:** Load `vault-guide/` files.

---

## Standing Decisions (Do Not Relitigate Without New ADR)

- **Mobile Framework:** React Native (Expo) - Selected for rapid cross-platform deployment.
- **Backend Framework:** Python (FastAPI) - Selected for development speed and typing support.
- **Database:** PostgreSQL - Handled via async SQLAlchemy.
- **No hardware integration:** We do not integrate with POS systems directly; the barista scans the customer's phone camera.

---

## Key Architectural Concepts

See `concepts/` for full atomic definitions. 

---

## Decision Records Index

All major decisions have ADRs or PDRs. Before proposing any architectural or product change, check:
- `/decisions/technical/` for stack/architecture decisions
- `/decisions/product/` for product/pedagogical decisions

**How to search decisions:** Query the `status` or `tags` in YAML frontmatter rather than reading all files. (e.g., `obsidian search query="[status: accepted]" path="decisions/"`).

---

## Decision Propagation Protocol

**Trigger:** Any new decision (ADR, PDR, tool adoption, architectural change).
**Rule:** Do not mark the task complete until every checkbox below is done or marked N/A.

- [ ] Write the ADR/PDR in `decisions/technical/` or `decisions/product/`
- [ ] Update `prototype/implementation-plan.md` 
- [ ] Append session log entry
- [ ] Update `architecture/CONSTITUTION.md` (if it touches invariants)
- [ ] Check companion docs for consistency
- [ ] Update `SYSTEM.md` (only if it changes Standing Decisions or Context Loading)

---

## Reweave Protocol

**Trigger:** New information arrives (research doc, competitive intel, strategy shift).
**Rule:** Do not mark the task complete until every checkbox below is done.

- [ ] **Identify affected docs.** Search the vault for existing ADRs, strategy, or architecture docs the new info touches.
- [ ] **Classify impact:** *Strengthened* (add link), *Weakened* (add note), or *Invalidated* (flag for human, propose new ADR).
- [ ] **Add `## Reweave Triggers`** to the new document listing affected vault files with `[[wikilinks]]`.
- [ ] **Route action items to plans.** 

---

## Post-Task Completion Gate

**Before marking any substantive task complete, run this checklist.** 

| Did the task… | Then you must… |
|---|---|
| Produce a new research doc? | Run the Reweave Protocol. |
| Make a decision (ADR/PDR)? | Run the Decision Propagation Protocol. |
| Generate action items? | Route to `implementation-plan.md`. |
| Write or edit any vault doc? | Run the 10-point tightening checklist. |
| Create or edit `[[wikilinks]]`? | Verify all targets resolve. |

---

## Research Traceability

Every empirical claim in an ADR, strategy doc, or architecture doc should be traceable to a specific research document in the vault. 
Format: `claim text ([[research/source-doc-name]] [maturity-tag])`

Tags: `[established]`, `[supported]`, `[emerging]`, `[theoretical]`.

---

## Session History

Full session history: [[session-history]]