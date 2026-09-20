# v0.4.4: seven shapes contributed by riskmandate.ai are promoted with their provenance, a vendor scope becomes a node, and the intake path is the same for anybody

> The second of the three requests riskmandate.ai published against this site on 12 September, the one it marked as unblocking a product. Seven deployment shapes it built ahead of this site, two Gmail scopes, a Drive scope, a Microsoft 365 connector, a Dropbox server, the Google...

*Source: <https://abp.sgit.ai/versions/v0.4.4/index.html> · site v0.4.4 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.4.4

# v0.4.4: seven shapes contributed by riskmandate.ai are promoted with their provenance, a vendor scope becomes a node, and the intake path is the same for anybody

The second of the three requests riskmandate.ai published against this site on 12 September, the one it marked as unblocking a product. Seven deployment shapes it built ahead of this site, two Gmail scopes, a Drive scope, a Microsoft 365 connector, a Dropbox server, the Google Workspace servers and an n8n instance measured on a live sandbox by an early user, are fetched as bytes, held under data/contributed/riskmandate/ unchanged with a hash per file and a hash over all of them, and promoted into the published profiles and mandates without renaming anything. Under the three layers a shape is a layer one fact owned by nobody and belongs at the address every consumer reads; the contributor's vaults can now pin this site's version of each shape rather than their own copy. The site now holds sixteen shapes and fifteen starting mandates, the contributed rows are counted beside the map's rows and never folded into them, and the evidence tier on every contributed row is the contributor's, which this site did not observe and does not raise.

| Field | Value |
|---|---|
| Version | `v0.4.4` |
| Date | 2026-09-20 |
| Commit | **`git rev-list -n 1 v0.4.4`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.4.4:`. The hash is not written into [`versions/v0.4.4.json`](../../versions/v0.4.4.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.4.4.json`](../../versions/v0.4.4.json) |

## What changed

- data/contributed/riskmandate/: twenty one files as fetched on 20 September 2026 from riskmandate.ai's public endpoint, a grant, a mandate and a vault record per shape, and a manifest carrying the retrieval time, the source address of each file, a hash per file and a hash over all of them. The build and the gate both recompute the hashes and refuse to proceed if a byte moved.
- Seven profiles and seven mandates promoted from those bytes. Each carries a provenance block in the same shape as every other file, so no consumer needs a special case, plus who contributed it, the contributor's own provenance block whole, and the contributor's contradictions, research needed and what the grammar cannot say, carried rather than dropped because they are the finding. Every capability id is one of the 23; is_bounded is recomputed from the barrier; the evidence tier is kept as stated.
- Sixteen stored deltas and sixteen fact sets, seven of them new, each pinning the contributor's retrieval time as the time it was computed against. Every capability page now shows the shape in up to 16 published shapes with whose material each row reaches, and every reach class page carries the contributed shapes' own definitions of host, tenant and world beside the map's, unmerged.
- The material property is valued for the first time: 37 contributed rows state whose material they reach. The nine promoted shapes still say null, and the gate refuses any value outside the four.
- A Scope node type and two edges, scoped_by and permits. A connector shape reaches a row through a scope in the vendor's own identifier, gmail.readonly or drive.file, which is not a tool; it is kept in the vendor's word and given its own node rather than filed as a tool. Walked on every build.
- The provenance line splits. The map's 21 of 99 stays the headline on every page that carries rows from every shape, and a second sentence beside it says how many rows were contributed, how many of those sit at the contributor's measured tier, and where the bytes are. A page about one promoted shape carries only the map's line, because every row on it is the map's.
- The data page carries the contributed shapes and the intake path, which is the same for anybody: a profile file and a mandate at an address the proposer publishes, held here as the bytes fetched with their hash, promoted without renaming, every id inside the grammar, and a row that needs a new word recorded as not in the grammar rather than forced.
- Two things this release does not do, stated so that nobody reads them in. riskmandate.ai's nine vaults for this site's own shapes are not imported, because they pin this site and importing them would be a loop. And the contributed shapes get no example page: their ABPs exist as data and riskmandate.ai renders each one live from its vault, which this site links to by address.

## What it was built against

- riskmandate.ai's Lab 03 of 12 September 2026, request 2, and its vault index at riskmandate.ai/vaults/index.json, read 20 September 2026, for the seven shapes and the addresses of their files.
- The seven grant and mandate files themselves, each carrying the contributor's own provenance: the vendor pages read and quoted on 13 to 16 September 2026, and for the n8n shape a dated probe of a sandbox instance by an early user's agent.
- The three layers page on this site, for the rule that a shape is a layer one fact and belongs at the address every consumer reads rather than in one consumer's vault.

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

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.4.4/index.html)*
