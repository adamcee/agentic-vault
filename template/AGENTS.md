# [Project Name] — Navigation Map & Orchestration
*Single Source of Truth (SSOT) for all agentic navigation and operational protocols.*

## VAULT TOPOLOGY

If a query requires domain-specific knowledge, agents must route to the corresponding directory:

- **`architecture/`**
  - `CONSTITUTION.md`: Core project and technical invariants.
  - System design documents and specifications.
- **`decisions/`**
  - `technical/`: ADRs for stack, database, and infrastructure.
  - `product/`: PDRs for pedagogy, GTM, and personas.
  - `_BASES_SCHEMA.md`: Frontmatter schema for structured ADR/PDR search.
- **`strategy/`**
  - Current product and business strategy.
  - User personas and journeys.
- **`concepts/`**
  - Atomic concept notes (zettelkasten link hubs). Define *what something is*. Not proposals.
- **`ideas/`**
  - Raw idea captures awaiting evaluation. Propose *something that could exist*. Frontmatter includes `resolved-by` field.
- **`research/`**
  - Market research, learning science, competitive intel, session syntheses.
- **`prototype/`** (or `src/`, `app/`)
  - `implementation-plan.md`: Vault ledger — active phases and open tasks.
  - `implementation-logs/`: Weekly append-only session logs.
  - `specs/` & `stories/`: Feature specifications and atomic work units.
- **`drafts/`**
  - Ingestion staging area: AI-generated content lands here before vault admission.
- **`vault-guide/`**
  - Vault design philosophy, style guides, and protocols.
- **`journal/`**
  - Human-only daily notes. Read-only for AI. Never write here.

---

## OPERATIONAL PROTOCOLS

### Stack Quick Reference

[Replace with your project's technical stack]

| Layer | Technology |
|-------|-----------|
| **Frontend** | [e.g., React / TypeScript] |
| **Backend** | [e.g., Node.js / Python] |
| **Database** | [e.g., PostgreSQL] |
| **Deployment** | [e.g., Vercel / AWS] |

### General Commands

[Replace with your project's frequently used shell commands]

```bash
# Install dependencies
npm install

# Test suite
npm run test

# Start local server
npm run dev
```

### Agentic Boundaries

- **Always:** Apply the 10-point tightening checklist to any vault document written or edited. Use `[[wikilinks]]` in vault docs. Keep code strictly within the established architecture.
- **Ask First:** Adding new external dependencies, changing database schemas, modifying authentication logic.
- **Never:** Commit secrets, modify `.env` files directly, write to `journal/` (human-only).

---

## VAULT FILE ACCESS PROTOCOL

Agents operating in the vault should use the most appropriate tool available in their environment:

1. **Obsidian MCP (Primary for Desktop):** 
   - `obsidian_read`, `obsidian_search`, `obsidian_create`
2. **Native Filesystem Tools (Primary for CLI):**
   - `read_file`, `replace`, `grep_search`, `glob`
3. **Obsidian CLI (For Metadata & Graph queries in CLI):**
   - If installed, use `run_shell_command` with `/Applications/Obsidian.app/Contents/MacOS/obsidian search ...`

---

## BOOTSTRAPPING HIERARCHY

1. **Bootstrap:** `SYSTEM.md` (Master context, protocols, standing decisions).
2. **Index:** `AGENTS.md` (This file — navigation map, stack reference).
3. **Execution:** Specific content files mapped in Vault Topology above.