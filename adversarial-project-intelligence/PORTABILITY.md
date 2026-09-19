# ADVERSARIAL PROJECT INTELLIGENCE — PORTABILITY

## Goal

Make the method reusable in other ChatGPT Projects, Work-style environments, repositories and agent systems without coupling it to Luca Moretti.

## Package model

Portable core:
- SKILL.md
- FRAMEWORK.md
- CASEBOOK.md
- REGRESSION_TESTS.md

Per-project adapter:
- source hierarchy;
- authoritative file map;
- domain-specific locks;
- authorization roles;
- persistence targets;
- domain skills to compose;
- effectful-action boundaries;
- project-specific state vocabulary if needed.

## Adapter template

```
PROJECT: <name>
AUTHORITATIVE_ROOT: <repository/workspace/source>
SOURCE_HIERARCHY:
  1. ...
LOCKS:
  - ...
DOMAIN_SKILLS:
  - ...
PERSISTENCE_TARGETS:
  decisions: ...
  lessons: ...
  state: ...
  evidence: ...
CRITICAL_EFFECTS:
  - ...
HUMAN_AUTHORITY:
  - ...
CLOSE_GATE:
  - ...
```

## ChatGPT Project use

Store the portable core in a central repository or shared knowledge location. Each project carries only its adapter and references the core.

Do not copy project-specific history into every project.

## Work / agent use

At task start:
1. load portable core;
2. load project adapter;
3. inspect current authoritative state;
4. choose review mode: lightweight, standard or high-risk;
5. execute the operating loop;
6. persist lessons and project truth in the adapter-defined targets.

## Versioning

Use semantic-style skill versions:
- PATCH: wording/clarity, no behavior change;
- MINOR: new lesson, gate or regression test;
- MAJOR: state model, authority model or core workflow changes.

Every behavior-changing release should cite its triggering case(s).

## Migration rule

When adopting this skill in an existing project:
1. do not rewrite history;
2. inventory current truth sources;
3. identify duplicated or conflicting authorities;
4. map existing states to the skill model;
5. import only generalized lessons into the core;
6. keep project-specific lessons in the adapter unless demonstrated to be universal.
