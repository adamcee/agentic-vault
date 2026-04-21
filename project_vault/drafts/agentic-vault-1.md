# The Agentic Vault: A Methodology for Building Long-Lived Projects with AI

*A practical framework for using AI as a persistent thought partner on work that lasts longer than a single chat.*

---

## Abstract

AI models are powerful thought partners with a specific failure mode: they forget. Every new conversation starts from zero. On projects that last longer than a single session — a product, a piece of software, a book, a research thread — this produces a predictable pattern of degradation. Decisions get relitigated. Rejected ideas resurface. The rationale behind choices is lost. Work that should compound instead churns.

The Agentic Vault is a methodology for using AI on projects where this cost is unacceptable. It treats the project folder, not the chat window, as the single source of truth. A small set of protocols handles the specific failure modes that appear when AI is used heavily over time: context rot, decision drift, evidence gaps, prose degradation, and relitigation.

This document describes the methodology, the failure modes that motivated it, the research it rests on, and the field test where it was developed and refined. It does not claim the methodology is finished. It does claim that every protocol in it was written in response to a specific recurring problem, and that the problems are ones anyone using AI heavily on a long-lived project will eventually encounter.

---

## 1. The Problem Space

### 1.1. What AI Does Well

Large language models are extraordinary at short-horizon intellectual work. Within a single conversation, they can reason across domains, hold many constraints in mind, produce drafts faster than any human collaborator, and engage as a thought partner at a quality that was unavailable at any price five years ago.

This is not the problem.

### 1.2. What AI Does Badly

The problem is what happens between conversations.

Every chat starts from zero. The model has no memory of what you decided yesterday, what you rejected last week, what evidence you based the architecture on, or what the project is even trying to do. Each session must be re-briefed, and the briefing is always incomplete.

On a short task, this is trivial. On a long project, the costs compound:

- **Relitigation.** The model suggests the same idea every few weeks because it has no record of the previous rounds of thinking. You end up re-explaining why MongoDB is not a fit, why the multi-agent approach was rejected, why you chose one framework over another. The conversation never moves forward because every session starts over.
- **Decision drift.** Standing commitments quietly erode. The model, asked to solve a problem, reaches for whatever pattern is most common in its training data — which may contradict a choice you made deliberately two months ago. Without a protocol, these contradictions land in the work without anyone noticing until much later.
- **Evidence gaps.** The model can generate a confident-sounding rationale for almost any position. On any given day, it will cite plausible-sounding research that does not exist. Without a protocol for tracing claims to actual sources, your project accumulates a quiet debt of unverified assertions that future work rests on.
- **Prose degradation.** AI output has a characteristic prose pattern — hedge-phrases, meta-commentary, reified abstractions, paragraph bloat. When AI output is admitted into project documents without tightening, that prose becomes the corpus future AI sessions read. The rot is self-reinforcing.
- **Context rot.** As a session runs longer or documents grow, the model's attention degrades. Critical information at the top of a file gets weighted less than recent chatter. By the time you notice, the session is producing work that contradicts the foundation it was given.

These are not speculative problems. They are the day-to-day experience of anyone using AI heavily for real work.

### 1.3. The Partial Solutions That Don't Work

Several obvious solutions have been tried. Each of them solves part of the problem and leaves the rest.

- **Longer context windows.** Modern models can accept hundreds of thousands of tokens. This makes the context-paste workflow survive longer before degrading, but it does not change the underlying failure. Attention still decays across a long context. Pasting the whole project into every chat costs time, tokens, and quality — and it still loses the graph structure that makes a project navigable.
- **Vendor memory features.** Most major AI tools now offer some form of persistent memory. These help with personal facts ("I live in Chicago") and are actively harmful for project memory. They summarize across sessions, which is exactly wrong for a project where the specifics of a decision — which alternatives were considered, why they were rejected — are the point. A summary of *"we decided to use Postgres"* is worthless. The rejected alternatives are what prevent the question from coming back.
- **Chat history search.** Searching old conversations for the decision you half-remember making is better than nothing and worse than writing it down. The signal-to-noise ratio is terrible. And the decisions you most need to find are the ones that were casual at the time and proved load-bearing later — exactly the ones no search query will surface.
- **Custom GPTs / project-scoped assistants.** These inject a fixed instruction set at session start. They help, but they are owned by a single vendor, they don't persist your actual project state, and they don't compose with other tools. The same project used in Claude, Gemini, Cursor, and an IDE plugin needs four separate configurations.

