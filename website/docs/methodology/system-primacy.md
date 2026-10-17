# SYSTEM.md Primacy

One file, `SYSTEM.md`, is the single source of truth for the project. Every AI tool reads it first.

If you use several AI tools (Cursor for code, Claude Desktop for planning, Gemini CLI for research), each has its own rule file, and those files drift apart. With one master file, every tool works from the same decisions, constraints, and directory map.

## Pointer Files

Each tool-specific rule file (`.cursorrules`, `CLAUDE.md`, `GEMINI.md`) is a few lines long and tells the AI to read `SYSTEM.md`. When a project rule changes, you edit one file instead of four.
