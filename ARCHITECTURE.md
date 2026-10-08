# Architecture Notes

Source: CONTEXT.md, REQUIREMENTS.md, FEATURES.md, and END_GOAL.md.

## Known Boundaries

- Streamlit is the staff console.
- FastAPI is the trusted backend for validation, state, authorization, and
  business rules.
- A future voice worker is distinct from the staff console and from Antigravity
  or Codex.
- LiveKit is planned for a later voice milestone.
- Telephony, model, and database providers are open decisions.

## Required State Principles

- Persist leads, imports, attempts, transcripts, assessments, and review evidence
  in durable storage once a database is approved.
- Keep call attempt state, call outcome, interest, contact preference, and next
  action distinct.
- Use durable call jobs/attempts, atomic claiming, unique attempt identities,
  leases, idempotency keys where supported, and reconciliation.
- Unknown dispatch state after a provider timeout must be reconciled before retry.
- Late provider events must not reopen terminal calls.

## Security Principles

- Enforce permissions in backend and worker code, not only by hiding Streamlit UI.
- Unknown contact eligibility blocks real calling.
- Re-imports must not erase suppression.
- Transcript or caller instructions cannot change developer rules, fees,
  permissions, or reveal other student information.

## Current Implementation Status

No application source has been found in this workspace yet. These notes are
architecture constraints for future M1-M5 implementation.
