---
description: "Install current DeGov governance research and security skills, verify readiness, and use evidence-based API research."
---

# Agent Skills

DeGov publishes reusable skills for DAO governance research and proposal-security analysis. They combine structured API evidence with official source verification and explicit uncertainty.

## Install or update

Give this request to your agent:

```text
Install or update the DeGov agent skills from https://github.com/ringecosystem/degov-agent-skills. Verify that DAO Governance Research and DAO Governance Security are available, then use the current OpenAPI at https://agent-api.degov.ai/openapi.json to make one free DAO discovery request without payment. Tell me when both skills are ready.
```

For command-line installation:

```bash
npx skills add ringecosystem/degov-agent-skills
```

After updating, verify that your agent loads the new files rather than a cached copy. The current [research skill](https://github.com/ringecosystem/degov-agent-skills/blob/main/skills/dao-governance-research/SKILL.md) declares version **1.0.1**; the [security skill](https://github.com/ringecosystem/degov-agent-skills/blob/main/skills/dao-governance-security/SKILL.md) declares **0.2.0**. These are skill versions, separate from the Agent API software release. The installed skills remain the source of truth for their behavior.

## When to use each skill

| Skill | Best-fit tasks |
| --- | --- |
| [DAO Governance Research](dao-governance-research.md) | Find DAOs and proposals, inspect outcomes and votes, research participants and voters, and read governance forum context |
| [DAO Governance Security](dao-governance-security.md) | Compare proposal text with executable actions, analyze funds and permissions, and identify process or execution risks |

Research uses the current public API for covered facts. It uses official sources directly for conceptual questions and whenever API coverage, freshness, or depth is insufficient. Full executable payloads and transaction evidence come from official governance sources and explorers.

## Payment capability

Free DAO discovery and detail need no wallet or API key. When a paid request returns 402, the research skill loads [MetaMask Agent Wallet](https://github.com/MetaMask/agent-wallet) and delegates offer inspection, authorization, spending controls, signing, settlement verification, and safe retries. Payment metadata comes from OpenAPI and the actual `PAYMENT-REQUIRED` challenge.

The governance skills do not implement a wallet or override its policy. When the wallet is unavailable or payment is not authorized, research can continue with official public sources and disclose that paid structured data was not used.

## Verify readiness

Confirm both skills are discoverable, inspect [OpenAPI](https://agent-api.degov.ai/openapi.json), and make a free `GET /v2/daos?limit=1` request. Expect a `data` array and top-level `page`. This verifies discovery and free access; payment capability is a separate wallet setup step. See the [API quickstart](../agent-api/quickstart.md).
