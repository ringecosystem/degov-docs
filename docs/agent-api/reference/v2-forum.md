---
description: "Current DeGov public API reference for forum topics."
---

# Forum topics

The [live OpenAPI specification](https://agent-api.degov.ai/openapi.json) is authoritative for methods, parameters, schemas, and payment metadata. Examples below are illustrative snapshots, not current governance claims. Replace opaque placeholders with IDs returned by the API. These are paid resources: unsigned curl examples return 402 unless called with an issued partner token or through an authorized x402 wallet. See [authentication](../authentication.md).

## `GET /v2/forum-topics`

Lists governance-related forum topics.

| Name              | Type      | Meaning                                                  |
| ----------------- | --------- | -------------------------------------------------------- |
| `query`           | string    | Case-insensitive substring of forum-topic title          |
| `daoId`           | string    | Exact DAO slug                                           |
| `provider`        | string    | Exact provider                                           |
| `lastPostedFrom`  | date-time | Inclusive latest-post lower bound                        |
| `lastPostedTo`    | date-time | Exclusive latest-post upper bound                        |
| `minCommentCount` | int       | Minimum posts after the opening topic post               |
| `sort`            | enum      | `lastPostedAtDesc`, `createdDesc`, or `commentCountDesc` |
| `limit`           | int       | 1-100, default 25                                        |
| `cursor`          | string    | Cursor from the preceding page                           |

Default sort: `lastPostedAtDesc`.

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/forum-topics?query=Aave%20V4&daoId=aavedao-eth&sort=commentCountDesc&limit=5"
```

Example item:

```json
{
  "topicId": "t1_<opaque>",
  "daoId": "aavedao-eth",
  "source": {
    "provider": "discourse",
    "externalId": "24293",
    "url": "https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293"
  },
  "title": "[ARFC] Aave V4 Activation on Ethereum Mainnet",
  "excerpt": "This ARFC proposes activating Aave V4 on Ethereum mainnet after the required technical and risk reviews.",
  "author": "alice",
  "category": { "id": "4", "name": "Governance" },
  "tags": [],
  "commentCount": 45,
  "likeCount": 112,
  "viewCount": 6949,
  "createdAt": "2026-03-13T18:00:12.676Z",
  "lastPostedAt": "2026-09-01T09:37:38.182Z",
  "dataAsOf": "2026-09-03T09:42:18.000Z"
}
```

`excerpt`, `author`, `category`, and either governance timestamp can be `null`. The excerpt is
either published by the forum or deterministically derived from the opening post; the author is the
opening-post identity when available. There is no topic-detail endpoint. Search matches titles only.
Open `source.url` when the user asks what the discussion actually says and the excerpt is
insufficient.
