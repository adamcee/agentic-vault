---
doctype: PDR
id: PDR-P001
domain: product
status: accepted
date: 2026-04-17
tags: [product, gamification, rewards]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P001: Gamified Tier System

## Context
Standard "Buy 10, Get 1 Free" punch cards are easily forgotten and offer no progressive incentives. We need a way to increase customer retention and order value beyond a simple linear reward.

## Decision
BrewTrack will implement a tiered loyalty system (e.g., Bronze, Silver, Gold). Customers earn 10 points per dollar spent. Reaching higher tiers permanently unlocks micro-perks (e.g., "Silver tier gets free alternative milk," "Gold tier gets free espresso shots").

## Alternatives Considered
- **Straight Punch Card (Buy 10 Get 1):** Rejected. Fails to incentivize higher-value purchases or create long-term lock-in.
- **Paid Subscription (e.g., Panera Sip Club):** Rejected. Too complex for independent coffee shops to manage financially without risking revenue loss.

## Consequences
- The database schema must track both lifetime points (for tier status) and current points (for redeemable rewards).
- The UI must prominently display the progress bar to the next tier to trigger the "endowed progress effect."