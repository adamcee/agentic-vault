# Decision Records (ADRs & PDRs)

We do not just record *what* we built; we record *why* we chose it, and what we rejected.

The Agentic Vault uses Architecture Decision Records (ADRs) and Product Decision Records (PDRs) located in the `decisions/` directory.

### Why this matters for AI
LLMs are highly prone to **relitigating decisions**. If you rejected using MongoDB three weeks ago, a fresh AI session today might suggest MongoDB again. 

By keeping a formal ADR that states "MongoDB was rejected because of X," the AI will read the decision record, understand the context, and suggest a different path without you having to correct it.

### Propagation and Reweave
The Agentic Vault relies on two protocols to keep decisions healthy:
1. **Decision Propagation Protocol:** When a new decision is made, the AI is instructed to actively push that decision into the implementation plan and the project `CONSTITUTION.md`.
2. **Reweave Protocol:** When new research or information arrives, the AI must look backward at existing ADRs to see if the new evidence strengthens, weakens, or invalidates a past decision.