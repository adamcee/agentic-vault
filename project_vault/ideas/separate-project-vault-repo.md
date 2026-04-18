---
id: separate-project-vault-repo
date: 2026-04-17
status: idea
tags: [architecture, repository-structure, quartz, publishing]
resolved-by: null
---
# Idea: Separate the Meta-Vault into its Own Repository

## Context
Currently, the `agentic-vault` repository contains four top-level directories: `template/`, `example/`, `website/`, and `project_vault/`. The `project_vault/` is the meta-vault we used to build the framework itself (dogfooding the methodology).

## The Proposal
Extract `project_vault/` into its own distinct GitHub repository (e.g., `agentic-vault-meta` or `agentic-vault-internal`). 

## Rationale
1. **Reduce User Confusion:** When a user clones the main `agentic-vault` repository, they might be confused by the presence of a `project_vault/` directory containing our internal ADRs and ideas (like this one) sitting right next to the pristine `template/`. Separating it keeps the main repository laser-focused on the user's needs.
2. **The Ultimate Quartz Showcase:** If `project_vault/` is in its own repository, we can deploy a dedicated Quartz instance for it. This would allow us to publicly publish the *actual, living graph* of how we build and maintain the Agentic Vault project. It becomes a massive, interactive case study of the methodology in action, complete with Backlinks, Graph View, and Hover Previews for all of our internal meta-decisions.

## Trade-offs
- It breaks the elegant symmetry of having the template, the example, the docs, and the meta-project all tracked in a single monorepo.
- Managing PRs and issues across two repositories increases maintainer overhead.

## Next Steps
- Decide if the marketing value of a live Quartz meta-vault outweighs the monorepo convenience.
- If accepted, create the new repository, move the files, and set up a Quartz deployment pipeline for it.