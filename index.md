# Agent Behaviour Policy

> You know what you asked for. You do not know what it can do. The Agent Behaviour Policy is the document that puts the two on the same page: the grant, the mandate, the delta and the barrier, for one agent in one deployment, with no score.

*Source: <https://abp.sgit.ai/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

# You know what you asked for. You do not know what it can do.

An **Agent Behaviour Policy** is a written description, for one agent in one deployment, of everything it can do, what it was authorised to do, the difference between the two, and what actually stands in the way. It is derived from the deployment rather than copied from a template. **It describes and it does not judge, so it carries no score.**

## The gap

**You know what you asked for.** Draft the reply, fix the build, summarise the ticket, book the travel. That is the mandate, and it is usually clear, whether or not anybody wrote it down.

**You do not know what it can do.** The agent runs with an account, on a machine, inside a container or on a desktop, with credentials and network access and a set of tools. Everything those permit is the grant. It is almost never enumerated, and when it is, it is larger than the person who deployed the agent expected.

> **Before you scroll.** For a deployment you actually run, write down how many of 23 capability primitives you think it has, and how many of those you asked for. Then read [the five worked examples](examples/index.md). The gap between your two numbers is the reason this document type exists.

## The four objects

An ABP is not a single list. It is four objects, and the order they are produced in matters.

| Object | What it is | How it is obtained |
|---|---|---|
| **The mandate** | What the agent is authorised and expected to do | **Elicited.** In minutes, because the deployer already knows it |
| **The grant** | Everything the agent can do | **Measured.** From the deployment shape, the account and the credentials |
| **The delta** | Excess where it can and you did not ask; shortfall where you asked and it cannot | **Derived.** Recomputed whenever the grant or the mandate changes, stored with the versions of both, and never edited by hand |
| **The barrier** | What stands between the agent and each capability | **Recorded**, per capability, from one of four kinds |

> **The delta is derived and never authored.** Nobody writes one: it is only ever the output of a computation over the grant and the mandate, and it is stored with the versions of both inputs and the time it was computed. This site said the opposite this morning, and **the correction is published rather than applied quietly**: [what changed and what follows from it](model/delta/index.md).

**A grant on its own is an inventory, and nobody acts on an inventory.** *Your agent can do three hundred and forty things* is a shrug. *Your agent can do three hundred and forty things and you authorised twelve* is a finding. [The model, in full](model/index.md).

## Only one kind of thing is actually in the way

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

> **A control bounds a grant only if it is enforced by something the grant does not include.** Read the third and fourth rows together and the test falls out of them. A setting the agent's own account could change is not a control, because the grant includes the ability to remove the bound. [The barrier](model/barriers/index.md).

## One setting, two documents

The clearest way to see what an ABP does is to change one setting and watch the document change. A coding agent on a developer's own machine, profiled twice: once with confirmations enabled, once with them disabled. Same product, same machine, same account.

|  | Confirmations on | Confirmations off |
|---|---|---|
| Grant | 16 | 16 |
| Mandate | 5 | 5 |
| Excess | 12 | 12 |
| Unbounded excess | 12 | 12 |
| Barrier on `execute.process.host` | setting (not a control) | none (not a control) |

**1 barrier moved and not one number did.** The confirmation prompt was the only thing standing between an authorised capability and the whole of the machine, and it was a setting the agent's own account could change, which is the third row and not the fourth. **The ABP is about the deployment, not the product**, and the pair says it in a way no paragraph can: [confirmations on](examples/claude-code-cli-confirmations-enabled/index.md) and [confirmations off](examples/claude-code-cli-confirmations-disabled/index.md).

## It describes and it does not judge

**The same ABP is dangerous in one deployment and harmless in another, and nothing about the document changed.** The most permissive grant imaginable, running where there are no assets and nothing reachable, is a low risk. The same grant with a production database attached tomorrow is a high one. Risk is a function of the ABP, the assets, the consequences and the date, and **the ABP is the one input that does not move.**

> **A policy cannot be dangerous. A deployment can.** So there is no rating on an ABP, no traffic light and no risk level, anywhere on this site or in its data. Every reader asks for one. **The score has a home and it is [the risk work above this](https://risks.sgit.ai/)**, where the assets are known and a named person signs. The people who sell do not sign, which is why the two are separate products and not two sections of one.

## What is here

**[What an ABP is](what-is-an-abp/index.md)**: The foundation document: the definition, the four objects, the barrier, one worked example with published numbers, and the questions we would like answered.
This is the document, rendered. Not a summary of it.

**[The delta](model/delta/index.md)**: Derived and never authored. Stored with its inputs pinned, recomputed when either moves, and the history is the business case.
Corrected on 11 September, in the open.

**[The model](model/index.md)**: The 23 capability primitives, the four barriers, the three undo classes, the graph rules and the schema.
Promoted from a published map, not invented here.

**[Five worked examples](examples/index.md)**: From the smallest grant in the set to a service account that outlives the turn. Derived from the data, with the delta computed on the page.
Each states how many rows were measured.

**[The data](data/index.md)**: The published vocabulary as JSON, at stable addresses with cross origin access, with the source bytes it was promoted from.
21 of 99 rows measured.

**[The docs](docs/index.md)**: Every reference document behind this site, rendered, each one click from its source bytes.
The index is generated from the files present.

**[Where a score lives](https://risks.sgit.ai/)**: The ABP is the input. The risk work above it knows the assets and the consequences, and a named professional signs.
Not here, and that is the point.

## What an ABP is not

- **Not an acceptable use policy.** That governs a person's use of a system. An ABP governs what an agent can and may do.
- **Not a risk assessment.** It has no assets in it and no consequences. It is the input to one.
- **Not a compliance assessment, a certification, an audit or a security review** of anything or anybody.
- **Not a guardrail.** It is what guardrails are compiled from. The barrier column says which prohibitions are guardrails already and which are sentences.
- **Not a claim about any product.** The capability rows come from published documentation and published measurement, with the source, the date and the measured ratio stated, and no adjective attached to any of them.
- **Not a template.** It is derived from one deployment, and a template cannot know what your agent can do.

## This site is the library. It is free, and it stays free

The argument, the model, the examples and the data are published here. **There is no checkout on this site and there will not be one.** The data files are the shared facts and they live in the repository so that people can propose changes to them, with evidence attached.

[Propose a change](data/index.md) · [The repository](https://github.com/SGit-AI/SGit-AI__Website__ABP) · [Everything on this site, in one file](llms-full.txt)

> **Provenance.** 21 of 99 capability rows on this page were measured, meaning seen directly on the thing itself. The other 78 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](data/upstream/pack.json).

> **Validity.** This describes the deployment shape as at 11 September 2026, from a twin last synchronised at no twin: these shapes are published profiles, not a synchronised environment. It is not an expiry and it does not mean stale: if the risk changed, the deployment changed, not this document.

---

*[Site index for agents](llms.txt) · [HTML version](https://abp.sgit.ai/index.html)*
