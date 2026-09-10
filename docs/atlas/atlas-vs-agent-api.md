---
description: "Choose DeGov Atlas for human exploration or Agent API for programmatic integration."
---

# Atlas vs. Agent API

| Need | Use |
| --- | --- |
| Browse, search, compare, and follow links as a person | Atlas |
| Build an agent, partner integration, or repeatable data workflow | Agent API |
| Inspect primary proposal or forum content | The official source linked by Atlas or the API |

Atlas is public to browse and includes application-specific activity, discussion, timeline, and signal views. The [Agent API](../agent-api/index.md) exposes a focused public subset through 11 documented governance operations. A feature visible in Atlas does not imply a matching public API endpoint.

Atlas's protected application routes are separate from the public OpenAPI contract. Use the Agent API base URL `https://agent-api.degov.ai` for integrations. Square's GraphQL and MCP services at `api.degov.ai` are another separate product surface with their own authentication.
