---
description: "DeGov Agent API cursor pagination, page metadata, and stale-cursor recovery."
---

# Pagination

Most list resources return rows in `data.items` and pagination in `meta.page`:

```json
{
  "data": { "items": [] },
  "meta": {
    "page": { "limit": 25, "hasMore": true, "nextCursor": "opaque-cursor" }
  }
}
```

Pass `nextCursor` back unchanged as `cursor`, keeping the same endpoint, limit, filters, and sort. Cursors are bound to the serving revision and can become stale after data publication changes; restart from the first page when the API rejects a cursor.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals?daoId=example-dao&limit=25&cursor=opaque-cursor"
```

Do not decode, construct, cache indefinitely, or reuse a cursor for another query.

## Voter-ranking exception

`GET /v2/daos/:daoId/voters` ranks voters and may use a rank-oriented cursor. Treat it exactly like every other opaque cursor; its internal ordering is not a page number.

## Common limits

- Most lists: maximum 100 rows.
- Events: maximum 200 rows.
- Proposal votes: maximum 500 rows.
- Events and signals: maximum 90-day window.
- Proposal and voter-history windows: maximum 365 days.
