---
description: "Resolve an exact proposal URL or complete source identity using a POST JSON request."
---

# Resolve an External Proposal

Use **`POST /v2/proposals/resolve`** when you have an exact proposal URL or its complete source identity but no public `proposalId`. The resolver returns one proposal item in `data`.

## By canonical URL

```bash
curl -sS -X POST \
  -H 'Content-Type: application/json' \
  -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  --data '{"by":"url","url":"https://snapshot.org/#/uniswapgovernance.eth/proposal/0x5ae3426216321df66a67eb677874b725f80e51888ad2da72b382b21669c554ee"}' \
  'https://agent-api.degov.ai/v2/proposals/resolve'
```

## By complete source identity

Send all four fields; use exact values from the provider or an API response:

```json
{
  "by": "source_id",
  "daoId": "uniswapgovernance-eth",
  "provider": "snapshot",
  "externalId": "0x5ae3426216321df66a67eb677874b725f80e51888ad2da72b382b21669c554ee"
}
```

These forms are mutually exclusive and reject extra fields. A title is not a resolver input: search proposal titles with `GET /v2/proposals?query=...` and narrow by DAO when possible.

Keep `data.proposalId` unchanged for proposal detail and vote requests. A `404 NOT_FOUND` means the exact source identity was not found; verify the official source instead of inventing an ID. For x402 payment, preserve the POST method and exact JSON body during the wallet-managed retry.
