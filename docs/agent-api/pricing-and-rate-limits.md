---
description: "Discover current per-operation DeGov API prices through OpenAPI and x402 offers, and handle rate limits safely."
---

# Pricing & Rate Limits

## Discover current prices

The public API has free, standard, and plus resources. Query the [OpenAPI specification](https://agent-api.degov.ai/openapi.json) for current advertised pricing; inspect the actual x402 challenge before authorizing payment.

```bash
curl -sS 'https://agent-api.degov.ai/openapi.json' | \
  jq '.paths["/v2/proposals"].get["x-payment-info"]'
```

`x-payment-info.price` describes the advertised amount, currency, and pricing mode, while `protocols` names the payment protocol. For x402, `PAYMENT-REQUIRED` supplies the exact payment asset, atomic amount, network, and recipient for the requested resource. Do not substitute a cached documentation example for a live offer.

| Tier | Operations |
| --- | --- |
| Free | DAO directory and DAO detail |
| Standard | Proposal list, exact proposal resolver, and forum topic list |
| Plus | Proposal detail, vote summary, vote rows, DAO participants, voter profile, and voter history |

The API uses per-request USDC payments on Base. No subscription or partner key is required for the x402 path. Issued partner keys have separately agreed plans and scopes. Square managed-hosting prices do not apply to Agent API calls or Atlas partnerships.

## Rate limits and quotas

Paid access is subject to its applicable plan and route limit. A **429 `RATE_LIMITED`** response can indicate a short-window limit or a partner's monthly quota exhaustion. Inspect the message and retry timing, and honor `Retry-After`. Normal success responses do not currently promise remaining-quota headers.

x402 access is charged per successfully settled request rather than from an included partner subscription quota. A 402 response is an offer, not proof of payment. Follow the wallet's recovery policy when a paid request times out; avoid blind signed retries.

For efficient research, discover DAOs for free, use standard resources to narrow candidates, and fetch plus resources only when they materially improve the answer.
