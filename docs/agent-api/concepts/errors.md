---
description: "Recover from current DeGov public API validation, missing data, x402, rate limits, and server errors."
---

# Errors

Documented non-payment errors use `error` and `requestId`:

```json
{
  "error": {
    "code": "INVALID_ARGUMENT",
    "message": "Request validation failed",
    "details": {
      "issues": [{ "path": "/limit", "message": "must be >= 1", "keyword": "minimum" }]
    }
  },
  "requestId": "req-example"
}
```

`details` is optional. Preserve `requestId` when reporting a failure.

| Status / code | Meaning | Recovery |
| --- | --- | --- |
| 400 `INVALID_ARGUMENT` | Unknown, malformed, conflicting, or out-of-range input | Correct the request against OpenAPI |
| 402 Payment Required | A paid resource needs a valid payment or partner credential | Inspect `PAYMENT-REQUIRED`; use the wallet's authorized workflow |
| 404 `NOT_FOUND` | Public resource not found | Obtain the correct ID from discovery or the exact resolver |
| 404 `DATA_NOT_AVAILABLE` | A normalized vote summary is unavailable | Try vote rows or the official source; disclose the gap |
| 413 `INVALID_ARGUMENT` | Resolver body exceeds the size limit | Send only the documented exact lookup body |
| 415 `INVALID_ARGUMENT` | Resolver body is not supported JSON | Set `Content-Type: application/json` |
| 429 `RATE_LIMITED` | Rate limit or monthly quota exhausted | Honor `Retry-After` and inspect the message |
| 500 `INTERNAL_ERROR` | Unexpected service failure | Keep the request ID and retry later |
| 503 `TEMPORARILY_UNAVAILABLE` | The resource cannot currently be served | Retry later or use an official source |

A 402 follows the x402 protocol envelope, not the non-payment error schema. In v0.9.1, anonymous paid-route requests receive this challenge before body parsing, validation, or data-availability checks. An invalid placeholder, missing resolver body, or malformed query can therefore return 402 instead of a validation error. Requests carrying credentials are still validated before access checks; free routes retain normal validation. An invalid or insufficient partner token can also return a challenge after valid input. Do not invent payment credentials or blindly repeat signed requests.

Unknown paths can return the framework's JSON 404 shape (`message`, `error`, `statusCode`) instead. Recover using the current [OpenAPI contract](https://agent-api.degov.ai/openapi.json); avoid guessing undocumented endpoints.
