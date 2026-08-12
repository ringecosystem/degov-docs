---
description: "Concise answers to common questions about DeGov Square, Atlas, Agent API, Agent Skills, voting, delegation, and integrations."
---

# Frequently Asked Questions

## DeGov.AI

### What does DeGov.AI provide?

DeGov.AI includes four connected products:

- [DeGov Square](governance/overview.md) for operating and participating in onchain governance.
- [DeGov Atlas](atlas/index.md) for browsing governance activity across DAOs.
- [Agent API](agent-api/index.md) for structured governance data and integrations.
- [Agent Skills](agent-skills/index.md) for governance research and proposal-security analysis.

### Which networks and DAOs are supported?

Square supports EVM-compatible governance deployments. Browse [DeGov Square](https://square.degov.ai) for available communities. Atlas and the Agent API cover the DAOs currently indexed by DeGov; use Atlas or `GET /v2/daos` for the current directory.

### How is Square different from Snapshot?

Square focuses on executable onchain governance built around OpenZeppelin Governor. Snapshot primarily provides offchain, signature-based voting; approved decisions usually need a separate execution process. See [Onchain and Offchain Governance](governance/intro/onchain-offchain.md).

### How can my DAO use DeGov Square?

Contact the DeGov team through [Telegram](https://t.me/RingDAO_Hub), or follow the [Square integration guide](integration/overview.md) to deploy and register an instance.

## Proposals & Voting

### How do I create a proposal?

Connect your wallet, make sure you meet the DAO's [proposal threshold](governance/parameters/proposal-thresholds.md), enter the proposal description and executable actions, review them carefully, and submit the transaction. See [Proposal Overview](governance/proposal/overview.md).

### How do I vote?

Open an active proposal, review its description and actions, choose the available voting option, and confirm the transaction in your wallet. Voting rules and whether a vote can be changed depend on the DAO's Governor contract. See [Voting](governance/proposal/voting.md).

### What happens if quorum is not reached?

The proposal does not succeed and its actions cannot proceed through the normal execution path. The exact status and resubmission rules depend on the DAO's contracts. See [Quorum](governance/parameters/quorum.md).

### How long does voting last?

Each DAO configures its own voting period. Check the DAO's governance parameters or the proposal deadline. See [Voting Period](governance/parameters/voting-period.md).

## Delegation

### What is delegation?

Delegation assigns your voting power to another address without transferring ownership of your tokens. You can normally change or revoke it later. See [Vote Delegation](governance/proposal/delegation.md).

### What is voting power?

Voting power is the amount counted for governance at the contract's selected snapshot or checkpoint. It can reflect your eligible balance and voting power delegated to you.

### Can I split delegation between several delegates?

Standard OpenZeppelin Governor delegation normally assigns an account's voting power to one delegate. A DAO can implement different rules, so verify its token and Governor contracts.

### What happens when I transfer tokens?

Token transfers change the voting power associated with the relevant account or delegate according to the token's checkpoint rules. The delegation preference may remain, but the delegated amount changes with the eligible balance.

## Agents, API & Integrations

### How do Agent Skills pay for API requests?

Paid Agent API resources use x402 on Base. DeGov Agent Skills use MetaMask Agent Wallet by default to inspect the offer, request authorization, sign, settle, and retry safely.

### How do I get a partner key?

Partner keys are issued by DeGov. [Contact the team](https://t.me/RingDAO_Hub) with your integration and expected usage. Keep issued keys out of source control and logs.

### Can I integrate DeGov with existing DAO tools?

Yes. Use the [Agent API](agent-api/index.md) for structured data integrations. For a Square deployment or governance-contract integration, start with the [Integration Overview](integration/overview.md) or contact the DeGov team.

### Which wallets work with Square?

Square supports EVM-compatible wallets through its available connection methods. Wallet and network availability can vary by deployment.

### Is governance activity private?

Onchain proposals, votes, addresses, and execution records are public. DeGov documentation and interfaces should not be treated as a privacy layer over public governance data.
