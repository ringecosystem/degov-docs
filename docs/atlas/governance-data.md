---
description: "DeGov Atlas governance data — coverage, freshness, bounded collections, and pagination semantics."
---

# Atlas Governance Data

This page explains how Atlas represents governance data so operators, researchers, and integrators can interpret what they see.

## Coverage

- Atlas covers the DAOs DeGov indexes across on-chain (Snapshot/Tally-style) and off-chain (forum) governance.
- Each DAO reports coverage metadata: whether vote data and forum data are available, and a coverage status (`complete` / `partial`).
- A DAO or proposal shown as `partial` may be missing fields (for example, proposal body text) — check the coverage field rather than assuming completeness.

## Freshness and generation awareness

- Atlas serves one published data generation per request.
- DAO-owned surfaces come from that active build; candidates in the middle of a rebuild do not affect 404s or availability.
- If a rebuild or backfill is in progress, responses carry freshness/coverage indicators so you can tell that data is partial.
- Rollback of a bad generation restores the previous snapshot without row-level rewrites.

## Bounded collections

Atlas keeps list/detail payloads bounded so pages stay fast:

| Collection | Bound |
| --- | --- |
| Proposal votes page | `limit` default 100, max 500; `offset` pagination; response includes `totalCount`, `nextOffset`, `truncated`, `coverage` |
| Voter profile votes | `vote_limit` default 20, max 100; `vote_offset` pagination |
| DAO timeline | at most the latest 240 monthly buckets |
| DAO quorum page | `limit` default 200, max 500 |

Where a `contract=v2` query parameter is accepted, the response uses the v2 envelope with independent proposal/requirement totals, truncation, and coverage.

## Relationship to the Agent API

Atlas is the human-facing surface over the same data layer as the [Agent API](../agent-api/index.md). Agents and integrations that need machine-readable, paginated, authenticated access — including vote results, voter profiles, and signals — should use the Agent API instead of scraping Atlas.
