# Connect MCP Toolbox to Gemini CLI or an AI IDE

The FinBot demo uses MCP Toolbox as the governed tool layer. You can use the same toolbox with Gemini CLI, local IDE agents, or any MCP-compatible client.

Official Gemini CLI MCP docs:

- https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html

## Option 1: Local MCP Toolbox

Use this when you want to run everything from your laptop.

1. Copy the sample tool config.

```bash
cp toolbox/tools.example.yaml toolbox/tools.local.yaml
```

2. Replace placeholders in `toolbox/tools.local.yaml`.

```text
GCP_PROJECT_ID
BILLING_EXPORT_DATASET
```

3. Authenticate locally.

```bash
gcloud auth application-default login
gcloud config set project <your-gcp-project-id>
```

4. Run MCP Toolbox locally.

```bash
toolbox --tools-file toolbox/tools.local.yaml --port 8080
```

Your local MCP endpoint is:

```text
http://localhost:8080/mcp
```

## Gemini CLI: Local Toolbox

Gemini CLI supports MCP servers through `mcpServers` in `settings.json`.

Project-level config:

```text
.gemini/settings.json
```

User-level config:

```text
~/.gemini/settings.json
```

Example:

```json
{
  "mcpServers": {
    "finops-toolbox-local": {
      "httpUrl": "http://localhost:8080/mcp",
      "timeout": 120000,
      "trust": false,
      "includeTools": [
        "get-cost-summary",
        "get-cost-by-project",
        "detect-cost-anomalies"
      ]
    }
  }
}
```

Then start Gemini CLI and check the MCP server status:

```bash
gemini
/mcp
```

Example prompt:

```text
Using the FinOps MCP tools, summarize the top GCP cost drivers for invoice month 202605.
```

## Option 2: MCP Toolbox on Cloud Run

Use this when you want a shared, production-style toolbox endpoint.

Recommended setup:

- Deploy MCP Toolbox to Cloud Run.
- Run it with a dedicated service account.
- Grant that service account only the required BigQuery roles.
- Keep Cloud Run authenticated.
- Grant invoker access only to trusted callers.

Cloud Run endpoint:

```text
https://<finops-toolbox-service>-<hash>-<region>.run.app/mcp
```

## Gemini CLI: Cloud Run Toolbox

For Cloud Run or other Google Cloud-hosted MCP servers, prefer Google-authenticated access instead of copying bearer tokens into config files.

Example using local Google Application Default Credentials:

```json
{
  "mcpServers": {
    "finops-toolbox-cloud-run": {
      "httpUrl": "https://<cloud-run-service-url>/mcp",
      "authProviderType": "google_credentials",
      "oauth": {
        "scopes": ["https://www.googleapis.com/auth/userinfo.email"]
      },
      "timeout": 120000,
      "trust": false,
      "includeTools": [
        "get-cost-summary",
        "get-cost-by-project",
        "detect-cost-anomalies"
      ]
    }
  }
}
```

If your Cloud Run service uses service-account impersonation, configure `targetServiceAccount` and `targetAudience` according to your organization’s auth model.

## Third-Party IDEs and AI Clients

Most MCP-compatible IDEs use a similar `mcpServers` configuration shape.

Local HTTP example:

```json
{
  "mcpServers": {
    "finops-toolbox": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

Remote Cloud Run example:

```json
{
  "mcpServers": {
    "finops-toolbox": {
      "url": "https://<cloud-run-service-url>/mcp",
      "headers": {
        "Authorization": "Bearer <OIDC_ID_TOKEN>"
      }
    }
  }
}
```

Avoid committing static tokens in client config. For production usage, prefer one of these patterns:

- Client-native Google auth, if supported.
- A short-lived OIDC token generated at runtime.
- An internal proxy that injects identity.
- IAP/OAuth in front of Cloud Run.
- Service-account impersonation for trusted developer environments.

## Verification

After connecting the MCP server, ask the client to list or inspect available tools.

Expected tools from the sample config:

- `get-cost-summary`
- `get-cost-by-project`
- `detect-cost-anomalies`

If tools do not appear:

- Restart the AI client after changing MCP config.
- Confirm the toolbox endpoint is reachable.
- Confirm the Cloud Run caller has `roles/run.invoker`.
- Confirm the toolbox service account can query BigQuery.
- Confirm tool names in `includeTools` match the MCP server output.
