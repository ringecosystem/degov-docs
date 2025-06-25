# FAQs

#### Who controls the private key of the agent?

Currently, the private key of the agent is controlled by the RingDAO team. We may consider decentralizing the control of the agent in the future, but for now, it is managed by the team to ensure the integrity and reliability of the agent's operations.

#### Will the agent is available for all DAOs on the DeGov platform?

There is no exact answer to this question. The agent service is developed as a plugin https://github.com/ringecosystem/degov-essential and work together with the DeGov platform. As the degov is open source, anyone can deploy their own degov instance. If you want to use the agent service, you need to maintain a extra agent service to work with your degov instance. By default, for all the DAOs created on the DeGov platform, the agent service is available and can be used by the community members to delegate their voting power to the agent.

#### Will all the DAOs on the DeGov platform use the only one X account to interact with the agent?

Yes, currently all the DAOs on the DeGov platform use the official X account [https://x.com/ai_degov](https://x.com/ai_degov)

#### Does the agent know who voted for/against/abstain on the proposal tweet poll?

No, the agent does not know who voted for/against/abstain on the proposal tweet poll because the limited visibility of the X platform. The agent can only see the total number of votes for each option (For/Against/Abstain) but not the individual voters' identities.

#### Will the vote on the proposal tweet poll be counted as the onchain vote?

No, the votes on the proposal tweet poll will not be counted as the onchain votes. The tweet poll is an offchain mechanism to gather community opinions. In addition, the tweet poll results is only part of the information that the agent uses to make a vote decision on the proposal.

#### Will someone maliciously vote on the proposal tweet poll to influence the agent's vote decision?

There is a possibility that someone may try to manipulate the proposal tweet poll by voting in a way that does not reflect their true opinion. 
However, please note that the tweet poll or comment is only part of the information that the agent uses to make a vote decision on the proposal. The agent will also analyze the onchain voting data and the judgment of the proposal itself to avoid being influenced by malicious votes.

#### For the proposal tweet poll, how does the agent handle the votes?

There is a poll end time set ahead of the proposal voting end time. The agent will analyze the tweet poll votes results before the proposal voting end time and make a vote decision based on the predefined voting strategy. See the section [How does the agent make a vote decision?](./voting.md#how-does-the-agent-make-a-vote-decision) for more details.


