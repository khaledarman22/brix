---
name: request-planning
description: Analyze a UI/UX request for Figma and assign the necessary responsibilities to user-designated skills, with scoped tasks, dependencies, and completion criteria. Use before design execution or when feedback materially changes the plan. Not for executing designs, writing skills, or answering general questions.
---

# Request Planning

## Purpose and Boundary

Turn the user's request into the smallest actionable plan that achieves their intended design outcome. Determine what work is needed and map it to the skills the user has designated. Return the plan to the orchestrator for execution.

A responsibility is a piece of work, not necessarily a separate agent. This skill does not spawn agents, execute downstream skills, create missing skills, or modify Figma designs. It may inspect available context through authorized read-only tools. It must not schedule itself recursively.

## Inputs

Use the current request, prior decisions still in effect, available project state, existing design references, and the user-designated skill set. Discover these from the current environment rather than assuming platform-specific paths, tools, or integrations.

When `project-memory` is designated, consume the state it restored before planning. Preserve valid task IDs, decisions, and completed outputs. It is a lifecycle skill managed by the orchestrator, not a design task to add repeatedly to the plan.

For reference research, assign only the needed designated research skills: strategy, discovery, actual visual review, evaluation, and recommendations. `research-memory` supports their lifecycle. Do not add research to a narrow task that does not need it. User-supplied references can skip new discovery after provenance and accessibility checks; visual review remains mandatory before evaluation or recommendation. Keep unavailable visual evidence marked `not reviewed`, never as an assumption that satisfies a design requirement.

Distinguish designated skills from skills merely installed in the host. Use installed skill metadata for discovery, but assign only skills the user has selected or allowed through project instructions. Confirm each assigned skill's instruction source and read enough of it to verify its scope, prerequisites, and output contract before finalizing the assignment.

## Planning Procedure

### Execution profiles

Assign `design-asset-manager` when production imagery/icons are required or a real visual finding calls for an image correction. Separate source selection or edit-package preparation from external execution, return review, designer placement, and in-context visual validation. An initial asset need may precede a screen; an edit triggered by visual review depends on the actual screenshot and finding. Do not send a prompt externally without authorization. Simple native shapes remain designer work. Asset production is covered only within the asset manager's available tools and defined scope; missing generation/edit capability remains explicit.

Organization planning must precede construction. Schedule destination creation together with its first real content as one bounded designer work unit, not as empty scaffolding or a later "move finished designs into containers" task. New screens/components are built inside their intended parents from the start. Scope movement of pre-existing content, Trash archival, and restoration separately. Assign an explicit visual review owner for organization: identity manager for preview boards, fidelity validator for screen boards or organization-only work, and planned in-task visual checks only for simple scoped edits. Each owner views actual board/container captures as well as relevant item detail.

When a request adds product surfaces, pages, screen groups, reusable component families, or scoped archival, assign `figma-file-organization` to plan names and on-demand destinations before the relevant designer writes. It does not execute mutations or decide product scope. Preserve support for multiple Provider/Vendor/etc. apps, websites, and dashboards without automatically creating all of them. Persist planned destinations without creating empty pages. Organization can proceed from known requirements alongside research; actual mutations still require the selected adapter and scoped design inputs.

Apply `figma-design-standards` as shared rules, not a new design phase. Assign scoped `figma-structure-validation` for every mutation task, including foundation previews and narrow edits; its result and the applicable visual checks are both required for completion. A small edit may use sequential roles within one task, but cannot omit structural evidence. Respect the deferred adapter selection in [the integration contract](../../FIGMA_INTEGRATION.md).

- **Research only:** finish after the requested shortlist/handoff. Do not create a direction or Figma design unless requested.
- **Reference-led design:** use the research outputs, creative direction, implementation, and validation stages needed for the request.
- **Narrow edit to an existing design:** assign `figma-designer` a scoped change brief containing the exact requested change, confirmed target, constraints to preserve, and acceptance checks. The designer captures and views the existing target as the visual baseline. No research or full creative direction is required unless the edit changes the direction materially. The implementation mapping and validation may reference this brief instead of a direction package; never invent an external reference. A simple text change may include verification within its execution task; consequential visual changes require the validation skill.

Persist the scoped change brief as a stable, revisioned task section in project state or a project artifact and pass its exact location to consumers. These profiles do not waive actual visual inspection.

For an existing project, assign scoped visual inspection and exact token/style/component collection to `design-identity-manager` before creative direction. Reuse valid identity records; do not force a whole-project audit for a narrow edit. For a new project, sequence director draft → manager identity proposal → designer foundation preview → manager visual review/adoption → director finalization → screen implementation → final visual validation. Represent these as distinct tasks so the initial draft does not depend on its own adopted identity. The preview uses the proposal; final screen execution uses the adopted revision. Full brand strategy, product research, and a comprehensive design-system library remain outside these scoped responsibilities unless separately covered. Production assets are assigned to the designated asset manager within its actual tool capabilities.

For reference-led execution, map selected references to `multimodal-creative-director`, its direction package to `figma-designer`, and actual outputs to `visual-fidelity-validation`. `shared-visual-assets` preserves the same inspectable images throughout; it is a lifecycle dependency, not a new design phase. Include image access and each role's actual inspection as prerequisites. Reuse valid packages for targeted repairs and do not require a new creative-direction cycle for every minor edit. Missing vision or Figma capability blocks dependent work, not unrelated planning.

Route foundation-preview outputs to the identity manager, not to final screen validation. Route identity extensions through a separate proposed revision, isolated preview, and manager adoption; keep the current adopted identity usable for unaffected work. If changing shared variables/components is required, plan an explicit affected-consumer migration scope. The director owns composition, the manager owns identity values, and the designer alone performs design-node writes. Validation requests that need node mutations become scoped designer tasks rather than permission for the validator to edit.

