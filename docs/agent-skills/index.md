---
description: "Install DeGov Agent Skills for DAO governance research and proposal security with MetaMask Agent Wallet payments."
---

# Agent Skills

DeGov publishes reusable skills that help agents research DAO governance and assess proposal security with evidence, primary-source verification, and explicit uncertainty.

## Install

```bash
npx skills add ringecosystem/degov-agent-skills
```

Repository: [ringecosystem/degov-agent-skills](https://github.com/ringecosystem/degov-agent-skills)

## Available skills

- [DAO Governance Research](dao-governance-research.md) answers questions about DAO activity, proposals, votes, voters, forums, events, and signals.
- [DAO Governance Security](dao-governance-security.md) assesses executable actions, funds flow, permissions, proposer and process anomalies, execution risk, and uncertainty.

## MetaMask Agent Wallet

The research skill is designed to use [MetaMask Agent Wallet](https://github.com/MetaMask/agent-wallet) by default for paid Agent API resources. When the API returns `402 Payment Required`, the skill loads `metamask-agent-wallet` and delegates offer inspection, user authorization, spending controls, signing, settlement verification, and retry safety to it.

The wallet implementation is not duplicated inside the governance skill. If MetaMask Agent Wallet is unavailable or payment is not authorized, the agent can continue with official public sources and disclose that paid structured data was not used.

## How they work together

```text
User question
  -> governance skill selects the smallest useful evidence set
  -> DeGov Agent API supplies covered structured data
  -> MetaMask Agent Wallet handles an x402 challenge when required
  -> official sources verify primary facts and fill coverage gaps
  -> agent produces a direct, source-aware answer
```
