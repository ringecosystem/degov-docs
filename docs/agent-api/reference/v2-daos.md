---
description: "Reference for DeGov Agent API DAO directory, detail, and timeline resources."
---

# DAOs

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/daos` | free | Discover covered DAOs |
| GET | `/v2/daos/:daoId` | free | Read one DAO summary |
| GET | `/v2/daos/:daoId/timeline` | plus | Aggregate monthly proposal or vote activity |

The directory supports `hasVoteData`, `hasForumData`, `coverageStatus`, `limit`, and `cursor`. Timeline requires `metric=proposals_created|votes_cast`, accepts `fromMonth` and `toMonth`, and is limited to 240 months.

```bash
curl -s "https://agent-api.degov.ai/v2/daos?hasVoteData=true&limit=50"
curl -s https://agent-api.degov.ai/v2/daos/example-dao
curl -H "x-degov-api-token: <token>" "https://agent-api.degov.ai/v2/daos/example-dao/timeline?metric=proposals_created&fromMonth=2026-01&toMonth=2026-08"
```
