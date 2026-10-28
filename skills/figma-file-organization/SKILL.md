---
name: figma-file-organization
description: Plan on-demand Figma pages, naming, product-surface separation, Auto Layout content containers, reusable-component placement, and recoverable Trash organization. Use when adding actual screens/components or organizing an explicitly scoped existing file; never scaffold empty pages.
---

# Figma File Organization

## Responsibility

Organize pages inside the selected Figma file, not separate Figma files or local folders. Determine the minimum destinations needed for real deliverables and hand a concrete organization plan to `figma-designer`. The designer remains the sole design-node writer; this skill does not independently mutate Figma or choose the visual identity.

Read [Figma Design Standards](../figma-design-standards/SKILL.md) and respect [the deferred integration contract](../../FIGMA_INTEGRATION.md). Use confirmed live file structure when connected. Until then an organization plan is provisional, not a claim that pages exist.

## On-Demand Pages

1. Identify actual products, audiences, platforms, and deliverables from the request. Multiple apps, websites, and dashboards are supported. Do not invent a vendor app, provider app, or dashboard just because the naming pattern supports it.
2. Inspect existing page IDs, names, contents, and organization mappings. Reuse a matching destination based on purpose and content, not its name alone. Preserve established naming conventions unless the user requests reorganization.
3. For new destinations use clear names, for example:
   - `App / Provider`, `App / Vendor`, or `App / Customer`.
   - `Web / Public`, `Web / Provider`, or `Web / Vendor`.
   - `Dashboard / Admin`, `Dashboard / Provider`, or `Dashboard / Vendor`.
   - `Components` for genuinely shared reusable components; add product-specific groups, or a scoped component page only when actual content and usability justify it.
   - `Trash` only when something is actually being retired within the authorized scope.
4. These examples are a naming vocabulary, not a template to generate in full. A single app with no relevant role distinction can simply use `App`. Keep different product surfaces distinct without duplicating shared components or tokens.
5. A planned destination may be recorded before execution, but create the page and its container only alongside its first real screen/component/archive item. Do not create empty App, Web, Dashboard, Components, or Trash pages as placeholders.

The existence of separate app pages does not imply separate brands. Reuse the project identity; request identity-manager clarification only when actual requirements call for distinct product identities or modes.

## Build in the Destination

Organization is a prerequisite to construction, not a cleanup phase after design. For new content, resolve the destination page and container/group before building the screen or component. Never finish a design on the page root or a staging page and then move it into its wrapper.

1. Prepare the first real content specification and resolve required inputs before creating a destination. A page name, empty screen frame, heading, or placeholder is not real content.
2. Reuse or create the needed page, then its Auto Layout content Frame and required group. Set layout and sizing before adding designed content.
3. Create the actual screen/component in that parent, verify its parent ID, and populate its own nested layout there. Pass a target-parent ID or equivalent nested specification to supported creation tools.
4. If a low-level API initially creates an empty node at the canvas root, attach that empty node to its intended parent immediately within the creation operation, before building its visual content. This API initialization detail is not permission to design outside the destination and reparent later. If the adapter can only create a finished design elsewhere, stop and report the capability gap.
5. Build main components in their intended component-family container from the outset; build instances in their intended screen parents. Tool-required variant-set assembly must stay in the planned component destination and be recorded, not become an end-of-task organization pass.
6. Record operation order, creation/attachment evidence, actual parent IDs, and first-content verification. Finish each newly created destination with real content before starting another destination. Do not schedule empty-page scaffolding as an independent completed task.

Use one supported creation batch where possible. If the adapter requires multiple calls, a parent may be briefly empty while its first content is being created; do not describe these calls as an atomic transaction or claim that no transient empty object can exist. Interrupted empty destinations remain incomplete and follow the recovery rules below.

Moving existing content is permitted only for separately scoped reorganization, archival, restoration, or an authorized migration. These cases do not permit build-then-move for new designs.

## Container Structure

