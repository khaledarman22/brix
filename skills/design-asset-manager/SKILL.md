---
name: design-asset-manager
description: Prepare production images, backgrounds, product photos, icons, and vector assets, and create image-edit handoffs with original images, actual placement captures, and English prompts. Use for design asset needs or visually identified asset corrections; does not write Figma nodes or send work to another agent without authorization.
---

# Design Asset Manager

## Responsibility and Inputs

Consume the asset requirement from planning, creative direction, or an actual visual-review finding. The director defines purpose/composition, the identity manager defines visual identity, you prepare the asset, and `figma-designer` places it. The relevant visual reviewer checks the result in context.

Read [the shared package contract](../shared-visual-assets/references/package-contract.md). Use `shared-visual-assets` for stable IDs, versions, provenance, and actual inspections. Production assets are separate from inspiration references. This skill does not change the identity or mutate Figma nodes. Any Figma reads/captures use the single selected adapter; connection work remains deferred.

For each asset need record the intended use, target screen/section, confirmed node ID when available, dimensions/aspect ratio, placement/crop, required formats, transparency, text-safe area, identity revision, and acceptance criteria. Unknown facts remain explicit. A new asset need may be planned before its target exists; a review-triggered correction requires the actual affected capture and finding ID.

## Select the Asset Route

1. Inspect available project assets and approved sources first. Reuse a suitable original rather than create needless duplicates.
2. For real products use supplied or approved authentic product photography. Preserve product shape, labels, branding, and material details in edits. Do not pass off generated imagery as a photograph of the user's real product. Illustrative placeholders must be explicitly identified and cannot satisfy a required authentic-product asset.
3. For expressive backgrounds and illustrations, source suitable licensed imagery or generate it when an actual authorized tool is available. Check the actual source and usage terms; search-result snippets or popularity do not establish reuse rights. Record unknown terms and do not promote an unlicensed reference screenshot into a final product asset.
4. For icons, inspect the project's existing set first. Prefer reusable vector assets from one coherent family, preserving license/attribution requirements. Do not mix unrelated stroke/weight systems without a direction decision. The designer creates their actual Figma components/instances.
5. For simple geometric shapes and editable treatments, return a native-vector construction brief to the designer instead of rasterizing or generating an unnecessary bitmap. External SVGs must be inspected and checked for unwanted content before use.
6. For composites or cutouts, retain originals and separate layers when useful. Request alpha transparency explicitly when needed; verify returned transparency through file data and actual viewing rather than trusting the prompt.

Open candidate pixels yourself before selecting them. Preserve their source, creator/usage terms when known, real dimensions, and hashes for local files. Keep source assets unchanged; register every derivative as a new version with parent links and edit provenance. If a tool is unavailable, prepare a truthful handoff or record a blocker, never invent generation or download success.

## Image-Edit Handoff for Another Agent

When actual visual review identifies an image problem or missing image, inspect the source image and target capture yourself. Choose a suitable editable source when needed, then prepare a package at `design/asset-requests/<request-id>.json` and its reusable English prompt at `design/asset-requests/<request-id>-prompt.md`.

The package must include:

- Original source asset IDs/versions and actual accessible image files, not descriptions alone.
- Actual screenshot of the intended placement, relevant detail crop with parent link, Figma node ID if confirmed, and screenshot/implementation revision.
- Review finding ID, observed problem, desired correction, and scope. Do not invent that review requested an edit.
- Identity/direction references and the actual visual identity examples needed for the edit.
- What to preserve, what may change, and what must not be introduced.
- Output dimensions/aspect ratio, format, alpha requirements, crop/subject placement, text-safe region, and any required variants.
- The exact prompt location, inspection requirements, expected return path/format, and acceptance criteria.

Write the prompt in English using concrete values from the brief and observed images. Name which attached image is the editable source and which is layout/identity context. Describe the actual edit, subject placement, background treatment, lighting/style, preserved product details, and text clearance as applicable. Do not add text/logos unless explicitly required. Do not prescribe generic edits that contradict the observed problem.

A prompt should follow this structure, omitting irrelevant clauses:

1. Edit the identified source image for the specified placement; identify the attached context capture.
2. Describe the visible problem and required transformation.
3. Specify preserved subject/product details and forbidden changes.
4. Specify project appearance, subject placement, crop, and clear area for UI text.
5. State exact deliverable specifications and checks for success.

Resolve blocking specifications before marking the package ready. Unknown dimensions are not silently invented; an explicitly authored size choice may be recorded when within scope. A target not yet rendered can support a provisional initial-generation brief, but cannot masquerade as a visually verified placement-edit request. Ask the designer for a real capture when an existing design must be reviewed.

Confirm all referenced images are accessible. Require the receiving agent to open them through actual vision inputs or image-viewing tools. A path or prompt alone is insufficient. Preparing this package does not authorize sending messages, spawning a worker, or uploading images to another service. Give the user the package to use, or dispatch only under explicit applicable authorization. Record `awaiting-external` only after the handoff is actually made, not just prepared.

## Returned Image and Placement

1. Receive the actual output and tie it to the request revision and original source version. If the target or identity changed meanwhile, mark the request stale and reconcile before use.
2. Preserve the original. Register the output as a derivative with provenance, dimensions/format, and a real hash where available. Check technical requirements and open the actual image yourself against the original and requested changes. A successful tool response is not visual acceptance.
3. Reject visible unwanted product changes, lost details, unwanted text, artifacts, wrong crop, or an unmet requested treatment. Return a specific corrected prompt/package revision when a further edit is warranted.
4. A satisfactory isolated image is `candidate-approved`, not final. Give the designer the pinned asset version and exact intended node; the designer places it in the existing target without rebuilding the screen outside its container.
5. Obtain a fresh screenshot from the actual placement. The assigned visual reviewer opens it with the original finding and identity examples, checking crop, integration, text legibility, quality, and required sizes. Mark `placed-verified` only when those checks pass and the node mapping is confirmed. Required structural checks for the Figma mutation still apply.

Image changes share the originating scope's repair budget when they fix a validation issue. Do not reset the counter by switching between image edits and Figma placement. For a standalone asset request use up to three correction rounds by default, recording progress and stopping on exhausted limits or no meaningful improvement.

## State and Completion

Request states: `draft`, `ready-for-handoff`, `awaiting-external`, `returned`, `candidate-approved`, `placed-verified`, `blocked`, or `stale`. Record actual dispatch/receipt separately. If the user asks only for a prompt/handoff, completion is the checked ready package; it does not require or imply dispatch or placement.

The asset manager owns asset requests and prompt files; the orchestrator updates shared asset/project records. Save only real artifacts when executing, not empty request folders during skill authoring. Link the request, source/output assets, original finding, target, and next step in project memory so another session can continue without recreating the brief.
