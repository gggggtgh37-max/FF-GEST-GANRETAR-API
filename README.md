# Guest Gen API — Vercel-ready safe deployment

## Deploy
1. Extract this ZIP and upload the folder to a GitHub repository.
2. Import the repository in Vercel.
3. Keep the project root at the folder containing `app.py` and `vercel.json`.
4. Deploy. No build command or environment variables are required.

## Routes
- `GET /` — service information
- `GET /health` — health check
- `GET /v3/generate` — returns HTTP 501 because third-party account registration is not included.

The original source attempted automated account creation against a third-party game service,
including fabricated client identity and forwarded-IP headers. Those operations are not
included in this deployment.
