---
description: "Read DeGov API detail responses and top-level cursor-paginated collections."
---

# Response Envelope

Detail responses contain one object in `data`. This is a shortened illustrative excerpt:

```json
{
  "data": {
    "daoId": "uniswapgovernance-eth",
    "name": "Uniswap"
  }
}
```

Collections contain a `data` array and a top-level `page`. An empty result is:

```json
{
  "data": [],
  "page": {
    "hasMore": false,
    "nextCursor": null
  }
}
```

When `hasMore` is true, pass `nextCursor` unchanged to the same route, filters, and sort. See [pagination](pagination.md).

The API does not wrap records in `items` or expose operational metadata. Resource records can contain `dataAsOf`; read it as source-observation provenance rather than a global freshness guarantee. See [data availability](readiness-and-coverage.md).
