# The delta

> Derived and never authored: stored with the versions of its inputs, recomputed when either moves, and never edited by hand. Reality is the third input, the history is the business case, and there are three clocks.

*Source: <https://abp.sgit.ai/model/delta/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The delta

# The delta

**The delta is derived and never authored.** Nobody writes a delta. It is only ever the output of a computation over the grant and the mandate, and it is stored along with the versions of both inputs and the time it was computed.

## This page corrects something this site said this morning

> **The foundation document says, twice, that the delta is computed and never stored.** The first half is right and the second half is wrong, and the correction was issued on the same day by the project lead. It is published here rather than applied quietly, because the method is to record the gap: [the dev brief that makes the correction](../../docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case/index.md), and [the foundation document as published](../../what-is-an-abp/index.md), which otherwise stands in full.

| Was | Is |
|---|---|
| The delta. Computed. Never stored, because the deployment changes. | **The delta. Derived.** Recomputed whenever the grant or the mandate changes, stored with the versions of both, and never edited by hand. |
| The delta is computed and never stored. A stored delta is a claim about somebody's environment on a day that has passed. | **The delta is derived and never authored.** Nobody writes a delta. It is only ever the output of a computation over the grant and the mandate, and it is stored along with the versions of both inputs and the time it was computed. **What must never happen is that somebody edits a delta**, because a hand edited delta is a fiction about an environment, and nothing downstream could tell. |

## What the old rule was protecting, and what survives

The sentence being corrected was guarding against three real things, and all three survive.

| The fear | Does the correction still handle it |
|---|---|
| A delta becomes a stale claim about somebody's environment | **Yes.** A stored delta carries the versions of its inputs and the time it was computed, so its staleness is a fact rather than a surprise |
| A delta gets hand edited into a fiction | **Yes, and more strongly.** Never authored is a harder rule than never stored, because it forbids the act rather than the artefact |
| A delta is treated as authoritative after the inputs move | **Yes.** It reacts. A recompute is cheap because the inputs are graphs |

**So the correction loses nothing and gains the history.** It is also the fourth instance of a pattern already in force across this network, which is why the corrected sentence is the one that fits and the old one was the odd one out: indexes are generated from the data they index, prose is derived from the graph and never hand edited, a bill of materials is generated from the dependency files, and the delta is derived from the grant and the mandate. **In every case the artefact is stored. What is forbidden is writing it.**

## The word for this already exists

**A stored result of a computation over other data, refreshed when its inputs change, never edited directly, is a materialised view.** The vocabulary is decades old and it carries exactly the right properties: it exists for use, it has a refresh policy, its staleness is knowable, and writing to it directly is a category error rather than a permission question.

The grant and the mandate are the append only side: a history of what changed and when. The delta is the read model computed from them. **The delta is a projection of the ABP graph, and so is the label, and so is the leaflet.**

### The stored record

| Field | Why |
|---|---|
| `grant_version` | The input, pinned |
| `mandate_version` | The input, pinned |
| `pack_version` | The published vocabulary it was computed against |
| `computed_at` | When |
| `computed_by` | Which version of the computation, because the computation is code and code changes |
| `excess` | Capabilities in the grant and not in the mandate |
| `unbounded_excess` | Excess whose barrier is one of the first three kinds |
| `shortfall` | Capabilities in the mandate and not in the grant |

> **No field in that record is writable by a person. The way to change a delta is to change a grant or a mandate.** So the release gate does not take the stored records on trust: it **recomputes every one of them** from the profile and the mandate it names and fails on a single row of disagreement. That check is a few lines, because the computation is a set difference, and it is a set difference because the grant and the mandate are held as graphs with a schema rather than as prose. **That is the underlying capability.** All of this can be done by hand today and almost nobody does it.

**16 stored deltas**, one per deployment shape and mandate pair: [`/data/deltas/index.json`](../../data/deltas/index.json).

## Reality is the third input

