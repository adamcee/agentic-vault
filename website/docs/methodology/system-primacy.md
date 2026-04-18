# The SYSTEM.md Primacy

The core philosophy of the Agentic Vault is the **Single Source of Truth (SSOT)**. 

When you use multiple AI tools (e.g., Cursor for coding, Claude Desktop for planning, Gemini CLI for research), their context windows easily drift out of sync. By enforcing a single `SYSTEM.md` file that all agents must read, you guarantee that your architectural decisions, directory maps, and rules are universally applied.

### The "Hub and Spoke" Architecture
Every agent-specific rule file (`.cursorrules`, `CLAUDE.md`, `GEMINI.md`) in this vault is simply a "spoke"—a tiny pointer file instructing the AI to read the central "hub" (`SYSTEM.md`).

This prevents you from having to manually update 4 different configuration files every time you change a project rule.