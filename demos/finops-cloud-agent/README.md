# FinBot - GCP FinOps Agent

FinBot is the demo agent from the session "Build. Observe. Scale." It analyzes Google Cloud billing data through MCP Toolbox and demonstrates production AI agent patterns with ADK, Gemini Enterprise Agent Platform and Google Cloud observability.

This folder is sanitized for public sharing. Add your own project IDs, datasets and deployment metadata locally.

## Project Structure

```
finops-cloud-agent/
├── app/
│   ├── agent.py          # ADK agent, MCP Toolbox toolset, Agent Engine app
│   ├── instructions.md   # FinBot system prompt and response policy
│   └── __init__.py
├── config/
│   ├── dev.env.example
│   └── prod.env.example
├── pyproject.toml
└── README.md
```

## Requirements

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/) ([add packages](https://docs.astral.sh/uv/concepts/dependencies/) with `uv add <package>`)
- **agents-cli**: Agents CLI - Install with `uv tool install google-agents-cli`
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **BigQuery billing export**: Standard billing export enabled for your own project.
- **MCP Toolbox**: Deployed locally or on Cloud Run with tools configured for your billing export dataset.

Google Cloud setup:

```bash
gcloud auth application-default login
gcloud config set project <your-gcp-project-id>
```

Required IAM for the identity used by MCP Toolbox:

- `roles/bigquery.dataViewer`
- `roles/bigquery.jobUser`

If MCP Toolbox runs on Cloud Run, the caller also needs:

- `roles/run.invoker`


## Quick Start

Install dependencies:

```bash
agents-cli install
```

Configure your local environment:

```bash
cp config/dev.env.example config/dev.env
export TOOLBOX_URL=http://localhost:8080
```

`TOOLBOX_URL` must point to a running MCP Toolbox server with billing tools configured for your BigQuery billing export.

Run with Agents CLI:

```bash
agents-cli playground
```

Alternative ADK commands:

```bash
uv run adk run app
uv run adk web .
```

Use `agents-cli playground` for the most reliable local path in this project. `adk run app` gives you an interactive CLI chat loop. `adk web .` starts the ADK web UI for the current agents directory, but it still requires `TOOLBOX_URL` and Google credentials to be configured.

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `uv run adk run app` | Run the agent in an interactive CLI loop |
| `uv run adk web .` | Start the ADK web UI for the current agents directory |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli deploy`  | Deploy agent to Agent Runtime                                                                |
| `agents-cli publish gemini-enterprise` | Register deployed agent to Gemini Enterprise                    |

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.

For public demos, keep message capture settings conservative and avoid storing sensitive prompts or responses in span attributes.
