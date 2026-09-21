# v0.4.1: the universes become data with a page each, the walk of one row is built on every build, and the gate checks that every node type is owned

> The map of v0.4.0 becomes files the build reads, pages that render one query, and a gate check. Thirteen universes are authored in admin/build/universes.py, each with its owner, its centre of gravity, its smallest node, its status, its node types and its verbs; the build writes...

*Source: <https://abp.sgit.ai/versions/v0.4.1/index.html> · site v0.6.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.4.1

# v0.4.1: the universes become data with a page each, the walk of one row is built on every build, and the gate checks that every node type is owned

The map of v0.4.0 becomes files the build reads, pages that render one query, and a gate check. Thirteen universes are authored in admin/build/universes.py, each with its owner, its centre of gravity, its smallest node, its status, its node types and its verbs; the build writes one file per universe under data/universes/ and an index that carries the walk of one capability row through nine of them, rebuilt from the published profile, mandate and delta on every build so the sentence on the page cannot drift from the rows it is made of. Every node type now names its universe, every edge names the universes of its domain and range, and a junction is computed from those rather than declared. The gate's fourteenth check holds all of it. The release also adds a research note under /docs/research/ on the prior work the fractal claim sits beside, with every reference resolved on the day.

| Field | Value |
|---|---|
| Version | `v0.4.1` |
| Date | 2026-09-20 |
| Commit | **`git rev-list -n 1 v0.4.1`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.4.1:`. The hash is not written into [`versions/v0.4.1.json`](../../versions/v0.4.1.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.4.1.json`](../../versions/v0.4.1.json) |

## What changed

- data/universes/index.json and thirteen files u0.json to u12.json. The index carries the walk: nine rows, one per universe, each naming the node the walk is standing on and the edge that leaves it, over authenticate-as.credential.tenant in the shape this site is built from, and the walk as one sentence.
- A page at /model/universes/ that renders that one query and lists the thirteen universes with their status, and a page per universe at /model/universes/uN/ rendering its ontology: node types with the counts of the ones that exist, verbs with inverses, domains and ranges, and the edges that cross its boundary today. There is no map of everything and there will not be one.
- data/graph/node-types.json: every type names its universe. data/graph/edges.json: every edge names the universe of its domain and of its range and whether it crosses. Six live edges cross a boundary today: grants, bounded_by, authorises, withholds, exceeds and falls_short_of.
- The gate's fourteenth check: every universe has an owner and a status from the declared set, every node type names a universe that exists, every junction is computed from the edge vocabulary and listed with an owner, a live status means every declared type is in the graph, a gap declares none, and the walk crosses nine universes over a row the shape actually grants.
- Two corrections to the v0.4.0 brief, recorded in the brief rather than applied quietly. The walk it drew stood on send.endpoint.world, which the shape it walked does not grant; the data walks authenticate-as.credential.tenant, which is excess and bounded, and the brief now says so above the table it corrects. And two statuses moved from live to partial when the status became a gate check: the source bytes are per file rather than per node, and the derivation's records are files rather than nodes.
- A research note at /docs/research/: an external review of the Fractal Semantic Graphs claim against distributed description logics, E-connections, distributed first order logic, named graphs, ontology alignment, federated query, OSLC, data mesh, OSCAL, PROV-O and provenance semirings, published as received with the citation markers that did not survive the paste removed, followed by this site's reading of it: every reference resolved on 20 September 2026 with its status, what the note changes on this site, and what it does not.

## What it was built against

- The v0.4.0 brief, for the universes, their ontologies and the build order it set out, of which this is the first release.
- graphs.sgit.ai v0.6.22, for the corrected fractal claim that the status field is written against: a live universe is one whose ontology exists, not one whose format is uniform.
- riskmandate.ai v1.26.2, for the vault pages the eighth universe's edges point at, linked here by address and never held.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.4.1/index.html)*
