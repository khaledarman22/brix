---
name: reference-apply
description: Interpret the user's chosen reference regions or comments and adapt them to the existing Figma product identity. Apply Brix's recorded project-fit selection or an explicit user choice, preserving existing identity and scope.
---
# Apply selected regions in the existing identity

Use [the shared store](../reference-search/references/store-contract.md). Resolve the selected reference version, board and intended destination from saved state and the user's current request. Reuse previous choices and applied mappings; do not restart research or create another board.

Read [project composition](references/project-composition.md) for composed-screen work. Start from the saved language and screen function; reference selection is optional when no visual gap remains. Use references as supporting evidence, not a new style per screen.

## Interpret selection

If no applicable explicit user choice exists and the project language has a concrete gap, use reference-evaluate to choose suitable inspected regions and record `selected_by: "brix"`, rationale and source/version locally, then proceed. Do not ask a routine A/B question. Respect a user-requested selection pause. The rules below for quotes and annotations apply to actual user selections, not autonomous decisions.

Accept natural-language choices, reference letters/IDs, explicit crop selections, or user-created annotations. When the user says they have selected something in Figma, read actual current selection/annotations through supported tools. Do not treat a node ID or cursor highlight without expressed intent as approval. If selection is unreadable, request a short description or a node link, not an unnecessary repeat of the full brief.

Map the chosen nodes/annotations to the exact reference version and region; for geometric crops account for image scaling, cropping and card padding. Save the user's words separately from your interpretation: what to take, what to avoid and which destination region it affects. “A's layout, B's cards” authorizes those aspects only, not either reference's entire visual style. “I like this” with an ambiguous target needs one focused clarification; preserve the known part and leave the ambiguous part pending.

Several references may supply different regions in one screen. Avoid asking the user to approve choices they already made. A user can override the ranking. Apply only chosen regions when other regions remain undecided. If the user asks to record preferences only, save them without editing product screens. A changed choice supersedes only that choice and its dependent region.

## Adapt, do not transplant identity

Follow [visual execution](references/visual-execution.md): view the selected original/crop and baseline, preserve concrete composition decisions, and compare the rendered result visually. Use this within the existing application and verification pass.

Inspect the relevant existing product tokens, type styles, components and neighboring content once. Use their actual IDs and behavior. Keep the structural ideas the user chose—hierarchy, composition, grouping, relative proportions or interaction pattern—while using the product's colors, fonts, spacing scale, radii, icons and component families. Preserve Arabic/RTL needs and actual content capacity. Do not overwrite the identity with the reference's branding or copy unlicensed imagery/logos into the product.

Map each chosen feature to existing components/tokens. Reuse instances and overrides; extend only a missing variant/property needed for this selection. If no usable identity exists, report that fact and ask for the essential identity source or explicit direction; do not invent an “existing” brand. If the user's chosen structure conflicts with the product's constraints, explain the concrete conflict and adapt the affected detail without silently discarding the choice. Ask only when the unresolved choice materially changes the requested result.

Build native editable Figma content using the relevant existing operation/component skills. Reference screenshots are evidence, not flattened final screens. Keep sources on the References page and product output in the intended destination; preserve unrelated work.

## Verify and remember

Review the changed scope for both fidelity to the selected aspects and consistency with the product identity. Check relevant spacing, sizing, text wrapping, component reuse and required states in the same normal visual/structural pass. Recheck only after a change or observed issue.

Save the actual destination node IDs, identity bindings, reference version and observed evidence in the selection's application record. Mark applied only after confirmation. In a follow-up, inspect relevant current state and update the affected region in place; never duplicate a screen just because the task resumed. Report the Figma link, which chosen parts were used, and any material adaptations or unresolved parts.
