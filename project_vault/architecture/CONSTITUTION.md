---
id: CONSTITUTION
date: 2026-04-17
status: Active
tags: [architecture, invariants, template-design]
---
# [[CONSTITUTION]].md — Agentic Vault Invariants

*This document defines the non-negotiable rules for building the Agentic Vault template. Violating any invariant requires creating an ADR.*

## Part I — Design Invariants

- **D1 — Strict Domain Agnosticism**
The `template/` directory must be a completely blank slate structurally. It must contain no specific product, persona, or technical stack references from its source (Chameleon). Placeholders must clearly indicate where the user should inject their own domain knowledge (e.g., `[Insert Project Name Here]`).

- **D2 — The "CLAUDE.md" Primacy**
The template relies on `CLAUDE.md` (or a similarly named master context file if we rename it to be model-agnostic, e.g., `SYSTEM.md` or `AGENT.md`) as the Single Source of Truth (SSOT). All other documentation stems from this routing point.

- **D3 — Tiered Accessibility (Graceful Degradation)**
The template must not break if a user lacks technical skills. Protocols must offer a "manual" or "web app" fallback. For instance, if an automated script or a `.claude/skill/` isn't available, the documentation must explain how to manually verify links or update indexes.

- **D4 — Principle over Tooling**
The vault methodology (Decision Records, Reweave Protocols, Research Traceability, Writing Discipline) is more important than the specific markdown editor. The template should recommend Obsidian (for its graph and linking features) but must remain fundamentally editor-agnostic markdown.

## Part II — Output Invariants

- **O1 — Three Distinct Outputs**
The project must produce:
1. `template/` — The blank, reusable directory structure.
2. `example/` — The populated demonstration vault.
3. `website/` or `docs/` — The tiered installation and philosophy guide.

- **O2 — The Interactive Setup Guide**
We must produce an interactive AI prompt that acts as an onboarding wizard. It will ask the user about their environment and context, then generate their initial `CLAUDE.md`, `CONSTITUTION.md`, and directory structure dynamically.