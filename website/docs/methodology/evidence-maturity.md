# Evidence Maturity Tags

Not all research carries equal weight. A thirty-year replicated finding and a preprint from last month both deserve to be cited — and neither deserves to be cited the same way.

## The Four Tags

| Tag | Meaning |
|---|---|
| `[established]` | 10+ years, extensively replicated, foundational to the field. |
| `[supported]` | Multiple studies, strong theoretical grounding, less than a decade of replication. |
| `[emerging]` | Single study or very recent work. Promising but not yet replicated. |
| `[theoretical]` | Conceptual framework or design principle without direct empirical validation in this specific context. |

A fifth tag, `[secondary]`, marks AI-generated syntheses or literature reviews that are not primary sources. It goes in the research doc's frontmatter, not inline.

## Usage

Tags appear inline next to the citation:

```
The protocol works in practice ([[research/source-name]] [supported]).
```

Tags also go in the research doc's own YAML frontmatter (`evidence-maturity: supported`) so the vault can be queried for all `[emerging]` claims when new replication evidence arrives.

## Why This Matters

Your project will outlive any specific piece of evidence. A system that treats a single emerging study the same as a thirty-year consensus will make confident commitments it cannot keep. A system that refuses to cite anything that isn't established will never ship.

The tags let you do both. An `[emerging]` citation can anchor a decision, but the tag is a flag — *"this is a bet on early evidence; revisit when replication arrives."* When that replication does arrive, the [Reweave Protocol](reweave-protocol.md) can query the vault for every `[emerging]` claim that depended on the prior study and upgrade the tags or revisit the decisions.

## The Common Failure Mode

AI-generated documents treat every citation as equally authoritative. The model cannot tell a peer-reviewed meta-analysis apart from a conference abstract, because the training data treats all prose the same. The tag system forces a human-in-the-loop calibration step. Once the tags are on the frontmatter, future AI sessions inherit the calibration.
