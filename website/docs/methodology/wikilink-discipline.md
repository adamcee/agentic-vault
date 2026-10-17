# Wikilink Discipline

Every reference to another vault document is a wikilink. Links let humans and AI agents navigate the vault by following connections instead of running full-text searches.

A link costs seconds to add. A missing link costs a search every time someone needs that connection.

## What to Link

- **Empirical claims** link to the vault research doc that supports them (see [Research Traceability](research-traceability.md)).
- **Decision references** link to the specific ADR or PDR.
- **Terms** link to the concept note that defines them.
- **Other cross-references** link to the canonical location, not a vague description of it.

## What Not to Link

- A doc to itself.
- Common words that happen to match a filename.
- Text inside YAML frontmatter or code blocks.

## Verifying Links

A broken link points to a connection that doesn't exist, which is worse than no link.

- After creating or editing links, run the template's `vault-link-check.py` on the files you changed, or read each target path by hand.
- Directory paths don't resolve as notes. Link to the directory's README instead.
- Links to notes that don't exist yet go in `.link-check-ignore`, so the checker skips them and a periodic triage can clear them out.
- Once the checker reports zero broken links, keep it there; any new result is a regression.

## Why It Matters

AI sessions often mention other work in prose (*"as discussed in the strategy doc"*) without linking. Those references don't appear in backlinks or graph view, and the [Reweave Protocol](reweave-protocol.md) can't find them.

The other protocols depend on links to find affected documents and connect claims to evidence.
