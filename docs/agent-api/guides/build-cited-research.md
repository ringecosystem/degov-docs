---
description: "Build a cited DAO governance explanation from current proposal resources and official source evidence."
---

# Build a Cited Research Brief

1. Discover a proposal or resolve an exact external URL.
2. Fetch proposal detail for its body, source links, voting window, outcome, and execution status.
3. Add vote summary or vote rows only when they affect the answer.
4. Open `source.url` and any `source.discussionUrl` for primary text, executable actions, or disputed facts.
5. Separate confirmed facts, interpretation, and missing evidence in your answer.

```bash
curl -sS -H "x-degov-api-token: $DEGOV_API_TOKEN" \
  "https://agent-api.degov.ai/v2/proposals/$PROPOSAL_ID"
```

A research brief is an agent-produced answer grounded in retrieved evidence, not a public API endpoint. The contract does not provide an evidence bundle or executable calldata. Verify targets, permissions, transfers, timelocks, and execution transactions through official governance sources and explorers.

Cite the relevant source URLs, explain the requested time range, and identify missing or stale information. `dataAsOf` is record provenance; a successful request does not guarantee complete or current coverage. For a security question, apply [DAO Governance Security](../../agent-skills/dao-governance-security.md) after collecting the available evidence.
