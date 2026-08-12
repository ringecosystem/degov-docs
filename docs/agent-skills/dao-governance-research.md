---
description: "DAO Governance Research skill — structured DeGov data plus official sources for accurate governance answers."
---

# DAO Governance Research

Use this skill when a question depends on recent DAO proposals, votes, forum activity, voter behavior, governance events, or source-backed evidence.

Repository: [dao-governance-research](https://github.com/ringecosystem/degov-agent-skills/tree/main/skills/dao-governance-research)

## Research flow

1. Identify the DAO, time range, and whether the request is discovery, a specific proposal, voter analysis, forum research, or security context.
2. Use free DAO and data-status resources when they can establish coverage.
3. Select the smallest set of current API resources that can answer the question.
4. Follow pagination only while more rows materially improve the answer.
5. Open official governance pages, forums, docs, and explorers when primary text or execution details need verification.
6. State missing, stale, backfilling, partial, or conflicting evidence.
7. Return useful prose rather than raw JSON.

## Payments

When an API request returns 402, the skill delegates offer inspection, authorization, spending controls, signing, settlement verification, and retry safety to the configured wallet capability. It does not bundle a CLI wallet or reproduce those policies.

If payment is unavailable or not authorized, continue through official web sources where possible and disclose the evidence limitation.

## Evidence rules

- Treat API data as evidence, not final prose.
- Never construct proposal keys, topic keys, or cursors.
- Prefer primary sources for proposal intent, executable actions, and deadlines.
- Do not infer outcomes, totals, or dates from titles.
- Use the security skill when the user asks whether a proposal is safe or risky.
