"""FinBot: GCP billing intelligence agent.

The agent loads its operating instructions from ``instructions.md`` and uses
MCP Toolbox as the governed data-access layer for BigQuery billing exports.
"""

import logging
import os
from datetime import date
from pathlib import Path

from google.adk.agents import Agent
from google.adk.agents.context_cache_config import ContextCacheConfig
from google.adk.apps.app import App
from google.adk.tools.base_toolset import BaseToolset
from toolbox_adk import CredentialStrategy
from vertexai.agent_engines.templates.adk import AdkApp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("finops_agent")

_INSTRUCTIONS = (Path(__file__).parent / "instructions.md").read_text()
TOOLBOX_URL = os.getenv("TOOLBOX_URL", "http://localhost:8080")


def build_instruction(_context) -> str:
    """Inject the current date into the agent instruction."""
    return _INSTRUCTIONS.format(today=date.today().isoformat())


class DynamicToolboxToolset(BaseToolset):
    """Request-scoped MCP Toolbox toolset.

    A new ToolboxToolset is created per request to avoid reusing async HTTP
    sessions across Agent Engine event loops. Tool ordering is kept stable so
    context-cache prefixes remain deterministic.
    """

    def __init__(self, server_url: str):
        super().__init__()
        self.server_url = server_url
        self.credentials = (
            CredentialStrategy.workload_identity(server_url)
            if "run.app" in server_url
            else None
        )

    async def get_tools(self, readonly_context=None):  # noqa: D102
        from google.adk.tools.toolbox_toolset import ToolboxToolset

        try:
            toolbox = ToolboxToolset(
                server_url=self.server_url,
                credentials=self.credentials,
            )
            tools = await toolbox.get_tools(readonly_context)
            return sorted(tools, key=lambda tool: tool.name)
        except Exception:
            logger.exception(
                "Toolbox tool discovery failed | server_url=%s",
                self.server_url,
            )
            raise


toolbox_toolset = DynamicToolboxToolset(TOOLBOX_URL)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="finops_agent",
    description="GCP FinOps agent — analyzes Cloud billing data via MCP Toolbox.",
    instruction=build_instruction,
    tools=[toolbox_toolset],
)

adk_app = App(
    name="finops_cloud_agent",
    root_agent=root_agent,
    context_cache_config=ContextCacheConfig(
        min_tokens=2048,
        ttl_seconds=300,
    ),
)

app = AdkApp(app=adk_app)

logger.info("Agent initialized | name=%s model=%s", root_agent.name, "gemini-2.5-flash")
