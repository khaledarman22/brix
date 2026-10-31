---
name: reference-board
description: Present cached UI references and their evaluations on a reusable References page in Figma, with stable labels and selectable regions. Use to create or update a reference board, not to apply a design to product screens.
---
# References page in Figma

Use [the shared store](../reference-search/references/store-contract.md), the existing reference captures and evaluations. Load the applicable Figma operation skills before tool calls. Do not rerun search/evaluation when the stored evidence already covers the request.

## Destination and capability

Resolve the actual target Figma file from the user or project records. Inspect the current tool capabilities and destination. Reuse the mapped References page or an unambiguous existing equivalent; otherwise create a page named `References` in the target Design file. Do not create a different Figma file or reorganize unrelated pages without the user's request. If the destination is ambiguous, ask only which file/page.

Before writing the board, verify a supported way to insert the real cached images. Use the connected tool's documented image/import capability; do not invent a local-path-to-Figma image API or assume network fetch works inside use_figma. If image import is unavailable, keep the catalog and report the blocker. Text-only cards or empty image rectangles do not fulfill presentation. Use the applicable platform skill standards for native editable layout and labels; imported reference screenshots may remain raster images.

## Board contents

Organize a section per requested screen/region. Each card contains:

- Stable letter and reference ID, a useful title, and source link.
- A legible actual image with preserved aspect ratio. Long references may use labeled region crops linked to the full source image; avoid illegible thumbnail-only boards.
- General quality verdict (strong/mixed/weak/unreviewed) with a reason, separate brief-fit ratings, a short reuse suggestion and a caveat. Label unevaluated items honestly; do not fabricate scores to fill the layout.
- The selected regions and rationale, labeled as Brix's choice or an explicit user choice; preserve user comments separately.

Use native editable frames/text and readable sizing. Keep images and optional crop frames individually addressable. Let the user point to an image, select a crop, draw an annotation, or describe a region in chat. Distinguish screenshot bounds from card padding when mapping annotations onto an image. Record actual Brix selections as designer decisions, never as user approval; do not fabricate selections or quotes.

## Update without duplication

Look up saved file/page/card/image IDs and reuse intact cards. Verify IDs refer to the right reference/version before updating. Patch changed metadata or add missing cards only. Do not clear/rebuild the page on every request, move the user's annotations, remove rejected cards automatically, or rename stable labels after selection. If several pages or cards could be the intended destination, resolve the ambiguity instead of deleting duplicates blindly.

After a coherent board update, inspect its visible result for loaded images, readable labels, clipping and meaningful comparison. Save confirmed node mappings and the presented status. Record the chosen regions and continue to product-screen execution under the project policy; the board is evidence, not a mandatory question. Include its link when useful for explaining the result. Wait only if the user explicitly asked to select before execution, and do not poll while waiting. Preserve prior explicit choices without asking again.
