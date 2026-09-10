---
description: "Current DeGov public API reference for participants & voters."
---

# Participants & Voters

The [live OpenAPI specification](https://agent-api.degov.ai/openapi.json) is authoritative for methods, parameters, schemas, and payment metadata. Examples below are illustrative snapshots, not current governance claims. Replace opaque placeholders with IDs returned by the API. These are paid resources: unsigned curl examples return 402 unless called with an issued partner token or through an authorized x402 wallet. See [authentication](../authentication.md).

## `GET /v2/daos/{daoId}/participants`

Ranks voters who have an effective latest vote in the DAO.

| Name     | Type   | Meaning                                                 |
| -------- | ------ | ------------------------------------------------------- |
| `sort`   | enum   | `votedProposalCountDesc` or `latestEffectiveVoteAtDesc` |
| `limit`  | int    | 1-100, default 25                                       |
| `cursor` | string | Cursor from the preceding page                          |

Default sort: `votedProposalCountDesc`.

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/daos/uniswapgovernance-eth/participants?sort=votedProposalCountDesc&limit=5"
```

Example item:

```json
{
  "voterId": "0x06c4865ab16c9c760622f19a313a2e637e2e66a2",
  "address": "0x06c4865ab16c9c760622f19a313a2e637e2e66a2",
  "votedProposalCount": 152,
  "earliestEffectiveVoteAt": "2021-05-27T13:01:20.000Z",
  "latestEffectiveVoteAt": "2025-08-26T01:25:19.000Z"
}
```

`address` and either timestamp can be `null`.

## `GET /v2/voters/{voterId}`

Returns one voter's participation totals across public active DAOs.

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/voters/0x06c4865ab16c9c760622f19a313a2e637e2e66a2"
```

Example `data`:

```json
{
  "voterId": "0x06c4865ab16c9c760622f19a313a2e637e2e66a2",
  "address": "0x06c4865ab16c9c760622f19a313a2e637e2e66a2",
  "daoCount": 41,
  "votedProposalCount": 2223,
  "earliestEffectiveVoteAt": "2021-05-05T14:41:56.000Z",
  "latestEffectiveVoteAt": "2025-08-26T01:25:19.000Z"
}
```

`address` and either timestamp can be `null`.

## `GET /v2/voters/{voterId}/votes`

Lists the voter's effective latest votes, newest first.

| Name        | Type      | Meaning                         |
| ----------- | --------- | ------------------------------- |
| `daoId`     | string    | Optional exact DAO slug         |
| `votedFrom` | date-time | Inclusive vote-time lower bound |
| `votedTo`   | date-time | Exclusive vote-time upper bound |
| `limit`     | int       | 1-100, default 25               |
| `cursor`    | string    | Cursor from the preceding page  |

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/voters/0x06c4865ab16c9c760622f19a313a2e637e2e66a2/votes?daoId=uniswapgovernance-eth&limit=5"
```

Example item:

```json
{
  "proposalId": "p1_<opaque>",
  "daoId": "uniswapgovernance-eth",
  "proposalTitle": "Establish Uniswap Governance as DUNI, a Wyoming DUNA",
  "proposalUrl": "https://snapshot.org/#/uniswapgovernance.eth/proposal/0xf9f9...",
  "choiceId": "1",
  "choiceLabel": "For",
  "rawChoice": 1,
  "votingPower": "1",
  "votedAt": "2025-08-26T01:25:19.000Z",
  "transactionHash": null
}
```

`choiceId`, `choiceLabel`, `votingPower`, `votedAt`, and `transactionHash` can be `null`. Interpret
`rawChoice` with the same caution as proposal vote rows when the normalized choice is unavailable.
