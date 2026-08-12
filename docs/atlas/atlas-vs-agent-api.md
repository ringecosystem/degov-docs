---
description: "Choose DeGov Atlas for human exploration or Agent API for programmatic integration."
---

# Atlas vs. Agent API

| Need | Use |
| --- | --- |
| Browse, search, compare, and follow links as a person | Atlas |
| Build an agent, partner integration, or repeatable data workflow | Agent API |
| Inspect primary proposal or forum content | The official source linked by Atlas or the API |

Atlas server routes under `/atlas/*` are protected implementation details used by the application. They are not a public integration contract, even though a route directory may be visible in OpenAPI. Do not scrape Atlas or call its protected backend routes; use the Agent API.
