# Research Traceability

Every empirical claim in a decision document links to the vault research doc that supports it. Without these links, the [Reweave Protocol](reweave-protocol.md) is guesswork.

## The Rule

Link to the vault research doc, not the external paper. The vault doc already holds the relevant finding.

**Format:** `claim text ([[research/source-doc-name]] [evidence-tag])`

**Unsourced claims** get an `[unsourced]` flag so a later session can fill the gap. Never write a research doc from memory. Research docs must come from source material the session can read, such as a paper, report, or article, not from training data.

## Findings vs. Interpretations

Mark which is which.

- **Finding.** The source states the claim directly. Use a plain link.
- **Interpretation.** The claim applies the source to your project. Say so: *"we read this to mean X for our context ([[source]])"*.

## Primary vs. Secondary Sources

Prefer primary sources: a claim traced only to a secondary synthesis, such as an AI-generated literature review, is weaker. Mark it, for example `([[ai-report-...|secondary]])`, so a later session knows to look for the primary.

## Why It Matters

AI sessions often produce decision documents that read well and can't be checked. A claim like *"30 years of peer-reviewed validation"* looks authoritative until you try to verify it.

With evidence links, each decision either holds up under new evidence, gets reweighted, or gets superseded, and the path stays visible. Without them, decisions go stale unnoticed.

See also [Evidence Maturity Tags](evidence-maturity.md).
