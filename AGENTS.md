# Agent Operating Notes

Source: COORDINATOR.md, adapted for this Codex workspace. Ignore Antigravity-only
subagent, profile, and skill references unless the current tool surface actually
provides them.

## Scope Discipline

- Work one milestone and one small task at a time in order: M0 -> M5.
- Track statuses separately from requirements: NOT_STARTED, READY, IN_PROGRESS,
  REVIEW, VERIFIED, BLOCKED.
- VERIFIED requires passing evidence from the relevant tests/checks.
- Do not infer owner approval from generated plans, empty decision rows, uploaded
  files, or broad build requests.

## Role Passes

When no independent reviewer is used, perform these passes sequentially:

1. Analyst: reconcile business flow, scope, and open decisions.
2. Architect: define boundaries, trade-offs, and data/API/service ownership.
3. Builder: implement only the approved bounded task.
4. Reviewer: review behavior, security, failure handling, and evidence.

Self-review must be labelled reviewer_type=SELF_REVIEW.

## Approval Boundaries

Stop for owner approval before:

- choosing paid database, LLM, telephony, or related providers;
- changing the fixed stack;
- enabling real calling;
- using real student data;
- making destructive changes;
- publishing externally;
- raising spend limits;
- adding unapproved features;
- changing contact, consent, language, or interest policy.

Ask only the specific blocking question.

## Safety Defaults

- Use synthetic data and mock telephony by default.
- Real calling must fail closed unless explicitly enabled in an authorized
  environment with approved recipients and limits.
- Enforce security and state rules in backend/worker code, not in prompts or UI
  visibility alone.
- Never print, store, or commit secrets. Use `.env.example` only.
