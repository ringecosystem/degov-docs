---
description: "DeGov Agent API pricing tiers, live route prices, quotas, and rate-limit behavior."
---

# Pricing & Rate Limits

Every route is free, standard, or plus. Fetch the authoritative route table before estimating cost:

```bash
curl -s https://agent-api.degov.ai/v2/meta/pricing
```

```json
{
  "data": {
    "token": "USDC",
    "network": "eip155:8453",
    "routes": [
      {
        "routeId": "v2.proposals.list",
        "method": "GET",
        "path": "/v2/proposals",
        "tier": "standard",
        "paid": true,
        "price": "0.005"
      }
    ]
  }
}
```

At the time of this example, standard calls cost `0.005 USDC` and plus calls cost `0.01 USDC`. Prices in the live response override documentation examples.

| Tier | Typical use |
| --- | --- |
| free | Pricing, data status, DAO discovery and detail |
| standard | Proposal and forum discovery, events, signals, proposal resolution |
| plus | Proposal detail, votes, evidence, timelines, and voter research |

Partner plans may enforce short-window rate limits and monthly quotas. A 429 response can mean either rate limiting or quota exhaustion; use the response code and retry guidance. x402 access is priced per successful paid request rather than by a partner subscription quota.

For efficient research, discover DAOs for free, use standard resources to narrow candidates, and call plus resources only for items that materially affect the answer.
