---
description: "Traverse live DeGov governance collections with opaque cursors and consistent filters."
---

# Pagination

All public collection operations use `limit` and `cursor`. `limit` is an integer from **1 to 100**, defaulting to **25**.

1. Make the first request without a cursor.
2. Read records from `data`.
3. If `page.hasMore` is true, use `page.nextCursor` for the next request.
4. Preserve the route, filters, and sort. Stop when `hasMore` is false and `nextCursor` is null.

Pass cursors unchanged. Do not decode, shorten, construct, or reuse them for another request shape. There is no separate offset-based participant-ranking contract.

Pagination is a live keyset traversal. Unrelated publications do not expire cursors, but inserts and updates can move matching records while you page. A traversal is not a frozen point-in-time snapshot. If results change during a full scan, restart and reconcile by stable resource ID rather than claiming snapshot completeness.

When both bounds are supplied, proposal creation, forum activity, and voter-history time windows must be ordered and at most **365 days**. Lower `From` bounds are inclusive; upper `To` bounds are exclusive. A single bound filters only that side of the interval; use both for a reproducible research interval. See the exact operation in [OpenAPI](https://agent-api.degov.ai/openapi.json).
