---
description: "Use current DeGov research skill behavior for structured governance evidence, source verification, and explicit uncertainty."
---

# DAO Governance Research

Use this skill when a question depends on recent DAO proposals, outcomes, votes, forum activity, or voter behavior. The [current skill](https://github.com/ringecosystem/degov-agent-skills/blob/main/skills/dao-governance-research/SKILL.md) declares version **1.0.1**.

## Research flow

1. Identify the DAO, time range, and requested type of evidence.
2. Search the free DAO directory and inspect `availableData` when useful.
3. Select the smallest useful set of current public resources from [OpenAPI](https://agent-api.degov.ai/openapi.json).
4. Read lists from `data`, follow top-level `page` only as needed, and preserve opaque IDs and cursors.
5. Explain voting `outcome` separately from `executionStatus`. Use official sources for executable actions, uncertain execution, or time-sensitive claims.
6. Disclose missing, stale, or conflicting evidence and answer in useful prose.

The resolver uses a POST JSON body with an exact URL or complete source identity. Titles use proposal search. The API supplies governance resources rather than operational health, evidence bundles, or timeline endpoints.

## Evidence rules

- Treat `dataAsOf` as source-observation provenance, not a global readiness or freshness guarantee.
- Treat `availableData` as resource availability and nullable participation totals as unknown, not zero.
- Preserve decimal-string voting power. Prefer normalized choice labels, retaining `rawChoice` when normalization is unavailable.
- Follow `source.url` for primary text, execution calls, calldata, timelocks, and transaction evidence.
- Use official web sources directly for conceptual questions or when API evidence is insufficient.
- Apply [the security skill](dao-governance-security.md) when the user asks whether a proposal is safe or risky.

## Payments and recovery

On a 402 response, the research skill delegates to `metamask-agent-wallet`. The wallet owns payment authorization, spending controls, signing, settlement verification, and safe retries. Current prices come from each paid operation's OpenAPI metadata and the actual challenge.

If that capability is unavailable or payment is not authorized, continue with official sources where possible and explain the evidence limitation. See the maintained [API reference](https://github.com/ringecosystem/degov-agent-skills/blob/main/skills/dao-governance-research/references/api.md) and [troubleshooting guide](https://github.com/ringecosystem/degov-agent-skills/blob/main/skills/dao-governance-research/references/troubleshooting.md).
