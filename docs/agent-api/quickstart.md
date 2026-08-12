---
description: "DeGov Agent API quickstart — check production data, list DAOs, and understand paid access."
---

# Quickstart

The first two calls are free and require no wallet or token.

## 1. Check data status

```bash
curl -s https://agent-api.degov.ai/v2/meta/data-status
```

```json
{
  "data": {
    "scope": "global",
    "counts": { "daos": 883, "proposals": 66437, "voteProposals": 66437 },
    "coverageStatus": "backfilling",
    "dataAsOf": "2026-08-12T06:15:50.433Z",
    "projections": { "pending": 0, "running": 10, "dead": 0 }
  },
  "meta": {
    "requestId": "req-example",
    "generatedAt": "2026-08-12T06:42:29.362Z",
    "dataAsOf": "2026-08-12T06:15:50.433Z"
  }
}
```

The values above are a fixed example. Use the live response for current counts and status. `backfilling` means the API is available while data coverage is still being completed.

## 2. List DAOs

```bash
curl -s "https://agent-api.degov.ai/v2/daos?hasVoteData=true&limit=3"
```

Lists use `data.items`, with pagination in `meta.page`:

```json
{
  "data": {
    "items": [
      {
        "daoId": "example-dao",
        "name": "Example DAO",
        "hasVoteData": true,
        "hasForumData": true,
        "coverageStatus": "ready"
      }
    ]
  },
  "meta": {
    "page": { "limit": 3, "hasMore": true, "nextCursor": "opaque-cursor" }
  }
}
```

Copy `nextCursor` unchanged into the next request; never construct or decode it.

## 3. Inspect live pricing

```bash
curl -s https://agent-api.degov.ai/v2/meta/pricing
```

The response identifies every route as `free`, `standard`, or `plus`. At the time of this example, standard calls cost `0.005 USDC` and plus calls cost `0.01 USDC` on Base. The live pricing response is authoritative.

## 4. See a paid-route challenge

Calling a paid route without credentials does not spend anything:

```bash
curl -i "https://agent-api.degov.ai/v2/proposals?daoId=example-dao&limit=1"
```

The API returns `402 Payment Required` and a `payment-required` header describing the x402 offer. Continue through either:

- a partner token in `x-degov-api-token`; or
- an x402-capable wallet that inspects, authorizes, signs, settles, and retries the request.

Do not copy a receiver address or price from documentation; use the challenge returned for that request.

## Next steps

- [Find active proposals](guides/find-active-proposals.md)
- [Inspect proposal votes](guides/inspect-proposal-votes.md)
- [Browse forum topics](guides/browse-forum-topics.md)
- [Authentication](authentication.md)
