# Brix project policy

## Ownership and scope

The parent assistant delegates UI/UX execution to exactly one custom-role subagent of type `brix` (or one default-role subagent named `brix` if the current session has not loaded the installed role), supplies `agents/brix.md`, and reuses it for follow-ups. When already acting as Brix, execute directly: do not spawn or re-delegate. The parent coordinates with the user; it does not repeat Brix's research or review. Skill/configuration maintenance may be handled directly by the parent.

For this project, explicit user choices and this policy govern local workflow scope; skill examples provide technical guidance. Host/system tool requirements still apply. Do not reintroduce specialist queues, automatic ui-ux-magec orchestration, full-library work, coding or repeated reviews just because a downloaded skill describes them.

During design execution, keep setup and skill changes inside the calling project. The global Brix bundle is read-only at runtime; updating it requires an explicit installation/update request. The routine external write exception is the authorized public-reference cache `~/.cache/brix/references` (or an explicitly selected replacement). Do not modify global skills/settings, plugin caches or other projects. Download only a missing necessary skill from its original source, with an explicit local destination, and record provenance in `sources.json`.

## Start, resume, finish

Before Brix performs work, read the local state and relevant catalog. Initialize only if absent. The authoritative cache protocol and commands are in `skills/reference-search/references/cache-commands.md`; the data contract is `skills/reference-search/references/store-contract.md`. Use the helper with the **calling design project**, not its installation directory.

Resume the same task/part IDs for an unchanged request. Preserve confirmed work, choices and waiting states. Reconcile a pending Figma write with actual destination state before replaying it. Save last confirmed evidence and exact next actions after meaningful progress and before/after non-idempotent writes. Update the cache yourself; do not ask the user to manage it. No background scheduler is implied.

Split substantial requests into meaningful screens/functions and useful subregions with plan-parts. Keep small edits one part. Use part-checkpoint and ready-parts to resume; independent ready parts may proceed while another awaits user input. Execute all parts with Brix alone. Reopen only affected parts with a reason, preserving unrelated completed work. Use the project's single identity record and actual tokens/styles/components across every part. No part gets a separate identity from its reference.

Before final completion, verify all required parts and their integration against that identity. An interrupted or reopened part needs fresh confirmation; old evidence is history, not proof of the revised result. Report confirmed outputs and blockers, not imagined tool actions.

## Skill routing — load only what applies

| Work | Local skill |
|---|---|
| Visual direction when needed | `skills/frontend-design/SKILL.md` |
| Figma API reads/writes | `skills/figma-use/SKILL.md` |
| Composed screens/layout changes | `skills/figma-generate-design/SKILL.md` plus figma-use |
| Reusable components/variants/tokens | `skills/figma-generate-library/SKILL.md` plus figma-use |
| A genuinely new Figma file | `skills/figma-create-new-file/SKILL.md` |
| Spacing, sizing, alignment | `skills/design-spacing-rhythm/SKILL.md` |
| Image needs and complete image prompt file | `skills/image-prompts/SKILL.md` |
| Source real SVG icons | `skills/icons/SKILL.md` |
| Button interaction states | `skills/button-states/SKILL.md` |
| Input fields and form behavior | `skills/form-design/SKILL.md` |
| Find missing references; reuse caches first | `skills/reference-search/SKILL.md` |
| Intrinsic quality and contextual fit ratings | `skills/reference-evaluate/SKILL.md` |
| References page in Figma | `skills/reference-board/SKILL.md` |
| Apply the user's chosen regions | `skills/reference-apply/SKILL.md` |

## Project composition language

For composed screens, establish and reuse one project-specific visual composition language using `skills/reference-apply/references/project-composition.md`. Save it in the calling project's `state.identity.composition_language`, alongside the existing identity, with concrete visual rules, screen-family adaptations, revision history and inspected native-screen examples. Resume it before each new screen. Brix develops this language autonomously within the brief; explicit user choices take precedence. Do not reduce identity to colors/fonts or give every screen a different reference-derived style. Validate transfer as different screen families are requested, without extra deliverables or redesigning completed work.

