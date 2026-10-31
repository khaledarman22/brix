---
name: reference-evaluate
description: Evaluate visually inspected UI references for a specific design brief, saving explained ratings and reuse suggestions. Use to compare candidate references; use contextual fit to select references autonomously while preserving explicit user choices.
---
# Evaluate reference suitability

Use [the shared store](../reference-search/references/store-contract.md). Work from cached captures and the brief. Reuse an evaluation for the same image version and requirements revision; do not research or inspect the same unchanged evidence again merely to produce another report.

Only rate what has actually been inspected. If the capture is unreadable or missing, leave scores null and mark what evidence is needed. A static screenshot cannot establish working accessibility, responsive behavior, usability success or conversion rates.

Rate each dimension from 1 to 5 with a short observation:

| Criterion | What to judge |
|---|---|
| Task and content fit | Does the pattern support this screen's purpose, amount of content and main action? |
| Hierarchy and layout | Grouping, scan order, emphasis, spacing and alignment visible in the capture |
| Type and visual clarity | Readability, visible contrast concerns, text density and consistency |
| Platform and adaptation | Fit to the target device/content/RTL; clearly separate observed behavior from inferred adaptability |
| Identity compatibility | How easily the useful composition can work with this product's existing tokens and components |

Anchors: 1 = poor fit requiring a fundamental change; 3 = useful with stated adaptations; 5 = strong fit supported by visible evidence. Use the intermediate values consistently. Do not manufacture precise decimal scores or claim these are objective measurements. Prefer a criterion breakdown plus a plain recommendation over an opaque aggregate. Unknowns stay unknown and do not become zero.

For each useful reference, identify the specific regions worth taking and the limitations/parts to avoid. A weak full-page fit can still contain a useful table, card, header or form. Record this at region level rather than rejecting the entire image. References with the same layout are alternatives, not evidence of broader coverage.

Assess how the useful principles support or extend the saved project composition language. Reject stylistic drift even when a candidate looks attractive alone; record intentional user-requested exceptions. Store the evaluation in the catalog. The Figma board can display compact scores, one main strength and one caveat. Choose the most suitable inspected regions based on the brief, platform, content, existing screen continuity and identity, rather than mechanically taking the highest score. Record the selected regions and rationale as Brix's decision, separately from the user's liked/rejected selections, and proceed within the requested design scope. An explicit user choice takes precedence even when lower-rated.

## Quality versus fit versus user taste

Save reusable intrinsic visual quality with `cache.py review`: verdict `strong`, `mixed`, `weak` or `unreviewed`; scores 1–5 (or null) for layout, typography, spacing and visual_clarity; concrete strengths/weaknesses, useful/avoid regions, actual inspection time and visual evidence. This answers “is this reference good or weak, and why?” without pretending taste is objective. For an eligible public capture, store this general review in the shared catalog; private captures remain local. Keep the source URL and version on the reference record. Reuse the same version's review across projects; re-review only for changed evidence or an identified assessment error.

Project fit uses the brief-specific criteria above and stays in local evaluations. User likes/rejections and their exact words stay in local selections. Never copy a brand-specific fit rating, client's preference or choice into general shared quality. A visually strong reference can be a poor fit for this project, and a weak page can still contain a useful region. Do not globally blacklist a reference because one user rejected it for one brief.

Do not delete weak references automatically: their recorded reasons prevent repeatedly fetching and proposing the same unsuitable options. Search may return them as known weak candidates; inspect reasons and reuse only a specifically useful region or changed evidence. The board should show a short general-quality verdict and a separate suitability assessment, followed by the source and main reason. Uninspected references remain unreviewed, never “bad” by default.

## Platform and domain eligibility

Apply platform eligibility before scoring: mobile app to mobile app, website to website, desktop application to desktop application, unless the user explicitly allows a cross-platform reference. Uncertain platform needs verification; a high aesthetic score cannot compensate for a mismatched platform. Classify the product shown, not the gallery hosting it or the viewport alone.

Business category is not an eligibility gate or an automatic score penalty. A flower-store brief may use fashion, grocery or other ecommerce references if the screen's user task, content structure and interaction fit. Explain fit through those properties, not shared subject matter. Keep domain-specific needs such as delivery slots or bouquet customization from the actual brief; adapt a reference only where it supports them.
