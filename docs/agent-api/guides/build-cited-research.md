---
description: "Build a source-aware DAO governance brief from proposal detail, evidence, and primary sources."
---

# Build a Cited Research Brief

**Tier:** plus after proposal discovery.

1. Resolve or discover a proposal key.
2. Fetch proposal detail for normalized content and source URLs.
3. Fetch evidence only when provenance, quality, or auditability affects the answer.
4. Open official source URLs to verify intent, executable actions, deadlines, or disputed facts.
5. Separate confirmed facts, interpretation, and missing evidence.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_opaque"

curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/proposals/p1_opaque/evidence"
```

Evidence can contain provenance, source references, intelligence availability, quality flags, and warnings. It is not required for an ordinary proposal explanation. Always disclose stale, partial, backfilling, unavailable, or conflicting evidence.
