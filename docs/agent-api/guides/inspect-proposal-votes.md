---
description: "Inspect proposal vote totals, quorum, choice distribution, and individual ballots."
---

# Inspect Proposal Votes

**Tier:** plus.

Start with the summary. It answers most questions without paging every ballot:

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_opaque/votes/summary"
```

Use `data.totals`, `data.quorum`, `data.choices`, and `data.coverageStatus`. Do not assume `data.proposal.outcome` is present; obtain lifecycle outcome from proposal detail when needed.

Fetch individual rows only for concentration, whale, timing, or audit analysis:

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_opaque/votes?order=power&limit=100"
```

Rows are in `data.items`. Voting power and aggregate counts are exact decimal strings. Follow `meta.page.nextCursor` only while more rows materially improve the analysis.
