# AI Admissions Calling Agent

This workspace is for a Python application using:

- FastAPI for trusted backend operations
- Streamlit for the staff console
- LiveKit for a later voice milestone

The current implementation is M1: validation, persistence, manual and Excel lead intake, dev access control, mock calling guard, Streamlit console. It
does not include provider integrations, real calls, real
student data, or production identity.

## Local Checks

Run tests:

```powershell
python -m pytest
```

Database Setup:

```powershell
$env:PYTHONPATH = "src"
python -m admissions_calling_agent.backend.persistence.setup --setup
```

Run the backend:

```powershell
$env:PYTHONPATH = "src"
python -m uvicorn admissions_calling_agent.backend.app:app --reload
```

Run the staff console:

```powershell
$env:PYTHONPATH = "src"
python -m streamlit run src/admissions_calling_agent/staff_console/app.py
```

Alternatively, install the project in editable mode before running commands:

```powershell
python -m pip install -e .[dev]
```

## Safety Status

Mock/synthetic mode is the only current mode. Real calling is not implemented and
must remain disabled until the owner explicitly approves providers, recipients,
policy, and spending limits.

## Dev auth
Set `DEV_AUTH_TOKEN` (any strong string). Send `X-Dev-Token` and `X-Dev-Role` (admin/mentor/uploader/operator). Non-production only.

## Deploy API to Vercel (demo, synthetic data only)
Import the GitHub repo in Vercel, add env var `DEV_AUTH_TOKEN`, deploy. Data is ephemeral. Run Streamlit elsewhere
(`STAFF_CONSOLE_API_BASE_URL` = your Vercel URL).
