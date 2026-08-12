---
description: "Reference for DeGov Agent API event and curated signal feeds."
---

# Events & Signals

| Method | Path | Tier | Purpose |
| --- | --- | --- | --- |
| GET | `/v2/events` | standard | Event-time governance records |
| GET | `/v2/signals` | standard | Curated and prioritized governance updates |

Both require RFC 3339 `from` and `to` with a maximum 90-day window.

Events accept `eventTypes`, `timeBasis`, `importanceMin`, DAO, limit, and cursor. Signals accept `signalTypes`, `timeBasis`, `priorityMin`, `surface`, DAO, limit, and cursor. Signals do not accept `sort`.

Event items expose `eventId`, `eventType`, `eventTimeMs`, DAO ID, item type, title, URL, importance, and available proposal/topic keys. Signal items expose ID, type, priority, actionability, DAO ID, title, summary, source URL, severity, and available keys.
