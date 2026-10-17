---
doctype: PDR
id: PDR-P002
domain: product
status: accepted
date: 2026-09-07
tags: [art, style, palette]
constitution-clause: P1
supersedes: null
superseded-by: null
---
# PDR-P002: Hand-Painted 2D Backgrounds with a Limited Palette

## Context
Teo paints every background alone, so the art style sets the pace of the whole project. The style also has to make the [[concepts/tide-window]] readable: players must see at a glance where the water is.

## Decision
Backgrounds are hand-painted in Krita at 1920×1080 with a 16-colour palette per scene. Each tide phase (high, ebbing, low) shifts the palette toward a set tint instead of being repainted.

## Alternatives Considered
- **Pixel art.** Faster per scene, but Teo's pixel work is weaker than his painting.
- **3D scenes with a painted shader.** Free camera moves, but modelling and lighting would take longer than painting.
- **Unlimited palette.** More freedom, but scenes drifted in tone during early tests and took longer to finish.

## Consequences
- **Palette shifts replace repaints.** One background serves all three tide phases, which absorbed [[ideas/tide-color-shift]].
- **About 9 hours per background.** This rate drives the scope math ([[research/scope-estimate]] [emerging]).
- **Strong first impression.** All 6 round 1 playtesters praised the backgrounds unprompted ([[research/playtest-round-1]] [emerging]). Painted art also stands out in store screenshots [unsourced].
