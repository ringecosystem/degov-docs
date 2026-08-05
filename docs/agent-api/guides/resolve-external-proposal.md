---
description: "Guide — resolve a Snapshot/Tally URL, external id, or proposal title to a canonical proposalKey."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Resolve an External Proposal

**User goal:** "I was given a Snapshot/Tally URL (or just a title/external id). Which proposal is it, and what's its canonical key?"

## Prerequisites

- Tier: `standard` (paid).
- Auth: x402 or partner token.
- Input: exactly one of `url`, `title`, or `externalId`.

## Call graph

```text
GET /v2/proposals/resolve        (standard)
  -> returns proposalKey
  -> GET /v2/proposals/:proposalKey        (plus, optional)
  -> GET /v2/proposals/:proposalKey/votes/summary   (plus, optional)
```

## 1. Resolve a URL

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/resolve?url=https%3A%2F%2Fsnapshot.org%2F%23%2Fproposal%2Fabc123"
```

## 2. Relevant response excerpt

```json
{
  "data": {
    "candidates": [
      {
        "proposalKey": "p1_eyJkYW9JZCI6ImVucy1kYW8iLCJwcm92aWRlciI6InNuYXBzaG90IiwiZXh0ZXJuYWxJZCI6ImFiYzEyMyJ9",
        "title": "Increase Protocol Budget",
        "match": { "type": "url_exact", "matchedFields": ["sourceUrl"] }
      }
    ]
  }
}
```

## 3. How to interpret

- `match.type` is a **real matching method**, not a made-up confidence score:
  - `url_exact` — the URL matched a known source URL.
  - `external_id_exact` — the external id matched exactly.
  - `title_exact` / `title_contains` — title matching, possibly with DAO disambiguation.
- Multiple candidates are possible for fuzzy titles; the caller decides.
- An empty `candidates` array means no match — try a different input or use the v1 surface / web search.

## 4. Next actions

- Open the proposal: `GET /v2/proposals/:proposalKey`.
- Get the vote result: `GET /v2/proposals/:proposalKey/votes/summary`.

## 5. Failure recovery

- `400 VALIDATION_ERROR` — you passed more than one primary selector, or none.
- `402` — payment required.
- Empty candidates — no match; relax the input or add `daoId`/`provider` disambiguation.

## When to use this endpoint

Only when the input came from **outside** the API (a link in chat, an external id, a spoken title). If you already have a `proposalKey` — from a list, event, or signal — you don't need resolve at all.
