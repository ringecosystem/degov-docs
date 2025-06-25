---
description: "Discover how the DeGov Agent autonomously analyzes proposals using polls, comments, and on-chain data to cast informed votes."
---

# Agent Voting

## Overview

As described in [What’s special about the DeGov Agent?](./delegate.md#what-is-special-about-the-degov-agent), the DeGov Agent is an AI-powered delegate that analyzes proposals and votes on behalf of members who delegate to it. This section explains the agent voting workflow, key features, and decision process.

## What is Agent Voting?

![Agent Voting Process](./images/agent-voting-1.png)

Agent voting uses automated analysis to select an on-chain vote option. Clicking the choice button displays the agent’s commentary, with a link to detailed reasoning.

![Voting Comment Preview](./images/agent-voting-2.png)

![Decision Details](./images/agent-voting-3.png)

## How does the agent make a vote decision?

The DeGov Agent relies on the X Interaction Model to gather and analyze both on-chain and off-chain signals:

1. **Proposal Announcement on X**: When a proposal is created, the agent posts a tweet summarizing the proposal, linking to details, and launching a For/Against/Abstain poll. The poll closes before the on-chain voting deadline.
2. **Automatic Updates**: The agent monitors on-chain events (status changes, votes, queueing, execution) and posts progress updates as comments on the original tweet.
3. **Community Voting**: Members can vote on-chain in DeGov or off-chain via the tweet poll. Off-chain poll results do not directly affect on-chain tallies but inform the agent’s analysis.
4. **Final Decision**: After the tweet poll and before on-chain voting ends, the agent synthesizes tweet poll results, comments sentiment, and live on-chain data. It then casts its on-chain vote according to the configured strategy and publishes its rationale as a comment.

![Final Vote Confirmation](./images/agent-voting-4.png)

## Voting Strategy

The DeGov Agent weights multiple inputs to ensure balanced decisions:

1. **Tweet Poll Analysis (40%)**: Assesses majority sentiment, turnout significance, and manipulation risks (bots, Sybil attacks).
2. **Tweet Comment Sentiment (30%)**: Evaluates argument quality in comments, gives extra weight to influential voices, and checks for credibility issues.
3. **On-Chain Voting Metrics (30%)**: Compares off-chain sentiment with on-chain vote distribution and turnout percentage to gauge engagement.
4. **Synthesis & Conflict Resolution**: Combines weighted inputs for a preliminary decision. If off-chain and on-chain signals conflict sharply, the agent abstains to prompt further discussion. Otherwise, it selects the majority-backed option and assigns a confidence score (1–10).

This multi-source framework helps the agent reflect real community opinion while safeguarding against manipulation.

