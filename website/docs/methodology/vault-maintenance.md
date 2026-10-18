# Vault Maintenance

A vault needs occasional upkeep, and the agent does most of it. Two protocols and a few scripts keep the plan short, the links working, and the writing tight.

## Plan Triage

Run it when the ledger passes about 200 open items, after a major change in direction, or quarterly. The agent checks each item against the logs and files, marks done and superseded items, flags overdue ones, moves reference material out of the plan, and records before-and-after counts, but it never reprioritizes; that's your call.

## Vault Review

Run it quarterly or after a long break. The review audits six areas, and it can run them as parallel read-only subagents: structure, decisions, writing discipline, drafts and the ledger, research and links, and lifecycle (stale ideas, docs due for archive).

Mechanical fixes happen in the same session. Anything that needs a decision goes to the ledger for you; findings never go into a standalone report, because report files go stale.

## Scripts

The template ships Python scripts in `.claude/skills/`. Each protocol page also gives a manual fallback.

| Script | What it does |
|---|---|
| `vault-links/vault-link-check.py` | Lists wikilinks that point nowhere, skipping targets listed in `.link-check-ignore`. |
| `vault-links/vault-autolink.py` | Previews, then adds, links where a note's name is mentioned in plain text. |
| `vault-maintenance/vault-lint.py` | Checks the session logs at session close and keeps `AGENTS.md` under the size some tools can read in one go. |
| `vault-maintenance/vault-review-scan.py` | Flags long paragraphs, filler words, stray checkboxes, and research docs missing Reweave Triggers. |
| `vault-maintenance/tag-aligner.py` | Normalizes frontmatter tags. |

## Archives

Retired docs move to an `archive/` folder inside their section. Archives are exempt from the tightening checklist and the scans, but links into them still resolve.
