# PROJECT ADAPTER TEMPLATE

PROJECT: <name>
UPSTREAM_SKILL: robertasarra/skilly/adversarial-project-intelligence
UPSTREAM_VERSION: <version or commit>

## Authoritative root
<repository/workspace/source>

## Source hierarchy
1. explicit current human instruction;
2. locked/non-negotiable rules;
3. approved authoritative decisions;
4. verified actual state/evidence;
5. living documentation;
6. approved strategy/specification;
7. planned work;
8. suggestions.

## Locks
- <project-specific locks>

## Domain skills
- <skills that compose with the portable core>

## Persistence targets
- decisions: <path/system>
- lessons: <path/system>
- state: <path/system>
- evidence: <path/system>

## Critical effects
- <deploy/publication/spend/privacy/etc>

## Human authority
- <roles and boundaries>

## Close gate
- <project-specific completion/persistence gate>

## Fallback rule
If the upstream source cannot be loaded, use the last vendored local copy and report its upstream version/commit. Do not silently merge divergent local edits into the portable core.
