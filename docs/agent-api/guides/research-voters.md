---
description: "Guide — research voters: DAO rankings, cross-DAO voter profiles, and vote history."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Research Voters

**User goal:** "Who holds the most voting power in DAO X, what does that voter look like across DAOs, and what have they voted on recently?"

## Prerequisites

- Tier: `plus` (paid).
- Auth: x402 or partner token.
- No key required to start — `daoId` is enough.

## Call graph

```text
GET /v2/daos/:daoId/voters              (plus) — ranked voters
  -> voterIdentity
  -> GET /v2/voters/:voterIdentity      (plus) — cross-DAO profile
  -> GET /v2/voters/:voterIdentity/votes (plus) — vote history
```

## 1. DAO voter ranking

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/daos/ens-dao/voters?limit=10"
```

```json
{
  "data": [
    {
      "rank": 1,
      "voterIdentity": "0xabc...",
      "totalVotingPower": "12345.67",
      "voteCount": "89",
      "proposalCount": "40"
    }
  ],
  "meta": { "page": { "limit": 10, "hasMore": true, "nextCursor": "..." } }
}
```

## 2. Cross-DAO profile

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/voters/0xabc..."
```

```json
{
  "data": {
    "voterIdentity": "0xabc...",
    "daoCount": "3",
    "voteCount": "145",
    "proposalCount": "77",
    "totalVotingPower": "54321.10",
    "daos": [
      { "daoId": "ens-dao", "voteCount": "89", "totalVotingPower": "12345.67", "lastVoteAt": "2026-08-03T10:00:00.000Z" }
    ]
  }
}
```

## 3. Vote history

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/voters/0xabc.../votes?daoId=ens-dao&limit=50"
```

```json
{
  "data": [
    {
      "proposal": { "proposalKey": "p1_...", "title": "Increase Protocol Budget" },
      "choiceKey": "1",
      "votingPower": "12.34",
      "votedAt": "2026-08-03T10:00:00.000Z",
      "transactionHash": "0x..."
    }
  ],
  "meta": { "page": { "limit": 50, "hasMore": false } }
}
```

## 4. How to interpret

- **V1 (ranking)** answers "who is powerful inside this DAO?".
- **V2 (profile)** answers "what does this voter do across all covered DAOs?".
- **V3 (votes)** answers "which specific proposals did they vote on?".
- `voterIdentity` is a normalized address for on-chain voters; 0x identities are lower-cased.

## 5. Next actions

- From a vote history row, open the proposal: `GET /v2/proposals/:proposalKey` (plus).
- Filter history by `daoId`, `from`, `to`.

## 6. Failure recovery

- `404 NOT_FOUND` — voter identity not found in coverage.
- `400 VALIDATION_ERROR` — malformed identity.
- `402` / `429` — pay / back off.
- Vote data not ready — empty rows with readiness, not an error.
