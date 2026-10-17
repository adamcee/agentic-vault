# Sources and Further Reading

*Citations for [Design & Goals](design-and-goals.md), by topic. Each entry includes a note on what the source covers, so the reference stays useful if the link breaks.*

## On Decision Records

- **Michael Nygard**, [*Documenting Architecture Decisions*](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011). The original essay on ADRs. The vault's ADR format descends from it.
- **Martin Fowler**, [*Documenting Architecture Decisions*](https://martinfowler.com/articles/2021-document-architecture.html) (2021). Expands on Nygard and places ADRs within broader architecture documentation.
- **ADR GitHub community**, [adr.github.io](https://adr.github.io/). Templates, tooling, and variations of the ADR format.
- **Joel Parker Henderson**, [Architecture Decision Record templates](https://github.com/joelparkerhenderson/architecture-decision-record). A collection of ADR templates and examples.

## On Zettelkasten and Linked Notes

- **Sönke Ahrens**, [*How to Take Smart Notes*](https://www.goodreads.com/book/show/34507927-how-to-take-smart-notes) (2017). An English introduction to Luhmann's zettelkasten method. The vault's concept notes and wikilink discipline come from this tradition.
- **Niklas Luhmann**, [*Communicating with Slip Boxes*](https://luhmann.surge.sh/communicating-with-slip-boxes). Luhmann's short essay on his note-taking practice, in English translation.
- **Andy Matuschak**, [*Evergreen notes*](https://notes.andymatuschak.org/Evergreen_notes). A modern adaptation of zettelkasten for research notes. Matuschak's site is itself an example.

## On Writing Discipline

- **International Organization for Standardization**, [*ISO 24495-1:2023 Plain language — Part 1: Governing principles and guidelines*](https://www.iso.org/standard/78907.html) (2023). The international plain language standard. Its four principles (relevant, findable, understandable, usable) frame the vault's writing rules.
- **William Strunk Jr. and E. B. White**, [*The Elements of Style*](https://www.bartleby.com/141/) (1959 and later editions). Strunk's first edition is public domain and online; the edition expanded by White is the most widely read. Source of *"omit needless words"* and *"use the active voice."*
- **U.S. Marine Corps**, [*MCDP-7 Learning*](https://www.marines.mil/Portals/1/Publications/MCDP%207.pdf) (2020). USMC doctrine on learning, cited for Commander's Intent.
- **U.S. Army**, [*AR 25-50 Preparing and Managing Correspondence*](https://armypubs.army.mil/ProductMaps/PubForm/Details.aspx?PRODUCT_ID=1004725). The Army regulation for military correspondence, including Bottom Line Up Front (BLUF).
- **Paul Graham**, [*Write Simply*](http://www.paulgraham.com/simply.html) (2021). A short essay on writing plainly.

## On Evidence and Calibration

- **Philip Tetlock and Dan Gardner**, [*Superforecasting: The Art and Science of Prediction*](https://www.goodreads.com/book/show/23995360-superforecasting) (2015). On calibration: matching confidence to the evidence rather than to how persuasive a claim sounds.
- **John P. A. Ioannidis**, [*Why Most Published Research Findings Are False*](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124) (*PLOS Medicine*, 2005). The paper on replication failure behind the distinction between `[established]` and `[emerging]` evidence.
- **Open Science Collaboration**, [*Estimating the reproducibility of psychological science*](https://www.science.org/doi/10.1126/science.aac4716) (*Science*, 2015). Evidence for the replication gap that maturity tags are meant to expose.

## On AI Tools

- **Anthropic**, [*Model Context Protocol*](https://modelcontextprotocol.io). An open protocol that gives AI tools structured access to external resources, including a vault.
- **Anthropic**, [*Claude Code documentation*](https://docs.claude.com/en/docs/claude-code/overview). A CLI coding agent the vault was tested with.
- **Cursor**, [cursor.com](https://cursor.com). An AI IDE with project rules files (`.cursorrules`), used by Tier 2 setup.
- **Windsurf**, [windsurf.com](https://windsurf.com). An AI IDE with project rules files.
- **Obsidian**, [obsidian.md](https://obsidian.md). The markdown editor the vault is designed around. The file format works in any editor.

## On Related Vault and Knowledge-Base Practices

- **Ars Contexta**, [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta). An AI vault generator. Wikilink discipline and reweave were adapted from it.
- **Foam**, [foambubble.github.io/foam](https://foambubble.github.io/foam/). A note system built on VS Code that treats linked markdown notes as the primary record.
- **TiddlyWiki**, [tiddlywiki.com](https://tiddlywiki.com). A self-contained personal wiki that predates most linked-note tools.

## On AI Collaboration and Context Management

- **Anthropic**, [*Prompt engineering overview*](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview). Anthropic's prompting guide.
- **Simon Willison**, [*Things I've learned about working with LLMs*](https://simonwillison.net/tags/llms/). A running log of practical notes on working with LLMs. Not cited by any protocol.
- **Andrej Karpathy**, posts on LLM-assisted software development. His line *"the hottest new programming language is English"* informs the vault's treatment of prompts as code.

---

## Suggest an Addition

To suggest a missing source, especially prior art on AI-assisted long-form work, open an issue on the [agentic-vault repository](https://github.com/adamcee/agentic-vault/issues) with the reference and a short note on what it covers.
