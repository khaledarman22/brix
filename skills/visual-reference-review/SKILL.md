---
name: visual-reference-review
description: Inspect actual reference images and rendered pages to review visible UI composition, sections, responsive views, and demonstrated states. Required before a reference can be evaluated or recommended; never substitutes textual descriptions for visual inspection.
---

# Visual Reference Review

## Evidence Rule

Every finding must come from actual visual inspection. Do not infer unseen behavior, hidden states, responsive layouts, font identities, spacing values, implementation quality, or usability outcomes. Source descriptions, markup, metadata, and another agent's prose do not replace viewing the visuals.

Use `not reviewed` for anything that could not be observed. A reference with no inspectable visual content is ineligible for approval. A reference with only a desktop image may support observations about that image, but cannot support claims about mobile behavior or interactions.

## Contract

Input: candidate records, accessible original images or rendered pages, and the requirements being reviewed.

Output: an evidence-linked review for each inspected candidate, including full-page observations, component observations, strengths, weaknesses, coverage, and unreviewed items. Return it for persistence and `reference-evaluation`.

Use `shared-visual-assets` to pin every viewed asset version and record the reviewer's actual inspection. For newly supplied references, register the images before review. A live page must have an inspectable capture or explicit observed version/state; later consumers must not unknowingly inspect changed content.

## Inspection

1. Open and view the actual image or rendered page. Record the source, capture or image reference, inspection time, viewport or image dimensions when known, and visible state. Inspect full-page context and relevant details; do not evaluate the whole page from a hero thumbnail.
2. Review visible layout, grid relationships, typography, color relationships, spacing, alignment, hierarchy, components, and sections. Describe concrete visible facts. Do not invent precise CSS values, font names, or numerical contrast ratios from appearance.
3. Review the whole page and individual requested elements independently, including hero, navigation, cards, typography, color treatment, and layout where present. Tie each strength or weakness to its visible location and the requirement it affects.
4. For responsive review, actually inspect relevant viewport sizes or supplied size-specific designs. Record the sizes and visible differences. One screenshot cannot establish responsiveness. Missing sizes remain `not reviewed`.
5. For interaction review, observe the actual transition and rendered resulting state in a safe, authorized context. Record action, before/after evidence, and observed result. Do not submit forms, make purchases, or alter external data merely to inspect a reference without authorization. Static images do not prove interactive behavior.
6. Accessibility observations are limited to what was visibly reviewed, such as clipping, visible focus, or hierarchy. Do not claim full accessibility compliance, measured contrast, keyboard support, or usability-test results without the appropriate direct checks.

## Review Record

Use candidate ID and include:

- Evidence references and exact page regions or components reviewed.
- Visible observations, separated by full page and relevant sections.
- Specific strengths and weaknesses with supporting evidence.
- Observed viewport sizes and interaction states.
- Required areas covered, and explicit `not reviewed` entries.
- Parts suitable for consideration and parts with visible conflicts with the brief.

Keep evaluative observations grounded in what is visible. Do not turn them into claims about conversion, performance, unseen functionality, or engineering feasibility. Reviewers receiving only prose must open the visual evidence themselves before making new visual judgments.

## Completion

Each finding can be traced to a viewed visual and a visible element. Images remain accessible through recorded references for subsequent evaluation and design handoff. If capture access fails, preserve the incomplete status rather than filling gaps with assumptions.
