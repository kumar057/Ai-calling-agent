# Coordinator Operating Procedure

## 1. Purpose
This file tells the Antigravity coding agent how to manage the build. It is a
written operating procedure, not executable software and not a mechanism that
starts agents by itself. The primary Antigravity session is the coordinator.
Use native subagents only when the installed surface actually exposes them.

## 2. Authority and state
Read AGENTS.md and all required business files first. Latest explicit owner
instructions override earlier project proposals; retain a decision history.
Do not infer approval from an empty decision row, a generated plan, an uploaded
Excel sheet, an assistant suggestion, or a broad “build the app” instruction.

Track requirement approval separately from implementation status:
NOT_STARTED -> READY -> IN_PROGRESS -> REVIEW -> VERIFIED.
BLOCKED is a visible state with reason and dependency, not disguised progress.
A feature is VERIFIED only when all required acceptance checks have evidence.

## 3. Work roles
| Role | Responsibility | Required output |
| --- | --- | --- |
| Coordinator/business analyst | Understand business flow, resolve scope, sequence work | Requirement mapping, approved plan, task assignment |
| Architect | Translate an approved feature into data/API/service boundaries | Small design note and trade-offs |
| Builder | Implement one assigned, bounded change | Code diff, tests, setup/doc changes |
| Reviewer | Check behavior, security, failures and evidence | PASS / CHANGES_REQUIRED / BLOCKED with findings |
| Operator/release reviewer | Check real integration, quotas, runbooks and rollback | Release checklist and evidence |

These are responsibilities, not a requirement for five paid agents. One agent may
perform them as separate passes. Independent review must be labelled as such only
when a different agent/human actually reviewed the work.

## 4. Session start
1. Inspect the workspace tree, existing instructions, Git status, dependencies,
   application entry points, tests, and available tools without modifying code.
2. Record whether this is Antigravity IDE, 2.0, or CLI and which customizations
   are actually discovered. Never invent installed capabilities.
3. Reconcile implementation with PROGRESS.md; inspect evidence before trusting it.
4. Explain the end-to-end business flow in plain language and distinguish
   confirmed requirements, safeguards, proposed enhancements and open choices.
5. Select one dependency-ready task within the owner's current authorization.

For the first session use the project-onboarding skill and produce an inspection
report plus an implementation plan. Stop for scope/plan approval before code.
Do not repeat questions whose answers already exist in the project files.

## 5. Task assignment contract
Every task must identify:
- Task ID and related requirement/feature IDs.
- Objective and expected user-visible behavior.
- Required input files and approved decisions.
- In-scope paths and explicitly excluded changes.
- Dependencies, risks, and permitted tools/environment.
- Acceptance tests and expected evidence.
- Owner and reviewer; deadline only if the human actually supplied one.

Do not ask a worker simply to “build the backend.” Give it the exact interface,
validation behavior, tests and file ownership for the current slice.

## 6. Implementation loop
A. PLAN: inspect relevant code and contracts, state the small change and test plan.
B. IMPLEMENT: edit only scoped files; preserve unrelated changes and interfaces.
C. VERIFY: run relevant tests plus regression checks; inspect actual UI behavior
   when UI work is involved. Use synthetic data and mock calls unless authorized.
D. REVIEW: compare the diff against requirements, failures, permissions, and scale.
E. FIX: address specific findings; rerun affected checks. Stop a fruitless loop
   after three failed repair cycles and record the blocker/evidence.
F. RECORD: update tasks, tests/evidence, progress, decisions if approved, and handoff.
G. CONTINUE: take the next ready task only within the approved milestone/scope.

Missing provider credentials block real integrations, not unrelated local work.
Finish interfaces and tests with labelled adapters; keep the real integration
BLOCKED. Do not silently select a database/provider or claim a mock is complete.

## 7. Optional native agent coordination
The pack provides `.agents/agents/admissions-builder.md` and
`.agents/agents/admissions-reviewer.md` for Antigravity 2.0/CLI surfaces documented
in SOURCES.md. Ordinary AGENTS.md plus skills is the baseline for the IDE.

Before invocation verify discovery and tool-name compatibility. The parent passes
the complete task contract and source file paths because a new subagent does not
inherit the whole parent conversation. Prefer one builder plus one reviewer.
The reviewer profile is intentionally read-only; the coordinator runs tests and
shares logs, and a human/independent runner can rerun them when required.

For parallel work use disjoint paths or isolated Git worktrees. Do not assign two
writers the same file or let multiple workers modify shared TASKS/PROGRESS at once.
The coordinator alone merges work and updates shared progress. Check integration
tests after merging; independent unit tests do not prove compatibility.

Without native subagents, perform sequential roles in the primary session and
record reviewer_type=SELF_REVIEW. Do not pretend an agent was spawned.

## 8. Review rubric
Review business correctness, API/data consistency, error recovery, authorization,
privacy, prompt injection, call-state handling, test quality and operational risk.
Report each as PASS / FAIL / NOT_TESTED with evidence. An optional 1-5 maturity
rating must have a reason and is not proof of scalability. A serious access bug,
duplicate-dial path, untested real call, fabricated fee, or lost transcript blocks
release regardless of an average score.

## 9. Approval boundaries
Routine local edits/tests within approved scope may continue. Stop for a decision
when changing the agreed stack, choosing paid services, enabling real calling,
using production data, making destructive changes, publishing externally,
raising spend limits, adding unapproved features, or changing contact/interest policy.
Use targeted questions only for the current blocking decision; do not repeatedly
ask the owner the entire question list.

## 10. Final report for every work cycle
Report: task; what changed; business outcome; exact checks and results; reviewer
and verdict; remaining blockers; mock versus live status; next dependency-ready
task. Record this in PROGRESS.md/HANDOFF.md as well as the conversation.
Stop claiming progress when tools cannot verify it. Do not mark a release complete
just because the code compiles or the interface looks finished.
