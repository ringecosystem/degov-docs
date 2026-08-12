---
description: "DAO Governance Security skill — evidence-first assessment of executable proposal risk and uncertainty."
---

# DAO Governance Security

Use this skill when the user asks whether a governance proposal is safe, malicious, unexpectedly permissive, or worth supporting from a security perspective.

Repository: [dao-governance-security](https://github.com/ringecosystem/degov-agent-skills/tree/main/skills/dao-governance-security)

## What it evaluates

- Executable actions and whether they match the proposal text.
- Token and native-asset movement, recipients, approvals, and amounts.
- Contract calls, upgrades, ownership, roles, and privileged permissions.
- Proposer identity, history, governance-process anomalies, and timing.
- Execution, simulation, cross-chain, ordering, and rollback risk.
- Missing evidence and how uncertainty changes the recommendation.

## Evidence sources

The skill prefers official governance interfaces, forums, DAO documentation, verified block explorers, contract ABIs, transaction simulations, treasury records, and prior proposals. It can compose with the research skill when structured proposal detail, votes, provenance, or source references would help.

API routing, pricing, payment, and transport details remain inside the research capability. This keeps the security rubric stable when an endpoint or tier changes.

When paid structured data is needed, the research skill uses MetaMask Agent Wallet for the x402 flow; the security skill itself remains focused on analysis rather than payment handling.

## Output

The result includes an overall risk level, confidence, recommendation, bottom line, executable-action table, evidence-backed findings, uncertainties, and concrete user actions. Missing or undecoded executable payloads prevent a confident low-risk conclusion.
