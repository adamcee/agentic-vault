# Implementation Plan: Agentic Vault Template
*Updated: 2026-04-17*

This is the vault ledger for building the Agentic Vault template project.

## Phase 1: Meta-Vault Initialization (Current)
- [x] Create project directory structure (`project_vault/`, `template/`, `example/`, `website/`).
- [x] Seed `project_vault/` with `CLAUDE.md`, `CONSTITUTION.md`, and this `implementation-plan.md`.

## Phase 2: Template Structure Creation
- [x] Create core directories in `template/` (`decisions/`, `strategy/`, `architecture/`, `research/`, `ideas/`, `drafts/`, `journal/`, `vault-guide/`).
- [x] Draft a model-agnostic master context file (e.g., `SYSTEM.md` or `CLAUDE.md`).
- [x] Translate Chameleon's `vault-guide/` (Philosophy, Writing Discipline, Protocols) into domain-agnostic template files.
- [x] Draft `AGENTS.md` equivalent with placeholders.
- [x] Create `decisions/` schema and index bases.

## Phase 3: Setup Automation & Skills
- [x] Port `.claude/skills/` from Chameleon, adapting instructions to be graceful if missing.
- [x] Write `init-vault.sh` or a Python setup script to scaffold a new vault from the template.
- [x] Add `.gitignore` and recommended `.obsidian/` configurations.

## Phase 4: README & Interactive Guide
- [x] Write the Tiered `README.md` (Web App, Desktop App, CLI).
- [x] Draft the Interactive AI Onboarding Prompt (The "Wizard").

## Phase 5: Example Repo Creation
- [x] Clone the finalized `template/` into `example/`.
- [x] Invent a fictional project (e.g., Local Coffee Shop App).
- [x] Populate `example/` with realistic ADRs, PDRs, a `CONSTITUTION.md`, and an `implementation-plan.md` to demonstrate the methodology in action.

## Phase 6: Website/Documentation
- [x] Build a simple landing page or MkDocs site in `website/` explaining the philosophy and linking to the template and example.

## Phase 7: Next Session Priorities
- [ ] Setup GitHub Pages for the main site (MkDocs deployment verification).
- [ ] Add a best-practice research doc (written by Claude) on the vault methodology, principles, and how it works to the project.
- [ ] Extract the `project_vault/` into a separate repository and build a beautiful, public Quartz site for it. Link it back to the main repository.
- [ ] Research and document a good Windows alternative to Obsidian, other general Obsidian alternatives, and a web-based note-taking alternative to give users multiple tooling options.
- [ ] Fix the BrewTrack example vault links (they currently route back to the homepage).