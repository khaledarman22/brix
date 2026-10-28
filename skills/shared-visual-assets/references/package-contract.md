# Shared Visual Package Contract

All paths below are relative to the active project directory, not the installed skill. Create files only when executing the corresponding workflow. Existing authoritative storage may supply equivalent records; record its exact location instead of maintaining competing manifests.

## Storage

- `assets/design/`: actual production images, icons, cutouts, and derivatives, registered in the shared registry below.
- `design/asset-requests/<request-id>.json` and `<request-id>-prompt.md`: versioned asset/edit request and English prompt owned by the asset manager.

- `design/organization/<file-record-id>.json`: actual page/container mappings and recovery records for one confirmed Figma file. Use a stable project record ID, not an assumed raw URL as a filename.

- `assets/refs/manifest.json`: asset registry and inspection records; images normally live beside it. Existing evidence may remain in `research/evidence/` and be referenced here.
- `design/references/<research-task-id>.json`: selected reference package emitted by recommendations, isolated per research task.
- `design/identity/<identity-id>.json`: versioned identity owned by `design-identity-manager`, including observed rules, proposals, adoption evidence, and changes.
- `design/directions/<direction-id>.json`: versioned visual direction emitted by the creative director.
- `design/previews/<preview-task-id>.json`: identity-preview mapping, kept separate from final screen implementation.
- `design/implementation/<direction-id>.json`: implementation mapping emitted by the designer.
- `design/validation/<direction-id>.md`: visual findings, evidence, and repair history.
- `design/validation/<task-id>-structure.md`: scoped FDS compliance, actual field evidence, exceptions, and structural issues.
- `design/evidence/`: actual Figma exports and inspected comparison captures.

Every JSON document includes `schema_version: 1`, project identity, record ID, revision, verified update time, and status. Use real values or explicit `null` plus a reason for unknown data. Never put example IDs or placeholders into a live package. Revisions increase on material changes; consumers pin the revision they used. Preserve prior revisions in project history or versioned sibling files before replacing a consumed package.

Every package reference includes its project-relative path or authoritative location, record ID, and exact revision. A revision number without a resolvable retained snapshot is insufficient. For file storage, archive consumed revisions under a sibling `history/` directory using `<record-id>.r<revision>.json` (or `.md` for reports) before replacing the active record. An established version-control history may be used instead if the exact retrievable commit and path are recorded. Do not overwrite packages belonging to another task. Existing `design/reference-package.json` files may remain in place when recorded explicitly; new tasks use task-scoped paths.

Before publishing a package, parse any JSON, validate its required fields and type-appropriate values, resolve record/asset IDs and revisions, and confirm local file existence. Inspect image pixels separately. Failed validation blocks the handoff, not unrelated work. Do not claim machine-enforced schema validation unless a validator actually ran.

Status meanings are type-specific: reference packages and directions use `draft`, `ready`, `blocked`, or `stale`; identity records use `observed`, `proposed`, `adopted`, `blocked`, or `stale`; implementation mappings use `in-progress`, `implemented`, `blocked`, or `stale`. Validation reports use `pass`, `needs-fixes`, or `blocked`, plus a freshness field. User selection and authorization remain separate fields. `ready` does not mean user-approved; `implemented` does not mean validated. A new upstream revision marks affected downstream records stale and requires reconciliation before reuse.

## Asset Registry

`assets` is a list of records containing:

- `asset_id`, `reference_id`, `version`, `kind` (`original`, `full-page`, `viewport`, `crop`, `derivative`, or `figma-export`).
- `path` or accessible `url`, `source_url`, `sha256` for local bytes, `width`, `height`, `captured_at`, and observed viewport/state when relevant.
- `parent_asset_id`, `parent_version`, and `crop_rect` (`x`, `y`, `width`, `height`) for crops.
- `availability`, `usage_terms` when known, and explicit reasons for unavailable information.

For production assets also record `usage_role` (`reference-only`, `production-candidate`, `production`, or `temporary`), `asset_type` (such as image, icon, or vector), source/creation method, known usage rights, and derivative parent asset IDs/versions. A generated or edited image can use `kind: original` for source bytes or `kind: derivative` for an edit; do not call an edited image an untouched original. Register generated imagery as generated, never as authentic product photography. Production `reference_id` may be null with its actual source provenance recorded. Usage-role promotion requires the asset manager's checks; final placement status belongs to the request and implementation mapping.

