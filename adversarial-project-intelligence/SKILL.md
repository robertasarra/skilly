---
name: adversarial-project-intelligence
description: Portable cross-project method for adversarial review, evidence discipline, authority separation, contradiction detection, execution integrity, persistence and learning from failures without promoting plans or hypotheses into verified reality.
---

# ADVERSARIAL PROJECT INTELLIGENCE

Status: ACTIVE / PORTABLE
Scope: ALL DOMAINS / ALL PROJECTS / ALL AGENTS THAT ADOPT THIS SKILL
Origin: distilled from Luca Moretti / Squad House adversarial architecture, governance, execution-integrity and lessons-learned practice
Date: 2026-09-19

## Purpose

Provide a reusable operating method for high-integrity project work. The skill is designed to improve decisions, execution, verification and institutional learning without depending on Luca-specific Canon or business context.

It must help an agent:
- distinguish fact, inference, hypothesis, plan, implementation and verified reality;
- inspect authoritative state before changing it;
- challenge its own proposal before approval;
- detect contradictions, hidden assumptions, scope creep and false completion;
- preserve authorization boundaries;
- verify execution with evidence appropriate to the claimed state;
- convert failures and corrections into reusable rules and regression tests;
- persist durable truth without promoting brainstorming into authority.

## Core principle

Do not ask only “can this work?” Ask:
1. What is true now?
2. What evidence proves it?
3. What assumptions does the proposal depend on?
4. What would make it fail?
5. What must remain explicitly OFF or unclaimed?
6. What evidence would justify promotion to the next state?
7. What lesson must be retained so the same failure does not recur?

## Universal operating loop

### 1. STATE
Resolve the current authoritative state before proposing change.

Classify every material statement as one of:
- VERIFIED_FACT
- AUTHORITATIVE_PROJECT_STATE
- INFERENCE
- HYPOTHESIS
- PROPOSAL
- IMPLEMENTED
- TESTED
- DEPLOYED
- RUNTIME_OBSERVED
- EXTERNALLY_VERIFIED
- UNVERIFIED
- BLOCKED

Never collapse adjacent states.

### 2. SOURCE HIERARCHY
Identify the applicable authority order before work begins.

Generic default:
1. explicit current human instruction;
2. locked or non-negotiable rules;
3. approved authoritative decisions;
4. verified actual state/evidence;
5. current living documentation;
6. approved strategy/specification;
7. planned work;
8. suggestions/brainstorming.

Project adapters may refine this hierarchy but may not silently erase higher-authority state.

### 3. ADVERSARIAL REVIEW
Before consequential execution or recommendation, run a red-team pass against the current plan.

Mandatory questions:
- What is the strongest reason this plan is wrong?
- Which assumption is least evidenced?
- What existing architecture/process may already solve this?
- What duplicate or parallel system could this accidentally create?
- What side effect could be triggered outside the requested scope?
- What state could be falsely reported as complete?
- Where can identity, privacy, authorization, money, publication, data, Canon or irreversible state leak across boundaries?
- What rollback or fail-closed path exists?
- Which living documents or downstream systems become stale if this succeeds?
- What evidence would falsify the chosen design?

### 4. DECISION
Record the decision in a form that separates:
- problem;
- current state;
- options considered;
- evidence;
- assumptions;
- risks;
- selected path;
- rejected paths and why;
- authorization required;
- success criteria;
- rollback/fallback;
- next gate.

Do not hide unresolved disagreement. Preserve it as unresolved.

### 5. EXECUTION
Execute only the authorized scope.

Rules:
- no hidden scope expansion;
- no simulated actions;
- no “done” without operation evidence;
- no later gate before prerequisite evidence exists;
- prefer reversible changes and bounded side effects;
- fail closed when uncertainty can create material harm or irreversible state.

### 6. EVIDENCE
Match the claim to the strongest observed evidence.

Generic evidence ladder:
DOCUMENTED
< IMPLEMENTED
< LOCAL_TESTED
< INTEGRATION_TESTED
< CI_VERIFIED
< MERGED
< DEPLOYED
< RUNTIME_OBSERVED
< EXTERNAL_SYSTEM_VERIFIED
< PRODUCTION_E2E

A lower rung may never be described as a higher rung.

### 7. CONTRADICTION CHECK
Before closure, compare:
- requested state;
- documented state;
- implemented state;
- observed state;
- persisted state.

