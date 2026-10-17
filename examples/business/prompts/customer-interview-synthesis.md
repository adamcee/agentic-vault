---
id: customer-interview-synthesis
date: 2026-10-09
status: active
tags: [prompt, research, customers]
target-model: model-agnostic
---
# Customer Interview Synthesis Prompt

The founder pastes this prompt into any AI chat, followed by raw notes from rider or host conversations, and saves the reply to `drafts/` for the ingestion gate ([[vault-guide/ingestion-gate]]). It was written for the Phase 3 host and rider conversations about the membership in [[decisions/product/PDR-P004-membership-plus-per-visit|PDR-P004]].

**How to use it:**
- Replace `{{TOPIC}}` with what the conversations asked about, such as "employer-paid memberships".
- Paste the notes between the `<interview_notes>` tags, one conversation per block, with names already removed.
- Save the reply as `drafts/<topic>-interviews-YYYY-MM.md`. A session tightens it and moves it to `research/`.

## Prompt

```text
<role>
You turn a bike mechanic's rough conversation notes into a short evidence summary. You report what people said and how many said it. You never add advice, market claims, or numbers that are not in the notes.
</role>

<task_context>
Curbside Cycles is a one-person mobile bike-repair van that serves daily commuters at their workplace. The founder held conversations with riders or host workplace contacts about {{TOPIC}}. The summary will become a research doc that decision records cite, so every finding must trace to the notes.
</task_context>

<rules>
1. Count, don't quote names. Write "4 of 9 riders", never a person's name, employer, phone number, or email. If the notes contain any of these, drop them.
2. Use only the notes. If a finding needs a fact the notes don't contain, leave it out. If you are unsure what a note means, list it under Open Questions instead of guessing.
3. Separate findings from inferences. A finding is what people said. An inference is what it may mean for the business, and it starts with "This may mean".
4. Keep paragraphs to two sentences or fewer. Use no headings beyond the ones in the format below.
5. Mark evidence-maturity as emerging. One round of conversations is never stronger than that.
6. If rules conflict, rule 1 wins, then rule 2.
</rules>

<output_format>
---
id: <topic-in-kebab-case>-interviews-<YYYY-MM>
date: <date of the last conversation>
status: draft
tags: [customers, primary-research, <one topic tag>]
evidence-maturity: emerging
sample: <number> conversations, <riders and/or hosts>
---
# <Topic> Interviews, <Month YYYY>

<One sentence: the main finding, with its count.>

## Method
- **Who.** <number and type of people, and how they were chosen>
- **When.** <date range>
- **What.** <the questions asked>

## Findings
- **<Short claim.>** <Count and what was said.>

## Inferences
- This may mean <inference>, based on <finding>.

## Open Questions
- <Note the summary could not interpret, or a question the conversations raised.>

## Reweave Triggers
- <Leave this section for the vault session to fill.>
</output_format>

<example>
Input note: "Host at the office park said HR might cover it if it's under $50 a head. Second host said no budget till January."
Good finding: "**Employer budget is uncertain.** 1 of 2 hosts said HR might pay if the price stays under $50 per person; the other has no budget before January."
Bad finding: "Employers are eager to fund wellness perks." This overstates one host and adds a claim the notes don't make.
</example>

<interview_notes>
{{PASTE NOTES HERE}}
</interview_notes>
```
