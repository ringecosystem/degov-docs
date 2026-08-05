---
description: "The dao-governance-research skill — DeGov Agent API as the primary source for DAO governance facts."
---

# DAO Governance Research

**When to use:** the user asks about Web3 DAO governance and the answer depends on accurate, recent governance information — DAO activity, proposal details, vote results, or governance timelines.

**Goal:** avoid hallucinating DAO governance facts. Use the DeGov [Agent API](../agent-api/index.md) as the primary evidence source, then web search as a follow-up layer when API coverage is missing, stale, too shallow, or needs source verification.

Repository: [dao-governance-research](https://github.com/ringecosystem/degov-agent-skills/tree/main/skills/dao-governance-research)

## Workflow

1. **Plan the query:** which DAO(s), what time range, discovery vs. detail, free vs. paid.
2. **Free first:** `data-status`, `daos`, DAO detail — no payment needed.
3. **Paid path requires explicit user consent:** present a clear choice between the DeGov Agent API paid path and web-search-only.
4. **Wallet:** the bundled CLI manages a dedicated local Base wallet for x402 payments (USDC). The wallet and passphrase stay local — never shared or exposed in chat.
5. **Answer:** turn API results into a plain-language explanation with sources; never dump raw JSON.
6. **Verify:** when linked sources matter, follow them; when API data is missing/stale/too shallow, say so and use official DAO forums, Snapshot/Tally pages, and announcements.

## API call patterns

The skill's CLI wraps the [Agent API](../agent-api/index.md) endpoints. High-level patterns:

| Question type | Endpoints |
| --- | --- |
| "What has DAO X been doing lately?" | `data-status`, DAO detail, `events` (or `signals` for curated) |
| "What are the biggest stories this week?" | `events` / `signals` with a 7-day window |
| "Explain this proposal (URL/title)" | `proposals/resolve` → `proposals/:proposalKey` |
| "How did the vote go?" | `proposals/:proposalKey/votes/summary` |
| "Who voted, with how much power?" | `proposals/:proposalKey/votes` |
| "Who are the top voters in DAO X?" | `daos/:daoId/voters` → `voters/:voterIdentity` |
| "What are people discussing?" | `forum-topics` → `forum-topics/:topicKey` |

## Rules

- Fetch `proposalKey` from the API; never construct it.
- Use `votes/summary` for results instead of paging `votes`.
- Use `evidence` only for citation/audit answers.
- State readiness/coverage limitations explicitly.
- Never push wallet setup after the user declines the paid path.
