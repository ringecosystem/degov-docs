# Frequently Asked Questions (FAQs)

This document provides answers to frequently asked questions about DeGov.AI including general information, proposal processes, and delegation, etc. Here you will find essential details to help you navigate the platform effectively.

## General

#### What's the difference between DeGov.AI and Snapshot?

DeGov.AI and Snapshot serve different purposes in the governance ecosystem:

- DeGov.AI is built on OpenZeppelin Governor and provides on-chain governance with smart contract execution. It integrates AI agents directly into the governance workflow for enhanced decision-making and features automatic proposal execution.

- Snapshot is primarily an off-chain voting platform that uses cryptographic signatures for gasless voting. While cost-effective, it requires manual execution of approved proposals.

DeGov.AI combines the best of both worlds: on-chain security with AI-powered enhancements and user-friendly interfaces. Learn more about [on-chain vs off-chain governance](/governance/intro/onchain-offchain/).

#### How can my DAO get support from DeGov.AI?

Getting support for your DAO is straightforward:

1. Community Support: Join our [Telegram channel](https://t.me/DeGov_AI) for community-driven help
2. Documentation: Review our comprehensive docs for self-service setup
3. GitHub: Report issues or contribute to our [open-source codebase](https://github.com/ringecosystem/degov)
4. Direct Contact: Reach out via our social channels for partnership opportunities

We're committed to supporting DAOs of all sizes in their governance journey.

#### How is AI integrated into DeGov.AI?

AI agents are seamlessly integrated throughout the governance process:

- Proposal Analysis: AI automatically summarizes complex proposals and identifies key points
- Real-time Insights: AI agents provide contextual information and data analysis during discussions
- MCP Integration: AI connects with external data sources through [Model Context Protocol](https://modelcontextprotocol.io/) for enriched decision-making
- Sentiment Analysis: AI helps gauge community sentiment on proposals
- Smart Recommendations: AI suggests optimal voting parameters and governance settings

The AI operates transparently, with all interactions visible to the community.

#### How can I create or vote on proposals?

Creating Proposals:
1. Connect your wallet to the DeGov.AI platform
2. Ensure you meet the proposal threshold requirements
3. Draft your proposal with clear title, description, and executable actions
4. Submit the proposal for community review

Voting on Proposals:
1. Navigate to active proposals in your DAO
2. Review the proposal details and AI-generated summaries
3. Cast your vote (For, Against, or Abstain)
4. Your voting power is automatically calculated based on your token holdings

Learn more about the complete [proposal lifecycle](/governance/proposal/lifecycle/) and [voting mechanisms](/governance/proposal/voting/). Try the process on our [demo platform](https://demo.degov.ai/) first!

#### Is there an off-chain platform for discussing proposals?

Yes! DeGov.AI provides multiple discussion channels:

- Integrated Comments: Each proposal includes a discussion thread
- Community Forums: DAO-specific discussion spaces
- AI-Moderated Discussions: AI agents help facilitate productive conversations
- External Integration: Connect with Discord, Telegram, or other community platforms

Discussions are designed to be inclusive and productive, with AI assistance to keep conversations on-topic.

#### I'm not a developer. Can I still use DeGov.AI?

Absolutely! DeGov.AI is designed for all community members:

- User-Friendly Interface: Intuitive web interface requires no coding knowledge
- Guided Workflows: Step-by-step processes for all governance actions
- AI Assistance: AI agents help explain complex proposals in simple terms
- Mobile-Friendly: Access governance features from any device
- Educational Resources: Comprehensive guides and tutorials available

No technical expertise required to participate in governance! Check out our [DAO introduction guide](/governance/intro/daos/) to get started.

#### I'm a developer. How can I set up a DAO?

Setting up a DAO on DeGov.AI involves several steps:

1. Smart Contract Deployment: Deploy governance contracts using our templates
2. Token Configuration: Set up your governance token with proper parameters
3. Governance Parameters: Configure voting periods, quorum, proposal thresholds
4. AI Agent Setup: Configure AI agents for your specific use case
5. Frontend Integration: Customize the governance interface for your community

Check our [Integration Guide](/integration/overview/) and [deployment documentation](/integration/deploy/) for detailed technical documentation.

#### Will DeGov.AI support other governance models in the future?

Yes! Our roadmap includes:

- Quadratic Voting: Enhanced voting mechanisms for fairer representation
- Delegation Networks: Advanced delegation trees and liquid democracy
- Multi-DAO Governance: Cross-DAO collaboration and coordination
- Custom AI Agents: Specialized AI agents for different governance needs
- Layer 2 Integration: Support for various blockchain networks

We're actively developing these features based on community feedback. Learn about current [governance models](/governance/intro/model/) we support.

#### What blockchains does DeGov.AI support?

Currently, DeGov.AI supports:

- Ethereum Mainnet: Full feature support
- Layer 2 Solutions: Polygon, Arbitrum, Optimism
- Testnets: Sepolia, Mumbai for development and testing

We're expanding to additional EVM-compatible chains based on community demand.

#### Is DeGov.AI secure?

Security is our top priority:

- Battle-tested Foundation: Built on OpenZeppelin Governor, used by major DAOs
- Open Source: All code is publicly auditable
- Regular Audits: Smart contracts undergo professional security audits
- Bug Bounty Program: Community-driven security testing
- Best Practices: Follows industry-standard security protocols

Your DAO's security is ensured through proven, transparent technology.

## Proposal

#### What is the proposal threshold?

The proposal threshold is the minimum amount of governance tokens required to create a proposal. This prevents spam and ensures proposers have stake in the DAO:

- Default Threshold: Typically 0.5-1% of total token supply
- Configurable: Each DAO can set their own threshold based on community size
- Token-based: Calculated based on your current token holdings
- Delegation Counts: Delegated tokens count toward your threshold

Check your DAO's specific threshold in the governance parameters section. Learn more about [proposal thresholds](/governance/parameters/proposal-thresholds/).

#### What is the lifecycle of a proposal?

A proposal goes through several stages:

1. Pending: Proposal is submitted and awaits the delay period
2. Active: Community can vote during the voting period
3. Succeeded/Defeated: Based on vote results and quorum requirements
4. Queued: Successful proposals enter timelock (if configured)
5. Executed: Proposal actions are automatically executed on-chain
6. Expired: Proposals not executed within the grace period expire

Each stage has specific timeframes defined by your DAO's governance parameters. See our detailed [proposal lifecycle guide](/governance/proposal/lifecycle/) for more information.

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

AI Assistance: Use AI agents to help refine your proposal and identify potential issues. Check out our [best practices guide](/best-practices/) for comprehensive recommendations.

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

Your vote is final and cannot be changed once submitted. Learn more about [voting mechanisms](/governance/proposal/voting/).

#### How can I check the status of a proposal?

Monitor proposal progress through multiple channels:

On-Platform:
- Proposal Dashboard: Real-time status updates and vote counts
- Activity Feed: Notifications for proposal state changes
- Vote Breakdown: Detailed voting statistics and trends

External Tools:
- Blockchain Explorers: Direct smart contract interaction history
- API Access: Programmatic access to proposal data
- Mobile Notifications: Push notifications for important updates

AI Insights: AI agents provide contextual updates and analysis of proposal progress. Follow the complete [proposal lifecycle](/governance/proposal/lifecycle/) to understand each stage.

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

Use AI insights to understand participation patterns and improve future proposals. Learn about [quorum requirements](/governance/parameters/quorum/) and how they affect proposal outcomes.

#### How long does the voting period last?

Voting periods are configurable per DAO but typically range from:

- Short Term: 3-7 days for routine decisions
- Standard: 1-2 weeks for major proposals
- Extended: 2-4 weeks for constitutional changes

Factors Affecting Duration:
- Proposal Importance: More critical decisions get longer periods
- Community Size: Larger communities may need more time
- Complexity: Technical proposals may require extended review

Check your DAO's specific voting period in the governance parameters. See our guide on [voting periods](/governance/parameters/voting-period/) for configuration details.


## Delegate

#### What is delegation?

Delegation allows token holders to assign their voting power to trusted community members who will vote on their behalf:

Key Concepts:
- Representative Democracy: Delegates act as representatives for token holders
- Expertise Leverage: Delegate to members with relevant knowledge and experience  
- Increased Participation: Ensures votes are cast even when you're unavailable
- Revocable: You can change or revoke delegation at any time

Self-Delegation: By default, you delegate to yourself and vote directly. Learn more about [delegation mechanisms](/governance/proposal/delegation/).

#### What is voting power?

Voting power determines the weight of your vote in governance decisions:

Calculation:
- Base Power: Derived from your governance token holdings
- Delegation: Includes tokens delegated to you by others
- Snapshot: Measured at the block when proposal voting begins
- Dynamic: Changes as token holdings and delegations change

Example: If you hold 100 tokens and have 50 tokens delegated to you, your voting power is 150. See our [voting guide](/governance/proposal/voting/) for detailed information.

#### How are governance tokens and voting power related?

The relationship is direct but includes delegation mechanics:

Token Holdings:
- 1 Token = 1 Vote: Basic principle (when self-delegated)
- Transferable: Voting power moves with token transfers
- Non-Custodial: Delegation doesn't transfer token ownership

Important Notes:
- Tokens in liquidity pools or exchanges typically cannot vote
- Some DAOs may have different token-to-vote ratios
- Historical holdings may affect voting power in some systems

#### How can I delegate my voting power?

Delegating is a simple process:

1. Choose a Delegate: Research potential delegates and their track record
2. Access Delegation Interface: Navigate to the delegation section
3. Enter Delegate Address: Input the wallet address of your chosen delegate
4. Confirm Transaction: Sign the delegation transaction
5. Verify: Confirm the delegation is active

Delegate Research:
- Review voting history and alignment with your values
- Check their participation rate and engagement level
- Consider their expertise in relevant areas

For detailed steps, see our [delegation guide](/governance/proposal/delegation/).

#### Can I split my voting power and delegate it to multiple delegates?

Currently, standard delegation assigns all voting power to a single delegate. However:

Alternatives:
- Periodic Re-delegation: Change delegates between proposals
- Selective Participation: Reclaim delegation for specific votes
- Future Features: Advanced delegation models are in development

Liquid Democracy: Future versions may support proportional delegation to multiple representatives.

#### Will delegation transfer my tokens to the delegate?

No, absolutely not! Delegation is completely separate from token ownership:

What Delegation Does:
- Assigns voting rights only
- Delegate votes with your power on proposals
- You retain full token ownership and control

What You Keep:
- Complete ownership of your tokens
- Ability to transfer, sell, or use tokens
- Right to revoke delegation at any time
- Access to all token utilities (staking, rewards, etc.)

Security: Your tokens never leave your wallet during delegation. Learn more about [delegation mechanics](/governance/proposal/delegation/).

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
- AI Analysis: Some platforms offer AI-generated delegate performance insights

Red Flags: Avoid delegates with poor participation, misaligned values, or lack of transparency.

#### Can I vote directly if I have delegated my tokens?

Yes! You have several options:

Override Options:
1. Revoke Delegation: Remove delegation and vote directly (affects all future proposals)
2. Direct Voting: On some platforms, you can vote directly while maintaining delegation
3. Temporary Reclaim: Some systems allow temporary delegation suspension

Process Varies: Check your specific DAO's delegation rules and interface options.

Best Practice: Communicate with your delegate about major decisions where you want to vote directly. See our [delegation guide](/governance/proposal/delegation/) for more details.

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

Yes! DeGov.AI is fully mobile-optimized:

Mobile Features:
- Responsive Design: Adapts to all screen sizes
- Touch-Friendly: Optimized for mobile interaction
- Wallet Integration: Works with mobile wallet apps
- Offline Reading: Cache proposals for offline review
- Push Notifications: Get alerts for important governance events

Supported Wallets: MetaMask Mobile, WalletConnect, Coinbase Wallet, and others.

#### What wallets are compatible with DeGov.AI?

DeGov.AI supports all major Ethereum wallets:

Browser Wallets:
- MetaMask
- Coinbase Wallet  
- Rainbow Wallet
- Brave Wallet

Hardware Wallets:
- Ledger (via MetaMask or WalletConnect)
- Trezor (via MetaMask or WalletConnect)

Mobile Wallets:
- MetaMask Mobile
- Trust Wallet
- WalletConnect-compatible wallets

Enterprise Solutions: Multi-sig wallets like Gnosis Safe are fully supported.

#### How does DeGov.AI handle privacy?

Privacy protection is built into our design:

On-Chain Transparency:
- Public Votes: All votes are publicly visible on the blockchain
- Pseudonymous: Linked to wallet addresses, not personal identities
- Immutable Record: Complete audit trail of all governance actions

Off-Chain Privacy:
- No Personal Data: No collection of personal information
- Optional Profiles: Delegate profiles are voluntary
- Encrypted Communications: Secure discussion channels
- GDPR Compliant: European data protection standards

AI Privacy: AI processing doesn't store personal voting patterns or preferences.

#### Can I integrate DeGov.AI with my existing DAO tools?

Yes! DeGov.AI offers extensive integration options:

API Access:
- RESTful API: Access all governance data programmatically
- GraphQL: Flexible data querying for complex applications
- Webhooks: Real-time notifications for proposal events
- SDK: JavaScript/TypeScript SDK for easy integration

Platform Integrations:
- Discord Bots: Governance notifications and commands
- Telegram Integration: Proposal updates and voting reminders
- Snapshot Compatibility: Migration tools and parallel operation
- Treasury Tools: Integration with multi-sig and treasury management

Custom Development: Our team can help with custom integrations for enterprise DAOs. Check our [integration overview](/integration/overview/) for technical details.
