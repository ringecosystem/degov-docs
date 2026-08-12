---
description: "Interpret coverage, freshness, and data availability in DeGov Atlas."
---

# Governance Data

Atlas indexes governance from supported proposal, vote, and forum sources. Availability differs by DAO and source.

- `hasVoteData` indicates whether Atlas has a supported vote surface for the DAO.
- `hasForumData` indicates whether supported forum discussions are indexed.
- Coverage can be ready, partial, backfilling, stale, or unavailable depending on the surface.
- Freshness describes how recently source data was materialized; it is separate from completeness.

Atlas serves published read models so an in-progress rebuild does not expose a half-updated page. Still, backfilling or partial coverage can mean that some proposals, votes, discussions, or fields are not yet present. Follow linked official sources when completeness affects a decision.
