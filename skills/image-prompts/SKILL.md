---
name: image-prompts
description: Write complete, copy-ready image generation or editing prompts for the images a Brix design needs, save them in a project file, and return its clickable link. Use when planning image assets or when the user requests image prompts.
---
# Image prompts for the design

Brix performs this work itself. Use the current brief, selected references, existing identity and saved part state; do not restart research. Cover each distinct image needed by the scoped design, including hero images, product imagery, backgrounds and illustrations. Reuse one image ID for the same asset used in several places. Source SVG icons with the icons skill; do not replace them with generated raster images.

Read the saved project composition language and its image-direction rules/visual anchors. Carry its framing, medium, lighting, crop and relationship to text into each prompt; do not invent a new art style per screen. Record the language revision used with prompt progress. Follow [project composition](../reference-apply/references/project-composition.md) when the direction needs establishment or revision.

## Write a complete prompt per image

Use a stable ID such as IMG-001 and record its purpose, screen/part and intended placement. Distinguish new generation, editing an existing asset, and reuse of an existing final image. For reuse, link the actual asset and preserve any known original prompt; do not invent its provenance. If a replacement is needed, write a clearly labeled replacement prompt.

Write the copy-ready prompt in English by default, with user-facing explanations in the user's language. Honor an explicitly requested prompt language. Every prompt must stand alone: repeat the relevant visual identity and concrete requirements rather than saying “same style as above.” Include:

- Subject, count, appearance, action, environment and relevant product details.
- Intended visual medium and treatment: photograph, illustration, 3D or other brief-appropriate style; materials, textures and level of realism.
- Composition, viewpoint, framing, focal hierarchy, subject position, background and negative space for the actual UI text placement, including RTL when applicable.
- Lighting, shadows, palette and mood grounded in the project's existing identity. Keep a coherent art direction across images without making every composition identical.
- Aspect ratio, intended display dimensions, crop-safe area and background transparency when needed. Describe these as requirements, not guaranteed tool capabilities; avoid arbitrary resolutions or lens jargon unrelated to the result.
- Exact visible text only when needed, including its language/spelling; otherwise keep UI headings, buttons and logos out of the generated artwork so they remain editable in Figma.
- Concrete exclusions relevant to this asset, such as extra objects, unsuitable cropping, unwanted lettering, watermarks or visual clutter. Integrate these into the prompt without relying on a tool-specific negative-prompt field.

For edits, identify the exact input asset/link and state what changes and what must remain unchanged, including product geometry, identity and framing. List required attachments beside the prompt. Do not claim to have inspected an unavailable image; mark missing inputs and draft assumptions explicitly. Never manufacture product details that require a real photo; retain that dependency.

Use a fenced text block per prompt with all visual instructions included. Put technical attachment paths and usage notes beside it. Avoid filler such as “best quality, 8K” as a substitute for actual direction. Do not leave template placeholders in a delivered prompt; if a critical input is missing, clearly mark the entry as a draft and ask only for that input while completing independent entries.

## Save, resume and deliver

Write a UTF-8 Markdown file at `deliverables/image-prompts/<stable-task-id>.md` inside the **calling design project**, never inside the installed skill. Include a compact index of image IDs, placements, generation/edit/reuse mode and readiness, followed by the full prompts. Use one file per task with all its parts; create distinct aspect-ratio variants only when the composition needs them. If no imagery is needed, report that fact rather than creating filler prompts.

Read any existing file before updating. Preserve user edits and unaffected prompts; update only changed image needs, keep stable IDs, and mark superseded versions clearly when needed. In the existing task/part checkpoint, record the relative file path, image IDs, confirmed prompt progress and the next action using the canonical cache protocol in [cache-commands](../reference-search/references/cache-commands.md). Prompt drafts and private asset paths stay project-local, never in the shared public-reference catalog. A saved prompt is not a generated image or an applied Figma asset; track those separately and do not mark dependent design work complete just because prompts exist.

Before returning, verify the file exists, every required image has an entry, and each ready prompt can be copied independently. Always include a clickable absolute file link in the response, e.g. `[برومبتات الصور](/absolute/project/deliverables/image-prompts/task-id.md)`, and briefly flag missing inputs. This is a local file link, not a public URL. Writing this file does not itself require generating images, uploading it or publishing a share link.
