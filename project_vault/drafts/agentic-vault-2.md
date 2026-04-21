# Sources and Further Reading

*Citations and references for the [whitepaper](index.md), organized by topic. Every source listed is one we actually consulted, not a training-data hallucination. Where an external link could change over time, we include a short note on what the source covers so the reference survives link rot.*

## On Decision Records

- **Michael Nygard**, [*Documenting Architecture Decisions*](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011). The original essay that formalized ADRs as a practice. The methodology's ADR format is a direct descendant.
- **Martin Fowler**, [*Documenting Architecture Decisions*](https://martinfowler.com/articles/2021-document-architecture.html) (2021). A widely-read treatment that expands on Nygard and situates ADRs within broader architectural documentation practice.
- **ADR GitHub community**, [adr.github.io](https://adr.github.io/). Collected templates, tooling, and variations. Useful for teams evaluating which ADR dialect to adopt.
- **Joel Parker Henderson**, [Architecture Decision Record templates](https://github.com/joelparkerhenderson/architecture-decision-record). A comprehensive reference collection of ADR templates and examples.

## On Zettelkasten and Linked Notes

- **Sönke Ahrens**, [*How to Take Smart Notes*](https://www.goodreads.com/book/show/34507927-how-to-take-smart-notes) (2017). The accessible English-language introduction to Luhmann's zettelkasten method. The methodology's concept notes and wikilink discipline are adapted from this tradition.
- **Niklas Luhmann**, [*Communicating with Slip Boxes*](https://luhmann.surge.sh/communicating-with-slip-boxes). The original short essay by Luhmann on his note-taking practice, translated into English.
- **Andy Matuschak**, [*Evergreen notes*](https://notes.andymatuschak.org/Evergreen_notes). A modern adaptation of zettelkasten for working research notes. Matuschak's broader site is itself an example of the form.

## On Writing Discipline

- **William Strunk Jr. and E. B. White**, [*The Elements of Style*](https://www.bartleby.com/141/) (1959 and later editions). The public-domain first edition by Strunk is available online; the White-extended edition is the one most widely read. The source of *"omit needless words,"* *"use the active voice,"* and the discipline of strong verbs over weak adjectives.
- **U.S. Marine Corps**, [*MCDP-7 Learning*](https://www.marines.mil/Portals/1/Publications/MCDP%207.pdf) (2020). The doctrine on learning in the USMC, which articulates the Commander's Intent principle used in the methodology's approach to `SYSTEM.md`.
- **U.S. Army**, [*AR 25-50 Preparing and Managing Correspondence*](https://armypubs.army.mil/ProductMaps/PubForm/Details.aspx?PRODUCT_ID=1004725). The formal regulation on BLUF (Bottom Line Up Front) writing for military correspondence.
- **Paul Graham**, [*Write Simply*](http://www.paulgraham.com/simply.html) (2021). A short essay on the ethics and practice of clear prose. Aligned with the methodology's writing discipline without overlapping in substance.

## On Evidence and Calibration

- **Philip Tetlock and Dan Gardner**, [*Superforecasting: The Art and Science of Prediction*](https://www.goodreads.com/book/show/23995360-superforecasting) (2015). On calibration as a practice — the habit of matching confidence to the evidence at hand rather than to the rhetorical weight of the claim.
- **John P. A. Ioannidis**, [*Why Most Published Research Findings Are False*](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124) (*PLOS Medicine*, 2005). The landmark paper on replication failure, which motivates the methodology's distinction between `[established]` and `[emerging]` evidence.
- **Open Science Collaboration**, [*Estimating the reproducibility of psychological science*](https://www.science.org/doi/10.1126/science.aac4716) (*Science*, 2015). Empirical evidence for the replication gap that the evidence-maturity tag system is designed to surface.

## On the AI Tooling Landscape

- **Anthropic**, [*Model Context Protocol*](https://modelcontextprotocol.io). The emerging open protocol for giving AI tools structured access to external resources. The methodology anticipates MCP as the standard transport layer for AI-to-vault communication.
- **Anthropic**, [*Claude Code documentation*](https://docs.claude.com/en/docs/claude-code/overview). The CLI-based AI coding tool that the methodology was extensively tested against.
- **Cursor**, [cursor.com](https://cursor.com). AI-native IDE that supports project-level rules files (`.cursorrules`) of the kind the methodology's Tier 2 installation relies on.
- **Windsurf**, [windsurf.com](https://windsurf.com). Another AI-native IDE with project rule support.
- **Obsidian**, [obsidian.md](https://obsidian.md). The primary markdown-based knowledge management tool the vault is designed for, though the methodology's file format is deliberately tool-independent.

## On Related Vault and Knowledge-Base Practices

- **Ars Contexta**, [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta). An AI-powered vault generator. Evaluated during the methodology's development; several practices (wikilink discipline, reweave) were cherry-picked and adapted.
- **Foam**, [foambubble.github.io/foam](https://foambubble.github.io/foam/). A personal knowledge management system built on VS Code. An earlier example of treating markdown notes as a first-class knowledge artifact.
- **TiddlyWiki**, [tiddlywiki.com](https://tiddlywiki.com). A long-standing self-contained wiki system. Predates most modern linked-notes tools and influenced many of the conventions the methodology uses.

## On AI Collaboration and Context Management

- **Anthropic**, [*Prompt engineering overview*](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview). The practical guide to effective prompting that underlies much of the methodology's assumptions about how to communicate with AI models.
- **Simon Willison**, [*Things I've learned about working with LLMs*](https://simonwillison.net/tags/llms/). A running log of practical observations on working with large language models. Not cited in any specific protocol, but consistently useful as a reality-check on what these tools can and cannot do.
- **Andrej Karpathy**, various Twitter threads on LLM-assisted software development. The idea of *"English is the new programming language"* and the associated observations about natural language as a high-level interface to compiled neural networks informs the methodology's treatment of prompts as code.

## On Project-Specific Research (Chameleon)

*These sources were consulted during the field test described in the whitepaper. They are listed here for readers who want to see the kind of research base the methodology is designed to accumulate and maintain.*

- **Albert T. Corbett and John R. Anderson**, [*Knowledge tracing: Modeling the acquisition of procedural knowledge*](https://link.springer.com/article/10.1007/BF01099821) (*User Modeling and User-Adapted Interaction*, 1994). The original Bayesian Knowledge Tracing paper. Still the foundation for most deployed knowledge-tracing systems thirty years later — an `[established]` citation in the methodology's own usage.
- **Sidney D'Mello and Arthur Graesser**, [*Dynamics of affective states during complex learning*](https://www.sciencedirect.com/science/article/abs/pii/S095947521100069X) (*Learning and Instruction*, 2012). Foundational work on the emotional states that arise during learning with intelligent tutoring systems.
- **Paulo Freire**, [*Pedagogy of the Oppressed*](https://www.goodreads.com/book/show/72657.Pedagogy_of_the_Oppressed) (1968). The philosophical foundation for the methodology's commitment to *contestability* — the idea that the system's representation of the learner must be open to correction by the learner.
- **Edward Deci and Richard Ryan**, [*Self-Determination Theory*](https://selfdeterminationtheory.org/). The ongoing research program on autonomy, competence, and relatedness as the foundations of motivation. Informs the methodology's treatment of personas and the design of learning interactions in the Chameleon field test.
- **Benjamin S. Bloom**, [*The 2 Sigma Problem*](https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf) (1984). The origin of the standing goal in educational technology: if one-to-one human tutoring produces two standard deviations of improvement over classroom instruction, what would it take to approximate that at scale? The methodology's field test project is one attempt at an answer.

*Detailed research notes and full citations for the Chameleon-specific work live in the project vault. The project site itself is at [chameleon.ai](https://chameleon.ai) (if launched) or will be announced there when it is.*

---

## How to Suggest Additions

If you believe something important is missing from this list — particularly on prior art for AI-assisted long-form work or for vault methodologies we should engage with — the best path is to open an issue on the [agentic-vault GitHub repository](https://github.com/adamcee/agentic-vault/issues) with the reference and a short note on what it covers.
