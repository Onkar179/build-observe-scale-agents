# Config

Example environment files for local and deployment-oriented runs.

| File | Purpose |
|---|---|
| `dev.env.example` | Local/dev environment template. |
| `prod.env.example` | Production-style environment template. |

Copy an example before editing:

```bash
cp config/dev.env.example config/dev.env
```

Never commit real `.env` files, project secrets or service account keys.
