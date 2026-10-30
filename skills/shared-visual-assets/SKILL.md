---
name: shared-visual-assets
description: Register and share actual image versions and scoped inspection evidence without duplicate assets or per-role inspections.
---

# Shared Visual Assets

Use [the record contract](references/package-contract.md) for fields and locations, and [Brix](../../AGENT.md) for inspection/documentation policy. This is shared storage support, not an additional phase or approval authority.

Register existing evidence in place. Store new reference images under `assets/refs/` and production assets under `assets/design/` when needed. Preserve originals. Source registration, successful download and dimensions do not prove inspection.

Assign stable IDs and byte versions with actual provenance, dimensions, source/usage terms, and SHA-256 for local bytes when available. Never invent metadata. A changed image gets a new version; a new task link or metadata update does not invalidate unchanged image evidence.

Crops/annotations are optional when needed to communicate a selected region. Use parent ID/version and actual source-pixel bounds; validate dimensions, nonnegative coordinates and nonzero in-bounds area. Do not create identical crops for whole-image references. Inspect only newly created or changed derivative scope using the shared policy; reuse the original inspection. Generated substitutes never count as original reference pixels.

Record actual observers and scoped evidence once. Consumers use those inspection IDs, not fabricated personal reviews. If the prior inspection is unavailable, acquire only missing scope. Do not force each role/host to reopen an unchanged asset merely at handoff.

Before a dependent write, resolve the required asset/version and evidence links. Reuse unchanged validated metadata; if bytes/access changed, check the affected entries. Keep missing evidence blocked without fabricating history. Serialize shared registry writes and preserve consumed revisions; owners keep identity, research and request status in their own records. Return IDs/location/revision only, plus genuinely new context.
