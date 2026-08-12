---
description: "Find active DAO proposals and capture proposal keys for detail and vote requests."
---

# Find Active Proposals

**Tier:** free DAO discovery, then standard proposal discovery.

1. Find the canonical `daoId` with `GET /v2/daos`.
2. Query proposals with an active lifecycle status.
3. Read rows from `data.items`.
4. Keep the returned `proposalKey` for detail or vote requests.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals?daoId=example-dao&lifecycleStatus=active&sort=endingSoon&limit=25"
```

```json
{
  "data": {
    "items": [
      {
        "proposalKey": "p1_opaque",
        "identity": { "daoId": "example-dao", "provider": "snapshot", "externalId": "0xabc" },
        "title": "Fund the governance working group",
        "lifecycleStatus": "active",
        "outcome": null,
        "endAt": "2026-08-14T18:00:00Z",
        "coverageStatus": "ready"
      }
    ]
  },
  "meta": { "page": { "limit": 25, "hasMore": false } }
}
```

If the DAO is missing, verify coverage with `data-status`. If the query is too broad, add a DAO, time window, status, or provider filter.
