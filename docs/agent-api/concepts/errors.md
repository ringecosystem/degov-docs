---
description: "DeGov Agent API error model — stable error codes, HTTP status mapping, and recovery actions."
---

!!! warning "Proposed Agent API v2 — not yet available"
    This page describes the proposed v2 contract. The v2 endpoints are **not live yet**. See [Agent API overview](../index.md).

# Errors

Every error response uses a stable envelope:

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Proposal was not found",
    "details": { "resource": "proposal" }
  },
  "meta": { "requestId": "req-01J..." }
}
```

`requestId` is echoed from the failed request so you can reference it in bug reports.

## Error codes

| HTTP | Code | Meaning | Recovery |
| --- | --- | --- | --- |
| 400 | `VALIDATION_ERROR` | A parameter is missing, malformed, or out of range | Fix the parameter per the endpoint reference |
| 400 | `WINDOW_TOO_LARGE` | A `from`/`to` window exceeds the endpoint's maximum | Narrow the window (e.g. ≤ 90 days for feeds) |
| 400 | `CURSOR_INVALID` | Cursor does not match this endpoint/filters/sort | Restart from the first page |
| 401 | `UNAUTHORIZED` | Missing or invalid credentials | Check the token / payment path |
| 402 | `PAYMENT_REQUIRED` | x402 challenge — payment required for a paid endpoint | Pay per the challenge and retry; see [Authentication](../authentication.md) |
| 403 | `FORBIDDEN` | Credentials valid but scope insufficient for this tier | Request the required scope on your partner token |
| 404 | `NOT_FOUND` | Resource not in coverage | Verify the key/identity; it may have left coverage |
| 409 | `PAYMENT_CONFLICT` | Payment idempotency conflict | Retry with the same payment reference |
| 409 | `CURSOR_STALE` | Data was rebuilt between pages | Restart from the first page |
| 422 | `CANDIDATE_BUDGET_EXCEEDED` | The query's candidate set exceeds server limits | Narrow filters (add `daoId`, tighten window/status) |
| 429 | `RATE_LIMITED` | Short-window rate limit exceeded | Back off and retry with exponential delay |
| 429 | `QUOTA_EXCEEDED` | Monthly quota exhausted | Upgrade plan or wait for the next period |
| 500 | `INTERNAL_ERROR` | Server-side failure | Retry later; report `requestId` if it persists |

## Notes

- `VALIDATION_ERROR` is strict in v2: out-of-range values are rejected, **not** silently clamped (unlike v1).
- `404` is about coverage, `readiness` non-`ready` is not a `404` — see [Readiness & Coverage](readiness-and-coverage.md).
- Business-level errors (400/404/422) count against monthly quota; auth/payment/rate-limit errors do not — see [Pricing & Rate Limits](../pricing-and-rate-limits.md).
