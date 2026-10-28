---
name: multimodal-creative-director
description: Inspect actual reference images and project identity to create a coherent, executable visual direction package for a Figma designer. Use after reference selection; never make reference-based design decisions from descriptions alone.
---

# Multimodal Creative Director

## Mandatory Rule

Never make visual design decisions based solely on textual descriptions of references. Always inspect the actual visual assets. Preserve visual references throughout the entire design pipeline, and ensure the implementation agent receives and can inspect the same reference images.

Read [the shared package contract](../shared-visual-assets/references/package-contract.md) and follow `shared-visual-assets` for registration, versioning, and inspection records.

## Inputs

Consume the Visual Reference Package, original images, available full-page captures and section crops, visual analyses, user requirements, and existing identity/tokens/components. Confirm the package revision and open the actual required images yourself, including full context around selected crops. A prior review or a list of paths does not satisfy this requirement.

Inspect the project's visual identity examples as well as authoritative token/component records when available. If identity is missing, mark it explicitly; do not invent an established identity. A new identity may be proposed only within the user's authorized design scope, with its status clearly recorded. Ask only when the missing choice blocks meaningful direction.

For an existing project, consume the scoped identity record from `design-identity-manager` before choosing the direction, open its visual examples yourself, and preserve its adopted rules. A reference with a different palette may inform composition without replacing project colors. Route unresolved identity conflicts to the manager.

For a new project, produce an initial `draft` direction first, marking identity as not yet established. Send the proposed treatments to `design-identity-manager` for formalization and visual review of a foundation preview. After adoption, finalize the direction as `ready` pinned to the exact adopted identity revision. The manager's record is authoritative for identity values; the direction must reference it rather than maintain a conflicting token catalog. Proposed additions to an existing identity follow the same manager-owned change process.

## Build the Direction

1. Compare the observed references against requirements and identity. Choose a coherent direction within the authorized scope, or prepare alternatives if requested or a material unresolved choice requires the user. Do not add an automatic approval gate.
2. Assign exact reference regions to specific decisions: hero composition, navigation structure, card rhythm, or another visible quality. Preserve access to the same original assets for the designer.
3. Resolve conflicts across reference typography, density, spacing, color, and component treatment. State which rule wins and why it fits the project's identity. Do not assemble unrelated parts without a common visual system.
4. Define layout, composition, hierarchy, required sizes, state rules, and how typography and spacing roles apply to each section. Reference observations describe only what was actually seen. New responsive behavior and composition choices are authored design decisions, not claims about unseen reference properties. Proposed identity-wide scales, colors, or component treatments go to the identity manager for formalization.
5. Reference existing tokens, styles, and components by their semantic names and confirmed IDs from the pinned identity. In a draft, identify requested additions as proposals. In a ready direction, resolve them to the adopted identity instead of defining a competing token table or overriding identity values locally.
6. Describe intended differences from the references, what must remain invariant, and the validation evidence required. Respect original image usage terms; reference screenshots are inspiration, not default product artwork.
7. Save the Visual Direction Package using the shared contract and return its path/revision, selected asset versions, and unresolved decisions. Keep the original visual package reachable through it.

## Completion

Identify required production assets by purpose, section, intended composition, and target proportions when known. Route them to `design-asset-manager`; reference screenshots are not automatically licensed production imagery. Keep source-reference decisions distinct from production asset choices, and record space/crop/text-clearance requirements needed by the designer and image editor.

The direction is more than a written concept: it links inspectable images and regions to concrete rules, identity constraints, tokens, and implementation instructions. Its director inspection records exist, the original images remain accessible, and the designer is instructed to open them independently. If relevant images cannot be viewed, mark the affected direction blocked rather than replacing evidence with prose.

An initial new-project draft can complete its planning task while identity is still proposed. It authorizes only the already scoped foundation-preview work, not final screen execution. A ready direction for final execution pins an adopted identity with actual visual evidence for the required scope.
