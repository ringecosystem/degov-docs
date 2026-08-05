---
description: "DeGov Agent API pagination — cursor-based pages, hasMore, nextCursor, and how to recover from stale cursors."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This page describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Pagination

Every v2 collection endpoint uses **cursor pagination**. There are no `total` counts and no `offset` parameters in v2.

## Page shape

```json
{
  "data": [ /* items */ ],
  "meta": {
    "page": {
      "limit": 25,
      "hasMore": true,
      "nextCursor": "eyJ2IjoxLCJlbmRwb2ludCI6..."
    }
  }
}
```

- `data` — the current page of items.
- `meta.page.limit` — the page size used.
- `meta.page.hasMore` — whether another page exists.
- `meta.page.nextCursor` — opaque cursor for the next page; present only when `hasMore` is `true`.

## Fetching the next page

Pass `nextCursor` back unchanged as the `cursor` query parameter, keeping all other filters identical:

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals?daoId=ens-dao&lifecycleStatus=active&limit=25&cursor=eyJ2IjoxLCJlbmRwb2ludCI6..."
```

Repeat until `hasMore` is `false`.

## Why not `total`?

Exact totals require counting the full candidate set on every request, which does not scale on live datasets. v2 returns deterministic pages instead. If you need an aggregate, use a dedicated endpoint (`/v2/meta/data-status` for dataset counts, `/v2/proposals/:proposalKey/votes/summary` for vote totals).

## Cursor semantics

Each cursor is bound to the request that produced it:

- **Endpoint** — a cursor from `/v2/proposals` is invalid on `/v2/events`.
- **Filters** — changing `daoId`, `lifecycleStatus`, or any filter invalidates the cursor.
- **Sort** — cursors are tied to the sort order used to create them.
- **Serving revision** — the cursor records the data revision it was created against.

## Error handling

| Situation | Response | Recovery |
| --- | --- | --- |
| Cursor reused with different endpoint/filters/sort | `400 CURSOR_INVALID` | Restart from the first page |
| Data was rebuilt between pages | `409 CURSOR_STALE` | Restart from the first page |
| Cursor missing/expired | `400 VALIDATION_ERROR` | Restart from the first page |

There is no way to jump to an arbitrary page; always page forward from the start.

## Limits

| Endpoint group | Default | Range |
| --- | --- | --- |
| Lists (`/v2/proposals`, `/v2/forum-topics`, `/v2/events`, `/v2/signals`, `/v2/daos`) | 25–50 | 1–100 |
| `/v2/proposals/:proposalKey/votes` | 100 | 1–500 |
| `/v2/voters/:voterIdentity/votes` | 50 | 1–100 |
