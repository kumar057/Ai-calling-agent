# Features and User Experience

All features start NOT_STARTED. This is an implementation proposal mapped to the
confirmed business flow. C requirements are required; S safeguards and optional
E scope are labelled in REQUIREMENTS.md. The proposed first UI is a staff-facing
Streamlit application, with FastAPI responsible for all business operations.

| Feature | What the person can do | Requirement mapping | Proposed milestone |
| --- | --- | --- | --- |
| F01 Lead intake | Upload .xlsx, map columns, preview issues, commit valid rows, or add one record | C01-C03, S01-S03 | M1 |
| F02 Lead workspace | Search/filter/paginate leads and open an individual record | C04, S01 | M1 |
| F03 Institution knowledge | Review and approve current course, fee, learning and product information | C06, S07 | M2 |
| F04 Campaign controls | Select eligible leads, inspect policy, start/pause approved calling | C05, S03-S06 | M2 mock; M4 real |
| F05 Calling service | Make and end real calls, handle conversation and failures | C05-C07, S04-S07, S10 | M3-M4 |
| F06 Call history | View call outcomes, timestamps, duration and both-speaker transcripts | C04, C08, S06, S09 | M2; M4 real |
| F07 Interest review | See evidence-based interest and correct it with an audit trail | C09, S08 | M2; M4 real |
| F08 Operations overview | Track attempts, connections, errors, backlogs, volume and cost | C10, S04, S11 | M4-M5 |
| F09 Staff administration | Apply approved access, contact policies and secure settings | S01, S03, S09-S12 | M1 baseline; M5 full |

## F01 — Intake journey
Upload -> choose sheet/columns -> validate -> show row outcomes -> confirm import
-> save once -> show report and lead-list link. A proposed report groups rows into
created, duplicate/review, invalid, and skipped with counts that reconcile. Do not
invent missing phone numbers or treat a blank permission field as granted.
Manual entry reuses backend validators. A committed import is recoverable after
refresh; duplicate clicks do not duplicate leads. Initial format proposal is
.xlsx; CSV, .xls, and exports require explicit support rather than silent acceptance.

## F02 — Mentor lead workspace
Proposed columns: name, masked contact where appropriate, source, course interest,
latest call outcome, latest interest, contact permission/suppression, and next
action when available. Provide a lead detail view with call history and evidence.
Empty, loading, no-results, validation, permission-denied, and server-error states
must be distinguishable. Data access is scoped in FastAPI.

## F03 — Institution knowledge
Proposed structured content: institution introduction, course names/descriptions,
fees and currency, learning modes, timing information when approved, mentor
support, online product usage, admission steps, and answers to common questions.
Draft -> approved -> archived version lifecycle. The live agent cannot use drafts
or fill missing content from general model knowledge. Synthetic course names and
fees used in tests must be unmistakably demo data.

## F04 — Campaign controls
Show eligibility counts and excluded reasons before any start operation. Display
recipient list scope, time window/timezone, retry rules, active-call cap, daily
attempt cap, budget, approved knowledge version, and test/live mode. Starting
must be authenticated, authorized and idempotent. Pausing blocks dispatch of new
attempts; already connected calls follow the selected graceful-stop policy.
Automatic scheduling remains possible after this control policy is approved.

## F05 — Conversation capability
The AI introduces itself and the institution using approved wording, confirms
whether the person can talk, understands their course needs, answers relevant
questions, and checks interest without pressure. It handles an interruption,
silence, background noise, uncertainty, a callback request and opt-out. It must
not ask for payment credentials or claim a human mentor has accepted a booking
unless a verified tool result confirms it. End the provider call, not only the
voice-agent process, and verify cleanup.

## F06/F07 — Lead result view
Show these independently: call outcome; transcript availability/quality; interest;
reason and supporting turns; questions/topics; course discussed; requested next
action; human review state; and contact suppression. The interest badge is not a
replacement for the transcript. No answer -> not assessed, not “not interested.”
A mentor can correct the latest effective assessment without deleting the AI
version. Audio controls are absent unless E02/D09 is approved and implemented.

## F08 — Dashboard
Count actual attempts separately from answered calls, unique leads, meaningful
conversations, and assessed conversations. Display the time range, timezone,
and metric definitions. Show provider-reported versus estimated cost separately.
Show queue, transcript and assessment backlogs rather than “completed” merely
because a call ended. Never multiply a mock benchmark into a production claim.

## F09 — Administration
Implement only the approved identity/role system. A private synthetic-data demo
may use a clearly isolated development identity, but it must not be deployable
with real records without authentication/authorization. Keep provider secrets
server-side and out of UI debug output. Configuration changes and content
approvals are auditable.

## Not screens to build yet
Student learning application, payment page, institution subscription checkout,
WhatsApp inbox, calendar scheduling, and public inbound call portal are outside
this initial feature map. Refer to E01-E06 for proposed additions.
