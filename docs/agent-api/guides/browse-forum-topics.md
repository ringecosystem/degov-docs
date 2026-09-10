---
description: "Search governance forum topics and use returned source URLs for full discussion evidence."
---

# Browse Forum Topics

Use the standard paid forum list to find governance-related discussions:

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  'https://agent-api.degov.ai/v2/forum-topics?daoId=uniswapgovernance-eth&query=governance&sort=commentCountDesc&minCommentCount=1&limit=25'
```

Read topics from `data`. Use `title`, `excerpt`, `author`, `commentCount`, and `lastPostedAt` to choose relevant discussions. `topicId` is useful for deduplication. Follow top-level `page` for more results.

`query` searches titles only. The list already targets governance-related topics. Other sorts are `lastPostedAtDesc` (default) and `createdDesc`; filter activity with `lastPostedFrom` and `lastPostedTo` within a 365-day window.

The public API has no standalone topic-detail endpoint. Open `source.url` to read the full thread. Excerpts and opening-post authors are best effort and may be null; do not infer discussion contents from a title. Inspect DAO `availableData` for resource availability, and use the official forum when coverage is insufficient.
