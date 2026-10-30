---
name: figma-design-standards
description: Mandatory implementation standards for any Figma design creation or edit, covering layout, reusable components, variants, shared tokens, styles, naming, and editability. Apply within the changed scope and verify through structural and visual evidence.
---

# Figma Design Standards

Standards version: `2`. Apply [Brix](../../AGENT.md) inspection/documentation policies. These are criteria for the changed scope and direct dependencies, not extra phases or runtime enforcement. Identity owns values; the director owns composition; the designer writes nodes.

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

## Exceptions and acceptance

Assess only applicable rules. Record justified exceptions once with rule, scope, reason, evidence, tradeoff and authority. Routine justified choices need no new approval. Exceptions cannot hide unavailable checks, waive real visual evidence or silently change adopted identity.

Evaluate structure and [visual release criteria](references/visual-release-checks.md) within the same shared before/after passes. Store both outcomes in one canonical record, with separate fields rather than mandatory separate reports. Each required applicable check needs actual evidence or a legitimate exception. Reuse current available results across roles and adoption. Missing evidence is unverified; observed failure needs scoped repair. Neither structural nor visual pass alone substitutes for the other.
