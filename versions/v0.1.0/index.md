# v0.1.0: the ontology is promoted out of a game and the five examples are derived rather than written

> The first version of abp.sgit.ai. The capability ontology the ABP needs already existed, published, as the data pack a game reads, so this release promotes it into a schema with a stable address rather than authoring a second one, and derives five worked ABPs from it. Nothing on...

*Source: <https://abp.sgit.ai/versions/v0.1.0/index.html> · site v0.5.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.1.0

# v0.1.0: the ontology is promoted out of a game and the five examples are derived rather than written

The first version of abp.sgit.ai. The capability ontology the ABP needs already existed, published, as the data pack a game reads, so this release promotes it into a schema with a stable address rather than authoring a second one, and derives five worked ABPs from it. Nothing on a generated page is typed in: every number, glyph and row is computed from data/ at build time, which is what makes the provenance line worth reading. The pipeline, the tagging and the page shell are the sibling game site's, with four changes, each of which is one of the five verifications the conventions ask for and the sibling did not have.

| Field | Value |
|---|---|
| Version | `v0.1.0` |
| Date | 2026-09-11 |
| Commit | **`git rev-list -n 1 v0.1.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.1.0:`. The hash is not written into [`versions/v0.1.0.json`](../../versions/v0.1.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.1.0.json`](../../versions/v0.1.0.json) |

## What changed

- The pipeline, the release gate and the page shell are copied from SGit-AI/SGit-AI__Website__Game__What-Can-It-Do at its v0.8.0: validate, then tag, then publish, with the tag derived from admin/build/version.txt and checked against the release commit's subject.
- data/ carries the published vocabulary: 23 capability primitives in verb.object.reach form, the four barriers, three undo classes, seven evidence tiers, nine deployment shapes and eight starting mandates, at stable addresses with cross origin access. Nothing is renamed; the source bytes are served unchanged under data/upstream/ and the build recomputes their hash on every run and refuses to write if it disagrees.
- Each example carries one grant-against-mandate figure that is not a table: the mandate in one column, the grant in the other, and a line joining every capability in both, so a mark with no line reaching it is excess. Colour is never the only channel, every mark carries its published barrier glyph and its full id, and the markdown twin states the same facts in prose.
- Five worked examples, derived from that data rather than authored, each with a label of nine fields, the grant ordered irreversible first, the mandate, the delta computed on the page, the prohibitions each carrying the barrier they sit at today, the measured-against-derived line, and the statement that none of it is an assessment.
- The docs section renders the foundation document, the three briefs and the six pack documents through the same block vocabulary as every other page, with the source bytes of each one click away and an index generated from the files present.
- The version surface the guidance asks for: versions/index.json with a file and a page per version, the badge in the chrome reading `current' from it and linking to that version's own details rather than to a generic changelog.
- llms.txt and llms-full.txt are generated from the site, and the gate fails the build if a page in the tree is missing from llms.txt.
- The version surface stops reading git. Recording the commit by resolving the tag at build time made the build non-deterministic -- it produced hashes on a checkout with tags and nulls on one without -- and the pipeline's own staleness check caught it on this release's first push. The file now records HOW TO RESOLVE the commit, `git rev-list -n 1 vX.Y.Z`, which is stable for anybody forever, and the gate checks that the resolution names this version's own tag. The guidance asks for a version to be verifiable later; a published resolution method is verifiable in a way a hash only half the world's checkouts can produce is not.
- Five structural guards beyond the house four: every page in llms.txt, no em dash or en dash anywhere outside the promoted data, no score vocabulary anywhere, no forbidden word, and the version surface agreeing with version.txt.

## What it was built against

- The foundation document of 11 September 2026, which is the definition and wins where it and the pack disagree.
- The build pack of 11 September 2026: what to build, the conventions, the model, the first examples, the hard rules and the prompt.
- The published capability map at what-can-it-do.games.sgit.ai, data pack v0.8.0, retrieved 2026-09-11, content hash sha256:d6d4ba40f1fb1f93.
- The vault and site building guidance at sgit.ai/docs/guidance/, read 11 September 2026.
- The five graph rules at graphs.sgit.ai, read 11 September 2026.
- The style guide at coding.sgit.ai, read 11 September 2026.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.1.0/index.html)*
