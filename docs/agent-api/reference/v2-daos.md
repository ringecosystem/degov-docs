---
description: "Current DeGov public API reference for free DAO discovery and DAO detail."
---

# DAOs

The [live OpenAPI specification](https://agent-api.degov.ai/openapi.json) is authoritative for methods, parameters, schemas, and payment metadata. Examples below are illustrative snapshots, not current governance claims. Replace opaque placeholders with IDs returned by the API.

## `GET /v2/daos`

Lists DAOs alphabetically by public `daoId`.

| Name     | Type   | Meaning                                      |
| -------- | ------ | -------------------------------------------- |
| `query`  | string | Case-insensitive substring of DAO name or id |
| `limit`  | int    | 1-100, default 25                            |
| `cursor` | string | Cursor from the preceding matching DAO page  |

```bash
curl -sS "https://agent-api.degov.ai/v2/daos?query=Uniswap&limit=25"
```

Example item:

```json
{
  "daoId": "uniswapgovernance-eth",
  "name": "Uniswap",
  "sources": ["discourse", "snapshot"],
  "availableData": ["proposals", "votes", "forumTopics"],
  "proposalCounts": { "total": 197, "active": 0 },
  "participation": { "voterCount": 30710, "voteCount": 313022 },
  "latestActivity": {
    "proposalCreatedAt": "2026-07-21T23:15:24.000Z",
    "forumLastPostedAt": "2026-07-10T09:08:39.987Z"
  },
  "dataAsOf": "2026-09-03T09:42:18.000Z"
}
```

`participation` is either the published complete vote totals or `null`. Timestamps inside
`latestActivity` can also be `null`. `availableData` is a resource-availability signal, not a
freshness guarantee.

Use `query` to resolve a natural-language DAO name; ask the user when multiple matches remain.

## `GET /v2/daos/{daoId}`

Returns one DAO item with the same fields as the directory.

```bash
curl -sS "https://agent-api.degov.ai/v2/daos/uniswapgovernance-eth"
```

An unknown slug returns `404 NOT_FOUND`.
