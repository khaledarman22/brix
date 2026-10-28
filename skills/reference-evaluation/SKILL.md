---
name: reference-evaluation
description: Evaluate and rank visually reviewed UI/UX references at page and component level, remove duplicates, and balance fit, quality, and observed diversity. Use after visual review; unviewed material cannot receive a passing evaluation.
---

# Reference Evaluation

## Contract

Input: research requirements, candidate records, visual review evidence, project feedback, and exploration mode.

Output: an explained ranking and coverage matrix, candidate decisions, duplicate groups, and research gaps. Return results for persistence and `reference-recommendations`.

## Evidence Gate

Open the visual evidence for any visual judgment you make. Existing reviews help locate evidence but do not replace viewing it. Exclude unavailable or unreviewed candidates from approved rankings. Reject or flag a candidate for a required property that has not been reviewed; do not silently score unknowns as good or bad.

Record your actual inspections against the pinned shared asset versions through `shared-visual-assets`. Eligibility is scoped to the proposed use: a reviewed hero may qualify for hero composition even when the reference's mobile view is not reviewed, but it cannot qualify as evidence for mobile behavior. Keep those coverage gaps explicit.

Source evaluation and reference evaluation are separate. Source provenance and accessibility affect traceability; source popularity does not establish reference quality.

## Evaluation

- Evaluate requirement fit, visible composition, hierarchy, typography, spacing, color treatment, observed states, and relevant component quality.
- Evaluate a page and its sections separately. A weak page may contain a useful reviewed component; record the exact usable part and exclusions.
- Assess visible distinctiveness relative to the reviewed candidate set. Do not claim global originality or authorship from appearance.
- Record directly demonstrated functions only. Visual evidence cannot prove engineering feasibility or general user experience outcomes. If implementation feasibility is required, label it `not reviewed` here and return that gap for a separately authorized implementation review.
- Use descriptive ratings (`strong`, `adequate`, `weak`, `not reviewed`) with evidence and reasons. Follow user-specified priorities; otherwise prioritize requirement fit, visual quality, and useful diversity in that order. Do not invent numerical measurements or precise objective scores.
- Remove exact duplicates using provenance and confirmed matching content. Compare actual visuals for near-duplicate compositions and record the concrete repeated features. Do not discard a distinct reference solely because its subject is similar.
- Semantic or visual similarity tools may assist grouping when actually available. Record the method and real output; never invent embeddings, similarity percentages, or a computed ranking. Tool suggestions require visual confirmation. Without them, explicitly use qualitative comparison.
- Rerank to preserve high quality while reducing redundant compositions. Include alternatives that visibly differ in relevant ways. Do not select a weaker unrelated reference just to meet a diversity quota.

## Output

For each evaluated reference include its ID, whole-page or partial-use scope, criterion ratings and evidence, acceptance or exclusion reason, and any required condition not reviewed. Distinguish evaluator decisions from the user's acceptance.

Map each requested component or section to its best reviewed candidates. Report uncovered requirements, duplicate groups, and coherent alternative directions supported by actual visuals. If coverage is insufficient, return focused gaps for more discovery within the remaining budget. At the limit, report incompleteness rather than approving insufficient results.

Report counts from actual records: discovered, visually reviewed, eligible, excluded, and duplicate candidates. If reporting a duplicate rate, state the numerator and denominator. Describe diversity using observed differences, not invented quality metrics.
