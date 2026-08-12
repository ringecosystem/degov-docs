---
description: "Use DeGov events and signals to follow governance activity during a defined time window."
---

# Follow Governance Signals

**Tier:** standard.

Choose the resource that matches the question:

- `events` for event-time records such as proposal creation, voting, execution, and active forum discussion.
- `signals` for curated, deduplicated, prioritized governance updates.

Both require `from` and `to`; the maximum window is 90 days.

```bash
curl -H "x-degov-api-token: <token>" \
  "https://agent-api.degov.ai/v2/signals?from=2026-08-01T00:00:00Z&to=2026-08-08T00:00:00Z&signalTypes=proposal_result,governance_radar&surface=agent&limit=50"
```

Signals use `signalTypes`; events use `eventTypes`. Signals do not accept a `sort` parameter. Read rows from `data.items`, explain why the highest-priority items matter, and open their source URLs when primary context is needed.
