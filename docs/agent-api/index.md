---
description: "DeGov Agent API — production governance data for proposals, votes, voters, forum topics, events, and signals."
---

# Agent API

The DeGov Agent API is the production, machine-readable interface to DeGov's governance data. It is designed for agents and integrations that need structured, source-aware DAO information.

**v2 is the current API for new integrations.** v1 remains available as a frozen compatibility surface; use the [migration runbook](migration-v1-to-v2.md) when moving an existing integration.

The same curated data powers [DeGov Atlas](../atlas/index.md). The API exposes it through focused resources with explicit pagination, freshness, coverage, pricing, and errors.

## Base URL

```text
https://agent-api.degov.ai
```

The `/v2` prefix is part of the current HTTP contract.

## Data status

The service can be available while a projection is still backfilling. Check the free `GET /v2/meta/data-status` resource before a research session and read `coverageStatus` and `dataAsOf` instead of treating backfilling as an outage.

## Endpoint groups

| Group | Resources | Tier |
| --- | --- | --- |
| Metadata | Pricing and data status | free |
| DAOs | Directory and detail | free |
| Proposals, forum, events, signals | Discovery and feeds | standard |
| Proposal details, votes, evidence, timelines, voters | Deep research | plus |

Prices are returned by the free [pricing resource](pricing-and-rate-limits.md) and may change.

## Start here

1. [Quickstart](quickstart.md) — make free calls and inspect a real 402 challenge.
2. [Authentication](authentication.md) — partner tokens and x402.
3. [Concepts](concepts/index.md) — response envelopes, keys, pagination, coverage, and errors.
4. [Guides](guides/index.md) — task-oriented research workflows.
5. [API reference](reference/index.md) — endpoints grouped by resource.

## Machine-readable contracts

- [Agent API v2 OpenAPI](https://agent-api.degov.ai/openapi/agent-v2.json)
- [Agent API v1 OpenAPI](https://agent-api.degov.ai/openapi/agent-v1.json)
- [Combined public OpenAPI](https://agent-api.degov.ai/openapi.json)

The current v2 OpenAPI is useful for route discovery, but it does not yet contain enough schemas, parameters, security declarations, and examples to replace the human-readable reference.
