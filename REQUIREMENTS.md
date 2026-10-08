# Requirements and Acceptance Criteria

## Status and authority
C = confirmed by the current user request. S = proposed engineering/launch
safeguard; include in the plan and obtain scope review, and do not enable live
calling before required safety controls exist. E = proposed enhancement, not
implicitly in scope. D = unresolved decision in DECISIONS.md. Implementation
status is tracked separately in TASKS.md/PROGRESS.md, initially NOT_STARTED.

## Confirmed functional requirements

### C01 — Excel lead intake
Authorized staff can upload an Excel sheet containing many student/customer
records. Recommended initial format is .xlsx; other Excel formats need explicit
scope. Provide a column mapping and validation preview before committing data.
Acceptance: a synthetic workbook imports its valid rows, reports invalid rows
with row number and reason, and reconciles the uploaded count to every outcome.
The application must not report success while silently dropping rows. The exact
required business fields are decided in D10; phone number is necessary to dial.

### C02 — Individual entry
Staff can add one lead through a form. Acceptance: the saved lead appears in the
mentor list after a refresh and uses the same validation rules as bulk intake.

### C03 — Database persistence
Persist leads and their associated conversation/results through the application.
Acceptance: restart UI/API processes and verify saved records remain retrievable
from the selected database. A Python list, browser state, CSV-only store, or a
mock repository does not satisfy production persistence. Database choice is D02.

### C04 — Mentor visibility
Mentors can view leads and inspect related call information. Acceptance: open a
lead and see its contact details, attempts, transcript(s), and latest reviewable
interest result. Proposed filters include name/phone, course, outcome, interest,
and assigned mentor. API results must be paginated for thousands of records.

### C05 — Automatic outbound calling
The application calls stored leads through a real telephone integration, under
the approved initiation/scheduling policy. Acceptance: a permitted test recipient
receives a call initiated by a worker, the provider IDs are correlated, and the
final call state is saved. Upload-triggered versus mentor-started calling is D05.
Do not implement a browser voice demo and label C05 complete.

### C06 — Institution and course explanations
The agent explains the institution, offered courses, fees, online/offline modes,
learning process, mentor application, and relevant online product using approved
information. Acceptance: approved test questions produce supported answers;
missing or expired information produces an honest uncertainty/escalation response.
The agent may explain relevant details conversationally rather than reading all
institution information at the beginning of every call.

### C07 — Two-way conversation
Students can ask questions and express interest, objections, confusion, or a
wish to stop. Acceptance: a voice pilot covers turn-taking, an interruption,
clarification, silence, and a student ending the call. Required languages and
code-switching behavior must be selected and tested under D07.

### C08 — Both-speaker transcripts
Save the student's recognized speech and the AI's delivered responses, linked
to the lead and call. Acceptance: speaker labels, ordered turns, timestamps,
and available final text are retrievable. Handle partial turns, duplicate events,
late finalization, disconnects, and transcription failures. Record completeness
and quality; never reconstruct missing speech as though it was observed. Distinguish
AI text generated from text actually played when the provider supports that signal.
Audio recordings are not required by C08; they remain a separate decision D09.

### C09 — Interest identification
After a conversation, assess interest and display an interested/not-interested
result where supported. Acceptance: explicit interest and explicit rejection are
recognized in representative dialogues; the evidence can be inspected. Proposed
states also include UNCLEAR and NOT_ASSESSED to avoid false binary labels.
Generic keywords may identify topics, but must not alone decide intent. D08
requires approval of the classification rubric and evaluation threshold.

### C10 — Daily calling volume
Design and validate for at least 1,000 calls/day, with the counted unit resolved
under D01. Acceptance: an approved load profile and eligible pilot/production
run show the required unit and report retries, unique leads, connection rates,
concurrency, duration, errors, and costs separately. Local simulation proves
software behavior only, not carrier quotas or 1,000 answered conversations.

## Proposed launch safeguards

### S01 — Identity and access
Use authenticated staff sessions and server-side role/scope checks before real
student data is accessible. Restrict imports, viewing transcripts, content
approval, campaign execution, overrides, exports, and settings by approved role.
Acceptance: an unauthorized API caller cannot access or mutate those resources.
Hiding a Streamlit button is not authorization. Identity integration is D12.

### S02 — Safe, repeatable intake
Validate headers/types, normalize phone numbers with explicit country context,
limit file size/row count, reject unsupported/macro content, and never execute
formulas. Detect duplicates within a file and existing records. Proposed policy:
flag duplicates for review; never silently overwrite known facts or reactivate
suppressed numbers. Re-uploading the same commit operation is idempotent.
Shared family numbers and cross-campaign duplicates need an approved policy.

