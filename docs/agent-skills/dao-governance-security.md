---
description: "The dao-governance-security skill — evaluate whether a governance proposal is malicious, risky, or safe."
---

# DAO Governance Security

**When to use:** the user asks whether a specific governance proposal is malicious, unexpectedly risky, or safe enough to support from a security perspective.

**Goal:** give a concrete, evidence-based security assessment with explicit uncertainty — never a vague risk label.

Repository: [dao-governance-security](https://github.com/ringecosystem/degov-agent-skills/tree/main/skills/dao-governance-security)

## Assessment rubric

The skill evaluates proposals across:

- **Executable actions:** what the proposal actually does if executed.
- **Token/native asset movement:** transfers, approvals, mints/burns, and their magnitudes.
- **Contract calls:** targets, functions, and parameters.
- **Permissions:** role changes, ownership transfers, upgrades.
- **Proposer reputation and process anomalies:** identity, history, and procedural red flags.
- **Execution risk:** failure modes and blast radius.
- **Uncertainty:** what is unknown and how it affects the verdict.

## Output

A structured analysis with:

- A clear verdict orientation (malicious / risky / safe enough) with confidence framing.
- Itemized findings tied to evidence and sources.
- Explicit uncertainty: what could not be verified and why.
- Plain-language recommendations for the user.

## Relationship to the Agent API

The skill uses the DeGov [Agent API](../agent-api/index.md) — proposal detail, votes, and [evidence](../agent-api/guides/build-cited-research.md) — as primary evidence, with official chain explorers and governance portals as verification sources. Data limitations from API readiness/coverage are surfaced rather than hidden.

Repository examples are synthetic (benign and risky) and are validated by a deterministic checker, so reviewers can inspect expected behavior without touching a live API.
