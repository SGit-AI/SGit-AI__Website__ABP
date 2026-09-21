# The three layers

> How a customer vault extends this vocabulary without merging anything: shared facts owned by nobody, per-party formulas, and declared bridges. Parties can disagree about meaning while still agreeing about facts.

*Source: <https://abp.sgit.ai/model/graph/layers/index.html> · site v0.5.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The graph](../../../model/graph/index.md) / The three layers

# The three layers

**A customer will disagree with some of this vocabulary, and they will often be right about their own estate.** The wrong response is to merge their definitions into these, because merging is a destructive operation and what it destroys is the finding. The right response is three layers.

## Layer 1: shared facts, owned by nobody

The factual graph, published here: **23 capability primitives**, **10 verbs**, **9 object classes**, **5 reach classes**, **4 barriers**, **16 deployment shapes** and what each one grants. **Nobody has to agree about what any of it means to agree that it is the case.**

> **This layer is free, public, versioned and hash verified, and it stays that way.** It lives at [`/data/`](../../../data/index.md) with cross origin access, so a vault reads it over the network rather than forking it. A consumer pins a version, because a clone that floats against the latest has no reproducible output.

## Layer 2: per-party formulas

**Each party classifies those shared nodes with its own rules.** A node type here is [a formula rather than a label](../../../model/graph/formulas/index.md), which is exactly what makes this possible: a customer does not need us to change a field, they write their own formula over the same facts.

| The formula here | A customer's version, and why |
|---|---|
| `[Control] := a [Barrier] -enforced_by-> an [Enforcer] the [Grant] does not include` | A regulated customer may require a control to be **evidenced as well as enforced**: `... and -backed_by-> [Evidence] -observed_on-> [System]`. Their unbounded excess is then higher than ours, on the same facts, and both numbers are correct. |
| `[Excess] := a [GrantedCapability] with no -authorised_by-> path` | A customer whose mandates are written per role rather than per deployment computes the same delta against a different mandate node. The capability rows do not move. |
| The five reach classes | An estate with a hard tenancy boundary may split `tenant` into two nodes. **They add nodes in their own vault; ours are untouched.** |

**Three different answers over one set of facts, each internally consistent, each inspectable.** None of them requires this site to change.

## Layer 3: declared bridges

**Explicit edges connecting the two vocabularies at specific points**, owned by whoever declared them and revisable without renegotiating anything. The edge is `similar_to`, it is symmetric, and it is partial on purpose.

> our [`read.record.browsing`](../../../model/capabilities/read.record.browsing/index.md) **similar_to** their `PII.access.browser`
> 
> Partial. Traversable. Arguable. And crucially: **a third party can add that edge without touching either node.** You do not need our permission, and we do not need yours. [Why anchor nodes rather than conformance claims](https://graphs.sgit.ai/v1/grammar/index.html#anchor-nodes).

**The wrong move is a conformance claim**: *we are compliant with vocabulary X*. That is all or nothing, and it is usually a lie by the second field. **Partial mapping is the normal case, not a defect.**

## What a vault actually holds

A customer vault is layers 2 and 3, pointing at layer 1 by address, version and hash. It does not fork the facts.

| In the vault | Not in the vault |
|---|---|
| Their mandates, in their own words | The capability primitives, which are read from here |
| Their formulas, including their own definition of a control | Our formulas, which are read from here |
| Their bridges to our vocabulary, and to any other | Any merged vocabulary, because there is none |
| Their deployment shapes, measured from their own estate | The 16 published shapes, which are read from here |
| Their stored deltas, derived and never authored | Anything they authored by hand into a delta |

> **And the version they pinned.** Anything computing from these files states which version it computed against, so a delta produced in the vault in March can be recomputed in September and the difference attributed to the right side. That is the same rule the [stored deltas](../../../model/delta/index.md) follow here.

## Why this is one mechanism rather than two

**Customisation and consolidation are the same operation.** Do not store a consolidated text and maintain it; hold the base plus the amendments and compute the result. A customer's vocabulary is the base plus their amendments, and so is ours, and so is the next customer's. There is no special case for the customer who disagrees, which is the test of whether the model is actually fractal: **the grammar survives every zoom and the ontology does not have to.** A customer's vault is a new ontology joined to this one by a named edge, which is the claim working; a system whose types and verbs are identical all the way down is a hierarchy. (Until v0.4.0 this sentence stated the test the other way round, as one format everywhere; the correction is graphs.sgit.ai's own, taken at its v0.6.21.)

> **The claim that carries this whole page.** Parties can disagree about meaning while still agreeing about facts, **which is the only stable basis for working together.** A customer who cannot accept our definition of a control can still accept that their agent can read every file the account can reach, and that is the sentence the ABP needed them to reach.

[The declared bridges as JSON](../../../data/bridges/index.json) · [The lexicon](../../../model/lexicon/index.md) · [Why vocabularies are bridged rather than merged](https://graphs.sgit.ai/v1/depth/index.html)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/graph/layers/index.html)*
