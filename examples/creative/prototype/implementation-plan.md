---
id: implementation-plan
title: Implementation Plan
date: 2026-04-06
status: Active
tags: [prototype, plan, ledger, production]
---
# Implementation Plan
*Updated: 2026-10-09*

This plan is the vault ledger, and AI sessions route every new action item here. Tasks that came from new evidence are marked `(reweave: [[research/...]])`.

## Phase 1: Concept (Done, April 2026)
- [x] Write the core fantasy: a night courier whose every quest is a letter ([[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]).
- [x] Choose Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]]).
- [x] Set the handheld PC as the minimum target ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]).
- [x] Draft the world: [[world/hollowmere]], five regions, and three factions ([[world/README]]).
- [x] Plan five regions ([[decisions/product/PDR-P002-five-regions|PDR-P002]], since superseded).
- [x] Run the paper prototype with five players ([[research/playtests/pt-01-paper-prototype]]).
- [x] Note the paper "combat" doubt for the greybox encounter test (reweave: [[research/playtests/pt-01-paper-prototype]]).
- [x] Store dialogue and letters as plain-text files with an in-house parser ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).

## Phase 2: Greybox (Done, May to June 2026)
- [x] Build hand-authored greybox paths for one region; procedural generation rejected ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]).
- [x] Build moon-phase path layouts with four phases ([[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]], [[architecture/systems/moon-and-paths]]).
- [x] Build turn-based encounters for playtest 2 ([[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]], since superseded).
- [x] Replace turn-based encounters with a parley prototype (reweave: [[research/playtests/pt-02-greybox-encounters]]).
- [x] Run playtest 3 on the parley prototype ([[research/playtests/pt-03-parley-prototype]]).
- [x] Write [[architecture/systems/parley]] and remove health and death from the design ([[decisions/product/PDR-P009-parley-encounters|PDR-P009]]).
- [x] Replace volumetric fog with a baked fog layer in Gloamwick (reweave: [[research/technical/handheld-perf-benchmark]]).
- [x] Record wetland ambience for the night soundscape ([[research/audio/field-recording-trip]]).
- [x] Build the sealed-letter open action ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- [x] Add a word count and a 120-word warning to the script parser (reweave: [[research/narrative/letter-length-test]]).

## Phase 3: Vertical Slice (Done, July to August 2026, finished 2026-08-28)
- [x] Write the [[prototype/specs/vertical-slice]] spec.
- [x] Paint Thimble Cross and the first Gloamwick route in the night palette ([[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]).
- [x] Give red and green route lanterns distinct shapes (reweave: [[research/accessibility/night-palette-colorblind-test]]).
- [x] Trim slice letters to the 120-word [[concepts/letter-budget]] (reweave: [[research/narrative/letter-length-test]]).
- [x] Build fast and kind postmarks with tier 1 abilities ([[architecture/systems/postmarks]]).
- [x] Switch saves to write-temp-then-rename (reweave: [[research/technical/save-corruption-test]]).
- [x] Split the music into layers that thin out on long walks (reweave: [[research/audio/music-listening-test]]).
- [x] Run the community survey ([[research/market/community-survey-01]]).
- [x] Set the launch price at $18 ([[decisions/product/PDR-P010-price-18-dollars|PDR-P010]]).
- [x] Run playtest 4 on the slice ([[research/playtests/pt-04-vertical-slice]]).

## Phase 4: Festival Demo (Done, September to 2026-10-05)
- [x] Write the [[prototype/specs/festival-demo]] spec.
- [x] Give every waymark in the demo a fixed landmark (reweave: [[research/playtests/pt-04-vertical-slice]]; absorbed [[ideas/waymark-landmarks]]).
- [x] Set letter bodies in a readable typeface and keep handwriting for headers and signatures (reweave: [[research/accessibility/letter-readability-audit]]).
- [x] Add the font toggle to settings and to the letter reader (reweave: [[research/accessibility/letter-readability-audit]]).
- [x] Pitch three publishers and log the feedback ([[research/market/publisher-pitch-feedback]]).
- [x] Re-plan for three regions and cut the Drowned Bell and the High Briar (reweave: [[research/production/scope-and-burn]]).
- [x] Move the Drowned Bell's best story to Sallow Ferry and fold the High Briar into Gloamwick's edges ([[decisions/product/PDR-P012-three-regions|PDR-P012]]).
- [x] Limit voice to barks and drop full voice acting (reweave: [[research/narrative/script-word-count]]).
- [x] Set launch languages to English, Spanish, and German ([[decisions/product/PDR-P014-launch-languages|PDR-P014]]).
- [x] Run playtest 5 on the demo build ([[research/playtests/pt-05-demo-build]]).
- [x] Ship the demo to the festival on 2026-09-29.
- [ ] Tighten [[drafts/ai-report-festival-marketing-plan]] through the ingestion gate. This was missed before the festival; keep the parts that apply to launch and delete the rest.

## Phase 5: Production (Current, from 2026-10-07)
- [x] Archive the festival build and tag it in version control.
- [x] Log festival results in [[research/market/demo-festival-results]].
- [ ] Evaluate a foldable map against the moon-shift design in [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]] and resolve [[ideas/foldable-map]] (reweave: [[research/market/demo-festival-results]]).
- [ ] Select a localization vendor from the three quotes for Spanish and German (reweave: [[research/localization/localization-cost-estimate]]).
- [ ] Run the readability audit on Spanish and German letters at 800p (reweave: [[research/accessibility/letter-readability-audit]]).
- [ ] Send the publisher who asked for a follow-up the festival results and the three-region plan (reweave: [[research/market/publisher-pitch-feedback]]).
- [ ] Submit the Northern Arts Fund application by 2026-11-30, asking for the localization cost ([[strategy/funding]]).
- [ ] Add festival comments about the letters and tone to the store page (reweave: [[research/market/demo-festival-results]]).
- [ ] Recheck runway against actual spend on 2026-12-05 (reweave: [[research/production/scope-and-burn]]).
- [ ] Finish Thimble Cross art, script, and music by 2027-01-29 ([[world/regions/thimble-cross]], [[strategy/release-plan]]).
- [ ] Finish Gloamwick, including the High Briar edges, by 2027-03-26 ([[world/regions/gloamwick]]).
- [ ] Finish Sallow Ferry, including the moved Drowned Bell story, by 2027-05-28 ([[world/regions/sallow-ferry]]).
- [ ] Build careful and nosy tier 2 and tier 3 abilities ([[architecture/systems/postmarks]]).
- [ ] Give every waymark in Gloamwick and Sallow Ferry a fixed landmark, as in Thimble Cross (reweave: [[research/playtests/pt-05-demo-build]]).
- [ ] Record voiced barks in English, Spanish, and German ([[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]).
- [ ] Review [[drafts/ai-lore-hushfolk-expansion]] against [[world/factions/the-hushfolk]] and [[world/characters/mothwife-sel]] before any of it enters `world/`.
- [ ] Run playtest 6 on a full three-region build on handhelds.
