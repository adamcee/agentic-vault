---
id: vault-design-philosophy
date: YYYY-MM-DD
status: Active
tags: [documentation, vault-administration, design-philosophy]
---
# Vault Design Philosophy

*A human reference for why the vault is organized this way. AI sessions don't need to load it at start.*

## Why the Vault Exists

The vault is the project's memory for humans and AI. Without it, each AI session starts fresh, repeats old questions, loses track of rejected alternatives, and drifts from standing decisions.

`SYSTEM.md` is the entry point. It tells a fresh session what the project is, what's been decided, what's off-limits, and where everything lives.

## Design Principles

1. **Decisions are first-class objects.** Each important decision has its own doc (ADR or PDR).
2. **Research is traceable, not decorative.** Empirical claims in ADRs link back to specific vault research docs.
3. **Forward propagation + backward reweave.** New decisions push forward into plans; new research forces backward checks of existing decisions.
4. **SYSTEM.md is a routing document, not an encyclopedia.**
5. **Wikilinks are structural.** Links let humans and AI agents navigate by following connections.
6. **Ideas have a home.** The `ideas/` directory captures raw product and technical ideas before they become decisions.

## Directory Structure Rationale

- **strategy/** and **decisions/** are separate because strategy states what you want, while decisions record what you chose.
- **concepts/** contains atomic definitions of key terms. It doesn't propose anything new.
- **ideas/** captures raw proposals until they are promoted, rejected, or absorbed.
- **research/** is evidence, not commitment.
- **architecture/** contains the system design docs, which are downstream of decisions.
- **prototype/** (or `src/`) contains implementation artifacts, downstream of architecture.

The flow: Research → Decisions → Architecture → Implementation.