# abp.sgit.ai

**The Agent Behaviour Policy.** You know what you asked for. You do not know what it can do.

This repository builds [abp.sgit.ai](https://abp.sgit.ai/), the free public library for the
Agent Behaviour Policy: the argument, the model, five worked examples and the published data.
Buying an ABP happens on the store. **There is no checkout here and there will not be one.**

## What an ABP is

A written description, for one agent in one deployment, of four things:

| Object | What it is | How it is obtained |
|---|---|---|
| The mandate | What the agent is authorised and expected to do | Elicited |
| The grant | Everything the agent can do | Measured |
| The delta | The difference | **Derived and never authored**: recomputed when either input moves, stored with both versions pinned |
| The barrier | What stands between the agent and each capability | Recorded, from one of four kinds |

**The delta rule was corrected on 11 September 2026**, the day the foundation document was
published, from *computed and never stored* to *derived and never authored*. Never authored is
the harder rule, because it forbids the act rather than the artefact. The correction is
published rather than applied quietly: see `/model/delta/` and the dev brief in
`docs/briefs/`.

**It describes and it does not judge, so it carries no score**, anywhere, including in the
data. The same ABP is dangerous in one deployment and harmless in another and nothing about the
document changed. A policy cannot be dangerous; a deployment can.

## The layout

```
index.html            the argument, in one screen
what-is-an-abp/       the foundation document, rendered, with its terms linked to their nodes
model/                the four objects, the capabilities, the lexicon, the barriers, undo, the delta, the graph, the schema
model/lexicon/        a page per word in the grammar: 10 verbs, 9 object classes, 5 reach classes, 9 families
articles/             one article per release, with the screenshots taken from that release's own tag
examples/             five ABPs, derived from the data rather than authored
data/                 the published vocabulary as JSON, the graph, the lexicon, the bridges, the universes, the stored deltas and fact sets, the source bytes under upstream/ and the contributed bytes under contributed/
docs/                 every reference document, rendered, one click from its bytes
versions/             index.json, a file and a page per version
llms.txt              generated, and every page is in it
llms-full.txt         the whole site in one fetch
admin/build/          the generator
```

## Building it

```
python3 admin/build/build_pages.py    # regenerates every page, twin, llms.txt, CNAME, versions/
node admin/build/validate.js          # the release gate
```

**Nothing under `model/`, `articles/`, `examples/`, `data/` (except `upstream/` and `contributed/`, which are fetched bytes, never edited), `docs/*/`, `versions/`,
`llms.txt`, `sitemap.xml`, `robots.txt` or `CNAME` is edited by hand.** They are generated, and
CI fails a push whose committed tree does not match what the generator produces.

| File | What it owns |
|---|---|
| `admin/build/version.txt` | The version. CI derives the tag from it. |
| `admin/build/promote_data.py` | Promotes the upstream pack into the published vocabulary. |
| `admin/build/abp.py` | The model: the label, and the delta that is derived and never authored. |
| `admin/build/graph.py` | The edge vocabulary, the node type formulas, and the graph builder. |
| `admin/build/lexicon_pages.py` | A page per word in the grammar, and the grammar pages. |
| `admin/build/abp_pages.py` | Every page computed from the data. |
| `admin/build/docs_pages.py` | The docs section. |
| `admin/build/gmail_pages.py` | The mailbox walkthrough: four steps and the thirteen prompts. |
| `admin/build/cost_pages.py` | The cost walkthrough: an ABP over how much rather than what, twelve prompts and an accountant. |
| `admin/build/cases.py` | The cases: one person's estate of deployments, the mandates elicited, the grants mostly not yet measured. |
| `admin/build/case_session_001.py`, `case_estate_002.py` | One authored case each: the site's own session as a ledger, and three surfaces over one record. |
| `admin/build/articles.py` | One article per release, and the register the index is generated from. |
| `admin/build/figures.py` | The figures: sixteen diagrams and one chart, each with a markdown equivalent. |
| `admin/build/build_pages.py` | The authored pages, the nav, the footer, the version log. |
| `admin/build/shell.py` | One block list, two surfaces: the page and its markdown twin. |
| `admin/build/validate.js` | The release gate. A failure means no tag and no publish. |

## The data

`data/` is the published vocabulary: 23 capability primitives in `verb.object.reach` form, four
barriers, three undo classes, seven evidence tiers, sixteen deployment shapes and fifteen
starting mandates, plus the stored deltas and fact sets, at stable addresses with cross origin
access. Nine of the shapes were promoted from the capability map and seven were contributed by
riskmandate.ai and promoted from `data/contributed/riskmandate/`, where the bytes as fetched
sit unchanged with a hash per file; the two sets are counted beside each other and never
folded together.

**It was not authored here.** It is promoted from the capability map published at
[what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai/map/index.html), pack
v0.8.0, retrieved 2026-09-11. Nothing is renamed. The bytes as fetched are served unchanged
under `data/upstream/`, and both the build and the gate recompute their hash and refuse to
proceed if it disagrees.

**21 of 99 capability rows were measured** and the rest derived. Every page carrying capability
rows says so.

## The ontology is a graph, not a list of strings

**`read.file.project` is three nodes joined by three edges**, and each of them has an address,
a JSON file and a page. A node carries no inherent meaning: what a thing IS emerges from the
edges traceable from it.

- **The lexicon** (`/model/lexicon/`, `data/lexicon/`): every word the grammar is spelled with.
  The reach class pages are the ones to read, because the deployment shapes **disagree**
  about what `host` means and the page keeps the disagreement rather than averaging it.
- **The edge vocabulary** (`data/graph/edges.json`): 15 edges, each a verb with a distinct and
  meaningfully named inverse, a stated domain and a stated range. Four reused from the
  network's published edge set under their published names, eleven proposed here and marked as
  such. **There is no generic association edge and there will not be one.**
- **The node type formulas** (`data/graph/node-types.json`): a node type is a required pattern
  of typed, directed paths, not a label. `[Control] := a [Barrier] -enforced_by-> an [Enforcer]
  the [Grant] does not include`. Walked on every build; the gate fails unless exactly one
  barrier matches.
- **The three layers** (`/model/graph/layers/`, `data/bridges/`): shared facts owned by nobody,
  per-party formulas, declared bridges. This is how a customer vault disagrees with this
  vocabulary **without merging anything and without either side asking permission**.

Two words in the published grammar, `receive` and `revoke`, have no primitive under them. They
are kept and marked `unused` rather than dropped: a node connected to nothing is literally
meaningless, and the gap is a finding about the vocabulary rather than a defect in it.

## Contributing

**A proposal to a data file carries evidence**: a source URL, a retrieval timestamp and a
content hash. A proposal that changes a capability row without one is an assertion, and the
gate refuses it.

**A consumer pins a version.** Anything computing from these files states which version it
computed against. A clone that floats against the latest has no reproducible output.

## The rules this repository is built under

- **No score.** No rating, no traffic light, no risk level, no severity, on any page or in any
  data file. The gate checks it.
- **The delta is derived and never authored.** Nobody writes one. The gate recomputes every
  stored delta from its own pinned inputs and fails on a single row of disagreement.
- **A threshold crossing is a record; the consequence is a policy somebody set in advance.**
  Nothing here decides what follows from a number.
- **Every prohibition carries its barrier.** One shown without it manufactures assurance.
- **Every page with capability rows carries its provenance**: measured against derived, and when.
- **No adjective about a named third party product.** This site publishes capability claims
  about nine named commercial products, with a source, a timestamp and a hash on each.
- **Nothing here is an assessment, an audit, a certification or a security review** of anything
  or anybody, and every example page says so.
- **Never probe anybody's system to find out.** A row is measured only from a system we are
  entitled to run, or from the vendor's own published documentation.
- **Agent, never agentic. Never shorten ABP to `the policy'.** The gate checks both. <!-- gate:names-the-rule -->
- **Zero em dashes, zero en dashes, ASCII outside a declared set of five published glyphs.**
  The gate checks it, which makes this the first repository in the estate that holds it.

## Licence

The code is under the licence in `LICENSE`. The documents under `docs/` and the promoted data
are CC BY 4.0, and they carry their own licence lines.
