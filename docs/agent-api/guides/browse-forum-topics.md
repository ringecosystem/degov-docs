---
description: "Guide — browse governance-related forum topics and open a topic detail."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Browse Forum Topics

**User goal:** "What are people discussing in DAO X's governance forum, and what is this specific thread about?"

## Prerequisites

- List: tier `standard` (paid).
- Detail: tier `plus` (paid).
- Auth: x402 or partner token.

## Call graph

```text
GET /v2/forum-topics              (standard)
  -> returns topicKey
  -> GET /v2/forum-topics/:topicKey   (plus)
```

## 1. List governance-related topics

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/forum-topics?daoId=ens-dao&governanceRelated=true&sort=updatedDesc"
```

```json
{
  "data": [
    {
      "topicKey": "t1_eyJkYW9JZCI6ImVuc...",
      "title": "Discussion: treasury diversification",
      "summary": "Community thread on treasury allocation...",
      "url": "https://forum.ens.domains/t/...",
      "category": "Treasury",
      "relevanceScore": 87,
      "replies": "34",
      "posts": "41",
      "updatedAt": "2026-08-04T18:00:00.000Z"
    }
  ],
  "meta": { "page": { "limit": 25, "hasMore": false } }
}
```

## 2. Open the topic detail

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/forum-topics/t1_eyJkYW9JZCI6ImVuc..."
```

Returns the normalized topic: full title, summary, author, category, tags, engagement metrics, and timestamps.

## 3. How to interpret

- `governanceRelated=true` filters to topics the pipeline scored as governance-relevant — use it for research; omit it for a pure engagement view.
- `relevanceScore` is a pipeline score; `replies`/`posts` are exact engagement counts.
- `topicKey` is opaque — copy it, never construct it (see [Proposal & Topic Keys](../concepts/proposal-and-topic-keys.md)).

## 4. Next actions

- If a topic references a proposal, resolve it with `GET /v2/proposals/resolve?url=...` and continue with the proposal guides.
- Sort options: `updatedDesc`, `createdDesc`, `repliesDesc`.

## 5. Failure recovery

- `400 VALIDATION_ERROR` — check `governanceRelated` boolean and `sort` value.
- `404 NOT_FOUND` — topic not in coverage.
- `402` / `429` — pay / back off.
