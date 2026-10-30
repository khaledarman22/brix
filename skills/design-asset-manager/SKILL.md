---
name: design-asset-manager
description: Source and prepare Brix production assets and English image-edit packages, preserving provenance and shared scoped verification.
---

# Design Asset Manager

Follow [Brix](../../AGENT.md), [record fields](../shared-visual-assets/references/package-contract.md) and [release checks](../figma-design-standards/references/visual-release-checks.md). Production assets do not satisfy UI-reference coverage. The designer places assets; this skill owns source/edit requests, not identity or design-node writes.

## Source

Consume the actual asset need: target, purpose, composition/aspect ratio, formats/transparency, text-safe area, identity and acceptance criteria. Reuse suitable supplied/project assets. An explicit internet sourcing request uses real sources, not unsolicited generation.

- Required product photos use actual supplied/official/authorized photographs. A conceptual UI may use suitable real stock photos labeled illustrative, never as verified inventory. No geometric, icon or generated substitute for required product photos.
- Decorative illustrations/backgrounds may use licensed sources or an available authorized generation tool. Identify source and known usage terms; popularity is not permission.
- Icons use the existing coherent family where suitable. Simple editable geometry belongs to the designer, not unnecessary bitmap generation. Inspect externally sourced SVGs for unwanted content.
- Preserve originals and product details; explicitly request/verify alpha when needed. Label generated content and derivatives accurately.

Evaluate actual candidate pixels once through the shared evidence policy; reuse available evidence. Register source, terms, dimensions, actual hash where available and version. Keep finite sourcing budget/counters in the request and stop on sufficient fit or a real limit. Asset search is separate from UI-reference search.

## Place or edit

For source-placement, keep one request with target, selected asset link, necessary specs, search resume point and canonical acceptance link. No edit prompt is needed if placement works. The designer places the asset and the normal after pass checks changed context. An isolated approved asset is `candidate-approved`; only verified actual placement is `placed-verified`.

If a concrete pixel defect needs editing, link its shared finding/source/context capture and prepare an English prompt. Layout/crop/mask fixes remain designer work. Required edits block affected final placement; optional improvements do not block already met criteria. Temporary previews remain labeled temporary.

The request links accessible originals, actual target capture/node when available, preserve/change/avoid constraints, identity, output dimensions/format/alpha, placement/text clearance, expected return and acceptance criteria. The prompt identifies editable source versus context, describes the actual correction and preserved product details, and states deliverable specs. Do not invent dimensions, findings, context screenshots or generic edits unrelated to the issue.

The prompt is stored once at `design/asset-requests/<id>-prompt.md`; the request is canonical for state. An optional `PROMPTS.md` contains links only. Preserve the exact dispatched revision. Dispatch to another person/agent/service only when explicitly authorized and supported; preparing a package does not grant permission. Pass existing actual inspection evidence and images; a recipient inspects only changed or unavailable scope, not merely because it is another role.

## Prompt files and final delivery

For every image-generation or image-edit prompt actually prepared, keep the reusable English prompt and an image-input section in the same canonical prompt file. Include clickable links to each exact input image, labeled by purpose: editable source, visual reference, or design/placement context. Identify which source each instruction applies to. Link actual images/captures, not only a gallery page, search result, asset ID or prose description. Keep original source-page attribution as an additional link when relevant; do not copy the full asset registry.

Use an accessible direct image URL or a clickable absolute local file path in the current host. Preserve stable asset/version links for portability and resolve paths from the calling project at delivery time; never hardcode the skill-installation folder. Disclose local-only access, expired links or missing inputs. Do not fabricate a public URL or upload private images merely to obtain one. A generation prompt with no image inputs should say so instead of inventing references.

Before final delivery, confirm the prompt file and input links resolve using available current evidence; this is a link/file check, not another visual inspection. Repair missing links within scope or report the precise gap. The final response gives the saved prompt location and a clickable link. For multiple prompts, use `PROMPTS.md` as a links-only index to the individual canonical files, each retaining its own image-input links. Do not duplicate prompt bodies in chat or the index. Clearly distinguish a prepared prompt from images still awaiting generation, editing or placement.

## Return and completion

Tie actual returned bytes to request/source revisions. If context changed, reconcile affected scope before use. Register the derivative and check its changed pixels/technical requirements once. Reject unwanted product alterations, artifacts, missing transparency or unmet treatment. Designer placement changes context, so its normal scoped after pass checks integration, crop and legibility using the same shared findings. Do not repeat unchanged source inspection.

Use the contract's request states and real dispatch/receipt events. Prompt-only tasks end at a verified ready package, not dispatch or placement. Required image fixes share the originating repair counter; standalone edits use Brix's default limit. On resume check actual request state before resending. Preserve canonical links in project state rather than copying request details.
