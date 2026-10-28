# Figma Integration — Deferred

## Current State

- Status: `deferred-by-user`.
- Selected adapter: none.
- Candidate integrations: the official MCP and the plugin the user will provide later.
- Adapter code, automatic pre-write interception, runtime access restrictions, and integration tests: not implemented.

Do not connect, configure, or select an integration as part of the current skill-authoring work. The presence of other Figma tools in a host does not select them for this agent. Continue writing and reviewing skills; leave integration work pending until the user resumes it.

## Selection When Resumed

Inspect the supplied integrations and choose one at the start of project execution based on the required capabilities and the user's preference. Record its exact identity, target file, supported reads/writes, image export, known gaps, and selection reason in project state. Use that one integration for Figma reads, writes, and exports; ordinary filesystem/image-viewing tools can still handle returned artifacts.

Do not mix the MCP and plugin or silently fail over. If the selected adapter becomes unavailable, stop dependent Figma operations and report the blocker. A user-authorized switch requires reconciling the actual file and pending mutations before continuing. On resume, verify the recorded selection rather than choosing again from scratch.

## Capabilities to Inspect Later

- Create content in a specified parent or attach empty nodes immediately before population; return ordered evidence and confirmed parent IDs. An adapter that only imports completed designs elsewhere for later relocation does not satisfy the required construction workflow.

- Confirm target file/page and read actual node hierarchy and properties.
- Inspect layouts, component/instance relationships, variants/properties, variables/modes, styles, constraints, and resizing.
- Execute scoped native design mutations and return confirmed node IDs and partial-failure information.
- Capture/export actual visuals and support viewing required sizes/states through the selected path.
- Determine whether all writes, including script execution, can pass through one controlled gateway and whether bypass paths can be restricted.

Do not assume either candidate exposes all capabilities. Select based on observed support. Missing required checks remain blocked or unreviewed; never mark them passed because an adapter is official.

## Deferred Enforcement Work

Once the selected interface is known, implement its adapter, supported deterministic rule checks, pre-operation checks, post-operation readback, exception handling, and audit trail. Test partial failures and duplicate-operation recovery. If bypass prevention cannot be enforced, report that limitation and retain evidence-based completion gates without claiming guaranteed prevention.

Until then, `figma-design-standards` and `figma-structure-validation` are instructions and evidence requirements, not executable middleware. No Figma validation or integration compatibility is claimed by completing these files.
