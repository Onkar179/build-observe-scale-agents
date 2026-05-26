# References

Curated references for the topics covered in the session.

## Agent Development

- [Agent Development Kit](https://adk.dev/) - open-source framework for building, debugging and deploying agents.
- [ADK docs](https://google.github.io/adk-docs/) - ADK concepts, agents, tools, sessions, evaluation and deployment patterns.
- [Deploy an agent on Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy) - deployment flow, requirements, resource configuration and permissions.

## MCP and Tooling

- [MCP Toolbox for Databases](https://mcp-toolbox.dev/) - official MCP Toolbox site.
- [MCP Toolbox GitHub repository](https://github.com/googleapis/mcp-toolbox) - source code and setup instructions.
- [Google MCP repository](https://github.com/google/mcp) - Google MCP ecosystem and server references.
- [Gemini CLI MCP server configuration](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html) - connecting MCP servers to Gemini CLI through stdio, SSE or streamable HTTP.

## Context Engineering and Caching

- [Vertex AI context caching overview](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) - explicit context caching concepts, use cases and constraints.
- [Gemini API context caching](https://ai.google.dev/gemini-api/docs/caching) - Gemini API caching concepts and examples.

## Observability

- [Trace an agent](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/tracing) - tracing support for Vertex AI Agent Engine and ADK-based agents.
- [Log an agent](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/logging) - logging patterns and how to inspect Agent Engine logs in Cloud Logging.
- [Cloud Trace documentation](https://cloud.google.com/trace/docs) - distributed tracing concepts and trace exploration.
- [Cloud Logging documentation](https://cloud.google.com/logging/docs) - structured logs and log exploration.
- [Cloud Monitoring documentation](https://cloud.google.com/monitoring/docs) - metrics, dashboards, alerting and SLOs.
- [OpenTelemetry semantic conventions for generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - evolving span and attribute conventions for GenAI workloads.

## BigQuery Billing Data and FinOps

- [Set up Cloud Billing export to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup) - required setup steps for exporting billing data.
- [Understand Cloud Billing data tables in BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables) - standard, detailed/resource-level and pricing export table references.
- [BigQuery ML `ML.FORECAST`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-forecast) - forecasting with `ARIMA_PLUS` and related time-series models.
- [BigQuery ML `ML.DETECT_ANOMALIES`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies) - anomaly detection with `ARIMA_PLUS`, `ARIMA_PLUS_XREG` and other model types.
- [BigQuery anomaly detection overview](https://cloud.google.com/bigquery/docs/anomaly-detection-overview) - model options and anomaly detection patterns.

## Security and Identity

- [Cloud Run IAM roles](https://cloud.google.com/run/docs/reference/iam/roles) - `roles/run.invoker` and service access controls.
- [BigQuery IAM roles](https://cloud.google.com/bigquery/docs/access-control) - dataset and job-level permissions such as data viewer and job user.
- [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) - local authentication for Google Cloud SDKs and tools.

## Topic Map

| Session topic | References |
|---|---|
| ADK agent implementation | ADK, ADK docs, Agent Engine deploy |
| MCP Toolbox and governed tools | MCP Toolbox, MCP Toolbox GitHub, Gemini CLI MCP |
| Context engineering | ADK docs, context caching overview, Gemini API caching |
| Context caching economics | Vertex AI context caching, Gemini API caching |
| Agent deployment | Agent Engine deploy, Cloud Run IAM |
| End-to-end observability | Agent tracing, Agent logging, Cloud Trace, Cloud Logging, Cloud Monitoring, OpenTelemetry GenAI conventions |
| Billing export setup | Cloud Billing export setup, billing data tables |
| Forecasting and anomaly detection | BigQuery ML `ML.FORECAST`, `ML.DETECT_ANOMALIES`, anomaly detection overview |
