# v0.1.0: the ontology is promoted out of a game and the five examples are derived rather than written

> The first version of abp.sgit.ai. The capability ontology the ABP needs already existed, published, as the data pack a game reads, so this release promotes it into a schema with a stable address rather than authoring a second one, and derives five worked ABPs from it. Nothing on...

*Source: <https://abp.sgit.ai/versions/v0.1.0/index.html> · site v0.1.0 · this file is generated from the same content
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
| Commit | `git rev-list -n 1 v0.1.0`, written into [`versions/v0.1.0.json`](../../versions/v0.1.0.json) once CI has tagged this release. Until then the file says where the hash will come from rather than carrying one that would be wrong. |
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
- Five structural guards beyond the house four: every page in llms.txt, no em dash or en dash anywhere outside the promoted data, no score vocabulary anywhere, no forbidden word, and the version surface agreeing with version.txt.

## What it was built against

- The foundation document of 11 September 2026, which is the definition and wins where it and the pack disagree.
- The build pack of 11 September 2026: what to build, the conventions, the model, the first examples, the hard rules and the prompt.
- The published capability map at what-can-it-do.games.sgit.ai, data pack v0.8.0, retrieved 2026-09-11, content hash sha256:d6d4ba40f1fb1f93.
- The vault and site building guidance at sgit.ai/docs/guidance/, read 11 September 2026.
- The five graph rules at graphs.sgit.ai, read 11 September 2026.
- The style guide at coding.sgit.ai, read 11 September 2026.

## The five verifications against the sibling

The pipeline, the release gate and the page shell were copied from [SGit-AI__Website__Game__What-Can-It-Do](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do) at its v0.8.0. The conventions ask for five things to be verified rather than assumed, and **an absent one is a finding that belongs in the first version's notes** rather than a thing to fix quietly.

| Verification | The sibling | What this repository does |
|---|---|---|
| The tag is derived from the version file, not typed by hand | **holds** | `admin/build/version.txt` owns the version. CI reads it, refuses to tag if the newest release commit's subject disagrees, refuses if the tag already exists on an earlier commit, and refuses if the bump is not the next minor or a deliberate major. Copied unchanged. |
| The build fails when `llms.txt` does not list every page | **did not hold** | The sibling generates `llms.txt` from its page list, so it cannot miss a page the generator knows about, and nothing fails if a page exists in the tree that the generator does not. Check 11 here walks the tree and fails on any `.html` page missing from `llms.txt`. |
| The custom domain survives a rebuild | **did not hold** | The sibling commits `CNAME` once. Here the build writes it from `SITE['host']`, and the canonical check reads the same file, so a domain change is one edit in one place. |
| The markdown twin of every page is produced by the build | **holds** | `shell.write_site` emits the `.html` and the `.md` from the same block list, and gate check 7 fails on a page without a twin. Copied unchanged, and it is the reason the twins cannot drift. |
| The version in the chrome comes from `versions/index.json` | **did not hold** | The sibling has no `versions/index.json` at all: the badge reads `version.txt` and links to a hand-maintained history page. Here the build generates `versions/index.json`, a file and a page per version, from the same string the tag is derived from, and the badge links to that version's own details. The published pipeline still owns the tag, so the two cannot disagree. |

**Two of the three that did not hold are one-line fixes and the third is a surface that did not exist.** None of them is a criticism of a site that has been publishing for weeks: they are the cost of a pipeline growing by copy, which is exactly what the five verifications are for.

## Where the sources disagree

The published source wins and the disagreement is recorded. **The estate's method is to record the gap, not to quietly resolve it.**

| The disagreement | What each says | What this site did |
|---|---|---|
| The foundation document and the published data, on what changes when confirmations go off | The foundation document says that turning confirmations off moves the barrier on **every capability in the delta** by one row. In the published pack it moves exactly one barrier, on `execute.process.host`, and that capability is **inside the mandate**: the deployer asked for it. So the label's numbers do not move at all and the two documents still differ materially. | The data wins on the fact and the foundation document wins on the wording, so both example pages state what actually changes. It makes the pair a **better** argument, not a worse one: identical headline numbers, a materially different document, which is the case for the leaflet and against any single number. |
| The pack and the sibling, on where the version lives | The conventions ask for `versions/index.json` as the home of the version. The sibling's working pipeline derives the tag from `admin/build/version.txt` and has no `versions/index.json`. | Both. `version.txt` still owns the tag, because that is the published pipeline and it wins; `versions/index.json` is generated from the same string, so the surface the guidance asks for exists and cannot drift from the tag. The gate checks the agreement. |
| The pack and the published data, on whether the smallest grant has an empty delta | The pack says the smallest shape in the set is where a reader who does not believe an agent can do much *finds the delta is still not empty*. In the published data that shape's grant is one capability and the starting mandate asks for exactly it, so **the delta is empty**. | The example says so, plainly, and says why an empty delta is a result rather than a failure: a method that could never report nothing would be a sales document, and the other four examples would be worth less for it. Changing the mandate to manufacture a delta would have been the dishonest fix. |
| The published headline and the pack's own vocabulary, on what `measured' means | The map's headline says 21 of 99 rows were measured. The pack's vocabulary defines `measured` as a dated probe with an evidence file, and **no row in the pack is at that tier**: the 21 are at `observed`, which is seen directly on the thing itself. | The site counts `observed` as measured, which reproduces the published figure, and says so in `data/provenance.json` and on the data page. Reproducing the number without the note would have been less careful than the map. |
| The hard rules and the published data, on em dashes and pure ASCII | Every document in this repository is to be pure ASCII, with zero em dashes and zero en dashes. The data promoted from the capability map carries all three, because it was written elsewhere and this site does not get to edit somebody else's bytes. | Both. The JSON keeps the upstream strings exactly as they arrived and `data/` is exempt from the guard for that reason; every upstream string rendered into a page is transliterated at render time; and the bytes are one click away under `/data/upstream/`. The guard is in the pipeline and fails the build everywhere else. |
| The guidance and the docs section, on rebuilding the markdown renderer | The guidance forbids rebuilding markdown viewing, file trees and page layouts, because the platform provides them. The docs section has to turn eleven markdown documents into pages. | `admin/build/docs_pages.py` translates a markdown document into the same small block vocabulary every other page here is written in, at build time. No viewer is shipped to a browser, no file tree and no layout engine, and the source bytes are served beside every rendered document. It is a judgement call and it is recorded as one rather than assumed. |

## What is not built yet, stated plainly

- **No view across the nine shapes.** Each example carries a grant-against-mandate figure, and there is no figure that puts one capability across every deployment shape at once. The third graph rule says render the result of a query rather than the whole graph, so that would be another query rather than a map.
- **No ABP for a shape outside the published map**, which means the cost of producing one where the grant has to be measured rather than looked up is still unknown, and that is the number the store needs.
- **No interchange form emitted.** The W3C vocabulary is described on [the graph page](../../model/graph/index.md) and nothing on this site serialises to it yet.
- **Quantity and agent-to-agent interaction are not modelled**, as the model page says. They are gaps in the ontology rather than in this site.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.1.0/index.html)*
