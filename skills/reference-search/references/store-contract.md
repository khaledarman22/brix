# Shared reference store

This is the single data contract for reference-search, reference-evaluate, reference-board and reference-apply. Read only this contract when another reference skill needs shared state; it does not trigger a new search.

## Two storage levels

Use [cache commands](cache-commands.md) for initialization, search, public-reference insertion, reuse and checkpoints. Runtime data is not part of the installed skills.

**Shared reference cache:** `~/.cache/brix/references/catalog.json` and `assets/`. Contains reusable public sources, capture versions/hashes, tags, platform, generic visible strengths/limitations and inspected evidence. This is a machine-local cache used across projects, not cloud sync. Never store project identity, client details, user selections or project-specific fit ratings here. Shared asset paths are relative to this cache root.

**Per-project cache:** `.brix/cache.json` points to the shared root; `.brix/references/catalog.json` contains the project's briefs, adopted reference copies, evaluations, Figma board mappings and user choices. Assets are copied into `.brix/references/assets/`; their paths are relative to the project. `.brix/state.json` holds per-task checkpoints, last confirmed outcomes, pending actions, waiting states and next actions, including design work outside reference search.

Initialize on first use and preserve existing state. The helper backs up schema-1 local catalogs before moving them to schema 2; it preserves existing IDs, records and unknown fields. Unsupported schemas require explicit migration, never a reset. Use the same local lock `.brix/.lock` when updating catalog records outside the helper, read the latest JSON, preserve unrelated fields and replace atomically. Shared writes use the shared `.lock`. Do not hold either lock while making network/Figma calls. Never overwrite another project's progress with global data.

An initial local catalog has schema_version 2 and empty `briefs`, `references`, `evaluations`, `boards`, `selections` arrays. Shared catalog has schema_version 2 and a `references` array. State has schema_version 2 and a `tasks` object. IDs remain stable and are never recycled; new cached references use the helper's content-derived IDs. Null means unknown, not a fabricated value. A stored intention is not evidence of tool success.

Look up local references first, then shared sources, then the web only for missing coverage. Copy a chosen shared reference into the project with `reuse`; don't redownload it. General image observations may be reused globally; assess only project-specific fit for a new brief. Do not inherit another project's fit rating as this project's decision. Brix selects using the current brief; preserve applicable explicit user choices.

## Records

### briefs

`id`, `scope` (screen/region), `purpose`, `platform`, `viewport`, `language`, `content_constraints`, `identity_context`, `requirements_revision`.

Increment the revision only for meaningful requirement changes; keep prior evaluations tied to their old revision.

### references

`id`, `title`, `source_url` (nullable for uploads), `canonical_url`, `gallery_url`, `source_kind` (live-product/concept/gallery/user-upload), `platform`, `regions`, `tags`, `access_status`, `versions`.

Each version: `id`, `asset_path`, `sha256`, `captured_at`, `viewport`, `state`, `inspected_at`, `inspection_notes`, `reuse_rights` (known terms or unknown). Optional crops: `id`, `asset_path`, `sha256`, `bounds_normalized` with x/y/width/height in 0..1 relative to this version. Crops retain their original source/version.

### evaluations

`id`, `reference_id`, `version_id`, `brief_id`, `requirements_revision`, `scores`, `evidence`, `strengths`, `limitations`, `reuse_regions`, `recommendation`, `evaluated_at`.

Scores use the criteria defined in reference-evaluate. They are the designer's reasoned assessment, never user ratings or measured conversion data. Keep old evaluations when the image/brief changes. A recommendation is not approval.

### boards

`id`, `brief_id`, `file_key`, `page_id`, `section_node_id`, `status`, `cards`, `last_verified_at`.

Each card: `reference_id`, `version_id`, `label`, `card_node_id`, `image_node_id`, `evaluation_id`, `annotation_node_ids`. Use stable labels A/B/C within that board; do not renumber cards after the user has referred to a letter. Add the reference ID visibly so letters from different boards are unambiguous. Node IDs/file keys must come from confirmed tool results. Reuse a page across boards in the same file. Store pending status if writes or image imports are incomplete; never mark a blank card presented.

### selections

`id`, `brief_id`, `reference_id`, `version_id`, `board_id`, `region` (crop ID, normalized bounds, node IDs or explicit textual description), `selected_by` (user/brix), `rationale`, `user_quote` (null for Brix decisions), `evidence_kind` (message/explicit-selection/annotation/designer-decision), `evidence_node_ids`, `take`, `avoid`, `target_region`, `status` (needs-clarification/selected/applied/rejected/superseded), `identity_bindings`, `application`.

