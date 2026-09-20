# v0.4.0: the ABP is mapped onto Fractal Semantic Graphs: one row crosses nine universes and each keeps its own ontology

> A map, and nothing built from it yet. By the zoom test as graphs.sgit.ai now states it, the graph this site holds at v0.3.0 decomposes one vocabulary very well and crosses into another in exactly two places, the reach class disagreement and the bridge to the game. An ABP is a...

*Source: <https://abp.sgit.ai/versions/v0.4.0/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.4.0

# v0.4.0: the ABP is mapped onto Fractal Semantic Graphs: one row crosses nine universes and each keeps its own ontology

A map, and nothing built from it yet. By the zoom test as graphs.sgit.ai now states it, the graph this site holds at v0.3.0 decomposes one vocabulary very well and crosses into another in exactly two places, the reach class disagreement and the bridge to the game. An ABP is a junction object: its four objects are owned by four different parties speaking four vocabularies, which is the case Fractal Semantic Graphs exists for. So this release publishes the map: the nine universes one capability row crosses from the source bytes to a licence condition, the ontology each keeps, the twenty two edges that cross a boundary with their owners, the lexicon as scopes, the positions on riskmandate.ai's three open requests, and the site changes in build order, one universe per release. It also corrects the fractal test this site quoted, which was the first edition's wording and scored decomposition as fractal.

| Field | Value |
|---|---|
| Version | `v0.4.0` |
| Date | 2026-09-20 |
| Commit | **`git rev-list -n 1 v0.4.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.4.0:`. The hash is not written into [`versions/v0.4.0.json`](../../versions/v0.4.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.4.0.json`](../../versions/v0.4.0.json) |

## What changed

- A dev brief in /docs/briefs/ carrying the map: the zoom test applied to v0.3.0 zoom by zoom, the ruling that altitude keeps its 20 August sense and universe is the word for a world with its own ontology, the walk of send.endpoint.world through nine universes as one sentence, each universe with its owner, node types, verbs, formulas and status, the junction edge set, the scoped lexicon, and the build order. It appears in the docs index, in llms.txt and in the sitemap with no second edit.
- The fractal test is corrected in two places it was quoted: the graph module's docstring and the three layers page. Both said that a system needing a new format or a special case is hierarchical rather than fractal, which is the first edition's wording and scores decomposition as a pass. The corrected statement is that the grammar survives every zoom and the ontology does not have to. The old sentence is recorded beside the new one rather than overwritten.
- The graph page links the map beside the lexicon, the edges, the formulas and the three layers, so it is reachable from the model and not only from the docs index.
- Nothing in the data moved. The universes, their files, their pages, the gate check over junction edges and the fact diff are the releases after this one, in the order the brief states.

## What it was built against

- The Fractal Semantic Graphs page at sgit.ai/demos/fractal-graphs/, read 20 September 2026: every node opens into a semantic graph with its own ontology, joined by named edges; only the grammar is shared; and this site is the rung where the graph meets a real permission set, a vocabulary and not yet a join.
- graphs.sgit.ai v0.6.22, read 20 September 2026, for the corrected fractal claim, the zoom test in two halves, and the lexicon held as scopes with overrides recorded.
- riskmandate.ai v1.26.2, read 20 September 2026, for the sixteen published behaviour policy vaults, the three open requests against this site in its Lab 03, and the delivered vault in its Lab 07.
- store.sgit.ai v0.3.24, read 20 September 2026, for the boundary between the three sites.

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
| SETTLED IN v0.2.0. The foundation document and the project lead, on whether a delta is stored | v0.1.0 built to the foundation document's rule that the delta is computed and NEVER STORED, and put a check in the release gate refusing any file that carried one. The project lead's correction, issued the same day, is that the second half was an error: the delta belongs in a vault along with the history of the grants and mandates that produced it. | v0.2.0 stores the deltas with their inputs pinned and inverts the check, so the gate now recomputes every one of them. **Never authored** is the rule that replaced it, and it is harder than the one it replaced. See [the delta](../../model/delta/index.md). |
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

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.4.0/index.html)*
