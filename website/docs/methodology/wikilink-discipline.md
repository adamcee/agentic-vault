# Wikilink Discipline

Every claim that rests on another vault document links to it. This is not decoration. It is how the vault remains navigable as it grows.

## The Compounding Investment

The cost of adding a link is near-zero. The cost of *not* adding it accumulates every week. A well-linked vault can be traversed by following connections — both by humans browsing and by AI agents searching for context. A poorly-linked vault requires full-text search for everything, which is slow for humans and expensive for AI.

## What to Link

- **Empirical claims** → the vault research doc that supports them (see [Research Traceability](research-traceability.md)).
- **Decision references** → the specific ADR or PDR.
- **Concept mentions** → the concept note that defines the term.
- **Cross-document references** → the canonical location, not a vague description of it.

## What Not to Link

- Self-links. A doc should not link to itself.
- Generic English words that happen to match a filename.
- Content inside YAML frontmatter or code blocks.

## Link Verification

A broken link is worse than no link — it signals a connection that doesn't exist.

- After creating or editing links, verify the targets resolve. AI sessions can read the target path to confirm. Batch verification scripts work too.
- Directory paths do not resolve as notes. Link to the directory's README instead.
- Intentional forward-references (linking a note that doesn't exist yet) are acceptable if flagged inline: *`[[future/note]] (does not exist yet — create when X happens)`*.

## The Common Failure Mode

AI sessions produce documents that reference other work in prose (*"as discussed in the strategy doc"*) without actually linking. These references are invisible to the graph. They do not surface in backlink queries, do not traverse in graph view, do not survive the [Reweave Protocol](reweave-protocol.md). A reference without a link is a claim that can't be followed.

Wikilinks are what make every other protocol in this methodology possible.