None of these are wrong. They are incomplete. They address the surface of the problem — *how does the AI know what I told it before?* — without addressing the deeper one: *how does a project accumulate memory that survives the specific session and the specific tool?*

### 1.4. The Underlying Principle

The methodology rests on a single observation. If the AI forgets but the project folder does not, the project folder is where the memory has to live.

Everything else follows from this. If memory lives in the folder, the AI has to read from the folder at session start. If the folder is where decisions are recorded, the format of those records matters. If the records need to be updated when evidence changes, there need to be protocols for that. If multiple AI tools are used against the same project, they all have to share the folder. The methodology is the set of protocols that make this work in practice.

## 2. The Core Protocols

The methodology is a small number of protocols, each addressing one failure mode from the previous section. Every protocol was written in response to a specific recurring problem, not as an abstract principle.

### 2.1. SYSTEM.md Primacy — The Single Source of Truth

**The failure mode:** A project used across multiple AI tools (one for planning, one for coding, one for research) accumulates drift. Each tool has its own configuration. Each configuration falls out of date at a different rate. The project's ground truth ends up scattered across three or four files that nobody updates together.

**The protocol:** One file, referred to as `SYSTEM.md` (or tool-specific equivalents like `CLAUDE.md`, `GEMINI.md`, `.cursorrules`), is the authoritative project context. Tool-specific rule files are thin pointers that route the AI to read `SYSTEM.md` first. When the project's context needs to change, it changes in one place.

This is described in more detail on [The SYSTEM.md Primacy](../methodology/system-primacy.md) page. The underlying idea — that long-lived artifacts require a single authoritative source — predates the methodology. It comes from the software engineering literature on configuration management, from the editorial practice of style guides, and from the military doctrine of Commander's Intent: one authoritative statement of the objective, referenced by every downstream order.

### 2.2. The Session Protocol — The Boot Sequence

**The failure mode:** Fresh sessions start from zero. Without a protocol, the human re-explains the project in every chat, the explanation is always incomplete, and the project slowly drifts from the human's explanation rather than from its actual state.

**The protocol:** Every substantive session begins with the same boot sequence. Read `SYSTEM.md`. Read the topology map. Find files modified since last session. Load the task-specific context for whatever work is being done now. The details are in [The Session Protocol](../methodology/session-protocol.md).

The boot sequence replaces the ad-hoc re-explanation with a reliable read. It scales; the explanation does not.

### 2.3. Decision Records — ADRs and PDRs

**The failure mode:** A project accumulates decisions informally, in chat logs and half-remembered conversations. Three weeks later, the rationale is gone. The AI proposes the rejected alternative because nothing in the project state says it was rejected.

**The protocol:** Important decisions are recorded in formal documents in a `decisions/` directory. Architecture Decision Records (ADRs) capture technical choices. Product Decision Records (PDRs) capture product and design choices. Each record includes context, the decision itself, alternatives considered, and consequences. Rejected decisions get recorded too — often in a `rejected/` subdirectory — precisely so they cannot be accidentally revived.

