# The graph

> The five published graph rules, what they force on this model, and the sentence test that decides whether the edges are right.

*Source: <https://abp.sgit.ai/model/graph/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The graph

# The graph

An ABP is a graph and every document is a projection of it. The five rules that govern it are published at [graphs.sgit.ai](https://graphs.sgit.ai/) and they govern the model rather than the styling. This page says what each one forces here.

| Rule | What it forces on this model |
|---|---|
| **Every edge is a verb with a distinct inverse.** | `is-granted` and `granted-to` are different edges with different fan out. The inverse is not the same edge walked backwards. |
| **The generic association edge is banned.** | There is no `relates-to` anywhere in this model. It constrains nothing and costs fan out. |
| **Never render the whole graph. Render the result of a query.** | There is no map of everything on this site. Each page answers one query: this shape's grant, this mandate's delta, this capability across every shape. |
| **Rich nodes are acceptable.** | A capability node carries its verb, object, reach, undo class and gloss. The blob is a rendering failure, not a modelling one. |
| **If a path does not read as a sentence in the reader's own language, the edges are wrong.** | The acceptance test, below. If a path fails it, the model changes and not the renderer. |

## Where the rules landed

| Address | What is there |
|---|---|
| [The lexicon](../../model/lexicon/index.md) | Every word the grammar is spelled with, as a node with its own address. `read.file.project` is three nodes and three edges. |
| [The edge vocabulary](../../model/graph/edges/index.md) | 15 edges, each a verb with a distinct inverse, a stated domain and range. No generic association edge. |
| [The node type formulas](../../model/graph/formulas/index.md) | Classification as a required path pattern, run on every build, rather than a label somebody applied. |
| [The three layers](../../model/graph/layers/index.md) | How a customer vault disagrees with this vocabulary without merging anything. |
| [The nine universes](../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md) | The map of the ABP onto Fractal Semantic Graphs: one capability row crosses nine universes, each with its own owner and ontology, joined by named edges. A brief at v0.4.0; the universes land one per release after it. |

## The sentence test

> agent `claude-code-cli-confirmations-disabled` **is-granted** capability `execute.process.host` **bounded-by** barrier `a-rule-somebody-wrote-down` **which-exceeds** mandate `ship-a-feature` **and-is** undo `no`

Every example page ends with that path, built from its own data, so the test is applied on every build rather than asserted once here.

## The five layers, and the tension in them

A five level compression hierarchy says a class name does not mean the same thing two levels up. The variant rule says every rendering must produce the same fact set, with an empty diff. Both are true, and the resolution is precise:

- **The fact set is the leaf assertions**: this shape has this capability, at this barrier, with this undo class; this mandate contains these capabilities; therefore this delta. **Identical in every rendering, and the diff is over these.**
- **The classes are how those facts are grouped for a reader.** An executive rendering groups by business consequence, an engineer's by reach and barrier. **Different at different altitudes, and that is correct rather than a defect.**

**So the fact diff is over leaf assertions, not over structure.** The label and the leaflet on every example page are two renderings of one fact set, and keeping them that way is why both are generated from the same call.

**Altitude is for stakeholder, depth is for detail.** The layers here are altitudes.

## The interchange vocabulary

The W3C has had a rights expression vocabulary since 2018: a policy carries permissions, prohibitions and duties, constraints cover time, purpose, count and place, the conflict strategy says **prohibitions win**, and a policy inherits from a parent, which is how a policy for an agent in an environment extends a policy for an agent. Use it as the interchange form through a profile that adds these capability primitives as actions.

> **Do not claim it enforces anything, because it does not.** It is a vocabulary for expressing a policy, not a thing that stands in the way. In the barrier's terms an interchange document is a rule somebody wrote down until something above the grant compiles it and enforces it.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/graph/index.html)*
