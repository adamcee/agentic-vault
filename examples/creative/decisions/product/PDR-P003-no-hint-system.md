---
doctype: PDR
id: PDR-P003
domain: product
status: accepted
date: 2026-09-09
tags: [puzzles, hints, difficulty]
constitution-clause: P2
supersedes: null
superseded-by: null
---
# PDR-P003: No Hint System; Puzzles Teach Through the Scene

## Context
Each puzzle must be solved within a [[concepts/tide-window]], so a stuck player watches the water return. Mara wanted the clues to live in the painted scenes and the journal, not in a help button.

## Decision
Low Tide ships without a hint system. Every clue is visible in the scene or recorded in Ines's journal once found, and a failed tide resets the puzzle, never the save.

## Alternatives Considered
- **On-demand hint button.** Players can skip the thinking, and the button breaks the quiet tone.
- **Timed hints.** A hint appears after a set time stuck, which players cannot control.
- **External walkthrough only.** Costs nothing to build but sends players out of the game.

## Consequences
- **Puzzle clarity carries the load.** Every puzzle needs a clue a first-time player can find.
- **Early support.** 4 of 6 round 1 playtesters solved both act 1 puzzles without help ([[research/playtest-round-1]] [emerging]).

## Reweave Notes
- **2026-10-05, weakened.** 5 of 8 round 2 playtesters were stuck over 10 minutes on the act 2 tide-chart puzzle, and 2 quit there ([[research/playtest-round-2]] [emerging]). Flagged for Mara and Teo but not superseded yet: a layered hint prototype ([[ideas/layered-hints]]) will be tested in playtest round 3 first (see [[prototype/implementation-plan]]).
