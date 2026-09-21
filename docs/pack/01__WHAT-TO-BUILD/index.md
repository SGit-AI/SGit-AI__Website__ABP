# What To Build

> Every site in the network is named for an argument rather than for a function, and there are twenty seven of them. The argument here is not a product name.

*Source: <https://abp.sgit.ai/docs/pack/01__WHAT-TO-BUILD/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The pack](../../../docs/index.md#pack) / What To Build

# What To Build

> **The source bytes.** This page is generated from [`docs/pack/01__WHAT-TO-BUILD.md`](../../../docs/pack/01__WHAT-TO-BUILD.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

## The argument this site owns

Every site in the network is named for an argument rather than for a function, and there are twenty seven of them. **The argument here is not a product name.**

> **You know what you asked for. You do not know what it can do.**

That is the thesis line for the home page. It is the corrected version of the memo of 11 September: the mandate is already understood, implicitly or explicitly, and the grant is not. **The site exists to close that gap in public, for free, and the store sells the instance of it.**

## Build order

The standard prompt asks for the pipeline first, and that is right. **Nothing below matters if the site does not publish.**

| # | Step | Done when |
|---|---|---|
| 1 | **CI pipeline and auto tagging**, copied from a sibling site's repository | A push to `dev` builds, tags and publishes |
| 2 | **Version surface**: `versions/index.json`, a per version file, and the version visible in the chrome as a link | The chrome shows the current version and it links to that version's own details |
| 3 | **`llms.txt` and `llms-full.txt`**, generated from the site rather than written | Every page appears in `llms.txt` |
| 4 | **The docs section**, using the platform's markdown rendering | Every document in this pack is readable on the site |
| 5 | **The data**, promoted from the game's pack into a published schema | `data/` serves the capabilities, profiles, barriers and undo classes at a stable address with cross origin access |
| 6 | **The model pages**: what an ABP is, the four objects, the graph | A reader can follow one capability from a product profile to a mandate to a delta to a prohibition |
| 7 | **The examples**: five ABPs, derived from the data | Each example states which of its rows were measured and which were derived |
| 8 | **The visualisations** | One grant against mandate view that is not a table |

## The site map

```
/                        the argument, in one screen, derived from the foundation document
/what-is-an-abp/         the foundation document, rendered, with each term linked to its node
/model/                  the graph: capabilities, barriers, undo, the schema
/examples/               five ABPs, one per deployment shape
/docs/                   every reference and guidance document, rendered
/data/                   the JSON, at stable addresses, CORS enabled
/versions/               the version history
/llms.txt                generated
/llms-full.txt           generated
```

**Scope by domain and link across.** This site says one thing properly. Where an argument belongs to a sister site, link to it rather than restating it: the graph rules to `graphs.sgit.ai`, the capability map to `what-can-it-do.games.sgit.ai`, the twin to `twins.sgit.ai`, the acceptance workflow to `risks.sgit.ai`, the style rules to `coding.sgit.ai`.

## The docs section, which was asked for specifically

**Every reference and guidance document in this pack goes into `/docs/`, rendered with the markdown rendering already used across the network.** Do not write a renderer. The guidance is explicit that markdown viewing, file trees and page layouts are platform provided and must not be rebuilt.

**What goes in it:**

| Section | Contents |
|---|---|
| `/docs/briefs/` | The foundation document first, then the three briefs, all unchanged with their own licence footers intact |
| `/docs/pack/` | The six numbered documents of this pack |
| `/docs/model/` | The schema and ontology documents you write, as markdown with their JSON twins |
| `/docs/inherited/` | Pointers to the guidance you inherited, with the date read. **Link, do not copy**, except where a rule is quoted |

**Two conventions from the guidance apply to every page in it.** Every page is reachable and machine readable, with a markdown twin and an entry in `llms.txt`. And anything rendered stays one click from its source bytes, so every rendered document shows a link to the file it came from.

**Indexes are generated from the data they index**, so `/docs/index` is built from the files present rather than maintained by hand. The guidance says an index that can disagree with its source is a defect.

## The examples, which are the point

The memo asks for the examples first and it is right, but they should be **derived rather than authored**. [`04__THE-FIRST-EXAMPLES.md`](../../../docs/pack/04__THE-FIRST-EXAMPLES/index.md) gives the five and where each one's rows come from.

**Each example page shows:**

1. **The label**: the one line on the outside, per [`03__THE-ABP-MODEL.md`](../../../docs/pack/03__THE-ABP-MODEL/index.md), with excess and unbounded excess as the two headline numbers, and no score.
2. The named deployment shape, in the product profile's published words.
3. **The grant**, as capability primitives, each with its barrier glyph and its undo class, ordered irreversible first and saying that reversibility is a property of the action rather than a severity.
4. **The mandate**, as the small set the deployer authorised.
5. **The delta**, computed, never stored, shown as excess in one colour and shortfall in the other.
6. **The prohibitions**, each carrying the layer it would be enforced at, and each marked as enforced or not enforced today.
7. **The provenance line**: how many rows were measured, how many derived, and when.
8. **The validity statement**: this describes the deployment shape as at this date; if the risk changed, the deployment changed, not this document.

**That sixth row is not optional.** The published map already does it, stating that twenty one of ninety nine rows were measured and the rest derived. **An example that hides that is worse than one that has few measured rows.**

## The community editable layer

**The data files are the shared facts and they live in this repository so that people can propose changes.** That is the four layer architecture: the site and its data are the library, and a cloned vault is the instance.

Two rules come with it, from 10 September:

**A proposal to a data file carries evidence.** Every node taken from a third party site carries a source URL, a retrieval timestamp and a content hash. A proposal that changes a capability row without one is an assertion.

**A consumer pins a version.** Anything that computes from these files states which version it computed against. A clone that floats against the latest has no reproducible output.

## What not to build

- **A markdown viewer, a file browser or a page layout engine.** Platform provided.
- **A checkout, a price or a payment link.** That is the store.
- **A new capability ontology.** It exists.
- **A general graph renderer.** The graph rules say never render the whole graph, render the result of a query.
- **An assessment of any named product.** See the hard rules.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/pack/01__WHAT-TO-BUILD/index.html)*
