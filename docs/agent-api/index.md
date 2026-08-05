---
description: "DeGov Agent API — a precise, machine-readable interface for DAO governance data: proposals, votes, voters, forum topics, events, and signals."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This section describes the proposed Agent API v2 contract. The v2 endpoints are **not live yet**. Until the v2 contract ships, the stable v1 endpoints described in the [v1 reference](reference/v1.md) remain the only available surface. Everything here is subject to review and change before launch.

# Agent API

The DeGov Agent API is a machine-readable interface over DeGov's governance data layer. It is designed for **agents, skills, and partners** that need precise, verifiable answers about DAO governance — not a general-purpose crawl of raw chain data.

The same curated data powers [DeGov Atlas](../atlas/index.md). The Agent API exposes it as narrow, resource-oriented endpoints with explicit pagination, freshness, coverage, and error semantics.

## Why v2 is different from v1

v1 (`/v1/*`) was designed as a small set of general endpoints: a mixed `activity` feed, a `brief`, and a generic `items/:kind/:externalId` lookup. v2 replaces that with **fine-grained, single-purpose endpoints**:

- One endpoint answers one question.
- Heavy fields (proposal body, live data, evidence) are opt-in per endpoint, never mixed into list responses.
- Every list endpoint uses cursor pagination with no misleading `total` counts.
- Every response carries `readiness` and `coverage` so callers know how much to trust the data.
- Proposals, forum topics, and voters are addressed by stable opaque keys returned by the API — callers never construct or guess identifiers.

## Base URL

```
https://agent-api.degov.ai
```

v1 endpoints live under `/v1/*`; the proposed v2 endpoints live under `/v2/*`. Machine-readable OpenAPI documents are published at:

- `/openapi/agent-v2.json`
- `/openapi/agent-v1.json`
- `/openapi/atlas.json`
- `/openapi.json` (combined public surfaces)

## Endpoint map

| Group | Endpoints | Tier |
| --- | --- | --- |
| Metadata | `/v2/meta/pricing`, `/v2/meta/data-status` | free |
| DAOs | `/v2/daos`, `/v2/daos/:daoId`, `/v2/daos/:daoId/timeline` | free / free / plus |
| Proposals | `/v2/proposals`, `/v2/proposals/resolve` | standard |
| Proposals (detail) | `/v2/proposals/:proposalKey`, `/votes/summary`, `/votes`, `/evidence` | plus |
| Forum | `/v2/forum-topics`, `/v2/forum-topics/:topicKey` | standard / plus |
| Feeds | `/v2/events`, `/v2/signals` | standard |
| Voters | `/v2/daos/:daoId/voters`, `/v2/voters/:voterIdentity`, `/v2/voters/:voterIdentity/votes` | plus |

## Start here

1. [Quickstart](quickstart.md) — make your first v2 call in five minutes.
2. [Authentication](authentication.md) — x402, partner tokens, and scopes.
3. [Concepts](concepts/proposal-and-topic-keys.md) — keys, pagination, readiness, errors.
4. [Guides](guides/find-active-proposals.md) — full workflows for real questions.
5. [API Reference](reference/v2.md) — the complete endpoint contract.
