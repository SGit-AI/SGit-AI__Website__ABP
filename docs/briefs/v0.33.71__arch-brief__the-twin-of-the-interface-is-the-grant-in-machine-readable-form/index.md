# The Twin Of The Interface Is The Grant In Machine Readable Form: Three Twins Are Needed Rather Than One, And The Mandate Check Becomes A Traversal Between Them

> version v0.33.71 date 20 September 2026 from Human (project lead) to Architecture, the Agent Behaviour Policy team, and whoever builds the first mailbox vault

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__the-twin-of-the-interface-is-the-grant-in-machine-readable-form/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / The Twin Of The Interface Is The Grant In Machine Readable Form: Three Twins Are Needed Rather Than One, And The Mandate Check Becomes A Traversal Between Them

# The Twin Of The Interface Is The Grant In Machine Readable Form: Three Twins Are Needed Rather Than One, And The Mandate Check Becomes A Traversal Between Them

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.71__arch-brief__the-twin-of-the-interface-is-the-grant-in-machine-readable-form.md`](../../../docs/briefs/v0.33.71__arch-brief__the-twin-of-the-interface-is-the-grant-in-machine-readable-form.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.71 **date** 20 September 2026 **from** Human (project lead) **to** Architecture, the Agent Behaviour Policy team, and whoever builds the first mailbox vault

**type** Architecture brief

*Sixth of the mailbox series, written as part of the handover pack for a session that will build the first working vault. The memo of 20 September asks for twins to be used inside the semantic graphs and, separately, for a twin of the mail platform's interface and a twin of the assistant's connector to that interface. This brief settles what a twin is here, argues that three are needed rather than two, and identifies what a twin actually buys, which is larger than a test harness. Limitations: no twin has been built; the field lists below are sketched from the interface facts established in the four earlier mailbox briefs and are not a complete reading of the platform's reference; the connector's tool surface has not been enumerated against a live deployment and that enumeration is the first task in the build order; and the word twin is used here in one of the two senses it has been given this week, with the other sense left needing a name.*

## What This Is

Three representations, what each is for, and the join that makes the mandate computable: **the memo asks for a twin of the mail platform's programming interface and a twin of the assistant's connector to it, and notes that twins will also be used inside the semantic graphs; settling the word first, a twin here is a modelled representation of a system that the estate does not control, written in the estate's own grammar, kept in step with the original and carrying the date and source of every claim, which is the sense the engineering world already gives the term and is not the sense used in the tool site memo of 19 September, where a twin was an actor that performs actions, so the second sense still needs a different word before either reaches a page; three twins are needed rather than the two the memo names, being the platform interface, the assistant's connector, and the mailbox itself, because they sit at three different layers of the enforcer ladder and carry three different barrier kinds; the first of these is worth more than a test harness, because a complete twin of the interface is the grant in machine readable form, so the grant column of a behaviour policy can be derived from it rather than authored, which is the ruling of 11 September satisfied by construction rather than by discipline; the second is where the interesting gap lives, since a connector typically exposes fewer capabilities than its authorisation grants, and the difference between what the scopes permit and what the tools offer is a real if weak barrier that nobody currently records; the third is the sample mailbox already argued for, whose value is that the whole pipeline can be exercised and attacked with no credential in existence; and the payoff that justifies building all three is that the mandate check stops being a rule engine and becomes a traversal, because a requested action in the message universe can be joined by a named edge to a method in the interface universe, and from there to the scope it requires, the reach it has and whether it can be undone, which means the question of whether an agent may do a thing is answered by walking a graph rather than by consulting prose.** New contributions: **the word settled in one sense with the other left open; three twins rather than two, each mapped to a layer of the enforcer ladder; the twin of the interface identified as the grant itself, which changes what it is for; the connector gap named as an unrecorded barrier; the mandate check expressed as a traversal with the joining edges given; a staleness discipline, since a twin of something you do not control is wrong the moment the original changes; and the minimum viable version of each twin for the first build.**

## What A Twin Is Here, And What It Is Not

**A twin is a modelled representation of a system the estate does not control, written in the estate's own grammar, kept in step with the original, with every claim carrying its source and the date it was last verified.**

**It is not a copy, a mock or a stub.** A mock imitates behaviour for a test. A twin describes a system so that questions can be asked of the description. The distinction matters because the first thing anybody will try to build is a mock, and a mock cannot answer the question this design needs answered, which is what the real thing permits.

**And it is not the other thing the word was used for this week.** The memo of 19 September used twin for the primitive that performs actions and triggers connections, which is an actor. A representation and an actor are different objects and the term cannot carry both. **The recommendation stands: keep twin for the representation, since that matches the settled engineering meaning, and find a plain word for the actor before either appears on a page.**

## Three Twins, Not Two, Because There Are Three Layers

**The ladder of enforcers established on 20 September says the barrier kind is a property of the layer. Each twin describes one layer and inherits its barrier kind.**

| Twin | What it models | Whose enforcement | Barrier kind at that layer |
|---|---|---|---|
| **Interface twin** | The mail platform's programming interface: scopes, methods, objects, limits, reversibility | The platform, which is outside everything above it | **Boundary** |
| **Connector twin** | The assistant's tool surface over that interface: which tools exist, what each calls, what triggers a prompt | The vendor's product, outside the model | Boundary in form, expectation in effect |
| **Mailbox twin** | One user's actual mail, labels, threads and read state, as data | Nobody. It is the subject, not a control | Not applicable |

**The memo names the first two. The third has already been argued for** as the sample mailbox that lets the pipeline be exercised with no credential in existence, and it belongs in the same family because it is built the same way and lives in the same vault.

## The Interface Twin Is The Grant

**This is the finding that changes what the twin is for.**

**A behaviour policy has four objects: the grant, the mandate, the delta and the barrier. The grant is everything the agent can do, and the standing ruling is that the delta is derived and never authored.** For that derivation to be honest the grant must itself be derived, and until now the grant has been assembled by reading documentation and writing rows.

**A complete twin of the interface removes that step.** If the twin holds every scope with its sensitivity tier, every method with the scopes it requires, the object class it touches, the reach it has and whether its effect can be undone, then the grant for a given authorisation is a query: **which methods are reachable with the scopes this deployment holds.** Nobody writes the rows. The rows fall out.

**Shape of it, in the estate's own grammar.** Nodes are typed, edges are verbs with inverses, properties carry data and never meaning.

```
(Scope  id=gmail.labels  tier=non-sensitive)
(Scope  id=gmail.send    tier=sensitive)
(Scope  id=gmail.modify  tier=restricted)

