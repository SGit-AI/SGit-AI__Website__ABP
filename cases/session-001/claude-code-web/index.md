# Case session-001: Claude Code on the web, one repository attached: the session that built v0.4.0 to v0.8.1

> The elicited mandate, the clauses and the discovery prompt for Claude Code on the web, one repository attached: the session that built v0.4.0 to v0.8.1, against the published shape this deployment is.

*Source: <https://abp.sgit.ai/cases/session-001/claude-code-web/index.html> · site v0.9.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Cases](../../../cases/index.md) / [session-001](../../../cases/session-001/index.md) / the session

# Claude Code on the web, one repository attached: the session that built v0.4.0 to v0.8.1

**Consent: the harness's permission mode, with a classifier that blocked five commands.** The mandate below was elicited, not authored: 6 lines the deployer said, 2 inferred from something they said, and 15 of the 23 primitives never raised. The grant is the published shape, measured.

> **Where the numbers on this page came from.** The repository's history and the code host's workflow log, read by the agent that ran the session on 22 September 2026. Every ledger line says which of those it came from, or that it is an estimate, or that the agent cannot see it. **The grant is measured**: the deployment is the published shape this site is maintained from, 13 of 20 rows seen on the container itself. The mandate is elicited from the deployer's messages and the harness's rules and has not been corrected by the deployer. No accountant has read the ledger.

## The mandate, line by line

| Capability | Side | How we know | From what |
|---|---|---|---|
| [`read.file.project`](../../../model/capabilities/read.file.project/index.md) Read the project it is working on | **wanted** | **said** | "start by reviewing the content on this site" |
| [`write.file.project`](../../../model/capabilities/write.file.project/index.md) Change the project it is working on | **wanted** | **said** | "build those two next versions" |
| [`write.repository.project`](../../../model/capabilities/write.repository.project/index.md) Commit to the repository it was pointed at | **wanted** | **said** | "commit your work", the harness's branch rules |
| [`write.repository.tenant`](../../../model/capabilities/write.repository.tenant/index.md) Push to a code host (any branch it can reach) | **wanted** | **said** | "push to dev what you have done, which should trigger the CI pipeline" |
| [`send.endpoint.allowed`](../../../model/capabilities/send.endpoint.allowed/index.md) Reach a permitted list of hosts | **wanted** | **said** | "read the guidance at sgit.ai/llms.txt", "read in detail the content at RiskMandate.ai" |
| [`execute.process.host`](../../../model/capabilities/execute.process.host/index.md) Run programs as the account | **wanted** | **inferred** | building and validating the site is running programs in the container; nobody said so and every release needed it |
| [`read.record.history`](../../../model/capabilities/read.record.history/index.md) Read a retained record: shell history, past sessions | **wanted** | **said** | the harness pointed at the session's own transcript for details lost to context compaction |
| [`create.schedule.tenant`](../../../model/capabilities/create.schedule.tenant/index.md) Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | **refused** | **inferred** | no routine, wakeup or new session was asked for, and the harness rule says not to poll |

**Unstated, 15 primitives:** `read.file.host`, `write.file.host`, `delete.file.host`, `execute.process.self`, `send.endpoint.world`, `read.credential.host`, `authenticate-as.credential.tenant`, `grant.credential.self`, `send.message.world`, `read.message.tenant`, `authenticate-as.credential.signing`, `create.record.world`, `write.budget.tenant`, `create.schedule.host`, `read.record.browsing`.

Unstated is not authorised, and it is not refused either. It is the list the deployer corrects, and the correction is the mandate.

### What the grammar has no word for

|  | Note |
|---|---|
| **how much** | every clause that actually governed this session was over a count, not a capability: how many commits, whether to spawn subagents, where scratch files go. None of them is a row in this table, which is the finding the cost walkthrough predicted |

- commit only when asked, which is a rule over when rather than over whether
- no subagents unless asked, which is a rule over delegation
- scratch files in the scratchpad, which is a rule over where
- one article per release, which is a rule over what must accompany a push
- do not poll in a loop, which is a rule over how often

The grammar was promoted from a capability map drawn for coding agents and browsers. Everything above carries in the clauses instead, which is where the rules that cannot be expressed as a permission were always going to live.

## The published shape, and the delta

**The shape this site is maintained from, measured by the thing being profiled: 13 of 20 rows seen on the container itself. For once the nearest shape is the deployment.**

> **This is the deployment's own delta on the grant side and a draft on the mandate side.** The shape was measured by the thing being profiled; the mandate is elicited and not yet corrected.

| Field | Against the published shape |
|---|---|
| Shape | Claude Code on the web (a remote session container) |
| Grant | 15 of 23 primitives, 13 of 20 rows measured |
| Mandate | 7 primitives wanted |
| Excess | 8 |
| Unbounded excess | 6 |
| Shortfall | none |

