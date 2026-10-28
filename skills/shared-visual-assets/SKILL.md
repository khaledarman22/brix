---
name: shared-visual-assets
description: Maintain versioned original reference images, captures, crops, and package manifests shared by research, creative direction, Figma execution, and validation. Use for visual handoffs and verifying that each consumer can actually inspect the same evidence.
---

# Shared Visual Assets

## Contract

Read [references/package-contract.md](references/package-contract.md) when creating or consuming a package. The contract defines shared records and paths; use it rather than inventing a different format for each role.

Maintain a shared store under the active project directory. Register existing evidence in place when possible; do not duplicate `research/evidence/` files merely to change their folder name. New reference assets normally go in `assets/refs/`. Preserve original bytes and create separate crops. Never substitute a generated reconstruction for an original reference.

This skill is a lifecycle service coordinated by the orchestrator. It does not approve references, create a direction, or authorize design changes. Do not create empty stores during skill authoring.

Register production assets from `design-asset-manager` in this same registry with an explicit usage role; store their bytes under `assets/design/` rather than mixing them with reference-only images. Do not create a second competing registry. Use stable links to originals and derivatives; record licensing/provenance and actual inspection separately from eligibility for final placement. Native-vector construction briefs are instructions to the designer, not fictitious image files.

## Register and Preserve

1. Read existing manifests before editing. Assign stable asset and reference IDs; record original source, capture type, dimensions, and version. For local files, calculate a SHA-256 digest using an available tool. Do not invent a digest.
2. Store full-page captures when obtainable and clearly distinguish them from original source images and viewport captures. Record viewport, state, and capture time. Missing full-page views remain unavailable, not reconstructed.
3. A crop records its parent asset ID and version plus its rectangle in parent-image pixels. Verify the crop visually. Retain the full parent image so composition can be understood in context.
4. Use project-relative paths. Preserve stable accessible remote references when local storage is unavailable or prohibited. Record their access limits and observed version; if the underlying content changes, register a new version and invalidate dependent reviews.
5. Keep provenance and known reuse permissions. Reference access does not grant permission to place a third-party screenshot or image in the product. Do not bypass access or media restrictions to populate the store.
6. Never overwrite an asset version used by an active direction. Register a replacement and mark dependent decisions, implementation, and validation as needing review. Do not automatically delete superseded evidence.

## Actual Inspection Gate

A file path, successful download, image dimensions, hash, or JSON entry does not prove that a model saw an image. Each consuming role must load the actual pixels through a vision-capable image input, screenshot tool, or image viewer exposed by its runtime.

After successful inspection, record the role, task/session identifier when available, asset ID/version, time, actual viewing method, and a concrete visible observation. Record an available tool-result reference for traceability, but do not fabricate runtime identifiers. This is an execution record, not cryptographic proof of perception.

The identity manager, creative director, designer, and validator each inspect their relevant assets themselves, even when the same agent performs the roles sequentially. Past inspection does not prove a new session has visual context; reopen the required assets on resume. If the host cannot provide actual images, block dependent visual decisions and report the missing capability. Text-only handoff is not an acceptable fallback.

## Writes and Handoffs

The orchestrator serializes manifest updates, rereads concurrent changes, preserves prior versions, and reads back saved files. Verify referenced paths and image accessibility before handing a package to another role. A receiving host must independently resolve and open the images; the shared folder is not automatic cross-machine synchronization.

The identity manager owns identity records; other specialist roles own their assigned direction, implementation, and validation files; the orchestrator owns shared registry updates. Register assets and their actual inspections before packages reference them. Persist prerequisites first, then the consuming package, then update the project checkpoint. An interrupted sequence is reconciled from saved revisions before continuing; no atomic multi-file transaction is assumed.

Return the package path/version, asset IDs, any unavailable images, and required next inspection. Record these references through `project-memory` and detailed research provenance through `research-memory` without duplicating their state databases.