The grant is a model of what the agent can do. The mandate is a statement of what somebody meant. **Both are interpretations, and both improve.** The customer says what they actually meant, and the mandate sharpens. Somebody discovers a capability nobody had listed, and the grant grows.

| What is observed | What it tells you |
|---|---|
| Something happened that is not in the grant | **The grant was incomplete.** Add the capability |
| Something was blocked that the grant said was possible | **A barrier was missed**, or recorded at the wrong kind. Correct it |
| Something in the mandate never happens | Either the mandate is aspirational, or the capability is missing and the shortfall is real |
| Something happens repeatedly that is in the grant and not in the mandate | **The mandate is wrong, or the deployment is.** This is the only row where the observation does not say which |

> **That last row is the one place a derived delta cannot resolve itself.** An agent doing something outside its mandate, repeatedly, without anybody complaining, means either that the mandate was written too narrowly or that something is happening nobody authorised. **This site publishes the observation. Which of the two it is belongs to the risk layer and to a person.** Record, not verdict, again.

**And the calibration loop is the answer to this site's honest weakness.** 21 of 99 capability rows are measured and the rest derived from documentation. Every deployment that runs and reports back moves a row from derived to measured, and because [the capability map](https://what-can-it-do.games.sgit.ai/map/index.html) is shared and public, **it moves for everybody**. That is the reason the map belongs in an open repository rather than inside a product.

### And the collection problem it creates

> **A calibration loop needs observation, and the downloadable builds in this estate are ruled never to transmit anything.** The resolution is that calibration happens inside the customer's own instance: their deployment observes, their grant improves, their delta recomputes, and none of it leaves. **What comes back to the shared map is a contribution, not telemetry**: a proposed correction to a capability row, carrying its evidence, submitted deliberately through the same mechanism as any other proposal, with a source, a timestamp and a hash. A person decides to send it. Nothing phones home. **That is slower, and it is the only version that is honest.**

## It reacts, and the trigger has a standard

Because the delta is derived, a change in either input propagates without anybody touching the document. **A template cannot do that and a rendered document cannot do that.** Three cases:

| What happens | What the ABP does |
|---|---|
| **A weakness is disclosed in a tool the agent can call.** | Nothing about the deployment changed, but a capability recorded at the fourth barrier is now at the first. The grant is the same and **the unbounded excess jumps**. The ABP changed because the world did |
| **A credential is quietly widened.** | Somebody adds a scope to a token to fix an unrelated problem. The grant grows, the mandate does not, and the excess grows by exactly the capabilities that scope carries. **Nobody involved thought they were changing a policy** |
| **A control ships.** | A gateway is deployed with default deny. A set of capabilities move from the second barrier to the fourth. **Unbounded excess falls, and the number it falls by is what the project bought** |

**The trigger for a recompute already has a standard, so it is a receiver rather than an invention.** The continuous access evaluation profile, published on the standards track by the shared signals working group, defines event types an identity provider transmits and a receiver consumes so that access can be attenuated as things change.

| Event type | What it means for the ABP |
|---|---|
| **Credential Change** | **The grant may have moved.** Recompute |
| **Token Claims Change** | **The grant may have moved.** Recompute |
| **Assurance Level Change** | A barrier may have moved |
| **Device Compliance Change** | A barrier may have moved |
| **Risk Level Change** | **Not ours.** That is the risk layer's input, not the ABP's |
| **Session Revoked, Established, Presented** | Session lifecycle, below the ABP's altitude |

> **Nothing here is wired, and one caveat travels with the citation.** The status of that specification could not be confirmed from its own page, which said standards track rather than final while sitting at a final address. It is named here because it is the right shape, and it should be checked before anybody cites it as settled.

## What hooks to it, and the hazard

Behaviours can be hooked to a derived delta: actions, the granting of a licence to operate and the removal of one. **That is where an ABP stops being a document.** It is also hazardous in a specific way: a computation error would revoke a licence.