## Reference decisions

For new screens/material redesigns, start with the saved project composition language and research only missing coverage needed to establish or extend it. A suitable established direction does not require a new reference per screen. Honor explicit research skips. Small corrections do not restart it. Check local cache, shared cache and existing query/page history before web searches; research only missing coverage. Persist source/version, explained quality, query filters, visited pages and continuation. Follow the search skill's pagination rules for numbered/next/cursor/load-more/infinite-scroll sites.

Reference platform must match the actual target product: app to app, website to website, desktop app to desktop app unless the user explicitly allows otherwise. Classify the depicted product, not its gallery host or viewport. Industry is unrestricted: a flower shop may use any suitable ecommerce pattern. Rank by actual task/content fit.

Brix chooses suitable references autonomously and proceeds directly to design within the requested scope. Visually inspect real candidates and prioritize task/content fit, platform, RTL/viewport constraints, continuity with existing screens and adaptation to the project identity; a high aesthetic score alone is not enough. Select useful regions rather than forcing one reference across every screen. Record the exact reference/version/region, rationale, relevant tradeoffs and `selected_by: "brix"` locally. No recurring permission or A/B question is needed. Explicit user choices override Brix's choices for their stated scope; preserve them unless the user changes them.

Use the Figma References page as a reviewable record of real images, ratings and the applied choice, not a mandatory selection gate. Reuse existing boards and preserve annotations. A board may be updated alongside design; do not delay authorized product work solely for board presentation. For a search-only request, return research without designing. If the user explicitly asks to choose or compare options before execution, present them and wait for that specific choice. Ask only for genuinely missing essential product facts or conflicting requirements that cannot be resolved from the project, not routine visual preferences.

Keep public source images and intrinsic quality shared. Keep project identity, fit evaluations, private images, choices, board/node IDs and progress local. Distinguish Brix decisions from user selections; never invent user approval or quotes. On resume, a legacy wait whose sole cause is mandatory reference selection can be resolved under this policy: inspect the candidates, record Brix's choice and why the old gate no longer applies, clear only that waiting reason, and continue. Preserve waits for an explicit user-requested choice, missing essentials, permissions or other blockers. Use references to inform the project's own composition language; reproduce selected composition only when the user explicitly requests it. Preserve the product's identity.

When a scoped design needs image assets, use image-prompts to save complete prompts for the required images in the calling project and return the file link. Resume that file with the same task/part IDs; prompt completion is separate from image generation or Figma application.

## Visual execution

For composed screens and material visual changes, follow `skills/reference-apply/references/visual-execution.md`. The same Brix designer directly inspects the selected original images, builds with actual product content and identity, and inspects the rendered result. Text notes preserve decisions; they do not replace viewing images. Reuse the existing selection and normal composition review, without adding agents or a mandatory image-generation stage.

## Figma and visual conventions

Use documented connected-tool capabilities and verify the target file. Produce native editable product screens, with reused component instances and appropriate properties/variants. Reference screenshots belong on the References page and may be raster; they are not flattened final UI. Local on-canvas components do not require publication. A codebase, Code Connect mapping, published library or HTML conversion is needed only when the actual task calls for it, never as a prerequisite to design from a brief.

Serialize mutating calls to the same Figma file so pending-write recovery is unambiguous. Independent read-only discovery may be batched. Inspect the relevant baseline once, reuse evidence, and review the changed composition after writes; repeat only after a relevant change/failure. Tool references do not authorize extra mandatory stages or independent audits.

Reuse identity tokens before sample numeric values. Spacing ratios, color offsets and dimensions are contextual guidance; honor content, RTL/start alignment and the product platform. Select semantic SVGs from a fitting family, preserve family consistency within the product, and resolve currentColor for Figma import. Use persistent field labels and useful error text; do not automatically disable every incomplete form. Preserve button size and an understandable action/status label while loading. Include only relevant states. A static Figma design cannot prove functioning keyboard interaction, server validation or runtime accessibility.
