---
description: "Vote delegation in DeGov.AI - how to activate your voting power, delegate to trusted representatives, or vote yourself. Essential first step for governance participation."
---

# Vote Delegation

!!! important "Important First Step"
    In DeGov.AI, you must delegate your voting power before you can participate in governance - even if you want to vote for yourself! This is a one-time setup that activates your tokens for voting.

Vote delegation lets you share your voting power with people you trust, or activate it for yourself. Think of it like giving someone your proxy vote in a shareholder meeting - they can vote on your behalf, but you still own your shares.

## What is Vote Delegation?

Delegation is a way to make sure your voice gets heard in governance, even if you can't vote on every single proposal yourself.

### The Basics
- **You keep your tokens**: Delegation doesn't transfer ownership, just voting power
- **It's reversible**: You can change your mind and pick someone else anytime
- **It's required**: Even to vote for yourself, you need to "delegate to yourself" first
- **It's flexible**: You can switch between voting yourself and having others vote for you

### Key People in Delegation
- **You (Delegator)**: The person who owns tokens and chooses where the voting power goes
- **Representative (Delegate)**: The person who receives voting power and casts votes
- **Self-Delegation**: When you delegate to yourself to vote directly

## How Delegation Works

### The Simple Version
1. **You have tokens** that give you voting power
2. **You choose who gets to use that power** (could be yourself or someone else)
3. **They vote using your power** on governance proposals
4. **You can change your choice** anytime you want

### What Doesn't Change
- You still own your tokens
- You can still sell or transfer your tokens
- Your tokens still have the same value
- You can still use them for other purposes

### What Does Change
- Someone else (or you) can now vote using the power from your tokens
- This only affects governance voting, nothing else

## Types of Delegation

### Option 1: Vote for Yourself (Self-Delegation)

**Best for people who**:

- Want to vote on proposals themselves
- Have time to research and stay informed
- Prefer to keep full control

**How it works**:

- You delegate your voting power to your own wallet address
- You can then vote directly on any proposal
- It's like registering to vote - you have to do it once to participate

### Option 2: Choose a Representative

**Best for people who**:

- Don't have time to research every proposal
- Want to support someone with relevant expertise
- Trust someone else's judgment on governance matters

**How it works**:

- You delegate your voting power to someone else's address
- They can vote using your power (combined with their own and others who delegated to them)
- You can watch their voting decisions and change delegates if you disagree

## Choosing Your Approach

### Questions to Ask Yourself

**Do you have time to stay informed?**

- Yes → Consider self-delegation
- No → Look for a good representative

**Do you understand the technical details?**

- Yes → Self-delegation might work well
- No → Find someone with relevant expertise

**Do you trust someone else's judgment?**

- Yes → Representative delegation could be perfect
- No → Self-delegation gives you full control

**How important is this to you?**

- Very important → Stay directly involved with self-delegation
- Somewhat important → Either approach works
- Not very important → Representative delegation saves time

## Finding Good Representatives

If you choose to delegate to someone else, look for people who:

### Have a Good Track Record
- Vote regularly on proposals
- Explain their reasoning clearly
- Have been consistent over time
- Don't miss important votes

### Share Your Values
- Have similar views on how the platform should develop
- Care about the same issues you do
- Have demonstrated good judgment in the past

### Are Transparent
- Explain how they make decisions
- Share their voting reasoning publicly
- Respond to questions from people who delegate to them
- Admit when they make mistakes

### Stay Active
- Participate in community discussions
- Keep up with platform developments
- Engage with governance regularly
- Don't disappear for long periods

!!! tip "Finding Representatives"
    Look for active community members in forums, social media, and governance discussions. Many platforms maintain lists of people who are willing to serve as delegates.

## How to Set Up Delegation

On the DeGov.AI platform, setting up delegation is straightforward:

- Connect your wallet in your DAO governance interface
- Go to the profile page and follow the instructions to delegate

## Managing Your Delegation

### Staying Informed
Even if you delegate to someone else, it's good to:

- Occasionally check how they voted
- Read their explanations for important decisions
- Make sure they're still active and engaged
- Verify they still share your values

### When to Change Delegates
Consider switching if your representative:

- Stops participating regularly
- Makes decisions you strongly disagree with
- Becomes inactive in the community
- Changes their approach in ways you don't like

### How to Change

On DeGov.AI, you can change your delegate at any time:

- Connect your wallet in the DAO governance interface
- Go to the delegations page and select a new delegate
- Confirm the change in your wallet

## Common Concerns and Questions

### "What if my delegate votes against my interests?"
- You can change delegates anytime
- Most delegates explain their reasoning publicly
- You can always switch back to self-delegation
- Your tokens remain yours regardless

### "What if my delegate becomes inactive?"
- Watch for warning signs like missed votes or no communication
- The community usually notices and discusses inactive delegates
- You can easily switch to someone more active
- Self-delegation is always an option

### "Can my delegate steal my tokens?"
- No! Delegation only affects voting power, not token ownership
- Your tokens stay in your wallet
- You can sell, transfer, or use them normally
- Delegation can be revoked instantly

### "What if I disagree with a specific vote?"
- Consider whether it's a pattern or a one-time disagreement
- Look at their explanation to understand their reasoning
- You might learn something new, or you might decide to switch delegates
- Remember that no delegate will agree with you 100% of the time

## Being a Good Delegate

If others delegate to you, remember:

