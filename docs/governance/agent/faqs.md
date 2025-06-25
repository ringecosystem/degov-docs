---
description: "Frequently asked questions about the DeGov Agent's key management, availability, and voting process."
---

# FAQs

**Who controls the agent’s private key?**  
The agent’s private key is currently managed by the RingDAO team to ensure reliability and security. We plan to explore decentralized key management in the future.

**Is the agent available for all DAOs on DeGov?**  
Yes. The agent runs as an open-source plugin (https://github.com/ringecosystem/degov-essential) alongside DeGov. Anyone hosting a DeGov instance can deploy the agent service and enable it for their DAO.

**Do all DAOs share the same X account?**  
Yes. All DAOs on the DeGov platform use the official X account: [@ai_degov](https://x.com/ai_degov).

**Can the agent see who voted in the tweet poll?**  
No. Due to X’s privacy limitations, the agent only sees aggregate poll results (For/Against/Abstain), not individual voter identities.

**Are tweet poll votes counted as on-chain votes?**  
No. The tweet poll is an off-chain gauge of community sentiment. On-chain votes follow DeGov’s smart contracts. Poll results only inform the agent’s analysis.

**What prevents malicious manipulation of the tweet poll?**  
The agent uses a multi-source strategy. Poll votes are one input, combined with on-chain vote data and comment sentiment. The agent also detects abnormal activity (bots, Sybil attacks) when evaluating poll results.

**How does the agent use tweet poll data?**  
The poll closes before on-chain voting ends. The agent analyzes poll results, sentiment from comments, and on-chain metrics to cast its vote based on its configured strategy. See [How does the agent make a vote decision?](./voting.md#how-does-the-agent-make-a-vote-decision) for details.


