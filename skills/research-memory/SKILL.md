---
name: research-memory
description: Resume and persist an existing Brix research-and-selection record without creating another report or inspection stage.
---

# Research Memory

The selection schema and ownership live in [reference-research-selection](../reference-research-selection/SKILL.md); persistence rules live in [project-memory](../project-memory/SKILL.md). Use those already-loaded instructions, not another research pipeline.

On resume restore exact task, selections, rejected uses, executed routes, counters and next missing area. Keep existing authoritative records in place; if memory is only an index, store links. Legacy candidate states remain readable: `candidate`, `reviewed`, `eligible`, `excluded`, `unavailable`, `stale`. These do not require separate stage writes.

Persist genuinely new batch results or feedback to the canonical record. Preserve consumed revisions and confirmed prior evidence, mark only affected invalidations, and do not reset budget or replay completed searches. Return location/revision plus new context only. Persistence failure blocks its dependent handoff without fabricating saved progress.
