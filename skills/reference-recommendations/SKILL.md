---
name: reference-recommendations
description: Present an evidence-backed visual reference shortlist, apply user feedback, and prepare an accessible visual handoff for a creative director or designer. Use after reference evaluation or when the user accepts, rejects, or redirects reference choices.
---

# Reference Recommendations

## Contract

Input: evaluated references, original visual evidence, coverage matrix, research mode, and project-specific decisions.

Output: a visual shortlist and a handoff manifest with real source links, images, reviewed parts, reasons, exclusions, alternatives, and selection status. This skill does not create the design or presume a creative-director skill exists.

## Present the Shortlist

Open the pinned visual assets yourself before making new visual comparisons or grouping directions. Record inspections through `shared-visual-assets`. Showing an image to the user or repeating a previous review does not prove your own inspection.

- Present a manageable set that covers the brief. Each recommendation must include a visible image or supported preview, its original source link, stable candidate ID, the exact useful section, and the evidence-backed reason for recommending it.
- Keep the full reference and any detail crop clearly identified. Preserve access to the original visual; never hand off only a textual description.
- If the environment cannot display a preview, provide the accessible image artifact and state the display limitation. If visual evidence cannot be accessed at all, do not present the reference as approved.
- Show meaningful alternatives and explain their visible differences. Keep any unreviewed viewport, state, or required criterion explicit.
- Group references into coherent directions based on observed typography, layout, density, color, and component treatment. Identify conflicting traits and what must not be combined; do not suggest random mixing of incompatible visual identities.
- Distinguish a recommendation from user acceptance. Do not invent approval or impose an approval gate unless the project workflow requires one. A handoff may remain clearly marked as provisional.

## Feedback

Support the following intents in the user's own wording:

- `Accept`: record the reference and accepted scope.
- `Reject`: record the reason if given; do not invent one or demand a reason unnecessarily.
- `Use Partially`: record the exact sections retained and excluded. Clarify if the selected part cannot be identified.
- `Explore Similar`: identify which observed qualities to preserve; route a focused search back through strategy and discovery.
- `Explore Different`: record which qualities should change and which requirements remain fixed; route a new search direction.

Return decisions to the orchestrator for `research-memory`. Apply preferences only within the current project unless the user explicitly broadens their scope. Re-evaluate affected candidates without restarting unrelated research. New candidates must pass actual visual review and evaluation before recommendation.

## Creative Handoff

Read [the shared package contract](../shared-visual-assets/references/package-contract.md). Produce its Visual Reference Package, registering original images, available full-page captures, and linked section crops through `shared-visual-assets`. Include user requirements and existing identity/token/component references with explicit gaps. Pin asset versions; verify access rather than handing off untested image paths. Route this package to `multimodal-creative-director` when direction work is in scope. The receiving role must open the images itself.

Provide a manifest of selected or provisionally recommended IDs, accessible original images and captures, source attribution, visual analyses, exact elements to use, elements to avoid, reasons, coverage, and unresolved gaps. Include coherent alternatives and feedback status.

Confirm that recorded local image paths exist or remote visual references remain accessible. Do not fabricate a recipient, skill, delivery, or completed design. If a creative-director or designer skill has not been designated, return the prepared package to the orchestrator and identify the missing execution capability. Sending to another person requires the user's authorization.

## Final Check

Recheck source links, actual visual-review evidence, requirement coverage, duplication, useful diversity, and image accessibility. Remove stale unsupported claims. If gaps remain, return a bounded follow-up research request or disclose incomplete coverage. Never invent results to finish a shortlist.
