---
name: research-strategy
description: Turn a scoped UI/UX reference-research task into a varied search strategy with coverage targets, exploration mode, and bounded effort. Use before discovering references or when results require a new direction.
---

# Research Strategy

## Contract

Input: the task from `request-planning`, explicit user requirements, supplied references, and project-specific exploration history from `research-memory`.

Output: a research brief containing the objective, required screens or components, constraints, coverage targets, search routes, mode, budget, and stopping criteria. Return it to the orchestrator for persistence and execution. Do not perform design work or claim that planned searches have run.

## Procedure

1. Extract the actual goal, task type, requirements, keywords, exclusions, and missing information. Reuse confirmed project context. Do not invent product needs. Ask only when a missing detail materially changes the search; otherwise keep it explicitly unspecified.
2. Identify the sections or components that need references. Avoid searching for a complete product when the request concerns one element.
3. Load past queries, explored sources, rejected references, selected directions, and feedback for this project. Retain excellent relevant references while avoiding repeated unproductive routes.
4. Choose the mode requested by the user, or use `Consistent` by default and state that choice:
   - `Consistent`: prioritize verified fit and quality, rechecking useful previous references.
   - `Explore`: expand source and visual-direction diversity while preserving requirements.
   - `Evolve`: build on a confirmed previous direction. If none exists, ask which direction to develop.
5. Build several materially different search routes using product context, task intent, component names, layout concepts, and relevant terminology. Vary combinations rather than changing one adjective. Source categories can include live products, portfolios, case studies, galleries, and documented component examples. Do not restrict discovery to famous domains.
6. Define coverage and a bounded budget. Follow the user's limits; otherwise start with up to 12 queries, 30 unique candidate pages, and 8 deep visual reviews. Aim for 3 sources when useful and available, but do not make this a minimum that overrides early stopping. The numerical limits are ceilings, not quotas. A narrow component request may need much less. Record any deliberate adjustment before using it.
7. Define sufficiency: each required area has at least one visually verified suitable reference, with a distinct alternative for consequential choices when available. Never force diversity at the expense of requirements. Stop earlier when coverage is sufficient, or at the budget limit with an honest gap report.

## Adaptive Search

If results are weak, change a query route, source category, or direction within the remaining budget. Preserve the original goal. If the budget is exhausted, return uncovered requirements and a proposed extension rather than searching indefinitely or lowering the verification standard.

Do not require approval for routine search changes within the authorized scope. Record the routes and limits so a resumed session continues the same research rather than restarting it.

The budget belongs to the research task across retries, routes, and resumed sessions. Count actual executed queries, unique candidate pages inspected, and unique candidate versions deeply reviewed; log failed calls separately. Reopening a pinned image for another role's inspection does not consume a new candidate review, but still requires actual viewing. Do not reset counters by starting a new route or run. A user-imposed cap requires their authorization to increase; a self-selected limit can be revised with an explicit reason and new finite cap recorded before further work.

## Completion

The brief identifies what to search for, what counts as sufficient, how to vary the search, and when to stop. Planned visual directions are search hypotheses only, never findings about references that have not been viewed.
