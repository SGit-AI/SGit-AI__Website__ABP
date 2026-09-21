# Agent Behaviour Policy (ABP): You Know What You Asked For, And You Do Not Know What It Can Do

> version v0.33.70 date 11 September 2026 from Dinis Cruz to Anyone deploying an agent, anyone building one, and anyone who has to sign for one

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.70__foundation__agent-behaviour-policy-you-know-what-you-asked-for-and-you-do-not-know-what-it-can-do/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / Agent Behaviour Policy (ABP): You Know What You Asked For, And You Do Not Know What It Can Do

# Agent Behaviour Policy (ABP): You Know What You Asked For, And You Do Not Know What It Can Do

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.70__foundation__agent-behaviour-policy-you-know-what-you-asked-for-and-you-do-not-know-what-it-can-do.md`](../../../docs/briefs/v0.33.70__foundation__agent-behaviour-policy-you-know-what-you-asked-for-and-you-do-not-know-what-it-can-do.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.70 **date** 11 September 2026 **from** Dinis Cruz **to** Anyone deploying an agent, anyone building one, and anyone who has to sign for one

**type** Foundation document (the definition and introduction of the Agent Behaviour Policy, written for publication and for feedback)

*This is the document everything else about the ABP stands on. It defines the term, says what an ABP contains and what it deliberately does not, gives one worked example with published numbers, and ends with the questions we would like answered by people who deploy agents for a living. It consolidates three internal briefs written on 11 September 2026 and rulings made on the days before. Everything factual in it carries a source and a date. Where a claim rests on something we measured, it says how much was measured and how much was derived. Nothing in it is a claim about any named product being good or bad, and nothing in it is a score.*

## What This Is

The introduction of a document type that does not yet exist in most organisations and should: **an Agent Behaviour Policy is a written description, for one agent in one deployment, of four things, being everything the agent can do, which we call the grant, what it was authorised and expected to do, which we call the mandate, the difference between the two, which we call the delta, and what stands between the agent and each capability, which we call the barrier; it is derived from the deployment rather than copied from a template, it is rendered as one line for a decision maker and a full table for an engineer from the same set of facts, and it describes without judging, so it carries no score, because the same ABP is dangerous in one deployment and harmless in another and nothing about the document changed; the reason it exists is a gap that is easy to state and hard to close, which is that most people who deploy an agent know what they asked it to do and almost nobody knows what it can do, and the ABP is the document that puts those two side by side.** New here: **the definition, the four objects, the barrier as the test of whether anything is actually in the way, the rule that the ABP never judges, and the questions we are asking you.**

## The Gap

**You know what you asked for.** When somebody deploys an agent, they know the job: draft the reply, fix the build, summarise the ticket, book the travel. That is the mandate, and it is usually clear, whether or not anybody wrote it down.

**You do not know what it can do.** The agent runs with an account, on a machine, inside a container or on a desktop, with credentials and network access and a set of tools. Everything those permit is the grant. **It is almost never enumerated, and when it is, it is larger than the person who deployed the agent expected.**

We have been measuring this. A published capability map covers nine common deployment shapes across twenty three capability primitives, and a published simulation of one ordinary assistant agent shows the shape of the result: **a grant of twelve capabilities, a mandate of four, and eight capabilities inside the agent's reach and outside its authority.** That eight is the delta, and in that example twice as many things were possible as were asked for.

**The ABP is the document that puts the grant and the mandate on the same page.** That is all it is. That turns out to be a great deal.

## The Four Objects

An ABP is not a single list. It is four objects, and the order they are produced in matters.

| Object | What it is | How it is obtained |
|---|---|---|
| **The mandate** | What the agent is authorised and expected to do | **Elicited.** In minutes, because the deployer already knows it |
| **The grant** | Everything the agent can do | **Measured.** From the deployment shape: the product, where it runs, with what account, with what credentials |
| **The delta** | The difference. Excess where it can and you did not ask; shortfall where you asked and it cannot | **Computed.** Never stored, because the deployment changes |
| **The barrier** | What stands between the agent and each capability | **Recorded**, per capability, from one of four kinds |

**The mandate must be captured even though it is already known**, because a grant on its own is an inventory, and nobody acts on an inventory. *Your agent can do three hundred and forty things* is a shrug. *Your agent can do three hundred and forty things and you authorised twelve* is a finding. The mandate is the edge that gives the grant a shape.

**The delta is computed and never stored.** A stored delta is a claim about somebody's environment on a day that has passed. The environment is the thing that changes, so the delta is recomputed from the grant and the mandate every time it is needed.

## The Barrier: What Is Actually In The Way

For every capability in the grant, the ABP records what stands between the agent and it. There are four kinds, and the published capability map already uses them:

| Barrier | Meaning | Is anything in the way |
|---|---|---|
| **Nothing** | The agent can simply do it | No |
| **A rule somebody wrote down** | An instruction in a prompt, a policy document, a line in a configuration the model reads | **No.** An instruction to the agent is inside the boundary the agent operates in |
| **A setting the agent's own account could change** | A configuration the agent has permission to alter | **No.** The grant includes the ability to remove the barrier |
| **A boundary enforced above it that it cannot reach** | A sandbox, a gateway, a tool that is not exposed, a network it cannot see | **Yes** |

**Only the fourth kind bounds anything.** That is not our opinion. All four of the major model providers have said in their own words during 2026 that an instruction at the prompt layer can be bypassed; one of them puts it as *the deterministic boundary is what gets hit when everything probabilistic misses.* The rule underneath is old and simple: **a control bounds a grant only if it is enforced by something the grant does not include.**

**So an ABP that lists a prohibition without its barrier is making a claim it cannot support.** Every prohibition in an ABP carries the kind of barrier behind it, and the honest ones say, for most deployments today, that the barrier is the second kind.

## One Worked Example, With Published Numbers

The clearest way to see what the ABP does is to change one setting and watch the document change.

Take a coding agent that runs on a developer's own machine. The published capability map profiles it twice: **once with confirmations enabled, once with confirmations disabled.** Same product, same machine, same account. One setting.

With confirmations enabled, a capability like *run programs as the account* has a barrier of the third kind: a setting the agent's own account could change. A person is asked before each action. **That is not a control, because the setting can be switched off from inside the grant, and because people approve almost everything they are asked.** One provider reports that users approved roughly ninety three per cent of permission prompts.

With confirmations disabled, the same capability has a barrier of the first kind: nothing.

**The grant did not change. The mandate did not change. The delta did not change. The barrier on every capability in the delta moved one row.** Two ABPs, one line different, and the second one is the one most people are actually running.

That is the whole argument in one setting. **The ABP is about the deployment, not the product.**

*The rows behind this example come from the published map, which states that of ninety nine tool capability rows across its set, twenty one were measured and the rest derived. We repeat that ratio rather than hide it.*

## It Describes And It Does Not Judge

**The ABP carries no verdict and no score.** This is the rule that makes it usable, and it takes a moment to see why.

**The same ABP is dangerous in one deployment and harmless in another, and nothing about the document changed.** The most permissive grant imaginable, running where there are no assets and nothing reachable, is a low risk. The same grant with a production database attached tomorrow is a high one. The same grant next to a second agent that can act on its outputs is a different risk again. **Risk is a function of the ABP, the assets, the consequences and the date. The ABP is the one input that does not move.**

**A policy cannot be dangerous. A deployment can.**

So there is no rating on an ABP, no traffic light, no risk level. Anybody who wants one will be asked for the other inputs first, because a score without the assets is wrong in one of the two rooms. **The score has a home, and it is the risk work that sits above the ABP, where the assets are known and a named person signs.** That work exists. It is not this document.

**Three things follow from describing without judging, and each is useful.**

**A long grant is an inventory, not an admission.** An ABP says a capability exists. It never says a risk is unacceptable.

**Correcting a draft is factual.** When we hand somebody a draft ABP for their deployment and ask if it is right, we are not asking them to agree that something is dangerous. We are asking whether their agent can do a thing. That is a question you can put to somebody who knows their business better than you do.

**The description keeps.** A verdict goes stale whenever anything in the environment moves. A description of the grant goes stale on a visible clock: when the product changes or the deployment does. **Every ABP carries a validity statement**: *this describes the deployment as at this date; if the risk changed, the deployment changed, not this document.*

## The Label And The Leaflet

An ABP is rendered twice from one set of facts.

**The label** is one line, for anybody:

| Field | Meaning |
|---|---|
| Shape | The named deployment, in the product's own published words |
| Grant | N of 23 primitives |
| Mandate | M primitives |
| **Excess** | In the grant, not in the mandate. **The finding** |
| **Unbounded excess** | Excess whose barrier is one of the first three kinds. **The purchase** |
| Irreversible | Granted capabilities that cannot be undone, as published |
| Widest reach | The furthest the agent can reach: its project, its host, its tenant, or the world |
| Measured | Rows measured against rows derived |
| As at | The date and the source version |

**Two numbers matter.** *Excess* answers the question this document exists for. *Unbounded excess* is the only number on the label a buyer can move: every real control put in place shifts one capability to the fourth barrier, and the number falls. **The gap between the two is the business case for a control, and it contains no verdict.**

**The leaflet** is the full table underneath: every primitive with its barrier, its reversibility, its provenance, and the mandate beside it. For the engineer, the auditor, and anybody who has to price it.

**Both are computed from the same facts, and the facts are identical in both.** What differs is how they are grouped, which is a question of who is reading.

## Why The Mandate Reaches Further Than Your Own Material

One consequence of writing the mandate down is that it makes visible something most deployments miss.

**A grant you hold over other people's material is not a grant you may pass on.** A client sent you a document. A customer gave you access. A colleague shared a folder. Handing an agent the credential that reaches those things is handing on a pass that was issued to you, and in most cases you were not given authority to do that. This is not an analogy. In data protection law it is one sentence: *the processor shall not engage another processor without prior specific or general written authorisation of the controller*, and the first processor stays liable for the second. In professional confidentiality it is a duty with two exits, legal compulsion or the client's consent, and a regulator wrote on 17 August 2026 that putting client documents into a public model tool is to place them in the public domain. In contract it is the permitted recipients clause of every confidentiality agreement, which names employees and advisers and does not name a model provider.

**The ABP does not decide any of that. It makes the question askable**, because the mandate is where you write down whose material the agent is meant to touch, and the grant is where you find out whose material it can.

## What An ABP Is Not

- **Not an acceptable use policy.** That governs a person's use of a system. An ABP governs what an agent can and may do. Borrowing the frame imports the wrong subject.
- **Not a risk assessment.** It has no assets in it and no consequences. It is the input to one.
- **Not a compliance assessment, a certification, an audit or a security review** of anything or anybody. It describes a deployment and certifies nobody.
- **Not a score.** See above.
- **Not a guardrail.** It is what guardrails are compiled from. The barrier column tells you which prohibitions are guardrails already and which are sentences.
- **Not a claim about any product.** The capability rows are drawn from published documentation and published measurement, with the source, the date and the measured ratio stated. No adjective is attached to any of them.
- **Not a template.** It is derived from one deployment. A template cannot know what your agent can do.

## Where It Comes From

We did not invent most of this, and we would rather say so.

The four kinds of barrier are already published on our capability map. The vocabulary for expressing permissions, prohibitions and duties with constraints on time, purpose and count has been a W3C recommendation since 2018, and it is in production use in the European data space architectures. The enforcement languages exist: the largest cloud's own agent gateway blocks everything by default and treats any prohibition as overriding any permission, with the reasoning formally verified. The industry's list of the ten agentic application risks, published 9 December 2025, puts tool misuse and privilege abuse at positions two and three, with least privilege and enumerated tool catalogues as the remedies. The United Kingdom's consumer regulator wrote on 9 March 2026 that a business using an agent *should be clear about what tasks an AI agent is allowed to perform, what data it can access, and what constraints apply.* And at least one underwriter of agents already requires, as a scoping input, a statement of the agent's capabilities, its autonomy level, its data access, the tools it can call and its deployment context, which is an ABP by another name.

**What did not exist was a document that puts all of that on one page for one deployment, derived rather than copied, and honest about what it is not.** One company sells a set of editable templates. We are aware of nothing that is derived from the deployment, nothing that carries the barrier, and nothing that refuses to carry a score.

## What We Are Asking You

This is the part we want back.

1. **Would you correct a draft?** If we gave you a draft ABP for your own deployment, derived from its shape, would you tell us where it was wrong? That correction is how the document gets made, and we want to know if the exchange works.
2. **Which capability did you not know about?** For the shape you run, which row of the grant was news to you?
3. **Are twenty three primitives enough?** We know two things are missing: quantity, since one request and a million are the same primitive today, and interaction between agents, since two agents each within mandate can compose into something neither was authorised to do. What else?
4. **Is the four kind barrier right?** Is there a kind of control we have not listed, or one we have placed in the wrong row?
5. **Does no score survive contact with your organisation?** Or will somebody upstream insist on a rating before they read it?
6. **Which deployment shape next?** We have nine. Which one do you actually run that we have not profiled?
7. **Is Agent Behaviour Policy the right name?** We considered and rejected several. If this one fails for you, we would like to know why.

## Honest Tensions

| Tension | Note |
|---|---|
| No score | It keeps the document true in every room, and it is the first thing every reader asks for |
| Derived, not templated | It is the only way the document can be right about your agent, and it means we cannot hand you one without knowing your shape |
| Twenty one of ninety nine measured | It is honest, and it means most rows are derived from documentation rather than observed |
| The barrier column | It makes the document useful, and it makes most current deployments look unbounded, because most prohibitions today are the second kind |
| The mandate is already known | It makes elicitation cheap, and a mandate nobody wrote down is one nobody can be held to |
| Describing without judging | It is what makes the ABP an input to everything above it, and it means the ABP alone tells you nothing about whether to worry |

## Open Questions

1. Which name for the deployment shapes, so that two people describing the same setup produce the same ABP?
2. What is the smallest grant that still produces a non empty delta, and is that the right first example?
3. Who elicits the mandate when the person at the table is not the person who authorised the agent?
4. How is quantity added to the primitives without breaking the nine profiles already published?
5. What does the validity statement look like when the product updates weekly?
6. Does the label work printed, at card size, with nine fields?
7. What is the right form for the data files so that people can propose a correction with its evidence attached?

## Relationship To Previous Briefs

This document consolidates three briefs of 11 September 2026: one on the product and how it is sold, one on the ABP as a graph with its renderings and its enforcement targets, and one on what sits above it. It inherits the rulings of 10 September on the words that may not be used, and the rule of 20 August that the record is published and the verdict is not. The capability grammar, the nine profiles and the four barriers come from the published capability map and the published simulation, and this document adds nothing to them except a name for the whole.

## Key Claims

| # | Claim |
|---|---|
| 1 | Most people who deploy an agent know what they asked it to do, and almost nobody knows what it can do |
| 2 | An ABP is a written description, for one agent in one deployment, of the grant, the mandate, the delta and the barrier |
| 3 | The mandate is elicited, the grant is measured, the delta is computed and never stored, and the barrier is recorded per capability |
| 4 | A grant on its own is an inventory, and the mandate is what turns it into a finding |
| 5 | There are four kinds of barrier, and only a boundary enforced above the agent that it cannot reach bounds anything |
| 6 | All four major model providers have said in 2026 that an instruction at the prompt layer can be bypassed, so a prohibition without its barrier is an unsupported claim |
| 7 | Changing one setting on one product moves every barrier in the delta by one row while the grant, the mandate and the delta stay the same |
| 8 | The ABP describes and does not judge, because the same document is dangerous in one deployment and harmless in another |
| 9 | So the ABP carries no score, and the score lives in the risk work above it, where the assets are known and a named person signs |
| 10 | The label carries two numbers that matter, excess and unbounded excess, and only the second can be moved by buying a control |
| 11 | A grant you hold over other people's material is not a grant you may pass on, and the ABP is where that question becomes askable |
| 12 | The parts of this existed already, published, and what did not exist was one page per deployment, derived, with the barrier, and without a score |

## Sources

All read 11 September 2026 unless stated.

**The measurements and the vocabulary.** The capability map, its nine profiles, twenty three primitives, four barriers, undo classes and its statement that twenty one of ninety nine rows were measured, at https://what-can-it-do.games.sgit.ai/map/index.html, with its mandates and deltas at the same site. The published simulation with a grant of twelve, a mandate of four and a delta of eight at https://sgit.ai/demos/vaults/licence-to-operate/index.html. The graph rules at https://graphs.sgit.ai/.

**That a prompt is not a control.** https://www.anthropic.com/engineering/how-we-contain-claude, 25 May 2026, and the approval rate reported at https://www.infoq.com/news/2026/07/anthropic-claude-containment/, 22 July 2026. https://aws.amazon.com/blogs/security/why-policy-in-amazon-bedrock-agentcore-chose-cedar-for-securing-agentic-workflows/, 20 May 2026. https://www.microsoft.com/en-us/security/blog/2026/07/16/least-privilege-for-ai-agents-identity-access-and-tool-binding/, 16 July 2026. The approach paper summarised at https://simonwillison.net/2025/Jun/15/ai-agent-security/, 2025.

**Where it comes from.** The rights expression vocabulary at https://www.w3.org/TR/odrl-model/, recommendation of 15 February 2018, and its adoption at https://www.w3.org/blog/2025/w3c-standard-odrl-policy-gaining-industry-adoption, 23 October 2025. The agentic application risk list at https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/, 9 December 2025. The consumer guidance at https://www.gov.uk/government/publications/complying-with-consumer-law-when-using-ai-agents, 9 March 2026. The underwriter's scoping requirements at https://www.aiuc-1.com/scoping. The template offer at https://agentguru.co/.

**The pass you may not hand on.** Article 28(2) and 28(4) of the General Data Protection Regulation. The warning notice of 17 August 2026 at https://www.sra.org.uk/.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.70__foundation__agent-behaviour-policy-you-know-what-you-asked-for-and-you-do-not-know-what-it-can-do/index.html)*
