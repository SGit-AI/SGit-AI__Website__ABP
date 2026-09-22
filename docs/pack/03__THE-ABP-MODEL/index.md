# The ABP Model

> The ABP describes. It does not judge. It states what the agent can do, what it was authorised to do, the gap between them, and what stands in the way. It says nothing about whether any of that is acceptable, because acceptability is not in...

*Source: <https://abp.sgit.ai/docs/pack/03__THE-ABP-MODEL/index.html> · site v0.8.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The pack](../../../docs/index.md#pack) / The ABP Model

# The ABP Model

> **The source bytes.** This page is generated from [`docs/pack/03__THE-ABP-MODEL.md`](../../../docs/pack/03__THE-ABP-MODEL.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

## The ABP is consequence agnostic, and that is the rule above every other rule

**The ABP describes. It does not judge.** It states what the agent can do, what it was authorised to do, the gap between them, and what stands in the way. It says nothing about whether any of that is acceptable, because acceptability is not in the document.

**The same ABP is dangerous in one room and harmless in the next, and nothing about the document changed.** The most permissive grant imaginable, running where there are no assets and nothing reachable, is a low risk. The same grant dropped into a production estate is an extreme one. The same grant tomorrow, after somebody connects a database, is a different risk again. **Risk is a function of the policy, the assets, the consequences and the date, and the ABP is the one input that does not move.**

**A policy cannot be dangerous. A deployment can.**

**Four consequences, and every one is a build decision.**

**The ABP carries no score.** No rating, no traffic light, no risk level, no severity, nowhere on this site. Every buyer will ask for one in the first meeting. **The score has a home and it is the risk product**, where the assets are known, the risk acceptance workflow exists, and a named professional signs. Putting a score on the ABP is the fastest way to make the document wrong in one of the two rooms.

**The record is what is sold, and the verdict is a service.** A description of the grant rots on a known clock: the product releases, the deployment changes. A verdict rots on an unknown one: anything in the environment moves. **The record is re-sellable because its clock is visible. The verdict is not, because its clock is not.**

**A long list is an inventory, not an admission.** The ABP asserts that a capability exists, never that a risk is unacceptable. That is materially different from a findings register, and it is worth drafting toward, with the honest caveat that it moves an exposure rather than removing it.

**The correction in the draft and correction sale is factual, not evaluative.** Nobody is asked to agree that something is dangerous. They are asked whether their agent can do a thing. That is a conversation you can have with somebody who knows their business better than you do.

**The three part structure this gives the ladder, which the project lead has adopted:**

| Part | What it is | Who owns it | Sold as |
|---|---|---|---|
| **The label** | The ABP. Describes the capability, context free | Us | The first product |
| **The patient record** | The twin. The interface to the real environment: assets, tools, data, what is connected | Us, hooked to the customer's reality | The first product, with the ABP |
| **The prescription** | The risk score and the acceptance. Combines the two and is signed | **A named professional who did not sell the first two** | The uplift |

**The third row is a constraint, not a preference.** The standing rule is that the people who sell do not sign. So the party that sells the label and the record cannot be the party that prescribes. **That is why the sequence separates cleanly.**

**Every ABP carries a validity statement.** Not an expiry meaning stale, but: *this describes the deployment shape as at this date; if the risk changed, the deployment changed, not this document.* The conformance vault already does this with attestations carrying a tier and an expiry.

**Two places where the principle, taken seriously, corrects our own data.**

**The undo class is the one column that is not fully context free.** Whether deleting a file is reversible depends on backups, snapshots and retention. So `undo: no` is a claim about the product's published behaviour, and the page says so, and says that the deployment can change it. Otherwise one contextual judgement has been smuggled into a document that claims to hold none.

**No assets does not mean no consequence.** It means no consequence to you. An agent with `send.endpoint.world` and `execute.process.host` in an empty environment can still reach third parties. That is the sub delegation argument in another form, and it is a reason the consequence model is genuinely hard and genuinely not ours to guess.

**Two known gaps in the model, stated plainly and not decorated.**

**Quantity is not modelled.** The twenty three primitives carry reach, being project, host, tenant, world and self, and they do not carry rate or volume. `send.endpoint.world` is the same primitive for one request and a million. The temporal operators in the policy language named in the second brief, count within and sum within, are the shape of the fix.

**Interaction between agents is not modelled.** Two agents each within mandate can compose into something neither was authorised to do. There is no primitive for it and no page for it.

## The label: what goes on the outside

**The project lead asked for a couple of metrics and a couple of abstraction layers.** Two layers, and the graph they are computed from.

**The label** is one line, on the outside, for anybody:

| Field | Meaning |
|---|---|
| **Shape** | The named deployment, in the product's published words |
| **Grant** | N of 23 primitives |
| **Mandate** | M primitives |
| **Excess** | Capabilities in the grant and not in the mandate. **The finding** |
| **Unbounded excess** | Excess capabilities whose barrier is one of the first three rows. **The business case** |
| **Irreversible** | Granted capabilities with `undo: no`, as published |
| **Widest reach** | The furthest reach class in the grant |
| **Measured** | Rows measured against rows derived |
| **As at** | The date and the source version |

**The two headline numbers are excess and unbounded excess.** The first answers the buyer's question, what can it do that I did not ask for. The second is the purchase: every control bought moves a capability from the first three barrier rows to the fourth, and the number goes down. **The ratio between them is what a control purchase changes, and it is the only number on the label that a buyer can move.**

**The leaflet** is the full table underneath: every primitive with its barrier, its undo class, its provenance, and the mandate beside it. For the engineer, the auditor and the underwriter.

**Neither carries a score. Both carry the validity line.**

**Ordering.** The default order on every rendering is irreversible first, because reversibility is a property of the action rather than of the context, and stating it as the reason keeps the ordering descriptive. The risk product reorders by consequence, because it knows the consequence.

## The four objects

An ABP is not a document. It is four objects, of which the document is a rendering.

| Object | How it is obtained | What it is |
|---|---|---|
| **The mandate** | **Elicited**, in minutes, because the deployer already knows it | What the agent is authorised and expected to do |
| **The grant** | **Measured**, from the deployment shape and the credentials | Everything the agent can do |
| **The delta** | **Computed, never stored** | The excess authority, and the shortfall |
| **The prohibitions** | The enforceable projection of the delta | The subset a control can bound, each carrying the layer it is enforced at |

**The order matters and the site should teach it in this order.** A grant alone is an inventory and a buyer shrugs at an inventory. A grant with a mandate beside it is a finding. **Three hundred and forty things is a shrug. Three hundred and forty things and you authorised twelve is a sale.**

## The capability grammar, which exists

`verb.object.reach`. Twenty three primitives, published on the map page. Examples in their published wording:

| Primitive | Published gloss |
|---|---|
| `read.file.project` | Read the project it is working on |
| `write.file.host` | Change any file the account can reach |
| `execute.process.host` | Run programs as the account |
| `send.endpoint.world` | Reach any host on the internet |
| `read.credential.host` | Read credentials stored where it runs |
| `write.repository.tenant` | Push to a code host |
| `create.schedule.host` | Create something that outlives the turn |
| `read.record.browsing` | Read every page you visit |

**Reach classes:** `project`, `host`, `tenant`, `world`, `self`.

**This grammar is the action vocabulary for everything else on the site.** Do not add a primitive without adding it to the published set, and do not rename one.

## The barrier, which is the enforcement model and already exists

Every capability in a profile carries a barrier glyph. The published wording for what it means:

> what stands between it and the capability: nothing, a rule somebody wrote down, a setting the agent's own account could change, or a boundary enforced above it that it cannot reach

**Those four are the enforcement layers, and the third and fourth are the whole argument.**

| Barrier | Is it a control | Why |
|---|---|---|
| Nothing | **No** | Unbounded |
| A rule somebody wrote down | **No** | A prompt or a prose rule. All four major model providers state in their own 2026 words that instructions at this layer can be bypassed |
| A setting the agent's own account could change | **No** | **The grant includes the ability to remove the bound** |
| A boundary enforced above it that it cannot reach | **Yes** | The only row that bounds anything |

**The third row is the enforcer test of 20 August, published as a glyph before it was named as a rule:** a control bounds a grant only if it is enforced by something the grant does not include.

**So every prohibition rendered anywhere on this site carries its barrier.** A prohibition displayed without one is a claim the site cannot support, and the assessment product exists to find the ones sitting at the second and third rows.

## The undo class, which is the severity model

The map already carries it: `yes`, `with-effort`, `no`, with the published note that **a capability that cannot be undone is a different kind of thing from one that can**.

**Use it as the ordering on every rendering.** An ABP that lists prohibitions alphabetically has buried the only ones that matter. Irreversible and unbounded is the first row of every document this site produces.

## The graph rules, which govern the model

Five rules, published at `graphs.sgit.ai`, and they are not stylistic.

1. **Every edge is a verb with a distinct inverse.** The inverse is not the same edge walked backwards: `owned_by` and `owns` have different fan out.
2. **The generic association edge is banned.** It constrains nothing and costs fan out.
3. **Never render the whole graph.** Render the result of a query.
4. **Rich nodes are acceptable.** The blob is a rendering failure, not a modelling one.
5. **If a path does not read as a sentence in the reader's own language, the edges are wrong.**

**Rule five is the acceptance test for this model, and it is cheap to apply.** The path should read:

> agent `claude-code-cli-confirmations-disabled` **is-granted** capability `execute.process.host` **bounded-by** barrier `a-rule-somebody-wrote-down` **which-exceeds** mandate `ship-a-feature` **and-is** undo `no`

If a path does not read like that, the edges are wrong and the model changes, not the renderer.

**Rule three is the answer to the memo's wish that every word be hyperlinked.** Every word can be a node and no page renders the graph. Each page renders one query: this profile's grant, this mandate's delta, this capability across all profiles.

## The five layers, and the tension nobody has stated

The memo says the book's five layers are what is happening here, and they are, with one complication that must be written down before the renderer is built.

**The book is a five level compression hierarchy**, and it states that **a class name does not mean the same thing two levels up**, because ontologies and taxonomies differ structurally across altitudes.

**The variant rule, in force since August, says every variant renders the same fact set and the diff must be empty.**

**Those two are in tension and the resolution is precise: the facts are identical across renderings, the classes are not.**

- **The fact set** is the leaf assertions: this profile has this capability, at this barrier, with this undo class; this mandate contains these capabilities; therefore this delta. **Identical in every rendering. The diff is over these.**
- **The classes** are how those facts are grouped for a reader: an executive rendering may group by business consequence, an engineer's by reach and barrier. **Different at different altitudes, and that is correct rather than a defect.**

**Write that down as the specification for the fact diff**, because the fact diff is the thing that has blocked a promise on each of the last four days, and this is the first statement precise enough to build it from. **The diff is over leaf assertions, not over structure.**

**Keep altitude for stakeholder and depth for detail.** That ruling is from 20 August and the layers here are altitudes.

## The vocabulary for the interchange form

The graph has a W3C vocabulary already, and the second brief in `briefs/` covers it with its limits. In short: a policy carries permissions, prohibitions and duties; constraints cover time, purpose, count and place; the conflict strategy says **prohibitions win**; and a policy inherits from a parent, which is how policy for an agent in an environment extends policy for an agent.

**Use it as the interchange vocabulary through a profile that adds these capability primitives as actions. Do not claim it enforces anything, because it does not.** The compile target for enforcement is named in the brief.

## What the site must never compute

**The delta is computed and never stored.** That is a standing ruling. A stored delta is a stale claim about somebody's environment, and the environment is the thing that changes.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/pack/03__THE-ABP-MODEL/index.html)*
