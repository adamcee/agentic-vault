---
id: vault-design-philosophy
date: YYYY-MM-DD
status: Active
tags: [documentation, vault-administration, design-philosophy]
---
# Vault Design Philosophy

*This document explains how and why the vault is organized. It's a human reference — read this when you need to understand the vault's architecture, not just use it.*

## Why the Vault Exists

The vault is the project's institutional memory for humans and AI. Every AI session starts fresh. Without the vault, each LLM session would repeat the same questions, lose track of rejected alternatives, and drift from standing decisions.

The vault makes markdown documents the AI memory and its source of truth. `SYSTEM.md` is the entry point: it tells a fresh AI session what the project is, what's been decided, what's off-limits, and where to find everything.

## Design Principles

1. **Decisions are first-class objects.** Each important decision has its own doc (ADR or PDR).
2. **Research is traceable, not decorative.** Empirical claims in ADRs link back to specific vault research docs.
3. **Forward propagation + backward reweave.** New decisions push forward into plans; new research forces backward checks of existing decisions.
4. **SYSTEM.md is a routing document, not an encyclopedia.**
5. **Wikilinks are structural.** Every link makes the vault more traversable for both humans and AI agents.
6. **Ideas have a home.** The `ideas/` directory captures raw product and technical ideas before they become decisions.

## Directory Structure Rationale

- **strategy/** and **decisions/** are separate because strategy is aspirational while decisions are committal.
- **concepts/** contains atomic definitions of key terms. It doesn't propose anything new.
- **ideas/** captures raw proposals. 
- **research/** is evidence, not commitment.
- **architecture/** contains the system design docs, which are downstream of decisions.
- **prototype/** (or `src/`) contains implementation artifacts, downstream of architecture.

The flow: Research → Decisions → Architecture → Implementation.