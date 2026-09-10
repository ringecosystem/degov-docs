---
description: "Use DeGov DAO slugs, opaque proposal and topic IDs, and normalized voter identities without guessing or decoding."
---

# Public Identifiers

| Field | Meaning | Obtain it from |
| --- | --- | --- |
| `daoId` | Public DAO slug | DAO directory |
| `proposalId` | Opaque proposal identifier beginning with `p1_` | Proposal list, exact resolver, or voter history |
| `topicId` | Opaque topic identifier beginning with `t1_` | Forum topic list |
| `voterId` | Normalized voter identity; EVM addresses are lowercase | Participant or vote resources |

Pass returned values back unchanged, URL-encoding path segments when constructing requests. Do not derive a DAO slug from a name, encode your own proposal identifier, or reuse a provider's raw ID as `proposalId`. The `p1_` and `t1_` prefixes identify opaque formats, not API versions.

The documentation uses `p1_<opaque>` as a placeholder: replace it with a real response value before calling a detail or vote route. `topicId` supports caching and deduplication; the public contract has no standalone forum-topic detail route.

For an exact external proposal URL or complete source identity, use [proposal resolution](../guides/resolve-external-proposal.md). For a title, use proposal search instead.
