# Cache commands

Run `scripts/cache.py` relative to the reference-search skill directory. Always pass the calling design project with `--project`; never infer it from the installed skill location. The script uses Python's standard library and POSIX file locks (macOS/Linux), not a background service.

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project init
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project status
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project find 'mobile checkout'
```

Default shared root: `~/.cache/brix/references`. `init` records the resolved location in the project's `.brix/cache.json`. Use `--shared-root /explicit/path` before the subcommand to override it. Never modify shared data through manual JSON writes without its `.lock`; this tool serializes writes and replaces JSON atomically. An unavailable shared path is a blocker for shared-cache operations, not a reason to discard local state or start the task again.

`find` matches all words against title/platform/regions/tags/visual_notes, local first then shared, deduplicated by ID. It is a keyword lookup, not semantic search: try synonyms and relevant tags before deciding the cache has no coverage. Inspect results for actual suitability.

## Add and reuse reference captures

Prepare a JSON metadata file inside the project. Required: `title`. Useful: `source_url`, `canonical_url`, `source_kind`, `platform`, `regions`, `tags`, `viewport`, `state`, `captured_at`, `inspected_at`, `visual_notes`, `reuse_rights`.

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project add --asset /absolute/design-project/capture.png --metadata /absolute/design-project/metadata.json
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project add --asset /absolute/design-project/public-capture.png --metadata /absolute/design-project/public-metadata.json --shared
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project reuse ref-RETURNED_ID
```

Use `--shared` only for verified public live-product/concept/gallery sources, with `public_source: true` and a public source URL. A URL or boolean alone does not prove publicity; the caller must verify the capture contains no account-specific/private content. Do not include user decisions, identity, credentials, query secrets or client/project information in public metadata. Private uploads and authenticated screenshots stay local unless the user separately authorizes sharing them across projects; the helper intentionally rejects those source kinds in the shared store.

IDs derive from canonical source + viewport/state + image hash; assets are content-addressed. Returned version IDs are hashes. Re-adding the same capture is idempotent. A changed image produces a new immutable reference record; keep the previous record for existing choices. Record `related_reference_ids` in local state when versions from the same source need grouping. `reuse` verifies the shared asset hash and copies it into the project, preserving local decisions. Copies let the project continue if the shared cache is unavailable. No automatic deletion or TTL.

The helper does not capture images or visually inspect them; supply only real captures and truthful metadata. It does not transfer project suitability scores to other projects.

## Checkpoint and resume

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project checkpoint task-001 --data /absolute/design-project/checkpoint.json
```

Checkpoint data is a JSON object. Minimum `status`: `in_progress`, `waiting_for_user`, `blocked`, or `complete`. Useful fields:

- `request`: current user intent, scope and constraints.
- `brief_ids`, `reference_ids`, `selection_ids`: catalog links.
- `figma`: actual destination file/page/node IDs and confirmed identity bindings.
- `last_confirmed`: completed operation and evidence, not merely intended work.
- `next_action`: concrete next step, not a new generic workflow.
- `pending_action`: null or an intended/in-flight mutation with operation ID, intended scope and known IDs.
- `waiting_for`: the precise unresolved user choice or blocker.

Updates merge with previous task fields; explicitly set `pending_action` and `waiting_for` to null when resolved. Revisions increment under the local lock. A task cannot become complete with a pending action. A completed task stays in the file when a new task begins. Checkpoint at meaningful boundaries and before/after potentially non-idempotent Figma writes; not after every read.

On resume, read status plus the local catalog before any new research. If a write was interrupted, inspect the exact destination/known IDs or operation status first; reconcile its observed result and clear the pending action. Never blindly replay it or mark success from a saved intention. Preserve explicit user selections and waiting states. If everything requested is complete, report that without rebuilding. The cache stores progress; it cannot itself resume a chat, poll Figma or execute work autonomously.

## Record reusable quality

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project review ref-RETURNED_ID --data /absolute/design-project/review.json --shared
```

Omit `--shared` for a local/private reference. `review.json` contains the exact version_id, verdict (strong/mixed/weak/unreviewed), scores with optional integer 1–5 or null values for layout/typography/spacing/visual_clarity, strengths, weaknesses, useful_regions, avoid_regions, evidence and inspected_at. Rated entries require evidence and inspection time. The helper checks format and reference/version existence, not whether an agent actually saw the image. Record that honestly. Identical reviews are idempotent; revisions are retained. Invoke `reuse` again to merge new shared general reviews into the local copy without changing local decisions.

