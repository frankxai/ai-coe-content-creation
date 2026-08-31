# Editorial and Release Quality Gates

## Commission gate

A content object cannot enter research without:

- named audience and job;
- owned search intent and canonical URL;
- one-sentence thesis;
- commercial role: free authority, paid manual, Academy, license, or archive;
- required original evidence;
- accountable editor;
- publisher imprint, legal publisher, and rights holder;
- freshness class and review SLA;
- kill/merge criterion.

## Evidence gate

- Every factual assertion resolves to a verified claim ID.
- Every claim has an exact source locator and immutable snapshot.
- Volatile claims include scope, version, effective time, and next review.
- Tier 3 discovery sources cannot verify a fact.
- Inferences are labeled and link to supporting claims.
- Contradictions are resolved, bounded, or shown.
- AI summaries are not evidence.
- Code and benchmarks are reproduced before publication when they carry the thesis.

## Editorial gate

- Direct answer appears before background.
- The work contains an original thesis, not only summary.
- The decision model states who should act, when, and under which constraints.
- Failure modes, recovery, cost, and governance are present where material.
- Vendor language is current and matches official sources.
- No generic filler, empty superlatives, or synthetic “AI-slop” cadence.
- Frank approves every work carrying his author byline.
- FrankX/Arcanea versions are excerpts or adaptations, never mirrored canonical copies.

## Search gate

- One indexable URL owns the intent.
- Owner URL, parent cluster, query, format, and commercial continuation are registered.
- Title and H1 are natural, not keyword-stuffed.
- The page contributes first-party evidence, executable assets, or a unique decision model.
- Canonical, sitemap, lastmod, internal links, and redirects are correct.
- Thin tags, filters, and archives remain noindex.
- Schema describes the real page object; it is not treated as a ranking tactic.
- Podcast/episode pages cannot cannibalize evergreen guide intent.

## Voice and rights gate

- Narrator, voice owner, provider, model, voice ID, territory, term, and commercial rights are recorded.
- Consent artifact exists for every clone.
- Clone training material and consent artifacts have private storage, least-privilege access, retention, and deletion rules.
- Synthetic narration is disclosed.
- No community/shared voice is assumed durable.
- No retiring voice is used as permanent identity.
- Frank clone is never represented as spontaneous live speech.
- Captured ChatGPT Voice output is not commercially distributed.
- Intro/outro music and sound effects have recorded rights.
- Audible/ACX eligibility is validated separately.

## Audio gate

- Spoken script is adapted from the approved semantic source.
- No factual meaning changes in narration.
- Numerals, URLs, acronyms, code, and product names are normalized.
- Pronunciation lexicon version is stored.
- Segment order and count match the manifest.
- ASR round-trip meets named-entity and semantic thresholds defined in the render configuration.
- Zero missing or reordered segments, zero clipping, zero unapproved technical-name pronunciation errors, zero repeated segments, and zero unexplained silence.
- A QC waiver requires reason, scope, policy, approver, and timestamp.
- Transcript, VTT/SRT, and chapter markers align.
- Podcast and audiobook mastering profiles remain separate.
- Human listens to opening, midpoint, ending, and all flagged segments.
- Flagship audio receives a full human listen before release.

## Render gate

### Web

- Valid semantic headings, links, figures, code, and source notes.
- No broken internal or external links.
- Core Web Vitals budget passes.
- Metadata and structured data validate.
- Accessibility checks pass.

### EPUB

- EPUBCheck completes with zero errors.
- Navigation, landmarks, internal links, alt descriptions, fonts, and cover metadata pass.
- No layout assumes a fixed page.

### PDF

- Fonts embed.
- No overflow, clipped figures, orphaned headings, or unreadable tables.
- Source notes and changelog are complete.
- Visual review passes all pages.

## Release gate

- Exact Git SHA, claim-set hash, render-config hash, prompt versions, rights manifest, and asset hashes are frozen.
- Requested formats pass validators.
- ReleaseManifestPayload excludes its own hash, approvals, receipts, and workflow state.
- RFC 8785 canonicalization produces the external envelope hash.
- Approval is bound to the exact envelope hash; a one-byte payload change invalidates it.
- Replaying the same publish event creates exactly one logical publication and one effective receipt.
- R2 enclosure hash, duration, MIME, byte range, and public GET/HEAD pass.
- RSS GUID is stable and independent of asset URL.
- Every mandatory distribution endpoint returns one content-hash-bound receipt; optional endpoint failure is reported without corrupting required-channel state.
- Rollback target is known.
- Public smoke test passes.
- Cost events are complete.

Linear completion is not release approval.

## Derivative gate

- Every derivative names its parent content_version_id.
- It inherits the claim lock.
- It introduces no new factual claim.
- It owns a distinct audience, intent, or format role.
- Syndication uses excerpt + canonical link.
- CTA and attribution remain consistent.

## Freshness gate

- Material source changes create immutable snapshots and diffs.
- Impacted claims are reverified or marked stale.
- Downstream content is identified by content_claims.
- Only invalidated chapters/segments rerender.
- Changelog states what changed and why.
- Critical source changes are detected within 12 hours and assessed within 24 hours.
- “Latest” claims without an owner and review SLA are prohibited.

## Incident and correction gate

- Material factual error can withdraw a release without deleting evidence.
- Correction creates a new version and visible change note.
- Published versions never move backward in state.
- Feed enclosure replacement is reserved for technical defects; material changes receive an update/correction release.
- Prior web/feed alias can be restored in under 15 minutes without deleting evidence.
- Blocked and failed runs have explicit resume, retry, dead-letter, abandon, and rollback events.
- Withdrawal preserves the immutable release and publishes a visible reason.

## Contract and CI gate

The runtime contract implementation cannot merge without:

- separate schemas for EditionDraft, ReleaseManifestPayload, ApprovalEvent, PublicationReceipt, and WorkflowState;
- deterministic RFC 8785 canonicalization and SHA-256 tamper tests;
- a valid draft fixture and valid published web/audio fixture;
- invalid fixtures for missing approval, missing audio rights, failed QC, unsupported waiver, missing mandatory receipt, and altered payload;
- Markdown, link, schema, fixture, and golden-release checks in required CI;
- one golden release whose web, EPUB, PDF, audio, transcript, approvals, and receipts join through the same content and version IDs.

## Commercial decision gate

Pilot evidence is directional, not statistical proof.

- A voice persona can graduate after a blinded panel review plus at least 20 target-listener comparisons, but the result is recorded as a pilot decision.
- A 30-day purchase signal means collected paid preorders or a predeclared number of verified buyer commitments—not likes, waitlist entries, or survey enthusiasm.
- A 90-day commercial gate reports collected revenue separately from a probability-weighted signed pipeline; neither is labeled as achieved recurring revenue.
