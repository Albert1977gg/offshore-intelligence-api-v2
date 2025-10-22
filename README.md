# 🌊 Offshore Intelligence API v2

A lightweight Flask API that provides:
- Offshore wind installation backlog data  
- Live offshore wind headlines (via RSS)

## Endpoints

| Path | Description |
|------|--------------|
| `/` | Health check |
| `/api/backlog` | Returns example offshore installation projects |
| `/api/news` | Fetches latest offshore wind headlines |
| `/openapi.yaml` | OpenAPI schema for integration with ChatGPT |

## Deployment
Hosted on **Render**, automatically redeploys on GitHub commits.
