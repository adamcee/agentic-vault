---
name: vault-start
description: "Session bootstrap for the Agentic Vault. MUST be invoked at the start of every AI session before any substantive work. Triggers: /vault-start, beginning of any session, or when AGENTS.md instructs you to run the startup protocol."
---

# Vault Session Bootstrap

Runs the Session Start Protocol in `AGENTS.md`. Do not skip steps or work from memory of a previous session.

## Step 1: Read AGENTS.md
Read `AGENTS.md` in full. Note the Hard Constraints, Standing Decisions, Current Phase, and Last Session Checkpoint.

## Step 2: Find What Changed Since the Last Session
Take the date of the last `## YYYY-MM-DD` heading in `session-history.md` (`grep '^## ' session-history.md | tail -1`). Then list files changed since that date:
- **Git:** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`
- **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
- **Obsidian MCP:** `obsidian_global_search(query=".", useRegex=true, modified_since="YYYY-MM-DD")`
- **None of these:** ask the user what changed.

## Step 3: Identify the Session Type
Ask the user what kind of session this is, such as planning, research, decision, writing, coding, or vault maintenance.

## Step 4: Load Task-Specific Context
Load the files listed for that session type under "Task-Specific Context Loading" in `AGENTS.md`.

## Step 5: Confirm Readiness
In a few sentences, tell the user what changed and what you loaded.
