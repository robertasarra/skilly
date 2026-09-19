# CHATGPT / WORK DISTRIBUTION — ADVERSARIAL PROJECT INTELLIGENCE

Status: READY FOR MANUAL/NATIVE SKILL IMPORT
Date verified: 2026-09-19
Canonical package: `adversarial-project-intelligence/`

## What is ready now

The folder `adversarial-project-intelligence/` is the canonical upload/source package. It contains:
- `SKILL.md` with valid skill frontmatter;
- framework;
- casebook;
- regression tests;
- portability guidance;
- adapter template;
- version/source provenance.

## ChatGPT Skills

For eligible ChatGPT workspaces, Skills are created or uploaded from the Skills surface under Plugins. The upload flow scans the skill before it becomes available.

Recommended distribution flow:
1. package the complete `adversarial-project-intelligence/` folder as a ZIP with that folder at the ZIP root;
2. in ChatGPT, open Plugins -> Skills;
3. choose Create -> Upload from your computer;
4. review the skill scan/result;
5. install it;
6. share/publish it to the workspace when workspace permissions allow;
7. keep this repository as the canonical upstream for future releases.

## ChatGPT Work / workspace agents

When the surface supports Skills, attach/install this skill and then provide only the project adapter or project files needed for the task. Do not copy project-specific Canon or business state into the portable core.

Suggested execution order:
1. load portable Adversarial Project Intelligence;
2. load the project adapter;
3. inspect authoritative current state;
4. select lightweight / standard / high-risk review mode;
5. execute domain work;
6. verify evidence/state promotion;
7. persist lessons and project truth in project-defined targets.

## Plugin packaging path

If the skill is later distributed as a ChatGPT Plugin, keep this directory as the skill payload and wrap it with plugin metadata rather than rewriting the core. Plugins may package skills with apps/tools; the portable core should remain tool-agnostic.

## Source-of-truth rule

- Canonical upstream: `robertasarra/skilly/adversarial-project-intelligence/`
- Project adapters: live in each consuming project.
- Vendored copies: fallback only.
- Universal behavior changes: upstream first, version there, then deliberately re-vendor.
- Platform installation is not evidence that every consuming project is synchronized; project adapters remain versioned independently.

## Current limitation

Repository preparation does not itself install the skill into a user's ChatGPT account or workspace. Native installation requires the eligible ChatGPT Skills UI/workspace permission and an explicit user/admin installation action.
