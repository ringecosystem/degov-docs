---
description: "DeGov Agent API pricing and rate limits — free, standard, and plus tiers, per-request x402 prices, and rate-limit buckets."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This page describes pricing for the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](index.md).

# Pricing & Rate Limits

## Tiers

Every endpoint belongs to exactly one tier:

| Tier | Examples | Access |
| --- | --- | --- |
| **free** | `/v2/meta/pricing`, `/v2/meta/data-status`, `/v2/daos`, `/v2/daos/:daoId` | No credentials |
| **standard** | `/v2/proposals`, `/v2/proposals/resolve`, `/v2/forum-topics`, `/v2/events`, `/v2/signals` | x402 or partner token |
| **plus** | proposal detail/votes/evidence, forum detail, timeline, voters, voter profile | x402 or partner token |

The canonical price per endpoint is always read from `GET /v2/meta/pricing` (free). Do not hardcode prices; they can change.

```json
{
  "data": {
    "token": "USDC",
    "network": "eip155:8453",
    "routes": [
      { "routeId": "v2.proposals.list", "method": "GET", "path": "/v2/proposals", "tier": "standard", "paid": true, "price": "0.005" },
      { "routeId": "v2.daos", "method": "GET", "path": "/v2/daos", "tier": "free", "paid": false, "price": null }
    ]
  }
}
```

## Rate-limit buckets

Paid routes map to one of two in-memory token buckets per limiter key:

| Bucket | Protects | Limiter key |
| --- | --- | --- |
| `standard` | Standard agent routes (lists, feeds, resolve) | `payer:<address>:standard` or `anonymous:standard` |
| `detail` | Heavy detail lookups (proposal detail, votes, evidence, timeline, voters) | `payer:<address>:detail` or `anonymous:detail` |

Bucket limits per plan are listed in [Authentication](authentication.md#rate-limits-and-quotas). When you exceed a limit you receive `429` with `RATE_LIMITED` or `QUOTA_EXCEEDED` — see [Errors](concepts/errors.md).

## What counts against monthly quota

- **Counted:** successful responses and business-level errors (invalid params, not found).
- **Not counted:** bad auth, missing payment, rate-limited requests, and server errors.

## Cost guidance

For a typical research session:

- Discovery is free (`data-status`, `daos`).
- A proposal list scan is a `standard` call.
- Opening a proposal detail, vote summary, or evidence is a `plus` call.
- If you only need the vote result, call `votes/summary` — not the full `votes` page.

The bundled [dao-governance-research skill](https://github.com/ringecosystem/degov-agent-skills) prints live budget guidance based on the pricing endpoint, so agents can estimate how many calls a given USDC budget covers before spending.
