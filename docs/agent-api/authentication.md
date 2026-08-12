---
description: "DeGov Agent API authentication — public resources, partner tokens, and x402 payments on Base."
---

# Authentication

The Agent API supports three access paths.

## Public resources

Pricing, data status, the DAO directory, and DAO detail are free and need no credentials.

## Partner tokens

Partner keys are issued directly by DeGov. [Contact us](https://t.me/RingDAO_Hub) with your integration and expected usage to request one, then send the issued token with each paid request:

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals?daoId=example-dao&limit=25"
```

Treat the token as a secret. Do not place it in browser URLs, source control, screenshots, or logs. Tokens can be scoped and revoked; contact DeGov for issuance, scope changes, revocation, or replacement.

An invalid or insufficient token may currently fall through to the normal 402 challenge. Clients should inspect the actual response instead of assuming every token failure is a fixed 401 or 403 envelope.

## x402 payment

Paid resources also support per-request USDC payment on Base (`eip155:8453`):

1. Send the request without payment credentials.
2. Read the `402 Payment Required` response and `payment-required` header.
3. Let an x402-capable wallet apply its normal authorization and spending controls.
4. Retry using the wallet-produced payment credential.
5. Verify settlement before treating the request as paid.

DeGov Agent Skills use MetaMask Agent Wallet as their default x402 wallet integration. The governance skill loads the wallet skill when it encounters a 402, while MetaMask owns authorization, spending controls, signing, settlement verification, and safe retries.

Always read current route prices from `GET /v2/meta/pricing`.

## Browser behavior

Requests from `https://docs.degov.ai` can preflight the `x-degov-api-token` header. This makes partner-token browser calls technically possible, but the current OpenAPI is not yet complete enough for a reliable generated Try It experience. Browser-based automatic x402 payment is not promised.