### Your Responsibilities
- Vote regularly and thoughtfully
- Explain your reasoning clearly
- Listen to feedback from your delegators
- Stay informed about governance issues
- Act in the community's best interest

### Best Practices
- **Communicate regularly** about your governance activity
- **Be transparent** about your decision-making process
- **Admit mistakes** when you make them
- **Stay accessible** for questions and feedback
- **Put the community first**, not just your own interests

## Learn More

Want to explore other aspects of governance?

- [Proposal Overview](overview.md) - Understanding what proposals are
- [Proposal Lifecycle](lifecycle.md) - How proposals move through different stages
- [Voting Guide](voting.md) - Everything about casting votes
- [Governance Parameters](../parameters/overview.md) - The rules that govern the system

---

## Technical Implementation Details

For developers and technically-minded users working with [OpenZeppelin Contracts 5.x](https://docs.openzeppelin.com/contracts/5.x/governance):

### Core Architecture
Delegation is implemented through the `ERC20Votes` extension, which integrates with the `IVotes` interface:

```solidity
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Permit} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import {ERC20Votes} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import {IERC6372} from "@openzeppelin/contracts/interfaces/IERC6372.sol";
```

### Core Delegation Functions
```solidity
// Delegate voting power to an address
function delegate(address delegatee) public virtual

// Delegate voting power using signature (EIP-712)
function delegateBySig(
    address delegatee,
    uint256 nonce,
    uint256 expiry,
    uint8 v,
    bytes32 r,
    bytes32 s
) public virtual

// Get current delegate for an address  
function delegates(address account) public view virtual returns (address)

// Get current voting power of an address
function getVotes(address account) public view virtual returns (uint256)

// Get historical voting power at specific timepoint
function getPastVotes(address account, uint256 timepoint) public view virtual returns (uint256)

// Get total supply at specific timepoint
function getPastTotalSupply(uint256 timepoint) public view virtual returns (uint256)
```

### ERC-6372 Clock Integration
OpenZeppelin 5.x uses the [ERC-6372 standard for time-based operations](https://eips.ethereum.org/EIPS/eip-6372):

```solidity
// Get current timepoint (timestamp or block number)
function clock() public view virtual returns (uint48)

// Get clock mode description
function CLOCK_MODE() public view virtual returns (string memory)

// For timestamp-based governance:
function clock() public view override returns (uint48) {
    return uint48(block.timestamp);
}

function CLOCK_MODE() public pure override returns (string memory) {
    return "mode=timestamp";
}
```

### Voting Power Calculation
```solidity
// Internal function that calculates voting power
function _getVotingUnits(address account) internal view virtual returns (uint256) {
    return balanceOf(account);
}

// How delegation affects voting power distribution
function _delegate(address delegator, address delegatee) internal virtual {
    address currentDelegate = delegates(delegator);
    _delegates[delegator] = delegatee;

    emit DelegateChanged(delegator, currentDelegate, delegatee);
    _moveDelegateVotes(currentDelegate, delegatee, _getVotingUnits(delegator));
}
```

### Checkpoint System
OpenZeppelin 5.x uses an efficient checkpoint system for historical data:

```solidity
// Internal checkpoint structure for vote tracking
struct Checkpoint {
    uint48 _key;    // Timepoint (timestamp or block number)
    uint208 _value; // Vote count at that timepoint
}

// Get checkpoints for an account
function checkpoints(address account, uint32 pos) public view virtual returns (Checkpoint memory)

// Get number of checkpoints for an account
function numCheckpoints(address account) public view virtual returns (uint32)
```

### Key Events
```solidity
event DelegateChanged(
    address indexed delegator, 
    address indexed fromDelegate, 
    address indexed toDelegate
);

event DelegateVotesChanged(
    address indexed delegate, 
    uint256 previousVotes, 
    uint256 newVotes
);
```

### Integration with Governor
The Governor contract reads voting power through the `IVotes` interface:

```solidity
import {GovernorVotes} from "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";

contract MyGovernor is Governor, GovernorVotes {
    constructor(IVotes _token) GovernorVotes(_token) {}
    
    // Governor automatically uses delegated voting power
    function _getVotes(
        address account,
        uint256 timepoint,
        bytes memory /*params*/
    ) internal view virtual override returns (uint256) {
        return token.getPastVotes(account, timepoint);
    }
}
```

### Self-Delegation Pattern
```solidity
// Users must delegate to themselves to activate voting power
function enableVoting() public {
    _delegate(msg.sender, msg.sender);
}

// Check if an address has activated voting
function hasActivatedVoting(address account) public view returns (bool) {
    return delegates(account) != address(0);
}
```

### Security Features

**Nonce-Based Signature Protection**:
```solidity
// Prevents signature replay attacks
function nonces(address owner) public view virtual returns (uint256)
```

**Atomic State Changes**:
- All delegation changes happen in a single transaction
- Vote power transfers are atomic and cannot be partially applied

**Historical Integrity**:
- Past voting power cannot be retroactively modified
- Checkpoints ensure accurate historical lookups

**Access Control**:
- Only token holders can delegate their own tokens
- Signature-based delegation requires valid EIP-712 signatures

### Gas Optimization Features

**Efficient Checkpointing**:
- Only creates new checkpoints when voting power actually changes
- Binary search for historical lookups

**Minimal Storage Updates**:
- Batches multiple operations to reduce gas costs
- Optimized storage layout for frequently accessed data

**ERC-6372 Efficiency**:
- Supports both timestamp and block number modes
- Governor automatically adapts to token's clock mode