## Track search pages and continue later

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project search-log --request /absolute/design-project/search.json
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project search-log --request /absolute/design-project/search.json --page /absolute/design-project/page.json
```

`search.json`: source (actual listing/search source URL), query, filters (sort/category/platform etc.), public_source. Add `--shared` only for a verified public query with public_source true and no project-specific or private content. Without `--page`, lookup is read-only; null means no history.

`page.json`: request_token (stable string identifying the actual requested URL/cursor/batch), url, pagination_mode (numbered/next-link/cursor/load-more/infinite-scroll/none), result_ids (saved reference IDs), next_token (observed next page/cursor or null), outcome (visited/blocked/failed), observed_at, end_confirmed (boolean), coverage_satisfied (boolean), reason, retry_after. All tokens must be observed, not invented endpoints. Coverage and exhaustion are distinct; set end_confirmed only with evidence of the end and no next token. A blocked/failed record points back to its own token for a later justified retry. Missing continuation pauses rather than claiming exhaustion. Repeated visited continuation tokens are flagged as a loop. The tool records state only; it does not fetch pages or automatically retry.

## Split a request and resume each part

Use the same Brix agent for all parts. Partition by meaningful screen/function and, when useful, by region within a screen. Do not split every tiny element into a task. Keep stable IDs and preserve the plan across sessions.

```sh
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project plan-parts task-001 --data /absolute/design-project/parts.json
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project ready-parts task-001
python3 -B <skill-dir>/scripts/cache.py --project /absolute/design-project part-checkpoint task-001 home-header --data /absolute/design-project/part-progress.json
```

`parts.json` has `request`, `identity` (only when establishing the project's single identity) and `parts`. Example shape:

```json
{
  "request": "Design the store home and checkout",
  "identity": {"id": "store-identity", "status": "unresolved", "bindings": {}},
  "parts": [
    {"id": "home", "title": "Home", "scope": "Assemble the home screen"},
    {"id": "home-header", "parent_id": "home", "title": "Header", "scope": "Navigation and search"},
    {"id": "home-products", "parent_id": "home", "title": "Products", "scope": "Product card section"},
    {"id": "checkout", "title": "Checkout", "scope": "Order details and submission"}
  ]
}
```

Supply actual identity bindings when known; an unresolved record is not permission to invent an existing brand. Subsequent plans reuse `state.identity`, never create a separate identity per part. Resolve/update the canonical identity from actual evidence under `.brix/.lock`, preserving state; do not change its ID or silently overwrite it through a plan. Parts refer to this identity through their task. Inspect actual styles/components when needed.

Optional `depends_on` lists prerequisite part IDs. Parent nodes are assembly/review containers: they complete after children; children must not depend on their parent, which would create a cycle. The helper rejects missing dependencies, cycles and duplicate IDs. Repeating an unchanged plan preserves progress, references and choices; no new task ID for an unchanged request. New scopes can be added without erasing finished parts. Explicitly reopen a completed part with `reopen_reason` before changing its scope.

`part-progress.json` uses status pending/in_progress/waiting_for_user/blocked/complete and the normal checkpoint fields: last_confirmed, next_action, pending_action, waiting_for, brief_ids, reference_ids, selection_ids, figma (actual destination IDs), and identity_revision_used if applicable. Record only real evidence. Set pending_action/waiting_for to null when resolved. Complete requires confirmed evidence, completed dependencies/children, and no unresolved action or choice. Overall task completion is rejected while any part is unfinished.

`ready-parts` returns ready IDs, pending writes requiring reconciliation, and parts waiting/blocked. Resume an in-progress part's next action first. Reconcile pending writes before replay; work on independent ready parts while another waits for user selection. For a legacy wait caused solely by mandatory reference selection, record Brix's evaluated choice and policy reason, clear that wait and continue. Preserve waits for user-requested selection, permissions, missing essentials or other blockers. Reopening a prerequisite marks completed parents/dependents pending for a scoped recheck, retaining their saved evidence; it does not erase or rebuild them. Unrelated complete parts stay complete. Save a final scoped integration check for shared identity and screen continuity, without redoing each completed part's full research/review.

## Audit clarifications

When reopening a completed part or changing its scope, the helper retains `previous_confirmation` and clears stale `last_confirmed`. Completion needs fresh observed evidence. `ready-parts` prioritizes in-progress work and returns `next_actions`; pending writes remain in `reconcile_first`. Whole-task completion for a part-based request must include a fresh `integration_check` describing actual identity/composition verification, and cannot retain `waiting_for`. This is the final integration review already required by the project policy, not an additional audit stage.

Re-adding identical original image bytes can repair a missing cached file without creating another reference; corrupt existing bytes are reported rather than overwritten silently. Do not discard source/version history to repair an asset.

## Composition-language persistence

Before composed-screen work, read `state.identity.composition_language`. Establish/update it as specified in store-contract under `.brix/.lock` with an atomic replacement preserving unrelated fields, not through `plan-parts` with a different identity. The existing helper preserves additive identity fields. Save the revision used in each task/part checkpoint as `composition_language_revision_used`. A new screen reuses the language; change its revision only with a recorded reason and retain previous evidence. See [project composition](../../reference-apply/references/project-composition.md).
