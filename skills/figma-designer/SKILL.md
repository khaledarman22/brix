---
name: figma-designer
description: Implement a visual direction, render an identity foundation preview, or make a scoped edit as native editable Figma elements. Use for design execution and targeted fixes with actual visual evidence and a pinned identity when applicable.
---

# Figma Designer

## Inputs and Gates

Read and apply [Figma Design Standards](../figma-design-standards/SKILL.md) for every mode. Follow [the integration contract](../../FIGMA_INTEGRATION.md); do not discover and use an unselected fallback connector.

Read [the shared package contract](../shared-visual-assets/references/package-contract.md). Consume the authorized Visual Direction Package, its exact reference asset versions, requirements, identity, and any scoped validation findings.

Scoped modes avoid circular dependencies:

- **Foundation preview:** accept the identity manager's persisted preview brief, proposed identity revision, and draft direction. Render only the authorized representative foundation/component examples, view them yourself, and return screenshots and exact node/binding mappings to `design-identity-manager`. A proposed identity is permitted for this preview; do not treat it as adopted for final screen execution.
- **Existing-design edit:** accept the persisted scoped change brief from planning instead of a full direction package. Capture and view the relevant current design, register it as a baseline, and pin its asset version. Preserve existing rules except for the explicit requested change. Map results to the change brief, and verify against the baseline plus acceptance criteria. Material direction changes return to planning.

Open the actual original images and relevant crops yourself through an available image-capable tool, or the captured existing-design baseline in scoped-edit mode. Record your own inspections through `shared-visual-assets`; the creative director's inspections are not a substitute. If you cannot see the required images, stop the affected visual implementation and report the blocker.

Discover the host's actual Figma integration and follow its applicable tool instructions. Confirm connection, target file/page, and relevant existing nodes before writing. Do not hardcode plugin names or assume the current file is the correct target. Read existing component, style, and variable data before reuse.

`design-identity-manager` owns identity collection and revisions. Consume its pinned record and open its actual visual examples yourself. Reading node data to implement bindings does not transfer identity ownership to you. Return proposed extensions or conflicts to the manager. For a narrow edit, reuse the current relevant identity or inspected baseline without forcing a whole-project identity audit.

## Execute

For production images/icons, consume the pinned output and placement brief from `design-asset-manager`. Inspect the asset yourself, preserve editable native geometry where appropriate, and place it inside the intended existing parent. Record the actual image asset/version, target node, crop/fit, and implementation revision. Return fresh target captures for in-context review. Missing required final assets or labeled temporary stand-ins cannot count as completed final design. Provide actual target captures when the asset manager needs an image-edit handoff; do not fabricate a placement screenshot.

When adding pages, screens, component families, or retiring content, consume the plan from [figma-file-organization](../figma-file-organization/SKILL.md). Create only destinations receiving real content in the current task. Build the specified Auto Layout content Frames and preserve nested screen dimensions, prototypes, and exports. Return actual page/container/node IDs to the organization record; include board-level captures for organization review as well as individual screen captures. A narrow existing-node edit does not require a new page or a whole-file organization pass.

For new designs, execute parent-first: ready first-content specification → destination page → configured Auto Layout content Frame/group → screen/component attached to its intended parent → visual content built inside it. Do not design on the canvas or a staging page and move the finished result afterward. Verify and record parent IDs before populating content. Only an empty node's immediate attachment during low-level initialization is permitted as described in the organization skill. Populate each created destination before starting another, and never count an empty frame or heading as delivered content.

1. Reconcile current Figma state with the saved implementation mapping. Preserve unrelated work and manual changes. If the direction is stale or conflicts with the actual identity, return the precise conflict for resolution rather than silently redesigning it.
2. Map the direction's sections and decisions to specific frames/components. Use native editable text, frames, components, instances, variables, and styles as supported. Do not use a flattened screenshot as the screen implementation.
3. Reuse confirmed existing components and token bindings. Create new values only from the identity manager's pinned proposal in preview mode or adopted identity for final execution. Return additional identity choices to the manager. If a dependency or binding is missing, record it instead of claiming a successful binding.
4. Apply meaningful Auto Layout, resizing behavior, and constraints for the requested sizes. Implement required states and content direction. A collection of fixed screenshots is not proof of responsive behavior.
5. Execute in small scoped steps. Record intended external mutations through project memory, then save returned node IDs and actual outcomes. After a timeout or uncertain response, inspect live state before retrying to prevent duplicates.
6. Export actual images of implemented frames and relevant states. Open them yourself against the same reference images and direction rules. Fix evident local problems within scope. Foundation previews go to `design-identity-manager` for identity review; final screen implementations and assigned visual repairs go to `visual-fidelity-validation`. A simple scoped edit may close with its planned in-task visual checks; it must not claim an independent validation pass.
7. Save the Implementation Mapping with actual file/page/node IDs, decision mappings, bindings, implemented sizes/states, image assets, and unresolved gaps. Register exports as `figma-export` assets, not original references.

## Repair Work

Preview proposals in isolated frames and separate temporary styles/variables when changing existing values would affect other consumers. Do not edit live shared tokens or main components to test a proposal. After identity adoption, apply only the authorized migration scope, inspect affected instances, and return actual bindings to the manager. Adoption alone does not authorize a project-wide migration.

For validation findings, change the smallest affected scope and preserve intended adaptations. Keep issue IDs and evidence links in the repair handoff. Export fresh images after changes and mark previous validation evidence stale for affected nodes. Do not declare the validator's issues passed without rechecking.

## Completion

Return every changed scope to `figma-structure-validation`, including previews, repairs, and small edits. Save before-state evidence when a change could detach instances or alter shared relationships. A task cannot close without its current structural report and applicable visual checks. Structural and visual repairs share the scope's existing repair budget.

Implementation exists in the confirmed Figma file, native structure and bindings have been inspected, relevant exported visuals have been viewed, and the versioned mapping identifies remaining gaps. Report implementation completion separately from final validation status. Missing tools, inaccessible references, or unverified writes must remain explicit.

In foundation-preview mode, completion means the preview's native nodes, bindings, and viewed screenshots are mapped to the proposed identity and ready for the identity manager's visual review. In scoped-edit mode, completion is measured against the change brief and baseline rather than an absent creative direction package.
