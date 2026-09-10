---
description: "Make free DAO requests, inspect the OpenAPI contract, and understand an unsigned x402 payment challenge."
---

# Quickstart

Start without an account, API key, wallet, or payment. The commands below require `curl`; the optional extraction command uses `jq`.

## 1. Find a DAO

```bash
curl -sS 'https://agent-api.degov.ai/v2/daos?query=Uniswap&limit=5'
```

Read the DAO objects from the top-level `data` array. Each includes `daoId`, `sources`, `availableData`, proposal counts, nullable participation totals, and `dataAsOf`. A list also includes `page.hasMore` and `page.nextCursor`.

## 2. Read its available data

Use a `daoId` returned by that directory, unchanged. This example selects the first match and stops if none exists:

```bash
DAO_ID=$(curl -sS 'https://agent-api.degov.ai/v2/daos?query=Uniswap&limit=5' | jq -er '.data[0].daoId') &&
  curl -sS "https://agent-api.degov.ai/v2/daos/$DAO_ID"
```

The response contains one object in `data`. `availableData` identifies the public resource families available for that DAO. `dataAsOf` describes source observations included in the record; neither field guarantees that every source is current.

## 3. Inspect the contract and pricing

```bash
curl -sS 'https://agent-api.degov.ai/openapi.json'
```

Use an operation's parameters, schemas, and `x-payment-info` to plan a request. Read [pricing](pricing-and-rate-limits.md) before paid data access. Discovery itself is free.

## 4. Inspect a paid-route challenge

```bash
curl -sS -i 'https://agent-api.degov.ai/v2/proposals?limit=1'
```

Without payment credentials or a partner token, this returns **402 Payment Required** and a `PAYMENT-REQUIRED` header. This unsigned request does not sign or settle a payment.

In v0.9.1, the challenge also describes the resource and includes Bazaar input/output schemas. Anonymous paid-route probes receive 402 before input validation, so a challenge alone does not prove that your parameters or identifiers are valid. Construct the actual request from OpenAPI.

To retrieve paid data, use an [issued partner token or an x402-capable wallet](authentication.md). [DeGov Agent Skills](../agent-skills/index.md) delegate payment authorization, spending controls, signing, and settlement verification to MetaMask Agent Wallet.

## Next steps

- [Find active proposals](guides/find-active-proposals.md).
- [Resolve an exact proposal URL](guides/resolve-external-proposal.md).
- [Read pagination](concepts/pagination.md) before traversing lists.
- If a request fails, use its [error code and recovery guidance](concepts/errors.md).
