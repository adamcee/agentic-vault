# The Session Protocol

A fresh AI session has no memory of your project. Every session starts from zero. The session protocol is the boot sequence that gives it the context it needs.

## The Boot Sequence

Every substantive session begins with the same sequence:

1. **Read `SYSTEM.md`** (the entry-point document, referred to as `CLAUDE.md` or `GEMINI.md` in tool-specific rule files). This is the routing document — not an encyclopedia, not a marketing brief. Current phase, hard constraints, standing decisions, pointers to everything else.
2. **Read `AGENTS.md`** if present. The vault topology map — which directories hold what, which files are authoritative.
3. **Find modified files since last session.** A single search for recently-changed files catches anything added outside the routing doc's awareness. This is the step most often skipped, and the one that most often causes AI sessions to work from stale context.
4. **Load task-specific context.** Different tasks need different files. A strategy session needs the strategy docs and personas. A coding session needs the architecture doc and relevant ADRs. The routing doc tells the session which context to load for which kind of work.

## Why This Beats "Just Tell the AI What You Want"

The alternative to a boot sequence is explaining the project fresh in every chat. That works for small projects. It fails for anything larger, for three reasons:

- **The human explanation is always incomplete.** You will forget to mention the constraint you decided on two weeks ago. The AI will confidently propose the thing you already rejected.
- **The explanation is lossy.** Each retelling drops details. The project drifts away from its actual state with every session.
- **The explanation is expensive.** Every chat that re-establishes context burns time and tokens that could have gone into the actual work.

The boot sequence replaces the retelling with a read.

## The Routing Document Is Not an Encyclopedia

A common mistake is to let the entry-point document grow into a compendium — every decision, every research finding, every historical note. Don't. The file is a router. Keep it small.

- **Hard constraints.** The things no session is permitted to violate without a decision record.
- **Current phase.** What the project is actively working on.
- **Standing decisions.** The short list of locked-in choices.
- **Pointers.** Links to everywhere the detail actually lives.

Details belong in the documents themselves. The routing doc exists so a fresh session knows which documents to read. Once it grows past that job, it stops serving it.

## The Common Failure Mode

Most projects that try to give their AI persistent memory do so by pasting ever-larger blocks of context into the first message of every chat. It works for a while, then it doesn't — the context bloats, the AI's attention degrades, and the experience slowly worsens in a way that's hard to attribute. The boot sequence replaces the paste with a protocol. The protocol scales; the paste doesn't.

See also: [The SYSTEM.md Primacy](system-primacy.md) for the single-source-of-truth principle this sequence depends on.
