# Design & Goals

*A method for using AI on work that lasts longer than one chat.*

---

## Summary

AI models forget everything between conversations. On a long project, that produces relitigated decisions, resurfacing rejected ideas, and lost rationale, so work that should build on itself keeps restarting.

The Agentic Vault treats the project folder, not the chat window, as the single source of truth. A small set of protocols handles the failures that show up under sustained AI use: context rot, decision drift, evidence gaps, prose degradation, and relitigation.

Each protocol was written in response to a recurring problem on a real project. The method is not finished.

---

## 1. The Problem

### 1.1. What Goes Wrong Between Sessions

Within one conversation, current models reason well and draft quickly. The next conversation knows nothing about the last one, and on a long project the costs add up:

- **Relitigation.** The AI has no record of earlier rounds, so it proposes the same ideas every few weeks. You re-explain why you rejected MongoDB, or why you chose one framework over another.
- **Decision drift.** Asked to solve a problem, the AI reaches for the most common pattern in its training data. That pattern may contradict a choice you made deliberately two months ago, and nobody notices until later.
- **Evidence gaps.** The AI can produce a confident rationale for almost any position and will cite research that does not exist. Without a way to trace claims to sources, the project builds on unverified assertions.
- **Prose degradation.** AI output carries hedges, meta-commentary, and padded paragraphs. Bloated documents are slow for you to read and hard to act on, and future sessions copy their style.
- **Context rot.** As a session or document grows, the model attends less to what came first. The session starts producing work that contradicts its own instructions.

### 1.2. Partial Fixes

Each common fix addresses part of the problem.

- **Longer context windows.** You can paste more of the project into each chat, but attention still decays over long contexts. Pasting costs time and tokens and loses the links between documents.
- **Vendor memory features.** These remember personal facts well but summarize across sessions. For project decisions, the summary drops what matters most. *"We chose Postgres"* is useless without the rejected alternatives and the reasons.
- **Chat history search.** The decisions you most need are often the casual ones that later turned out to matter. Search rarely surfaces them.
- **Custom GPTs and project assistants.** These inject fixed instructions at session start. They belong to one vendor, don't hold changing project state, and don't carry over to other tools.

All of these answer *how does the AI remember what I told it?* None answers *how does a project keep its memory across sessions and across tools?*

### 1.3. Memory Lives in the Folder

The AI forgets, but the project folder does not. So the folder has to hold the memory.

So the AI reads the folder at session start, decisions follow a consistent format, protocols keep records current as evidence changes, and every AI tool reads the same folder.

## 2. What the Vault Enables

On the project where the method was developed, the vault made the following routine:

- **Disposable sessions.** Sessions write checkpoints to the vault as they go. A crashed, interrupted, or week-old session costs nothing, because the next one resumes from the last checkpoint.
- **Many tools, one state.** CLI agents, desktop apps, and chat apps from different vendors work on the same project. Each tool's rule file is a short pointer to the same master file, so no tool works from stale instructions.
- **Planning separate from code.** The vault holds strategy, decisions, and plans. Coding agents in separate code repositories read it for constraints and write only to `drafts/`. Planning sessions and coding sessions share decisions without sharing a working tree.
- **Research that stays connected.** Hundreds of research documents link to the decisions they support. When new evidence arrives, the affected decisions can be found and rechecked.
- **Non-code work in the same system.** Market research, business planning, and product strategy follow the same decision records and protocols as the architecture.
- **Long breaks without loss.** The decisions log, ideas list, and session history let you return after weeks and continue where you stopped.

## 3. The Protocols

Each protocol addresses one failure from Section 1.

### 3.1. AGENTS.md Primacy

**Failure:** A project used across several AI tools has a configuration file per tool. Each falls out of date at a different rate, and the project's ground truth ends up split across files nobody updates together.

**Protocol:** One file, `AGENTS.md`, holds the authoritative project context. Tool-specific files (`CLAUDE.md`, `GEMINI.md`, `.cursorrules`) are short pointers to it, so context changes happen in one place. See [AGENTS.md Primacy](agents-md-primacy.md).

