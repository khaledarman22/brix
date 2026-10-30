---
name: figma-structure-validation
description: Supply structural criteria for Brix shared inspection passes, using actual node data without separate mandatory reports or Figma mutations.
---

# Structural Criteria

Follow [Brix](../../AGENT.md) and [Figma Design Standards](../figma-design-standards/SKILL.md). This skill is part of the same scoped before/after pass as visual review, not an installed interceptor or another stage.

Consume current task scope, identity, changed nodes, required sizes/states, exceptions and available actual structural evidence. Reuse covered checks for the same version. Acquire only missing/changed evidence via the selected integration; screenshots do not prove component types, bindings or layout properties.

Within changed scope and direct dependencies:

- Assess applicable FDS-01–14 from actual node configuration, relationships and operation evidence. Preserve unrelated valid checks.
- Compare needed before/after relationships for detach, reparenting, prototype and export changes. Missing historical evidence is unverified, not proof of preservation; do not fabricate it.
- For forms, compare real selected variants/properties with canonical state expectations. Names alone do not prove runtime behavior.
- For mockup shells, check actual fixed radius and clipping per release checks. For organization, inspect nonempty destinations, Frame Auto Layout, real component sets, nested screen/export integrity and authorized recovery records.

Write structural criteria into the single canonical inspection record: rule/target, observed field evidence, outcome (`pass`, `fail`, `not-applicable`, `not-reviewed`, `exception-accepted`), reason and finding ID when needed. Link existing reports if present; do not regenerate a separate report. Required failures/missing checks prevent scoped acceptance.

Return targeted corrections to the designer; do not mutate nodes or identity. Recheck only relevant change, defect or unavailable evidence. Share the same repair counter with visual/image work. A structural pass does not establish visual quality, so the shared pass must also cover required visual criteria.
