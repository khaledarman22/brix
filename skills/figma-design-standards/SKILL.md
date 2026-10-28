---
name: figma-design-standards
description: Mandatory implementation standards for any Figma design creation or edit, covering layout, reusable components, variants, shared tokens, styles, naming, and editability. Apply within the changed scope and verify through structural and visual evidence.
---

# Figma Design Standards

Standards version: `2`.

## Application

Every role creating or changing Figma design nodes must read and apply these standards, including foundation previews, repairs, migrations, and scoped edits. This is a shared rule set, not an additional design phase or permission to modify unrelated work. `figma-designer` implements; `figma-structure-validation` verifies the actual structure; visual reviewers inspect rendered results.

The identity manager owns identity values and reusable treatment rules. The director owns composition. Do not resolve an implementation limitation by silently changing the adopted identity.

## Rules

| ID | Standard | Applicability and evidence |
| --- | --- | --- |
| FDS-01 | Use Auto Layout by default for content frames, sections, and components. | Inspect actual layout configuration. Absolute placement is for justified overlays, decoration, or equivalent spatial requirements; record why and verify resize behavior. A free-positioned canvas is not itself a failure. |
| FDS-02 | Use components for reusable elements. | Inspect actual component/instance types and relationships. Identify reuse by role and behavior, not merely repeated geometry. Do not turn every shape or one-off section into a component. |
| FDS-03 | Model required component states as coherent variants where appropriate. | Inspect component sets, variant properties, and required state coverage. Do not invent Hover for interfaces that do not need it or generate all possible combinations unnecessarily. |
| FDS-04 | Bind shared or centrally adjustable values to variables where supported. | Read actual bindings and resolved values/modes. One-off values may remain literal. Unsupported bindings are disclosed; do not claim that every property can bind on every integration. |
| FDS-05 | Follow the pinned identity's semantic token system. | Check relevant colors, typography, spacing, sizes, corners, and other shared rules against the authoritative identity. No independent conflicting token catalog. |
| FDS-06 | Reuse text and effect styles when they express shared identity treatments. | Read style references and relevant overrides. Do not require meaningless styles for unique treatments or detach a shared style without justification. |
| FDS-07 | Expose appropriate component properties. | Use Text, Boolean, and Instance Swap properties where consumers need those controls. Inspect definitions and instance behavior; properties are not required when they add no useful flexibility. |
| FDS-08 | Configure resizing and constraints deliberately. | Inspect applicable Hug, Fill, fixed dimensions, min/max behavior, and constraints in context. Verify the actual appearance at required sizes; field names alone do not prove responsiveness. |
| FDS-09 | Search the relevant existing component library before creating another component. | Record inspected candidates and reuse decision. Reuse suitable instances; explain why a genuinely new component is needed. Missing access is not proof that no component exists. |
| FDS-10 | Use meaningful names and logical hierarchy. | Follow the project's existing conventions, group by responsibility, and avoid accidental wrapper depth or generic names on meaningful changed elements. Do not rename unrelated nodes. |
| FDS-11 | Preserve instance relationships. | No unnecessary detach. Record any required detach before execution with target, reason, and affected consumers. Compare before/after evidence; a final standalone frame alone cannot prove how it was created. |
| FDS-12 | Deliver native, editable structure and verified results. | Inspect node types, relationships, and bindings, then view actual exported results. A flattened screenshot or arbitrary pile of positioned shapes is not a valid substitute for an editable interface. |
| FDS-13 | Organize only actual content with clear pages and Auto Layout content Frames. | Follow `figma-file-organization`. Confirm nonempty created destinations, meaningful product/role names, actual Frame layout settings, nested screen integrity, and recoverable authorized Trash moves. Do not apply Frame layout properties to a Page or reorganize unrelated legacy pages. |
| FDS-14 | Build new designs in their intended parents from the outset. | Verify creation/attachment order and parent IDs before content population. No completed design built outside then moved into a wrapper. Empty-node API initialization may attach immediately before design; scoped moves of existing content are separate operations. Final hierarchy alone cannot prove creation order. |

## Applicability and Exceptions

Assess each rule within the requested change and its affected dependencies. Distinguish `not-applicable` from `not-reviewed`. Do not expand a label edit into an unsolicited whole-file refactor.

An exception records rule ID, node/scope, reason, evidence, tradeoff, and authority from the user's request or established project constraints. Routine justified implementation choices do not require fresh user approval. Exceptions cannot invent evidence, hide an unsupported required check, waive actual visual review, or contradict an explicit user requirement. A missing tool capability is a blocker or unreviewed item, not an exception that passes.

The designer proposes exceptions; the structural validator checks their applicability and the visual reviewer checks visible consequences. Identity-changing exceptions return to the identity manager. Record accepted exceptions visibly in the final report.

## Completion Gate

Every mutation task needs a current scoped structural report from `figma-structure-validation` and the applicable visual review. Foundation previews require the identity manager's visual review; final screens require assigned fidelity validation; simple edits may retain planned in-task visual checks. The same agent may execute roles sequentially; do not claim independent review in that case.

Structural pass requires actual supported evidence for every required applicable check, with justified exceptions documented. Visual pass never substitutes for structural pass and vice versa. Automated interception and integration-specific enforcement remain deferred under [the integration contract](../../FIGMA_INTEGRATION.md).
