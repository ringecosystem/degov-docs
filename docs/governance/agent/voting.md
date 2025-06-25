# Agent Voting

## Overview

As the question [What special about the DeGov Agent?](./delegate.md#what-special-about-the-degov-agent) mentioned, the DeGov Agent differentiates itself from other delegates by being an automated AI-powered agent that can analyze proposals and vote on behalf of the community members who delegate their voting power to it. This section will explain how the agent voting works, what it does, and how it makes decisions.

## What is Agent Voting?

![alt text](./images/agent-voting-1.png)

As the image above shows, the agent voting is a process where the agent analyzes the proposals and makes a vote decision based on its analysis. You can click the Choice button to see the agent voting comment, which includes a external link to the details of the motivation behind the vote decision. 

The voting comment looks like this:

![alt text](./images/agent-voting-2.png)

The decision details look like this:

![alt text](./images/agent-voting-3.png)

## How does the agent make a vote decision?

Once you have know how the agent voting works, you may wonder how the agent makes a vote decision. That's really a good question. 

Before explaining the vote decision process, let's first introduce one important design of the Degov Agent: The X Interaction Model.

The X Interaction Model is a design that utilizes the MCP capabilities of the agent to interact proposal with X functionality. A example looks like this: [https://x.com/ai_degov/status/1937692289633067321](![alt text](./images/agent-voting-3.png)). Let's break down the components of the X Interaction Model:

1. When a proposal is created on the DeGov platform, the agent will analyze the proposal, fetch the nessary information, and post a tweet on the official X account of the DeGov Agent. This tweet will include a link to the proposal, a summary of the proposal, and a poll with the For/Against/Abstain options for the community members to vote on. Note the poll end time is set ahead of the proposal voting end time.
2. All the onchain actions about this proposal, such as the proposal status change, other's vote actions, queue, execute, etc., will trigger the agent to made a comment on the previous proposal creation tweet. 
3. During the proposal voting period, users can vote on the proposal to express their preference  by either voting on the proposal directly on the DeGov platform or by voting on the tweet poll created by the agent. Please note that the tweet poll is offchain and the votes on the tweet poll will not be counted as the onchain votes. 
4. Before the proposal voting end time and after the tweet poll end time, the agent will analyze the proposal onchain voting collected so far on the DeGov platform and the tweet poll votes results, comment on the proposal creation twee, then make a vote decision on the proposal acording to the predefined voting strategy. Then, the agent will construct a vote transaction and send it to the DeGov platform to cast the vote onchain.

That's how the agent makes a vote decision. The agent will always make a vote decision before the proposal voting end time representing the community members who delegate their voting power to it. The agent will also make a comment while voting, you can click the comment to see the details of the vote decision.

![alt text](./images/agent-voting-4.png)

## The Agent Voting Strategy

The DeGov Agent employs a rigorous, multi-source analysis framework to determine its voting decision for each governance proposal. The strategy is as follows:

1. Twitter Poll Analysis (40%)
The agent first evaluates the sentiment and credibility of the Twitter poll associated with the proposal. It identifies the majority sentiment (For/Against/Abstain), assesses whether participation is meaningful relative to the follower base, and checks for signs of manipulation such as bot activity or Sybil attacks.

2. Tweet Comment Analysis (30%)
The agent conducts a detailed sentiment analysis of the comments under the proposal tweet. It extracts and evaluates the quality of arguments from both supporters and opponents, pays special attention to influential voices (KOLs, team members, whales), and again checks for credibility issues like bot activity.

3. On-Chain Voting Data Verification (30%)
The agent compares on-chain voting results with social sentiment, analyzing both the breadth (number of unique voters) and depth (distribution of voting power) of participation. It also assesses overall turnout as a percentage of circulating supply to gauge community engagement.

4. Synthesis and Final Decision
The agent integrates the above analyses using their conceptual weights to form an initial decision. If there is a severe conflict—where social sentiment (Twitter poll and comments) is the direct opposite of on-chain voting—the agent will abstain, signaling the need for further community discussion. Otherwise, the agent selects the outcome most strongly supported by the weighted data and assigns a confidence score (1-10) based on the consistency and quality of the data.

This strategy ensures that the agent’s vote reflects both on-chain stakeholder actions and the broader community’s social sentiment, while safeguarding against manipulation and signaling when further deliberation is needed.

