---
description: "Research DAO voter rankings, cross-DAO profiles, and voting history."
---

# Research Voters

**Tier:** plus.

1. Rank voters within a DAO.
2. Capture the returned `voterIdentity`.
3. Open the cross-DAO profile.
4. Fetch vote history only when the individual records matter.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/daos/example-dao/voters?limit=25"

curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/voters/voter%3A0xabc"

curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/voters/voter%3A0xabc/votes?daoId=example-dao&limit=50"
```

Ranking and vote-history lists use `data.items`. Treat `voterIdentity` as the resource handle; ranking and profile responses do not promise a separate `voterAddress` field.
