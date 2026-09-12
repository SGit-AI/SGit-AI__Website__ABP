# A browser extension with broad host permissions

> An Agent Behaviour Policy for A browser extension with broad host permissions: a grant of 3, a mandate of 1, an excess of 2 and an unbounded excess of 2. Derived from published data, with no score.

*Source: <https://abp.sgit.ai/examples/browser-extension-broad-host-permissions/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Examples](../../examples/index.md) / A browser extension with broad host permissions

# A browser extension with broad host permissions

**The deployment shape:** A browser extension with broad host permissions, variant `broad-host-permissions`.

Other people's data, and the mandate nobody wrote down. The pages you visit were not all yours to hand over. This is where the mandate reaches further than your own material.

## Before you scroll

> **Write down a number.** Of the 23 capability primitives, how many do you think this deployment has? And of those, how many do you think the person who deployed it asked for? The page answers both below. Writing the guess down first is the one thing that makes a static page do any of the work [the game](https://what-can-it-do.games.sgit.ai/map/index.html) does.

## The label

One line, on the outside, for anybody. Two numbers matter: **excess** answers the question this document exists for, and **unbounded excess** is the only number on it that buying a control moves.

| Field | Value | Meaning |
|---|---|---|
| Shape | **A browser extension with broad host permissions, broad-host-permissions** | The named deployment, in the product's published words |
| Grant | **3 of 23 primitives** | Everything the agent can do |
| Mandate | **1 primitives** | What the deployer authorised and expected |
| Excess | **2** | In the grant, not in the mandate. The finding |
| Unbounded excess | **2** | Excess whose barrier is not a control. The only number a control purchase moves |
| Irreversible | **3** | Granted capabilities with undo: no, as published |
| Widest reach | **world** | The furthest reach class in the grant |
| Measured | **0 of 3 rows** | Rows seen directly against rows derived |
| As at | **11 September 2026, pack v0.8.0** | The date and the source version |

> **There is no score on this label, and there will not be one.** The same ABP is dangerous in one deployment and harmless in the next and nothing about the document changed. A policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the assets, the consequences and the date, and only the first of those is here. The score belongs to [the risk work above it](https://risks.sgit.ai/), where the assets are known and a named person signs.

## 1. The shape

Not an agent by name, and it has a grant: an extension granted 'read and change all your data on all websites' reads every page you visit, reaches any host, and acts inside the sites you are logged into. Nobody wrote it a mandate. DERIVED from the permission model the browser documents; not measured on any instance.

Tools in this shape: `the extension`. Profile version `2026-09-05`, surface `extension`.

What the reach classes mean here, which is the profile's to say rather than the grammar's: **host** means your browser - every page, every logged-in site, **tenant** means the sites you are logged into, as you, **world** means the internet, from your browser.

**What it cannot reach, and why.** A grant is as much about the boundaries that hold as the ones that do not.

| What | Why | Source |
|---|---|---|
| files on your disk | the browser sandbox; an extension reads pages, not the filesystem | `the browser's extension permission model` |

## 2. The grant, measured

Everything the agent can do: **3 of 23** primitives. Ordered irreversible first, then weakest barrier first. **Reversibility is a property of the action, not a severity**, and stating it as the reason is what keeps the ordering descriptive.

|  | Capability | Undo | Barrier | Known by | The mandate |
|---|---|---|---|---|---|
| ● | [`read.record.browsing`](../../model/capabilities/read.record.browsing/index.md) Read every page you visit | no | none (not a control) | documented | **authorised** |
| ● | [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) Reach any host on the internet | no | none (not a control) | documented | **excess** (refused) |
| ◐ | [`authenticate-as.credential.tenant`](../../model/capabilities/authenticate-as.credential.tenant/index.md) Act in accounts with the credentials it holds | no | setting (not a control) | documented | **excess** (refused) |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## 3. The mandate, elicited

**A browser extension I installed.** I want it to work on the sites I use it on. I did not install it so that it could see every page I visit, act inside the accounts I am logged into, or send what it sees anywhere.

A mandate is elicited rather than measured, in minutes, because the deployer already knows it. This one was not: it is a first draft written to be argued with, authored 2026-09-09 by the site, as a starting point - not measured, not surveyed; the first thing to argue with. It authorises **1** primitives, refuses **2** and says nothing either way about **20**. [Propose a change to it](../../data/index.md).

| Capability | What the mandate says about it |
|---|---|
| [`read.record.browsing`](../../model/capabilities/read.record.browsing/index.md) | the want is 'the sites I chose'; the grant is every page - the same capability at two different reaches, which is what the reduction ('on click, or on a list of sites') narrows |

## 4. The delta, derived

> **This delta is derived and never authored.** Nobody wrote it. It is the output of a computation over the grant and the mandate, stored at [`/data/deltas/generic__browser-extension__broad-host-permissions__browser-extension-i-installed.json`](../../data/deltas/generic__browser-extension__broad-host-permissions__browser-extension-i-installed.json) with the version of both inputs pinned, the time it was computed and the version of the computation that produced it. **The release gate recomputes it on every build and fails on a single row of disagreement**, which is how a machine holds a rule that forbids the act rather than the artefact. [Why this changed this morning](../../model/delta/index.md).

**Excess: 2.** In the grant and not in the mandate. That is the published definition and it is wider than the set the mandate refused outright: **2** were refused and **0** were never mentioned. A capability the mandate never mentioned was not authorised, and hiding the split would be the other kind of dishonesty.

**Unbounded excess: 2.** The excess whose barrier is one of the first three rows: nothing, a rule somebody wrote down, or a setting the agent's own account could change. None of those bounds anything. Every one of the 2 excess capabilities here is unbounded.

The excess is listed as prohibitions below.

**Shortfall: 0.** There is nothing the mandate asked for that this deployment cannot do.

## The same facts, as a figure

The table above is complete and it is the wrong shape for the one question this document exists to answer, which is how much of the right hand side has nothing on the left. **A mark with no line reaching it is excess.**

*[A figure here in the page: the mandate in one column and the grant in the other, with a line joining every capability that is in both. **2 marks on the grant side have no line reaching them**, of which 2 sit at a barrier that is not a control. The table below the figure carries the same facts, row by row.]*

## 5. The prohibitions

The enforceable projection of the delta: one sentence per excess capability, each carrying the layer it would be enforced at and whether it is enforced today. **2 of 2 are not enforced today.** They are sentences, not controls.

|  | Prohibition | Barrier today | Enforced today | Layer a control would sit at |
|---|---|---|---|---|
| ● | The agent must not reach any host on the internet. [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ◐ | The agent must not act in accounts with the credentials it holds. [`authenticate-as.credential.tenant`](../../model/capabilities/authenticate-as.credential.tenant/index.md) | setting | **not enforced** (a sentence, not a control) | boundary |

> **Why the barrier is on every row.** A prohibition shown without its barrier manufactures assurance. All four major model providers stated in their own 2026 words that an instruction at the prompt layer can be bypassed, and the rule underneath is older than any of them: a control bounds a grant only if it is enforced by something the grant does not include. The right hand column is where a control would have to sit, not a recommendation that you buy one.

## 6. The provenance

> **Provenance.** 0 of 3 capability rows on this page were measured, meaning seen directly on the thing itself. The other 3 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../../data/upstream/pack.json).

**No row here was obtained by probing anybody's system.** A row is measured only from a system we are entitled to run, or from the vendor's own published documentation. Causing a computer to output data intending unauthorised access is an offence with no damage requirement and no research defence.

## 7. What this is not

> **This is not an assessment.** Nothing here is an audit, a certification, a compliance assessment or a security review of any named product. It is an illustration of a method, using a published configuration, and every row carries its source, its date and whether it was measured or derived. No adjective is attached to any of it, and there is no score.

> **Validity.** This describes the deployment shape as at 11 September 2026, from a twin last synchronised at no twin: these shapes are published profiles, not a synchronised environment. It is not an expiry and it does not mean stale: if the risk changed, the deployment changed, not this document.

**Three clocks, and only the first is ours.** An ABP is exactly as fresh as the twin, and the twin is exactly as fresh as its connection to somebody else's systems. That is a parameter rather than a defect to hide, and the gap between the second clock and the third belongs to the risk layer, because how much it matters depends on the assets.

| Clock | What it measures | Who controls it |
|---|---|---|
| The ABP's clock | When the grant was last measured or calibrated | Us, and it can run on events |
| The twin's clock | When the twin last synchronised with the real environment | The customer's integration |
| Reality's clock | Never stops | Nobody |

## Follow one capability through the model

The fifth graph rule says a path should read as a sentence in the reader's own language, and it is the acceptance test for this model:

agent [`browser-extension-broad-host-permissions`](../../examples/browser-extension-broad-host-permissions/index.md) **is-granted** capability [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) **bounded-by** barrier [`none`](../../model/barriers/index.md) **which-exceeds** mandate [`browser-extension-i-installed`](../../model/index.md) **and-is** undo [`no`](../../model/undo/index.md).

[The four objects](../../model/index.md) · [The capability grammar](../../model/capabilities/index.md) · [The barriers](../../model/barriers/index.md) · [This shape as JSON](../../data/profiles/generic/browser-extension/broad-host-permissions.json) · [This mandate as JSON](../../data/mandates/browser-extension-i-installed.json)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/examples/browser-extension-broad-host-permissions/index.html)*
