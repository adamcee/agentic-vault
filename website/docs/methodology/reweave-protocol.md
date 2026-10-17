# The Reweave Protocol

When new evidence arrives, check it against the decisions it could affect. A decision made six weeks ago rested on six-week-old evidence, and it may no longer hold.

Without this step, new research sits in the vault unconnected to the decisions it bears on.

## Trigger

New research, competitive information, a strategy shift, or an outside event: anything that could change what you would decide today.

## Steps

1. **Find affected docs.** Search the vault for ADRs, PDRs, strategy, and architecture docs the new information touches. Ask of each: *"If this doc were written today, would its conclusions change?"*
2. **Classify the impact** on each affected doc:
    - **Strengthened.** Add a link to the new source in the doc's rationale.
    - **Weakened.** Write a dated note into the affected doc and flag it for human review. Backlinks show that two docs connect, but not that one now undercuts the other.
    - **Invalidated.** Don't change it silently. Flag it for human review and propose a superseding ADR or PDR.
3. **Record the triggers.** The new document gets a `## Reweave Triggers` section listing affected files, each with a one-line impact statement. If nothing is affected, say so.
4. **Route action items** to the implementation plan, not the research doc, and log the reweave in the week's implementation log.

**Backfill on touch:** any research doc you read in full or edit that lacks a `## Reweave Triggers` section gets one before the task closes.

## Relation to Decision Propagation

[Decision propagation](decision-records.md) pushes new decisions forward into the plan and the constitution, while reweave pulls new evidence back through existing decisions. Without reweave, the vault fills with decisions whose rationale no longer holds.

AI sessions tend to treat new research as standalone: they write the doc, cite its contents, and stop. Reweave is the step most often skipped.
