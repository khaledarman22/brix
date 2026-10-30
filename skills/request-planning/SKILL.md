---
name: request-planning
description: Scope Brix design tasks, requirements, dependencies and acceptance criteria without executing design or duplicating research stages.
---

# Request Planning

Follow [Brix](../../AGENT.md). Restore existing task state first; do not invoke this skill for ordinary questions or skill authoring.

## Minimal plan

Extract the requested outcome, exact changed scope, target platform/file, constraints, existing identity and usable evidence. Ask only for essential unresolved inputs. Preserve task IDs and completed work when feedback changes scope.

Use one authoritative plan in project state or the existing task system. Each task needs ID, scope, owner/skill, input links, dependencies, deliverable, acceptance criteria and readiness. Use `ready`, `waiting-on-dependency`, `needs-input`, `missing-skill`, `needs-connection`, or `needs-capability`; execution status belongs to project memory. Do not create a duplicate brief/plan file or repeat linked requirements.

- Simple edit: one scoped change task with baseline, preserve constraints and shared before/after verification; no research unless explicitly requested.
- New design/research: one `reference-research-selection` task with coverage for every new screen, followed by application to design. Block only uncovered screens. Research-only work stops at selection.
- Existing identity: consume its authoritative record and available relevant inspection; no whole-product audit for a small change.
- New/extended identity: director's draft → scoped identity proposal → actual designer preview → adoption from shared after-pass evidence → final application. These are dependencies inside application, not repeated research or review pipelines. Preview may use proposed values; final implementation uses adopted values. Avoid a preview/adoption circular dependency.
- Organization/assets: add responsibilities only for actual destinations or required assets. Placement followed by an edit is distinct from initial placement; do not create a dependency cycle. Product photos are not UI references.

## Decisions and acceptance

Own one confirmed locale/direction and form-state record. For each needed state declare fields, constraints and their source, sample synthetic values, messages and expected button/loading behavior. References guide appearance, not backend rules. Ask for missing product language; do not infer it from a wordmark. An in-scope visual-policy proposal must be labeled before implementation and must not be presented as working backend behavior.

Assign who resolves visual/structural findings using the same inspection pass. Coverage includes only changed elements and direct dependencies, with relevant sizes/states. A shared-component edit may affect instances; preserve unaffected valid checks. Do not schedule a fresh pass merely for adoption or a role handoff.

Feedback updates only affected dependencies. A reference rejection invalidates its specified use; explicit alternative-reference requests reopen only that research scope. Preserve budgets, canonical links and authorizations. Mark missing capabilities honestly rather than inventing skills or expanding scope.
