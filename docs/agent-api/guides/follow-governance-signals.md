---
description: "Guide — follow curated governance signals and drill into the most urgent proposal."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This guide describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Follow Governance Signals

**User goal:** "What are the highest-priority governance signals right now, and what is the most urgent proposal about?"

## Prerequisites

- Tier: `standard` (paid).
- Auth: x402 or partner token.
- Window `from`/`to` required (max 90 days).

## Call graph

```text
GET /v2/signals                 (standard)
  -> returns proposalKey on each signal
  -> GET /v2/proposals/:proposalKey         (plus, for details)
  -> GET /v2/proposals/:proposalKey/votes/summary  (plus, for results)
```

## 1. Query high-priority signals

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/signals?from=2026-08-04T00:00:00Z&to=2026-08-06T00:00:00Z&priorityMin=80&surface=agent"
```

## 2. Relevant response excerpt

```json
{
  "data": [
    {
      "signalId": "sig-...",
      "signalType": "proposal_deadline_reminder",
      "priority": { "score": 92, "band": "high" },
      "daoId": "ens-dao",
      "title": "Increase Protocol Budget",
      "deadlineAtMs": "2026-08-07T12:00:00.000Z",
      "proposalKey": "p1_eyJkYW9JZCI6ImVucy1kYW8iLCJwcm92aWRlciI6InNuYXBzaG90IiwiZXh0ZXJuYWxJZCI6ImFiYzEyMyJ9",
      "summary": "Voting ends in under 48 hours"
    }
  ],
  "meta": { "page": { "limit": 50, "hasMore": false } }
}
```

## 3. How to interpret

- Signals are **curated, deduplicated, scored** items — the `surface` parameter selects the audience (`agent`, `atlas_latest`, `atlas_priority`, `telegram_realtime`).
- `priority.score` (0–100) and `priority.band` drive triage; don't re-derive importance client-side.
- `proposalKey` lets you jump straight to the underlying proposal.

## 4. Next actions

- Details: `GET /v2/proposals/:proposalKey` (plus).
- Results: `GET /v2/proposals/:proposalKey/votes/summary` (plus).
- If you need the **raw** event timeline instead of curated signals, use `GET /v2/events` — see [Events vs Signals](../reference/v2.md#events-vs-signals).

## 5. Failure recovery

- `400 WINDOW_TOO_LARGE` — narrow the window to ≤ 90 days.
- `400 VALIDATION_ERROR` — check `surface` and `priorityMin` values.
- `402` / `429` — pay / back off as usual.

## Choosing between events and signals

| Endpoint | Answers | Shape |
| --- | --- | --- |
| `/v2/events` | "What governance events happened in this window?" | Raw event timeline with `eventType` and timestamps |
| `/v2/signals` | "What should I pay attention to?" | Deduplicated, scored, surface-specific |
