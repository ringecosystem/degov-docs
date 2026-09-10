---
description: "Interpret governance timestamps, proposal lifecycle and execution, decimal voting power, and nullable values."
---

# Timestamps & Numbers

## Timestamps

Public timestamps are RFC 3339 date-time strings, or null where the provider has no reliable value.

| Field | Meaning |
| --- | --- |
| `createdAt` | Source proposal or forum-topic creation |
| `votingStartsAt`, `votingEndsAt` | Proposal voting window |
| `sourceUpdatedAt` | Provider-reported proposal update |
| `lastPostedAt` | Forum activity time |
| `votedAt` | Source vote time |
| `dataAsOf` | Latest source observation included in this published record |

Do not substitute voting deadlines or source-observation times for proposal creation. Preserve the time zone when explaining a deadline. `From` filters include their lower bound; `To` filters exclude their upper bound.

## Proposal state

`status` describes the voting lifecycle: `pending`, `active`, `closed`, or null. `outcome` describes the decision: `passed`, `failed`, `canceled`, `no_quorum`, or `unknown`. `executionStatus` independently describes execution: `not_started`, `queued`, `executed`, `expired`, `not_applicable`, or `unknown`.

A passed proposal is not necessarily executed. An active proposal normally has an unknown outcome. Verify unknown execution through `source.url` instead of inferring a transaction from the voting result.

## Numbers

Counts such as `voteCount` and `votedProposalCount` are JSON integers. `votingPower`, `knownVotingPower`, quorum requirements, and quorum progress are decimal strings; use decimal arithmetic rather than binary floating point. Null means unavailable, not zero.

Vote summaries include votes with missing power in the vote count while excluding their unknown power from the known-power total. Ballot rules define the units, so do not compare raw power across unrelated DAOs or strategies. Governor quorum follows the provider's counting rules and does not automatically include Against votes.
