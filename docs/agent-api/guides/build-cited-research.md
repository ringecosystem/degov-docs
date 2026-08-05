---
description: "Guide — build a research brief with citable sources and explicit data limitations using the evidence endpoint."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Build a Cited Research Brief

**User goal:** "Generate a research summary of this proposal with verifiable sources and clear statements about data limitations."

## Prerequisites

- Tier: `plus` (paid).
- Auth: x402 or partner token.
- Key: you already have `proposalKey` (from a list, resolve, event, or signal).

## Call graph

```text
GET /v2/proposals/:proposalKey              (plus) — what the proposal says
GET /v2/proposals/:proposalKey/votes/summary (plus) — how the vote went
GET /v2/proposals/:proposalKey/evidence      (plus) — where the facts come from
```

## 1. Get the proposal body

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_..."
```

## 2. Get the vote result

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_.../votes/summary"
```

```json
{
  "data": {
    "totals": { "votes": "81234", "uniqueVoters": "4521", "votingPower": "1234567.890123456789012345" },
    "quorum": { "raw": "100K", "progress": "0.7342", "reached": true },
    "choices": [ { "key": "1", "label": "For", "votes": "60123", "votingPower": "812345.67" } ]
  }
}
```

## 3. Get citable evidence (optional but recommended for research)

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_.../evidence"
```

```json
{
  "data": {
    "proposal": { "proposalKey": "p1_...", "title": "Increase Protocol Budget", "sourceUrl": "https://..." },
    "provenance": [
      { "field": "title", "source": "serving.proposals", "provider": "snapshot", "observedAt": "2026-08-05T07:20:00.000Z" }
    ],
    "intelligence": { "status": "available", "artifactVersion": "proposal_dossier_v1", "sourceRefs": [], "warnings": [] },
    "qualityFlags": ["registry_body_available"],
    "warnings": []
  }
}
```

## 4. How to interpret

- **P3 (detail)** answers "what does the proposal say?".
- **P4 (votes/summary)** answers "what was the result?".
- **P6 (evidence)** answers "where did these facts come from, can I trust them, and what is missing?".
- `warnings` lists missing or uncertain fields; `qualityFlags` lists what is reliable.
- The evidence endpoint is **not** a duplicate of the detail endpoint. It exists for citation and audit. A normal chat answer does not need it.

## 5. Next actions

- Cite `sourceUrl` / `sourceRefs` in the report.
- State `coverageStatus` and `warnings` explicitly when the data is partial.
- For per-voter detail, use `GET /v2/proposals/:proposalKey/votes` — see [Inspect Proposal Votes](inspect-proposal-votes.md).

## 6. Failure recovery

- `404 NOT_FOUND` — the proposal is no longer in coverage; fall back to web sources.
- `402` / `429` — pay / back off.
- `readiness` non-`ready` — note it in the report rather than presenting data as complete.
