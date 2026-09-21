# v0.4.1: The map became files, pages and a gate check, and the walk is rebuilt on every build

> A map in prose is a claim. Thirteen universes as data with a page each, a walk computed from the published rows, and a fourteenth check that refuses to publish a world nobody owns. The walk immediately found an error in the brief that drew it.

*Source: <https://abp.sgit.ai/articles/nine-universes-as-data/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Articles](../../articles/index.md) / v0.4.1

# v0.4.1: The map became files, pages and a gate check, and the walk is rebuilt on every build

A map in prose is a claim. Thirteen universes as data with a page each, a walk computed from the published rows, and a fourteenth check that refuses to publish a world nobody owns. The walk immediately found an error in the brief that drew it.

> **This is the article for release v0.4.1, published 20 September 2026.** Every release of this site gets one, and it explains what that release changed and why rather than restating [v0.4.1's own release record](../../versions/v0.4.1/index.md). It is release 5 of 10 on this site. Every screenshot below was captured from a checkout of the `v0.4.1` tag, so it shows the site as it stood at that release and not as it stands today. Read on to [v0.4.2](../../articles/the-fact-diff-reads-the-published-page/index.md), or back to [v0.4.0](../../articles/an-abp-is-a-junction-object/index.md).

## A map in prose is a claim

v0.4.0 drew the map in a brief. A brief is a document, and a document cannot be checked. **This release turns the map into files the build reads, pages that render one query, and a check that refuses to publish a world nobody owns.**

Thirteen universes are authored once, in one module, each with its owner, its centre of gravity, its smallest node, its status, its node types and its verbs. The build writes one file per universe and an index that carries the walk.

## The walk is computed, not written

The index carries one capability row walked through nine universes. Every cell of it is built from the published profile, the published mandate and the stored delta on every build, **so the sentence it reads as cannot drift from the rows it is made of.**

![A nine row table following one capability through nine universes, and the same walk written out as one sentence](../../assets/articles/v041-walk.png)

*One row, nine worlds, and the fifth graph rule applied across nine vocabularies rather than within one. Every clause of the sentence underneath is a node this site holds or an edge somebody has declared. (abp.sgit.ai at v0.4.1, captured 20 September 2026 from a checkout of the v0.4.1 tag.)*

> **The walk found an error in the brief that drew it, on its first run.** The brief walked `send.endpoint.world` through the container shape. That shape does not grant it: it grants `send.endpoint.allowed`, and the mandate asked for it, so the path would never have reached a prohibition at all. The data walks `authenticate-as.credential.tenant`, which is excess and bounded. The correction is recorded in the brief, above the table it corrects, rather than applied quietly.

## Thirteen worlds, and a status that is a claim

![Thirteen universes with their level, owner, status, node types and verb counts](../../assets/articles/v041-thirteen.png)

*Nine the walk crosses and four it names. A status is not a label here: live means every node type the universe declares exists in the graph today, and a gap must declare none. (abp.sgit.ai at v0.4.1, captured 20 September 2026 from a checkout of the v0.4.1 tag.)*

| Status | What it claims | What the gate checks |
|---|---|---|
| `live` | its node types exist in the graph today | every declared type is in the graph, or the build fails |
| `partial` | some of them do | the ones marked as existing really do |
| `one-edge` | an edge reaches in and finds no vocabulary yet | the same |
| `outside` | another site owns it; this one holds the anchors | it claims no node types of its own |
| `gap` | named so the next release has an address | it declares none |

**Two statuses moved during this release because the status became a check.** The source bytes and the derivation were written down as live in the brief. The gate disagreed: provenance is per file rather than per node, and a delta record is a file rather than a node in the graph. Both are `partial`, and the prose in the brief stands as written with the data as the record.

## A junction is computed rather than declared

The property that turns a set of graphs into a fractal rather than a pile is the edge that crosses from one world into another. **This site does not declare which edges those are.** Every node type names its universe, every edge names the universes of its domain and range, and an edge crosses when the two differ.

![Six edges that cross a universe boundary, each with its inverse, the world it leaves and the world it enters](../../assets/articles/v041-junctions.png)

*Computed from the edge vocabulary, so this table cannot disagree with it. The brief names twenty two junctions in all; these are the ones the graph held at this release. (abp.sgit.ai at v0.4.1, captured 20 September 2026 from a checkout of the v0.4.1 tag.)*

## One page per world

![The enforcement universe page: its owner, centre of gravity, smallest node and status, with the node types it has and the ones it needs](../../assets/articles/v041-u4.png)

*Each universe renders its own ontology. The formula column separates what is walked on every build from what the world needs and does not have, which is the honest shape of a world that is one edge deep. (abp.sgit.ai at v0.4.1, captured 20 September 2026 from a checkout of the v0.4.1 tag.)*

## The fourteenth check, and proving it bites

A check that has never failed is a check nobody has tested. Before this release was committed the index was corrupted three ways on purpose, and the gate named each one.

```
$ node admin/build/validate.js
validate: 3 error(s)
  x data/universes/index.json: u3 has no owner -- a world nobody owns is a
    merge waiting to happen
  x data/universes/index.json: grants crosses from u2 to u1 and is not listed
    as a junction
  x data/universes/index.json: the walk stands on send.endpoint.world, which
    anthropic/claude-code-remote/ccr-container does not grant
```

## And a reading of the prior work, published as received

The same release carries something that is not this site's: an external review of the Fractal Semantic Graphs claim against the research it sits beside. Distributed description logics and their bridge rules, E-connections, distributed first order logic, named graphs, ontology alignment, federated query, engineering lifecycle integration, data mesh, machine readable control catalogues and two formal accounts of provenance.

![A table of twenty four references with the address each was resolved at and its status](../../assets/articles/v041-research-refs.png)

*The review arrived with its citation markers stripped by the paste, so every reference was located and fetched on the day. Three resolved to a publisher that refused an unauthenticated fetch, which is a fact about the publisher; one vendor page had moved; one paper could not be located at all, and the table says so. (abp.sgit.ai at v0.4.1, captured 20 September 2026 from a checkout of the v0.4.1 tag.)*

> **The review's sharpest point is taken and is not yet built.** A bridge that says *same individual* is not a bridge that says *approximate match*, and a client that follows an edge without knowing which of those it is has not interpreted it. Every junction and every declared bridge should carry a kind. That is written down as the next change rather than quietly added to the data, because the map is published and changing it silently is the thing this site keeps refusing to do.

[The universes](../../model/universes/index.md) &#183; [The universes as JSON](../../data/universes/index.json) &#183; [The research note](../../docs/index.md#research) &#183; [v0.4.1's own release record](../../versions/v0.4.1/index.md)

## Read the sequence

| Direction | The release |
|---|---|
| **Older** | [v0.4.0: An ABP is a junction object, which is what Fractal Semantic Graphs is for](../../articles/an-abp-is-a-junction-object/index.md) |
| **Newer** | [v0.4.2: The fact diff was named as a blocker on four consecutive days, and it reads the published page](../../articles/the-fact-diff-reads-the-published-page/index.md) |
| **All of them** | [One article per release](../../articles/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/articles/nine-universes-as-data/index.html)*
