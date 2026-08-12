---
description: "Reference for DeGov Agent API forum topic discovery and detail resources."
---

# Forum

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/forum-topics` | standard | Search covered governance discussions |
| GET | `/v2/forum-topics/:topicKey` | plus | Read one normalized topic |

The list supports DAO, provider, governance relevance, updated-time window, minimum replies, sort, limit, and cursor. Sort values are `updatedDesc`, `createdDesc`, and `repliesDesc`.

Treat `topicKey` as opaque. Structured forum coverage varies by DAO; check `hasForumData` first.
