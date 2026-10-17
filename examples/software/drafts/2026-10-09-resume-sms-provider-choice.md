---
id: 2026-10-09-resume-sms-provider-choice
date: 2026-10-09
status: hand-over
tags: [hand-over, sms, vendors]
---
# Resume: SMS Provider Choice

The SMS provider comparison is saved but not tightened, and no provider decision has been drafted. The next session runs the ingestion gate on [[drafts/ai-report-sms-provider-comparison]], then drafts the provider ADR in chat. Delete this note when the gate pass closes.

## Done
- Wrote [[prompts/sms-provider-research-brief]] and ran it in a deep-research tool.
- Saved the report as [[drafts/ai-report-sms-provider-comparison]] without edits.
- Added the gate pass and the provider decision to [[prototype/implementation-plan]].

## Next
1. **Check every claim against a source.** The report cites nothing. Confirm per-message prices, two-way messaging, and sender registration on each provider's own pricing and documentation pages.
2. **Cut what can't be checked.** Remove the deliverability "reputation" for Provider A and the "reported delays" for Provider B unless a source turns up.
3. **Add pilot volume.** The pilot sent 603 messages in two weeks, about 100 per location per week ([[research/pilot-usage-weeks-1-2]]). Price each provider at that volume against the $49 fee in [[decisions/product/PDR-P001-flat-fee-per-location|PDR-P001]].
4. **Promote it.** Save the untouched original as `research/_source-sms-provider-comparison.md`, move the clean doc to `research/` with `evidence-maturity: secondary` and `## Reweave Triggers`, and run the reweave.
5. **Draft the decision in chat.** List three alternatives and write the ADR only after the owner approves it.

## Open Questions for the Owner
- Should staff be able to accept a swap by replying to the text? If so, two-way messaging becomes a requirement.
- How long can the US carrier registration for business texting take? A long wait would affect the first paying locations in Phase 3.

## Files Touched
- [[prompts/sms-provider-research-brief]] (new)
- [[drafts/ai-report-sms-provider-comparison]] (new)
- [[prototype/implementation-plan]]
