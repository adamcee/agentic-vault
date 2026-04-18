---
name: vault-start
description: "Session bootstrap for the Agentic Vault. MUST be invoked at the start of every AI session before any substantive work. Triggers: /vault-start, beginning of any session, or when SYSTEM.md instructs you to run the startup protocol."
---

# Vault Session Bootstrap

This skill ensures you load the correct context before doing work. 

**Do not skip any step. Do not summarize. Execute each step in order.**

## Step 1: Active Read of SYSTEM.md
Read `SYSTEM.md` using the appropriate read tool for your environment. Pay attention to Hard Constraints, Standing Decisions, and Current Phase.

## Step 2: Active Read of AGENTS.md
Read `AGENTS.md` to understand the directory topology and boundaries.

## Step 3: Find What Changed Since Last Session
Find the last session date from `SYSTEM.md`. Then find files modified since that date.
- **If Obsidian MCP is available:** `obsidian_global_search(query=".", useRegex=true, modified_since="YYYY-MM-DD")`
- **If Git is available:** `git log -1 --before="YYYY-MM-DD" --format=%H` then run `git diff --name-status <hash>`
- **Fallback:** If neither is available, ask the user what files they modified recently.

## Step 4: Identify Session Type
Ask the user what type of session this is (e.g., Coding, Planning, Research, Maintenance).

## Step 5: Load Task-Specific Context
Based on the session type, load the files specified in `SYSTEM.md`'s "Task-Specific Context Loading" section.

## Step 6: Confirm Readiness
Tell the user what you found in the modified scan, what context you loaded, and that you are ready to start. Keep it brief.