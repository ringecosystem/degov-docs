---
description: "All 11 current public DeGov API operations, access tiers, and authoritative OpenAPI discovery."
---

# API Reference

Base URL: `https://agent-api.degov.ai`. These are the **11 public operations** in the current V2 contract. [OpenAPI](https://agent-api.degov.ai/openapi.json) supplies the complete typed contract and each paid operation's `x-payment-info`.

| Method | Path | Access | Reference |
| --- | --- | --- | --- |
| GET | `/v2/daos` | Free | [DAOs](v2-daos.md) |
| GET | `/v2/daos/{daoId}` | Free | [DAOs](v2-daos.md) |
| GET | `/v2/daos/{daoId}/participants` | Plus | [Participants & Voters](v2-voters.md) |
| GET | `/v2/proposals` | Standard | [Proposals](v2-proposals.md) |
| POST | `/v2/proposals/resolve` | Standard | [Proposals](v2-proposals.md) |
| GET | `/v2/proposals/{proposalId}` | Plus | [Proposals](v2-proposals.md) |
| GET | `/v2/proposals/{proposalId}/vote-summary` | Plus | [Proposals](v2-proposals.md) |
| GET | `/v2/proposals/{proposalId}/votes` | Plus | [Proposals](v2-proposals.md) |
| GET | `/v2/forum-topics` | Standard | [Forum topics](v2-forum.md) |
| GET | `/v2/voters/{voterId}` | Plus | [Participants & Voters](v2-voters.md) |
| GET | `/v2/voters/{voterId}/votes` | Plus | [Participants & Voters](v2-voters.md) |

The [V2 OpenAPI alias](https://agent-api.degov.ai/openapi/agent-v2.json) serves the same specification. Only use documented operations; the public contract does not advertise application or operational routes.

- Inputs are strict: unknown fields, unsupported sort values, and invalid ranges return a validation error.
- All lists use `limit` from 1 to 100 (default 25) and opaque cursors.
- See [response envelopes](../concepts/response-envelope.md), [pagination](../concepts/pagination.md), and [errors](../concepts/errors.md).
- A generated client must handle x402 or an issued partner token for paid resources; an OpenAPI import alone does not authorize payment.
