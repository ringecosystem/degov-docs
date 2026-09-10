---
description: "Find active DAO proposals using current status filters and preserve returned proposal IDs for follow-up research."
---

# Find Active Proposals

1. Find the DAO using the free directory's `query` parameter.
2. Request its active proposals, optionally sorted by the closest known voting deadline.
3. Read the top-level `data` array and preserve each returned `proposalId`.

```bash
curl -sS 'https://agent-api.degov.ai/v2/daos?query=Uniswap&limit=5'

curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  'https://agent-api.degov.ai/v2/proposals?daoId=uniswapgovernance-eth&status=active&sort=votingEndsAtAsc&limit=25'
```

The second request is paid; the header illustrates issued partner-token access. An x402-capable wallet is the alternative.

Use `status=active&status=pending` to request multiple statuses. Do not comma-separate them. `query` searches proposal titles; `createdFrom` and `createdTo` filter creation time, not voting deadlines. Each time window is at most 365 days.

Explain `status`, `outcome`, and `executionStatus` separately. Verify deadlines against `source.url` when they affect an action. Follow `page.nextCursor` only while more results are useful; an empty list means no matching proposals in the published view.
