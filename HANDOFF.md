# Handoff

## Current State
Milestone: M1 - Lead foundation. Tasks M1-T01..T05, T08, T09 VERIFIED; T06, T07 (Streamlit UI) and T10 in REVIEW.
Reviewer: SELF_REVIEW. `python -m pytest` -> 46 passed.

## Important note
The earlier `src/` and `tests/` folders were not in the uploaded pack, so M1-T01..T03 were
re-implemented from the specs. If you have the original code locally, diff before merging.

## What exists
FastAPI backend (leads, Excel preview/commit, dev auth, mock calling guard), SQLAlchemy+Alembic persistence,
Streamlit console, Vercel entrypoint (`api/index.py`, `vercel.json`).

## Mock versus live
Mock/synthetic only. No real calls, LLMs, speech or telephony providers. No API keys are needed or used.

## Deployment caveats (owner must accept)
- Vercel hosts the FastAPI API only; Streamlit needs a long-running server (e.g. Streamlit Community Cloud, Render).
- Vercel storage is ephemeral (`/tmp` SQLite): demo data disappears. Not a production database (D02).
- Dev identity is NON-PRODUCTION: set a strong DEV_AUTH_TOKEN, use synthetic data only.

## Open decisions
D01, D08, D11, D13. Next ready task: M2 planning (institution knowledge + mock conversation) after owner approval.
