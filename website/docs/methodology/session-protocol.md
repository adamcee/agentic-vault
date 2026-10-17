# The Session Protocol

Every substantive session starts with the same four steps, so a new session begins from the project's current state.

## The Steps

1. **Read `SYSTEM.md`.** Tool-specific pointer files (`CLAUDE.md`, `GEMINI.md`) send the AI here. It holds the current phase, hard constraints, standing decisions, and pointers to everything else.
2. **Read `AGENTS.md`** if present. It maps which directories hold what and which files are authoritative.
3. **Find files changed since the last session.** One search catches work done outside the master file's awareness. This step is skipped most often, and skipping it is the usual cause of sessions working from stale context.
4. **Load the context the task needs.** A coding session needs the architecture docs and relevant ADRs. A strategy session needs the strategy docs. `SYSTEM.md` lists which files go with which kind of work.

## Why Not Just Explain the Project Each Time

Explaining the project fresh in every chat works for small projects and fails for larger ones:

- **You leave things out.** You forget the constraint you set two weeks ago, and the AI proposes the option you already rejected.
- **Each retelling loses detail.** The project drifts away from its actual state.
- **It costs time and tokens** that could go to the work.

Pasting larger and larger context blocks into the first message has the same problem at a slower pace. The context bloats and the AI's attention degrades.

## Keep SYSTEM.md Small

`SYSTEM.md` routes a session to the right documents. It is not an archive. Keep it to:

- **Hard constraints** that no session may violate without a decision record.
- **The current phase.**
- **Standing decisions**, as a short list.
- **Pointers** to where the details live.

Once it grows past that, it stops doing its job.

See also [SYSTEM.md Primacy](system-primacy.md).
