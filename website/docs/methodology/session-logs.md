# Session Logs

Every session that changes the vault leaves two records: one line in `session-history.md` and a short section in the week's implementation log. Both are append-only, so the next session, or you after a month away, can see exactly what happened.

## The Two Logs

- **`session-history.md`** has one `## YYYY-MM-DD` heading per date and one line per session: `- (agent, session type) what changed`. Its last heading is the date the [Session Protocol](session-protocol.md) uses to find recent changes.
- **`prototype/implementation-logs/YYYY-Www.md`** has one file per week, with a section per session listing what changed, decisions made, reweaves run, and action items sent to the ledger.

## Rules

- **Append, never rewrite.** Add entries with a single append (`>>` in a shell, or an MCP append). Rewriting a log lets two parallel sessions erase each other's entries.
- **Past weeks are closed.** A correction goes in the current week as a dated note, not into an old file.
- **Check at session close.** The template's `vault-lint.py` confirms the logs only grew, the headings are in order, and the weekly log agrees with the history.

## Two Task Lists

The AI writes action items only to `prototype/implementation-plan.md`, the ledger, while you curate your own working list in `prototype/human-task-list.md` by moving items from the ledger during a weekly review. The AI reads your list but never writes to it.
