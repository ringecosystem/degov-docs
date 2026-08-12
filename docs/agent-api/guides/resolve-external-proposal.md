---
description: "Resolve a governance proposal URL, title, or external ID to a DeGov proposal key."
---

# Resolve an External Proposal

**Tier:** standard.

Use resolve only when you have a URL, title, or external ID but no `proposalKey`. Supply exactly one identifier and add `daoId` or `provider` when it reduces ambiguity.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/resolve?url=https%3A%2F%2Fsnapshot.org%2F%23%2Fexample%2Fproposal%2F0xabc&daoId=example-dao"
```

Read candidates from `data.candidates`. `match.type` describes how the candidate matched; it is not a probability. Select the candidate whose DAO, provider, title, and source URL agree with the user's input, then pass its opaque `proposalKey` to detail resources.

An empty candidate list means the proposal was not resolved. Try a more exact identifier or verify it through the official governance source.
