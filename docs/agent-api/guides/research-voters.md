---
description: "Research DAO participants and cross-DAO voter history using returned voter identities."
---

# Research Voters

Start with a DAO's participant ranking, then select only the voter profiles or histories needed for the question. All three resources are paid plus operations.

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  'https://agent-api.degov.ai/v2/daos/uniswapgovernance-eth/participants?sort=votedProposalCountDesc&limit=5'
```

Read the `data` array. Preserve a returned `voterId`, URL-encode it when needed, and use it for detail and history:

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  "https://agent-api.degov.ai/v2/voters/$VOTER_ID"

curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  "https://agent-api.degov.ai/v2/voters/$VOTER_ID/votes?daoId=uniswapgovernance-eth&limit=25"
```

Participant ranking counts proposals with an effective latest vote. `latestEffectiveVoteAtDesc` is the alternative ranking sort. Both ranking and history use cursor pagination; history is newest first and supports `votedFrom` and `votedTo` within 365 days.

Voter totals and histories describe observed participation, not a person's identity or reputation. EVM `voterId` values are lowercase addresses; other providers can use other non-blank identities. `address` and timestamps can be null. If publication is unavailable, honor a 503 response and use official sources instead of treating it as zero activity.
