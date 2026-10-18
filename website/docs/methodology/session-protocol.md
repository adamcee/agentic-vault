# The Session Protocol

Every substantive session starts with the same four steps, so a new session begins from the project's current state. Every session that changes the vault ends by appending to its [session logs](session-logs.md).

## The Steps

1. **Read `AGENTS.md`.** Tool-specific pointer files (`CLAUDE.md`, `GEMINI.md`) send the AI here. It holds the current phase, hard constraints, standing decisions, the directory map, and pointers to everything else.
2. **Find files changed since the last session.** The last `## YYYY-MM-DD` heading in `session-history.md` gives the date, and one `git diff` or `find` lists what changed since. This step is skipped most often, and skipping it is the usual cause of sessions working from stale context.
3. **Ask what kind of session this is**, such as planning, research, or coding.
4. **Load the context the task needs.** A coding session needs the design docs and relevant ADRs. A strategy session needs the strategy docs. `AGENTS.md` lists which files go with which kind of work.

The template's `vault-start` skill runs these steps as tool calls, so a session can't skip them by working from memory. Claude Code runs it automatically through `CLAUDE.md`, you can type `/vault-start`, and Gemini CLI can link the same skill; agents without skills follow the steps as written in `AGENTS.md`.

## Why Not Just Explain the Project Each Time

Explaining the project fresh in every chat works for small projects and fails for larger ones:

- **You leave things out.** You forget the constraint you set two weeks ago, and the AI proposes the option you already rejected.
- **Each retelling loses detail.** The project drifts away from its actual state.
- **It costs time and tokens** that could go to the work.

Pasting larger and larger context blocks into the first message has the same problem at a slower pace. The context bloats and the AI's attention degrades.

## Keep AGENTS.md Small

`AGENTS.md` routes a session to the right documents. It is not an archive. Keep it to:

- **Hard constraints** that no session may violate without a decision record.
- **The current phase.**
- **Standing decisions**, as a short list.
- **Pointers** to where the details live.

Once it grows past that, it stops doing its job.

See also [AGENTS.md Primacy](agents-md-primacy.md).