Record Brix's autonomous choice with selected_by=brix, evidence_kind=designer-decision, user_quote=null and a brief rationale linked to the evaluated scope. Explicit user choices use selected_by=user and preserve the user's actual words/evidence separately from interpretation. Missing selected_by in legacy entries retains its original user-evidence meaning; do not relabel history. A score or cursor highlight is not user approval. Preserve previous choices; supersede only the affected decision, and never override an explicit user choice with an autonomous one. These additive fields need no schema reset; board_id may be null before a board exists.

`identity_bindings`: actual existing variable/style/component IDs where known, with semantic roles and necessary adaptations. `application`: destination file/page/node IDs, reference version applied, observed validation evidence and timestamp. Leave application empty until a real confirmed change.

## Reuse and freshness

Consult the catalog at session start. Keep assets/evaluations/boards for reuse; do not delete rejected or unused evidence automatically. Do not recapture or re-evaluate solely due to elapsed time. Verify a saved node mapping when it is about to be used; repair a missing card by its stable reference ID and version, preserving human annotations. Changing a source image never silently moves a user selection onto the new version.

For a new brief, reuse an existing image and assess only new contextual fit. For an unchanged brief and version, reuse the evaluation. Never reapply an already-applied choice to an unchanged destination without a new user request or a confirmed repair need.

## Resume state

At every resumed task, consult `.brix/state.json` and the local catalog before acting. Continue from `next_action` after checking `last_confirmed`; pending Figma writes require reconciliation, not automatic replay. Keep user decisions local. A `waiting_for_user` checkpoint for a user-requested choice or missing essentials stays waiting until an actual response. Under the autonomous-selection policy, resolve only legacy waits caused solely by mandatory reference choice: record Brix's evaluated selection and policy reason, clear that wait and resume. Never clear permission or unrelated blockers. Save checkpoints after confirmed board presentation, received choices and verified application, and before/after risky writes. Do not repeat completed search, rating, board construction or design application just because a new chat opened.

## Quality and pagination records

Each reference may contain `quality_reviews`, written by the helper's `review` command: version_id, verdict, scores (layout/typography/spacing/visual_clarity), strengths, weaknesses, useful_regions, avoid_regions, evidence and inspected_at. These are general visible-quality assessments. Local `evaluations` still store contextual project fit; `selections` store attributed user or Brix decisions, with project-fit rationale kept local. Shared ratings must contain no project/client context. Reuse merges new general quality reviews without overwriting local choices.

Each cache root also supports `searches.json`: schema_version 2, `searches` object keyed by a stable hash of source + normalized query + filters. Local path: `.brix/references/searches.json`; shared path: shared-root/searches.json. Each search records the request, observed pages/batches, deduplicated result IDs, visited tokens, next token, status, reason and retry-after. A successful page cannot be erased by a failed retry; history is retained. Browser-session/private continuations stay local. Search completion is not design approval.

The cache helper serializes writes and deduplicates identical observations. Agents must supply actual evidence and update these records while working; this is not a scheduler. Never truncate/reset the store to “clean it up” or remove rejected candidates merely to improve results. Missing/corrupt assets should be marked and repaired from verified sources, without fabricating new scores or discarding user selections.

## Part progress and canonical identity

`state.identity` is the project's single identity record (stable id, revision/context and actual bindings or explicitly unresolved status). `tasks[task_id].identity_id` references it. `tasks[task_id].parts` maps stable part IDs to title, scope, parent_id, depends_on, status, revision and checkpoint evidence. Choices/briefs/boards remain in the local catalog and are linked by each part's IDs; nothing here belongs to the shared public cache. Use plan-parts/part-checkpoint/ready-parts as documented in cache-commands. Whole-task checkpoint cannot overwrite parts or bypass unfinished-part checks.

## Project composition language

`state.identity.composition_language` is the single project-local record for visual composition. Add it without changing the state schema version or identity ID. Preserve all existing identity bindings and task history. Use the existing local lock and atomic update protocol, reading current state under the lock. `plan-parts` reuses the saved identity; never pass a conflicting replacement identity just to update this record.

Fields: `id` (stable), `revision` (integer), `status` (draft/established), `rationale`, `principles` (specific rule, reason, applicability and binding IDs where known), `screen_families`, `source_references` (actual version/region and interpreted contribution), `visual_anchors` (actual Figma file/node IDs, local export paths, inspected_at, language revision and principles demonstrated), `validation_coverage`, `exceptions`, `history` (previous revision/decisions/evidence and reason for change). Empty evidence means unverified. Established means demonstrated in the recorded coverage, not tested on every screen family. Unknowns remain explicit.

Task/part checkpoints record `composition_language_revision_used`, applicable principles and observed integration evidence. A language revision is independent of token/brand revisions; keep history and record affected parts for scoped rechecking. Preserve explicit user decisions. Existing projects without this field resume normally and establish it during the next authorized composed-screen task; do not reset caches or fabricate retrospective evidence. See [project composition](../../reference-apply/references/project-composition.md) for the workflow.
