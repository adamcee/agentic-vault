# AGENTS.md — Night Post Master Context
*Single source of truth for every AI agent working in this vault. Load this file first in every session. Updated: 2026-10-09.*

`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and `.windsurfrules` are short pointers to this file. They hold only tool-specific notes. Project content goes here, never in a pointer file.

## Last Session Checkpoint

On 2026-10-09, the session closed the Festival Demo phase and started Production in [[prototype/implementation-plan]], routing tasks from the festival results logged in [[research/market/demo-festival-results]], including an evaluation of [[ideas/foldable-map]] (opened 2026-10-06) and localization vendor selection. The open question for Ines is whether 23 map requests justify a map that could undercut the moon-shift design in [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]].

Full log: [[session-history]].

---

## Session Start Protocol

Run these steps at the start of every session. Agents with skills can run them as the `vault-start` skill.

1. **Read this file in full**, then your tool's pointer file if it adds notes.
2. **Find what changed since the last session.** Take the date of the last `## YYYY-MM-DD` heading in [[session-history]], then list files changed since that date:
   - **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`
   - **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
   - **No shell:** ask the user what changed.
3. **Ask the session type**: writing, design, art, build, research, decision, production, or vault maintenance.
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
- **`world/` is settled canon.** AI-written lore lands in `drafts/` and enters `world/` only after Ines reviews it against canon. If a script, letter, or design doc contradicts `world/`, `world/` wins until Ines changes it ([[world/README]]).

Night Post's product and stack invariants live in [[architecture/CONSTITUTION]]. In short: no death or fail state from encounters, every letter readable at handheld size, offline and single-player with no microtransactions, scope that fits three people and an October 2027 launch, Godot 4 and GDScript only, 30 frames per second at 800p on the handheld floor, and all text in plain-text files under version control.

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

## What Night Post Is

Night Post is a narrative adventure RPG for PC and handheld PCs. The player is Wren, the newest courier of the Night Post, delivering letters after dark through Hollowmere, a forest whose paths rearrange with the phase of the moon; every quest is a letter, and Wren may open sealed ones ([[architecture/game-design-overview]], [[world/hollowmere]]).

The team is three people, self-funded: Ines Okafor (writer, narrative designer, project lead, and vault owner), Tomas Varga (programmer and composer), and Priya Lund (artist and UI designer). The goal is an 8 to 10 hour game at $18, launching in October 2027 in English, Spanish, and German, as set out in [[strategy/goals-and-audience]] and [[strategy/release-plan]].

---

## Current Phase

Phase 5, Production, started 2026-10-07 after the online demo festival (2026-09-29 to 2026-10-05). The first milestone is final art, script, and music for [[world/regions/thimble-cross]] by 2027-01-29; in the meantime the team must resolve [[ideas/foldable-map]], choose a localization vendor, and submit the Northern Arts Fund application by 2026-11-30 ([[strategy/funding]]).

---

## Vault Structure

- **`architecture/`**: `CONSTITUTION.md` (hard constraints), the game design overview, system docs in `systems/`, and interface docs in `ui/`.
- **`decisions/`**
  - `technical/`: ADRs for tools, stack, and system design.
  - `product/`: PDRs for product, business, and creative choices.
  - `rejected/`: decisions considered and declined.
  - `_BASES_SCHEMA.md`: frontmatter schema for decision records.
- **`strategy/`**: goals, audience, positioning, release plan, and funding.
- **`concepts/`**: definitions of key terms. A concept note says *what something is*.
- **`ideas/`**: raw proposals awaiting evaluation. Each has a `resolved-by` field.
- **`world/`**: settled canon for Hollowmere: regions (with cut regions under `regions/cut/`), factions, characters, and the timeline. AI lore drafts wait in `drafts/` until Ines approves them.
- **`research/`**: evidence, such as interviews, tests, market data, and source summaries.
- **`prototype/`**: `implementation-plan.md` (the production plan and ledger) and milestone specs in `specs/`. Game code lives in a separate Godot repository.
- **`drafts/`**: staging area for AI-generated content.
- **`vault-guide/`**: how the vault works, plus style guides.
- **`journal/`**: human-only notes. Read-only for AI.
- **`session-history.md`**: one line per session, append-only.

---

## Tools & Stack

| Area | Tool |
|---|---|
| Engine | Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-4-engine]]) |
| Script and letters | Plain-text script files loaded by an in-house parser ([[decisions/technical/ADR-T003-plain-text-dialogue-files]]) |
| Art | Krita for painted 2D backgrounds and characters |
| Music and sound | Reaper, plus field recordings from [[research/audio/field-recording-trip]] |
| Version control | Git, with Git LFS (large file storage) for art and audio |
| Test hardware | One handheld PC at the 800p floor ([[concepts/handheld-floor]]) |

**Common commands** (run from the game repository): `godot --path game/` opens the project; `godot --headless --path game/ --script tools/word_count.gd` reports words per letter against the 120-word [[concepts/letter-budget]].

---

## Agentic Boundaries

- **Always:** Apply the tightening checklist to any vault document you write or edit. Use `[[wikilinks]]`.
- **Ask first:** Any change to `world/` canon, new Godot add-ons or plugins, anything that spends money (vendors, contractors, ads), store page copy, and changes to price, launch date, or launch languages.
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

- **Writing (letters, dialogue, lore):** the `world/` docs for the region and characters involved, [[concepts/letter-budget]], [[concepts/sealed-letter]], and [[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]. New lore goes to `drafts/`, not `world/`.
- **Design (systems and levels):** [[architecture/game-design-overview]], the relevant doc in `architecture/systems/`, the matching `concepts/` notes, and the constitution's clauses P1 and P4.
- **Art (backgrounds, characters, interface):** [[decisions/product/PDR-P005-painted-night-palette|PDR-P005]], [[research/accessibility/night-palette-colorblind-test]], [[architecture/ui/letter-reader]], and [[decisions/product/PDR-P011-readable-letters|PDR-P011]].
- **Build (code, tools, performance):** [[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]], [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]], [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]], [[decisions/technical/ADR-T005-atomic-saves|ADR-T005]], Part II of the constitution, and the current plan phase.
- **Research (playtests, surveys, audits):** `research/` and the decisions it may affect. Playtests most often bear on [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]] and [[decisions/product/PDR-P011-readable-letters|PDR-P011]]; market data on [[decisions/product/PDR-P010-price-18-dollars|PDR-P010]].
- **Decision:** `decisions/` index and `architecture/CONSTITUTION.md`. Check for an existing or rejected decision before proposing a new one.
- **Production (planning, strategy, funding):** [[prototype/implementation-plan]], the `strategy/` docs, [[research/production/scope-and-burn]], and the current spec in `prototype/specs/`.
- **Vault maintenance:** `vault-guide/`, [[session-history]], and the `drafts/` folder.

---

## Standing Decisions (Do Not Relitigate Without a New Decision Record)

- **Core fantasy:** every quest is a letter carried by a night courier ([[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]).
- **Engine:** Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]]).
- **Performance floor:** a handheld PC at 30 frames per second and 800p ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]).
- **Text format:** dialogue and letters in plain-text files the writer edits directly ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).
- **Saves:** write to a temp file, then rename ([[decisions/technical/ADR-T005-atomic-saves|ADR-T005]]).
- **Music:** layers that thin out on long walks and return at arrivals ([[decisions/technical/ADR-T006-adaptive-music-layers|ADR-T006]]).
- **Moon-shifting paths:** paths rearrange by moon phase ([[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]). Playtest 4 weakened this on 2026-08-18, and fixed waymark landmarks answered it.
- **Art:** painted 2D in a limited night palette ([[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]). The colorblind test weakened this on 2026-07-27, so route lanterns also differ in shape.
- **Sealed letters:** players may open them, with social consequences only ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- **Encounters:** parley, with no health and no death ([[decisions/product/PDR-P009-parley-encounters|PDR-P009]], which superseded [[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]]).
- **Price:** $18 at launch ([[decisions/product/PDR-P010-price-18-dollars|PDR-P010]]).
- **Letters on screen:** handwriting for headers and signatures only, a readable body typeface, and a font toggle ([[decisions/product/PDR-P011-readable-letters|PDR-P011]], which superseded [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]]).
- **Regions:** three, with the Drowned Bell and the High Briar cut ([[decisions/product/PDR-P012-three-regions|PDR-P012]], which superseded [[decisions/product/PDR-P002-five-regions|PDR-P002]]).
- **Languages:** English, Spanish, and German at launch ([[decisions/product/PDR-P014-launch-languages|PDR-P014]]).
- **Rejected:** procedural forest generation ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]), online co-op ([[decisions/rejected/PDR-P007-co-op-courier-mode|PDR-P007]]), and full voice acting ([[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]).

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
