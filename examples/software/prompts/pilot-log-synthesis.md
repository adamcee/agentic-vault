---
id: pilot-log-synthesis
date: 2026-10-06
status: Active
tags: [prompt, pilot, usage-data]
target-model: Claude
---
# Pilot Log Synthesis Prompt

A prompt that turns a two-week export of the audit log and SMS send log into a research doc draft. It produced the first version of [[research/pilot-usage-weeks-1-2]] on 2026-10-06; rerun it for each later two-week window.

## Prompt

```
<role>
You summarize usage logs for a restaurant scheduling app. You count, you never estimate, and you quote the log rows behind every unusual case.
</role>

<task_context>
Brigade is in a two-restaurant pilot. Restaurant A has one location and one manager; Restaurant B has two locations and two managers who share scheduling.
Open question: does every shift swap still need manager approval, or could same-role swaps that add no overtime be approved automatically?
Period: {start_date} to {end_date}.
</task_context>

<user_input>
{audit_log_csv}
{sms_send_log_csv}
</user_input>

<instructions>
Think step by step in <thinking> tags before writing. Compute each metric per restaurant and in total:
- weekly schedules published, and the device type each was built on
- staff who opened at least one shift link, and staff who installed the PWA
- swap requests, same-role swap requests, approvals, and denials
- median minutes from swap request to manager decision
- SMS messages sent
Then describe every denied swap and every swap that waited more than three hours, citing the log rows.
</instructions>

<constraints>
- Use only the logs provided. If a metric cannot be computed from them, write "not in export" instead of a number.
- Do not name staff; use roles ("a server", "a line cook").
- No paragraph longer than two sentences.
</constraints>

<output_format>
Frontmatter with date, tags, evidence-maturity: emerging, and a source line naming the export and period.
A first sentence stating the main finding, then ## Pilot Setup, ## Findings (one table), ## Interpretations (each marked as an inference), and ## Reweave Triggers naming the decision records the numbers strengthen or weaken.
</output_format>
```
