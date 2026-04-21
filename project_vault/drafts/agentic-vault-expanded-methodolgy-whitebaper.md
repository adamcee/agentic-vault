# Agentic Vault — Expanded Methodology + Whitepaper

Drop for `adamcee/agentic-vault`. Two deliverables:

1. **`methodology/`** — eight new markdown pages that extend the existing `website/docs/methodology/` section. Each page is short, matches the site's existing voice, and opens with a concrete failure mode before presenting the protocol. Designed to drop into `website/docs/methodology/` and be added to `mkdocs.yml` nav.
2. **`whitepaper/`** — long-form synthesis (`whitepaper.md`) plus supporting citation file (`sources.md`). Designed to live at `website/docs/whitepaper/` or to be exported as a downloadable PDF.

## Integration

### Add the new methodology pages to mkdocs.yml

The existing nav has three methodology pages. Add the new ones after them:

```yaml
  - The Methodology:
    - methodology/system-primacy.md
    - methodology/decision-records.md
    - methodology/writing-discipline.md
    # new pages below
    - methodology/reweave-protocol.md
    - methodology/research-traceability.md
    - methodology/evidence-maturity.md
    - methodology/wikilink-discipline.md
    - methodology/ideas-lifecycle.md
    - methodology/ingestion-gate.md
    - methodology/personas-as-constraint.md
    - methodology/session-protocol.md
  - Whitepaper:
    - whitepaper/index.md
    - whitepaper/sources.md
```

### On voice

The existing pages are ~100–300 words, BLUF, no filler. The new pages match that. They are not marketing copy. They describe failure modes in terms anyone who has used AI for real work will recognize.

### On positioning

Every page leads with the problem, not the solution. The word "agentic" does not appear in the page bodies — it's in the repo name, that's enough. The framing throughout is: *AI has a memory problem; here is the protocol that handles it.*

### On attribution

The methodology was developed in building Chameleon (an adaptive learning platform, `chameleon.ai`). The whitepaper cites Chameleon as the field test where these protocols earned their keep. That's honest and gives readers a concrete anchor for what the protocols actually look like under load.

### On Gemini handoff

The whitepaper is structured so that Gemini can expand each section independently. Every section has a stable heading and explicit links into the methodology pages. If Gemini is asked to produce a deeper version of any section, the section's existing structure and citations should be preserved — Gemini should extend, not rewrite.
