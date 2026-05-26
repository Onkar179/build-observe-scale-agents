# MCP Toolbox

This folder contains a sanitized MCP Toolbox configuration for the FinBot demo.

| File | Purpose |
|---|---|
| `tools.example.yaml` | Example BigQuery-backed MCP tools for billing summary, project breakdown and anomaly detection. |

Before running it:

1. Copy `tools.example.yaml` to a local config file.
2. Replace `GCP_PROJECT_ID` and `BILLING_EXPORT_DATASET`.
3. Confirm the billing export tables exist.
4. Run MCP Toolbox locally or deploy it to Cloud Run.

Do not commit real project IDs, billing account IDs, credentials or customer data.
