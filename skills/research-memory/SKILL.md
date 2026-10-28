---
name: research-memory
description: Persist and restore project-specific reference exploration, visual evidence, evaluations, and user feedback. Use throughout reference research to avoid lost progress and unproductive repetition across sessions.
---

# Research Memory

## Storage and Ownership

Maintain `research/REFERENCE_MEMORY.md` under the active project directory established by `project-memory`. Store visual evidence separately under `research/evidence/` when local capture is supported and permitted; otherwise record accessible original image or capture references. Do not create empty evidence directories unnecessarily.

`PROJECT_STATE.md` stores only the research summary, memory path, active task, blockers, and next action. The detailed exploration record lives here. If another authoritative project system already stores these records, use this file as its resume index instead of duplicating an editable database.

Use `shared-visual-assets` as the registry of image versions and actual per-role inspections. Existing research evidence can be registered in place. Link candidate records to shared asset IDs and versions rather than copying images or maintaining conflicting availability records. A changed reference version invalidates dependent visual reviews and evaluations until rechecked.

The orchestrator is the writer. Research skills return structured updates; workers must not race to overwrite this file. Read existing contents and reconcile newer edits before writing. Do not replace an unrelated file, discard uncertain records, or assume synchronization across hosts.

## Record Structure

- **Project and run:** format version `1`, project identity, research task ID, brief, mode, budget and consumption, verified update time, active route, and next action.
- **Search log:** actual query, source, result page or cursor, timestamp, examined results, unsuccessful routes, and remaining routes. Separate planned searches from executed searches.
- **Sources:** provenance facts, accessibility, attribution where available, and observed issues. Keep source quality separate from reference quality.
- **Candidates:** stable ID, canonical URL, title, creator if known, query provenance, original visual references, local evidence paths, discovery status, and duplicate relationships.
- **Visual reviews:** viewed images, viewport sizes, observed states, actual findings with locations, review time, and `not reviewed` fields. Never turn absent evidence into a conclusion.
- **Evaluations:** page and component ratings, reasons, accepted or excluded scope, coverage, observed similarity groups, and evaluation method.
- **Directions and recommendations:** previously explored directions, shortlisted IDs, alternatives, chosen parts, and handoff artifacts.
- **User feedback:** actual decisions and reasons, selected scope, source or time where available, and current project preferences. Separate user acceptance from agent recommendations.

Use exactly these candidate states: `candidate`, `reviewed`, `eligible`, `excluded`, `unavailable`, or `stale`. Preserve per-use evaluations separately when only part of a reference qualifies. Store duplicate/unrelated exclusions as reasons, not new status names. Keep user decisions in a separate field. IDs remain stable across runs and sessions.

The saved brief and cumulative budget counters are keyed by research task ID; resumption and revised search routes do not reset them. Record actual counters according to `research-strategy`, along with any authorized or explicitly revised limit.

## Lifecycle

1. At research startup, read existing records before choosing queries. Restore the current brief and incorporate new user instructions without erasing useful prior evidence.
2. Save after each meaningful discovery batch, visual-review batch, evaluation, recommendation, or feedback update. Checkpoint the exact next route or candidate, not just “continue research.”
3. Reuse cached evidence when it still covers the current requirement. Check source and evidence accessibility before final recommendation. If the source changed or a new viewport or interaction is required, mark affected findings stale and inspect again.
4. Historical captures remain evidence of the captured version only. Do not present them as the current live page without rechecking it. Never fabricate a freshness guarantee or reanalyze unchanged evidence unnecessarily.
5. Avoid repeating unsuccessful queries without a reason. Retain strong reusable references; repeated use is acceptable when relevant. Vary exploration based on this project's history, not on an invented global preference profile.
6. After writing, read back the changed record and return a compact summary for `project-memory`. If persistence fails, report the unsaved update and preserve the prior file. Do not claim the exploration is stored.

## Boundaries

Save concise observations and references, not full chat transcripts, secrets, credentials, or unnecessary personal data. Record only real tool outputs and viewed evidence. Writing memory does not perform discovery or visual review.

Prefer project-relative artifact paths. When a project moves, resolve them from the current project directory; reconnect live services separately. Missing evidence or changed URLs must be marked for revalidation, not silently removed or treated as successful checks.

## Completion

The saved file can be read, candidate and task IDs remain traceable, actual search budget consumption is recorded, user preferences remain project-scoped, and the orchestrator knows the next action and the path to the research record.
