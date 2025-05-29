---
description: "Configure quorum requirements for DAO proposals - the minimum participation needed for valid governance decisions. Learn optimal settings to balance security and functionality."
---

# Quorum

!!! important "Balance is Critical"
    Setting quorum too high can make governance non-functional, while too low can enable minority attacks. Monitor and adjust based on actual participation patterns.


## Overview

Quorum represents the minimum threshold of voting power that must participate in a governance proposal for the vote to be considered valid. This parameter ensures that decisions have sufficient community participation and aren't made by a small minority of token holders.

## How It Works

During the voting period, the governance contract tracks the total voting power that has cast votes (both FOR and AGAINST). For a proposal to pass, the total participation must meet or exceed the quorum threshold, **and** the majority of votes must be in favor.

## Types of Quorum

### **Absolute Quorum**
- Fixed percentage of total token supply
- Most common implementation in OpenZeppelin Governor
- Example: 10% of all tokens must participate

### **Relative Quorum** 
- Percentage of circulating/active tokens
- More dynamic but complex to implement
- Example: 15% of tokens held by active addresses

## Key Considerations

### **Security vs Efficiency**
- **Higher Quorum**: More secure decisions, harder to manipulate
- **Lower Quorum**: Faster decision-making, risk of minority control

### **Token Distribution**
- Consider how tokens are distributed across holders
- Account for inactive or lost tokens in calculations

### **Voter Apathy**
- Many token holders don't actively participate in governance
- Quorum should be achievable with engaged community members

## Recommended Values

| DAO Maturity | Community Engagement | Recommended Quorum | Rationale |
|--------------|---------------------|-------------------|-----------|
| **New DAO** | Unknown | 3% - 5% | Allow governance to function while building engagement |
| **Growing DAO** | Moderate | 5% - 10% | Standard range for most DAOs |
| **Mature DAO** | High | 10% - 20% | Higher security for established communities |
| **High-Stakes DAO** | Variable | 15% - 25% | Maximum security for critical decisions |

### **Example Configurations**

```solidity
// Conservative approach for new DAO
quorum = 4% of total supply

// Standard for established DAO
quorum = 10% of total supply

// High security for treasury decisions
quorum = 15% of total supply
```

## Best Practices

1. **Start Low**: Begin with achievable quorum levels to ensure governance functions
2. **Monitor Participation**: Track voting participation over time
3. **Gradual Increases**: Raise quorum as community engagement grows
4. **Failure Analysis**: If proposals consistently fail due to quorum, consider adjustments
5. **Emergency Procedures**: Have backup mechanisms for critical time-sensitive decisions

## Common Challenges

### **Quorum Not Met**
- Proposals fail despite community support
- Consider voter education and engagement strategies
- May need to lower quorum temporarily

### **Whale Manipulation**
- Large holders can artificially inflate participation
- Consider vote delegation to distribute power
- Implement voting power caps if necessary

## Related Parameters

- **[Proposal Thresholds](proposal-thresholds.md)**: Minimum tokens needed to create proposals
- **[Voting Period](voting-period.md)**: Time available to reach quorum
- **[TimeLock Delay](timelock-delay.md)**: Execution delay after successful votes