For a Figma export, `reference_id` may be null with reason `implementation-output` or `existing-design-baseline`. Record confirmed file/page/node IDs and the baseline or implementation record instead. Do not invent an external source URL for a local user-provided image; record its actual provenance. Stable asset ID/version remains required for all kinds.

`inspections` contains role, task/session where known, asset ID/version, timestamp, actual viewing method, available tool-result reference, and a concrete visible observation. An asset registration is not an inspection.

## Visual Reference Package

Include original requirements and constraints, their source, the research task, and:

- `references`: stable reference IDs, source URLs, original/full-page/crop asset IDs and versions, reviewed parts, analysis record locations, evaluations, recommendation reasons, and user-selection status.
- `identity`: locations and revisions of existing identity rules, tokens, styles, components, and visual identity examples. Include actual Figma IDs where confirmed. Explicitly record missing identity information.
- `coverage`: requirements covered and items not reviewed.
- `inspection_requirements`: assets each downstream role must open, including full context for crops.

Analyses can be linked by stable record ID and file section in research memory rather than copied. The image assets must remain directly accessible independently of the prose.

## Visual Direction Package

Include `direction_id`, source package revision, requirement scope, current selection/authorization status, and:

- `references`: pinned asset IDs/versions, `use_for`, exact regions, `preserve`, `adapt`, and `avoid`.
- `decisions`: stable decision ID, affected section/component, concrete rule, supporting asset/region or explicit user requirement, rationale, and intended departure from the reference.
- `layout_rules`, `typography_rules`, `spacing_rules`, responsive target sizes, required states, and specific designer instructions.
- `identity_preserve`: exact identity constraints and existing component/style/variable IDs when available.
- `tokens`: references to semantic token names and bindings in the pinned identity revision. Draft directions may include separately labeled `identity_change_requests` with proposed treatments; ready directions must resolve them through the identity manager. Do not duplicate an editable value catalog here. Proposed values are deliberate design choices, not measurements guessed from screenshots.
- `validation_targets`: visible outcomes to verify and structural checks needed for implementation.
- `inspection_records`: references to the director's actual inspections, plus unresolved blockers.

Current authorization may allow choosing a direction without asking again. Preserve whether it was user-selected, agent-selected within scope, or awaiting a required decision; do not label all selections user-approved.

## Project Identity Record

Record the inspected Figma target, confirmed token/style/component names, IDs and values, actual visual example asset versions, constraints provided by the user, inspection time, and unknown or inaccessible fields. Preserve observed and proposed values separately. `design-identity-manager` produces and owns this record; the creative director, designer, and validator consume its pinned revision and actual visuals. A package producer may reference an existing authoritative identity record instead of copying it.

An adopted identity includes `visual_review` with inspected example asset versions, the manager's inspection records, required size/mode/state coverage, resolved conflicts, and adoption authority. Keep `observed_values` and `proposed_changes` distinct. Define semantic colors, typography, spacing, corners, shadows, and relevant component rules within scope. Existing bindings have real Figma IDs; proposed bindings remain null until created. `change_log` records the prior revision, rationale, affected consumers, migration scope, and unresolved impact. No global migration is implied by adoption.

For a new project, the proposal references the initial draft direction revision. Its preview mapping uses `basis_type: identity-preview`, the preview brief, proposed identity revision, draft direction revision, and actual evidence/node mappings. An adopted revision cites the reviewed preview and proposal. The finalized direction references the adopted identity; do not rewrite the initial draft or preview to pretend they originally used it. Preserve this revision chain without circular dependencies.

Store preview mappings at the preview-task path above, not at the final implementation path. An existing-project identity extension may pin a scoped change brief and previous direction instead of a newly created director draft. Its proposal and preview remain separate from the currently adopted identity. The preview mapping records isolation from live shared bindings and the preview nodes; it does not imply final-screen completion.

