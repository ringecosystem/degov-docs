---
description: "Configure proposal delay parameters for your DAO - the time between proposal creation and voting start. Learn optimal settings for review periods and community preparation."
---

# Proposal Delay

!!! important "Clock Mode Considerations"
    Modern OpenZeppelin Governor implementations support both block-based and timestamp-based clocks. Timestamp-based clocks ([ERC-6372](https://eips.ethereum.org/EIPS/eip-6372)) provide more predictable timing across different networks and are generally recommended for new deployments.

## Overview

Proposal delay (also known as voting delay) is the time period between when a proposal is created and when voting can begin. This parameter provides a buffer period for the community to review proposals, discuss their implications, and prepare for informed voting.

## How It Works

When a proposal is submitted, it enters a "pending" state for the duration of the proposal delay. During this time:

- The proposal cannot be voted on
- Community members can review the proposal details
- Discussion and debate can occur
- Token holders can delegate their voting power if needed

After the delay period expires, the proposal moves to the "active" state and voting begins.

## Purpose and Benefits

### **Review and Analysis Time**
- Allows thorough examination of proposal implications
- Enables community research and due diligence
- Prevents rushed decisions on complex matters

### **Defense Against Attacks**
- Provides time to detect and respond to malicious proposals
- Allows coordination of defense against governance attacks
- Gives large token holders time to participate if needed

### **Community Preparation**
- Time for discussion and consensus building
- Opportunity for delegation and vote preparation
- Allows global community participation across time zones

## Time Units

Proposal delays are specified in the unit defined by the token's `clock()` function (following [ERC-6372](https://eips.ethereum.org/EIPS/eip-6372)):

- **Block-based clock** (default): Delays measured in block numbers
- **Timestamp-based clock**: Delays measured in seconds (Unix timestamp)

The clock mode is determined by the voting token implementation and affects all Governor timing parameters.

### **Block-based Clock** (Default)
```solidity
// Example: 1 day delay on different networks
// Ethereum (~12s blocks): ~7,200 blocks  
// Polygon (~2s blocks): ~43,200 blocks
// BSC (~3s blocks): ~28,800 blocks
votingDelay = 7200; // 1 day on Ethereum
```

### **Timestamp-based Clock**
```solidity
// Example: Direct time-based delays
votingDelay = 86400; // 1 day (86400 seconds)
votingDelay = 259200; // 3 days (259200 seconds)
```

## Recommended Values

| Clock Mode | Duration | Value | Use Case |
|------------|----------|-------|----------|
| **Timestamp** | 6 hours | 21,600 | Operational decisions |
| **Timestamp** | 1 day | 86,400 | Standard proposals |
| **Timestamp** | 3 days | 259,200 | Critical changes |
| **Timestamp** | 7 days | 604,800 | Constitutional modifications |
| **Block (Ethereum)** | 1 day | ~7,200 blocks | Standard delay |
| **Block (Ethereum)** | 3 days | ~21,600 blocks | Extended review |

### **Example Configurations**

```solidity
// Timestamp-based clock (recommended)
votingDelay = 86400;  // 1 day in seconds
votingDelay = 259200; // 3 days in seconds
votingDelay = 21600;  // 6 hours in seconds

// Block-based clock (legacy approach)
votingDelay = 7200;   // ~1 day on Ethereum
votingDelay = 21600;  // ~3 days on Ethereum
```

## Delay Strategies by Proposal Type

### **Routine Operations** (6-24 hours)
- Parameter adjustments
- Routine budget allocations
- Regular maintenance updates

### **Standard Governance** (1-2 days)
- New feature implementations
- Partnership agreements
- Medium-impact changes

### **Critical Changes** (3-7 days)
- Smart contract upgrades
- Treasury management changes
- Fundamental protocol modifications

## Best Practices

1. **Balance Speed and Security**: Longer delays provide more security but slow decision-making
2. **Consider Your Community**: Global communities may need longer delays for participation
3. **Match Proposal Importance**: More critical proposals should have longer delays
4. **Choose Appropriate Clock Mode**: Timestamp-based clocks provide more predictable timing
5. **Emergency Procedures**: Have mechanisms for time-critical decisions

## Common Patterns

### **Tiered Delays**
```solidity
// Timestamp-based delays (recommended)
routine_delay = 21600;   // 6 hours
standard_delay = 86400;  // 1 day  
critical_delay = 259200; // 3 days

// Block-based delays (for reference)
routine_delay = 1800;    // ~6 hours on Ethereum
standard_delay = 7200;   // ~1 day on Ethereum
critical_delay = 21600;  // ~3 days on Ethereum
```

### **Minimum Viable Delay**
- Shortest delay that still provides adequate review time
- Balances security with operational efficiency

## Related Parameters

- **[Voting Period](voting-period.md)**: Duration of the actual voting phase
- **[TimeLock Delay](timelock-delay.md)**: Additional delay before execution
- **[Proposal Thresholds](proposal-thresholds.md)**: Requirements to create proposals