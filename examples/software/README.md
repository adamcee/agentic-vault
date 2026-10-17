# Example Vault: Brigade (Software)

Brigade is a fictional shift-scheduling web app for small independent restaurants with one to three locations, built by a solo developer and a co-founder who ran restaurant operations. This vault shows the project about six weeks in, from 2026-08-31 to 2026-10-09, after manager interviews replaced a React Native plan with a web app and a two-restaurant pilot started to question a swap-approval rule.

## Tour

1. **Master file:** [AGENTS.md](AGENTS.md) holds the project, phase, stack, standing decisions, and the Last Session Checkpoint.
2. **Superseded decision:** [ADR-T001](decisions/technical/ADR-T001-react-native-manager-app.md) was weakened by interviews and replaced by [ADR-T002](decisions/technical/ADR-T002-responsive-web-pwa.md), which explains what changed.
3. **Rejected decision:** [ADR-T004](decisions/rejected/ADR-T004-shared-spreadsheet-backend.md) records why a shared spreadsheet backend was declined.
4. **Reweave:** [pilot usage data](research/pilot-usage-weeks-1-2.md) ends with Reweave Triggers that weakened [PDR-P002](decisions/product/PDR-P002-manager-approval-for-swaps.md) and added tasks to the [implementation plan](prototype/implementation-plan.md).
5. **Evidence maturity:** [manager interview synthesis](research/manager-interview-synthesis.md) moved from `emerging` to `supported` after a second round, and [PDR-P001](decisions/product/PDR-P001-flat-fee-per-location.md) cites it inline beside an honest `[unsourced]` flag.
6. **Idea, promoted:** [SMS links instead of a staff app](ideas/sms-links-instead-of-staff-app.md) became ADR-T002.
7. **Idea, rejected:** [tip-pooling calculator](ideas/tip-pooling-calculator.md) was declined under a constitution clause.
8. **Idea, absorbed:** [copy last week](ideas/copy-last-week.md) became a plan task.
9. **Idea, open:** [auto-approve same-role swaps](ideas/auto-approve-same-role-swaps.md) waits on pilot follow-up.
10. **Draft awaiting tightening:** [SMS provider comparison](drafts/ai-report-sms-provider-comparison.md) is raw AI prose held at the ingestion gate.
11. **Admitted doc and its original:** [competitor feature scan](research/competitor-feature-scan.md) passed the gate, and [its untouched original](research/_source-competitor-feature-scan.md) sits beside it.
12. **Session logs:** [session-history.md](session-history.md) logs eight sessions, one line each in the form `(agent, session type) what changed`, across Claude Code, Claude Desktop, and Codex.
13. **Weekly logs:** [prototype/implementation-logs/](prototype/implementation-logs/README.md) holds one file per week from the first session, such as [2026-W41](prototype/implementation-logs/2026-W41.md), with a section for each session in the history.
14. **Ledger vs. human task list:** the [implementation plan](prototype/implementation-plan.md) is the AI's ledger, sorted into Now, owner calls, decisions owed, and drafts awaiting promotion. The [human task list](prototype/human-task-list.md) is the owner's own short list, with a few items pulled from the ledger.
15. **Hand-over note:** the 2026-10-09 session stopped before the gate pass and left [a resume note](drafts/2026-10-09-resume-sms-provider-choice.md) saying what's done, what's next, and what the owner must answer.
16. **`[unsourced]` claim backfilled:** [PDR-P002](decisions/product/PDR-P002-manager-approval-for-swaps.md) said swaps stall when the manager is off shift with no source; the pilot data now backs that claim, as logged in [2026-W41](prototype/implementation-logs/2026-W41.md).
17. **Reusable prompts:** [prompts/](prompts/README.md) holds the [research brief](prompts/sms-provider-research-brief.md) behind the SMS draft and the [log synthesis prompt](prompts/pilot-log-synthesis.md) behind the pilot data doc.
