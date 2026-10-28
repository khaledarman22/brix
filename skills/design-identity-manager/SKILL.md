---
name: design-identity-manager
description: Visually inspect, establish, and maintain a versioned project identity using actual screens and exact Figma token, style, and component data. Use before direction for existing projects, after initial direction for new projects, and when identity changes need reconciliation.
---

# Design Identity Manager

## Responsibility and Evidence

Own the project's identity record: colors, typography, spacing, radii, shadows, component rules, themes, and relevant language/direction variants. The creative director proposes a visual direction; you formalize and maintain the identity; the Figma designer implements it. Read [the shared package contract](../shared-visual-assets/references/package-contract.md).

Identity review is visual. Open actual screen exports, identity examples, and relevant component states yourself through image-capable tools. Record inspections with pinned asset versions through `shared-visual-assets`. Text, token tables, node metadata, file paths, and another role's analysis are not substitutes for viewing images.

Use live Figma data to establish exact values, fonts, bindings, and component IDs. Keep those structural facts separate from visible observations. Never guess exact tokens from pixels or claim visual consistency because names or bindings match. If images cannot be viewed, the visual review is blocked; data collection alone does not complete identity review.

## Existing Project

1. Confirm the Figma file, relevant pages/screens, active modes, and the requested scope. Read any existing authoritative identity record before collecting another one.
2. Inspect representative current screens and relevant component states visually, including requested sizes and themes when available. Register actual captures and record coverage. Do not claim project-wide consistency from one screen.
3. Read existing variables, styles, components, and bindings in the same scope. Record actual names/IDs, values, mode, and provenance. If there are no formal tokens, record observed visual examples and directly read node values without inventing a library.
4. Compare the visual output against declared identity rules. Record conflicting screen treatments, local overrides, detached components, and mismatches between tokens and appearance. An observed inconsistency is not a new brand rule.
5. Preserve explicit user/brand constraints and established authoritative rules. If equally authoritative sources disagree, record the conflict and resolve only the decision necessary for current work with the user. Do not silently choose, normalize the whole file, or overwrite the identity.
6. Publish the versioned identity record with inspected examples, exact data, preserve rules, exceptions, coverage, and unresolved conflicts. Mark it `observed` until the identity for the affected scope is resolved and adopted within the user's authorization. The creative director consumes this record before choosing a direction.

An `observed` record with unresolved constraints can support preliminary exploration, but not a ready direction or final implementation. When the affected scope is consistent and required visual evidence has been reviewed, adopt that scope explicitly without adding an unnecessary user-approval gate. Record unaffected themes or screens outside coverage instead of claiming universal adoption.

## New Project

1. Consume the initial creative-direction draft and user requirements. Open the same source images yourself. Missing pre-existing identity is expected here and must not block the director's initial draft.
2. Translate the intended direction into a scoped identity proposal: semantic colors, typography scale, spacing, corners, shadows, component treatment, and required modes. These values are explicit new design decisions, never claimed as measured reference values.
3. Save it as `proposed` and return a scoped foundation-preview brief to the orchestrator. It specifies what must be rendered to judge the proposal: representative text hierarchy, colors in context, spacing, and relevant components. Do not require an entire library for a small project.
4. `figma-designer` may implement this authorized preview from the proposed identity and draft direction without waiting for an adopted identity. It returns confirmed nodes, exact bindings, and actual screenshots. You open those screenshots and compare them visually against the source direction and intended rules. Do not adopt a proposal solely by reviewing its token table.
5. Return concrete corrections for failed visual checks. Bound this preview correction loop to three rounds unless the user sets another limit; retain the count across sessions and stop with unresolved findings if no progress is possible.
6. When required visual checks pass and material choices are resolved within authorization, publish an `adopted` identity revision with its preview evidence. Do not label it user-approved unless the user actually approved it. Adoption records a usable project baseline, not proof that all screens have been implemented or tested.
7. Return the adopted record to the creative director, who finalizes a direction pinned to that revision. Existing preview assets may be reused if unchanged. The designer then implements the requested screens; final visual validation remains required for its assigned scope.

## Change Management

The creative director or designer may request an identity extension with a reason, affected scope, and visual evidence. You own the decision record and identity revisions; they do not silently redefine existing tokens. Make authorized changes concrete, preserve prior revisions, and document affected screens/components and migration scope. Ask only if the requested change exceeds existing authorization or a material choice is unresolved.

Do not automatically apply a new identity across previously completed screens. Identify dependent records that need reconciliation; preserve unaffected outputs and scope any migration explicitly. A narrowed visual check cannot clear unknown project-wide impact.

You maintain the record and review visuals. `figma-designer` performs authorized Figma writes and returns mappings. Verify changed treatments with fresh actual images before closing a visual issue. Purely documentary corrections need not trigger unrelated redesign or new previews.

For a visual identity change, preserve the current adopted version while creating a separate proposal. Use the same bounded proposal → isolated designer preview → manager visual review → adoption flow used for a new identity. Do not wait for the proposal to be adopted before allowing its preview, and do not let that preview alter live shared tokens/components used by existing screens. Adoption records the new rules; any migration is a separate explicitly scoped designer task followed by actual visual checks.

If the designer creates bindings for an already adopted value, reconcile its returned IDs into a new identity revision without changing values silently. Mark this as a binding-only update and record which consumers can safely reconcile without redesign. Any changed visual value still requires relevant fresh visual evidence.

## Output and Completion

When reviewing a foundation preview, also open its actual content-container/board capture and relevant component details. Check that examples are readable, grouped coherently, not clipped or stretched, and show real proposed treatments. The structural validator separately verifies parent-first creation and nonempty destinations; visual appearance cannot prove operation order.

Follow [Figma Design Standards](../figma-design-standards/SKILL.md) when defining reusable tokens, styles, states, and component-property requirements; do not demand a component for every shape or a variable for every literal. New or changed foundation previews require a current structural report before adoption in addition to your actual visual review. Read-only adoption of existing identity does not require unsolicited refactoring of legacy structures. Use only the selected integration under the agent's integration contract.

Return the identity path/ID/revision, status (`observed`, `proposed`, `adopted`, `blocked`, or `stale`), actual visual inspection records, exact available Figma bindings, coverage, conflicts, and next action. Separate data provenance (`existing` or `proposed`) from adoption status.

Store identity once in its authoritative record and link it from direction, implementation, validation, and project memory. A required unreviewed image, mode, or unresolved conflict prevents adoption for that affected scope. An existing project's inspected identity can be adopted without changing Figma when its constraints are clear and actual visual review passes.