The idea is older than AI. Configuration management, editorial style guides, and military Commander's Intent all rely on one authoritative statement that everything downstream references.

### 3.2. The Session Protocol

**Failure:** Without a routine, you re-explain the project in every chat. The explanation is always incomplete, and the project drifts toward your retelling instead of its actual state.

**Protocol:** Every substantive session starts the same way. Read `AGENTS.md`, find files changed since the last logged session, and load the context the task needs. See [The Session Protocol](session-protocol.md).

### 3.3. Decision Records (ADRs and PDRs)

**Failure:** Decisions made in chat disappear. Three weeks later the rationale is gone, and the AI proposes the rejected alternative because nothing says it was rejected.

**Protocol:** Major decisions go in `decisions/`. Architecture Decision Records (ADRs) cover technical choices; Product Decision Records (PDRs) cover product choices. Each records context, the decision, alternatives considered, and consequences, and is drafted in chat and approved by the owner before it's written. Rejected options are recorded too, in a `rejected/` folder, so they can't be revived by accident.

The format comes from Michael Nygard's ["Documenting Architecture Decisions" (2011)](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), later spread by [Martin Fowler](https://martinfowler.com/articles/2021-document-architecture.html) and [adr.github.io](https://adr.github.io/). The vault adds PDRs, records rejections explicitly, and ties records to the other protocols, as described in [Decision Records](decision-records.md).

### 3.4. Decision Propagation

**Failure:** An ADR gets written, and the decision exists nowhere else. The implementation plan and the master file don't mention it, so later sessions don't know about it.

**Protocol:** A decision is complete only when it has been pushed into every document that should reflect it: the implementation plan, the constitution of invariants, and the master file. A short checklist runs at the end of every decision.

### 3.5. The Reweave Protocol

**Failure:** New evidence enters the project but never touches the decisions it affects. Months later you are working from decisions whose rationale no longer holds.

**Protocol:** When new information arrives, find the decisions it touches. Mark each as strengthened, weakened, or invalidated. Add links, and propose a superseding record for anything invalidated. See [The Reweave Protocol](reweave-protocol.md).

Propagation pushes decisions forward into the plan, and reweave pulls new evidence back through existing decisions. A project needs both.

### 3.6. Research Traceability

**Failure:** A decision cites *"thirty years of peer-reviewed validation."* It sounds authoritative but can't be checked, and when contradicting evidence arrives, nobody can find the decisions that relied on it.

**Protocol:** Every empirical claim in a decision document links to the vault research document that supports it. Unsourced claims are flagged `[unsourced]`. See [Research Traceability](research-traceability.md).

The norm comes from academic citation practice and systematic reviews, where tracing claims to sources is what makes results reproducible.

### 3.7. Evidence Maturity Tags

**Failure:** AI-written documents cite a replicated meta-analysis and a single preprint in the same confident tone. Decisions end up resting on thin evidence without anyone noticing.

**Protocol:** Every citation carries one of four tags: `[established]`, `[supported]`, `[emerging]`, or `[theoretical]`. Tags appear inline and in the research document's frontmatter. See [Evidence Maturity Tags](evidence-maturity.md).

Four levels are enough to separate a foundational finding from a promising lead without requiring a formal review of every source.

### 3.8. Wikilinks

**Failure:** Documents mention each other in prose without linking. Backlink queries miss these references, and the vault can't be navigated by following connections.

**Protocol:** Every reference to another vault document is a wikilink. See [Wikilink Discipline](wikilink-discipline.md).

The other protocols depend on links: reweave uses them to find affected documents, traceability to connect claims to evidence, and propagation to confirm a decision reached the right places. Without links, every protocol falls back to full-text search.

### 3.9. The Ingestion Gate

**Failure:** AI-generated reports get pasted straight into the vault. You stop reading documents that bury the point, and future sessions copy their style.

**Protocol:** AI-generated content lands in `drafts/` first. It moves into the vault only after passing a tightening checklist. See [The Ingestion Gate](ingestion-gate.md).

