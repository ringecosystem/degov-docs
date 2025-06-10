---
description: "Frequently asked questions about DeGov.AI covering general information, proposal processes, delegation, AI agents, and platform features. Essential guidance for users."
---

# Frequently Asked Questions (FAQs)

This document provides answers to frequently asked questions about DeGov.AI including general information, proposal processes, and delegation, etc. Here you will find essential details to help you navigate the platform effectively.

## General

#### What blockchains does DeGov.AI support?

Currently, DeGov.AI supports Darwinia Chain, which is an EVM-compatible blockchain in the Polkadot ecosystem. We plan to expand support to other EVM-compatible chains in the future, including Ethereum Mainnet, Arbitrum, Base, and Ethereum Sepolia. Stay tuned for updates.

#### How does DeGov.AI utilize AI capabilities?

Integrating AI into our product is a core focus starting from the first version. We aim to solve long-term challenges in the decentralized governance space, such as proposal quality, voting participation, and decision-making efficiency by leveraging AI agents.

Currently, the following AI-related features are in our roadmap:

- Integrated AI agents assist with proposal review, summarization, and voting analysis. One of the biggest challenges in the governance process is the complexity of proposals and the difficulty for community members to understand their implications. By reducing the cognitive load, we aim to increase participation and improve decision-making quality.
- AI agents can serve as special roles in the governance process, accepting delegation and voting on behalf of the community. AI agents can collect and analyze the community's opinions, preferences, and feedback, and then cast votes based on the aggregated data. This approach can avoid the preference of a few individuals dominating the decision-making process, ensuring that the community's collective voice is represented.
- Multiple AI agents can collaborate to analyze complex proposals and provide insights. This collaborative approach allows for a more comprehensive understanding of proposals, as different AI agents can bring their unique perspectives and expertise to the table.

Bringing AI into governance opens up exciting possibilities for the future of decentralized organizations. We are actively developing these features this year, see our [Roadmap](roadmap.md) for the latest updates.

#### Is there an off-chain platform for discussing proposals?

DeGov.AI focuses on on-chain governance and doesn't provide a built-in off-chain discussion area. However, we provide an off-chain discussion entry point in the dashboard page that can link to your existing community forum or chat platform. This flexible approach allows you to use your preferred tools for discussions while keeping governance actions on-chain.

#### What's the difference between DeGov.AI and Snapshot?

DeGov.AI and Snapshot serve different purposes in the governance ecosystem:

- DeGov.AI is built on OpenZeppelin Governor and provides on-chain governance with smart contract execution. It integrates AI agents directly into the governance workflow for enhanced decision-making and features automatic proposal execution.

- Snapshot is primarily an off-chain voting platform that uses cryptographic signatures for gasless voting. While cost-effective, it requires manual execution of approved proposals.

DeGov.AI combines the best of both worlds: on-chain security with AI-powered enhancements and user-friendly interfaces. Learn more about [on-chain vs off-chain governance](governance/intro/onchain-offchain.md).

#### How can my DAO get support from DeGov.AI?

Getting support for your DAO is straightforward:

