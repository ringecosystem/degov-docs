---
description: "DeGov Agent API authentication — x402 per-request payment on Base, partner API tokens, and access tiers."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This page describes authentication for the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](index.md).

# Authentication

The Agent API has three access paths. Free endpoints need no authentication.

## 1. Public / free

Endpoints in the **free** tier — `/v2/meta/pricing`, `/v2/meta/data-status`, `/v2/daos`, `/v2/daos/:daoId` — require no credentials.

## 2. x402 payment (per-request, no key)

Paid endpoints can be used on a pay-per-request basis through [x402](https://x402.org) on Base, settled in USDC. There is no subscription and no API key to provision.

How it works:

1. Send the request without credentials.
2. The API responds `402 Payment Required` with an x402 challenge describing the required payment (token, amount, network, recipient).
3. The caller (an agent or CLI) submits the payment and retries the request with the payment header.
4. Settlement is on-chain; receipts are verifiable via the returned transaction hash.

The official CLI — bundled with the [dao-governance-research skill](https://github.com/ringecosystem/degov-agent-skills) — implements this flow automatically with a dedicated local wallet. Browser-based "Try It" tools are **not** expected to sign payments; use the CLI or curl for paid calls.

Always check current prices before paying: `GET /v2/meta/pricing` (free).

## 3. Partner API tokens

Partner integrations receive an API key used with the `x-degov-api-token` header:

```bash
curl -H "x-degov-api-token: <token>" https://agent-api.degov.ai/v2/proposals?daoId=ens-dao
```

Token properties:

- Issued by DeGov on request; the raw token is shown exactly once at creation and stored as a verifier/hash on the server.
- Revocable immediately.
- Scoped per access tier:
  - `v1:paid:standard`, `v1:paid:plus`, `v1:paid:*` — v1 endpoints.
  - `v2:paid:standard`, `v2:paid:plus`, `v2:paid:*` — v2 endpoints.
  - `v2:paid:*` grants the highest v2 permission scope.
- Existing partner keys issued before v2 are automatically upgraded to `v2:paid:*` when v2 launches; nothing needs to be re-issued on the partner side.

### Rate limits and quotas

Rate limits are enforced per limiter key and per backend process, and monthly quotas apply to partner-key requests:

| Plan | Monthly limit | Standard bucket | Detail bucket |
| --- | --- | --- | --- |
| Developer | 3,000/month | 30 rpm, burst 10 | 10 rpm, burst 5 |
| Business | 20,000/month | 120 rpm, burst 40 | 30 rpm, burst 10 |
| Custom | 100,000/month baseline | 300 rpm, burst 100 | 75 rpm, burst 25 |
| x402 pay-per-use | None (per-request) | 60 rpm, burst 20 | 20 rpm, burst 8 |

See [Pricing & Rate Limits](pricing-and-rate-limits.md) for the endpoint-to-bucket mapping.

## Internal access (not public)

DeGov's own services use a separate internal token (`x-degov-internal-token`) for trusted server-to-server calls. This token is **never** exposed to partners, browsers, logs, or public documentation.

## Security notes

- Never share a partner token, wallet private key, or passphrase.
- Raw tokens appear once at issuance; treat them like credentials.
- If a token leaks, revoke it immediately through DeGov support and request a replacement.
