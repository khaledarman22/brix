---
name: reference-search
description: Find and cache real UI design references for Brix, reusing previously inspected references before searching again. Use for reference discovery or filling missing reference coverage, not for applying a selected design.
---
# Reference search and reuse

Work as the single Brix designer. This skill owns discovery and the shared reference store, not evaluation, Figma presentation or design application.

Read [the shared store contract](references/store-contract.md) before changing records. All four reference skills use a shared public-reference cache plus a separate project catalog/checkpoint store. Read [cache commands](references/cache-commands.md) when operating them. Use only the designated shared cache outside the project; never modify global skills/settings or another project.

## Reuse before searching

Read the saved project composition language first. Research only a specific missing principle or screen-family pattern; do not choose a fresh style for every screen. Derive a compact brief from the user's requested screen/region: purpose, platform, content needs, viewport, language/RTL and existing identity constraints. Record unknowns as unknown; ask only when needed to choose relevant references.

Resume from the project checkpoint first. Search the local catalog, then the shared cache by purpose, region, layout pattern and platform. Adopt useful shared captures with the cache helper instead of downloading them again. Read existing evaluations and user choices. Reuse a suitable cached version even across sessions; a new turn or role is not a reason to browse, download, evaluate or present it again. A reference can suit several screens, but suitability ratings belong to their specific brief. Do not re-offer a rejected choice for the same brief without new relevant evidence or a user request.

Search online only when the user requests fresh examples or the cache lacks suitable coverage, a required image is unavailable, or relevant requirements have changed. Search the uncovered region, not the whole product again. Start with a small diverse set; stop when meaningful options cover the request instead of chasing a fixed quota. Use real product pages, public case studies or reputable design galleries; prefer original sources and distinguish concept shots from shipped products. Match interaction/content needs, not merely industry labels.

## Capture and identify

Open and visually inspect the actual reference through available browser/image tools. Search thumbnails or text snippets alone are unverified candidates. Do not invent screenshots, URLs or observations. Save permitted screenshots/images locally with their source URL, capture context and content hash. Record the original product/source where traceable and keep gallery URLs separately. User-provided images need no artificial web source.

Deduplicate using the canonical source + viewport/state and image hash. Strip known tracking parameters but preserve functional query parameters. Different screen states from one URL may be separate captures. Add a new asset version when the actual image changes; do not overwrite a version already cited by a user selection. Record visually similar candidates as related instead of adding duplicate cards.

If a source is blocked, keep its access status and use an accessible alternative. Do not repeat the same failed fetch without a reason. An unavailable live URL does not invalidate a usable cached capture. A reference is inspiration, not automatic permission to reuse its brand assets in the finished design.

Save public reusable captures to the shared cache and adopt needed copies locally; private captures stay local. Save the current brief, fit evaluations and progress checkpoint only in this project. Save a brief summary of coverage. For design requests, continue with reference-evaluate, select the best-fitting inspected regions under the project policy, record Brix's rationale and proceed to reference-apply. Use reference-board as a reviewable record, not a selection gate. Wait only when the user explicitly requested to choose before execution. For an explicitly search-only request, stop after discovery. Do not create approvals or specialist agents.

## Maintain the cache while working

Brix owns cache maintenance as part of doing the task; do not ask the user to save records or remind you. Read checkpoint, catalogs, quality reviews and prior search history before browsing. Save each completed search page's results and continuation token, each inspected capture's provenance, and each evaluation/choice as it becomes known. Save successful Figma writes and the next action at meaningful boundaries. Keep source URLs, image hashes and ratings tied to the actual captured version. No cache record should claim an inspection, successful import or approval that did not happen.

For the same unchanged request, reuse matching cached results, quality reviews and local evaluations, and resume the recorded next action instead of repeating the search or asking for an already-recorded selection. Shared search history covers public queries only; private queries, briefs and user feedback stay local. A shared search marked covered means its earlier search stopped with enough candidates, not that every future project is satisfied. Assess its saved results against the current brief before browsing further. The helper supplies persistence; Brix must invoke it during work, not run a background job.

## Pagination is part of reference research

Inspect the source's actual navigation: numbered pages, next links, cursors, Load more buttons or infinite scrolling. Never assume the first page is the entire collection. Use observed URLs/tokens and supported browser tools; do not invent page endpoints, bypass access limits or declare exhaustion from a failed load.

Use the `search-log` helper described in [cache commands](references/cache-commands.md). Key history by source, normalized query and filters (including sort/category/platform where relevant). Check local history and then eligible public shared history before requesting a page. Record each successfully visited page/batch, its returned reference IDs, the next observed continuation and outcome. For scroll/load-more sessions, store a stable batch marker and enough local navigation context to resume; if the session/cursor expired, re-open only the necessary listing route, skip already-seen item IDs and do not re-capture or re-rate unchanged items.

Continue into later pages when coverage is missing; stop once suitable options cover the request or the user/search budget limits are reached. Distinguish covered, genuinely exhausted, blocked, failed and paused states. Save a continuation even when coverage is already sufficient, so a later request for alternatives can continue. For genuine exhaustion record visible evidence such as an absent/disabled next control or an explicit end response. An empty transient batch is not proof of the end. Detect repeated page tokens or repeated item batches and pause/recheck navigation rather than loop forever. Respect retry-after/rate limits; do not retry failed pages automatically on every turn.

Public-source history may be shared across projects, but keep session cookies, credentials and private/signed cursor URLs out of that cache. Such continuations belong in local state or must be re-established through the browser. Stale routes or changed sort/filter settings require a new/revised search context, not reuse of an unrelated cursor.

## Platform match, cross-industry relevance

Match the reference's actual product platform to the target: mobile app designs use mobile app screens; websites use website screens; desktop applications use desktop application screens. A responsive website viewed on a phone is still a website, not evidence of a mobile app reference. A gallery website may host app screenshots: classify the depicted product, not the site hosting the image. Verify the platform from the source and visible evidence; mark uncertain candidates unknown and do not present them as matched. Cross-platform references require an explicit user instruction for that scope.

Industry is not a required match. For a flower shop, search ecommerce patterns from any retail category when they support the same task: product discovery, categories, product detail, cart, checkout or delivery. Search primarily by platform + user task + screen/pattern + content needs, not only by the client's business niche. Transferable hierarchy and behavior matter more than matching flowers, fashion or electronics. Keep the user's actual product requirements; do not import another industry's requirements just because its layout is useful.

Include target platform and relevant screen/task in saved search filters so app and website searches do not share a continuation accidentally. Filter both local and shared candidates by verified platform before ranking. Reuse cross-industry references when content density, navigation and action structure fit; note concrete adaptations rather than penalizing a different industry by itself.
