# ADVERSARIAL PROJECT INTELLIGENCE — CASEBOOK

This casebook distills reusable lessons from the Luca Moretti / Squad House project without carrying Luca-specific Canon into the portable skill.

## CASE-001 — Technical milestone recorded locally but project state remained stale

Situation:
A real technical milestone was recorded in domain evidence, while project summary, diary, handoff or status artifacts were not reconciled in the same cycle.

Failure:
“Persisted” was treated as equivalent to “one relevant file was updated”.

General rule:
A material state change requires an impact sweep across the authoritative living set. Persistence is complete only when affected artifacts are classified UPDATED, NOT_IMPACTED or PENDING.

Regression test:
Given a material state transition, the agent must identify every living artifact that could now be stale and cannot claim complete persistence while any materially affected one remains unclassified.

## CASE-002 — Existing architecture risked being duplicated

Situation:
A new structure was considered before fully inspecting the repository.

Failure:
Parallel architecture could have created competing truth layers and long-term drift.

General rule:
Inspect authoritative structure before adding new architecture. Prefer extending an existing owner over creating a parallel subsystem.

Regression test:
Before creating a new top-level architecture/domain, the agent must demonstrate that no existing owner already covers the responsibility.

## CASE-003 — Test double mistaken for provider evidence

Situation:
Deterministic mocks/test doubles validated orchestration.

Risk:
Passing synthetic tests could be described as proof of external provider behavior.

General rule:
Synthetic evidence proves only the controlled layer it exercises. It cannot prove transport, authorization, provider semantics or production behavior.

Regression test:
Any conclusion based on mocks must explicitly state the boundary and must not use EXTERNAL_SYSTEM_VERIFIED or PRODUCTION_E2E.

## CASE-004 — Ambiguous external publish outcome

Situation:
An effectful external publish could succeed while its response was lost.

Risk:
Blind retry could duplicate publication; blind failure classification could record a false failure.

General rule:
When an effectful external outcome is ambiguous, reconcile external state before retrying or assigning a terminal verdict. Introduce an explicit UNCONFIRMED state when truth is not held.

Regression test:
Simulate a lost response after external acceptance. The system must neither republish blindly nor record a definitive failure without reconciliation.

## CASE-005 — Concurrent idempotency race

Situation:
Two requests attempted the same unique idempotent operation concurrently.

Risk:
The loser surfaced as an internal error even though a valid winner already existed.

General rule:
Concurrency-sensitive idempotency must converge on the winning durable record and preserve conflict behavior for genuinely different payloads.

Regression test:
Race two equivalent requests; exactly one durable operation may exist and both callers must converge on it. Race with conflicting payloads; the conflict must remain visible.

## CASE-006 — Brainstorming versus authority

Situation:
Creative and architectural exploration generated plausible future decisions.

Risk:
An idea could silently become Canon, approved state or implementation truth.

General rule:
Idea generation and authority promotion are separate workflows. Persistence of an idea does not promote it.

Regression test:
Persist a candidate. Verify that its authority remains CANDIDATE unless an explicit promotion event occurs.

## CASE-007 — Generated depiction mistaken for real-world fact

Situation:
AI-generated visuals contained plausible brands, objects or details.

Risk:
Plausibility could be mistaken for real existence, exact model identification or verified partnership.

General rule:
Generated depiction is evidence only of generated content, never of external-world fact.

Regression test:
Any exact real-world claim derived only from generated media must be blocked or downgraded to UNVERIFIED.

## CASE-008 — Camera/operator continuity exposed hidden physical inconsistency

Situation:
A scene was visually plausible in isolation but impossible given who was supposed to hold the camera.

General rule:
For any system involving physical or operational actors, model the operator and state transitions, not only the visible outcome.

Portable interpretation:
Always ask who/what performs the action, where that actor/system is before and after, and whether the transition is physically or operationally possible.

Regression test:
A proposed sequence with an impossible operator transition must fail the consistency gate.

## CASE-009 — “GREEN” before the appropriate evidence rung

Situation:
A lower-level gate passed while higher-level runtime or provider evidence was still absent.

General rule:
GREEN is local to a named gate. Never generalize a lower-layer PASS into end-to-end completion.

Regression test:
If CI passes but runtime is unobserved, final status must not say production verified.

## CASE-010 — Correction without durable learning

Situation:
An error was corrected in conversation or implementation but no reusable prevention mechanism was created.

Risk:
The same class of failure can recur.

General rule:
Material corrections must produce at least one of: new rule, preflight check, test, gate, source-hierarchy update or persistence requirement.

Regression test:
For every material postmortem record, verify that a future behavior-changing control exists.


## CASE-011 — PR metadata claimed more than the diff proved

Situation:
A PR body/checklist described controls as implemented before the exact diff/head/test evidence existed.

General rule:
Metadata is intent/evidence indexing, not proof. Claims must be reconciled against concrete artifacts.

Regression test:
Every implementation/validation claim in delivery metadata must map to an actual path/diff/test or be downgraded.

## CASE-012 — Exact validated head changed after GREEN

Situation:
A branch received additional writes after the head used for CI/review had been validated.

Risk:
The evidence no longer described the candidate being merged.

General rule:
Validation attaches to an exact immutable candidate. New writes require revalidation.

Regression test:
If head SHA changes after validation, previous exact-head approval cannot authorize merge of the new head.

## CASE-013 — Mock or adapter looked operational

Situation:
A sandbox, adapter or compatibility layer had labels/names that could be interpreted as real integration capability.

General rule:
Simulation state must be explicit. Existence, naming and local tests never promote a substitute into real operational capability.

Regression test:
A mock/stub/sandbox must remain non-operational and non-authoritative until replaced and externally evidenced.

## CASE-014 — Compatibility preserved shape but changed meaning

Situation:
A field/API kept the same surface while its historical value or semantics changed.

General rule:
Compatibility includes name, type, semantics and materially relied-upon values.

Regression test:
A compatibility claim must test old caller behavior, not only schema shape.

## CASE-015 — Optional signal could override stronger authority

Situation:
Caller-provided scores/facts/flags could alter a decision without explicit authority/provenance.

General rule:
Decision-changing optional inputs require provenance and authority; source precedence must be explicit.

Regression test:
An unauthorized optional signal cannot disable or override a hard gate derived from stronger current evidence.

## CASE-016 — Vacuous “all complete” on empty collection

Situation:
A universal predicate returned true for an empty credentials/requirements set.

General rule:
Completeness predicates require minimum cardinality before checking “all”.

Regression test:
Empty required collections must fail completeness unless emptiness is explicitly valid by contract.
