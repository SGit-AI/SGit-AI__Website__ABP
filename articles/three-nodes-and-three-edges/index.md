# v0.3.0: read.file.project was a string with a gloss beside it, which is schema-first thinking in graph syntax

> Thirty three words that existed only as substrings got a node, a file and a page each. A node type stopped being a label and became a formula the build walks. And the reach pages started keeping nine disagreeing definitions of one word instead of averaging them.

*Source: <https://abp.sgit.ai/articles/three-nodes-and-three-edges/index.html> · site v0.9.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Articles](../../articles/index.md) / v0.3.0

# v0.3.0: read.file.project was a string with a gloss beside it, which is schema-first thinking in graph syntax

Thirty three words that existed only as substrings got a node, a file and a page each. A node type stopped being a label and became a formula the build walks. And the reach pages started keeping nine disagreeing definitions of one word instead of averaging them.

> **This is the article for release v0.3.0, published 12 September 2026.** Every release of this site gets one, and it explains what that release changed and why rather than restating [v0.3.0's own release record](../../versions/v0.3.0/index.md). It is release 3 of 12 on this site. Every screenshot below was captured from a checkout of the `v0.3.0` tag, so it shows the site as it stood at that release and not as it stands today. Read on to [v0.4.0](../../articles/an-abp-is-a-junction-object/index.md), or back to [v0.2.0](../../articles/a-rule-corrected-nine-hours-later/index.md).

## The model pages were a projection of nothing

For two releases this site said, on the graph page, that an ABP is a graph and every document is a projection of it. It was not. A capability was an identifier with a gloss beside it, and the gloss was the definition.

> **That is a self-describing node, which is schema-first thinking dressed in graph syntax.** The meaning was attached to the node rather than derived from its edges. `read.file.project` was a string, so `read`, `file` and `project` were unaddressable: nothing could link to them, nothing could disagree with them, and a customer vault had nowhere to attach a bridge.

*[A figure here in the page: on the left, read.file.project as one string with a gloss beside it, the shape until v0.2.0. On the right, the same primitive as a node joined by has_verb to `read`, by acts_on to `file` and by reaches to `project`, each of which is a node with a page and a file of its own]*

![A table spelling out one primitive as five nodes joined by five named edges](../../assets/articles/v030-lexicon-spelled.png)

*One primitive, spelled out. Each of those is a link because each of those is a node with an address, a JSON file and a page of its own. (abp.sgit.ai at v0.3.0, captured 20 September 2026 from a checkout of the v0.3.0 tag.)*

## The page that carries the disagreement

The reach class pages are the ones to read, and `host` is the clearest case in the model. **The nine deployment shapes do not agree about what it means**, and the page keeps the disagreement rather than averaging it.

![Nine rows, one per deployment shape, each with that shape's own definition of the word host](../../assets/articles/v030-host-disagreement.png)

*Nine definitions of one word, none of them merged, each owned by the shape that said it. A reader deciding what `host` costs them has to read the row for the shape they run, not an average of the rows. (abp.sgit.ai at v0.3.0, captured 20 September 2026 from a checkout of the v0.3.0 tag.)*

**That is the ABP's own argument in one column.** The same word, the same grammar, and a materially different exposure depending on where the agent runs. It is also the first place on this site where zooming into a node lands you somewhere with its own vocabulary, which is the property the releases six months of releases later would be named after.

## Classification stopped being a label

Until this release a barrier carried `is_control: true`, which is a label somebody applied. A node type is now a **required pattern of typed, directed paths** that a node either matches or does not, and the build walks it.

![Thirteen node types, each with a formula and the count of nodes that matched](../../assets/articles/v030-formulas-table.png)

*Thirteen formulas, walked against the graph on every build. The counts are the result of running them rather than fields anybody set, which is why a formula that stops matching is a finding rather than a cosmetic change. (abp.sgit.ai at v0.3.0, captured 20 September 2026 from a checkout of the v0.3.0 tag.)*

![The Control formula, with a table showing which of the four barriers matches it](../../assets/articles/v030-control-formula.png)

*The one that carries the argument. Exactly one of the four barriers matches, and the release gate fails if that stops being true, because every page on this site is written against it. (abp.sgit.ai at v0.3.0, captured 20 September 2026 from a checkout of the v0.3.0 tag.)*

**Judgment does not disappear**, and that objection deserves a direct answer. Somebody still decided that a control must be enforced from outside the grant. What changes is where that decision lives: out of a classifier's head and into a formula that is visible, versioned, inspectable and arguable. You can now disagree with a classification by pointing at a line, which you could not do before.

## Fifteen edges, and no generic one

The edge vocabulary arrived in the same release: fifteen edges, each a verb with a distinct and meaningfully named inverse, a stated domain and a stated range. **The inverse is not the same edge walked backwards**: `grants` and `granted_by` have different fan out, and that asymmetry is what stops a traversal exploding.

> **There is no generic association edge in this model and there will not be one.** It constrains nothing and costs fan out. If you find yourself wanting one, the honest move is a new edge with a sentence, a different sentence for its inverse, and a stated domain and range. Four of the fifteen are reused from the network's published edge set under their published names; eleven are proposed here and say so.

## The construction a customer vault needs

A customer will disagree with some of this vocabulary, and they will often be right about their own estate. **The wrong response is to merge their definitions into these**, because merging is destructive and what it destroys is the finding.

![A table of this site's formulas beside a customer's stricter versions of them](../../assets/articles/v030-layers.png)

*Layer two: each party classifies the same shared nodes with its own rules. A regulated customer who requires a control to be evidenced as well as enforced writes their own formula over the same facts, and both numbers are correct. (abp.sgit.ai at v0.3.0, captured 20 September 2026 from a checkout of the v0.3.0 tag.)*

**Parties can disagree about meaning while still agreeing about facts**, which is the only stable basis for working together. A customer who cannot accept this site's definition of a control can still accept that their agent can read every file the account can reach, and that is the sentence the ABP needed them to reach.

## What the gate found on its first run

A thirteenth check arrived with the graph, and it found something immediately: **`receive` and `revoke` are in the published verb list and no primitive uses them.**

> **They are kept and marked rather than dropped.** A node connected to nothing is literally meaningless, so those two words mean nothing in this graph yet, and saying so is more useful than writing them a definition no edge supports. It is a finding about the vocabulary rather than a defect in it, and it is the kind of gap that only becomes visible once the words are nodes.

[The lexicon](../../model/lexicon/index.md) &#183; [The edge vocabulary](../../model/graph/edges/index.md) &#183; [The node type formulas](../../model/graph/formulas/index.md) &#183; [The three layers](../../model/graph/layers/index.md) &#183; [v0.3.0's own release record](../../versions/v0.3.0/index.md)

## Read the sequence

| Direction | The release |
|---|---|
| **Older** | [v0.2.0: A rule this site published in the morning was wrong by the afternoon, and the correction is on the page](../../articles/a-rule-corrected-nine-hours-later/index.md) |
| **Newer** | [v0.4.0: An ABP is a junction object, which is what Fractal Semantic Graphs is for](../../articles/an-abp-is-a-junction-object/index.md) |
| **All of them** | [One article per release](../../articles/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/articles/three-nodes-and-three-edges/index.html)*
