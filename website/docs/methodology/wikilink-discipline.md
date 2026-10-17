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

- After creating or editing links, confirm the targets exist. An AI session can read each target path, or a script can check them in bulk.
- Directory paths don't resolve as notes. Link to the directory's README instead.
- Links to notes that don't exist yet are fine if flagged inline: *`[[future/note]] (does not exist yet — create when X happens)`*.

## Why It Matters

AI sessions often mention other work in prose (*"as discussed in the strategy doc"*) without linking. Those references don't appear in backlinks or graph view, and the [Reweave Protocol](reweave-protocol.md) can't find them.

The other protocols depend on links to find affected documents and connect claims to evidence.
