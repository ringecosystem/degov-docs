---
description: "Guide — find all currently active proposals for a DAO with the DeGov Agent API."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Find Active Proposals

**User goal:** "Which proposals are currently being voted on for DAO X?"

## Prerequisites

- Tier: `standard` (paid).
- Auth: x402 or partner token — see [Authentication](../authentication.md).
- No key required: this endpoint returns everything you need.

## Call graph

```text
GET /v2/proposals            (standard)
  -> returns proposalKey     (needed only if you open details next)
```

## 1. Query the list

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals?daoId=ens-dao&lifecycleStatus=active&sort=endingSoon&limit=20"
```

## 2. Relevant response excerpt

```json
{
  "data": [
    {
      "proposalKey": "p1_eyJkYW9JZCI6ImVucy1kYW8iLCJwcm92aWRlciI6InNuYXBzaG90IiwiZXh0ZXJuYWxJZCI6ImFiYzEyMyJ9",
      "title": "Increase Protocol Budget",
      "lifecycleStatus": "active",
      "outcome": "unknown",
      "endAt": "2026-08-07T12:00:00.000Z"
    }
  ],
  "meta": { "page": { "limit": 20, "hasMore": false } }
}
```

## 3. How to interpret

- `lifecycleStatus: "active"` — the proposal is currently in its voting window.
- `outcome: "unknown"` — no outcome yet; it is still live.
- `endAt` — voting deadline, useful for "ending soon" summaries.
- `proposalKey` — copy it if you want to open the proposal next.

## 4. Next actions

- Open the proposal body: `GET /v2/proposals/:proposalKey` (plus).
- Get the live vote result: `GET /v2/proposals/:proposalKey/votes/summary` (plus) — see [Inspect Proposal Votes](inspect-proposal-votes.md).
- Page through more results with `meta.page.nextCursor` — see [Pagination](../concepts/pagination.md).

## 5. Failure recovery

- `402` — payment required; pay per the x402 challenge and retry.
- `400 VALIDATION_ERROR` — check `lifecycleStatus` spelling and `limit` range.
- `429` — back off and retry.
- `409 CURSOR_STALE` / `400 CURSOR_INVALID` — restart from page one.

## Filters worth knowing

| Parameter | Purpose |
| --- | --- |
| `daoId` | Restrict to one DAO |
| `provider` | Restrict to a governance provider (e.g. `snapshot`) |
| `lifecycleStatus` | `active`, `pending`, `closed`, `unknown` (comma-separated) |
| `outcome` | `passed`, `failed`, `executed`, `canceled`, `unknown` |
| `timeField` + `from`/`to` | Window on `createdAt`, `startAt`, `endAt`, or `updatedAt` |
| `sort` | `updatedDesc`, `createdDesc`, `endingSoon` |
