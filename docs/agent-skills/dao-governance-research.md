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

## MetaMask Agent Wallet

MetaMask Agent Wallet is the skill's default payment integration. When an API request returns 402, the research skill loads `metamask-agent-wallet` and delegates offer inspection, authorization, spending controls, signing, settlement verification, and retry safety to it.

The governance skill does not duplicate wallet code or wallet policy. If MetaMask Agent Wallet is unavailable or payment is not authorized, it continues through official web sources where possible and discloses the evidence limitation.

## Evidence rules

- Treat API data as evidence, not final prose.
- Never construct proposal keys, topic keys, or cursors.
- Prefer primary sources for proposal intent, executable actions, and deadlines.
- Do not infer outcomes, totals, or dates from titles.
- Use the security skill when the user asks whether a proposal is safe or risky.
