---
description: "DeGov Agent API timestamps and numbers — RFC 3339 UTC timestamps and exact decimal strings for voting power and quorum."
---

# Timestamps & Numbers

## Timestamps

API timestamps are **RFC 3339 UTC** strings:

```
2026-08-05T07:30:00.000Z
```

- `generatedAt` — when this response was produced.
- `dataAsOf` — how fresh the underlying data is.
- Resource timestamps (`createdAt`, `startAt`, `endAt`, `votedAt`, ...) — source event times.
- Time-window query parameters (`from`, `to`) use the same format and define a **half-open interval** `[from, to)`: `from` is inclusive, `to` is exclusive.

## Numbers

Values that represent money, voting power, or other exact quantities are returned as **decimal strings**, not JSON numbers:

```json
{
  "totals": { "votingPower": "1234567.890123456789012345" },
  "quorum": { "progress": "0.7342", "reached": true }
}
```

- Strings preserve full precision (up to 78-digit decimals where the chain provides it).
- JSON numbers would lose precision on large values — never parse them as `Number` for arithmetic.
- Governance aggregates such as voting power, vote-summary totals, timeline values, and voter counts are decimal strings. Ordinary metadata such as `rank` and global data-status counters can be JSON numbers.

## Rules for callers

1. Compare timestamps as ISO strings or parse to epoch millis explicitly — don't rely on locale parsing.
2. Treat every numeric-looking string as a decimal; format for display, don't round for logic.
3. Quorum comparisons should use `quorum.reached` / `quorum.progress` from the API, not re-derive them client-side.
