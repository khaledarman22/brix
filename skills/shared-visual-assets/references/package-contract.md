# Brix Record Contract

This document defines storage/fields, not additional workflow. [AGENT.md](../../../AGENT.md) owns scope, research, per-screen coverage, identity, inspection frequency and Record Once. Read only relevant sections. All paths are relative to the calling project. Existing authoritative records may supply equivalent fields in place; do not create empty files, migrate valid records, or require one file per conceptual record.

## Ownership and locations

| Record | Owner | Suggested location for new records |
| --- | --- | --- |
| Task, requirement/locale/form decisions, resume point | Orchestrator/planning | `PROJECT_STATE.md` or existing task system |
| Research intent, search history, selections and screen/part coverage | Research-and-selection | `research/REFERENCE_MEMORY.md#<task-id>` |
| Asset metadata and source/derivative links | Shared asset registry | `assets/refs/manifest.json` |
| Identity values, component families, adoption | Identity manager | Existing identity or `design/identity/<id>.json` |
| New composition decisions | Creative director | Task section or `design/directions/<id>.json` |
| Actual node/operation mappings, before/after checks and findings | Designer/coordinated reviewers | Task section or `design/implementation/<id>.json` |
| Isolated identity-preview mapping | Designer | Task section or `design/previews/<id>.json` |
| Asset request and English edit prompt | Asset manager | `design/asset-requests/<id>.json`, `<id>-prompt.md` |
| Actual destination/archival mappings | Designer | Task section or `design/organization/<id>.json` |

An existing reference package or separate structural/visual report remains usable at its canonical location. New work uses one inspection record for both criteria; no separate report pair is required. Preview and final-screen scopes remain distinguishable without duplicating findings. Optional indexes contain links only, not mirrored status, prompts or descriptions.

## Identity, revisions and statuses

New structured records use `schema_version: 1`, project identity, stable record/task ID, revision and type-appropriate status. Actual changes get real update times. Missing facts are explicit null/unknown with a reason; never invent IDs or measurements.

A record reference is location + ID + exact consumed revision. Preserve consumed versions using one existing history/version-control store, or targeted deltas; do not create per-consumer copies. Unrelated registry metadata additions do not invalidate unchanged image bytes or inspection. Resolve affected pins when their inputs change. A revision number without retrievable content is not evidence.

- Tasks: `pending`, `running`, `completed`, `blocked`, `failed`; planning readiness is separate.
- Research/direction: `draft`, `ready`, `blocked`, `stale`; coverage distinguishes `ready_scope` and `blocked_scope`.
- Identity: `observed`, `proposed`, `adopted`, `blocked`, `stale`.
- Implementation: `in-progress`, `implemented`, `blocked`, `stale`.
- Shared review: `pass`, `needs-fixes`, `blocked`, with freshness separate. Findings: `open`, `fixed-awaiting-review`, `resolved`, `blocked`.
- Asset requests: `draft`, `ready-for-handoff`, `awaiting-external`, `returned`, `candidate-approved`, `placed-verified`, `blocked`, `stale`.

Ready/selected/adopted never means user-approved without actual approval. Implementation completion does not imply accepted design. Validate changed records/JSON and needed links before dependent use, reusing unchanged validations. Failed persistence blocks affected handoff, not independent work. Never claim automated validation unless it ran.

## Assets

Store stable `asset_id`, byte `version`, kind (`original`, `full-page`, `viewport`, `crop`, `annotation`, `derivative`, `figma-export`), actual path/URL, source/provenance, dimensions, capture state/time when relevant, local SHA-256 when available, availability and known usage terms. Production assets also record role/type and source or generation method. Reference access is not a reuse license.

Derivatives retain parent ID/version and actual pixel geometry. Check bounds and scaling; optional polygons need valid in-bounds non-self-intersecting geometry. Whole-image selections may use the original without duplicate crops. Preserve original bytes; never substitute generated reference pixels. Production and reference assets have distinct roles even in the same registry.

Figma captures carry confirmed file/page/node IDs and baseline/output record links, not fabricated external URLs. Generated assets are labeled generated; real product-photography requirements are in release checks. No future inspection may be pre-populated.

## Selection and per-screen coverage

