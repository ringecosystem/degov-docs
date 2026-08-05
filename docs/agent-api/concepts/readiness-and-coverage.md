---
description: "DeGov Agent API readiness and coverage — ready, backfilling, stale, unavailable, and how to interpret data completeness."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This page describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Readiness & Coverage

v2 separates two ideas that are easy to confuse: **how fresh/consistent the pipeline is** and **how complete the data is for a resource**.

## Readiness (pipeline state)

`meta.readiness.status` describes whether the serving data revision is consistent and safe to query:

| Status | Meaning | What to do |
| --- | --- | --- |
| `ready` | Data revision is fully published and consistent | Query normally |
| `backfilling` | A rebuild/backfill is in progress; serving still works but may be partial | Treat results as partial; re-check `data-status` later |
| `stale` | Latest source data has not been materialized yet | Results are older than expected; check `dataAsOf` |
| `unavailable` | No usable serving revision | Avoid paid queries; use the v1 surface or web sources |

Readiness is **not** a 404: a known resource that is still backfilling returns `200` with its data plus `readiness.status: "backfilling"`, not `404`.

## Coverage (data completeness)

Each resource carries its own `coverageStatus` describing data quality for that item or DAO — for example `complete` or `partial`. A DAO can be `ready` in pipeline terms while a specific proposal has `partial` coverage (e.g. body text missing because the provider did not expose it).

## Where to find them

```json
{
  "data": { "...": "..." },
  "meta": {
    "dataAsOf": "2026-08-05T07:29:30.000Z",
    "readiness": { "status": "ready" }
  }
}
```

- Global pipeline state: `GET /v2/meta/data-status` (free).
- Per-DAO pipeline state: `GET /v2/meta/data-status?daoId=ens-dao` (free).
- Per-resource coverage: the resource's own `coverageStatus` field.

## Rules of thumb for agents

1. Check `data-status` once before a research session; don't check it per request.
2. If `readiness` is not `ready`, say so in your answer instead of presenting partial data as complete.
3. If a resource reports `partial` coverage, note which fields are missing.
4. `404 NOT_FOUND` means the resource is not in coverage at all — not that it is temporarily unavailable.
