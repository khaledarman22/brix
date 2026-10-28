---
name: figma-structure-validation
description: Verify actual Figma node structure against mandatory design standards after creation or changes. Read layout, component, variable, style, resizing, and naming evidence; return scoped issues without modifying the design.
---

# Figma Structure Validation

## Inputs

Read [Figma Design Standards](../figma-design-standards/SKILL.md) and [the package contract](../shared-visual-assets/references/package-contract.md). Consume the changed-node mapping, pinned identity, task scope, required states/sizes, before-state evidence, and declared exceptions. Use only the selected integration documented under [the integration contract](../../FIGMA_INTEGRATION.md).

This skill defines a verification procedure. It is not a programmed validator or an installed write interceptor. Do not claim automated enforcement or validation until the corresponding tools actually run.

## Procedure

1. Confirm the selected integration, target file, current affected nodes, and implementation/preview revision. If integration is unselected or cannot read required structure, record `blocked`; do not use another connector silently.
2. Read live node data for the changed scope and relevant dependencies. Check FDS-01 through FDS-14 using actual layout settings, node types, component links and sets, properties, variable bindings/resolved modes, style IDs/overrides, constraints, resizing configuration, and hierarchy as applicable. Use the integration's real schema; do not invent fields.
3. Verify reusable-component choices against the inspected library and required behavior. Flag a missing reuse search if relevant; do not infer that a new component is necessary merely because none was reported.
4. For potential detach or relationship loss, compare recorded before-state with current nodes and confirmed mutation results. If historical evidence is missing, mark that historical check unreviewed rather than declaring no detach occurred. Current node-type checks remain possible.
5. Assess each declared exception against the standard and actual evidence. Report the rule's outcome as `pass`, `fail`, `not-applicable`, `not-reviewed`, or `exception-accepted`, with a reason. Required unreviewed checks prevent overall pass. Contextual component/variable decisions require explained judgment, not a blind count.
6. Return node-specific corrections to the designer through the orchestrator. Read again after repair. You do not mutate nodes, normalize the file, redefine identity values, or accept screenshots as proof of structural fields.

## Report

For FDS-13, inspect the organization plan and confirmed page/container mappings: created destinations must contain real content; primary scoped containers must be Auto Layout Frames; screen dimensions, component-set types, and existing relationships must remain correct. Check before/after prototype links and export targets when nesting changes them. Verify archived items have recovery records and no unresolved active dependencies. Visual layout quality still requires viewed captures; node data alone cannot clear clipping or composition issues.

An empty screen frame, page title, or collection of empty groups does not satisfy FDS-13. Check actual requested descendants against the first-content specification. For FDS-14, examine actual ordered creation/attachment and population evidence, including parent IDs or a supported nested creation request and confirmed result. Final hierarchy or a screenshot cannot prove that content was built there. Missing operation evidence is `not-reviewed` for this required historical check, not a pass. Distinguish authorized moves of pre-existing nodes from prohibited build-then-move for new designs.

Save `design/validation/<task-id>-structure.md` with project/file identity, task ID, standards version `2`, pinned implementation or preview mapping revision (or organization/change record for organization-only work), identity revision when applicable, examined node IDs, capture/read time, actual tool evidence references or bounded field excerpts, rule outcomes, exceptions, and coverage gaps.

Each issue includes stable ID, FDS rule ID, affected nodes, expected structure, actual observed values, severity, corrective action, and status (`open`, `fixed-awaiting-review`, `resolved`, or `blocked`). Resolve only after actual reinspection. Preserve consumed report revisions using the shared package contract.

Overall status is `pass`, `needs-fixes`, or `blocked`; record freshness separately. Use `blocked` when required evidence cannot be acquired, even if observed failures also exist. `pass` means all required checks passed or have legitimate accepted exceptions, not that visual quality passed.

## Handoff and Repair Limits

Return the report to the orchestrator and relevant visual reviewer. A foundation preview's structural result is required before identity adoption; final task completion needs both required reports on the same current implementation. Visual review may proceed while a structural issue is being diagnosed, but cannot close the combined task.

Coordinate with visual validation under one repair budget per implementation scope, defaulting to three repair-and-review rounds unless the user sets another limit. Do not multiply the budget by assigning a separate allowance to each validator. Identity previews use their existing identity-preview repair budget. Recheck affected rules and dependencies after mutation; preserve unrelated valid results with explicit revision reconciliation.
