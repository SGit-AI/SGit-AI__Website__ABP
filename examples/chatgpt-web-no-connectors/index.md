# Chat in the browser, nothing connected

> An Agent Behaviour Policy for chatGPT (in the browser, no connectors): a grant of 1, a mandate of 1, an excess of 0 and an unbounded excess of 0. Derived from published data, with no score.

*Source: <https://abp.sgit.ai/examples/chatgpt-web-no-connectors/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Examples](../../examples/index.md) / Chat in the browser, nothing connected

# Chat in the browser, nothing connected

**The deployment shape:** ChatGPT (in the browser, no connectors), variant `default`.

The smallest grant in the set. A reader who does not believe an agent can do much starts here, and finds that the delta is still not empty. It establishes the four objects with the fewest moving parts.

## Before you scroll

> **Write down a number.** Of the 23 capability primitives, how many do you think this deployment has? And of those, how many do you think the person who deployed it asked for? The page answers both below. Writing the guess down first is the one thing that makes a static page do any of the work [the game](https://what-can-it-do.games.sgit.ai/map/index.html) does.

## The label

One line, on the outside, for anybody. Two numbers matter: **excess** answers the question this document exists for, and **unbounded excess** is the only number on it that buying a control moves.

| Field | Value | Meaning |
|---|---|---|
| Shape | **ChatGPT (in the browser, no connectors), default** | The named deployment, in the product's published words |
| Grant | **1 of 23 primitives** | Everything the agent can do |
| Mandate | **1 primitives** | What the deployer authorised and expected |
| Excess | **0** | In the grant, not in the mandate. The finding |
| Unbounded excess | **0** | Excess whose barrier is not a control. The only number a control purchase moves |
| Irreversible | **0** | Granted capabilities with undo: no, as published |
| Widest reach | **project** | The furthest reach class in the grant |
| Measured | **0 of 1 rows** | Rows seen directly against rows derived |
| As at | **11 September 2026, pack v0.8.0** | The date and the source version |

> **There is no score on this label, and there will not be one.** The same ABP is dangerous in one deployment and harmless in the next and nothing about the document changed. A policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the assets, the consequences and the date, and only the first of those is here. The score belongs to [the risk work above it](https://risks.sgit.ai/), where the assets are known and a named person signs.

## 1. The shape

An assistant in the vendor's environment. It reaches what you paste or upload and nothing on your machine: the vendor's environment is a boundary you did not build. DERIVED from the assess library's web tree. Browsing, if on, is the vendor's egress, not yours.

Tools in this shape: `conversation and uploads`. Profile version `2026-09-05`, surface `web`.

What the reach classes mean here, which is the profile's to say rather than the grammar's: **host** means the vendor's environment; not your machine, **tenant** means nothing of yours, **world** means the vendor's egress, if browsing is on.

**What it cannot reach, and why.** A grant is as much about the boundaries that hold as the ones that do not.

| What | Why | Source |
|---|---|---|
| your machine's files | the vendor's environment is a boundary you did not build | `assess/library.json (web: home)` |
| your accounts | no connectors are on | `assess/library.json (web: connect)` |

## 2. The grant, measured

Everything the agent can do: **1 of 23** primitives. Ordered irreversible first, then weakest barrier first. **Reversibility is a property of the action, not a severity**, and stating it as the reason is what keeps the ordering descriptive.

|  | Capability | Undo | Barrier | Known by | The mandate |
|---|---|---|---|---|---|
| ● | [`read.file.project`](../../model/capabilities/read.file.project/index.md) Read the project it is working on | yes | none (not a control) | derived | **authorised** |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## 3. The mandate, elicited

**Chat in the browser, nothing connected.** I paste things in and read what comes back. That is the whole mandate, and the honest baseline: a chat window with nothing connected should be able to do nothing else.

A mandate is elicited rather than measured, in minutes, because the deployer already knows it. This one was not: it is a first draft written to be argued with, authored 2026-09-09 by the site, as a starting point - not measured, not surveyed; the first thing to argue with. It authorises **1** primitives, refuses **14** and says nothing either way about **8**. [Propose a change to it](../../data/index.md).

## 4. The delta, derived

> **This delta is derived and never authored.** Nobody wrote it. It is the output of a computation over the grant and the mandate, stored at [`/data/deltas/openai__chatgpt-web__default__chat-no-connectors.json`](../../data/deltas/openai__chatgpt-web__default__chat-no-connectors.json) with the version of both inputs pinned, the time it was computed and the version of the computation that produced it. **The release gate recomputes it on every build and fails on a single row of disagreement**, which is how a machine holds a rule that forbids the act rather than the artefact. [Why this changed this morning](../../model/delta/index.md).

**Excess: 0.** In the grant and not in the mandate. That is the published definition and it is wider than the set the mandate refused outright: **0** were refused and **0** were never mentioned. A capability the mandate never mentioned was not authorised, and hiding the split would be the other kind of dishonesty.

**Unbounded excess: 0.** The excess whose barrier is one of the first three rows: nothing, a rule somebody wrote down, or a setting the agent's own account could change. None of those bounds anything.

> **The delta on this shape is empty, and that is a result rather than a failure.** Everything this deployment can do, the mandate asked for. An ABP that could never come back with nothing to report would not be a description, it would be a sales document, and the other four examples would be worth less for it. Note what the grant still is, though: one capability, and a record once read is exposure that cannot be unread, on the vendor's side.

**Shortfall: 0.** There is nothing the mandate asked for that this deployment cannot do.

## The same facts, as a figure

The table above is complete and it is the wrong shape for the one question this document exists to answer, which is how much of the right hand side has nothing on the left. **A mark with no line reaching it is excess.**

*[A figure here in the page: the mandate in one column and the grant in the other, with a line joining every capability that is in both. **0 marks on the grant side have no line reaching them**, of which 0 sit at a barrier that is not a control. The table below the figure carries the same facts, row by row.]*

## 5. The prohibitions

The enforceable projection of the delta: one sentence per excess capability, each carrying the layer it would be enforced at and whether it is enforced today.

> **There are no prohibitions on this ABP, because the delta is empty.** Nothing this deployment can do sits outside what the mandate asked for. That does not mean nothing is worth deciding: it means the decision was already taken when the mandate was written.

> **Why the barrier is on every row.** A prohibition shown without its barrier manufactures assurance. All four major model providers stated in their own 2026 words that an instruction at the prompt layer can be bypassed, and the rule underneath is older than any of them: a control bounds a grant only if it is enforced by something the grant does not include. The right hand column is where a control would have to sit, not a recommendation that you buy one.

## 6. The provenance

> **Provenance.** 0 of 1 capability rows on this page were measured, meaning seen directly on the thing itself. The other 1 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../../data/upstream/pack.json).

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

agent [`chatgpt-web-no-connectors`](../../examples/chatgpt-web-no-connectors/index.md) **is-granted** capability [`read.file.project`](../../model/capabilities/read.file.project/index.md) **bounded-by** barrier [`none`](../../model/barriers/index.md) **which-exceeds** mandate [`chat-no-connectors`](../../model/index.md) **and-is** undo [`yes`](../../model/undo/index.md).

### The same row, across nine universes

That path stays inside one vocabulary. The same row also crosses nine worlds, each owned by a different party and each with its own ontology, and the fifth rule holds across them too. Built from this page's own data on every build; [what the universes are](../../model/universes/index.md).

> The words `read`, `file` and `project` spell a primitive that the shape `default` grants through conversation and uploads as a row whose evidence tier is derived, bounded by `none`, which nothing enforces and which is not a control, which the mandate `chat-no-connectors` asked for, so the derivation of 2026-09-11 records it as aligned, which the leaflet renders as an authorised row, and which the licence in riskmandate.ai's vault for this shape carries in its scope, for an owner who has not yet signed.

> **Every number on this page is a leaf assertion in one fact set**, at [`/data/facts/openai__chatgpt-web__default__chat-no-connectors.json`](../../data/facts/openai__chatgpt-web__default__chat-no-connectors.json), and the release gate parses the label, the leaflet, the prohibitions and the figure back out of this page's markdown twin and fails the build on a single one that differs. The label and the leaflet are two renderings of one fact set, and that is checked rather than asserted.

[The four objects](../../model/index.md) · [The capability grammar](../../model/capabilities/index.md) · [The barriers](../../model/barriers/index.md) · [This shape as JSON](../../data/profiles/openai/chatgpt-web/default.json) · [This mandate as JSON](../../data/mandates/chat-no-connectors.json) · [The fact set](../../data/facts/openai__chatgpt-web__default__chat-no-connectors.json)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/examples/chatgpt-web-no-connectors/index.html)*
