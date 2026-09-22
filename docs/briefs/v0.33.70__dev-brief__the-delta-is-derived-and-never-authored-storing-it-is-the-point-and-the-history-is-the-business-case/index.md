# The Delta Is Derived And Never Authored: Storing It Is The Point, And The History Is The Business Case

> version v0.33.70 date 11 September 2026 from Human (project lead) to Whoever builds the ABP data model, whoever wires the recompute, and whoever has to correct a document that is already published

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / The Delta Is Derived And Never Authored: Storing It Is The Point, And The History Is The Business Case

# The Delta Is Derived And Never Authored: Storing It Is The Point, And The History Is The Business Case

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case.md`](../../../docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.70 **date** 11 September 2026 **from** Human (project lead) **to** Whoever builds the ABP data model, whoever wires the recompute, and whoever has to correct a document that is already published

**type** Dev brief (a correction to a published formulation, and the specification it turns into)

*Fifth of 11 September, and the first document in this corpus written to correct one already pushed. The foundation document published earlier today carries the sentence that the delta is computed and never stored, twice. The project lead's correction is that the second half is wrong and the first half was the point. This brief states the correction, gives the replacement wording verbatim so it can be pasted, and then works out what follows, which is more than a wording change. Both the corpus and the outside were searched. The outside search found a standard for the event that triggers a recompute, and a product announced two days ago that measures a neighbouring thing and thereby sharpens what this one measures. Limitations: nothing here is built; the calibration loop has a collection problem that is named and not solved; and one specification's status could not be confirmed from its own page.*

## What This Is

The correction of one phrase in a published document, and the specification that the corrected phrase turns out to require: **the foundation document states that the delta is computed and never stored, on the reasoning that a stored delta is a claim about an environment on a day that has passed; the project lead's correction is that computed was the whole point and never stored was an error, because the delta belongs in a vault along with the history of the grants and the mandates that produced it, since both of those are interpretive and improve over time as the customer says what they actually meant and as more of what the agent can do is discovered, because reality is the calibrator, in that something happening which is not in the grant means the grant was incomplete and something being blocked which the grant said was possible means a barrier was missed; the power of a computed delta is a direct consequence of holding the grant and the mandate as graphs with a schema and an ontology that can be calculated against, which is the underlying capability, because all of this can be done manually today and almost nobody does it, and a programmatic delta is not a given; a computed delta reacts to changes in either input without anybody touching it, which means behaviours can be hooked to it, including actions, consequences, the granting of a licence to operate and the removal of one, so that a newly discovered weakness or a quietly widened credential moves the agent outside the authorised set without a human noticing; and the history matters commercially, because a project that introduces a control reduces the grant and therefore the delta, and that before and after is the business case, read off a series rather than constructed; the first finding is that the correct formulation is that the delta is derived and never authored, which keeps everything the original ruling was protecting while removing the error, and that the thing being described already has a name in computing, being a materialised view, stored for use, refreshed from its inputs, never hand edited, and carrying its own staleness; the second is that reality is a third input alongside the grant and the mandate, and the calibration loop it creates is the answer to the honest weakness in the published document, which is that twenty one of ninety nine capability rows are measured and the rest derived; the third is that the event which triggers a recompute has an existing standard with defined event types, so the recompute trigger is a receiver rather than an invention; the fourth is that a product announced on 9 September 2026 detects drift between an agent's runtime behaviour and its authorised scope, which is a neighbouring measurement and makes the distinction sharp, because behaviour drift is detected after an action and capability excess exists before any action; and the fifth is that hooking a consequence to a computed value is powerful and hazardous, and the estate's own rule resolves it, because the delta crossing a threshold is a record and the consequence is a policy somebody set in advance.** New contributions: **the correction with replacement wording; reality as the third input and the calibration loop; the recompute trigger mapped onto an existing standard; the history as a business case read rather than constructed; the three clocks and the gap the risk layer accounts for; the distinction from behaviour drift; and the collection problem the loop creates against a product that promises not to phone home.**

## The Correction

**The published foundation document says this, in two places.**

In the four objects table:

> **The delta.** Computed. Never stored, because the deployment changes.

And in the body:

> **The delta is computed and never stored.** A stored delta is a claim about somebody's environment on a day that has passed. The environment is the thing that changes, so the delta is recomputed from the grant and the mandate every time it is needed.

**The first half is right and the second half is wrong.** The delta is computed. It is also stored, and storing it is most of what makes it useful.

**The replacement wording, for the table:**

> **The delta.** Derived. Recomputed whenever the grant or the mandate changes, stored with the versions of both, and never edited by hand.

**The replacement wording, for the body:**

> **The delta is derived and never authored.** Nobody writes a delta. It is only ever the output of a computation over the grant and the mandate, and it is stored along with the versions of both inputs and the time it was computed. That is what makes it checkable rather than stale: a stored delta that carries its inputs can be recomputed and compared, and one that carries no inputs is the claim the older wording was afraid of. **What must never happen is that somebody edits a delta**, because a hand edited delta is a fiction about an environment, and nothing downstream could tell.

## What The Old Ruling Was Protecting, And What Survives

**Being fair to the sentence being corrected: it was guarding against three real things, and all three survive the correction.**

| The fear | Does the correction still handle it |
|---|---|
| A delta becomes a stale claim about somebody's environment | **Yes.** A stored delta carries the versions of its inputs and the time it was computed, so its staleness is a fact rather than a surprise |
| A delta gets hand edited into a fiction | **Yes, and more strongly.** Never authored is a harder rule than never stored, because it forbids the act rather than the artefact |
| A delta is treated as authoritative after the inputs move | **Yes.** It reacts. A recompute is cheap because the inputs are graphs |

**So the correction loses nothing and gains the history.**

**And this is the fourth instance of a pattern already in force across the estate**, which is worth noticing because it means the corrected sentence is the one that fits and the old one was the odd one out:

- **Indexes are generated from the data they index**, so they cannot disagree with the source. Stored, derived, never authored.
- **Prose is derived from the graph and never hand edited**, which was the renderer rule of this morning's second brief.
- **A software bill of materials is generated from the dependency files** rather than asserted, which was the finding in the findability brief of 10 September.
- **The delta is derived from the grant and the mandate** and never authored.

**In every case the artefact is stored. What is forbidden is writing it.**

## The Word For This Already Exists

**A stored result of a computation over other data, refreshed when its inputs change, never edited directly, is a materialised view.** The vocabulary is decades old and it carries exactly the right properties: it exists for use, it has a refresh policy, its staleness is knowable, and writing to it directly is a category error rather than a permission question.

**The related pair is worth naming too.** The grant and the mandate are the event sourced side: an append only history of what changed and when. The delta is the read model computed from them. **That is the same shape as the estate's own published pattern in two places, where a story is a graph and an article is a projection, and where briefs are arguments and infographics are projections.** The delta is a projection of the ABP graph, and so is the label, and so is the leaflet.

**Practical consequence for the model: the delta gets a stored record with a fixed shape.**

| Field | Why |
|---|---|
| `grant_version` | The input, pinned |
| `mandate_version` | The input, pinned |
| `computed_at` | When |
| `computed_by` | Which version of the computation, because the computation is code and code changes |
| `excess` | Capabilities in the grant and not in the mandate |
| `unbounded_excess` | Excess whose barrier is one of the first three kinds |
| `shortfall` | Capabilities in the mandate and not in the grant |

**No field in that record is writable by a person.** The way to change a delta is to change a grant or a mandate.

## Reality Is The Third Input

**This is the part of the correction that is not a wording change.**

The grant is a model of what the agent can do. The mandate is a statement of what somebody meant. **Both are interpretations, and both improve.** The customer says *what I actually meant was this*, and the mandate sharpens. Somebody discovers a capability nobody had listed, and the grant grows.

**And reality calibrates both.**

| What is observed | What it tells you |
|---|---|
| Something happened that is not in the grant | **The grant was incomplete.** Add the capability |
| Something was blocked that the grant said was possible | **A barrier was missed**, or recorded at the wrong kind. Correct it |
| Something in the mandate never happens | Either the mandate is aspirational, or the capability is missing and the shortfall is real |
| Something happens repeatedly that is in the grant and not in the mandate | **The mandate is wrong, or the deployment is.** This is the interesting one and it is the only case where the observation does not say which |

**That last row is worth dwelling on, because it is the one place a computed delta cannot resolve itself.** An agent doing something outside its mandate, repeatedly, without anybody complaining, means either that the mandate was written too narrowly or that something is happening nobody authorised. **The ABP publishes the observation. Which of the two it is belongs to the risk layer and to a person.** Record, not verdict, again.

**And the calibration loop is the answer to the published document's honest weakness.** Twenty one of ninety nine capability rows are measured and the rest are derived from documentation. **Every deployment that runs and reports back is an experiment that moves a row from derived to measured**, and because the capability map is shared and public, it moves for everybody. **That is a network effect and it is the reason the map should stay in the open repository rather than inside a product.**

## The Delta Reacts, And The Trigger Has A Standard

**Because the delta is derived, a change in either input propagates without anybody touching the document.** That is the property a template cannot have and a rendered document cannot have, and it is the strongest differentiator yet, stronger than derived from your deployment, because it is *continuously* derived.

**Three worked cases.**

**A weakness is disclosed in a tool the agent can call.** Nothing about the deployment changed. But a capability that was recorded at the fourth barrier, a boundary enforced above the agent, is now at the first. **The grant is the same and the unbounded excess jumps.** The ABP changes because the world did.

**A credential is quietly widened.** Somebody adds a scope to a token to fix an unrelated problem. The grant grows, the mandate does not, and the excess grows by exactly the capabilities that scope carries. **Nobody involved thought they were changing a policy.**

**A control ships.** A gateway is deployed with default deny. A set of capabilities move from the second barrier to the fourth. **Unbounded excess falls, and the number it falls by is what the project bought.**

**The trigger for a recompute already has a standard, and the estate should receive rather than invent one.** The continuous access evaluation profile, published 29 August 2025 on the standards track by the shared signals working group, defines event types transmitted by an identity provider and consumed by a receiver so that access can be attenuated as things change. Its own framing is that transmitters send continuous updates which receivers use to attenuate access for human or robotic users, devices, sessions and applications.

| Event type | What it means for the ABP |
|---|---|
| **Credential Change** | **The grant may have moved.** Recompute |
| **Token Claims Change** | **The grant may have moved.** Recompute |
| **Assurance Level Change** | A barrier may have moved |
| **Device Compliance Change** | A barrier may have moved |
| **Risk Level Change** | Not ours. This is the risk layer's input, not the ABP's |
| **Session Revoked, Established, Presented** | Session lifecycle, below the ABP's altitude |

**So the recompute trigger is a receiver for two or three event types, and the rest is the graph.** That is a small build and it is standards shaped. **The status of that specification could not be confirmed from its own page**, which said standards track rather than final while sitting at a final address, and somebody should check before it is cited publicly.

## What Hooks To It, And The Hazard

**The project lead's point is that behaviours can be hooked to the delta: actions, consequences, the granting of a licence to operate and its removal.** That is right and it is where the ABP stops being a document.

**And it is hazardous in a specific way: a computation error would revoke a licence.** The estate's own rule resolves it cleanly.

**The delta crossing a threshold is a record. The consequence is a verdict.** So the ABP publishes the crossing, with its inputs and its computation version, and **the consequence is a policy that the customer or the underwriter set in advance**, not a judgement the ABP makes. That keeps the ABP consequence agnostic while making the automation real, and it means an automatic suspension is always traceable to a threshold somebody chose and a computation anybody can rerun.

**One elegant fit worth recording.** The statute analysed in this morning's third brief already provides for exactly this shape: a warranty breach **suspends** cover for losses occurring after the breach and before it is remedied, rather than discharging the contract. **A continuously computed delta is a thing that can trigger a suspensive condition and evidence it**, and remedy is visible in the same series. Nobody has to notice. That is a better fit between a statutory mechanism and a data structure than anything else in this estate.

## The History Is The Business Case, Read Rather Than Constructed

**Store the series and the business case stops being a document somebody writes.**

A control project has a date. The series has grants, mandates and deltas with dates. So the value of the project is a subtraction:

> On 14 March the gateway was deployed. Unbounded excess fell from thirty one to six. Excess was unchanged, because the agent can still do the same things; what changed is that twenty five of them are now bounded by something it cannot reach.

**That sentence contains no verdict, no score and no adjective, and it is the strongest thing a security team can take to a budget conversation.** It is also checkable, because both ends of it are stored records with their inputs pinned.

**Three uses of the series, in order of how soon they pay.**

**Justifying what was already bought**, which is the easiest and the one every security team needs and cannot produce today.

**Pricing what to buy next.** The capabilities in unbounded excess, ordered by how many would move to the fourth barrier per control, is a shopping list with an effect size on each row.

**Evidencing a condition over time.** An underwriter or an auditor asking whether a control was in place throughout a period is asking a question about a series, not about a snapshot. **A stored history answers it and a recomputed present cannot.** This is the strongest argument of the three and it is the one the old wording made impossible.

## Three Clocks, And The Gap That Belongs To The Risk Layer

**The project lead's last point is the honest limit and it should be written down as three clocks.**

| Clock | What it measures | Who controls it |
|---|---|---|
| **The ABP's clock** | When the grant was last measured or calibrated | Us, and it can be fast |
| **The twin's clock** | When the twin last synchronised with the real environment | The customer's integration |
| **Reality's clock** | Never stops | Nobody |

**Inside the vault and the graph, the first clock can run in near real time on events.** The second is a connection to somebody else's systems and its latency is a property of their estate, not of our software. **The third does not wait.**

**So the ABP is exactly as fresh as the twin, and the twin is exactly as fresh as its connection.** That is not a defect to hide. It is a parameter, and it belongs on the label as part of the validity statement: **as at this date, from a twin last synchronised at this date.**

**And the gap between the second and third clocks is a risk that the risk layer accounts for**, which is the correct home for it, because how much that gap matters depends on the assets, and the ABP does not know the assets.

## Drift Is A Neighbouring Measurement, And The Difference Is The Mandate

**A product announced on 9 September 2026, two days ago, detects what it calls identity drift for agents**, comparing an agent's runtime behaviour against its original purpose and authorised scope, and triggering responses including reducing permissions, revoking credentials, disconnecting tools and application level kill switches. Another large vendor has announced continuous identity for agents. **The market has a word for the phenomenon and it is drift.**

**This is validation and it sharpens the distinction rather than blurring it.**

|  | What it compares | When you learn |
|---|---|---|
| **Behaviour drift** | What the agent **did** against what it was allowed to do | **After the action** |
| **Capability excess** | What the agent **can do** against what it was authorised to do | **Before any action** |

**You can only detect drift once an agent has drifted.** The ABP states that the drift is possible before it happens, which is a different product and an earlier one in the sequence. **Both want a mandate, and the mandate is the scarce input**, which is the strongest reason to make eliciting it cheap and to publish the method.

**One datum from that announcement is worth keeping**, because it is a competitor's own number supporting the thesis of the published foundation document: **fifty seven per cent of enterprise identity is described as unseen and unmanaged.** You do not know what it can do, said by somebody selling a different answer to it.

## The Collection Problem This Creates

**The calibration loop needs observation, and the toolkit brief of 10 September rules that the downloadable builds never transmit anything.** Those are in tension and the tension should be resolved now rather than in month three.

**The resolution is that calibration happens inside the customer's own instance.** Their deployment observes, their grant improves, their delta recomputes, and none of it leaves.

**What comes back to the shared map is a contribution, not telemetry**: a proposed correction to a capability row, carrying its evidence, submitted deliberately through the same mechanism as any other proposal to the public data files, with a source, a timestamp and a hash. **A person decides to send it. Nothing phones home.**

**That keeps both promises**, and it means the shared map improves at the speed of deliberate contribution rather than at the speed of collection. **Slower, and it is the only version that is honest.**

## What This Does Not Try To Be

- **A schema.** The delta record's fields are listed. No file format, no identifier scheme and no storage layout is specified.
- **A recompute implementation.** The trigger is mapped onto existing event types. Nothing is wired.
- **A competitive analysis.** Two products are named from announcements read on one day, to draw one distinction. Neither was used or tested.
- **A rewrite of the published document.** Two passages are quoted and two replacements are given. Everything else in that document stands.
- **A decision about the consequence hooks.** The hazard is named and the shape of the safe version is given. What thresholds, set by whom, is not answered.

## Honest Tensions

| Tension | Note |
|---|---|
| Correcting a published document | It is the estate's method, and it is the third correction issued in two days |
| Storing the delta | It makes the history and the business case possible, and it creates an artefact that can be quoted out of date |
| Reality as an input | It is what makes the grant improve, and it requires observing something we have promised not to observe |
| Hooking consequences | It makes the ABP operational, and a computation error becomes an outage |
| The three clocks | It is honest, and it tells a buyer their ABP is only as fresh as an integration they have not built |
| Publishing the calibration loop openly | It improves the map for everybody including competitors, and the map being shared is what makes it worth calibrating |
| Drift is a neighbouring product | The distinction is real and earlier in the sequence, and a buyer with a drift tool will believe they already have this |

## Open Questions

1. **What is the recompute policy?** On every event, on a schedule, on read, or a combination. It decides how much the receiver has to do.
2. **Is the specification final?** Its own page says standards track at a final address, and it should be checked before being cited publicly.
3. **Who sets the thresholds that consequences hook to?** The customer, the underwriter, or a default we publish. All three have different liability shapes.
4. **How is a calibration contribution submitted without revealing the deployment?** A correction to a capability row implies somebody runs that shape.
5. **Does the shortfall matter commercially?** Capabilities in the mandate and not in the grant are a real finding and nobody has proposed selling anything against them.
6. **What happens to a stored delta whose computation version is superseded?** Recomputed, marked, or left as the record of what was believed at the time. The third is the most honest and the least useful.
7. **Can the series be published without the deployment?** The business case sentence is compelling and it describes a customer's estate.

## Relationship To Previous Briefs

**From the foundation document published earlier today**, it corrects two passages and leaves the rest standing, including the four objects, the four barriers and the rule that the ABP describes and does not judge.

**From this morning's second brief**, it takes the projection pattern and finds that the delta is a projection too, alongside the label and the leaflet.

**From this morning's third brief**, it takes the suspensive condition under the statute, and finds that a continuously computed delta is the thing that can trigger one and evidence it.

**From the toolkit brief of 10 September**, it takes the rule that the offline builds do not transmit, and resolves the tension that the calibration loop creates against it.

**From the vault architecture brief of 10 September**, it takes the customer's data vault as the home for the series, and the pinning rule that a consumer states the versions it computed against.

**From the findability brief of 10 September**, it takes the derived rather than asserted principle and records this as the fourth instance of it.

**From the ruling of 20 August**, it takes publish the record and never the verdict, and applies it to the one place where automation would otherwise make the estate a decision maker.

## Key Claims

| # | Claim |
|---|---|
| 1 | The published wording is wrong in half: the delta is computed, and it is also stored |
| 2 | The correct formulation is that the delta is derived and never authored, which forbids the act rather than the artefact |
| 3 | Everything the old ruling protected survives, because a stored delta carries its inputs, their versions and the time it was computed |
| 4 | It is a materialised view, and the estate already applies the same pattern to indexes, prose and bills of materials |
| 5 | Reality is a third input, because something happening that is not in the grant means the grant was incomplete |
| 6 | The calibration loop is the answer to twenty one measured rows of ninety nine, and it improves the shared map for everybody |
| 7 | A derived delta reacts to a change in either input without anybody touching the document, which no template can do |
| 8 | The recompute trigger has an existing standard with defined event types, so it is a receiver rather than an invention |
| 9 | A threshold crossing is a record and the consequence is a policy somebody set in advance, which keeps the ABP consequence agnostic while the automation is real |
| 10 | A continuously computed delta can trigger and evidence a suspensive condition, which is the statutory mechanism analysed this morning |
| 11 | The history makes the business case a subtraction that is read rather than constructed, and it is the only way to evidence a control over a period |
| 12 | Behaviour drift is detected after an action and capability excess exists before any action, and both need a mandate that only one of them elicits |

## Sources

All read 11 September 2026.

**Inside the estate.** The foundation document published earlier today. The capability map with its nine profiles, twenty three primitives, four barriers and its statement that twenty one of ninety nine rows were measured, at https://what-can-it-do.games.sgit.ai/map/index.html. The graph rules at https://graphs.sgit.ai/. The site building guidance, for the rule that indexes are generated from the data they index, at https://sgit.ai/docs/guidance/index.html. The three briefs of this morning and the toolkit, vault architecture and findability briefs of 10 September.

**The recompute trigger.** The continuous access evaluation profile at https://openid.net/specs/openid-caep-1_0-final.html, dated 29 August 2025, whose own page described it as standards track rather than final and whose status should be confirmed before public citation. The working group at https://openid.net/wg/sharedsignals/ and its specification list at https://openid.net/wg/sharedsignals/specifications/.

**The neighbouring measurement.** The drift detection and kill switch announcement of 9 September 2026 at https://www.helpnetsecurity.com/2026/09/09/orchid-security-ai-agents-application-level-kill-switches/ and https://www.globenewswire.com/news-release/2026/09/09/3358716/0/en/orchid-security-adds-ai-readiness-controls-identity-drift-detection-and-application-level-kill-switches-for-ai-agents.html, including the figure that fifty seven per cent of enterprise identity is unseen and unmanaged. The continuous identity announcement at https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-continuous-identity-for-ai-agents/. Neither product was used or tested and no adjective is attached to either.

**The statutory mechanism.** Section 10 of the Insurance Act 2015 at https://www.legislation.gov.uk/ukpga/2015/4/section/10, analysed in this morning's third brief.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-the-point-and-the-history-is-the-business-case/index.html)*
