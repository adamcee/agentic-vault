---
doctype: ADR
id: ADR-T001
domain: technical
status: accepted
date: 2026-08-31
tags: [engine, godot, pipeline]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T001: Build Low Tide in Godot 4 with GDScript

## Context
Low Tide needs 2D scenes with painted backgrounds, a dialogue system, and puzzle logic, exported to Windows, macOS, and Linux. Teo is the only programmer and also paints every background, so engine time comes straight out of art time.

## Decision
Build the game in Godot 4 using GDScript only. Scenes, dialogue triggers, and puzzle state live in Godot's scene and resource files under version control.

## Alternatives Considered
- **A large commercial 3D-first engine.** Teo has used one before, but its 2D workflow adds setup the game does not need, and its licence terms have changed more than once.
- **A dedicated visual-novel framework.** It handles dialogue well but makes the point-and-click puzzles awkward to build.
- **A custom engine in a general-purpose language.** Full control, but months of work before the first playable scene.

## Consequences
- **Free and open source.** No licence fees or revenue share, and the editor runs well on Teo's laptop.
- **One export pipeline.** GDScript-only code keeps exports to all three desktop platforms on a single path (see [[architecture/CONSTITUTION]] S1).
- **Smaller plugin pool.** Some tools, such as a dialogue editor, may need to be built in-house.
- **Console ports get harder.** Godot console exports go through third parties, which is acceptable because the release is PC only.
