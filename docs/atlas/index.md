---
description: "DeGov Atlas — governance intelligence: DAO directories, proposal details, votes, and voter profiles."
---

# DeGov Atlas

DeGov Atlas is the public governance intelligence surface of DeGov.AI. It turns distributed on-chain and off-chain governance activity into shared context: what proposals exist, how votes went, who participates, and what is happening across the ecosystem.

Atlas is a public web application — no authentication or payment is required to browse it.

## What you can do with Atlas

- **DAO directory:** discover covered DAOs and their governance footprint.
- **Proposal details:** read proposal pages, lifecycle status, and outcomes.
- **Vote breakdowns:** per-proposal vote totals, choice distribution, and coverage.
- **Voter profiles:** per-voter participation across DAOs, including vote history.
- **Governance feed:** recent proposals and forum activity across the ecosystem.
- **DAO timelines:** monthly proposal and vote trends.

## Data semantics

Atlas reads the same curated data layer as the [Agent API](../agent-api/index.md):

- Data is **generation-aware**: Atlas serves a consistent published snapshot per request; in-progress rebuilds do not cause half-old/half-new reads.
- Detail collections are bounded (default 100, maximum 500 for votes; profile vote pages default 20, maximum 100). Responses carry page metadata (`totalCount`, `nextOffset`, `truncated`) and coverage.
- Monthly timeline aggregation returns at most the latest 240 months.
- See [Governance Data](governance-data.md) for coverage and freshness semantics.

## Access

- Live site: [atlas.degov.ai](https://atlas.degov.ai)
- API surface: public `/atlas/*` endpoints on the DeGov backend; machine-readable contract at `/openapi/atlas.json`.

## For agents and partners

If you are building an agent or integration, prefer the [Agent API](../agent-api/index.md): it offers typed, paginated, authenticated access to the same data with explicit readiness, coverage, pricing, and error semantics.
