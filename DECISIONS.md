# Decisions

All entries are OPEN unless the owner explicitly approves them later. Recommended
defaults are proposals, not implementation approval.

## D01 - Call Volume Count Definition

Status: OPEN

Question: What counts toward the 1,000 calls/day target: dial attempts, connected
conversations, or unique leads reached?

Options:
- Attempts/day: easiest to measure and load-test, but does not prove people
  answered.
- Connected conversations/day: closer to business value, but depends on recipient
  answer rates and provider classification quality.
- Unique leads/day: avoids retry inflation, but needs separate attempt metrics.

Recommended default proposal: Use attempts/day for software capacity validation
in M5, while reporting connected conversations and unique leads separately. Do
not treat attempts as enrollment or interest.

## D02 - Database Choice

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Which database should provide production persistence?

Options:
- SQLite for local M1 development only: simple, low setup, weaker for concurrent
  production workers.
- Postgres for production: stronger concurrency and operational fit, requires
  setup and ownership.
- Abstraction compatible with SQLite locally and Postgres later: flexible, but
  must be approved before implementation.

Decision: SQLite for local development behind a database abstraction that stays Postgres-compatible. No production database claim yet.

## D03 - Launch Institution and Tenant Scope

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Is version one restricted to 10000Coders or intended for multiple
independent institutions?

Options:
- Single institution: simpler roles, content, reporting, and release controls.
- Multi-institution SaaS: broader product, but requires isolation, billing, tenant
  administration, and stronger operational proof.

Decision: Single institution (10000Coders context). No multi-tenant work.

## D04 - Telephony Provider

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Which provider, if any, should be used for real outbound telephone
calls?

Options:
- Mock adapter: safe default for development and tests, no real calls.
- India-focused telephony provider: may fit local calling workflows better, but
  needs current provider review, contracts, compliance checks, and credentials.
- Global programmable voice provider: mature APIs may help integration, but cost,
  local rules, availability, and phone-number requirements need review.

Decision: Mock telephony and deterministic mock conversation only. Do not select any telephony provider.

## D05 - Calling Initiation and Scheduling Policy

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Should calls start after upload, by mentor/operator action, or by an
approved campaign schedule?

Options:
- Upload-triggered: fast automation, higher risk of accidental dialing.
- Manual mentor/operator start: clearer control, less automation.
- Approved campaign schedule: best fit for safeguards, pacing, and eligibility.

Decision: Upload alone must never trigger calls.

## D06 - LLM, Speech, and Voice Provider Choice

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Which model, transcription, text-to-speech, and voice-runtime services
should be used with LiveKit later?

Options:
- Mock text conversation in M2: safe and testable, no live speech proof.
- Approved model/speech provider for M3: enables voice sandbox, may create paid
  usage and data handling obligations.

Decision: Mock telephony and deterministic mock conversation only. Do not select any LLM or speech provider.

## D07 - Languages and Code-Switching

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Which languages are approved for the calling experience, and how should
code-switching be handled?

Options:
- English only initially.
- English and Telugu after explicit approval and test coverage.

Decision: English only for M1/M2.

## D08 - Interest Classification Rubric and Threshold

Status: OPEN

Question: What evidence makes a lead interested, not interested, unclear, or not
assessed?

Options:
- Simple rubric from representative transcript examples: transparent and easy to
  test, less nuanced.
- Model-assisted classification with versioned rubric: more flexible, requires
  evaluation and guardrails.

Recommended default proposal: Use states INTERESTED, NOT_INTERESTED, UNCLEAR,
and NOT_ASSESSED with evidence references. No binary label without supporting
turns.

## D09 - Recording, Transcription Notice, and Audio Storage

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Are calls recorded, what notice is given, and is audio retained?

Options:
- Transcript only: satisfies confirmed transcript need without audio playback.
- Audio recording and playback: useful for review, but optional enhancement with
  consent, storage, access, and retention implications.

Decision: Transcripts and metadata only. No audio recording.

## D10 - Required Lead Fields and Validation Rules

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: Which fields are required for manual and Excel intake?

Known requirement: phone number is necessary to dial.

Decision: Approved for M1 synthetic data. Required lead fields: name (or display label), phone number, source, contact-permission status. Optional: course interest. A blank permission value is NOT treated as granted. Default country context for phone normalization: India (+91), explicit and configurable.

## D11 - Institution Knowledge Ownership and Approval

Status: OPEN

Question: Who owns and approves course, fee, product, mentor, timing, and learning
process content?

Options:
- Administrator approval workflow.
- Named owner/staff approval outside the app initially.

Recommended default proposal: Treat institution knowledge as versioned approved
content. The agent may use only approved versions, never drafts or general model
knowledge for fees, discounts, certificates, schedules, refunds, or placement
claims.

## D12 - Identity and Access Integration

Status: APPROVED (Approved by owner instruction on 2026-10-08)

Question: What authentication and role system should protect staff/admin/operator
actions?

Options:
- Development-only synthetic identity: useful for isolated demos, not deployable
  with real data.
- Approved identity provider or internal account system: required before real
  data and live calling.

Decision: Approved for M1 synthetic data only. Backend-enforced development roles (admin, mentor, uploader, operator), clearly labelled non-production, never deployable with real records.

## D13 - Retention, Deletion, Export, and Suppression Metadata

Status: OPEN

Question: How long are leads, transcripts, assessments, access logs, and
suppression metadata retained, and what deletion/export process is required?

Options:
- Short pilot retention for synthetic/test data.
- Owner-approved production retention schedule with deletion/export process.

Recommended default proposal: Keep synthetic/test data local for development.
Before real data, approve retention periods, deletion/export behavior, and the
minimal metadata retained for suppression after content deletion.