(Method id=labels.delete)
   --requires_scope-->  (Scope gmail.labels)
   --mutates-->         (ObjectClass Label)
   --has_reach-->       (Reach tenant)
   --undo_class-->      (Undo none)          # no recovery path exists

(Method id=messages.batchModify)
   --requires_scope-->  (Scope gmail.modify)
   --mutates-->         (ObjectClass Message)
   --bounded_by-->      (Limit ids_per_request=1000)
   --returns-->         (Response empty)     # no receipt

(Method id=drafts.create)  --requires_scope--> (Scope gmail.compose)
(Method id=drafts.send)    --requires_scope--> (Scope gmail.compose)
```

**Those last two lines are the whole reason to build this.** The finding that no scope permits drafting without permitting sending took a direct reading of two reference pages to establish. In a twin it is a one line query: which pairs of methods share a required scope while differing in consequence. **A twin turns a finding that had to be noticed into a finding that can be asked for.**

**Minimum viable interface twin, for the first build:** the seven or eight scopes with their tiers, the dozen methods this workflow can reach, and for each method the scope, object class, reach, undo class and any hard limit. Perhaps sixty nodes. Every one carrying the reference page it came from and the date it was read.

## The Connector Twin Is Where The Unrecorded Gap Lives

**The interface twin says what the platform permits. The connector twin says what the assistant is actually offered, and the two are not the same.**

**A connector typically exposes fewer capabilities than its authorisation grants.** The scopes may permit label deletion while the tool surface offers no delete tool. That difference is a real constraint on what can happen, it is enforced by the vendor's product rather than by the model, and **nobody currently records it anywhere.**

**So the connector twin has its own node type and one important edge back to the first twin.**

```
(Tool id=send_email  surfaced_by=connector)
   --invokes-->          (Method messages.send)
   --gated_by-->         (Approval per-action  default=on  overridable_by=workspace-owner)
   --prompt_shows-->     (Field action_class)   # and not the object, the count or the reversibility

(Scope gmail.labels) --granted_but_unreachable--> (Gap no-tool-surfaces-label-deletion)
```

**Three things fall out of that and each is useful on its own.**

**The unreachable set is a barrier worth naming.** Capabilities the authorisation grants and the tool surface does not offer are bounded by the vendor's product. Weak, because a product update can surface a tool tomorrow, and real today. **It should appear in a behaviour policy as a barrier with a stated expiry, which is what the barrier expiry field proposed on 12 September was for.**

**The approval gate becomes a property rather than a claim.** Which tools prompt, what the prompt displays, and who can turn it off are fields, so the finding that the prompt names an action class and not its object stops being an observation in a brief and becomes a value in a graph.

**And the delta between the two twins is computable.** What the scopes permit, minus what the tools offer, is the gap a platform update could close without anybody being told.

**Minimum viable connector twin:** enumerate the tools the connector actually surfaces in a live deployment, map each to a method in the interface twin, and record the approval behaviour of each. **This enumeration has not been done and it is the first task in the build order**, because everything downstream depends on knowing what the tool surface actually is rather than what the documentation implies.

## The Mandate Check Becomes A Traversal

**This is the payoff, and it is what makes the twins worth the effort rather than merely tidy.**

**The previous brief established that a message becomes a graph in which a request is a proposition: `(Message) --requests--> (RequestedAction)`.** The twins supply the other side. One joining edge connects the two universes:

```
(RequestedAction class=resend-credential)
   --would_require-->  (Method messages.send)
