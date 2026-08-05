---
description: "Guide — inspect a proposal's vote result and per-voter vote breakdown with pagination."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Inspect Proposal Votes

**User goal:** "How did the vote go, did quorum pass, and who voted with the most power?"

## Prerequisites

- Tier: `plus` (paid).
- Auth: x402 or partner token.
- Key: `proposalKey` (from a list, resolve, event, or signal).

## Call graph

```text
GET /v2/proposals/:proposalKey/votes/summary   (plus) — aggregates
GET /v2/proposals/:proposalKey/votes           (plus) — per-voter rows, paginated
```

## 1. Vote summary — aggregates

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_.../votes/summary"
```

```json
{
  "data": {
    "proposal": { "proposalKey": "p1_...", "title": "Increase Protocol Budget", "outcome": "passed" },
    "totals": { "votes": "81234", "uniqueVoters": "4521", "votingPower": "1234567.890123456789012345" },
    "quorum": { "raw": "100K", "progress": "0.7342", "reached": true },
    "choices": [ { "key": "1", "label": "For", "votes": "60123", "votingPower": "812345.67" } ],
    "coverageStatus": "complete"
  }
}
```

Interpretation:

- `outcome` — final result of the proposal.
- `quorum.reached` — whether quorum was met (`progress` is a decimal string).
- `choices` — per-choice vote counts and voting power.
- If readiness is not `ready`, `totals`/`quorum` are `null` and `choices` empty — this is **not** a 404.

## 2. Vote rows — per voter, first page by power

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_.../votes?order=power&limit=100"
```

```json
{
  "data": [
    {
      "voteId": "123456",
      "voterIdentity": "0xabc...",
      "choiceKey": "1",
      "choice": { "label": "For" },
      "votingPower": "12.340000000000000000",
      "votedAt": "2026-08-03T10:00:00.000Z",
      "transactionHash": "0x..."
    }
  ],
  "meta": { "page": { "limit": 100, "hasMore": true, "nextCursor": "eyJ2Ijox..." } }
}
```

## 3. Next page

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_.../votes?order=power&limit=100&cursor=eyJ2Ijox..."
```

## 4. How to interpret

- `order=power` — highest voting power first; `order=time` — most recent first.
- Only the **latest valid ballot** per voter is returned; recast (superseded) ballots are not exposed.
- `votingPower` is a decimal string — do not parse to JS `Number` for arithmetic.

## 5. Failure recovery

- `400 CURSOR_INVALID` / `409 CURSOR_STALE` — restart from page one with the same filters.
- `404 NOT_FOUND` — proposal not in coverage.
- `402` / `429` — pay / back off.
- Vote data not ready — response returns empty rows with readiness, not an error.

## When to use which

- Need the result fast → `votes/summary` only.
- Need a ranked list of who voted → `votes?order=power`.
- Need recent ballots → `votes?order=time`.
