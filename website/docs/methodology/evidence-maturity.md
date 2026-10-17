# Evidence Maturity Tags

Each citation carries a tag stating how well established its evidence is. A thirty-year replicated finding and last month's preprint both belong in the vault, but they shouldn't carry the same weight.

## The Four Tags

| Tag | Meaning |
|---|---|
| `[established]` | 10+ years, extensively replicated, foundational to the field. |
| `[supported]` | Multiple studies and strong theoretical grounding, with less than a decade of replication. |
| `[emerging]` | A single study or very recent work, not yet replicated. |
| `[theoretical]` | A conceptual framework without direct empirical validation in this context. |

A fifth tag, `[secondary]`, marks AI-generated syntheses and literature reviews. It goes in the research doc's frontmatter, not inline.

## Usage

Tags appear inline next to the citation:

```
The protocol works in practice ([[research/source-name]] [supported]).
```

Tags also go in the research doc's YAML frontmatter (`evidence-maturity: supported`). You can then query the vault for every `[emerging]` claim when new replication evidence arrives.

## Why It Matters

If you treat a single new study like a thirty-year consensus, you make commitments the evidence can't support. If you cite only established work, you can't act on anything new.

The tags let you do both: an `[emerging]` citation can support a decision while marking it as a bet to revisit. When replication arrives, the [Reweave Protocol](reweave-protocol.md) finds the decisions that depended on the earlier study.

AI-written documents cite a meta-analysis and a conference abstract in the same confident tone. Tagging adds a human calibration step, and later sessions inherit it from the frontmatter.
