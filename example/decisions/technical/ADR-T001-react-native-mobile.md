---
doctype: ADR
id: ADR-T001
domain: technical
status: accepted
date: 2026-04-17
tags: [mobile, react-native, expo, frontend]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T001: React Native (Expo) for Mobile Frontend

## Context
BrewTrack needs a mobile application that works on both iOS and Android. As a solo developer, maintaining two separate codebases (Swift and Kotlin) is untenable. The app primarily relies on QR code scanning, push notifications, and standard REST API calls.

## Decision
We will use **React Native** managed by **Expo** for all mobile application development.

## Alternatives Considered
- **Flutter:** Rejected. While performant, the ecosystem is heavily Dart-based, and the team has much more existing context and experience with TypeScript and the React ecosystem.
- **Swift / Kotlin (Native):** Rejected. Too slow for a solo dev to build and maintain feature parity across two separate OS platforms.
- **Progressive Web App (PWA):** Rejected. Apple's inconsistent support for Push Notifications and camera access in PWAs degrades the primary QR scanning and notification features.

## Consequences
- We will be constrained by the libraries supported by the Expo ecosystem, although Expo's recent updates to custom dev clients mitigate this.
- Rapid deployment and Over-The-Air (OTA) updates are possible via Expo Application Services (EAS).
- Reaffirms [[CONSTITUTION]] clause S1.