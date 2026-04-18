# Implementation Plan: BrewTrack MVP
*Updated: 2026-04-17*

This is the vault ledger for building the BrewTrack prototype.

## Phase 1: Foundation
- [x] Write ADR for React Native selection (ADR-T001).
- [x] Write PDR for Gamified Tier System (PDR-P001).
- [x] Establish the project `SYSTEM.md` and `CONSTITUTION.md`.
- [ ] Initialize the Expo app in `/mobile`.
- [ ] Initialize the FastAPI server in `/backend`.

## Phase 2: Core QR Mechanics
- [ ] Design the database schema for Users, Cafes, and Scans.
- [ ] Build the QR code generation endpoint in FastAPI.
- [ ] Build the QR code scanner component in React Native.
- [ ] Wire up the "Scan to Award Points" logic.

## Phase 3: Gamification UI
- [ ] Implement the Tier Progress Bar component.
- [ ] Build the rewards catalog view.
- [ ] Wire up the point redemption logic in the backend.