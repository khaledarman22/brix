# Project composition language

Build one recognizable visual composition language per project and carry it across screens. Colors, fonts and component tokens alone do not constitute this language: it describes relationships between content, imagery, hierarchy and space. Apply this within the existing design task, with no extra agent, approval gate, mandatory moodboard or whole-library phase.

## Establish or resume

Read `state.identity.composition_language` and its visual evidence before designing a composed screen. Reuse its current revision; do not regenerate it for each screen or chat. Inspect representative existing screens directly and respect user decisions. Polished work is evidence of established conventions; inconsistent or unfinished screens need assessment, not blind adoption. A missing record does not authorize redesigning existing screens.

When absent, synthesize a compact direction from the product's purpose, audience, platform, content, identity and inspected visual evidence. Use cached references first and research only unresolved visual questions. References inform principles; do not assign a different reference's composition to each screen. Choose autonomously within scope, preserving explicit choices. No fixed number of references or alternatives is required.

Record concrete decisions with rationale and applicable contexts for the aspects the project needs:

- Hierarchy and reading order: focal element, title placement/width/wrapping, relationship of title, copy and main action.
- Spatial rhythm: grouping, alignment, density, occupied versus empty space, and relationships to existing spacing/grid tokens.
- Imagery: photography or illustration direction, subject framing, crop, scale, backgrounds, relationship to text and restrained decorative motifs.
- Shape and emphasis: how panels, surfaces, edges, overlap and accents support composition, using existing components/tokens where appropriate.
- Screen-family adaptations: expressive discovery, quiet forms and dense transactional screens can share hierarchy, framing and rhythm without having an identical layout.

Avoid “premium, clean, modern” without observable rules. Do not fabricate distinctiveness through clutter or force images onto focused tasks. Numeric relationships are contextual decisions, not universal ratios. Preserve RTL, text capacity, accessibility and platform conventions.

## Make the direction visible

Use the first authorized screen or region to demonstrate the proposed language with real content and native editable layers. Save an actually viewed export and Figma node IDs as a visual anchor, noting the defining relationships. Prose, a logo/color sheet, or an external screenshot alone cannot validate the project's own language.

Compare the result with the intended principles and product goals; refine targeted decisions if the image does not support them. Optional visual alternatives or generated art may resolve uncertainty but are not mandatory. Choose and continue without routine reference-selection questions.

Mark validation coverage honestly. One inspected screen demonstrates only its context; the first different screen family tests transfer. Do not create extra screens just to claim cross-screen validation. A later authorized form, catalog or checkout retains visual relationships while adapting to content. Record which principles transferred and necessary exceptions.

## Apply to each screen

Start from the saved language, the screen's job and existing components, not a newly found reference layout. Record the language revision used and relevant rules in the part checkpoint. Consult a new reference only to solve a concrete gap; explain how its useful principle fits the language. An explicit request to reproduce a reference remains valid within its scope; record a scoped exception if needed rather than silently redefining the project.

In the normal visual review, compare the rendered screen with project visual anchors at useful resolution. Verify hierarchy, rhythm, imagery and component relationships as well as tokens. Unrelated layouts with matching colors are not a passing integration check. Correct accidental drift while preserving justified variation between screen families. Do not prioritize reference similarity over a coherent, usable product.

## Save and evolve

Persist under `state.identity.composition_language` using the local store contract and existing `.brix/.lock` plus atomic-write protocol. Preserve unrelated state. Never put project language in the public cache or installed bundle. Save the initial draft before implementing it, and confirmed evidence after inspecting the result. Pending Figma mutations still belong in normal task/part checkpoints.

The record contains a stable ID, revision, draft/established status, rationale, concrete principles and screen-family adaptations, actual token/component bindings, source provenance, visual anchors, coverage, exceptions and change history. Unknowns stay explicit; never invent IDs or approval. If storage is denied, save a recovery record in an authorized destination and report authoritative state as unsynced; do not bypass permissions.

Revise for explicit feedback, changed requirements or a demonstrated limitation in a new context. Increment the language revision and retain prior decisions/evidence with the reason in history. Record affected parts for scoped rechecking without rebuilding unrelated completed work. Historical evidence is not current validation. Preserve the identity ID and existing brand tokens unless changing them is authorized.
