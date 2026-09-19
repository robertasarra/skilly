# ADVERSARIAL PROJECT INTELLIGENCE — FRAMEWORK

## A. Separation of truth layers

Use separate dimensions for:

### Epistemic state
- VERIFIED
- INFERRED
- HYPOTHETICAL
- UNVERIFIED

### Decision state
- IDEA
- CANDIDATE
- APPROVED
- LOCKED
- DEPRECATED

### Execution state
- PROPOSED
- AUTHORIZED
- EXECUTED
- TESTED
- MERGED
- DEPLOYED
- RUNTIME_VERIFIED
- PERSISTED

These dimensions must not be collapsed into a single vague “status”.

## B. Adversarial review modes

### Lightweight
Use for low-risk reversible work.
Check assumptions, duplication, evidence and scope.

### Standard
Use for substantive project decisions.
Add alternatives, failure modes, authorization, rollback and contradiction review.

### High-risk
Use for actions involving production, money, publication, privacy, credentials, identity routing, destructive changes, legal/commercial commitment or irreversible effects.
Require fail-closed behavior, explicit authority, rollback/kill-switch analysis and evidence before state promotion.

## C. Decision record template

- Context
- Current authoritative state
- User intent
- Constraints
- Evidence
- Unknowns
- Options
- Adversarial findings
- Decision
- Explicit non-decisions
- Authorized execution scope
- Success evidence
- Rollback
- Open loops

## D. State promotion rule

Promotion is monotonic only when evidence supports it.

Examples:
- DOCUMENTED -> IMPLEMENTED requires actual implementation evidence.
- IMPLEMENTED -> TESTED requires test evidence.
- MERGED -> DEPLOYED requires deployment evidence.
- DEPLOYED -> RUNTIME_VERIFIED requires observed runtime evidence.
- RUNTIME_VERIFIED -> EXTERNAL_SYSTEM_VERIFIED requires confirmation from the relevant external system when applicable.

If evidence is lost, stale or contradicted, downgrade the claim instead of preserving an unsupported higher status.

## E. Contradiction classes

- SOURCE_CONFLICT: sources disagree.
- STATE_DRIFT: living docs no longer match observed reality.
- AUTHORITY_CONFLICT: a lower-authority change conflicts with higher authority.
- SCOPE_CONFLICT: implementation exceeds authorization.
- EVIDENCE_CONFLICT: claimed state exceeds observed evidence.
- CONCURRENCY_CONFLICT: parallel work changed the same mutable state.
- TEMPORAL_CONFLICT: old plan conflicts with newer verified actual state.

Never average conflicts. Reconcile or preserve them explicitly.

## F. Learning system

A lesson must be:
- triggered by an observed failure, correction or near miss;
- generalized only as far as evidence supports;
- connected to a concrete future check;
- reviewable for deprecation if context changes.

A useful lesson changes either:
- a preflight question;
- a gate;
- a test;
- a source hierarchy;
- a persistence rule;
- an execution constraint.

## G. Definition of complete

A substantive task is complete only when the claimed completion state matches evidence and all materially affected durable state has either:
- been reconciled; or
- been explicitly marked pending.

Completion is not synonymous with:
- code written;
- a PR opened;
- a merge accepted;
- a deployment initiated;
- a document edited;
- a model producing plausible output.
