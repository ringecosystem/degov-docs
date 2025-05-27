# Proposal Overview

Think of governance proposals as the community's way of making important decisions together. Just like how a neighborhood association might vote on new community rules or how to spend shared funds, DeGov.AI uses proposals to let everyone have a say in how the platform evolves.

## What is a Governance Proposal?

A governance proposal is simply a suggestion that the community votes on. Anyone who holds enough governance tokens can suggest changes, and then everyone gets to vote whether they agree or disagree. It's democracy in action, but for a digital community!

## Types of Proposals

DeGov.AI community members can suggest different kinds of changes:

### Changing How Things Work
- Adjusting voting rules (like how long voting lasts or how many people need to participate)
- Updating platform settings and limits
- Fine-tuning how the system operates

### Improving the Platform
- Adding new features that make DeGov.AI better
- Fixing bugs or security issues
- Upgrading the technology behind the scenes

### Managing Community Funds
- Deciding how to spend money from the community treasury
- Funding new projects or initiatives
- Supporting developers and contributors

### Community Decisions
- Approving partnerships with other organizations
- Supporting community-led projects
- Creating new groups or committees

## What Goes Into a Proposal?

Every proposal needs to include several pieces of information:

### Clear Description
A good proposal explains:
- What exactly is being suggested
- Why this change would be helpful
- How it might affect the community
- When it would be implemented

### Action Plan
The specific steps that will happen if the proposal passes. This might include:
- Which parts of the system will be changed
- What new features will be added
- How funds will be spent

!!! tip "Writing Good Proposals"
    The best proposals are easy to understand and explain clearly what will happen. Remember, the community needs to understand what they're voting for!

## Who Can Create Proposals?

Not everyone can create proposals - this helps prevent spam and ensures serious suggestions. To create a proposal, you need:

### Enough Tokens
You must own a certain number of governance tokens. This shows you have a stake in the community's success.

### Clean Record
You can't have another proposal already being voted on. This keeps things organized and manageable.

### Active Participation
Your tokens need to be "activated" for voting (this is called delegation - more on this in other guides).

## How Proposals Get Unique Names

Each proposal gets a special fingerprint (called an ID) that's created from its contents. This ensures:
- No two identical proposals can exist
- Proposals can't be changed after creation
- Everyone can verify what they're voting on

## Safety Features

DeGov.AI has built-in safety features to protect the community:

### Waiting Periods
Even after a proposal passes, there's a waiting period before changes take effect. This gives everyone time to:
- Review what was approved
- Prepare for changes
- Catch any potential problems

### Community Watch
During the waiting period, the community can:
- Double-check that everything looks correct
- Raise concerns if something seems wrong
- Make sure the changes are what everyone expected

!!! info "Why the Wait?"
    Think of this like a "cooling off" period. It ensures that important changes don't happen too quickly and gives everyone a chance to speak up if needed.

## Saving Money on Fees

DeGov.AI is designed to be cost-effective:

### Bundling Changes
Multiple related changes can be grouped together in one proposal, saving on transaction fees.

### Smart Processing
The system is optimized to use less energy and cost less money when executing approved proposals.

## The Journey of a Proposal

Proposals go through several stages:

1. **Waiting to Start**: Newly created proposals have a brief waiting period before voting begins
2. **Active Voting**: Community members cast their votes
3. **Counting Results**: The system checks if enough people voted and if the proposal passed
4. **Approved**: Successful proposals enter a safety waiting period
5. **Ready to Execute**: After the waiting period, approved changes can be implemented
6. **Complete**: The proposal has been fully implemented

For more details about these stages, see our [Proposal Lifecycle](lifecycle.md) guide.

## How to Get Involved

Ready to participate in governance? Here's how to start:

### Step 1: Get Governance Tokens
You'll need to own some governance tokens to participate in voting.

### Step 2: Activate Your Voting Power
This involves a simple process called "delegation" - even if you're voting for yourself.

### Step 3: Stay Informed
- Follow community discussions
- Read proposal descriptions carefully
- Ask questions if something isn't clear

### Step 4: Vote Thoughtfully
- Take time to understand each proposal
- Consider how changes might affect the community
- Vote on proposals that interest you

### Step 5: Track Progress
- Watch how proposals develop
- See which ones get implemented
- Learn from the process

## Learn More

Want to dive deeper? Check out these related guides:

- [Proposal Lifecycle](lifecycle.md) - How proposals move through different stages
- [Voting Guide](voting.md) - Everything about casting your vote
- [Vote Delegation](delegation.md) - How to delegate your voting power
- [Governance Parameters](../parameters/overview.md) - The rules that govern the system

---

## Technical Details

For developers and technically-minded users, here are the implementation specifics:

### Smart Contract Framework
DeGov.AI proposals are implemented using the OpenZeppelin Governor framework, providing:
- Battle-tested security
- Standard governance patterns
- Interoperability with other protocols

### Proposal Structure
Each proposal consists of:
- `targets[]`: Array of contract addresses to call
- `values[]`: Array of ETH amounts to send (usually zero)
- `calldatas[]`: Array of encoded function calls
- `description`: Human-readable proposal text

### Unique Identification
Proposals receive deterministic IDs calculated as:
```solidity
proposalId = keccak256(abi.encode(targets, values, calldatas, descriptionHash))
```

### Timelock Integration
Approved proposals are queued in a TimelockController contract:
- Enforces execution delays for security
- Allows proposal cancellation in emergencies
- Provides predictable execution timing

### Gas Optimization
- Batch multiple operations in single proposals
- Optimized calldata encoding
- Efficient state transitions