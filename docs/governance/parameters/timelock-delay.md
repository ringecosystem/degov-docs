# TimeLock Delay

!!! important "Balance is Critical"
    TimeLock delay is the final security layer in governance, providing a necessary waiting period after a proposal has been approved. Setting it too short can expose the DAO to risks, while too long can hinder responsiveness to urgent issues.

## Overview

TimeLock delay is an additional waiting period after a proposal has been successfully voted on and before it can be executed. This parameter provides a final security layer, giving the community time to react to approved proposals and potentially intervene if necessary.

## How It Works

The TimeLock mechanism works in stages:

1. **Proposal Passes**: Voting period ends with successful outcome (quorum met + majority approval)
2. **Queue Period**: Proposal is queued in the TimeLock contract, moves to "Pending" state
3. **Delay Period**: Mandatory waiting period before execution is allowed
4. **Ready State**: Once delay expires, proposal becomes "Ready" and can be executed
5. **Execution or Cancellation**: Proposal is either executed (moves to "Done") or cancelled (returns to "Unset")

## Security Benefits

### **Final Safeguard**
- Offers a crucial window to identify and thwart harmful proposals.
- Allows time for urgent governance actions.
- Guards against hasty or improperly influenced decisions.

### **Empowering Community Intervention**
- Facilitates emergency actions by multisig groups.
- Enables the community to organize and propose alternatives.
- Provides an opportunity for significant token holders to coordinate.

### **Ensuring Openness and Foresight**
- Makes upcoming changes publicly visible to all.
- Gives ecosystem members early notification.
- Allows integrators and users time to prepare and coordinate.

## Recommended Values

| Risk Level | Delay Period | Use Cases | Rationale |
|------------|--------------|-----------|-----------|
| **Low Risk** | 24-48 hours | Parameter tweaks, routine operations | Minimal delay for low-impact changes |
| **Medium Risk** | 2-7 days | Feature updates, moderate treasury actions | Standard security without excessive delays |
| **High Risk** | 7-14 days | Protocol upgrades, major treasury moves | Maximum security for critical changes |
| **Critical** | 14-30 days | Core contract changes, constitutional updates | Extended protection for fundamental changes |

### **Example Configurations**

```solidity
// Standard TimeLock delays
routine_timelock = 2 days
standard_timelock = 7 days  
critical_timelock = 14 days

// In blocks (Ethereum ~12s blocks)
routine_timelock = 14400 blocks    // 2 days
standard_timelock = 50400 blocks   // 7 days
critical_timelock = 100800 blocks  // 14 days
```

## Emergency Mechanisms

### **Emergency Pause**
- Ability to pause TimeLock execution in emergencies
- Usually controlled by security council or multisig
- Should have clear criteria and oversight

### **Expedited Execution**
- Bypass or reduce TimeLock for critical security fixes
- Requires high threshold (e.g., supermajority + multisig)
- Should be rare and well-documented

### **Community Veto**
- Mechanism for community to cancel queued proposals
- Could be through emergency governance or token holder petition
- Provides democratic override of TimeLock

## Best Practices

1. **Risk-Based Delays**: Match delay length to proposal risk and impact
2. **Clear Categories**: Define proposal types and their associated delays
3. **Emergency Procedures**: Have well-defined emergency override mechanisms
4. **Communication**: Clearly communicate upcoming executions to community
5. **Monitoring**: Track queued proposals and execution patterns

## Common Patterns

### **Graduated Delays**
```solidity
if (treasuryAmount > 10M) {
    timelock = 14 days;
} else if (treasuryAmount > 1M) {
    timelock = 7 days;
} else {
    timelock = 2 days;
}
```

### **Proposal Impact Assessment**
- Automated scoring of proposal risk
- Delay assignment based on impact score
- Community input on risk categorization

## Execution After Delay

After the TimeLock delay period expires, proposals become "Ready" for execution. **Important**: OpenZeppelin's TimelockController does not implement an execution window or automatic expiration. Once a proposal becomes "Ready", it remains executable indefinitely until either:

- **Executed**: Successfully carried out, moving to "Done" state
- **Cancelled**: Manually cancelled by authorized parties, returning to "Unset" state

This design provides maximum flexibility but requires active management of queued proposals. Communities should establish governance practices for:

- Regular review of queued proposals
- Clear cancellation procedures for outdated proposals
- Monitoring and alerting for long-pending executions

## Related Parameters

- **[Voting Period](voting-period.md)**: Duration of voting before TimeLock
- **[Proposal Delay](proposal-delay.md)**: Initial delay before voting
- **[Quorum](quorum.md)**: Participation needed for proposal to reach TimeLock

## Monitoring and Analytics

Track key metrics for TimeLock effectiveness:

- **Execution Rate**: Percentage of queued proposals actually executed
- **Cancellation Rate**: How often proposals are cancelled during delay
- **Community Response**: Engagement during TimeLock periods
- **Emergency Usage**: Frequency of override mechanisms