The checklist is described in [AI Writing Discipline](writing-discipline.md). It draws on four sources:

- **ISO 24495-1:2023, the international plain language standard.** Readers should get what they need, find it, understand it, and use it.
- **Strunk & White, *The Elements of Style*.** Active voice, omit needless words, concrete nouns and strong verbs.
- **Military correspondence doctrine.** Bottom Line Up Front (BLUF), Commander's Intent, and brevity, as in the U.S. Army's [AR 25-50](https://armypubs.army.mil/ProductMaps/PubForm/Details.aspx?PRODUCT_ID=1004725).
- **Engineering documentation practice.** Documents get read in a hurry, so the critical information goes first.

### 3.10. The Ideas Lifecycle

**Failure:** Ideas arrive faster than they can be evaluated. The ones not ready for a decision record die in chat logs and resurface weeks later.

**Protocol:** An `ideas/` folder holds short notes for unevaluated ideas. Each has a `resolved-by` field recording whether it was promoted to a decision, rejected, absorbed into another document, or left open. See [The Ideas Lifecycle](ideas-lifecycle.md).

### 3.11. Session Logs

**Failure:** Sessions run in parallel or weeks apart, and nobody can tell what changed or who changed it. A session that rewrites a shared log can erase another session's entries.

**Protocol:** Each session appends one line to `session-history.md` and a section to the week's implementation log, and never rewrites either. A lint script checks the logs at session close. See [Session Logs](session-logs.md).

### 3.12. Vault Maintenance

**Failure:** The plan grows past what anyone reads, links break, and old docs pile up.

**Protocol:** The agent triages the plan when it passes about 200 open items and reviews the whole vault quarterly, fixing mechanical problems itself and sending decisions to you. Scripts check links and writing. See [Vault Maintenance](vault-maintenance.md).

## 4. Principles

### 4.1. The Folder Is the Primary Artifact

In most AI workflows, the conversation is where work happens and files are where it ends up. The vault reverses this: work accumulates in the files, and the chat moves it between you and the files.

In practice, each document has to work for you months later and for the next AI session, which has no context at all. Source code and lab notebooks work the same way.

### 4.2. Decisions Over Opinions

An opinion is something the AI said in a chat. A decision is written down in `decisions/` with its rationale and rejected alternatives.

Decisions can be revisited through the Reweave Protocol, but they cannot be quietly undone. Separating what was discussed from what was committed keeps open questions from staying open forever.

### 4.3. Evidence Over Tone

AI writes authoritative-sounding prose about anything. The vault's answer is to make claims traceable, so trust rests on the evidence instead of the tone.

An unsourced claim isn't necessarily wrong, but the flag tells future sessions it hasn't been checked. An `[emerging]` tag marks a bet to revisit when replication arrives.

### 4.4. You Decide, the Agent Maintains

You set direction and make the calls: approve or reject decision records, choose what to work on, and review what the AI flags. Your own notes live in `journal/` and your task list, which the AI never writes.

The agent does the upkeep. It starts every session up to speed with `vault-start`, drafts decision records for your approval, runs the protocols (propagation, reweave, session logs, link checks), tightens its own writing, and proposes a superseding record instead of quietly contradicting a standing decision.

### 4.5. Start Small

Not every project needs every protocol. A short experiment doesn't need the reweave discipline, and a small project doesn't need an ADR for every choice. The setup tiers reflect this:

- **Tier 1 (web chat).** Fill out `AGENTS.md` and paste it at the start of each chat.
- **Tier 2 (AI IDE).** The IDE's AI reads `AGENTS.md` automatically.
- **Tier 3 (CLI agents).** The full vault and protocols, read at every session start.

A project can start at Tier 1 and add protocols as it grows.

## 5. The Field Test

The method was developed on a software product over about eight months, during which the vault grew to more than fifty decision records, roughly 250 research documents, and four stack changes. Work ran across Claude Code, Claude Desktop, Gemini, Codex, and IDE-based tools.

Several protocols were added in response to specific failures:

- **Ingestion Gate.** A vault audit found that roughly forty percent of writing-discipline violations came from AI research reports admitted without tightening.
- **Evidence Maturity Tags.** A decision cited a single new study with the same weight as an established meta-analysis.
- **Ideas Lifecycle.** The same product ideas kept coming back because the previous round of thinking had nowhere to live.
- **Reweave Protocol.** New research should have changed an earlier decision and didn't, because nothing in the workflow connected them.

### 5.1. What Worked

- **Decisions stayed settled.** No properly propagated and linked decision was relitigated. Decisions changed through explicit superseding records, not drift.
- **New research updated old decisions.** The Reweave Protocol caught several decisions whose rationale new evidence had weakened.
- **Tools stayed in sync.** Claude, Gemini, Cursor, and CLI agents read the same master file, and configuration drift did not recur.

### 5.2. What Didn't

- **The vault needed periodic triage.** The implementation plan grew past two hundred open tasks before a triage protocol was added. Large projects will need one.
- **Writing discipline slipped under time pressure.** The tightening checklist had to become a hard gate instead of a norm. The Ingestion Gate exists for this reason.
- **Some protocols were overkill early.** Running a full reweave on a two-week-old project with four decisions is wasted effort.

### 5.3. Limits

- **AI still needs supervision.** If models had reliable project memory, calibrated evidence handling, and disciplined prose, most of these protocols would be unnecessary.
- **Human judgment stays in the loop.** Every protocol includes a human step.
- **The protocol set is incomplete.** New failure modes will likely call for new protocols.

## 6. Related Work

The method combines existing practices and adapts them for AI-assisted work.

- **Architecture Decision Records.** Michael Nygard, [*Documenting Architecture Decisions*](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011). PDRs extend this format.
- **Zettelkasten.** Niklas Luhmann's note-taking method, introduced to a wide audience by Sönke Ahrens in [*How to Take Smart Notes*](https://www.goodreads.com/book/show/34507927-how-to-take-smart-notes) (2017). The `concepts/` folder and wikilink discipline come from this tradition.
- **Plain language.** [ISO 24495-1:2023](https://www.iso.org/standard/78907.html), whose four principles frame the writing rules.
- **Strunk & White.** [*The Elements of Style*](https://www.bartleby.com/141/), the source of the sentence-level rules.
- **Military correspondence doctrine.** BLUF, Commander's Intent, and brevity.
- **Ars Contexta.** [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta), an AI vault generator. Wikilink discipline and the reweave protocol were adapted from it. The vault relies more on human tightening than on auto-generation.
- **Obsidian.** [obsidian.md](https://obsidian.md), the main editor the vault is built around. Plain markdown with YAML frontmatter keeps the vault usable in any editor.
- **AI coding tools.** [Cursor](https://cursor.com), [Windsurf](https://windsurf.com), [Claude Code](https://docs.claude.com/en/docs/claude-code/overview), and [Gemini CLI](https://github.com/google-gemini/gemini-cli) motivated the multi-tool requirements.
- **Model Context Protocol.** [MCP](https://modelcontextprotocol.io) gives desktop AI apps read and write access to the vault.

As far as we know, this particular combination is new: decision records tied to propagation and reweave, an ingestion gate for AI content, and maturity tags on evidence. The individual parts are not.

## 7. How to Adopt

Add each protocol when its failure shows up. Full setup is in the [Quickstart](../installation/quickstart.md).

1. **Start with `AGENTS.md`.** Write what the project is, who it's for, and the current phase. Load it at the start of every AI session and update it when something important changes.
2. **Add decision records when you catch yourself relitigating.** The second time you have the same argument with the AI, write an ADR.
3. **Add the ingestion gate when AI prose creeps in.** If you've pasted AI reports into project docs, the checklist pays off right away.
4. **Add traceability when a claim turns out to be wrong.** The first decision that rests on an invented citation makes the case.
5. **Add reweave when new evidence starts driving decisions.** Before then, it's overhead.

---

*Citations are listed in [Sources & Further Reading](sources.md). The source is on [GitHub](https://github.com/adamcee/agentic-vault).*
