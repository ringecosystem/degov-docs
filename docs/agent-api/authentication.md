---
description: "Access free DeGov data anonymously or use x402 and scoped partner tokens for paid governance resources."
---

# Authentication

## Free resources

The OpenAPI specification, DAO directory, and DAO detail require no credentials. You can explore available data without an account or wallet.

## Partner tokens

Partner keys are issued directly by DeGov. [Contact the team](mailto:support@degov.ai) with your integration and expected usage. Send the issued token in a request header:

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  'https://agent-api.degov.ai/v2/proposals?limit=5'
```

Set `DEGOV_API_TOKEN` through your environment or secret manager. Keep tokens out of URLs, browser code, source control, and logs.

| Scope | Access |
| --- | --- |
| `v2:paid:standard` | Standard paid operations |
| `v2:paid:plus` | Plus paid operations |
| `v2:paid:*` | Both paid tiers |

A plus scope alone does not grant standard access. Keys also have an access plan, expiry, and revocation state. Contact DeGov for issuance, scope changes, replacement, or revocation. `atlas:read` is for the Atlas application and does not grant Agent API paid access.

An absent, invalid, or insufficient partner token can fall through to the normal x402 challenge. Inspect the response rather than assuming every token failure produces 401 or 403.

## x402 payment

Paid resources also accept per-request USDC payment on Base (`eip155:8453`):

1. Make the request and read the **402** response and `PAYMENT-REQUIRED` header.
2. Pass the offer to an x402-capable wallet for authorization and spending controls.
3. Retry the same method, URL, and body using its `PAYMENT-SIGNATURE` credential.
4. Check the successful response and `PAYMENT-RESPONSE` settlement result.

[DeGov Agent Skills](../agent-skills/index.md) use MetaMask Agent Wallet for this workflow. The wallet owns signing and safe retries. A discovered offer or verified signature alone is not settlement; unsuccessful handler responses are not settled. Do not blindly replay signed requests after a transport failure.

Current advertised prices are in the operation's `x-payment-info` in [OpenAPI](https://agent-api.degov.ai/openapi.json). The actual challenge specifies the asset, amount, network, and recipient.

## Product boundaries

The Agent API does not require an OAuth login for these public or paid access paths. Square's GraphQL and MCP services use `api.degov.ai` and have separate authentication; they are not the Agent API base URL. Use the current [Agent API reference](reference/index.md) for programmatic governance research.

Requests from DeGov Docs can preflight the partner-token header, but that does not make a browser a safe place to embed a private key. Automatic browser x402 payment is not part of this documentation.
