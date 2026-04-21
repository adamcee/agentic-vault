# The Reweave Protocol

A decision made six weeks ago rested on the evidence available six weeks ago. When new evidence arrives, that decision may no longer hold — but only if someone checks.

Without a protocol, new research sits in your vault disconnected from the decisions it affects. The reweave forces the connection.

## Trigger

New research, competitive intelligence, a strategy shift, an external event. Anything that could change what you would decide today.

## Steps

1. **Find affected docs.** Search the vault for ADRs, PDRs, strategy, and architecture docs the new info touches. The governing question: *"If this doc were written today, would its conclusions change?"*
2. **Classify the impact** for each affected doc:
    - **Strengthened** — add a link to the new source in the existing doc's rationale.
    - **Weakened** — add a note and link, flag for human review.
    - **Invalidated** — do not change silently. Flag for human review and propose a superseding ADR/PDR.
3. **Record the triggers.** The new document gets a `## Reweave Triggers` section listing affected files with one-line impact statements. If nothing is affected, say so explicitly.
4. **Route any action items** to the implementation plan, not the research doc.

## Why This Is Forward-Looking's Twin

[Decision Records](decision-records.md) push decisions forward into the plan and the constitution. Reweave pulls new evidence backward through the stack of existing decisions. Both are required. Forward propagation without reweave produces a vault that accumulates decisions it no longer believes in.

## The Common Failure Mode

AI sessions default to treating new research as standalone. They write the new doc, cite what's in it, and stop. The reweave step is the one most often skipped — and the one that keeps the vault honest over time.
