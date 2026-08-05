---
description: "DeGov Agent Skills — reusable agent knowledge for DAO governance research and proposal security analysis."
---

# Agent Skills

DeGov publishes reusable agent skills that turn the [Agent API](../agent-api/index.md) into reliable, evidence-based answers about DAO governance.

Repository: [ringecosystem/degov-agent-skills](https://github.com/ringecosystem/degov-agent-skills)

## Available skills

### DAO Governance Research

Answers questions like:

- "What has ENS been doing lately?"
- "What are the biggest DAO governance stories this week?"
- "Can you explain this ENS proposal?"

The skill uses the DeGov Agent API as the **primary evidence source** for supported DAO data — free discovery endpoints first, paid endpoints only after the user explicitly chooses the paid path — then uses web search as a secondary layer when API data is missing, stale, too shallow, or needs source verification.

Paid calls settle in USDC on Base through x402. The skill bundles a CLI with a dedicated local wallet, live budget guidance, and clickable settlement receipts.

See [DAO Governance Research](dao-governance-research.md).

### DAO Governance Security

Evaluates whether a governance proposal is malicious, unexpectedly risky, or safe enough to support — covering executable actions, token movement, contract calls, permissions, proposer reputation, process anomalies, execution risk, and explicit uncertainty.

See [DAO Governance Security](dao-governance-security.md).

## How skills and the Agent API fit together

```text
User question
  -> skill selects the right Agent API workflow (guides in the Agent API docs)
  -> free endpoints when enough, paid endpoints after explicit consent
  -> web sources only as a follow-up layer for verification
  -> plain-language, source-aware answer
```

Agents should treat API data as evidence, not as final prose, and explain context and uncertainty clearly.
