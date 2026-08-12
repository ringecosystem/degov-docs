---
description: "Reference for DeGov Agent API voter ranking, profile, and voting-history resources."
---

# Voters

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/daos/:daoId/voters` | plus | Rank voters within one DAO |
| GET | `/v2/voters/:voterIdentity` | plus | Cross-DAO voter profile |
| GET | `/v2/voters/:voterIdentity/votes` | plus | Paginated voting history |

Ranking accepts `limit` and cursor. History additionally supports DAO and RFC 3339 time filters. The API resource handle is `voterIdentity`; do not require a separate `voterAddress` field.

Voting power and analytics counts are exact decimal strings. See [Research Voters](../guides/research-voters.md).