A direction's `identity` reference, implementation mapping, and final validation report all pin the same adopted identity revision for the affected scope. A finalization-only direction update can reuse unchanged preview evidence after explicit reconciliation; changed rules require new relevant visual checks.

The preceding adopted-identity requirement applies to ready reference-led directions and final implementations. Drafts, proposals, and previews retain their historical proposal references. Scoped edits can use their inspected baseline where the plan explicitly permits it. Never mark historical preview evidence stale merely because adoption cites it; assess whether the underlying visual rules changed.

## Scoped Existing-Design Edit

A narrow edit may use a persisted change brief instead of a Visual Direction Package. Its task ID, revision, exact requested change, target, preserve rules, acceptance criteria, and inspected baseline asset versions are required. It may reside in a stable section of project state; retain the consumed section snapshot when changing it. Implementation and validation records use `basis_type: scoped-edit` and its exact reference instead of a fabricated direction reference. For reference-led design use `basis_type: visual-direction`. File names use the scoped task ID when no direction ID exists.

## Implementation Mapping

Pin the direction revision and exact reference versions. Include confirmed Figma file/page/node IDs, decision-to-node mapping, token/component bindings, actual implemented sizes and states, implementation evidence assets, designer inspection records, unresolved gaps, and last confirmed mutation. A screenshot alone does not prove native editability or Auto Layout.

For scoped edits pin the change brief and baseline versions instead. Each relevant acceptance criterion maps to the actual changed nodes. Preserve the difference between unchecked criteria and irrelevant criteria with recorded reasons.

## Validation Report

Pin direction and implementation revisions. Record inspected reference and output asset versions, actual viewport/state coverage, and structural evidence. Each issue has an ID, severity, affected node/region, expected rule, observed result, both evidence references, required correction, and status. Distinguish deliberate adaptations from unintended deviations. Record repair rounds and the next action. Possible overall results are `pass`, `needs-fixes`, or `blocked`; missing required evidence cannot pass.

For scoped edits pin the change brief rather than a direction. Each issue is `open`, `fixed-awaiting-review`, `resolved`, or `blocked`; only actual reinspection resolves an issue. A pass is valid only for the recorded current revisions. Record staleness separately instead of allowing an old pass to authorize a changed implementation.

## Combined Completion

Asset requests use the common revision fields and statuses from `design-asset-manager`. Include original source versions, actual context-capture assets, target node or explicit planned target, originating finding, identity/direction revisions, edit instructions, preserve/avoid rules, output specifications, prompt path/revision, and acceptance criteria. Save actual handoff/return events without inventing another agent's execution. Retain the source package and returned derivative links. Placement verification requires a fresh viewed capture and actual node mapping; a ready prompt alone completes only a prompt-preparation task.

Organization records also retain the planned first-content specification, actual content roots and parent IDs, ordered creation/attachment/population evidence, and incomplete-destination recovery state. Record operation kind (`new-in-place`, `existing-reorganization`, `archive`, or `restore`) so historical checks do not confuse legitimate moves with deferred organization of newly designed content. Organization-only validation may pin this record and a scoped change brief instead of an unrelated screen implementation. Board captures are visual assets; creation-order evidence is actual tool operation data, not a retrospective assertion.

Organization records follow the same common revision fields and use `draft`, `ready`, `blocked`, or `stale`. Include the confirmed Figma file identity, page names/IDs and surface purposes, container/group IDs, actual content IDs, and any archival source-parent/order mappings and dependency checks. `ready` requires actual nonempty created destinations and verified structure; planned page names alone remain `draft`. The designer owns this record and the orchestrator links it from project memory. The shared asset registry holds actual visual captures, not duplicate organization state.

Structural and visual reports remain separate. Both pin the same current implementation or preview revision and affected identity where applicable. Structural validation follows `figma-design-standards` and reports actual field evidence; visual review requires actual pixels. Foundation previews pair structural validation with the identity manager's visual review. Simple scoped edits may pair structural validation with the planned in-task visual evidence. Any required blocked or failing check prevents overall completion. Use one repair counter per scope and retain it across sessions. Integration-specific checks and enforced write interception remain deferred until an adapter is supplied and selected.
