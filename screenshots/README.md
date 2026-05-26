# Screenshots

Selected screenshots from the FinBot demo and post-session analysis.

These images are intentionally minimal. They support the architecture and results shown in the main README without turning the repository into a raw screenshot dump.

The Gemini CLI screenshots capture an agentic analysis workflow over Agent Runtime observability data, using MCP-connected Google Cloud context to compare token usage and latency across baseline and optimized sessions.

| File | What it shows |
|---|---|
| `agent-platform-cache-spans.png` | Agent Platform trace span view filtered to `create_cache`, showing explicit context cache creation spans. |
| `agent-runtime-trace-dag.png` | Agent Runtime trace DAG with LLM calls, context caching and MCP tool execution. |
| `gemini-cli-latency-comparison.png` | Gemini CLI analysis comparing baseline vs optimized/cached agent latency across turns. |
| `gemini-cli-token-savings.png` | Gemini CLI analysis of fresh-token reduction after context caching. |

Notes:

- The screenshots are evidence artifacts, not required to run the demo.
- Avoid adding raw billing data, private project IDs, billing account IDs, user emails, request payloads or unredacted trace/log content.
