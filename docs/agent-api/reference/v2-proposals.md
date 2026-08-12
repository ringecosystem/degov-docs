---
description: "Reference for DeGov Agent API proposal discovery, detail, votes, and evidence resources."
---

# Proposals

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/proposals` | standard | Filter and sort proposals |
| GET | `/v2/proposals/resolve` | standard | Resolve URL, title, or external ID |
| GET | `/v2/proposals/:proposalKey` | plus | Proposal body and lifecycle detail |
| GET | `/v2/proposals/:proposalKey/votes/summary` | plus | Vote totals, quorum, and choices |
| GET | `/v2/proposals/:proposalKey/votes` | plus | Paginated individual ballots |
| GET | `/v2/proposals/:proposalKey/evidence` | plus | Provenance, sources, and quality signals |

Proposal list filters include DAO, provider, proposer, lifecycle status, outcome, RFC 3339 time window, sort, limit, and cursor. Resolve accepts exactly one of `url`, `title`, or `externalId`, plus optional narrowing filters.

Keys are opaque and must come from list, resolve, event, or signal results. Vote rows accept `order=power|time`, `limit`, and `cursor`.

See [Find Active Proposals](../guides/find-active-proposals.md) and [Inspect Proposal Votes](../guides/inspect-proposal-votes.md).
