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
model/                the four objects, the 23 capabilities, the barriers, undo, the delta, the graph, the schema
examples/             five ABPs, derived from the data rather than authored
data/                 the published vocabulary as JSON, the stored deltas, and the source bytes under upstream/
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

**Nothing under `model/`, `examples/`, `data/` (except `upstream/`), `docs/*/`, `versions/`,
`llms.txt`, `sitemap.xml`, `robots.txt` or `CNAME` is edited by hand.** They are generated, and
CI fails a push whose committed tree does not match what the generator produces.

| File | What it owns |
|---|---|
| `admin/build/version.txt` | The version. CI derives the tag from it. |
| `admin/build/promote_data.py` | Promotes the upstream pack into the published vocabulary. |
| `admin/build/abp.py` | The model: the label, and the delta that is derived and never authored. |
| `admin/build/abp_pages.py` | Every page computed from the data. |
| `admin/build/docs_pages.py` | The docs section. |
| `admin/build/build_pages.py` | The authored pages, the nav, the footer, the version log. |
| `admin/build/shell.py` | One block list, two surfaces: the page and its markdown twin. |
| `admin/build/validate.js` | The release gate. A failure means no tag and no publish. |

## The data

`data/` is the published vocabulary: 23 capability primitives in `verb.object.reach` form, four
barriers, three undo classes, seven evidence tiers, nine deployment shapes and eight starting
mandates, plus the stored deltas, at stable addresses with cross origin access.

**It was not authored here.** It is promoted from the capability map published at
[what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai/map/index.html), pack
v0.8.0, retrieved 2026-09-11. Nothing is renamed. The bytes as fetched are served unchanged
under `data/upstream/`, and both the build and the gate recompute their hash and refuse to
proceed if it disagrees.

**21 of 99 capability rows were measured** and the rest derived. Every page carrying capability
rows says so.

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
