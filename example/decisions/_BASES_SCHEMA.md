# Decision Records Schema

This schema is used by Obsidian Bases (or simple text search) to index ADRs and PDRs.

## YAML Template

Copy this frontmatter into every new decision record:

```yaml
---
doctype: ADR  # or PDR
id: ADR-T00X  # or PDR-P00X
domain: technical  # or product
status: accepted  # or rejected, deprecated, proposed
date: YYYY-MM-DD
tags: [kebab-case, list, of, topics]
constitution-clause: null  # or S1, P3, etc. if relevant
supersedes: null
superseded-by: null
---
```