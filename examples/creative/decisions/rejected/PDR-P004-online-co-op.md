---
doctype: PDR
id: PDR-P004
domain: product
status: rejected
date: 2026-09-14
tags: [multiplayer, co-op, scope]
constitution-clause: P3
supersedes: null
superseded-by: null
---
# PDR-P004: Online Two-Player Co-op Mode (Rejected)

## Context
Teo proposed an online mode where two players share one island, each seeing clues the other cannot. Split-clue puzzles suit the tide theme, and a friend's suggestion made the idea sound cheap.

## Decision
Rejected. Low Tide stays a single-player, offline game.

## Alternatives Considered
- **Online co-op with split clues.** The proposal as stated.
- **Local co-op on one screen.** No servers, but it still doubles puzzle design and testing.
- **Single-player only.** Chosen.

## Reasons for Rejection
- **Breaks two invariants.** Online play needs networking, accounts, and server upkeep, against [[architecture/CONSTITUTION]] P1 and P3.
- **Doubles puzzle work.** Every puzzle would need a solo and a two-player version.
- **Weak fit with the story.** Ines's return to the island is a solitary story, and a second player would change its tone.
- **Revisit only if** the single-player game ships and a second, separate project is planned.
