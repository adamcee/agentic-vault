# [[CLAUDE]].md — Agentic Vault Meta-Project
*Load this file first in every AI session for the `agentic-vault` meta-project. Updated: 2026-04-17.*

## What This Project Is

This is the meta-vault used to build and organize the **Agentic Vault Template**. 

The goal is to distill the highly effective structure, protocols, and discipline of the `chameleon_vault` into a domain-agnostic, reusable "Agentic Knowledge Base" template. This template is designed for both non-technical founders/writers and developers who want to manage context efficiently with AI agents (Claude Code, Gemini CLI, Obsidian MCP).

## Current Phase

**Phase 1: Meta-Vault Initialization** (Just starting!)
We are setting up the structure to build the template itself. See `prototype/implementation-plan.md` for the full roadmap.

## Project Structure

```text
/Users/adamcee/ai/agentic-vault/
├── project_vault/    ← You are here. The meta-vault managing the creation of the template.
├── template/         ← The pristine, domain-agnostic vault structure to be published.
├── example/          ← A populated example (e.g., a local coffee shop app) demonstrating ADRs and PDRs.
└── website/          ← Documentation and landing page.
```

## Hard Constraints

- **Domain Agnostic:** The `template/` must contain absolutely zero references to Chameleon, Elixir, pyBKT, or Marcus/Destiny. It must be generic.
- **Graceful Degradation:** The template must be usable by non-technical people who just copy/paste text into a web app, all the way up to devs using CLI agents. Instructions in the template's `CLAUDE.md` must account for missing skills or CLI tools.
- **Progressive Enhancement:** Documentation (READMEs and guides) must be tiered (Tier 1: Web App, Tier 2: Desktop App + MCP, Tier 3: CLI tools).
- **Dogfooding:** Any structural decision or protocol we plan to put in the `template/` should first be implemented or documented in this `project_vault/`.

## Standing Decisions

- **Naming:** Temporary working title is "Agentic Vault" or "AI-Native Vault Template". Final name pending.
- **Architecture:** The template will perfectly mirror the `chameleon_vault` directory structure (`decisions/`, `strategy/`, `architecture/`, `research/`, `ideas/`, `drafts/`, `journal/`, `vault-guide/`).

## Task-Specific Context Loading

- **Template Generation Session:** Load `architecture/CONSTITUTION.md` and the relevant phase in `prototype/implementation-plan.md`. Read the original `chameleon_vault` equivalents to ensure no structural nuance is lost.
- **Documentation Session:** Load the target `README.md` or guide, and refer to `strategy/` for the target audience.