### S03 — Contact eligibility and suppression
Store source and contact permission evidence/status independently from interest.
Unknown eligibility must block real calling until checked. Enforce opt-out,
wrong-number suppression, allowed destinations, and approved calling windows
immediately before dialling, not only when a campaign was created. Re-imports
must not erase suppression. A callback request is not automatically broad
marketing consent. India/provider-specific review is a live-release gate.

### S04 — Campaign controls and limits
Provide start, pause, resume, and a dispatch kill switch; emergency termination
of active calls is a separate controlled action. Enforce approved attempts/day,
per-contact retries, pacing, concurrent-session limits, call duration, and budget.
Pause prevents new attempts; define what happens to existing conversations.
Acceptance: competing workers and campaigns cannot exceed the configured limits.
Do not invent legal calling hours or configure all-day promotional dialing.

### S05 — Durable work and ambiguous dispatch
Keep call jobs/attempts in durable storage. Claim work atomically; use unique
attempt identities, leases, idempotency keys where supported, and reconciliation.
At-least-once job delivery must not cause duplicate dial operations. A timeout
after submitting a provider request may mean the call exists: mark UNKNOWN and
reconcile provider state before retrying. Do not claim universal exactly-once
phone calls across an external provider. See ARCHITECTURE.md.

### S06 — Reliable call lifecycle
Persist distinct attempt state, outcome, interest, contact preference, and next
action. Verify webhook authenticity using the selected provider's actual scheme;
deduplicate and process out-of-order events. Retain terminal history; late events
must not reopen an ended call. Reconcile missing events and stop orphaned calls.
Voicemail, no answer, busy, failed, and wrong party must not become student interest.

### S07 — Approved knowledge and bounded tools
Only designated staff approve current course/fee/product content. Version it and
record what version was used by a call. The agent must not invent discounts,
refund terms, schedule availability, certificates, or placement guarantees.
Expose narrow validated tools, not arbitrary SQL, a shell, or unrestricted HTTP.
Caller/transcript instructions cannot change developer rules, fees, permissions,
or reveal another student's information. Knowledge ownership is D11.

### S08 — Evidence-based, reviewable assessment
Separate topic extraction, student intent, contact preference, and next action.
Use transcript turn references and a short reason. Maintain model/prompt/rubric
versions. Missing/poor-quality evidence routes to UNCLEAR or NOT_ASSESSED.
Confidence is optional and must not be presented as a calibrated probability
without evaluation. Mentor corrections include editor/time/reason; AI re-runs
must not overwrite a protected human decision or newer transcript version.

### S09 — Privacy, disclosure, and retention
Use an owner-approved AI introduction and any applicable recording/transcription
notice. Retain only approved fields for approved periods, with access logs,
protected storage/transport, and a deletion/export process. Define what metadata
is retained for suppression when content is deleted. Do not assume recording
consent and permission to place a promotional call are the same. D09/D13 apply.
This document does not certify compliance with any jurisdiction.

### S10 — Safe development versus live execution
Development/test uses synthetic leads and a mock telephony adapter by default.
Live calls require approved providers, an authorized environment, eligible
recipients, explicitly allowed test numbers for a pilot, and a spending cap.
Acceptance: missing configuration fails closed; a test or load command cannot
accidentally dial a real recipient. Mock results are visibly labelled.

### S11 — Monitoring and recovery
Track lead/import/campaign/attempt/provider IDs without exposing PII in ordinary
logs. Alert on dispatch stalls, increasing failures, transcript/assessment backlogs,
call cleanup failure, and budget limits. Store reconciliation and retry errors.
Acceptance: an operator diagnoses a failed attempt and performs a documented
restore/recovery drill. Monitor backend and voice-worker health separately.

### S12 — Quality and deployment evidence
Document tested dependencies, migrations, backup/restore, secure configuration,
rollback, run commands, and test evidence. Use automated checks plus reviewed
end-to-end pilot evidence. Any quality or performance target is proposed until
approved. Never replace failing assertions with passing mocks to mark a task done.

## Proposed enhancements — do not implement by default
| ID | Candidate | Reason it is not yet committed |
| --- | --- | --- |
| E01 | Automatic mentor assignment and follow-up tasks | Exact workflow unanswered |
| E02 | Audio recording and playback | Transcript requirement does not imply audio storage |
| E03 | Live transfer/demo/calendar booking | Needs provider support and business availability |
| E04 | Multiple institution tenants and SaaS billing | Initial institution scope unanswered |
| E05 | WhatsApp/SMS/email brochures and notifications | Channels and contact permissions not selected |
| E06 | Inbound calls or public browser voice widget | Current requirement is outbound calling |

## Requirement changes
For any scope change, record the owner's instruction, affected IDs, data/API/test
impact, approval, and effective date in DECISIONS.md. Update dependent features
and tasks; do not overwrite historical implementation evidence.
