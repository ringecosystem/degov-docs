---
description: "Discover how the DeGov Agent autonomously analyzes proposals using polls, comments, and on-chain data to cast informed votes."
---

# Agent Voting

## What is Agent Voting?

As described in [What’s special about the DeGov Agent?](./delegate.md#what-is-special-about-the-degov-agent), the "DeGov Agent" is a specialized AI-powered delegate that analyzes proposals and votes on behalf of members who delegate to it, it always appears first in the `Delegates` tab. see the image below:

![alt text](./images/agent-delegates.png)

Agent voting uses automated analysis to select an on-chain vote option with a comment explaining the decision, then votes on-chain before the proposal deadline. You can click the agent's vote comment to view the detailed reasoning behind its decision.

![Agent Voting Process](./images/agent-voting-1.png)

The agent's vote comment looks like this:

![Voting Comment Preview](./images/agent-voting-2.png)

The decision details looks like this:

![Decision Details](./images/agent-voting-3.png)

The above details page explains in detail what the agent's vote is based on, including the analysis of the proposal, the sentiment of comments, and the results of the tweet poll. This transparency helps community members understand how the agent arrived at its decision. 

However, where does these information come from? Keep reading to find out.

## How does the agent make a vote decision?

The DeGov Agent relies on the X Interaction Model to gather and analyze both on-chain and off-chain signals:

1. **Proposal Announcement on X**: When a proposal is created, the agent posts a tweet summarizing the proposal, linking to details, and launching a For/Against/Abstain poll. The poll closes before the on-chain voting deadline. 
    
    An example tweet might look like this: [https://x.com/ai_degov/status/1945708657796165884](https://x.com/ai_degov/status/1945708657796165884)

    ![Final Vote Confirmation](./images/agent-voting-4.png)

    You can also view the tweet link in the proposal details page, which looks like this:

    ![Final Vote Confirmation](./images/agent-voting-5.png)
    
2. **Automatic Updates**: The agent monitors on-chain events (status changes, votes, queueing, execution) and posts progress updates as comments on the original tweet.
3. **Community Voting**: Members can vote on-chain in DeGov or off-chain via the tweet poll. Off-chain poll results do not directly affect on-chain tallies but inform the agent’s analysis.
4. **Final Decision**: After the tweet poll and before on-chain voting ends, the agent synthesizes tweet poll results, comments sentiment, and live on-chain data. It then casts its on-chain vote according to the configured strategy and publishes its rationale as a comment.



## Voting Strategy

The DeGov Agent weights multiple inputs to ensure balanced decisions:

1. **Tweet Poll Analysis (40%)**: Assesses majority sentiment, turnout significance, and manipulation risks (bots, Sybil attacks).
2. **Tweet Comment Sentiment (30%)**: Evaluates argument quality in comments, gives extra weight to influential voices, and checks for credibility issues.
3. **On-Chain Voting Metrics (30%)**: Compares off-chain sentiment with on-chain vote distribution and turnout percentage to gauge engagement.
4. **Synthesis & Conflict Resolution**: Combines weighted inputs for a preliminary decision. If off-chain and on-chain signals conflict sharply, the agent abstains to prompt further discussion. Otherwise, it selects the majority-backed option and assigns a confidence score (1–10).

This multi-source framework helps the agent reflect real community opinion while safeguarding against manipulation.

