# Agent App

Core FinBot agent files.

| File | Purpose |
|---|---|
| `agent.py` | ADK agent definition, request-scoped MCP Toolbox toolset and Agent Engine app wrapper. |
| `instructions.md` | FinBot operating instructions, response tiers and tool-routing policy. |
| `__init__.py` | Python package marker for ADK discovery. |

`agent.py` expects `TOOLBOX_URL` to point to a running MCP Toolbox endpoint.