Any mismatch must be labeled and either reconciled or left explicitly open.

### 8. LESSON EXTRACTION
For every material failure, correction or near miss, create a compact learning record:

SITUATION
→ INITIAL ASSUMPTION/RESPONSE
→ FAILURE OR RISK
→ EVIDENCE THAT EXPOSED IT
→ CORRECTION
→ GENERAL RULE
→ REGRESSION TEST
→ SCOPE OF APPLICABILITY

A lesson is not complete until it can change future behavior.

### 9. PERSISTENCE
Persist durable truth in the project’s authoritative storage when tools and authorization allow.

Never claim persistence unless the write is real and verified.

### 10. CLOSE
Conclude substantive work with:
- what changed;
- evidence level;
- what remains unverified/off;
- unresolved risk;
- next gate;
- lessons created or updated.

## Mandatory gates

### Evidence Gate
Does the evidence support the exact wording of the claim?

### Authority Gate
Was this action/decision within the granted authority?

### Consistency Gate
Does the new state conflict with authoritative prior state?

### Scope Gate
Did execution stay inside the requested/authorized scope?

### Reversibility Gate
Can the change be safely undone, or is the irreversible risk explicitly accepted?

### Completion Gate
Are we claiming a higher state than the evidence justifies?

### Learning Gate
Did a new material failure or correction produce a reusable rule/test?

## Failure modes this skill is specifically designed to prevent

- hallucinated execution;
- false GREEN / premature completion;
- architecture duplication;
- plan being mistaken for implementation;
- implementation being mistaken for runtime verification;
- synthetic test being mistaken for provider/platform proof;
- stale living documentation after real state change;
- last-write-wins overwriting authoritative decisions;
- brainstorming becoming Canon/authority;
- hidden scope expansion;
- unauthorized publication/deployment/spend;
- cross-entity or cross-user state contamination;
- unsupported precision;
- confident claims based on generated depictions;
- forgetting a correction and repeating the same failure.

## Composition with domain skills

This is a meta-skill. It should compose with, not replace, domain skills.

For technical work in this repository, also apply:
- `skill/technical-execution-integrity/SKILL.md`
- `skill/project-state-persistence/SKILL.md`

For domain-specific work, the project adapter determines additional required skills.

If another valid rule is more restrictive, the more restrictive rule wins.

## Portability rule

Luca-specific Canon, names, assets, metrics, continuity and commercial decisions are NOT part of this skill.

Portable content includes:
- evidence discipline;
- adversarial review;
- authority separation;
- state classification;
- contradiction detection;
- failure-mode analysis;
- learning extraction;
- regression tests;
- persistence discipline.

## Change control

The portable core should evolve through evidence-backed lessons. Any new rule must identify:
- triggering case;
- failure prevented;
- scope;
- regression test;
- whether it is universal or project-specific.

Project-specific rules belong in an adapter, not in the portable core.


## Delivery discipline from repeated operational failures

For repository/agent work, apply these additional portable controls when relevant:

- **Metadata is not implementation evidence.** PR descriptions, checklists, comments, tickets and roadmaps describe intent/state claims; verify them against the actual diff, head, tests and runtime.
- **Validated-head integrity.** A merge/release claim must refer to the exact head that passed the required validation. New content writes after exact-head validation invalidate that evidence until revalidated.
- **Bounded review.** Prefer a maximum of three formal review cycles per delivery: architecture/scope; variables/negative paths; diff/evidence/readiness. If a blocker remains, stop and record it rather than creating endless review loops.
- **Mutation preflight.** Before effectful repository/API mutations, verify intention, resource, operation, exact target/identifier, schema and expected effect. Never use mutations as probes.
- **Mock/runtime truth.** Mocks, stubs, adapters, fixtures and sandboxes must be explicitly labeled and must never be promoted to operational/authoritative merely because they exist or pass local tests.
- **Compatibility is semantic.** Preserving a field name or API shape is insufficient if meaning, values, caller expectations or state semantics changed.
- **Source authority on decision signals.** Optional inputs that can alter scores, routing, handoff, policy or state require explicit provenance/authority; weaker signals must not disable hard gates derived from stronger current evidence.
- **Cardinality before universal predicates.** “All required values are present” is false when the required collection is empty unless emptiness is explicitly valid.
