---
description: "Reference for DeGov Agent API pricing and data-status resources."
---

# Metadata

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/meta/pricing` | free | Live token, network, tier, and route pricing |
| GET | `/v2/meta/data-status` | free | Global or per-DAO freshness and coverage |

`data-status` accepts optional `daoId`. Global data includes counts, `coverageStatus`, `dataAsOf`, and projection state. Per-DAO data includes DAO identity, coverage, vote coverage, and latest successful sync.

```bash
curl -s https://agent-api.degov.ai/v2/meta/pricing
curl -s "https://agent-api.degov.ai/v2/meta/data-status?daoId=example-dao"
```
