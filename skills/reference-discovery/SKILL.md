---
name: reference-discovery
description: Find real UI/UX reference candidates across sources and result pages, verify their destinations, and collect provenance and accessible visual material. Use with a research brief; does not approve references or replace visual review.
---

# Reference Discovery

## Contract

Input: a research brief, remaining budget, and prior discovery records.

Output: candidate records with stable IDs, real URLs, provenance, accessible visual references, and discovery status. Return records to the orchestrator for `research-memory`; route eligible candidates to `visual-reference-review`.

## Discovery

- Use available search and browsing tools. If access is unavailable, record the blocker; never invent sources, results, URLs, titles, or screenshots.
- Search different sources and follow relevant result pages or pagination within the budget. Do not treat the first result page or source ranking as a quality ranking.
- Record query, source, result page or cursor, and discovery time. Resume from recorded progress instead of repeating completed searches.
- Open candidate destinations to confirm that they contain the referenced work. A search snippet or title can support initial relevance filtering, but cannot support visual evaluation or approval.
- Collect the original title, creator attribution when available, canonical source URL, and the actual images or live page that can be inspected. Record missing data as unknown.
- Obtain suitable screenshots or accessible image references when supported. Preserve original visual access for later reviewers. Do not substitute generated imagery for the discovered reference or bypass access restrictions.
- Before visual review, return the acquired assets for registration through `shared-visual-assets`. Pass stable asset IDs and versions with each candidate so review evidence pins the actual images from the start, not only at final recommendation.
- Assess source facts separately: provenance, creator attribution, access availability, and any observed content mismatch. Fame is not a quality criterion. A source can contain both strong and weak references.
- Filter obviously unrelated results cheaply. Normalize URLs and detect exact duplicates before expensive review. Visually similar but different candidates require actual visual inspection before grouping.
- Switch routes or sources when results are weak. Request a revised strategy from the orchestrator if needed; honor the remaining budget.

## Candidate Record

For each candidate record: ID, title, source URL, creator if known, discovery query and page, discovery time, target requirement, image or capture references, access limitations, and the canonical state defined in `research-memory`. Use `candidate` for items awaiting visual review, `unavailable` for inaccessible content, and `excluded` with a reason for duplicates or unrelated content. Link duplicate IDs. A requirement match at this stage is provisional.

Record image access and known usage terms separately. Being useful as inspiration does not establish permission to reuse an image in the final design.

## Completion

Return the actual candidates and search coverage, not just a list of domains. Include searched routes, unvisited routes, remaining budget, and access failures. A reference that cannot be visually inspected remains unapproved and cannot enter the final shortlist.
