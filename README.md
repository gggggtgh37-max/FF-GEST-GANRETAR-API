# Guest Gen API — Vercel deployment

## Deploy
1. Extract these files so `app.py`, `requirements.txt`, and `vercel.json` are in the repository root.
2. Import the repository into Vercel as a new project (or select the existing project).
3. In Project Settings → General, ensure Root Directory is the folder containing these files.
4. Deploy from the Production branch and wait for the deployment to show **Ready**.
5. In Project Settings → Domains, add `anff95.vercel.app` to this exact project. If it is already assigned to another project, remove it there first, then add it here.

## Test
- `/` — API information
- `/health` — health check

This deployment is a basic API health/status service. It does not implement third-party guest-account registration.
