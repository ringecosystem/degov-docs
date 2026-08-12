---
description: "DeGov Agent API proposal and topic keys — opaque identifiers returned by the API, never constructed by callers."
---

# Proposal & Topic Keys

The current API addresses proposals and forum topics with **opaque keys** that the API generates and returns. Callers copy the key and pass it to the next endpoint. They never construct, parse, or guess keys.

## Why not raw identifiers?

Provider identifiers differ across governance systems. The API instead returns one transport-safe value:

- The key encodes the full identity (`daoId`, `provider`, `externalId`) internally.
- It is versioned, so the encoding can evolve without breaking callers.
- External ids containing `/`, `:`, `%`, or Unicode round-trip safely.
- Serving-layer internal ids (which can change when data is rebuilt) are never exposed.

## Format

| Kind | Prefix | Example |
| --- | --- | --- |
| Proposal | `p1_` | `p1_eyJkYW9JZCI6ImVucy1kYW8iLCJwcm92aWRlciI6InNuYXBzaG90IiwiZXh0ZXJuYWxJZCI6ImFiYzEyMyJ9` |
| Forum topic | `t1_` | `t1_eyJkYW9JZCI6ImVuc...` |

The part after the prefix is a base64url-encoded identity payload. Treat it as opaque data.

## Where keys come from

| Endpoint | Returns |
| --- | --- |
| `GET /v2/proposals` | `proposalKey` on each item |
| `GET /v2/proposals/resolve` | `proposalKey` on each candidate |
| `GET /v2/events` | `proposalKey` / `topicKey` on each event item |
| `GET /v2/signals` | `proposalKey` / `topicKey` on each signal |
| `GET /v2/forum-topics` | `topicKey` on each item |
| `GET /v2/voters/:voterIdentity/votes` | `proposalKey` on each vote item |

## Using a key

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_eyJkYW9JZCI6ImVucy1kYW8iLCJwcm92aWRlciI6InNuYXBzaG90IiwiZXh0ZXJuYWxJZCI6ImFiYzEyMyJ9/votes/summary"
```

The same key works across every sub-resource of the proposal:

- `GET /v2/proposals/:proposalKey`
- `GET /v2/proposals/:proposalKey/votes/summary`
- `GET /v2/proposals/:proposalKey/votes`
- `GET /v2/proposals/:proposalKey/evidence`

## Rules for callers

1. **Never construct a key.** If you don't have one, get it from a list, resolve, events, or signals endpoint.
2. **Never decode or re-encode a key.** Pass it through unchanged, including URL encoding of the full path segment.
3. **A malformed key** returns `400 VALIDATION_ERROR`.
4. **A well-formed key with no matching proposal** returns `404 NOT_FOUND`.
5. **Keys are not secrets.** They identify public governance data, but they are also not stable forever — if a proposal disappears from coverage, its key may stop resolving.
