# Tasks

Statuses: NOT_STARTED, READY, IN_PROGRESS, REVIEW, VERIFIED, BLOCKED.

## M0 - Understand and Approve

### M0-T01 - Repository and Specification Inspection

Status: REVIEW
Requirement/feature IDs: M0, C01-C10, S01-S12, F01-F09
Objective: Inspect the workspace, reconcile scope, record open decisions, and
prepare an M1 implementation plan.
In-scope paths: `CONTEXT.md`, `REQUIREMENTS.md`, `FEATURES.md`, `END_GOAL.md`,
`COORDINATOR.md`, `AGENTS.md`, `DECISIONS.md`, `TECHNOLOGY.md`,
`ARCHITECTURE.md`, `SOURCES.md`, `PROGRESS.md`, `TASKS.md`, `HANDOFF.md`.
Excluded changes: application code, dependency installation, provider selection,
real calls, real student data, destructive changes.
Acceptance tests/evidence: all source docs read; tree/status/dependency/entry
point/test inspection recorded; D01-D13 recorded; M1 task plan produced.
Risks: source files were located at workspace root rather than under `docs/`;
workspace is not a Git repository.
Reviewer: SELF_REVIEW

## M1 - Lead Foundation Plan

### M1-T01 - Python Project Skeleton and Local Checks

Status: VERIFIED
Requirement/feature IDs: S10, S12; supports F01, F02, F09
Objective: Create the minimal Python project structure for FastAPI, Streamlit,
and automated tests without implementing business behavior.
In-scope paths: `pyproject.toml`, `README.md`, `.env.example`, `.gitignore`,
backend package, staff console package, test configuration.
Excluded changes: database/provider selection, real calls, real student data,
production deployment.
Acceptance tests: local test command runs; backend health endpoint test passes;
Streamlit entry point is documented; no secrets are present.
Risks: dependency choices must stay within the fixed stack and avoid paid
services.
Evidence: `python -m pytest` passed on 2026-10-08 with 1 test passing and 12
FastAPI/Starlette deprecation warnings under Python 3.14. Direct package import
works when `src` is on `PYTHONPATH`. `fastapi.testclient.TestClient` hung in this
environment, so the current skeleton test verifies the registered route directly.
Reviewer: SELF_REVIEW

### M1-T02 - Lead Field Contract and Validation Rules

Status: VERIFIED
Requirement/feature IDs: C01, C02, S02, S03, D10, F01
Objective: Define and test the lead intake data contract used by both manual and
Excel flows.
In-scope paths: backend schemas/domain validation, validation tests, synthetic
fixtures.
Excluded changes: real student data, calling logic.
Acceptance tests: valid synthetic leads pass; invalid phone/missing required
fields fail with row/form reasons; blank permission is not treated as granted.
Risks: D10 is approved for synthetic data only.
Evidence: Created LeadCreate pydantic model with phone normalization (+91 default context) and explicit permission checks. `python -m pytest tests/backend/test_lead_validation.py` passes 6 tests.
Reviewer: SELF_REVIEW

### M1-T03 - Persistence Boundary and Local Database Setup

Status: VERIFIED
Requirement/feature IDs: C03, S05, S12, D02, F01, F02
Objective: Implement durable lead persistence behind an approved database
boundary.
In-scope paths: backend persistence layer, migration/setup notes, repository
tests.
Excluded changes: silently choosing a production database, provider secrets,
call-job dispatch.
Acceptance tests: create lead, restart API/test process, retrieve saved lead;
pagination query works on synthetic records.
Risks: D02 is approved for SQLite local / Postgres-compatible abstraction.
Evidence: Created LeadRepository with SQLAlchemy 2.x and SQLite, enforced constraints on suppression. Tests cover pagination, missing config failure, suppression retention on updates, duplicate lookups, and restarts.
Reviewer: SELF_REVIEW

### M1-T04 - Manual Lead API

Status: VERIFIED
Requirement/feature IDs: C02, C03, S01-S03, F01
Objective: Add backend endpoints for creating one lead through validated input.
In-scope paths: FastAPI lead routes, service layer, persistence tests, API tests.
Excluded changes: Streamlit UI, Excel import, calling/campaign behavior.
Acceptance tests: authorized synthetic staff can create a lead; unauthorized
caller is rejected; saved lead appears in API list/detail after refresh.
Risks: D12 identity approach is open; use only approved dev identity if allowed.
Evidence: POST/GET /leads tests: 401/403/503 auth, create, visible after simulated restart, 409 duplicate, 422 invalid/blank permission. 46 tests pass.
Reviewer: SELF_REVIEW


### M1-T05 - Excel Intake Preview and Commit API

