# Project Context

Version: 1.0 | Prepared: 8 October 2026 | Owner: Naveen
Status: business brief plus explicitly labelled implementation proposals.
This pack contains specifications and coding-agent instructions, not a built app.

## 1. Business and problem
We are building an AI admissions calling and lead-qualification application for
educational institutions that offer online courses, offline courses, or both.
The institution receives thousands of prospective-student/customer records.
Its staff should not have to repeat the same introductory course and fee
conversation manually for every lead.

10000Coders is the owner's relevant institution context. Whether version one is
restricted to that institution or sold to multiple independent institutions is
not decided. Do not build multi-tenant billing or claim multi-institution
isolation has been validated before that scope is approved.

## 2. Confirmed current business request
- Staff, mentors, or another authorized institution-side user upload Excel
  sheets or enter student/customer records individually.
- The application saves the collected records in its database.
- Mentors can view the stored leads and their subsequent calling information.
- The AI automatically makes outbound calls to those leads under the approved
  calling policy.
- It explains the institution, offered courses, fee structure, online/offline
  learning, mentor application, online product, and the learning process.
- It listens and answers the student's questions rather than delivering only
  an uninterrupted prerecorded message.
- It stores what the student said and what the AI said as a call transcript.
- It evaluates the conversation and shows whether the student is interested.
- The target is at least 1,000 calls per day. The meaning of a counted call
  (attempt, answered conversation, or unique student) remains unresolved.

The current request adds persistence, outbound calling, scale, and transcripts
to the earlier course-enquiry classroom outline. Those current explicit needs
supersede earlier exercise-only statements such as “no database today.” They do
not authorize paid production actions or make unselected providers approved.

## 3. People and permissions
| Person | Business need | Decision status |
| --- | --- | --- |
| Product owner | Approve requirements, budget, providers, and releases | Owner role known |
| Institution administrator | Manage institution content and authorized staff | Proposed role |
| Mentor/admissions staff | View leads, transcripts, interest, and follow-up needs | Viewing confirmed; editing rights proposed |
| Data uploader | Add leads manually and through Excel | Confirmed capability; exact role assignment open |
| Student/prospect | Receive relevant information and express questions/preferences | Confirmed |
| Operator | Monitor campaigns, failures, limits, and emergency pause | Proposed role |

A person may hold more than one role. Exact access rules require approval.
Students need no login merely to answer an outbound telephone call.

## 4. Business flow
Lead source -> Excel/manual intake -> validate and preview -> save leads ->
mentor lead list -> approved campaign/eligibility checks -> durable call queue ->
telephone conversation -> transcript -> evidence-based interest assessment ->
mentor review and the approved follow-up action.

Validation, approval, queuing, permission checks, and human correction are
recommended implementation safeguards, not additional promises already made
by the owner. They are specified separately in REQUIREMENTS.md.

## 5. Technology context to preserve
Earlier project notes explicitly chose Python Streamlit for the interface and
Python FastAPI for the backend. LiveKit was planned for voice, with integration
details still open. Database, model provider, and telephone provider were not
selected. See TECHNOLOGY.md and the user-context sources in SOURCES.md.

Streamlit is the staff console, not the telephone network. FastAPI is the trusted
application backend. The production voice worker is distinct from Antigravity.

## 6. Terms that must stay distinct
- Lead: a prospective student/customer record, not necessarily an enrolled student.
- Campaign: an approved selection of leads and calling rules; proposed UI concept.
- Call attempt: one actual dial operation; retries are separate attempts.
- Connected conversation: a call where the intended kind of recipient answered;
  provider “answered” events alone may also include voicemail/IVR.
- Transcript: machine-produced text of each side of a call. It may contain
  recognition errors or missing portions and must display quality limitations.
- Interest: an evidence-based assessment, not a guarantee of admission or payment.
- Follow-up: the next action requested or approved; separate from interest.
- Suppression: a contact must not be dialled under the applicable policy.

## 7. Open boundaries
The owner has not yet selected the launch institution model, exact languages,
call windows, automatic-start trigger, provider, recording policy, budget,
retention period, or precise interest threshold. Telugu and English are relevant
candidate languages from the surrounding project context, not a signed-off
multilingual requirement. Do not add Hindi or any other language by assumption.

No repository has been inspected for this pack. Existing implementation status,
installed Antigravity surface/version, credentials, and deployment access are
unknown. Audit these before changing code; do not echo secret values.

## 8. Product principle
A mentor should be able to open a student record and understand: what happened,
what was discussed, whether interest was expressed, the evidence behind that
assessment, and what action is needed next. Never substitute a decorative
interest badge for actual conversation evidence.