The format is adapted from a widely-used practice in software engineering, formalized by Michael Nygard in his essay ["Documenting Architecture Decisions" (2011)](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) and popularized through [Martin Fowler's writing on ADRs](https://martinfowler.com/articles/2021-document-architecture.html) and the [adr.github.io community resources](https://adr.github.io/). The methodology extends the practice in three ways: it adds PDRs for product-side decisions, it makes rejection a first-class artifact rather than an implicit absence, and it integrates the records with the other protocols (propagation, reweave, traceability) so that the records are active rather than archival.

See [Decision Records (ADRs/PDRs)](../methodology/decision-records.md) for the site's short-form treatment.

### 2.4. Decision Propagation — Forward Consistency

**The failure mode:** A decision is made, an ADR is written, and the decision exists nowhere else. The implementation plan doesn't reflect it. The project's routing document doesn't mention it. Future sessions, reading the plan or the routing doc, have no idea the decision exists. The decision is *orphaned*.

**The protocol:** A new decision is not complete when the ADR is written. It is complete when the decision has been pushed into every document that should reflect it — the implementation plan, the constitution of invariants, the routing document. This is the Decision Propagation Protocol. It is a small checklist, run at the end of every decision, that prevents orphaning.

### 2.5. The Reweave Protocol — Backward Consistency

**The failure mode:** New evidence arrives. A research paper, a competitive development, a change in external conditions. The new evidence enters the project but does not touch the decisions it should affect. Six months later, you are operating on decisions whose rationale no longer holds, because nobody checked.

**The protocol:** When new information enters the vault, run the [Reweave Protocol](../methodology/reweave-protocol.md). Find the decisions the new information touches. Classify each — strengthened, weakened, or invalidated. Add links. For invalidations, propose a superseding decision record.

Decision Propagation pushes decisions forward into the project. The Reweave Protocol pulls new evidence backward through the stack of existing decisions. Both are required. A project with one but not the other accumulates commitments it no longer believes in.

### 2.6. Research Traceability — Evidence-Linked Claims

**The failure mode:** A decision document says *"thirty years of peer-reviewed validation."* It sounds authoritative. It cannot be audited. When new evidence arrives that contradicts the claim, there is no way to find the decisions that depended on the old evidence.

**The protocol:** Every empirical claim in a decision document links to the specific research document in the vault that supports it. Unsourced claims are explicitly flagged `[unsourced]` rather than hidden. The full protocol is on [Research Traceability](../methodology/research-traceability.md).

The practice is adapted from academic citation norms and from the more specific norms of systematic review methodology, where claim-to-source traceability is the precondition for reproducibility. It is also connected to the broader practice of *epistemic hygiene* in organizations — the idea, articulated in various forms by writers on forecasting and decision-making (Philip Tetlock's work on calibration, the AI alignment community's writing on belief propagation), that beliefs are only as good as the evidence they can be traced to.

### 2.7. Evidence Maturity Tags — Calibrating Confidence

**The failure mode:** AI-generated documents treat every citation as equally authoritative. A thirty-year replicated meta-analysis and a conference-abstract preprint get the same grammatical treatment. The result is false confidence on positions that rest on thin evidence.

**The protocol:** Every citation gets a maturity tag. `[established]`, `[supported]`, `[emerging]`, `[theoretical]`. Tags appear inline with the citation and in the research doc's YAML frontmatter. Full detail on [Evidence Maturity Tags](../methodology/evidence-maturity.md).

The four-level tagging scheme is a compromise. More granularity would be harder to apply consistently; fewer levels would collapse meaningful distinctions. Four levels force the person tagging to make a judgment that's usable — is this a foundational finding, or a promising lead, or a framework without direct evidence in this context? — without demanding a formal meta-analysis for every citation.

### 2.8. Wikilinks — The Connective Tissue

**The failure mode:** Documents reference each other in prose but don't link. The cross-references are invisible to the project's graph structure. Backlink queries miss them. The project accumulates the form of a knowledge base without the navigability of one.

**The protocol:** Every reference to another vault document is a wikilink, not a prose mention. See [Wikilink Discipline](../methodology/wikilink-discipline.md).

Wikilinks are what make every other protocol in the methodology possible. The Reweave Protocol depends on links to find affected docs. Research Traceability depends on links to connect claims to evidence. Decision Propagation depends on links to confirm decisions have been pushed into the docs that need them. A project without link discipline is a project where the protocols degrade to full-text search, which is slow for humans and expensive for AI.

### 2.9. The Ingestion Gate — Keeping AI Prose Out of the Corpus

**The failure mode:** AI-generated content gets pasted directly into the vault. The prose carries AI writing patterns — hedge-phrases, reified observations, paragraph bloat. Over time, the vault's voice drifts toward the average AI-generated document. Future AI sessions read that prose as the project's voice and produce more of it. The rot is self-reinforcing.

**The protocol:** AI-generated content lands in `drafts/` first. Nothing moves into the main vault until it passes a tightening checklist. The full rule is on [The Ingestion Gate](../methodology/ingestion-gate.md).

The underlying writing discipline — BLUF, paragraph ban, no meta-commentary, no reification — is described on [AI Writing Discipline](../methodology/writing-discipline.md). It is not invented. It is synthesized from three existing traditions:

- **Strunk & White's *The Elements of Style*** — active voice, omit needless words, concrete nouns and strong verbs. The 1959 text is still the shortest route to prose that can survive heavy reading.
- **USMC operational writing doctrine** — Bottom Line Up Front (BLUF), Commander's Intent, tactical brevity. The doctrine is documented in [MCDP-7 (*Learning*)](https://www.marines.mil/Portals/1/Publications/MCDP%207.pdf) and the joint military-correspondence style guides.
- **Engineering communication practice** — the idea, widely held in software engineering, that documents are read under load and must surface the critical information first.

The synthesis is not academic. The rules were adopted because they made AI output legible and kept AI sessions from re-contaminating the vault with their own worst habits.

### 2.10. The Ideas Lifecycle — A Home for Raw Thought

**The failure mode:** A project accumulates ideas faster than it can evaluate them. The ones that aren't ready for a decision record die in chat logs. The same half-formed ideas resurface every few weeks because nobody wrote down the last round of thinking.

**The protocol:** An `ideas/` directory holds lightweight notes — a name, a date, a few sentences — for ideas that aren't yet ready for formal evaluation. Each idea has a `resolved-by` field that tracks what happened: promoted to a decision record, rejected, absorbed into another doc, or still open. Details on [The Ideas Lifecycle](../methodology/ideas-lifecycle.md).

The directory is the shortest-form memory in the methodology. It costs almost nothing to maintain and prevents the single most common form of relitigation.

### 2.11. Personas as Design Constraint

**The failure mode:** Personas written as marketing artifacts — a stock photo, a name, a list of demographics — cannot be used to reject design decisions. Any option can be justified against a vague persona. The persona document exists but does no work.

**The protocol:** Personas are written with enough specificity that a design question can actually be answered against them. The wound is named concretely. The hidden competence is named. The affective signals are named. The resulting persona is a test case the design has to pass, not a reference for the pitch deck. Detail on [Personas as Design Constraint](../methodology/personas-as-constraint.md).

This is the most project-specific of the protocols. On some projects (pure infrastructure, tooling), personas aren't the right unit and a different design constraint serves the same function. The generalization is: *the project needs a concrete target it can test decisions against, specific enough to reject options with.*

## 3. The Philosophy

The protocols above are mechanics. Underneath them is a small set of commitments about how to use AI on work that matters.

### 3.1. The Project Folder as the Primary Artifact

In a typical AI workflow, the conversation is the primary artifact. The chat window is where the work happens; the files are where the work ends up. The methodology inverts this. The files are where the work accumulates; the chat is the ephemeral layer that moves work between the human and the files.

This inversion has concrete consequences. It means formatting the files for machine-parseability, not just human reading. It means writing documents to be re-read by a stranger (the next session's AI), not to be understood by a reader who already has the context. It means treating the file structure itself as part of the project, not as administrative overhead.

The idea is not new. It is the same logic that makes software source code, not build artifacts, the primary engineering artifact — and that makes a lab notebook, not a particular experiment, the primary scientific artifact. Long-lived work lives in the accumulating record, not in any particular session with the record.

### 3.2. Decisions Over Opinions

An AI will cheerfully offer an opinion on any question. This is a feature, not a bug — the ability to reason across domains is exactly what makes AI useful. But opinions are cheap, and a project that accumulates opinions without decisions accumulates noise.

The methodology distinguishes. An opinion is something the AI said in a chat. A decision is something that has been written down, with rationale and rejected alternatives, in the project's decisions directory. Opinions are temporary; decisions are structural. A decision can be revisited — through the Reweave Protocol — but it cannot be quietly undone.

This is adapted directly from the practice of decision records in software engineering, but the principle is broader. The distinction between *considered* and *committed* is the distinction that makes a project navigable. Without it, every open question stays open forever.

### 3.3. Evidence Over Authority

An AI will write authoritative-sounding prose about anything. The methodology's response to this is not to distrust the AI. The response is to require that claims be traceable, so that trust can be placed in the evidence rather than in the tone.

This is the principle behind [Research Traceability](../methodology/research-traceability.md) and [Evidence Maturity Tags](../methodology/evidence-maturity.md). An unsourced claim is not automatically wrong — but it is flagged as unsourced, so future sessions know they are reading a claim that has not yet been connected to evidence. An `[emerging]` citation is not automatically unreliable — but the tag marks it as a bet that should be revisited when replication arrives.

The underlying commitment is that the project's confidence should match the evidence, not the prose style.

### 3.4. The Vault as Contract

The protocols together constitute an implicit contract between the human and every AI session that touches the project. The human agrees to maintain the vault — write the decision records, run the protocols, tighten the drafts. The AI agrees to read the vault first, respect the standing decisions, propose superseding records rather than silently contradicting, and route its own output through the tightening checklist.

This works because both sides get something from it. The human gets a project that compounds rather than churns. The AI gets a context that lets it contribute high-quality work rather than low-quality work. Neither side is doing the other a favor. The contract is the mechanism that lets both sides do their part of the work well.

### 3.5. Graceful Degradation

Not every project can afford every protocol. A small project does not need ADRs for every decision. A short-lived experiment does not need the full reweave discipline. The methodology is designed to degrade gracefully — to be useful at small scale and still be useful at larger scale.

The installation guide captures this with three tiers:

- **Tier 1 (web app user).** Copy the template. Fill out `SYSTEM.md`. Paste it as the first message of every chat.
- **Tier 2 (IDE prosumer).** Scaffold the vault. The included rules files route the IDE's AI to read `SYSTEM.md` automatically.
- **Tier 3 (CLI power user).** Full vault with all protocols. CLI agents read the routing docs at every session start. The vault becomes the authoritative state.

A project can start at Tier 1 and upgrade as it grows. Protocols can be adopted incrementally — start with decision records, add reweave when the project gets big enough that decisions need to be reconsidered, add research traceability when external evidence starts driving the work. The methodology is not all-or-nothing.

## 4. The Field Test

The methodology was developed while building Chameleon, an adaptive learning platform for adults with math anxiety in workforce reskilling contexts. This was not a toy project. It involved thirty-plus decision records, hundreds of research documents, four stack pivots, and sustained AI collaboration across Claude, Gemini, and multiple IDE-based tools over roughly a year.

Several protocols in this methodology were not in the initial plan. They were written in response to specific failures:

- **The Ingestion Gate** was added after a vault audit found that roughly forty percent of writing-discipline violations originated from AI-generated research reports that had been admitted without tightening.
- **Evidence Maturity Tags** were added after a decision was made citing a single emerging study with the same grammatical weight as an established meta-analysis. The tag system forced the kind of calibration that prevented the same mistake twice.
- **The Ideas Lifecycle** was added after noticing that the same product ideas were being proposed across sessions because there was nowhere to record the previous round of thinking.
- **The Reweave Protocol** was added after new research arrived that should have updated a prior decision and didn't, because nothing in the workflow made that connection happen.

Each protocol, in other words, was earned. The methodology is not a clean theory. It is a running log of the specific failures that break AI-assisted long-form work, with the protocols that address them.

### 4.1. What Worked

- **Decision records accumulated without churning.** Across thirty-plus ADRs and PDRs, the project did not relitigate any decision that had been properly propagated and linked. When decisions changed, they changed through explicit superseding records, not through silent drift.
- **New research integrated without invalidating old work silently.** The Reweave Protocol caught several cases where new evidence should have updated existing decisions. Without it, those decisions would have continued to shape work while resting on outdated rationale.
- **Multi-tool collaboration stayed coherent.** The same project, used across Claude, Gemini, Cursor, and CLI agents, maintained consistent state because all tools read from the same routing document. Configuration drift — the original failure that motivated SYSTEM.md Primacy — did not occur.

### 4.2. What Didn't

- **The vault became unwieldy without periodic triage.** At certain points, the implementation plan accumulated more than two hundred open tasks. The methodology did not include a triage protocol at first; one had to be added. Large projects will need this.
- **The writing discipline was hard to hold under time pressure.** When a session was rushed, prose slipped. The tightening checklist had to become a hard gate rather than a soft norm. This is why the Ingestion Gate explicitly requires every AI-generated document to pass the checklist before admission.
- **Some protocols were overkill early.** Running the full Reweave Protocol on a two-week-old project with four decisions is overhead. The protocols are designed to scale down as well as up, but the discipline to not apply them prematurely takes practice.

### 4.3. What the Methodology Does Not Claim

- **It does not claim AI is a finished collaborator.** The methodology exists because AI is imperfect. If models had reliable project memory, strong calibration on evidence, and disciplined prose by default, most of the protocols would be unnecessary.
- **It does not claim to eliminate the need for human judgment.** Every protocol has a human-in-the-loop step. The methodology makes the human's judgment more effective; it does not replace it.
- **It does not claim the protocols are complete.** The ones described here are the ones that earned their place through repeated use. Future failure modes will likely motivate future protocols.

## 5. Related Work

The methodology is not invented from scratch. It is a synthesis of existing practices from several traditions, adapted for the specific failure modes of AI-assisted long-form work.

- **Architecture Decision Records** — Michael Nygard, [*Documenting Architecture Decisions*](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011). The format that PDRs extend and that the methodology integrates with propagation and reweave protocols.
- **Zettelkasten** — Niklas Luhmann's note-taking method, popularized for software and knowledge work by Sönke Ahrens in [*How to Take Smart Notes*](https://www.goodreads.com/book/show/34507927-how-to-take-smart-notes) (2017). The methodology's `concepts/` directory and wikilink discipline are direct descendants of zettelkasten practice, adapted for AI consumption.
- **Strunk & White** — [*The Elements of Style*](https://www.bartleby.com/141/), the ur-text for American English prose discipline. The methodology's writing rules lean heavily on this foundation.
- **USMC operational writing doctrine** — BLUF, Commander's Intent, tactical brevity. The synthesis of these practices with Strunk & White produces writing that survives both human and machine reading under load.
- **Ars Contexta** — [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta). An AI-powered vault generator evaluated during the methodology's development. Cherry-picked rather than adopted wholesale: the wikilink discipline and reweave protocol were adapted from its ideas, but the methodology as a whole is more opinionated about human-in-the-loop tightening than Ars Contexta's auto-generation approach.
- **Obsidian** — [obsidian.md](https://obsidian.md). The primary tool the methodology is designed around, though the protocols are tool-independent. The file format (plain markdown with YAML frontmatter) is chosen to survive any specific editor.
- **The broader AI-tooling landscape** — [Cursor](https://cursor.com), [Windsurf](https://windsurf.com), [Claude Code](https://docs.claude.com/en/docs/claude-code/overview), [Gemini CLI](https://github.com/google-gemini/gemini-cli). Tools that make CLI-level AI collaboration practical and that motivated the multi-tool compatibility requirements.
- **Model Context Protocol (MCP)** — [Anthropic's MCP specification](https://modelcontextprotocol.io). The emerging protocol for giving AI tools structured access to external resources. The methodology anticipates MCP becoming the standard way AI tools read from project vaults.

The specific synthesis in this methodology — the integration of ADRs with propagation and reweave, the ingestion gate for AI-generated content, the maturity tagging for evidence, the use of personas as hard design constraints — is, to our knowledge, novel. The individual elements are not.

## 6. How to Adopt

The methodology is designed to be adopted incrementally. Full installation is described on the [Installation Quickstart](https://adamcee.github.io/agentic-vault/installation/quickstart/) page. The shortest useful version is:

1. **Start with `SYSTEM.md`.** Write down, in one file, what your project is, who it's for, and what the current phase is. Paste it at the start of any AI conversation about the project. Update it when something important changes.
2. **Add decision records when you find yourself relitigating.** The first time you notice you've had the same argument with the AI twice, that's a signal to write an ADR.
3. **Add the ingestion gate when AI prose starts creeping in.** If you've pasted AI-generated reports into project docs, the tightening checklist starts paying back immediately.
4. **Add traceability when a claim turns out to be wrong.** The first time a decision rests on a claim the AI made up, traceability becomes non-optional for you.
5. **Add reweave when new evidence starts arriving.** Before new evidence is driving decisions, reweave is overhead. Once it is, reweave is necessary.

The protocols earn their place when the failure mode they address actually shows up. Adopting them all at once, before you've felt the failures, is more overhead than the benefit.

## 7. Conclusion

AI is a powerful thought partner with a specific weakness: it forgets. On work that lasts longer than a single conversation, that weakness compounds into relitigation, decision drift, evidence gaps, prose degradation, and context rot. The obvious solutions — longer contexts, vendor memory features, chat search — address the surface of the problem but not the structure.

The Agentic Vault methodology is one answer to the structural problem. Treat the project folder, not the chat window, as the single source of truth. Adopt a small set of protocols that handle the specific failure modes of heavy AI use over time. Keep the protocols honest by tying them to the problems they solve — add them when failures happen, and not before.

None of this is a silver bullet. It is a craft practice, earned through sustained use on real work. The methodology is offered in that spirit: not as a framework to be adopted wholesale, but as a working set of tools that made one ambitious project possible, and that may help others doing similar work.

---

*This whitepaper is a living document. For source material, ongoing updates, and the methodology in practice, see the [Agentic Vault documentation site](https://adamcee.github.io/agentic-vault/) and the [repository on GitHub](https://github.com/adamcee/agentic-vault). For a full list of citations, see the [Sources](sources.md) page.*
