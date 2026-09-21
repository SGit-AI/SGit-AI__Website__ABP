# A CI job on a hosted runner, under a service account

> An Agent Behaviour Policy for actions runner (a hosted CI job): a grant of 8, a mandate of 5, an excess of 4 and an unbounded excess of 3. Derived from published data, with no score.

*Source: <https://abp.sgit.ai/examples/github-actions-hosted-runner/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Examples](../../examples/index.md) / A CI job on a hosted runner, under a service account

# A CI job on a hosted runner, under a service account

**The deployment shape:** Actions runner (a hosted CI job), variant `ci`.

Persistence, and reach beyond the turn. A service account rather than a person, a push to a code host, and the irreversible class arriving in a deployment nobody thinks of as an agent.

## Before you scroll

> **Write down a number.** Of the 23 capability primitives, how many do you think this deployment has? And of those, how many do you think the person who deployed it asked for? The page answers both below. Writing the guess down first is the one thing that makes a static page do any of the work [the game](https://what-can-it-do.games.sgit.ai/map/index.html) does.

## The label

One line, on the outside, for anybody. Two numbers matter: **excess** answers the question this document exists for, and **unbounded excess** is the only number on it that buying a control moves.

| Field | Value | Meaning |
|---|---|---|
| Shape | **Actions runner (a hosted CI job), ci** | The named deployment, in the product's published words |
| Grant | **8 of 23 primitives** | Everything the agent can do |
| Mandate | **5 primitives** | What the deployer authorised and expected |
| Excess | **4** | In the grant, not in the mandate. The finding |
| Unbounded excess | **3** | Excess whose barrier is not a control. The only number a control purchase moves |
| Irreversible | **3** | Granted capabilities with undo: no, as published |
| Widest reach | **world** | The furthest reach class in the grant |
| Measured | **8 of 8 rows** | Rows seen directly against rows derived |
| As at | **11 September 2026, pack v0.8.0** | The date and the source version |

> **There is no score on this label, and there will not be one.** The same ABP is dangerous in one deployment and harmless in the next and nothing about the document changed. A policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the assets, the consequences and the date, and only the first of those is here. The score belongs to [the risk work above it](https://risks.sgit.ai/), where the assets are known and a named person signs.

## 1. The shape

An ephemeral CI job with no agent, no hooks, and one platform-enforced grant: the workflow's permissions block. MEASURED on 26 August by measure.py inside the runner (the library's second entry), translated into findings on 5 September. Unrestricted egress; the token cannot write.

Tools in this shape: `the job's shell`. Profile version `2026-08-26`, surface `ci`.

What the reach classes mean here, which is the profile's to say rather than the grammar's: **host** means the runner - destroyed after the job; not your machine, **tenant** means the repository, with the workflow's token, **world** means the internet, unrestricted.

**What it cannot reach, and why.** A grant is as much about the boundaries that hold as the ones that do not.

| What | Why | Source |
|---|---|---|
| your machine | a hosted runner | `library entry 2` |
| the repository, for writing | the token is contents:read | `evidence: ci.permissions-block` |

## 2. The grant, measured

Everything the agent can do: **8 of 23** primitives. Ordered irreversible first, then weakest barrier first. **Reversibility is a property of the action, not a severity**, and stating it as the reason is what keeps the ordering descriptive.

|  | Capability | Undo | Barrier | Known by | The mandate |
|---|---|---|---|---|---|
| ● | [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) Delete files anywhere the account can reach | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`read.file.host`](../../model/capabilities/read.file.host/index.md) Read any file the account can reach | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) Reach any host on the internet | no | none (not a control) | observed | **authorised** |
| ● | [`execute.process.host`](../../model/capabilities/execute.process.host/index.md) Run programs as the account | with-effort | none (not a control) | observed | **authorised** |
| ● | [`write.file.host`](../../model/capabilities/write.file.host/index.md) Change any file the account can reach | with-effort | none (not a control) | observed | **excess** (unstated) |
| ● | [`write.file.project`](../../model/capabilities/write.file.project/index.md) Change the project it is working on | with-effort | none (not a control) | observed | **authorised** |
| ○ | [`write.repository.project`](../../model/capabilities/write.repository.project/index.md) Commit to the repository it was pointed at | with-effort | boundary | observed | **excess** (unstated) |
| ● | [`read.file.project`](../../model/capabilities/read.file.project/index.md) Read the project it is working on | yes | none (not a control) | observed | **authorised** |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## 3. The mandate, elicited

**A CI job on a hosted runner.** Check out the code, build it, run the tests, fetch what it needs, and - when a release is cut - push the tag. I did not want it reading credentials beyond its own token.

A mandate is elicited rather than measured, in minutes, because the deployer already knows it. This one was not: it is a first draft written to be argued with, authored 2026-09-09 by the site, as a starting point - not measured, not surveyed; the first thing to argue with. It authorises **5** primitives, refuses **1** and says nothing either way about **17**. [Propose a change to it](../../data/index.md).

