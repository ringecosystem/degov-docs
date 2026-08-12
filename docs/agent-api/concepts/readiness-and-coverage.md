---
description: "Interpret DeGov Agent API availability, serving readiness, freshness, and resource coverage."
---

# Readiness & Coverage

Keep three questions separate.

## 1. Is the service available?

HTTP availability tells you whether the API can answer. A healthy service can still be backfilling data.

## 2. Is the serving revision ready?

When present, `meta.readiness.status` describes publication state:

| Status | Interpretation |
| --- | --- |
| `ready` | The current published revision is ready to query |
| `backfilling` | Data is available, but coverage may still be growing |
| `stale` | Results may lag source systems; inspect `dataAsOf` |
| `unavailable` | No usable serving revision is available for that request |

## 3. Is this dataset or resource complete?

`coverageStatus` and related fields describe completeness for a global dataset, DAO, proposal, or vote surface. Values can include `ready`, `partial`, `backfilling`, `stale`, or `unavailable`, depending on the resource. Do not treat readiness and coverage as one shared enum.

Use the free status resource before a research session:

```bash
curl -s https://agent-api.degov.ai/v2/meta/data-status
curl -s "https://agent-api.degov.ai/v2/meta/data-status?daoId=example-dao"
```

Disclose material gaps in user-facing answers. A non-ready state is not automatically a 404, and a 404 does not mean a global outage.
