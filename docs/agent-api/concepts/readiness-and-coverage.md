---
description: "Distinguish public resource availability, nullable data, source observations, and temporary API unavailability."
---

# Data Availability

Use free DAO directory and detail responses to inspect `availableData`, such as `proposals`, `votes`, or `forumTopics`. These indicate available resource families, not that every record is complete or current.

## Source observations

`dataAsOf` on DAO, proposal, forum-topic, and vote-summary records is the latest source observation included in that published record. It is not a build timestamp or a promise that every provider and related resource is current. Verify deadlines, execution, and other time-sensitive claims through the returned official source URL.

## Missing and unavailable data

- An empty collection means no records matched in the current published view. It does not establish the absence of all historical source activity.
- DAO `participation` can be null when complete participation totals are unavailable. Nullable values are not zero.
- `404 DATA_NOT_AVAILABLE` for a vote summary means the ballot cannot currently be normalized. The proposal and individual vote rows may still be available.
- `503 TEMPORARILY_UNAVAILABLE` means the service cannot currently supply that public resource. Retry later or continue with official sources and disclose the limitation.
- Missing excerpts, source dates, normalized choices, and execution evidence remain null or unknown. Do not fill them with inference.

Public API records do not expose ingestion jobs, serving revisions, or pipeline readiness. Use the actual resource response and [error guidance](errors.md), rather than probing operational endpoints. If `availableData` and a successful resource response disagree, preserve that uncertainty in the answer.