| Capability | What the mandate says about it |
|---|---|
| [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md) | deliberately in the mandate: most release workflows push a tag, and this profile's token is contents:read - so this row is a shortfall, and the kind the game calls 'a gap you were counting on' |
| [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) | unstated: the runner is destroyed after the job |

## 4. The delta, derived

> **This delta is derived and never authored.** Nobody wrote it. It is the output of a computation over the grant and the mandate, stored at [`/data/deltas/github__actions-runner__ci__ci-job.json`](../../data/deltas/github__actions-runner__ci__ci-job.json) with the version of both inputs pinned, the time it was computed and the version of the computation that produced it. **The release gate recomputes it on every build and fails on a single row of disagreement**, which is how a machine holds a rule that forbids the act rather than the artefact. [Why this changed this morning](../../model/delta/index.md).

**Excess: 4.** In the grant and not in the mandate. That is the published definition and it is wider than the set the mandate refused outright: **0** were refused and **4** were never mentioned. A capability the mandate never mentioned was not authorised, and hiding the split would be the other kind of dishonesty.

**Unbounded excess: 3.** The excess whose barrier is one of the first three rows: nothing, a rule somebody wrote down, or a setting the agent's own account could change. None of those bounds anything.

The excess is listed as prohibitions below.

**Shortfall: 1.** Asked for and cannot: [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md).

## The same facts, as a figure

The table above is complete and it is the wrong shape for the one question this document exists to answer, which is how much of the right hand side has nothing on the left. **A mark with no line reaching it is excess.**

*[A figure here in the page: the mandate in one column and the grant in the other, with a line joining every capability that is in both. **4 marks on the grant side have no line reaching them**, of which 3 sit at a barrier that is not a control, and 1 on the mandate side reach nothing. The table below the figure carries the same facts, row by row.]*

## 5. The prohibitions

The enforceable projection of the delta: one sentence per excess capability, each carrying the layer it would be enforced at and whether it is enforced today. **3 of 4 are not enforced today.** They are sentences, not controls.

|  | Prohibition | Barrier today | Enforced today | Layer a control would sit at |
|---|---|---|---|---|
| ● | The agent must not delete files anywhere the account can reach. [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not read any file the account can reach. [`read.file.host`](../../model/capabilities/read.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not change any file the account can reach. [`write.file.host`](../../model/capabilities/write.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ○ | The agent must not commit to the repository it was pointed at. [`write.repository.project`](../../model/capabilities/write.repository.project/index.md) | boundary | **enforced** | already enforced above the grant |

> **Why the barrier is on every row.** A prohibition shown without its barrier manufactures assurance. All four major model providers stated in their own 2026 words that an instruction at the prompt layer can be bypassed, and the rule underneath is older than any of them: a control bounds a grant only if it is enforced by something the grant does not include. The right hand column is where a control would have to sit, not a recommendation that you buy one.

## 6. The provenance

> **Provenance.** 8 of 8 capability rows on this page were measured, meaning seen directly on the thing itself. The other 0 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../../data/upstream/pack.json).

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

agent [`github-actions-hosted-runner`](../../examples/github-actions-hosted-runner/index.md) **is-granted** capability [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) **bounded-by** barrier [`none`](../../model/barriers/index.md) **which-exceeds** mandate [`ci-job`](../../model/index.md) **and-is** undo [`no`](../../model/undo/index.md).

### The same row, across nine universes

That path stays inside one vocabulary. The same row also crosses nine worlds, each owned by a different party and each with its own ontology, and the fifth rule holds across them too. Built from this page's own data on every build; [what the universes are](../../model/universes/index.md).

> The words `delete`, `file` and `host` spell a primitive that the shape `ci` grants through the job's shell as a row whose evidence tier is observed, bounded by `none`, which nothing enforces and which is not a control, which the mandate `ci-job` left unstated, so the derivation of 2026-09-11 records it as unbounded excess, which the leaflet renders as a prohibition that is a sentence and not a control today, and which the licence in riskmandate.ai's vault for this shape carries as a condition beside its enforcer, for an owner who has not yet signed.

> **Every number on this page is a leaf assertion in one fact set**, at [`/data/facts/github__actions-runner__ci__ci-job.json`](../../data/facts/github__actions-runner__ci__ci-job.json), and the release gate parses the label, the leaflet, the prohibitions and the figure back out of this page's markdown twin and fails the build on a single one that differs. The label and the leaflet are two renderings of one fact set, and that is checked rather than asserted.

[The four objects](../../model/index.md) · [The capability grammar](../../model/capabilities/index.md) · [The barriers](../../model/barriers/index.md) · [This shape as JSON](../../data/profiles/github/actions-runner/ci.json) · [This mandate as JSON](../../data/mandates/ci-job.json) · [The fact set](../../data/facts/github__actions-runner__ci__ci-job.json)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/examples/github-actions-hosted-runner/index.html)*
