---
id: sms-provider-research-brief
date: 2026-10-09
status: Active
tags: [prompt, research-brief, sms, vendors]
target-model: model-agnostic deep-research tool
---
# SMS Provider Research Brief

A deep-research brief that compares three hosted SMS APIs for Brigade's shift alerts. It produced [[drafts/ai-report-sms-provider-comparison]] on 2026-10-09; the output lands in `drafts/` and passes [[vault-guide/ingestion-gate]] before it enters `research/`.

## Prompt

```
<role>
You are a research analyst comparing SMS API providers for a two-person software team. You report what each provider's own pages say and mark anything you cannot source.
</role>

<task_context>
Brigade is a shift-scheduling web app for independent restaurants with one to three locations. Every shift change and login link reaches staff by SMS, so SMS is the main channel to staff and a direct cost against a flat $49 monthly fee per location.
Pilot volume: 603 messages in two weeks across three locations, about 100 per location per week.
The research informs one decision: which provider to use for the first paying locations in the United States.
Providers to compare: Provider A, Provider B, Provider C.
</task_context>

<questions>
1. What does each provider charge per outbound SMS in the US, and what would 100, 500, and 2,000 messages per location per week cost each month?
2. Does each provider support two-way messaging, so staff can reply to a text to accept a swap?
3. What does each provider require for US business sender registration, and how long does approval take?
4. What delivery-status data does each API return, such as delivered, failed, or carrier-rejected?
</questions>

<constraints>
- Prefer each provider's official pricing pages, API documentation, and status pages. Use third-party reviews only when no official source answers a question, and label them.
- Ignore marketing features, email, voice, and chat channels.
- Cite a URL for every factual claim. If you cannot find a source for a claim, mark it [unsourced] rather than inventing a citation.
- Separate findings (what a source states) from inferences (what you conclude for Brigade).
- Do not recommend a provider. The team decides.
- Keep the report under 1,200 words.
</constraints>

<output_format>
YAML frontmatter with date, tags, and evidence-maturity: secondary.
## Findings: one table with providers as columns and the four questions as rows, then cited notes per question.
## Inferences: at most five bullets, each naming the finding it rests on.
## Reweave Triggers: which of these may change: the flat-fee pricing decision (cost per location) and the web-app-with-SMS decision (SMS as the main channel).
</output_format>
```
