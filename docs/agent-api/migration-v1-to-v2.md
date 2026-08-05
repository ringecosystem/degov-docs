---
description: "DeGov Agent API migration guide — map v1 endpoints and workflows to the proposed v2 contract."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**; v1 remains the stable surface. See [Agent API overview](index.md).

# Migration Guide: v1 → v2

v2 is a **new contract**, not a rename of v1. v1 stays available and supported. Use this map to plan your migration.

## Endpoint mapping

| v1 endpoint | v2 replacement | Notes |
| --- | --- | --- |
| `GET /v1/meta/pricing` | `GET /v2/meta/pricing` | Same purpose; v2 returns route ids like `v2.proposals.list`. |
| `GET /v1/daos` | `GET /v2/daos` | v2 items add coverage, vote status, and counts. |
| `GET /v1/system/freshness` | `GET /v2/meta/data-status` | Global or per-DAO; v2 separates readiness from coverage. |
| `GET /v1/activity` | `GET /v2/events` or `GET /v2/signals` | No fuzzy one-to-one: choose raw events or curated signals. |
| `GET /v1/governance-events` | `GET /v2/events` | RFC 3339 `from`/`to` instead of `start_ms`/`end_ms`; window cap 90 days. |
| `GET /v1/governance-signals` | `GET /v2/signals` | Adds `surface`, `priorityMin`, typed evidence. |
| `GET /v1/proposals/lookup` | `GET /v2/proposals/resolve` | Returns real `match.type` instead of fabricated confidence. |
| `GET /v1/items/proposal/:externalId` | `GET /v2/proposals/:proposalKey` | Requires a `proposalKey` from a list/resolve/event/signal. |
| `GET /v1/items/forum_topic/:externalId` | `GET /v2/forum-topics/:topicKey` | Requires a `topicKey` from the forum list. |
| `GET /v1/daos/:daoId/brief` | Compose `GET /v2/daos/:daoId` + `/v2/proposals` + `/v2/events` | No brief endpoint in v2; assemble what you need. |
| `GET /v1/daos/:daoId/proposals/:source/:externalId/evidence` | `GET /v2/proposals/:proposalKey/evidence` | Same purpose, key-based addressing. |

## New capabilities in v2

| Capability | Endpoint |
| --- | --- |
| Vote result, choice totals, quorum | `GET /v2/proposals/:proposalKey/votes/summary` |
| Per-voter ballot rows (paginated) | `GET /v2/proposals/:proposalKey/votes` |
| DAO monthly trends | `GET /v2/daos/:daoId/timeline` |
| DAO voter ranking | `GET /v2/daos/:daoId/voters` |
| Cross-DAO voter profile | `GET /v2/voters/:voterIdentity` |
| Voter vote history | `GET /v2/voters/:voterIdentity/votes` |
| Forum topic directory | `GET /v2/forum-topics` |

## What changed in the contract

| Concern | v1 | v2 |
| --- | --- | --- |
| Parameter validation | Clamps out-of-range values | Rejects with `VALIDATION_ERROR` |
| Time format | `start_ms` / `end_ms` (epoch ms) | `from` / `to` (RFC 3339 UTC) |
| Pagination | Legacy `total`/offset semantics | Cursor pages, `hasMore`, no totals |
| Identifiers | `kind + externalId` | Opaque `proposalKey` / `topicKey` |
| Data state | `freshness.cacheStatus` | `readiness` + per-resource `coverageStatus` |
| Numbers | Mixed | Decimal strings for exact values |
| Confidence | Fabricated `matchConfidence` | Real `match.type` in resolve |

## Migration checklist

1. Replace `start_ms`/`end_ms` with RFC 3339 `from`/`to`.
2. Add cursor handling: read `meta.page.nextCursor`, pass as `cursor`, restart on `CURSOR_INVALID`/`CURSOR_STALE`.
3. Fetch `proposalKey` from a list/resolve/event/signal before calling detail endpoints.
4. Choose `events` or `signals` explicitly instead of `activity`.
5. Treat decimal strings as exact values; don't round.
6. Check `readiness`/`coverageStatus` and say so when data is partial.
7. Use `votes/summary` for results instead of paging `votes`.
8. Use `evidence` only for citation/audit answers.