1. Community Support: Join our [Telegram channel](https://t.me/DeGov_AI) for community-driven help
2. Documentation: Review our comprehensive docs for self-service setup
3. GitHub: Report issues or contribute to our [open-source codebase](https://github.com/ringecosystem/degov)
4. Direct Contact: Reach out via our social channels for partnership opportunities

We're committed to supporting DAOs of all sizes in their governance journey.

#### How can I create or vote on proposals?

Creating Proposals:

1. Connect your wallet to the DeGov.AI platform
2. Ensure you meet the [proposal threshold](governance/parameters/proposal-thresholds.md) requirements
3. Draft your proposal with clear title, description, and executable actions
4. Submit the proposal for community review

Voting on Proposals:

1. Navigate to active proposals in your DAO
2. Review the proposal details and AI-generated summaries
3. Cast your vote (For, Against, or Abstain)
4. Your voting power is automatically calculated based on your token holdings

Learn more about the complete [proposal lifecycle](governance/proposal/lifecycle.md) and [voting mechanisms](governance/proposal/voting.md). Try the process on our [demo platform](https://demo.degov.ai/) first!


#### I'm not a developer. Can I still use DeGov.AI?

Absolutely! DeGov.AI is designed for all community members:

- User-Friendly Interface: Intuitive web interface requires no coding knowledge
- Guided Workflows: Step-by-step processes for all governance actions
- AI Assistance: AI agents help explain complex proposals in simple terms
- Mobile-Friendly: Access governance features from any device
- Educational Resources: Comprehensive guides and tutorials available

No technical expertise required to participate in governance! Check out our [DAO introduction guide](governance/intro/daos.md) to get started.

#### I'm a developer. How can I set up a DAO?

If you're a developer, familiarity with smart contract development and deployment is essential. Here's how to get started: Check our [Integration Guide](integration/overview.md) and [deployment documentation](integration/deploy.md) for detailed technical documentation.

#### Will DeGov.AI support other governance models in the future?

Yes! We're actively developing these features based on community feedback. Learn about current [governance models](governance/intro/model.md) we support.

#### Is DeGov.AI secure?

Security is our top priority:

- Battle-tested Foundation: Built on OpenZeppelin Governor, used by large DAOs like Uniswap and Compound
- Open Source: All code is publicly auditable
- Regular Audits: Smart contracts undergo professional security audits
- Bug Bounty Program: Community-driven security testing
- Best Practices: Follows industry-standard security protocols

Your DAO's security is ensured through proven, transparent technology.

## Proposal

#### What is the proposal threshold?

The proposal threshold is the minimum amount of governance tokens required to create a proposal. This ensures that only committed community members can initiate governance actions, preventing spam and low-quality proposals. Learn more about [proposal thresholds](governance/parameters/proposal-thresholds.md).

#### What is the lifecycle of a proposal?

A proposal goes through several stages:

1. Pending: Proposal is submitted and awaits the delay period
2. Active: Community can vote during the voting period
3. Succeeded/Defeated: Based on vote results and quorum requirements
4. Queued: Successful proposals enter timelock (if configured)
5. Executed: Proposal actions are automatically executed on-chain

Each stage has specific timeframes defined by your DAO's governance parameters. See our detailed [proposal lifecycle guide](governance/proposal/lifecycle.md) for more information.

#### What are the best practices for creating a proposal?

Follow these guidelines for successful proposals:

Content Guidelines:
- Clear Title: Descriptive and concise summary
- Detailed Description: Explain the problem, solution, and expected outcomes
- Executable Actions: Specify exact smart contract calls and parameters
- Impact Analysis: Describe potential effects on the community

Process Best Practices:
- Community Discussion: Engage in preliminary discussions before formal submission
- Stakeholder Input: Gather feedback from key community members
- Technical Review: Ensure all smart contract interactions are correct
- Timeline Considerations: Account for voting and execution periods

AI Assistance: Use AI agents to help refine your proposal and identify potential issues. Learn more about [proposal creation](governance/proposal/overview.md) for details.

#### How can I vote on a proposal?

Voting is straightforward:

1. Access the Proposal: Navigate to the active proposals list
2. Review Details: Read the proposal description and AI summary
3. Check Voting Power: Confirm your available voting power
4. Cast Your Vote: Choose For, Against, or Abstain
5. Confirm Transaction: Sign the transaction with your wallet

Voting Options:
- For: Support the proposal
- Against: Oppose the proposal  
- Abstain: Counted toward quorum but neutral on outcome

Your vote is final and cannot be changed once submitted. Learn more about [voting mechanisms](governance/proposal/voting.md).

#### How can I check the status of a proposal?

DeGov.AI provides real-time updates on proposal status. See the [proposal lifecycle](governance/proposal/lifecycle.md) for details on each stage. Key status indicators include:

- Pending: Proposal is awaiting the delay period
- Active: Voting is currently open
- Succeeded: Proposal passed with sufficient votes
- Defeated: Proposal failed to meet quorum or majority
- Queued: Proposal is waiting for timelock execution
- Executed: Proposal actions have been successfully executed

#### Can I change my vote after submitting it?

No, votes are final and immutable once submitted to the blockchain. This ensures:

- Vote Integrity: Prevents manipulation and vote buying
- Transparency: All votes are permanently recorded
- Fair Process: Equal treatment for all participants

Before Voting:

- Review all proposal details carefully
- Consider AI-generated analysis and summaries
- Participate in community discussions
- Ensure you understand the implications

Take your time to make informed decisions.

#### What happens if a proposal doesn't reach quorum?

When a proposal fails to reach the required quorum:

- Status: Proposal is marked as "Defeated"
- No Execution: Proposal actions are not executed
- Resubmission: The proposal can be resubmitted with modifications
- Learning Opportunity: Analyze why quorum wasn't reached

Common Reasons for Low Turnout:

- Insufficient community engagement
- Poor proposal timing
- Lack of clear communication
- Technical complexity

Use AI insights to understand participation patterns and improve future proposals. Learn about [quorum requirements](governance/parameters/quorum.md) and how they affect proposal outcomes.

#### How long does the voting period last?

Voting periods are configurable per DAO but typically range from:

- Short Term: 3-7 days for routine decisions
- Standard: 1-2 weeks for major proposals
- Extended: 2-4 weeks for constitutional changes

Factors Affecting Duration:

- Proposal Importance: More critical decisions get longer periods
- Community Size: Larger communities may need more time
- Complexity: Technical proposals may require extended review

Check your DAO's specific voting period in the governance parameters. See our guide on [voting periods](governance/parameters/voting-period.md) for configuration details.


## Delegate

#### What is delegation?

Delegation allows token holders to assign their voting power to trusted community members who will vote on their behalf:

Key Concepts:

- Representative Democracy: Delegates act as representatives for token holders
- Expertise Leverage: Delegate to members with relevant knowledge and experience  
- Increased Participation: Ensures votes are cast even when you're unavailable
- Revocable: You can change or revoke delegation at any time

Self-Delegation: By default, you delegate to yourself and vote directly. Learn more about [delegation mechanisms](./governance/proposal/delegation.md).

#### What is voting power?

Voting power includes all the governance tokens you hold, plus any tokens delegated to you by others. It determines how much influence you have in governance decisions. 

Example: If you hold 100 tokens and have 50 tokens delegated to you, your voting power is 150. See our [voting guide](./governance/proposal/voting.md) for detailed information.

#### How are governance tokens and voting power related?

The relationship is direct but includes delegation mechanics:

Token Holdings:

- 1 Token = 1 Vote: Basic principle (when self-delegated)
- Transferable: Voting power moves with token transfers
- Non-Custodial: Delegation doesn't transfer token ownership

#### How can I delegate my voting power?

DeGov.AI provides a simple interface for delegation. Navigate to the delegation section in your DAO dashboard and click the "Delegate" button. 

For detailed steps, see our [delegation guide](./governance/proposal/delegation.md).

#### Can I split my voting power and delegate it to multiple delegates?

Currently, standard delegation assigns all voting power to a single delegate. 

#### Will delegation transfer my tokens to the delegate?

No, absolutely not! Delegation is completely separate from token ownership.

What Delegation Does:

- Assigns voting rights only
- Delegate votes with your power on proposals
- You retain full token ownership and control

What You Keep:

- Complete ownership of your tokens
- Ability to transfer, sell, or use tokens
- Right to revoke delegation at any time
- Access to all token utilities (staking, rewards, etc.)

Security: Your tokens never leave your wallet during delegation. Learn more about [delegation mechanics](./governance/proposal/delegation.md).

#### Does it support partial delegation?

Standard OpenZeppelin Governor delegation is all-or-nothing:

Current System:

- Delegate all voting power to one address
- Cannot split power between multiple delegates
- Self-delegation keeps all power with you

Workarounds:

- Multiple Wallets: Split tokens across wallets for different delegation strategies
- Dynamic Delegation: Change delegates based on proposal topics
- Direct Voting: Temporarily reclaim delegation for important votes

Future Development: Partial and liquid delegation features are being explored for future releases.

#### How do I find good delegates?

Choosing the right delegate is crucial for effective governance:

Research Criteria:

- Voting History: Consistent participation and thoughtful decisions
- Expertise: Knowledge relevant to DAO's focus areas
- Alignment: Values and vision that match your own
- Communication: Active in community discussions and transparent about decisions

Available Information:

- Delegate Profiles: Many platforms provide delegate information pages
- Voting Records: Public blockchain records of all votes
- Community Feedback: Discussion forums and social media presence

Red Flags: Avoid delegates with poor participation, misaligned values, or lack of transparency.

#### Can I vote directly if I have delegated my tokens?

Yes! You can always vote directly even if you have delegated your tokens. 

#### What happens to my delegation if I transfer my tokens?

Token transfers affect delegation differently:

When You Transfer Tokens:

- Delegation Stays: Your delegation preference remains with your wallet
- Voting Power Reduces: Delegate's power decreases by the amount transferred
- New Balance: Delegation applies to your remaining token balance

When You Receive Tokens:

- Auto-Delegation: New tokens follow your current delegation setting
- Increased Power: If tokens come from non-delegated source, your delegate's power increases

Important: Always check delegation status after significant token movements.

## Technical

#### What are the gas costs for governance actions?

Gas costs vary by action and network:

Typical Costs (Ethereum Mainnet):

- Voting: 50,000-100,000 gas
- Proposal Creation: 200,000-500,000 gas  
- Delegation: 50,000-80,000 gas
- Proposal Execution: Varies by proposal complexity

Cost Optimization:

- Layer 2 Networks: Significantly lower costs on Polygon, Arbitrum, etc.
- Batch Transactions: Combine multiple actions when possible
- Gas Timing: Monitor gas prices for optimal transaction timing

Free Features: Reading proposal data, checking voting power, and browsing are gasless.

#### Can I use DeGov.AI on mobile devices?

Currently, DeGov.AI is optimized for desktop use, but we are actively working on a mobile-friendly version.

#### What wallets are compatible with DeGov.AI?

Any EVM-compatible wallet can be used with DeGov.AI.

#### How does DeGov.AI handle privacy?

Privacy protection is built into our design:

On-Chain Transparency:

- Public Votes: All votes are publicly visible on the blockchain
- Pseudonymous: Linked to wallet addresses, not personal identities
- Immutable Record: Complete audit trail of all governance actions

Off-Chain Privacy:

- No Personal Data: No collection of personal information
- Optional Profiles: Delegate profiles are voluntary
- Off-Chain Discussions: Use your preferred platforms for discussions

AI Privacy: AI processing doesn't store personal voting patterns or preferences.

#### Can I integrate DeGov.AI with my existing DAO tools?

Integration depends on the specific tools and their compatibility with EVM standards. Please contact us to discuss integration options.