---
name: project-memory
description: Persist and resume Brix task state with canonical references and changes only; not for skill authoring or ordinary conversation.
---

# Project Memory

Follow [Brix's documentation and inspection policies](../../AGENT.md). Use `PROJECT_STATE.md` in the calling project, not the skill folder. If an authoritative task system already exists, keep only an index to it. Do not create state for ordinary conversation or skill authoring.

## Restore

Read existing state before editing; confirm project identity and reconcile newer concurrent changes. Recover task IDs, current decisions, artifacts, integration selection/deferred status, blockers and next action through their canonical links. Do not replay completed work or re-inspect unchanged available evidence just because a session resumed.

An unfinished external operation has uncertain outcome: inspect only its affected live resources before retrying. Preserve known results and mark unavailable verification, rather than resetting the project or inventing past success.

## Store once

Keep project identity/path; objective and genuinely new constraints; one task row per responsibility; links to canonical decisions, research, identity, assets, implementation and shared inspections; and a concrete next action. Task rows own execution status: `pending`, `running`, `completed`, `blocked`, `failed`. Readiness is separate. Do not mirror status, coverage, decisions, review verdicts or asset details in summary sections.

A task links exact consumed revisions and outputs. New facts belong to their owner; research stores selection, registry stores assets, inspection record stores findings. The checkpoint does not copy them. Organization and asset requests likewise remain canonical elsewhere. No chronological milestone transcript is required.

Before an external mutation, keep intent, target and success-recovery method if they are not already recorded in the task. Resolve it from actual tool results. Save only real changes at meaningful boundaries, not on every handoff, resume or final response. Use real timestamps only for actual changes.

The orchestrator serializes shared writes, preserves unread/unrelated data, and confirms changed records persisted. Retain consumed history through the existing version store, not repeated full copies. Resolve inconsistent task rows against actual evidence; never blindly mark complete to match prose. Persistence failure blocks dependent mutations/handoffs whose outcome would be lost, while independent read-only work may continue. Never save secrets.

## Completion

Resolve required task evidence and findings once; unchanged available shared passes are reusable. Link the actual output and remaining next action, or mark the task complete only when its scoped criteria passed. A complete research or implementation step alone is not accepted design. Report unsaved progress honestly if persistence fails.
