---
description: "Use the current DeGov Agent API for DAO discovery, proposals, votes, forum topics, participants, and voter history."
---

# Agent API

The DeGov Agent API gives agents and integrations structured DAO governance data with official source links. Start with free DAO discovery, then request the proposal, vote, forum, or voter evidence needed for your task.

Base URL: **`https://agent-api.degov.ai`**. The current public contract contains **11 operations** under `/v2`.

## When to use it

| Need | Resource | Access |
| --- | --- | --- |
| Find a DAO and inspect available data | DAO directory and detail | Free; no wallet or API key |
| Find proposals or resolve an exact proposal URL | Proposal list and resolver | Paid standard |
| Read proposal content and analyze ballots | Proposal detail, vote summary, and vote rows | Paid plus |
| Find governance discussions | Forum topic list | Paid standard |
| Research participation | DAO participants, voter profile, and voter history | Paid plus |

Paid calls accept x402 payment or an issued partner token. Prices and payment protocols are declared in the [OpenAPI contract](https://agent-api.degov.ai/openapi.json); the actual 402 challenge supplies the payment offer. See [pricing and rate limits](pricing-and-rate-limits.md).

The public API is focused on governance resources. Operational status, private feeds, executable calldata, evidence bundles, and timeline endpoints are outside this contract. Use returned official source URLs for primary evidence beyond the available fields. [Atlas](../atlas/index.md) provides its own human-facing activity views.

## Start here

1. [Quickstart](quickstart.md) — find a DAO without signing up or paying.
2. [Authentication](authentication.md) — free resources, partner tokens, and x402.
3. [Concepts](concepts/index.md) — identifiers, pagination, availability, and errors.
4. [Guides](guides/index.md) — focused research workflows.
5. [API reference](reference/index.md) — all 11 public operations.
6. [Agent Skills](../agent-skills/index.md) — install reusable research and security guidance.

## Contract and version

[OpenAPI](https://agent-api.degov.ai/openapi.json) is the authoritative specification for methods, paths, typed inputs, responses, errors, and payment metadata. [The V2 alias](https://agent-api.degov.ai/openapi/agent-v2.json) serves the same specification. Each operation has a unique `operationId` for generated clients and agent tools.

These docs follow [Agent API v0.9.1](https://github.com/ringecosystem/degov-agent-api/releases/tag/v0.9.1), released on 10 September 2026. API namespace `v2` and software release `v0.9.1` identify different things. This release keeps the 11 operations and successful response contracts, and improves anonymous x402 discovery; see [authentication](authentication.md).

A release tag does not itself upgrade every deployment. The live OpenAPI and actual response headers describe the deployment you are calling. Follow them when inspecting capabilities and offers.
