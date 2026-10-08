# End Goal and Definition of Done

## Business destination
Deliver a working institution-side application that turns uploaded student leads
into real outbound educational enquiry conversations, preserves both sides of
each conversation, and gives mentors reviewable interest information.

## Observable complete journey
An authorized staff member imports an Excel file or adds a lead manually, sees
validated records saved in the database, and selects the approved automatic
calling process. An eligible student receives a real telephone call. The agent
uses approved institution information to answer questions about courses, fees,
learning modes, mentor support, and the online product. Afterwards, a mentor
opens the lead, reads the conversation and its quality status, sees the interest
assessment and supporting evidence, and handles the approved next action.

The user-stated target is at least 1,000 calls/day. Production acceptance must
resolve D01 in DECISIONS.md and demonstrate the corresponding metric; a script
that merely inserts 1,000 fake call rows does not meet it.

## Delivery stages — proposed ordering
| Stage | Working outcome | What it does NOT prove |
| --- | --- | --- |
| M0: Understand and approve | Repository audit, reconciled scope, approved implementation plan | No app completion |
| M1: Lead foundation | Streamlit -> FastAPI -> selected database; Excel/manual records persist | No real phone calls |
| M2: Conversation simulation | Approved knowledge, sample dialogues, transcripts, assessment and review | No speech or telephony quality |
| M3: Voice sandbox | LiveKit-based voice path tested with approved model access | No telephone carrier integration |
| M4: Telephone pilot | Approved test-number calls, correct cleanup, transcript and result end to end | No 1,000/day capacity claim |
| M5: Controlled production | Security, operations, eligible campaign runs, capacity evidence, owner sign-off | No guarantee all prospects answer or enroll |

Build these stages as connected parts of the final system, not throwaway demos
that hide missing database or phone integrations. A browser/console voice test is
an intermediate verification tool; public student browser calling is not required.

## Release gates
- Confirmed requirements C01-C10 map to implemented features and passing tests.
- Launch safeguards S01-S12 are reviewed and satisfied before real campaigns.
- The business owner approves institution facts, language scope, calling policy,
  recipient eligibility, external services, and the count definition for scale.
- State and security rules are enforced by backend/worker code, not only prompts.
- Transcript ingestion supports partial/incomplete calls without invented text.
- Interest is independent from no-answer/busy/failed call outcomes; “unclear”
  or “not assessed” remains available when evidence is insufficient.
- Mentor overrides remain auditable and are not overwritten by stale AI jobs.
- Provider errors, retries, duplicate events, and worker restarts are tested.
- Budget and emergency-stop controls work, with separate pilot and production
  authorization. Real calling remains disabled in development and test.
- An operator can deploy the approved services, check health, restore data,
  diagnose a failed call, pause dispatch, and follow the rollback runbook.
- Repository setup commands, tests, dependency versions, and evidence are current.

## Proposed measurable checks, not promised service levels
Use a 1,000-row synthetic import with deliberate invalid/duplicate rows and
reconcile every row to an outcome. Replay 1,000 simulated attempts with duplicate
webhooks and worker interruption. Separately run permissioned telephone tests.
Measure daily attempts, answered calls, unique leads, complete transcripts,
assessment completion, unresolved reviews, provider errors, latency, and cost.
The owner must approve any performance/quality threshold before it becomes a
production acceptance contract; no fabricated “99.9% accuracy” requirement.

## Explicit exclusions until approved
Inbound calling, WhatsApp/SMS/email automation, payment collection, enrollment
checkout, full LMS rebuilding, marketing lead scraping, cloning a person's
voice, automatic discounts, job/placement guarantees, public student accounts,
live human transfer, and multi-institution subscription billing.

## Honesty at handover
Report each component as NOT_STARTED, IN_PROGRESS, BLOCKED, REVIEW, or VERIFIED.
A local test is not a production test. A mock provider is not a live integration.
This documentation pack itself is not an implementation or a deployment.
