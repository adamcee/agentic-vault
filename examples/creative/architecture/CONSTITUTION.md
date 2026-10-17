---
id: CONSTITUTION
date: 2026-08-31
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Low Tide Invariants

*These invariants define what Low Tide must and must not do, and they are non-negotiable. Breaking one requires a new ADR or PDR that supersedes the clause by name, and "it would be easier" is not a reason.*

## Part I — Game Invariants

- **P1 — Two-Person Scope:** Every feature must be buildable and maintainable by Mara and Teo alone. Nothing may depend on a third person's ongoing work, such as voice acting, server upkeep, or community moderation.
- **P2 — No Lost Progress:** A failed puzzle or a missed [[concepts/tide-window]] resets the puzzle, never the save.
- **P3 — Offline, Single-Player:** The game runs fully offline with no accounts, telemetry, or network features. Playtest data comes from notes and recordings, not from the game.

## Part II — Engine and Pipeline Invariants

- **S1 — Godot and GDScript Only:** All game code is GDScript in Godot 4, with no C# or native extensions, so one export path covers Windows, macOS, and Linux ([[decisions/technical/ADR-T001-godot-engine|ADR-T001]]).
- **S2 — Everything in Version Control:** Scenes, scripts, dialogue, and source paintings live in the Git repository, with large art files stored through Git LFS.

## Part III — Violation Protocol

If there is a genuine reason to violate any invariant in this document:
1. Stop. Do not implement the violation.
2. Create an ADR in `/decisions/technical/` or a PDR in `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the record reviewed by both team members before implementing.
