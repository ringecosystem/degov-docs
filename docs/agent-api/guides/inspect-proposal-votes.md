---
description: "Interpret normalized vote totals and quorum, then inspect effective votes using current sort and pagination fields."
---

# Inspect Proposal Votes

Obtain a `proposalId` from proposal discovery or exact resolution, then start with the normalized summary:

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  "https://agent-api.degov.ai/v2/proposals/$PROPOSAL_ID/vote-summary"
```

Read `data.choices`, `data.totals`, `data.quorum`, and `data.dataAsOf`. Get `outcome` and `executionStatus` from proposal detail. These are separate from vote totals.

For concentration or timing analysis, fetch effective vote rows:

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  "https://agent-api.degov.ai/v2/proposals/$PROPOSAL_ID/votes?sort=powerDesc&limit=100"
```

Rows are in `data`; continue through top-level `page` only as needed. `sort=timeDesc` orders by vote time. Each voter has at most one effective latest vote per proposal, rather than a history of every ballot change.

- Preserve decimal-string voting power. Counts are integers; votes with missing power still contribute to the vote count.
- Prefer `choiceId` and `choiceLabel`. If null, preserve `rawChoice` without inventing ballot meaning.
- A null quorum or progress is unknown, not failure. Governor quorum follows the source counting rules.
- `404 DATA_NOT_AVAILABLE` can mean the ballot cannot be normalized even when individual vote rows exist. Continue with those rows or the official source and state the limitation.
