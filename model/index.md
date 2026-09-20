# The model

> The four objects an ABP is made of, the grammar they are written in, the barrier that decides whether anything is in the way, and the graph rules that govern all of it.

*Source: <https://abp.sgit.ai/model/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The model

# The model

An ABP is not a document. It is four objects, of which the document is a rendering. The order they are produced in is the order this page teaches them, because a grant without a mandate beside it is an inventory and nobody acts on an inventory.

## The four objects

| Object | What it is | How it is obtained |
|---|---|---|
| **The mandate** | What the agent is authorised and expected to do | **Elicited.** In minutes, because the deployer already knows it |
| **The grant** | Everything the agent can do | **Measured.** From the deployment shape: the product, where it runs, with what account, with what credentials |
| **The delta** | The difference. Excess where it can and you did not ask; shortfall where you asked and it cannot | **Derived.** Recomputed whenever the grant or the mandate changes, stored with the versions of both, and never edited by hand |
| **The barrier** | What stands between the agent and each capability | **Recorded**, per capability, from one of four kinds |

**Three hundred and forty things is a shrug. Three hundred and forty things and you authorised twelve is a finding.** The mandate is the edge that gives the grant a shape, and it has to be captured even though it is already known.

## Why the delta is derived and never authored

> **Nobody writes a delta.** It is only ever the output of a computation over the grant and the mandate, and it is stored along with the versions of both inputs and the time it was computed. That is what makes it checkable rather than stale. [What follows from that](../model/delta/index.md), including why this site said the opposite this morning.

## The pieces

**[The capability grammar](../model/capabilities/index.md)**: `verb.object.reach`. 23 primitives, each with the undo class of its effect.
Promoted from the published map. Nothing renamed.

**[The barrier](../model/barriers/index.md)**: Four kinds, and only the fourth bounds anything.
The enforcer test, published as a glyph before it was named as a rule.

**[The undo class](../model/undo/index.md)**: Three classes, and the ordering on every rendering this site produces.
A property of the action. Not a severity.

**[The lexicon](../model/lexicon/index.md)**: Every word the grammar is spelled with, as a node with its own address: ten verbs, nine object classes, five reach classes, nine families.
`read.file.project` is three nodes, not a string.

**[The delta](../model/delta/index.md)**: Derived and never authored. Stored with its inputs pinned, recomputed when either moves, and never edited by hand.
Corrected on 11 September, in the open.

**[The graph](../model/graph/index.md)**: Five rules that govern the model rather than the styling.
Rule five is the acceptance test and it is cheap to apply.

**[The universes](../model/universes/index.md)**: One capability row walked through nine worlds, from the source bytes to a licence condition, each with its own owner and ontology.
An ABP is a junction object. This is Fractal Semantic Graphs applied to it.

**[The schema](../model/schema/index.md)**: What is in the published files, and what a consumer has to state.
A consumer pins a version.

**[The five examples](../examples/index.md)**: Five ABPs, derived from the data rather than authored.
Each states which rows were measured and which derived.

## What is deliberately not modelled

**Quantity.** The primitives carry reach and not rate. `send.endpoint.world` is the same primitive for one request and a million. The temporal operators of a policy language, count-within and sum-within, are the shape of the fix and they are not here yet.

**Interaction between agents.** Two agents each within mandate can compose into something neither was authorised to do. There is no primitive for it and this is the only sentence about it on the site.

**Consequence.** Deliberately, and it is the rule above every other rule on this site. No assets, no consequences, no score. That is not modesty: **no assets does not mean no consequence, it means no consequence to you.** An agent with `send.endpoint.world` and `execute.process.host` in an empty environment can still reach third parties.

> **Provenance.** 21 of 99 capability rows on this page were measured, meaning seen directly on the thing itself. The other 78 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../data/upstream/pack.json).

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/model/index.html)*
