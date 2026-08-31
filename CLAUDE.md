# CLAUDE.md — Starlight Publishing Engine

## Repository role

This repository is the strategy, contract-design, canonical editorial source, and evaluation surface for the Starlight Intelligence Institute publishing system.

The production runtime will be extracted into a dedicated `starlight-publishing-os` monorepo after contract acceptance and a passing golden release.

## Authority boundaries

- GitHub: prose, semantic MDX, diagrams, prompts, schemas, tests, fixtures, code.
- Supabase/Postgres: sources, snapshots, claims, verification events, graph edges, workflow projections, approvals, receipts, metrics.
- R2: immutable snapshots and release binaries.
- Trigger.dev: long-running production orchestration.
- Notion, Linear, and Google Drive: projections; they cannot overwrite canonical Git or Supabase state.

## Required operating sequence

1. Commission a bounded intent and canonical URL.
2. Build a primary-source research pack and immutable snapshots.
3. Extract versioned claims and independent verification events.
4. Lock the claim set.
5. Draft semantic MDX from only the locked pack.
6. Run factual, editorial, code, citation, search, accessibility, rights, and render gates.
7. Build an immutable ReleaseManifestPayload.
8. Canonicalize and externally hash the payload.
9. Obtain a human ApprovalEvent for the exact hash.
10. Render and publish mandatory formats/channels idempotently.
11. Store PublicationReceipts and run smoke tests.
12. Monitor claims, search, completion, conversion, cost, and freshness.

## Contract rules

- Never combine mutable workflow state, immutable release payload, approval, and post-publication receipts in one object.
- A release payload never contains its own hash.
- A one-byte payload change invalidates prior approval.
- Claim history is append-only; stale or disputed claims can be reverified through a new event.
- A living URL is an alias to the latest approved immutable version.
- No factual assertion can publish without a verified claim ID and exact immutable source locator.
- No audio can publish without narrator identity, disclosure, commercial rights, and passing QC.
- No release is approved by closing a Linear issue.

See `docs/CONTRACTS.md`, `docs/ARCHITECTURE.md`, and `docs/QUALITY-GATES.md`.

## Agent boundaries

- Radar writes candidate source events only.
- Ingestion writes immutable snapshots only.
- Claim Compiler writes candidate claim versions.
- Adversarial Verifier writes verification events; it cannot edit prose.
- Editorial Architect owns thesis and outline.
- Chapter agents write only assigned paths from locked research.
- Lab agent runs code/examples in a sandbox.
- Voice Editor and Citation Auditor propose or block; neither publishes.
- Narration Adapter cannot change factual meaning.
- Audio Producer writes staged assets only.
- Release Operator can publish only an approved envelope hash.
- Atomizer cannot introduce new claims.
- Freshness Agent opens update candidates; it never mutates published releases.

Every delegated task must declare permitted source/claim IDs, expected schema, cost ceiling, maximum calls, output path, and evaluation rubric.

## Repository transition

The prior Content Magic instructions and `ACTIVE/` output workflow are legacy only. Do not invoke them for Starlight editions. Existing assets may be mined as non-authoritative source material after rights and evidence review.

## First golden release

**Graph Engineering for AI Agents**

Pass condition:

- original thesis, three diagrams, two reproduced workflows, decision model, failure modes, and cost;
- web, EPUB, PDF, spoken script, audio, transcript, and source notes share the same content/version IDs;
- every factual assertion resolves to a verified claim;
- all required assets pass validators;
- exact-hash human approval exists;
- publication is idempotent;
- prior web/feed alias can be restored in under 15 minutes without deleting evidence.
