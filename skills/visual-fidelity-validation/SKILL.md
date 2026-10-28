---
name: visual-fidelity-validation
description: Visually compare actual Figma outputs with pinned reference images, direction rules, and project identity, consume the separate structural report, and route scoped repairs. Use after implementation or fixes; does not require pixel-identical copying.
---

# Visual Fidelity Validation

## Contract

Read [the shared package contract](../shared-visual-assets/references/package-contract.md). Input: pinned Visual Direction Package, Implementation Mapping, original reference images, project identity, and current Figma outputs. Output: a versioned validation report with actual evidence, issues, and `pass`, `needs-fixes`, or `blocked` status.

For a scoped existing-design edit, accept the persisted change brief, inspected pre-change baseline, and implementation mapping instead of a creative direction package and external references. Validate the requested change and preservation constraints against actual before/after visuals. Structural checks are required where relevant to the changed scope; mark unrelated checks `not applicable` with a reason, not `not reviewed`. Never turn a scoped edit into a full-page redesign audit.

For reference-led final implementation, pin the same adopted identity revision used by the designer. Open the identity manager's actual visual examples alongside current output and source references. A matching token name or binding is not a visual pass. Report visible identity deviations with both evidence references. Implementation mistakes return to the designer; disputed rules or identity changes return to `design-identity-manager` through the orchestrator. Never change the identity to make a failing output pass. The manager's earlier foundation review does not replace final screen validation.

## Review

For organization-only work, use the scoped organization/change brief and before/after captures instead of requiring a new creative direction or external references. Open actual content-container/board captures to review group arrangement, clipping, overlap, labels, and preservation of screen proportions, plus detailed screen/component images where needed. For new screen boards apply these same checks alongside normal fidelity review. Leave creation-order claims to the structural validator's operation evidence; final appearance cannot establish how nodes were created.

`figma-structure-validation` owns FDS compliance and structural evidence. Consume its current report; do not duplicate its rule ledger or treat its pass as visual proof. You own actual appearance, responsive visual behavior, and fidelity findings. Use the same selected adapter.

1. Confirm the intended Figma file and current nodes. Export fresh screenshots for the required frames, sizes, and states; record their origin and register them through `shared-visual-assets`.
2. Open those screenshots and the same original reference versions yourself. Open identity visuals where relevant. Neither an implementation summary nor an export path proves that comparison occurred. Record your own actual inspections.
3. Compare full-page composition and relevant details: layout, alignment, spacing, typography, hierarchy, color treatment, and component relationships. Tie each finding to a visible region, direction rule, and reference evidence.
4. Check identity against the actual project tokens/components and visible identity examples. Respect documented deliberate changes. The target is faithful visual intent adapted to the project, not 100% pixel equality with a reference.
5. Review requested responsive sizes through actual rendered previews and view them. Obtain Auto Layout, constraints, sizing, and binding results from the structural validator's live-data report. Use read-only preview controls when available. If checks require changing nodes or creating copies, request those scoped preview mutations from `figma-designer` through the orchestrator, then view the returned result. The validator does not mutate design nodes. Screenshots alone do not prove Auto Layout.
6. Review states and interactions only when actually demonstrated within authorized scope. Mark unavailable sizes, states, images, or structural data `not reviewed`; do not infer behavior or pass a required unchecked criterion.

## Findings and Repairs

If a visible issue requires an image change, record the exact target, actual screenshot, asset version, visible problem, and desired outcome. Route source selection/edit-prompt preparation to `design-asset-manager` through the orchestrator, then placement to the designer. Reopen the fresh in-context output before resolving the finding. An isolated improved image does not close a placement issue. Use the same scope repair counter rather than creating an extra image-edit allowance.

Record each issue with a stable ID, severity, exact node/region, expected rule, observed mismatch, output/reference evidence, and a targeted correction. Distinguish intentional deviations from mistakes. Do not report invented similarity percentages or claim a computational metric was run when it was not.

Return scoped fixes to `figma-designer` through the orchestrator. The validator does not independently redesign the direction. After fixes, capture and inspect fresh outputs; review affected areas and relevant dependencies rather than restarting unrelated research.

Share one repair counter with structural validation for this implementation scope; do not allocate three rounds to each validator. Follow the user's repair limit. Otherwise allow up to three repair-and-review rounds for the same scope, preserving the cumulative count across sessions. A recurring issue may be retried only with a concrete changed correction and remaining rounds; stop when there is no meaningful corrective progress, the limit is reached, or necessary evidence remains inaccessible. Material scope changes return to planning instead of silently resetting the loop. Never lower the standard to claim completion.

## Completion

Save the report and evidence references, update project memory through the orchestrator, and state coverage precisely. `pass` requires all required criteria to have been checked with no unresolved required fixes. `needs-fixes` identifies observed deviations. `blocked` identifies missing evidence or capability. Optional unreviewed items stay visible even when required checks pass.

A visual `pass` describes only this report. Overall task completion also requires a current structural pass; missing structural evidence cannot be hidden by visual success.
