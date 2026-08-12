---
description: "Browse governance-related forum topics and open a selected discussion."
---

# Browse Forum Topics

**Tier:** standard list, plus detail.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/forum-topics?daoId=example-dao&governanceRelated=true&sort=repliesDesc&limit=25"
```

Read topics from `data.items`. Use the title, summary, URL, reply count, updated time, and relevance to select useful discussions. Capture `topicKey` and pass it unchanged to detail:

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/forum-topics/t1_opaque"
```

Forum coverage varies by DAO. Check `hasForumData` during DAO discovery and use the official forum directly when structured coverage is unavailable.