```

**With that edge in place, the questions a mandate has to answer are all traversals.**

| Question | The walk |
|---|---|
| What would this request actually do? | `RequestedAction -> would_require -> Method -> mutates -> ObjectClass` |
| Do we even hold the authorisation? | `Method -> requires_scope -> Scope`, then test membership in the granted set |
| How far does it reach? | `Method -> has_reach -> Reach` |
| Could we undo it? | `Method -> undo_class -> Undo` |
| Is a person required? | `RequestedAction -> authorised_by -> MandateClause`, or the absence of one |
| Is anything actually stopping it? | `Method -> bounded_by -> Barrier`, and its kind and layer |

**Which means the behaviour policy stops being prose that a component is asked to honour and becomes a set of edges a validator checks.** That is the difference between an expectation and something a tool can enforce, which is the test this series keeps returning to.

**And it makes the delta per message rather than per deployment.** The published model computes a delta for an agent in a deployment. With the twins joined, every inbound message produces its own small delta: here is what it asked for, here is what that would require, here is what you authorised, here is the difference. **That is a far more sellable artefact than a static table, and it only exists because two universes were joined by a named edge.**

## A Twin Of Something You Do Not Control Is Wrong The Moment It Changes

**The honest half. A twin drifts, silently, because the original is not obliged to tell anybody.**

**Every node carries its provenance and its verification date.** The reference page it came from, the date it was read, and a hash of the retrieved bytes where the source is stable enough to hash. The regulation graph in the published estate does exactly this and ends every provenance chain in a hash of the retrieved bytes; the same discipline applies here for the same reason.

**Every twin carries a staleness statement on its face.** Verified on this date, against these sources, and here is what has not been checked since.

**Corrections supersede rather than overwrite**, which is the published grammar rule, and it matters more here than anywhere else in the estate: when a scope's behaviour changes, the old node is what every prior decision was made against, and deleting it destroys the record of why those decisions looked right.

**And a twin states what it does not model.** Rate limits not measured, error behaviours not enumerated, undocumented endpoints not represented. **A twin that does not list its own gaps will be trusted for things it cannot answer**, which is the failure mode of every model of an external system.

## Where The Twins Live

**One vault, three directories, because they version together and are read together.**

```
twins/
  interface/     scopes, methods, objects, limits, undo classes
  connector/     tools, approvals, the granted-but-unreachable set
  mailbox/       the sample mailbox: messages, labels, threads, read state
  PROVENANCE.md  what was read, when, and what has not been checked since
