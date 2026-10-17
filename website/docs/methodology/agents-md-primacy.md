# AGENTS.md Primacy

One file, `AGENTS.md`, is the single source of truth for the project. Every AI tool reads it first.

If you use several AI tools (Cursor for code, Claude Desktop for planning, Gemini CLI for research), each has its own rule file, and those files drift apart. With one master file, every tool works from the same decisions, constraints, and directory map.

## Why AGENTS.md

`AGENTS.md` is a shared convention that many coding agents, including Codex and Cursor, read by default. Using it as the master file means fewer tools need a pointer at all.

## Pointer Files

For tools that look elsewhere, the template includes short pointer files: `CLAUDE.md` and `GEMINI.md` import `AGENTS.md` with an `@AGENTS.md` line, and `.cursorrules` and `.windsurfrules` tell the AI to read it. Pointer files hold only tool-specific notes, so a project rule changes in one place.
