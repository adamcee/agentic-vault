---
id: CONSTITUTION
date: 2026-04-17
status: Active
tags: [architecture, invariants]
---
# [[CONSTITUTION]].md — BrewTrack Invariants

*This document defines what the project is and is not allowed to do. These constraints are non-negotiable. Violating any invariant requires creating a new ADR that explicitly supersedes the relevant clause. "It would be easier" is not sufficient justification.*

## Part I — Product & Domain Invariants

- **P1 — No POS Integrations:** We do not integrate directly with Square, Toast, or clover. The app operates entirely standalone via a merchant-facing scanner app or customer-facing QR codes. Integrating with POS systems requires complex enterprise sales motions that we want to avoid.
- **P2 — Privacy First:** We do not sell or share customer data across cafes. A customer's profile is siloed to the specific cafe they are interacting with.

## Part II — Stack Invariants

- **S1 — React Native Only:** The mobile application must use React Native via Expo. Do not introduce native Swift or Kotlin code unless absolutely necessary via an Expo plugin.
- **S2 — Fast API:** The backend is Python via FastAPI. Do not use Django.

## Part III — Violation Protocol

If there is a genuine reason to violate any invariant in this document:
1. Stop. Do not implement the violation.
2. Create an ADR in `/decisions/technical/` or `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the ADR reviewed before implementing.