---
description: "Current DeGov public API reference for proposal search, exact resolution, details, and votes."
---

# Proposals

The [live OpenAPI specification](https://agent-api.degov.ai/openapi.json) is authoritative for methods, parameters, schemas, and payment metadata. Examples below are illustrative snapshots, not current governance claims. Replace opaque placeholders with IDs returned by the API. These are paid resources: unsigned curl examples return 402 unless called with an issued partner token or through an authorized x402 wallet. See [authentication](../authentication.md).

## `GET /v2/proposals`

Lists proposals using title search and exact structured filters.

| Name          | Type       | Meaning                                                      |
| ------------- | ---------- | ------------------------------------------------------------ |
| `query`       | string     | Case-insensitive substring of proposal title                 |
| `daoId`       | string     | Exact public DAO slug                                        |
| `provider`    | string     | Exact, case-sensitive provider returned by the API           |
| `proposerId`  | string     | Exact normalized proposer identity                           |
| `status`      | repeatable | `pending`, `active`, or `closed`; repeat for multiple values |
| `createdFrom` | date-time  | Inclusive proposal creation lower bound                      |
| `createdTo`   | date-time  | Exclusive proposal creation upper bound                      |
| `sort`        | enum       | `createdDesc` or `votingEndsAtAsc`                           |
| `limit`       | int        | 1-100, default 25                                            |
| `cursor`      | string     | Cursor from the preceding page                               |

Default sort: `createdDesc`.

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/proposals?query=cirBTC&daoId=aavedao-eth&status=active&status=pending&sort=votingEndsAtAsc&limit=10"
```

Example item:

```json
{
  "proposalId": "p1_<opaque>",
  "daoId": "aavedao-eth",
  "title": "[ARFC] Onboard cirBTC on Aave v3 Core and Aave V4 Core",
  "proposerId": "0x66a28531e6f390a8cd44ab0c57a0f1aeb7e673ff",
  "source": {
    "provider": "snapshot",
    "externalId": "0xe7ce...",
    "url": "https://snapshot.org/#/aavedao.eth/proposal/0xe7ce...",
    "discussionUrl": "https://governance.aave.com/t/arfc-onboard-cirbtc-on-aave-v3-core-and-aave-v4-core/25128/4"
  },
  "status": "active",
  "outcome": "unknown",
  "executionStatus": "unknown",
  "createdAt": "2026-09-01T09:58:40.000Z",
  "votingStartsAt": "2026-09-02T09:58:40.000Z",
  "votingEndsAt": "2026-09-05T09:58:40.000Z",
  "dataAsOf": "2026-09-03T09:42:18.000Z"
}
```

`proposerId`, `discussionUrl`, `status`, and the three governance timestamps can be `null`.
`outcome` is the voting or governance-decision result: `passed`, `failed`, `canceled`, `no_quorum`,
or `unknown`. `executionStatus` is separate and is `not_started`, `queued`, `executed`, `expired`,
`not_applicable`, or `unknown`. A passed proposal is not necessarily executed; treat `unknown` as
missing source evidence rather than guessing. An active proposal normally has `outcome: "unknown"`
and `executionStatus: "unknown"`. Search matches titles only, not proposal bodies.

## `POST /v2/proposals/resolve`

Resolves exactly one proposal from either its canonical URL or complete source identity. The JSON
body is a discriminated union; extra fields are rejected.

By URL:

```bash
curl -sS -X POST \
  -H "content-type: application/json" \
  --data '{"by":"url","url":"https://snapshot.org/#/uniswapgovernance.eth/proposal/0x5ae3426216321df66a67eb677874b725f80e51888ad2da72b382b21669c554ee"}' \
  "https://agent-api.degov.ai/v2/proposals/resolve"
```

By source identity:

```bash
curl -sS -X POST \
  -H "content-type: application/json" \
  --data '{"by":"source_id","daoId":"uniswapgovernance-eth","provider":"snapshot","externalId":"0x5ae3426216321df66a67eb677874b725f80e51888ad2da72b382b21669c554ee"}' \
  "https://agent-api.degov.ai/v2/proposals/resolve"
```

The response `data` is one proposal-list item. A title is not a supported resolver input.

## `GET /v2/proposals/{proposalId}`

Returns the proposal-list fields plus body, normalized choices, quorum, and source update time.

```bash
curl -sS "https://agent-api.degov.ai/v2/proposals/p1_<opaque>"
```

Additional fields:

```json
{
  "body": "## Summary\n\nThe proposal asks the DAO to...",
  "choices": [
    { "id": "1", "label": "For" },
    { "id": "2", "label": "Against" },
    { "id": "3", "label": "Abstain" }
  ],
  "quorumRequired": "40000000",
  "sourceUpdatedAt": "2026-07-26T20:15:24.000Z"
}
```

`body`, `choices`, `quorumRequired`, and `sourceUpdatedAt` can be `null`. Choice ids are provider
safe: Snapshot choices are normally one-based, while DeGov Square Governor choices use `0` Against,
`1` For, and `2` Abstain. The shared `executionStatus` field exposes normalized lifecycle evidence
when the provider supports it, but the contract does not expose executable calls, calldata,
execution transactions, or a timelock ETA. Use `source.url` for those details and whenever
`executionStatus` is `unknown`.

## `GET /v2/proposals/{proposalId}/vote-summary`

Returns totals for proposals whose ballot choices can be normalized.

```bash
curl -sS "https://agent-api.degov.ai/v2/proposals/p1_<opaque>/vote-summary"
```

Example `data`:

```json
{
  "proposalId": "p1_<opaque>",
  "choices": [
    {
      "id": "1",
      "label": "For",
      "voteCount": 117,
      "knownVotingPower": "5347713.994141648005204052"
    },
    { "id": "2", "label": "Against", "voteCount": 0, "knownVotingPower": "0" },
    {
      "id": "3",
      "label": "Abstain",
      "voteCount": 1,
      "knownVotingPower": "1813.5906598898705"
    }
  ],
  "totals": {
    "voteCount": 118,
    "knownVotingPower": "5349527.584801537875704052"
  },
  "quorum": {
    "requiredVotingPower": "40000000",
    "progressPercent": "13.373818962004",
    "reached": false
  },
  "dataAsOf": "2026-07-26T04:54:01.000Z"
}
```

Voting power is a decimal string and must not be converted to a binary floating-point number.
`voteCount` includes votes with unknown voting power; `knownVotingPower` excludes their missing
power, so a value of `"0"` does not prove that nobody voted. Compare voting power only within the
same proposal, because providers and ballot strategies define its units. A `quorum` value of `null`
means no usable provider requirement is available; nullable progress and reached fields mean
attainment could not be calculated safely. Governor quorum follows its `COUNTING_MODE` membership
instead of counting Against votes automatically. A `404 DATA_NOT_AVAILABLE` response means a
normalized summary is unavailable; it does not mean the proposal does not exist.

## `GET /v2/proposals/{proposalId}/votes`

Lists effective latest votes for one proposal, with at most one current vote per voter.

| Name     | Type   | Meaning                        |
| -------- | ------ | ------------------------------ |
| `sort`   | enum   | `powerDesc` or `timeDesc`      |
| `limit`  | int    | 1-100, default 25              |
| `cursor` | string | Cursor from the preceding page |

Default sort: `powerDesc`.

```bash
curl -sS \
  "https://agent-api.degov.ai/v2/proposals/p1_<opaque>/votes?sort=powerDesc&limit=5"
```

Example item:

```json
{
  "voter": {
    "voterId": "0x8d07d225a769b7af3a923481e1fdf49180e6a265",
    "address": "0x8d07d225a769b7af3a923481e1fdf49180e6a265"
  },
  "choiceId": "1",
  "choiceLabel": "For",
  "rawChoice": 1,
  "votingPower": "2301703.801449782",
  "votedAt": "2026-07-26T04:54:01.000Z",
  "transactionHash": null
}
```

`address`, `choiceId`, `choiceLabel`, `votingPower`, `votedAt`, and `transactionHash` can be `null`.
Use `choiceId`/`choiceLabel` when present. `rawChoice` preserves any provider JSON value, including
a complex ballot for which the API deliberately leaves the normalized choice fields null.
