# The same coding agent, confirmations off

> An Agent Behaviour Policy for claude Code (the CLI, on your own machine): a grant of 16, a mandate of 5, an excess of 12 and an unbounded excess of 12. Derived from published data, with no score.

*Source: <https://abp.sgit.ai/examples/claude-code-cli-confirmations-disabled/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Examples](../../examples/index.md) / The same coding agent, confirmations off

# The same coding agent, confirmations off

**The deployment shape:** Claude Code (the CLI, on your own machine), variant `local-confirmations-off`.

The same agent, one setting different. Two documents for one agent, differing in one line. It makes the case that the ABP is about the deployment rather than the product in a way no paragraph can.

## Before you scroll

> **Write down a number.** Of the 23 capability primitives, how many do you think this deployment has? And of those, how many do you think the person who deployed it asked for? The page answers both below. Writing the guess down first is the one thing that makes a static page do any of the work [the game](https://what-can-it-do.games.sgit.ai/map/index.html) does.

## The label

One line, on the outside, for anybody. Two numbers matter: **excess** answers the question this document exists for, and **unbounded excess** is the only number on it that buying a control moves.

| Field | Value | Meaning |
|---|---|---|
| Shape | **Claude Code (the CLI, on your own machine), local-confirmations-off** | The named deployment, in the product's published words |
| Grant | **16 of 23 primitives** | Everything the agent can do |
| Mandate | **5 primitives** | What the deployer authorised and expected |
| Excess | **12** | In the grant, not in the mandate. The finding |
| Unbounded excess | **12** | Excess whose barrier is not a control. The only number a control purchase moves |
| Irreversible | **8** | Granted capabilities with undo: no, as published |
| Widest reach | **world** | The furthest reach class in the grant |
| Measured | **0 of 22 rows** | Rows seen directly against rows derived |
| As at | **11 September 2026, pack v0.8.0** | The date and the source version |

> **There is no score on this label, and there will not be one.** The same ABP is dangerous in one deployment and harmless in the next and nothing about the document changed. A policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the assets, the consequences and the date, and only the first of those is here. The score belongs to [the risk work above it](https://risks.sgit.ai/), where the assets are known and a named person signs.

## 1. The shape

The same assistant with its confirmations turned off (an always-allow, or the flag that skips permissions). The rows are the sibling's; what changes is one control: the prompt on execution goes from a setting to nothing. The diff between this profile and local-default is the answer to 'what does turning that off actually give it'. DERIVED, not measured.

Tools in this shape: `shell (Bash)`, `files (Read, Edit, Write)`, `fetch (WebFetch)`. Profile version `2026-09-05`, surface `cli`.

What the reach classes mean here, which is the profile's to say rather than the grammar's: **host** means your machine, as your user account, **tenant** means your accounts, with the credentials in your home directory, **world** means the internet.

## 2. The grant, measured

Everything the agent can do: **16 of 23** primitives. Ordered irreversible first, then weakest barrier first. **Reversibility is a property of the action, not a severity**, and stating it as the reason is what keeps the ordering descriptive.

|  | Capability | Undo | Barrier | Known by | The mandate |
|---|---|---|---|---|---|
| ● | [`authenticate-as.credential.signing`](../../model/capabilities/authenticate-as.credential.signing/index.md) Sign commits with the key it holds | no | none (not a control) | documented | **excess** (refused) |
| ● | [`authenticate-as.credential.tenant`](../../model/capabilities/authenticate-as.credential.tenant/index.md) Act in accounts with the credentials it holds | no | none (not a control) | derived | **excess** (refused) |
| ● | [`create.record.world`](../../model/capabilities/create.record.world/index.md) Publish packages, images or pages under the name it holds | no | none (not a control) | documented | **excess** (refused) |
| ● | [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) Delete files anywhere the account can reach | no | none (not a control) | derived | **excess** (refused) |
| ● | [`read.credential.host`](../../model/capabilities/read.credential.host/index.md) Read credentials stored where it runs | no | none (not a control) | documented | **excess** (refused) |
| ● | [`read.file.host`](../../model/capabilities/read.file.host/index.md) Read any file the account can reach | no | none (not a control) | derived | **excess** (refused) |
| ● | [`read.record.history`](../../model/capabilities/read.record.history/index.md) Read a retained record: shell history, past sessions | no | none (not a control) | documented | **excess** (refused) |
| ● | [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) Reach any host on the internet | no | none (not a control) | derived | **excess** (unstated) |
| ● | [`execute.process.host`](../../model/capabilities/execute.process.host/index.md) Run programs as the account | with-effort | none (not a control) | derived | **authorised** |
| ● | [`write.file.host`](../../model/capabilities/write.file.host/index.md) Change any file the account can reach | with-effort | none (not a control) | derived | **excess** (refused) |
| ● | [`write.file.project`](../../model/capabilities/write.file.project/index.md) Change the project it is working on | with-effort | none (not a control) | derived | **authorised** |
| ● | [`write.repository.project`](../../model/capabilities/write.repository.project/index.md) Commit to the repository it was pointed at | with-effort | none (not a control) | derived | **authorised** |
| ◉ | [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md) Push to a code host (any branch it can reach) | with-effort | expectation (not a control) | derived | **excess** (unstated) |
| ● | [`create.schedule.host`](../../model/capabilities/create.schedule.host/index.md) Create something that outlives the turn where it runs (a cron, a service) | yes | none (not a control) | derived | **excess** (refused) |
| ● | [`read.file.project`](../../model/capabilities/read.file.project/index.md) Read the project it is working on | yes | none (not a control) | derived | **authorised** |
| ◐ | [`grant.credential.self`](../../model/capabilities/grant.credential.self/index.md) Change its own permission settings | yes | setting (not a control) | derived | **excess** (refused) |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## 3. The mandate, elicited

**A coding assistant on my machine.** I want it to read and change the project I pointed it at, run the build and the tests, commit to that repository, and fetch the packages and docs it needs. I did not sign up for it reading the rest of my disk, my credentials or my shell history, sending anything to anyone, publishing under my name, changing its own permission settings, or leaving anything behind that runs after it stops.

A mandate is elicited rather than measured, in minutes, because the deployer already knows it. This one was not: it is a first draft written to be argued with, authored 2026-09-09 by the site, as a starting point - not measured, not surveyed; the first thing to argue with. It authorises **5** primitives, refuses **11** and says nothing either way about **7**. [Propose a change to it](../../data/index.md).

| Capability | What the mandate says about it |
|---|---|
| [`execute.process.host`](../../model/capabilities/execute.process.host/index.md) | 'run my tests' is, on a machine with no sandbox, 'run programs as me' - the want is honest and the consequence is the whole point of the delta |
| [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md) | left unstated on purpose: some people want it to push, some do not, and the mandate should not pretend to know |
| [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) | unstated: the want is 'the hosts it needs', which is the allowed-list capability; whether the whole internet is acceptable is a real decision |

## 4. The delta, computed

> **This delta was computed when this page was built, from the grant and the mandate, and it is not stored anywhere.** A stored delta is a stale claim about somebody's environment, and the environment is the thing that changes.

**Excess: 12.** In the grant and not in the mandate. That is the published definition and it is wider than the set the mandate refused outright: **10** were refused and **2** were never mentioned. A capability the mandate never mentioned was not authorised, and hiding the split would be the other kind of dishonesty.

**Unbounded excess: 12.** The excess whose barrier is one of the first three rows: nothing, a rule somebody wrote down, or a setting the agent's own account could change. None of those bounds anything. Every one of the 12 excess capabilities here is unbounded.

The excess is listed as prohibitions below.

**Shortfall: 1.** Asked for and cannot: [`send.endpoint.allowed`](../../model/capabilities/send.endpoint.allowed/index.md).

## The same facts, as a figure

The table above is complete and it is the wrong shape for the one question this document exists to answer, which is how much of the right hand side has nothing on the left. **A mark with no line reaching it is excess.**

*[A figure here in the page: the mandate in one column and the grant in the other, with a line joining every capability that is in both. **12 marks on the grant side have no line reaching them**, of which 12 sit at a barrier that is not a control, and 1 on the mandate side reach nothing. The table below the figure carries the same facts, row by row.]*

## 5. The prohibitions

The enforceable projection of the delta: one sentence per excess capability, each carrying the layer it would be enforced at and whether it is enforced today. **12 of 12 are not enforced today.** They are sentences, not controls.

|  | Prohibition | Barrier today | Enforced today | Layer a control would sit at |
|---|---|---|---|---|
| ● | The agent must not sign commits with the key it holds. [`authenticate-as.credential.signing`](../../model/capabilities/authenticate-as.credential.signing/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not act in accounts with the credentials it holds. [`authenticate-as.credential.tenant`](../../model/capabilities/authenticate-as.credential.tenant/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not publish packages, images or pages under the name it holds. [`create.record.world`](../../model/capabilities/create.record.world/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not delete files anywhere the account can reach. [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not read credentials stored where it runs. [`read.credential.host`](../../model/capabilities/read.credential.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not read any file the account can reach. [`read.file.host`](../../model/capabilities/read.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not read a retained record: shell history, past sessions. [`read.record.history`](../../model/capabilities/read.record.history/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not reach any host on the internet. [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ● | The agent must not change any file the account can reach. [`write.file.host`](../../model/capabilities/write.file.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ◉ | The agent must not push to a code host (any branch it can reach). [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md) | expectation | **not enforced** (a sentence, not a control) | boundary (host rule) · setting (hook) |
| ● | The agent must not create something that outlives the turn where it runs (a cron, a service). [`create.schedule.host`](../../model/capabilities/create.schedule.host/index.md) | none | **not enforced** (a sentence, not a control) | boundary |
| ◐ | The agent must not change its own permission settings. [`grant.credential.self`](../../model/capabilities/grant.credential.self/index.md) | setting | **not enforced** (a sentence, not a control) | boundary |

> **Why the barrier is on every row.** A prohibition shown without its barrier manufactures assurance. All four major model providers stated in their own 2026 words that an instruction at the prompt layer can be bypassed, and the rule underneath is older than any of them: a control bounds a grant only if it is enforced by something the grant does not include. The right hand column is where a control would have to sit, not a recommendation that you buy one.

## 6. The provenance

> **Provenance.** 0 of 22 capability rows on this page were measured, meaning seen directly on the thing itself. The other 22 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../../data/upstream/pack.json).

**No row here was obtained by probing anybody's system.** A row is measured only from a system we are entitled to run, or from the vendor's own published documentation. Causing a computer to output data intending unauthorised access is an offence with no damage requirement and no research defence.

## 7. What this is not

> **This is not an assessment.** Nothing here is an audit, a certification, a compliance assessment or a security review of any named product. It is an illustration of a method, using a published configuration, and every row carries its source, its date and whether it was measured or derived. No adjective is attached to any of it, and there is no score.

> **Validity.** This describes the deployment shape as at 11 September 2026. It is not an expiry and it does not mean stale: if the risk changed, the deployment changed, not this document.

## Follow one capability through the model

The fifth graph rule says a path should read as a sentence in the reader's own language, and it is the acceptance test for this model:

agent [`claude-code-cli-confirmations-disabled`](../../examples/claude-code-cli-confirmations-disabled/index.md) **is-granted** capability [`authenticate-as.credential.signing`](../../model/capabilities/authenticate-as.credential.signing/index.md) **bounded-by** barrier [`none`](../../model/barriers/index.md) **which-exceeds** mandate [`coding-assistant-on-my-machine`](../../model/index.md) **and-is** undo [`no`](../../model/undo/index.md).

[The four objects](../../model/index.md) · [The capability grammar](../../model/capabilities/index.md) · [The barriers](../../model/barriers/index.md) · [This shape as JSON](../../data/profiles/anthropic/claude-code/local-confirmations-off.json) · [This mandate as JSON](../../data/mandates/coding-assistant-on-my-machine.json)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/examples/claude-code-cli-confirmations-disabled/index.html)*
