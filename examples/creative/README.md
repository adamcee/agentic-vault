---
title: Night Post — Example Vault
---
# Night Post — Example Vault

Night Post is a narrative adventure about the newest courier of a postal service that only works after dark. You carry letters through Hollowmere, a forest whose paths rearrange with the phase of the moon, and every letter is a quest.

You can open the sealed ones. What you read changes what people say to you, and in a game with no combat and no villain, the trouble comes from unpaid debts, old grudges, and what you chose to know.

This vault is fictional. It follows a three-person team from the first session on 2026-04-06 to the start of Production on 2026-10-09, through five playtests, a demo festival, three superseded decisions, and two cut regions.

## Start Here

Open [[AGENTS]] first. It is the file every AI session reads before acting: the game, the current phase, the hard constraints, the standing decisions, and the Last Session Checkpoint.

## Tour

### Session Protocol: How a New Session Picks Up the Thread
- **Checkpoint:** the Last Session Checkpoint in [[AGENTS]] says what the 2026-10-09 session did and what question waits for the human.
- **Log:** [[session-history]] has one line per session from 2026-04-06 to 2026-10-09. Every decision and research doc appears on its date.
- **Constitution:** [[architecture/CONSTITUTION]] holds the invariants, and each clause names the decision that added it.

### Decision Records: Superseded, Rejected, and Weakened
- **Superseded after a playtest:** [[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]] planned turn-based encounters. Two playtests later, [[decisions/product/PDR-P009-parley-encounters|PDR-P009]] replaced them with parley and explains what changed.
- **Superseded by scope:** [[decisions/product/PDR-P002-five-regions|PDR-P002]] planned five regions, and [[decisions/product/PDR-P012-three-regions|PDR-P012]] cut two when the money and the publishers said no.
- **Superseded by accessibility:** [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]] gave way to [[decisions/product/PDR-P011-readable-letters|PDR-P011]], traced step by step in the next section.
- **Rejected:** [[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]] (procedural forest), [[decisions/rejected/PDR-P007-co-op-courier-mode|PDR-P007]] (online co-op, blocked by a constitution clause), and [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]] (full voice acting).
- **Weakened but standing:** [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]] and [[decisions/product/PDR-P005-painted-night-palette|PDR-P005]] each carry a dated reweave note. The team fixed the problem without replacing the decision.

### Reweave: One Finding Followed End to End
1. **The playtest:** [[research/playtests/pt-04-vertical-slice]] found that 4 of 10 handheld players squinted at handwritten letters. Its Reweave Triggers flagged PDR-P006.
2. **The audit:** [[research/accessibility/letter-readability-audit]] measured the problem against the standard in [[research/accessibility/text-contrast-and-size-standards]].
3. **The decision:** [[decisions/product/PDR-P011-readable-letters|PDR-P011]] superseded PDR-P006 and moved handwriting to headers and signatures.
4. **The constitution:** clause P2 of [[architecture/CONSTITUTION]] now requires every letter to be readable at handheld size.
5. **The plan:** the font toggle appears in [[prototype/implementation-plan]] as a task marked with its research source, and [[architecture/ui/letter-reader]] was rewritten.
6. **The check:** [[research/playtests/pt-05-demo-build]] found 5 of 12 players used the toggle, which strengthened PDR-P011.

A second chain runs from [[research/market/publisher-pitch-feedback]] and [[research/production/scope-and-burn]] to [[decisions/product/PDR-P012-three-regions|PDR-P012]] and the cut regions in `world/regions/cut/`.

### Research: Types of Evidence and Their Maturity
- **Playtests:** five, from [[research/playtests/pt-01-paper-prototype]] to [[research/playtests/pt-05-demo-build]]. [[research/playtests/pt-03-parley-prototype]] is tagged `supported` because it repeated an earlier finding.
- **Market:** [[research/market/community-survey-01]], [[research/market/publisher-pitch-feedback]], and [[research/market/demo-festival-results]].
- **External standards:** [[research/accessibility/text-contrast-and-size-standards]] is the only `established` doc, and it cites published standards only.
- **Technical, audio, and narrative tests:** [[research/technical/save-corruption-test]], [[research/audio/music-listening-test]], and [[research/narrative/letter-length-test]], each of which led to a decision or a concept.
- **An honest gap:** [[decisions/product/PDR-P010-price-18-dollars|PDR-P010]] cites its evidence inline and flags one claim `[unsourced]`.

### Ideas: Every State
- **Promoted:** [[ideas/talk-instead-of-fight]] became PDR-P009.
- **Absorbed:** [[ideas/waymark-landmarks]] became a plan task, and [[ideas/postmark-badges]] became [[concepts/postmark]].
- **Rejected:** [[ideas/crafting-system]] and [[ideas/full-day-night-cycle]], each with a one-line reason.
- **Open:** [[ideas/foldable-map]] (from 23 festival comments), [[ideas/letter-writing-minigame]], [[ideas/ledger-upgrades]], and [[ideas/one-handed-mode]].

### World Canon Versus an AI Lore Draft
- **Canon:** [[world/README]] explains how lore enters `world/`. [[world/factions/the-hushfolk]] says the Hushfolk never lie, and [[world/characters/mothwife-sel]] is their envoy to the Night Post.
- **The draft:** [[drafts/ai-lore-hushfolk-expansion]] is padded AI lore that gets both facts wrong. It makes the Hushfolk liars and Sel a hidden matriarch who never speaks to outsiders, which is why it waits in `drafts/` for a human.
- **Cut regions:** [[world/regions/cut/the-drowned-bell]] and [[world/regions/cut/the-high-briar]] stay on file so nobody rebuilds them by accident.

### Ingestion Gate: Drafts and Their Originals
- **Admitted with originals kept:** [[research/market/genre-comparables]] sits beside [[research/market/_source-genre-comparables]], and [[research/localization/localization-cost-estimate]] sits beside [[research/localization/_source-localization-cost-estimate]]. Compare each pair to see what tightening removes.
- **Still waiting:** [[drafts/ai-report-festival-marketing-plan]] is raw AI prose that missed the festival it was written for. Its tightening task is still open in the plan.

### Design and Production
- **Game design:** [[architecture/game-design-overview]] and the system docs [[architecture/systems/parley]], [[architecture/systems/moon-and-paths]], [[architecture/systems/postmarks]], and [[architecture/systems/lantern-oil-economy]].
- **Strategy:** [[strategy/goals-and-audience]], [[strategy/positioning]], [[strategy/release-plan]], and [[strategy/funding]].
- **Production plan:** [[prototype/implementation-plan]] runs from Concept to Production, with milestone specs in [[prototype/specs/vertical-slice]] and [[prototype/specs/festival-demo]].