> **The delta crossing a threshold is a record. The consequence is a verdict.** So this site publishes the crossing, with its inputs and its computation version, and **the consequence is a policy the customer or the underwriter set in advance**, never a judgement the ABP makes. That keeps the ABP consequence agnostic while the automation is real, and it means any automatic suspension is traceable to a threshold somebody chose and a computation anybody can rerun.

## The history is the business case, read rather than constructed

Store the series and the business case stops being a document somebody writes. A control project has a date; the series has grants, mandates and deltas with dates; so the value of the project is a subtraction:

> On 14 March the gateway was deployed. **Unbounded excess fell from thirty one to six. Excess was unchanged**, because the agent can still do the same things; what changed is that twenty five of them are now bounded by something it cannot reach.

**That sentence contains no verdict, no score and no adjective**, and both ends of it are stored records with their inputs pinned, so it is checkable.

| Use of the series | How soon it pays |
|---|---|
| **Justifying what was already bought** | The easiest, and the one every security team needs and cannot produce today |
| **Pricing what to buy next** | The capabilities in unbounded excess, ordered by how many would move to the fourth barrier per control, is a list with an effect size on each row |
| **Evidencing a condition over time** | Asking whether a control was in place throughout a period is a question about a series, not a snapshot. **A stored history answers it and a recomputed present cannot.** This is the one the old wording made impossible |

## Three clocks, and the gap that is not ours

| Clock | What it measures | Who controls it |
|---|---|---|
| The ABP's clock | When the grant was last measured or calibrated | Us, and it can run on events |
| The twin's clock | When the twin last synchronised with the real environment | The customer's integration |
| Reality's clock | Never stops | Nobody |

**So an ABP is exactly as fresh as the twin, and the twin is exactly as fresh as its connection.** That is a parameter rather than a defect to hide, and it belongs on the label as part of the validity statement: as at this date, from a twin last synchronised at this date.

**And the gap between the second clock and the third is a risk that [the risk layer](https://risks.sgit.ai/) accounts for**, which is the correct home for it, because how much that gap matters depends on the assets, and the ABP does not know the assets. [The twin](https://twins.sgit.ai/) is the interface to the real environment.

## Drift is a neighbouring measurement, and the difference is the mandate

The market has a word for a related phenomenon and it is drift. Products announced in September 2026 compare an agent's runtime behaviour against its authorised scope. **That is validation, and it sharpens the distinction rather than blurring it.**

|  | What it compares | When you learn |
|---|---|---|
| **Behaviour drift** | What the agent **did** against what it was allowed to do | **After the action** |
| **Capability excess** | What the agent **can do** against what it was authorised to do | **Before any action** |

**You can only detect drift once an agent has drifted.** An ABP states that the drift is possible before it happens, which is a different thing and an earlier one in the sequence. **Both want a mandate, and the mandate is the scarce input**, which is the strongest reason to make eliciting it cheap and to publish the method.

> **No adjective is attached to any named product on this site, and none is here.** Neither product was used or tested. One number from one of those announcements is worth keeping because it is somebody else's figure supporting this site's thesis: fifty seven per cent of enterprise identity is described as unseen and unmanaged. *You do not know what it can do*, said by somebody selling a different answer to it.

## What is not settled

- **What the recompute policy is**: on every event, on a schedule, on read, or a combination. It decides how much the receiver has to do.
- **Who sets the thresholds a consequence hooks to**: the customer, the underwriter, or a default published here. All three have different shapes.
- **How a calibration contribution is submitted without revealing the deployment**, since a correction to a capability row implies somebody runs that shape.
- **Whether the shortfall matters commercially.** Capabilities in the mandate and not in the grant are a real finding and nobody has proposed anything against them.
- **What happens to a stored delta whose computation version is superseded**: recomputed, marked, or left as the record of what was believed at the time. The third is the most honest and the least useful.

[The full brief](../../docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case/index.md) · [The stored deltas](../../data/deltas/index.json) · [The four objects](../../model/index.md)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/delta/index.html)*
