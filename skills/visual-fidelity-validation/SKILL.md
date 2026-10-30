---
name: visual-fidelity-validation
description: Supply changed-scope visual and composition criteria for the single Brix after pass, reusing available evidence across roles.
---

# Visual Criteria

Follow [Brix](../../AGENT.md) and [Visual Release Checks](../figma-design-standards/references/visual-release-checks.md). Use the same canonical inspection record as structural checks. Do not require another observer, full-page audit, intermediate-layout check or separate visual report.

## Basis

Use the scoped change brief and inspected baseline for simple edits. For new screens use mapped ready reference coverage, application decisions and adopted identity. Confirm current selected versions and scoped rejections through existing records. Missing historical UI research is not a defect for a simple edit.

Reuse available actual visual evidence for the same scope/version. When a pass is needed, compare relevant baseline/reference and changed output at readable scales; do not infer viewing from export paths or prose. Changed requirements, a defect or unavailable evidence permits only a targeted repeat.

## Within the shared after pass

Check affected massing, proportions, alignment, whitespace, focal/action order, density and content balance against declared application decisions. Correct labels and attractive styling do not excuse materially wrong composition. Distinguish justified adaptations from drift; do not accept a rewritten plan solely because it matches an already failed result.

Check changed controls against shared component treatments, typography, colors and state semantics. Different reference sources do not justify fragmented button/input systems. Check scoped readability, clipping, locale/RTL, required sizes and form-state consistency. Consume actual structural results without repeating their ledger. Static images do not prove interaction/backend behavior; keep those limitations explicit.

Record only new findings with ID, affected region/node, expectation, actual observation, evidence, required correction and state (`open`, `fixed-awaiting-review`, `resolved`, `blocked`). Store findings once; other records link them. Required observed defects mean `needs-fixes`; required inaccessible evidence means `blocked`. Do not fabricate similarity metrics or approval.

The designer repairs nodes; identity conflicts return to its owner. Inspect only repaired scope under Brix's shared repair budget. A missing intermediate-layout record is not a finding. Acceptance consumes the current shared pass rather than performing it again.
