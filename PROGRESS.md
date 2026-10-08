# Progress

## M0 - Understand and Approve

Status: REVIEW
Reviewer: SELF_REVIEW

### Inspection Report

Workspace path:
`C:\Users\gudda\OneDrive\Pictures\Desktop\Ai calling agent`

Observed files:
- `CONTEXT.md`
- `REQUIREMENTS.md`
- `FEATURES.md`
- `END_GOAL.md`
- `COORDINATOR.md`

Path note: The owner referenced `docs/*.md`, but the specification files are
present at the workspace root.

Git status: BLOCKED for repository checks. The workspace is not currently a Git
repository, so branch, diff, and commit status are unavailable.

Dependencies: No dependency manifest was found. No `requirements.txt`,
`pyproject.toml`, lockfile, or package metadata was present.

Entry points: No Streamlit app, FastAPI app, worker, script, or service entry
point was found.

Tests: No test files or test configuration were found.

Application implementation: NOT_STARTED. The workspace currently contains a
specification pack and generated coordination documents only.

### Business Flow in Plain Language

Institution staff collect prospective student leads by uploading an Excel file
or entering a single lead. The backend validates the data, saves approved records,
and lets mentors review the lead list. After owner-approved calling policy and
eligibility checks, a campaign queues calls. A future calling worker conducts the
conversation using approved institution knowledge, records both sides of the
transcript, assesses interest from evidence, and shows mentors what happened and
what follow-up is needed.

### Confirmed Requirements

- Excel lead intake, including validation preview and reconciled outcomes (C01).
- Individual lead entry using the same validation rules (C02).
- Durable database persistence after a database is selected (C03).
- Mentor visibility into leads, attempts, transcripts, and interest (C04).
- Automatic outbound calling through a real integration later, under policy (C05).
- Approved institution/course/fee/product explanations (C06).
- Two-way student conversation (C07).
- Both-speaker transcripts linked to lead and call (C08).
- Evidence-based interest identification (C09).
- Design and validation toward at least 1,000 calls/day after D01 is resolved
  (C10).

### Safeguards to Preserve

S01-S12 require backend-enforced identity/access, safe intake, contact eligibility
and suppression, campaign controls, durable jobs, reliable call lifecycle,
approved knowledge, evidence-based assessment, privacy/retention controls, safe
development defaults, monitoring/recovery, and deployment evidence.

### Proposed Enhancements Not in Default Scope

E01-E06 are not implemented by default: automatic mentor assignment, audio
recording/playback, live transfer/demo/calendar booking, multi-institution SaaS
billing, WhatsApp/SMS/email notifications, and inbound/public browser calling.

### Open Decisions

Open decisions D01-D13 are recorded in `DECISIONS.md`. All defaults there are
proposals only.

### SELF_REVIEW

Verdict: PASS for M0 inspection and planning readiness, with blockers noted.

Evidence:
- All five source specification files were read completely from the workspace
  root.
- Repository inspection found no app source, Git repository, dependency manifest,
  entry points, or tests.
- Missing coordination documents were created from the specification pack without
  application code changes.

Remaining blockers:
- Owner approval is needed for the M1 plan and the open decisions that affect
  implementation, especially D02, D10, and D12.

## M1 - Lead Foundation

### M1-T01 - Python Project Skeleton and Local Checks

Status: VERIFIED
Reviewer: SELF_REVIEW

What changed:
- Added Python project metadata in `pyproject.toml`.
- Added a FastAPI backend entry point with `GET /health`.
- Added a Streamlit staff console shell.
- Added `.env.example`, `.gitignore`, README run notes, and a backend health test.

Business outcome:
The workspace now has a runnable foundation for the fixed Python/FastAPI/
Streamlit stack. No lead data, database, provider integration, identity system,
or calling behavior was implemented.

Checks and results:
- `python -m pytest` -> PASS, 1 test passed.
- Direct backend import with `src` on `PYTHONPATH` -> PASS, app title reported as
  `Admissions Calling Agent API`.

Evidence notes:
- FastAPI/Starlette emitted 12 deprecation warnings under Python 3.14.
- `fastapi.testclient.TestClient` hung in this environment, so the current M1-T01
  test verifies the registered `/health` route directly.

Mock versus live status:
Mock/synthetic only. Real calling is still not implemented and remains disabled.

Next task:
M1-T02 is VERIFIED.

### M1-T02 - Lead Field Contract and Validation Rules

Status: VERIFIED
Reviewer: SELF_REVIEW

What changed:
- Created `LeadCreate` Pydantic model with fields: name, phone_number, source, contact_permission_granted, course_interest.
- Implemented explicit phone number normalization using a configurable country context (default +91).
- Implemented strict contact permission checking (blank is not granted).
- Added test suite `test_lead_validation.py` covering valid leads, normalization, missing fields, invalid phone numbers, and blank permissions.

Business outcome:
The backend now enforces the approved data contract (D10) for any future manual or Excel intake, ensuring no lead is saved without valid contact information and explicit permissions.

Checks and results:
- `python -m pytest tests/backend/test_lead_validation.py` -> PASS, 6 tests passed.

Evidence notes:
- Phone normalization explicitly prefixes +91 or other contexts.
- Blank permission results in a clear validation error.

Mock versus live status:
Mock/synthetic only. Real calling remains disabled.

Next task:
M1-T03 is VERIFIED.

### M1-T03 - Persistence Boundary and Local Database Setup

Status: VERIFIED
Reviewer: SELF_REVIEW

What changed:
- Configured SQLAlchemy 2.x and Alembic (design note created in DESIGN_M1_T03.md).
- Created `LeadModel` mapped to a SQLite database.
- Implemented `LeadRepository` exposing an abstract boundary for the API/service layer.
- Added tests verifying pagination limits (max page size 100), duplicate-phone lookups, retention of suppression flags on re-imports, missing config failure, and cross-process durability.

Business outcome:
The application can now durably save leads in a local database (SQLite) using a Postgres-compatible abstraction, ensuring no data loss on restarts and protecting against improper updates to suppressed leads.

Checks and results:
- `python -m pytest tests/backend/test_repository.py` -> PASS, verified cross-process restart, 100-limit pagination, duplicate lookup, suppression flag logic.
- Total pytest suite -> PASS, 12 tests passed.

Mock versus live status:
Mock/synthetic only. Local SQLite database. No external integrations.

Next task:
M1-T04 is READY (Manual Lead API)

### M1-T04..T10 (this cycle)
Status: see TASKS.md. Checks: `python -m pytest` -> 46 passed; Streamlit AppTest smoke -> no exceptions;
Vercel entrypoint import -> OK. Mock/synthetic only; UI not browser-tested; Vercel deploy NOT performed from this environment.