“Visual Reference Package” is the one canonical research-and-selection record, not another deliverable. The selection skill defines compact search fields and budget. Each selected entry links source/asset version, useful region, fit/quality rationale, intended use, material adapt/avoid constraints, actual inspection evidence and selection authority. Optional region derivatives have links only when useful.

Every new screen has a stable screen/part ID, whole-composition support, relevant region selections and coverage (`covered`, `gap`, or explicitly `user-exempted`). Source/target platform and platform evidence establish `matched`, `mismatched` or `unverified`; industry/function are context, not eligibility gates. Crops retain source-platform provenance. Keep actual content requirements separate from visual support.

The task's `ui_reference_gate` links coverage and evidence instead of copying them. Gate status is `pending`, `satisfied`, `blocked`, or `user-exempted`, keyed to request/scope/research iteration. Only covered scope proceeds. Simple edits use `research_mode: existing-context` and need no historical gate; explicit reference search uses `requested-search`. Other new design work follows the canonical research rule.

Actual user rejections have canonical wording/source, exact scope and selection/reference IDs. Exclude rejected uses through aliases, crop lineage and shared decisions, while preserving history and unrelated valid uses. Newly affected gaps return to the same research task; do not silently bypass a rejection with another ID. Explicit searches for alternatives record what is genuinely new or why the request remains unresolved.

## Requirements, identity and application

Planning owns confirmed `ui_locale`, direction and source; forms declare required fields, constraints/source, synthetic sample values, visible messages and expected button/loading state. Label proposed visual policy distinctly from existing behavior. Record these once and link them; a reference is not evidence of backend rules.

Identity owns observed/proposed/adopted tokens and component roles/states, actual Figma IDs/bindings, unknowns and adoption evidence. Proposed IDs remain unknown until created. Extensions record affected scope and prior revision. A preview may use a proposal; final screens pin adopted identity. Adoption does not authorize migration or invalidate unchanged preview evidence.

Application records only new spatial decisions: selected ID/region, target screen/part, intended masses/proportions, axes, whitespace, focal/action order, and justified adaptations for content and shared identity. Link existing selection analysis and tokens. Do not invent measured source values or rewrite intended relationships solely to excuse a defect.

Implementation maps those decisions (or scoped-edit brief) to real nodes, changed bindings, sizes/states, asset versions and actual operations. Use `basis_type: visual-direction`, `scoped-edit`, or `identity-preview`. Do not fabricate reference provenance for nodes derived from identity or requirements.

## Shared inspection and acceptance

One canonical pass record stores before/after phase, actual observer, scope, inspected versions, viewing/read method and evidence links. Visual `composition_checks` include affected relationship, baseline/reference/output, observed outcome and linked finding. Structural criteria include actual field/operation evidence, FDS rule and outcome (`pass`, `fail`, `not-applicable`, `not-reviewed`, `exception-accepted`). Findings own expectation, observation, affected node/region, required correction and state.

Decision owners consume this evidence: identity manager adopts previews; scoped reviewer resolves screen/organization/placement findings; orchestrator closes tasks. These ownership labels do not require more observers, reports or passes. All required applicable visual and structural criteria must pass; missing evidence stays blocked and visible defects need correction. No historical intermediate-layout record is required.

A repair, relevant requirement/content change or unavailable evidence triggers only affected reinspection under AGENT.md. Keep one repair counter per scope, including asset fixes. Reuse current available before/after evidence across roles, sessions and acceptance steps without another audit.

## Asset edits and organization

Asset requests identify source-placement or image-edit, target, source/output versions, requirements, optional/required correction, finding link if any, and actual dispatch/receipt. The reusable English prompt is canonical in its own file; `PROMPTS.md`, if useful, contains request/prompt links only. Keep in-flight prompt revisions retrievable. Prepared is not dispatched, returned is not placed, and placement is not verified without the shared after pass.

Organization mappings record confirmed file/page/container/content IDs, operation kind (`new-in-place`, `existing-reorganization`, `archive`, `restore`), first real content, actual ordered creation/attachment evidence and recovery state. Planned names are not real objects. Archive records retain original parent/order and dependency checks; no unsolicited deletion or automatic Trash purge. Operation evidence can be linked to retained tool results rather than transcribed into another log.