A Figma Page is the canvas; the Auto Layout container is a native Frame inside that page. Do not claim to apply Auto Layout to the Page itself or confuse a Figma Section with an Auto Layout Frame.

For each new or explicitly organized content page, use one primary content Frame named for its purpose, such as `App / Provider / Content` or `Components / Content`. It is a layout wrapper, not automatically a Component or a screen in the prototype.

- Use Auto Layout on this primary Frame. A vertical stack of content groups is the default; choose another supported arrangement only when the actual content requires it.
- Group screens by flow or feature, and components by family. Use nested Auto Layout Frames for rows/groups where needed. Do not create empty headings or empty groups.
- Keep each actual screen as a separate editable Frame with its required device dimensions and internal layout. The outer wrapper organizes the board; it must not stretch every screen to a common width or become the exported product screen.
- Configure padding, gap, and resizing deliberately. Use project tokens where they genuinely apply; board-only presentation spacing may be an explicit one-off value. Do not force canvas arrangement values into product tokens.
- Avoid clipping screens, components, shadows, or variant examples inside the board wrapper. Check actual rendered content and scroll/resize behavior where applicable.
- Component families retain genuine Component Set/variant structures. Do not replace them with ordinary nested Frames to satisfy a wrapper rule.
- Verify prototype starting points, links, screen exports, and component relationships in the hierarchy where content was built. If the selected integration or Figma behavior cannot support a required arrangement without breaking these, report the specific blocker/conflict instead of flattening the screen or claiming success.

For an existing page, reuse its appropriate container if present. A narrow edit does not authorize wrapping or moving the entire existing page. Create the required wrapper for new scoped content without disturbing unrelated layout; migrate existing content only when organization is part of the authorized task. Record any legacy layout outside scope.

## Components and Trash

Place actual reusable main components on the appropriate Components page/container; keep instances in product screens. Search existing libraries first, preserve component IDs and bindings, and do not clone identical components for Provider and Vendor merely because their screens are on different pages. Shared identity ownership remains with `design-identity-manager`.

Trash is recoverable retirement, not permanent deletion. Create it only with the first authorized retired item. Group real archived items in its Auto Layout content container and record their original page, parent, order/position, node IDs, reason, and replacement where applicable. Never classify user-owned content as obsolete without task authorization.

Before moving main components or linked screens, inspect live consumers and prototype relationships. Do not detach instances or break active flows to archive a node. Keep still-used definitions in place until a scoped replacement/migration is completed, or report the dependency. Moving to Trash does not itself eliminate references.

Do not purge Trash automatically. Restoration is a scoped designer operation using the recorded original location, with a current-state check first. Missing original parents require an explicit appropriate destination; do not invent successful restoration.

## Output and Execution Handoff

Return an organization plan keyed by task and revision, with:

- Confirmed Figma file, required surface/role, page name/purpose, existing page ID or `planned` status.
- Real first content item, target container/group, and names to use.
- Reuse/create/move/archive decisions, affected IDs, dependencies, and preservation constraints.
- Required visual and structural checks, including nested screen/prototype/export behavior.
- Parent-first creation order, intended parent for each content root, first real content specification, and operation evidence needed to distinguish in-place construction from later relocation.

The orchestrator stores this plan in the task record; the designer returns confirmed IDs and before/after mappings. Persist actual organization under `design/organization/<file-record-id>.json` using the shared package revision conventions. No additional empty page or asset is needed to store the plan.

If execution fails after creating an empty destination, inspect actual state before retrying. Prefer completing the intended content. Remove a newly created empty page/container only when it is confirmed to belong solely to the interrupted task and contains no user work or dependencies; otherwise record the incomplete state. Never delete pre-existing empty pages as unsolicited cleanup.

## Completion

Every created destination contains real requested content, names distinguish actual product surfaces, content containers use verified Auto Layout, screen/component structures remain native, and archive operations are recoverable. `figma-structure-validation` verifies nodes and mappings; the appropriate visual reviewer opens actual page/container and screen captures. A naming plan alone is not completed file organization.
