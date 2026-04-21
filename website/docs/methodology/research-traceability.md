# Research Traceability

Every empirical claim in a decision document must link to the specific research doc that supports it. Without traceability, the [Reweave Protocol](reweave-protocol.md) is guesswork.

## The Norm

When a decision cites evidence, link to the vault research doc — not the external paper. The vault doc is where the relevant finding is already extracted and summarized.

**Format:** `claim text ([[research/learning-science/source-doc-name]] [evidence-tag])`

**Unsourced claims** get flagged with `[unsourced]` so a future session can fill the gap. Do not create a research doc from memory. Research docs must be based on actual source material — a paper, a report, an article the session has access to. Never training data.

## Findings vs. Interpretations

Be explicit about which is which.

- **Finding** — the source directly states the claim. Plain link.
- **Inference** — the claim is your interpretation of the source for your project's context. Say so: *"we interpret this to mean X for our context ([[source]])"*.

## Primary vs. Secondary Sources

Prefer primary. A claim traced only to a secondary synthesis (e.g., an AI-generated literature review) is weaker than one traced to the original paper. When only a secondary exists, mark it: `([[gemini-report-...|secondary]])` so a future session knows to look for the primary.

## The Common Failure Mode

AI sessions routinely produce decision documents that read well but cannot be audited. A claim like *"30 years of peer-reviewed validation"* looks authoritative until you try to verify it. Traceability turns the claim into something a future session (human or AI) can actually check.

This is the mechanism that lets your vault degrade gracefully. Decisions documented without evidence links rot invisibly. Decisions with evidence links either hold up under new evidence (strengthened), get reweighted (weakened), or get superseded (invalidated) — but the path is always visible.

See also: [Evidence Maturity Tags](evidence-maturity.md) for how to calibrate confidence in the evidence itself.