|  | Capability | Undo | Barrier | Known by | The mandate |
|---|---|---|---|---|---|
| ● | [`authenticate-as.credential.signing`](../../../model/capabilities/authenticate-as.credential.signing/index.md) Sign commits with the key it holds | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`delete.file.host`](../../../model/capabilities/delete.file.host/index.md) Delete files anywhere the account can reach | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`read.credential.host`](../../../model/capabilities/read.credential.host/index.md) Read credentials stored where it runs | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`read.file.host`](../../../model/capabilities/read.file.host/index.md) Read any file the account can reach | no | none (not a control) | observed | **excess** (unstated) |
| ● | [`read.record.history`](../../../model/capabilities/read.record.history/index.md) Read a retained record: shell history, past sessions | no | none (not a control) | observed | **authorised** |
| ○ | [`authenticate-as.credential.tenant`](../../../model/capabilities/authenticate-as.credential.tenant/index.md) Act in accounts with the credentials it holds | no | boundary | inferred | **excess** (unstated) |
| ○ | [`send.endpoint.allowed`](../../../model/capabilities/send.endpoint.allowed/index.md) Reach a permitted list of hosts | no | boundary | observed | **authorised** |
| ● | [`execute.process.host`](../../../model/capabilities/execute.process.host/index.md) Run programs as the account | with-effort | none (not a control) | observed | **authorised** |
| ● | [`write.file.host`](../../../model/capabilities/write.file.host/index.md) Change any file the account can reach | with-effort | none (not a control) | observed | **excess** (unstated) |
| ● | [`write.file.project`](../../../model/capabilities/write.file.project/index.md) Change the project it is working on | with-effort | none (not a control) | observed | **authorised** |
| ● | [`write.repository.project`](../../../model/capabilities/write.repository.project/index.md) Commit to the repository it was pointed at | with-effort | none (not a control) | observed | **authorised** |
| ◐ | [`write.repository.tenant`](../../../model/capabilities/write.repository.tenant/index.md) Push to a code host (any branch it can reach) | with-effort | setting (not a control) | observed | **authorised** |
| ● | [`read.file.project`](../../../model/capabilities/read.file.project/index.md) Read the project it is working on | yes | none (not a control) | observed | **authorised** |
| ◐ | [`create.schedule.tenant`](../../../model/capabilities/create.schedule.tenant/index.md) Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | yes | setting (not a control) | self-reported | **excess** (refused) |
| ○ | [`create.schedule.host`](../../../model/capabilities/create.schedule.host/index.md) Create something that outlives the turn where it runs (a cron, a service) | yes | boundary | observed | **excess** (unstated) |

[The shape's own page](../../../examples/index.md) &#183; [the delta as JSON](../../../data/cases/session-001/deltas/claude-code-web.json)

## The clauses, drafted for the deployer to correct

In their voice, as instructions to the assistant, carrying everything the grammar has no word for. **This is the second barrier kind**: a rule written down. It bounds nothing and it moves where responsibility lands, which is [step four of the walkthrough](../../../gmail/what-a-prompt-cannot-do/index.md).

**The clauses: Rules for this repository.** Paste at the top of any conversation where the assistant has this. Edit first: the lines you change are the ones that were actually yours.

```
Rules for the session that maintains this site. You run in a container with this repository
attached and you can push to the release branch, which deploys.

  LIMITS PER TURN
    - one commit per release and one push per release; never push to deploy twice within
      a few minutes, because the second run cancels the first
    - tell me the count before any turn that will change more than the build regenerates

  RESEARCH
    - read the repository and the transcript before you fetch anything
    - never poll the code host or the live site in a loop; one check after a wait, or
      wait for the notification

  DELEGATION
    - no subagents and no workflows unless I ask

  OTHER PEOPLE
    - never open a pull request, assign anything or notify anyone unless I ask
    - stop and ask when a push would publish something from a private source

  ALWAYS
    - scratch files go in the scratchpad and never in the tree
    - one article per release, with its screenshots from that release's tag
    - end every release with a ledger: commits, pushes, pipeline runs, files by hand, files
      generated, fetches, questions asked of me, and what you could not count
```

## The discovery prompt, for this deployment

The grant is measured, and this is what checks it against today's build.

**Prompt B: What you can do with this repository.** One table, hardest thing to undo at the top, every line marked read or inferred.

```
Before the next release, produce the ledger for this session so far, in the form on the
cost walkthrough: files written by hand, files generated, commits, pushes, pipeline runs
started, fetches, subagents, questions you asked me, things you handed me to read, and
tokens or "cannot see". Count from git and from the code host's workflow log wherever you
can, and mark every other line as an estimate. Then list every clause in force in this
session and say whether it was kept.
```

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one. A case describes one person's deployments in their own words and against published shapes with their sources and dates.

[The mandate as JSON](../../../data/cases/session-001/mandates/claude-code-web.json) &#183; [The estate](../../../cases/session-001/index.md) &#183; [The walkthrough](../../../gmail/index.md)

|  |  |
|---|---|
| **The estate** | [The session that built this site's last twelve releases, as a ledger](../../../cases/session-001/index.md) |

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/cases/session-001/claude-code-web/index.html)*