### 1. Establish the requested outcome

Extract:

- The requested change or deliverable and why it is needed, when known.
- The affected product, flow, screens, components, and Figma target when provided.
- Explicit constraints such as device sizes, language, RTL, brand rules, accessibility requirements, and requested order.
- Existing work that can be reused, and boundaries that must remain unchanged.

Do not invent audiences, product requirements, research findings, or design decisions. Label reasonable working assumptions. Ask only about missing information that changes scope or prevents a necessary step. An unknown Figma target need not block provisional planning, but must remain a prerequisite for operations on that target.

### 2. Inspect relevant context

Use existing project records and supplied references first. When an existing Figma design is relevant and accessible, verify the connection and intended target, then inspect only the structure needed to scope the request. Record confirmed references rather than invented node IDs.

If the design cannot be inspected, distinguish known facts from unverified assumptions. Make inspection a prerequisite for tasks that depend on the current design. Do not claim that existing components, styles, or states have been checked.

### 3. Identify the necessary responsibilities

Choose responsibilities because the requested outcome needs them, not because a role exists. Possible responsibilities include understanding requirements, examining existing UX, researching references, defining flows and states, interpreting brand rules, defining reusable foundations, sourcing assets, composing Figma screens, and reviewing results.

These are examples, not a mandatory pipeline. Reuse established decisions and foundations. A narrow change can be one execution task with verification included. Do not add separate research, branding, design-system, or review phases unless their outputs are actually needed.

For every responsibility, identify its concrete deliverable and why the request requires it. Merge tasks that have the same scope and no useful handoff between them. Split tasks when they require different skills, inputs, ownership, or completion evidence.

### 4. Assign skills and dependencies

- Map each task to an exact available, designated skill and its verified instruction source.
- If several skills overlap, follow the user's explicit choice; otherwise choose the narrowest suitable designated skill and briefly explain a consequential choice.
- If no designated skill covers a responsibility, mark it as `missing-skill`, describe the required capability, and leave the skill assignment empty. Do not invent a skill name as if it were installed or assign specialized work to the orchestrator as a workaround.
- Reserve `orchestrator` ownership for coordination, preparing handoffs, and tracking results.
- Make prerequisite outputs explicit. Dependencies must refer to real task IDs and form an acyclic sequence.
- Mark tasks as eligible for parallel execution only if their inputs are independently available and their write scopes do not overlap. Eligibility does not authorize subagents or require parallel execution.
- Preserve user-specified ordering. Surface conflicts with necessary dependencies before the affected work begins.

### 5. Return an executable plan

Use the existing project planning format if one is defined. When `project-memory` is designated, return the plan to the orchestrator for saving in `PROJECT_STATE.md` through that skill, or in the existing authoritative system referenced by the checkpoint. Do not create a separate competing plan file. Otherwise return a concise plan in the conversation and persist it only when the project workflow requires it or resumption benefits from it.

Include a brief objective, scope, confirmed context, relevant assumptions, and any questions or missing capabilities. For each task provide:

| Field | Required content |
| --- | --- |
| ID | Stable identifier within this plan, such as T1. |
| Responsibility | The work needed and its purpose. |
| Scope | Specific screens, components, files, or other resources affected; identify unresolved targets. |
| Assigned skill | Exact skill name and instruction source, `orchestrator` for coordination, or empty when missing. |
| Inputs | Required request details, references, and upstream outputs. |
| Dependencies | Prerequisite task IDs, or none. |
| Deliverable | Concrete output and its intended destination when known. |
| Completion criteria | Observable evidence that this task achieved its purpose. |
| Readiness | `ready`, `waiting-on-dependency`, `needs-input`, `missing-skill`, `needs-connection`, or `needs-capability`, with the reason when not ready. |

Use short task blocks or a table according to readability; a single task can be a compact block. Where several blockers apply, list all of them. Identify the next runnable task or independent tasks and explain what resolves any blocked branch.

Keep planning and execution status distinct: a completed plan does not mean its design tasks are completed. If a blocking question is outstanding, return a provisional plan and continue planning independent branches. Do not add a general approval gate; the orchestrator may proceed with already authorized, ready tasks.

## Feedback and Replanning

When feedback arrives, compare it with the current plan. Update only affected tasks and their dependents. Preserve task IDs, valid outputs, and completed work where possible. Mark outputs that became stale and explain why. A small change within an existing task does not require rebuilding the entire plan.

## Completion Check

Before handing the plan back, verify that:

- Every task supports the user's request and has a concrete output and completion criterion.
- Every assigned skill exists, is designated for use, and covers the assigned responsibility.
- Missing skills, unknown targets, and unavailable connections are explicit rather than hidden by assumptions.
- Dependencies are valid, have no cycles, and permit a clear next action when requirements are available.
- Scope and write ownership are unambiguous enough for execution; proposed parallel tasks do not conflict.
- No design execution, Figma mutation, or creation of extra skills occurred during planning.

## Calibration Examples

- **Change a button label in a known frame:** one task using a suitable designated Figma editing skill, including verification of the text and layout. No new research or design-system phase.
- **Design a login screen in an established product:** determine required states, use existing foundations, compose the screen, and verify it. Combine these responsibilities when one designated skill covers them; do not assume separate agents are needed.
- **Design a dashboard without a designated design skill:** scope the required output and record the missing capability. Do not invent an installed skill or start drawing as a fallback.
- **Update one screen after feedback:** revise that screen's task and any dependent verification. Preserve unrelated screens and completed research.