```

**The mailbox twin is the one that must never contain real correspondence.** It is going to be attacked deliberately, published as a demonstration, and read by people who are not the mailbox's owner. Synthetic content, shaped like the real thing.

## Build Order For The Twins

**One. Enumerate the connector's actual tool surface.** In a live deployment, list every tool the assistant is offered, and for each, the approval behaviour observed. This is the only step that cannot be done from documentation and everything else depends on it.

**Two. Build the interface twin for the methods those tools reach**, plus the methods the scopes permit and no tool surfaces, because that set is the gap.

**Three. Compute the grant from it** and compare against a grant written by hand. If the two differ, the twin is incomplete and the difference names what is missing.

**Four. Build a small mailbox twin**, twenty synthetic messages including five hostile ones.

**Five. Join the universes**, add `would_require` edges from a handful of requested action classes to methods, and answer the six traversal questions above by query rather than by reading.

## What This Does Not Try To Be

**It is not the twins.** Fragments are given to make the shape concrete; the field sets are sketches and the first real version will differ.

**It is not a complete reading of the platform's reference.** The facts used here come from the four earlier mailbox briefs, each of which read specific pages for specific questions.

**It is not a claim that the connector twin can be built from documentation.** It says the opposite: the tool surface must be enumerated from a running deployment.

**It is not a model of the assistant itself.** The model layer is an expectation and modelling it would suggest otherwise.

**And it does not settle the second meaning of the word.** It uses one and flags the other.

## Honest Tensions

**A twin is a second copy of a truth somebody else owns, and second copies drift.** The provenance and staleness discipline detects drift rather than preventing it, and the detection only works if somebody re-reads the sources on a rhythm nobody has set.

**The interface twin makes the grant derivable and makes it look more authoritative than it is.** A query result feels like a measurement. It is a query over a hand-built model of somebody else's system, and the confidence it projects is not the confidence it earns.

**The connector gap is real today and expires without notice.** Recording a barrier whose basis is that no tool exists yet invites a behaviour policy to claim protection that a product update removes silently. The expiry field exists for exactly this and will be left empty by whoever is in a hurry.

**Three twins is three things to maintain for a workflow that currently handles one mailbox.** The argument for building all three now is that the joins are the point and two twins do not join to anything. The argument against is that this is a great deal of modelling before a single message has been processed, and it is a fair argument.

**And the mandate-as-traversal design is elegant in a way that should be suspected.** Every question becoming a graph walk is satisfying, and satisfaction is not evidence. The first time a real mandate needs a condition that is not expressible as an edge, the design will acquire a rule engine beside the graph, and the honest thing is to expect that rather than to resist it.

## Open Questions

**Can the connector's tool surface be enumerated reliably, or does it vary by account and plan?** If it varies, the connector twin is per deployment rather than shared, which changes what can be published.

**Where does `would_require` come from?** Somebody has to state that a requested action class maps to a method. That mapping is authored, which makes it the one hand-written link in an otherwise derived chain, and it deserves the same review as a taxonomy.

**How often should a twin be re-verified?** Nobody has set a rhythm. Monthly is a guess.

**Should the interface twin be published?** It is a useful, vendor-neutral, permissively licensed description of what a mail connector can do, which is a gap nobody fills. It also hands an attacker a map.

**And does the mailbox twin need to be realistic to be useful?** Synthetic content is safe and may not exercise the extraction vocabulary the way real mail does, which would make the coverage measurement optimistic.

## Relationship To Previous Briefs

| Date | Document | Relationship |
|---|---|---|
| 11 Sep | The ruling that the delta is derived and never authored | Satisfied by construction here: the grant is a query over the interface twin |
| 12 Sep | The brief adding barrier position and expiry fields | The connector gap is a barrier with an expiry, which is what that field was for |
| 19 Sep | The two mailbox briefs | Supply the scope tiers, the label undo class and the batch limits that populate the interface twin |
| 20 Sep | The mailbox pipeline brief | Established the sample mailbox as the harness, which is the third twin here |
| 20 Sep | The split and the schema brief | Its closed boundary is what the twins give a vocabulary to |
| 20 Sep | The universe transitions brief | Supplies the message universe that the twins join to by a single named edge |

## Key Claims

| # | Claim |
|---|---|
| 1 | A twin is a representation of a system the estate does not control, kept in step and carrying provenance, and is not a mock |
| 2 | The word is being used in two senses this week, a representation and an actor, and only the first is used here |
| 3 | Three twins are needed rather than two: the interface, the connector and the mailbox, matching three layers of the enforcer ladder |
| 4 | A complete interface twin is the grant in machine readable form, so the grant is queried rather than authored |
| 5 | The finding that drafting and sending share a scope becomes a one line query in a twin rather than something that had to be noticed |
| 6 | A connector usually exposes fewer capabilities than its authorisation grants, and that unreachable set is an unrecorded barrier with an expiry |
| 7 | What the prompt displays becomes a field in the connector twin rather than an observation in a brief |
| 8 | One joining edge, from a requested action to a method, turns the mandate check into a traversal |
| 9 | The delta becomes per message rather than per deployment, which is a more sellable artefact than a static table |
| 10 | A twin of an external system drifts silently, so every node carries provenance and every twin carries a staleness statement and its own gaps |
| 11 | The mailbox twin must be synthetic, because it will be attacked deliberately and published as a demonstration |
| 12 | The connector tool surface cannot be enumerated from documentation and must be read off a live deployment, which is the first build task |

## Sources

- The four earlier mailbox briefs of 19 and 20 September 2026, for the scope tiers, the identity of the draft and send scopes, the label undo class, the batch limits and the approval behaviour, each of which cites the platform reference page it was read from
- The published fractal semantic graphs page, for the definition of a universe, the altitude vocabulary and the provenance discipline that ends every chain in a hash. https://sgit.ai/demos/fractal-graphs/index.html
- The published grammar, for edges as verbs with inverses, properties carrying data and never meaning, and supersede never delete. https://graphs.sgit.ai/v1/grammar/index.html
- The Agent Behaviour Policy site, for the four objects and the rule that the delta is derived. https://abp.sgit.ai/
- The project lead's voice memo of 20 September 2026, for the request for twins of the interface and the connector and for their use inside the graphs

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__the-twin-of-the-interface-is-the-grant-in-machine-readable-form/index.html)*
