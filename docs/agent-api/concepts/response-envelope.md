---
description: "DeGov Agent API response envelopes for resources, lists, pagination, and readiness metadata."
---

# Response Envelope

Single-resource responses place the resource directly in `data`:

```json
{ "data": { "daoId": "example-dao", "name": "Example DAO" }, "meta": { "requestId": "req-example" } }
```

List responses place rows in `data.items`:

```json
{
  "data": { "items": [] },
  "meta": {
    "requestId": "req-example",
    "generatedAt": "2026-08-12T06:42:29.362Z",
    "readiness": { "status": "ready", "currentRevision": "revision" },
    "page": { "limit": 25, "hasMore": false }
  }
}
```

`meta.page` appears on paginated lists. `meta.readiness` appears when publication state is relevant; do not assume every response contains it. `generatedAt` describes response creation, while `dataAsOf` describes underlying data freshness.
