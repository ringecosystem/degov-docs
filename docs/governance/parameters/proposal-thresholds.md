# Proposal Thresholds

!!! important "Balance is Critical"
    Setting proposal thresholds too high can disenfranchise smaller token holders, while too low can lead to spammy proposals. Monitor and adjust based on community feedback.

## Overview

Proposal thresholds define the minimum number of tokens a user must hold or have delegated to them in order to create a governance proposal. This parameter serves as a spam prevention mechanism and ensures that only stakeholders with meaningful investment in the DAO can initiate governance actions.

## How It Works

When a user attempts to create a proposal, the governance contract checks their voting power (tokens owned + tokens delegated to them) against the proposal threshold. If their voting power meets or exceeds the threshold, the proposal can be created.

## Key Considerations

### **Anti-Spam Protection**
- Higher thresholds prevent low-effort or malicious proposals
- Reduces governance noise and keeps focus on meaningful proposals

### **Accessibility vs Security**
- Lower thresholds make governance more accessible to smaller token holders
- Higher thresholds may exclude legitimate community members but provide better security

### **Token Distribution Impact**
- Consider your DAO's token distribution when setting thresholds
- Should be achievable for dedicated community members but not trivial

## Recommended Values

| DAO Size | Token Supply | Recommended Threshold | Rationale |
|----------|--------------|----------------------|-----------|
| **Small DAO** | < 1M tokens | 0.5% - 1% of supply | Encourages participation while preventing spam |
| **Medium DAO** | 1M - 100M tokens | 0.1% - 0.5% of supply | Balances accessibility with quality control |
| **Large DAO** | > 100M tokens | 0.01% - 0.1% of supply | Maintains accessibility for large token distributions |

### **Example Configurations**

```solidity
// For a DAO with 10M token supply
proposalThreshold = 10000 tokens  // 0.1% of supply

// For a DAO with 1M token supply  
proposalThreshold = 5000 tokens   // 0.5% of supply
```

## Best Practices

1. **Start Conservative**: Begin with a moderate threshold and adjust based on community feedback
2. **Monitor Usage**: Track proposal creation patterns and adjust if needed
3. **Community Input**: Involve the community in threshold discussions
4. **Regular Review**: Periodically review and adjust as the DAO matures
5. **Consider Delegation**: Remember that tokens can be delegated, affecting effective threshold accessibility

## Related Parameters

- **[Quorum](quorum.md)**: Minimum participation needed for proposal passage
- **[Voting Period](voting-period.md)**: Time available for voting on proposals
- **[Proposal Delay](proposal-delay.md)**: Delay before voting begins