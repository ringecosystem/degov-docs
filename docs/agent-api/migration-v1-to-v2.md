---
description: "Runbook for migrating an existing DeGov Agent API integration from v1 to current v2 resources."
---

# Migrate from v1 to v2

v2 is the current contract for new integrations. v1 remains available as a frozen compatibility surface without a published shutdown date.

## Before switching

1. Inventory the v1 routes, response fields, pagination, and authentication scopes your integration uses.
2. Confirm the partner token includes the required v2 paid scopes, or prepare an x402-capable wallet.
3. Add data-status and coverage handling.
4. Run v1 and v2 in parallel against representative DAOs before changing production traffic.

## Main changes

| Concern | v1 | v2 |
| --- | --- | --- |
| Lists | Legacy shapes | Rows in `data.items`, page in `meta.page` |
| Time windows | Epoch-millisecond parameters | RFC 3339 `from` and `to` |
| Resource identity | Provider kind and external ID | Opaque `proposalKey` and `topicKey` |
| Activity | Mixed activity resources | Explicit events or curated signals |
| Data state | Freshness fields | Publication readiness plus resource coverage |
| Exact values | Mixed number handling | Decimal strings for governance analytics |

## Route mapping

| v1 workflow | v2 workflow |
| --- | --- |
| DAO list/detail | `/v2/daos`, `/v2/daos/:daoId` |
| Freshness | `/v2/meta/data-status` |
| Activity/events/signals | `/v2/events` or `/v2/signals` |
| Proposal lookup | `/v2/proposals/resolve`, then proposal detail |
| DAO brief | Compose DAO detail, proposal list, and events as needed |
| Evidence | `/v2/proposals/:proposalKey/evidence` |

## Cutover and rollback

1. Compare key business outputs, not raw JSON equality.
2. Verify pagination to completion and restart behavior for stale cursors.
3. Confirm partial/backfilling states are disclosed rather than hidden.
4. Switch a small traffic segment, monitor errors and cost, then expand.
5. Keep the v1 path deployable until v2 behavior is verified; rollback routes traffic to v1 without changing stored v2 keys into guessed legacy identifiers.
