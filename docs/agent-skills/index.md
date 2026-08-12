---
description: "Install and use DeGov Agent Skills for evidence-based DAO governance research and proposal security analysis."
---

# Agent Skills

DeGov publishes reusable skills that help agents research DAO governance and assess proposal security with explicit evidence and uncertainty.

## Install

```bash
npx skills add ringecosystem/degov-agent-skills
```

Repository: [ringecosystem/degov-agent-skills](https://github.com/ringecosystem/degov-agent-skills)

## Available skills

- [DAO Governance Research](dao-governance-research.md) uses the DeGov Agent API for covered structured data and official sources for verification, context, and coverage gaps.
- [DAO Governance Security](dao-governance-security.md) evaluates executable actions, funds flow, permissions, proposer and process anomalies, execution risk, and uncertainty.

## How the capabilities compose

```text
User question
  -> research skill selects the smallest useful evidence set
  -> DeGov Agent API supplies covered structured data
  -> official sources verify intent and primary facts
  -> wallet capability handles authorization and settlement after a 402
  -> agent produces a direct, source-aware answer
```

The governance skills do not bundle a wallet, duplicate wallet authorization policy, or require a custom paid-call confirmation script. If payment is unavailable or not authorized, research can continue with official public sources while disclosing that structured paid API data was not used.