Status: VERIFIED
Requirement/feature IDs: C01, C03, S02, S03, F01
Objective: Parse `.xlsx` uploads, map columns, validate rows, preview outcomes,
and commit valid rows idempotently.
In-scope paths: FastAPI import routes, Excel parser service, validation tests,
synthetic workbooks.
Excluded changes: `.xls`/CSV support unless approved, formula execution, real
student data, automatic calling after upload.
Acceptance tests: synthetic workbook reports created/invalid/duplicate/skipped
counts that reconcile to total rows; repeat commit does not duplicate leads.
Risks: Excel parsing dependency must be reviewed; duplicate policy needs owner
confirmation where business-specific.
Evidence: xlsx preview/commit tests: counts reconcile on 7-row and 1,000-row synthetic files, idempotent commit, re-import flags existing duplicates, formulas/macros/non-xlsx rejected, preview saves nothing.
Reviewer: SELF_REVIEW


### M1-T06 - Staff Console Lead Intake UI

Status: REVIEW
Requirement/feature IDs: C01, C02, C03, S01-S03, F01
Objective: Build Streamlit screens for manual entry and Excel preview/commit
against backend APIs.
In-scope paths: Streamlit staff console pages/components, UI tests or smoke
checks, demo synthetic workbook.
Excluded changes: direct database writes from Streamlit, provider settings,
campaign start controls.
Acceptance tests: manual lead save appears after refresh; workbook preview shows
row-level reasons before commit; server errors and permission errors are visible.
Risks: UI must not bypass backend validation or authorization.
Evidence: Streamlit script runs headless via AppTest with no exceptions; no browser end-to-end run was performed.
Reviewer: SELF_REVIEW


### M1-T07 - Mentor Lead Workspace API and UI

Status: REVIEW
Requirement/feature IDs: C04, S01, F02
Objective: Provide paginated lead listing and lead detail views with placeholders
for future call information.
In-scope paths: FastAPI list/detail endpoints, Streamlit lead workspace, tests.
Excluded changes: transcript generation, interest assessment, campaign controls,
audio playback.
Acceptance tests: paginated synthetic leads can be searched/filtered; lead detail
shows contact data and empty call state distinctly.
Risks: access rules depend on D12.
Evidence: API list/detail/search/pagination tested (VERIFIED level); Streamlit workspace only smoke-checked.
Reviewer: SELF_REVIEW


### M1-T08 - Backend-Enforced Development Access Baseline

Status: VERIFIED
Requirement/feature IDs: S01, S10, F09, D12
Objective: Establish a safe development-only access model if approved, ensuring
all protected API actions check authorization server-side.
In-scope paths: backend auth/dependency layer, tests, `.env.example`, staff
console session wiring if needed.
Excluded changes: production identity provider selection, real records, public
deployment claims.
Acceptance tests: unauthorized API calls fail; role-limited calls fail; UI
visibility alone is not relied on for access control.
Risks: D12 is open; any dev identity must be clearly non-production.
Evidence: Dev token + role header enforced server-side; fails closed (503) without DEV_AUTH_TOKEN; role-limited calls return 403. NON-PRODUCTION.
Reviewer: SELF_REVIEW


### M1-T09 - Mock Calling Safety Guard

Status: VERIFIED
Requirement/feature IDs: S03, S10; supports later C05/F04/F05
Objective: Add a fail-closed configuration boundary proving M1 cannot dial real
numbers.
In-scope paths: backend configuration, mock adapter interface placeholder, safety
tests.
Excluded changes: real telephony provider, campaign dispatch, provider webhooks.
Acceptance tests: missing live-call approval/config blocks real adapter use;
mock mode is visibly labelled; tests cannot dial real numbers.
Risks: Must remain a safety boundary, not a claimed C05 implementation.
Evidence: calling_guard tests: default mock labelled; LIVE_CALLS_ENABLED=true and non-mock CALLING_MODE raise LiveCallingBlocked.
Reviewer: SELF_REVIEW


### M1-T10 - M1 Evidence and Handoff Updates

Status: REVIEW
Requirement/feature IDs: S12
Objective: Update progress, task status, run commands, and verification evidence
after each approved M1 task.
In-scope paths: `TASKS.md`, `PROGRESS.md`, `HANDOFF.md`, README/run notes.
Excluded changes: changing historical evidence, marking untested work VERIFIED.
Acceptance tests: every completed task has checks listed with results; blockers
are explicit; mock versus live status is clear.
Risks: Documentation must follow evidence, not optimism.
Evidence: Docs updated this cycle; see HANDOFF.md.
Reviewer: SELF_REVIEW

