---
description: "Set optimal voting periods for DAO governance - how long community members have to vote on proposals. Balance timely decisions with broad participation."
---

# Voting Period

!!! important "Voting Period Overview"
    The voting period is a critical parameter in DAO governance, determining how long community members have to cast their votes on proposals. It balances the need for timely decision-making with the desire for broad participation.

## Overview

The voting period defines how long community members have to cast their votes on a governance proposal. This parameter directly impacts participation rates, decision-making speed, and the inclusivity of your DAO's governance process.

## How It Works

Once a proposal becomes active (after the proposal delay), the voting period begins. During this time:

- Token holders can vote FOR, AGAINST, or ABSTAIN
- Votes can be cast directly or through delegates
- Voting power is based on token balance at proposal creation (snapshot)
- The period ends at a specific block number, regardless of participation

## Key Considerations

### **Participation vs Speed**
- **Longer periods**: Higher participation, slower decisions
- **Shorter periods**: Faster execution, risk of excluding participants

### **Global Community**
- Consider time zones and accessibility
- Weekend vs weekday voting patterns
- International community coordination needs

### **Proposal Complexity**
- Simple proposals may need less time
- Complex technical proposals benefit from longer discussion periods

## Recommended Values

| Proposal Type | Duration | Blocks (Ethereum) | Rationale |
|---------------|----------|-------------------|-----------|
| **Routine Operations** | 3-5 days | 21,600-36,000 | Quick decisions for regular business |
| **Standard Proposals** | 5-7 days | 36,000-50,400 | Balanced participation and efficiency |
| **Major Changes** | 7-14 days | 50,400-100,800 | Maximum participation for important decisions |
| **Constitutional Changes** | 10-21 days | 72,000-151,200 | Extended time for fundamental changes |

### **Network-Specific Examples**

```solidity
// Ethereum (12s blocks)
standard_voting_period = 40320 blocks  // 7 days
extended_voting_period = 80640 blocks  // 14 days

// Polygon (2s blocks)  
standard_voting_period = 302400 blocks // 7 days
quick_voting_period = 129600 blocks    // 3 days

// BSC (3s blocks)
standard_voting_period = 201600 blocks // 7 days
routine_voting_period = 86400 blocks   // 3 days
```

## Voting Period Strategies

### **Fixed Duration**
- Same period for all proposals
- Simple and predictable
- Most common implementation

### **Variable Duration by Type**
- Different periods for different proposal categories
- More flexible but complex to implement
- Requires careful categorization

### **Dynamic Duration**
- Adjusts based on participation rates
- Can extend if participation is low
- Advanced feature requiring custom implementation

## Participation Patterns

### **Early vs Late Voting**
- Many voters participate early in the period
- Some wait for discussion and delegate votes
- Consider "last-minute" voting behavior

### **Engagement Strategies During Voting**
- Community calls and discussions
- Delegate recommendations and analysis
- Voting reminders and updates

## Best Practices

1. **Start Conservative**: Begin with longer periods and adjust based on participation data
2. **Monitor Participation**: Track when votes are cast during the period
3. **Community Feedback**: Survey participants about optimal voting windows
4. **Seasonal Adjustments**: Consider holidays and community events
5. **Clear Communication**: Announce voting periods clearly with countdowns

## Common Challenges

### **Low Participation**
- Extend voting periods temporarily
- Improve community engagement and education
- Consider incentive mechanisms

### **Vote Concentration**
- Many votes cast in final hours
- May indicate need for better early engagement
- Consider participation incentives

### **Technical Issues**
- Network congestion affecting voting
- Have contingency plans for technical problems
- Consider gas cost implications during high-congestion periods

## Extending Voting Periods

Some scenarios may require period extensions:

- Critical security vulnerabilities discovered
- Major market events affecting decision context
- Technical issues preventing participation
- Exceptionally complex proposals requiring more analysis

## Related Parameters

- **[Proposal Delay](proposal-delay.md)**: Time before voting begins
- **[Quorum](quorum.md)**: Minimum participation required
- **[TimeLock Delay](timelock-delay.md)**: Delay after voting ends