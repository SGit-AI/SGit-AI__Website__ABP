# The capability grammar

> verb.object.reach: 23 capability primitives, each with its reach and the undo class of its effect. The action vocabulary for everything else on this site.

*Source: <https://abp.sgit.ai/model/capabilities/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The capabilities

# The capability grammar

`verb.object.reach`. **23 primitives**, 10 verbs, 9 object classes and 5 reach classes. This grammar is the action vocabulary for everything else on this site, and it was not invented here.

> **This site did not author this.** The grammar, the 23 primitives and their published glosses come from [the capability map](https://what-can-it-do.games.sgit.ai/map/index.html). Promoting an ontology means giving it an address, not a new vocabulary, so nothing here is renamed. A new primitive is a new verb, object class or reach, and it needs a probe; a specific path, host or mailbox is an **instance** of a primitive, never a new one.

## The reach classes

| Reach | What it means |
|---|---|
| `self` | the agent's own process, sandbox or turn |
| `project` | the working tree or workspace it was pointed at |
| `host` | the machine, container or account it runs as |
| `tenant` | the organisation's accounts, repositories and services |
| `world` | anything on the internet |

**What host, tenant and world mean is the deployment's to say, not the grammar's.** For an agent in a vendor's container, host is the container and tenant is a scoped token: not your machine and not your accounts. Every example page states its own reach names for this reason.

## The 23 primitives

| Primitive | Published gloss | Reach | Undo | In how many shapes |
|---|---|---|---|---|
| [`read.file.project`](../../model/capabilities/read.file.project/index.md) | Read the project it is working on | project | yes | 7 of 9 |
| [`write.file.project`](../../model/capabilities/write.file.project/index.md) | Change the project it is working on | project | with-effort | 5 of 9 |
| [`read.file.host`](../../model/capabilities/read.file.host/index.md) | Read any file the account can reach | host | no | 7 of 9 |
| [`write.file.host`](../../model/capabilities/write.file.host/index.md) | Change any file the account can reach | host | with-effort | 6 of 9 |
| [`delete.file.host`](../../model/capabilities/delete.file.host/index.md) | Delete files anywhere the account can reach | host | no | 4 of 9 |
| [`read.record.history`](../../model/capabilities/read.record.history/index.md) | Read a retained record: shell history, past sessions | host | no | 4 of 9 |
| [`execute.process.host`](../../model/capabilities/execute.process.host/index.md) | Run programs as the account | host | with-effort | 6 of 9 |
| [`execute.process.self`](../../model/capabilities/execute.process.self/index.md) | Run programs inside its own sandbox only | self | yes | 0 of 9 |
| [`send.endpoint.allowed`](../../model/capabilities/send.endpoint.allowed/index.md) | Reach a permitted list of hosts | tenant | no | 1 of 9 |
| [`send.endpoint.world`](../../model/capabilities/send.endpoint.world/index.md) | Reach any host on the internet | world | no | 6 of 9 |
| [`read.credential.host`](../../model/capabilities/read.credential.host/index.md) | Read credentials stored where it runs | host | no | 4 of 9 |
| [`authenticate-as.credential.tenant`](../../model/capabilities/authenticate-as.credential.tenant/index.md) | Act in accounts with the credentials it holds | tenant | no | 7 of 9 |
| [`grant.credential.self`](../../model/capabilities/grant.credential.self/index.md) | Change its own permission settings | self | yes | 3 of 9 |
| [`send.message.world`](../../model/capabilities/send.message.world/index.md) | Send a message to anyone | world | no | 0 of 9 |
| [`read.message.tenant`](../../model/capabilities/read.message.tenant/index.md) | Read mail or chat it is connected to | tenant | no | 1 of 9 |
| [`write.repository.project`](../../model/capabilities/write.repository.project/index.md) | Commit to the repository it was pointed at | project | with-effort | 4 of 9 |
| [`write.repository.tenant`](../../model/capabilities/write.repository.tenant/index.md) | Push to a code host (any branch it can reach) | tenant | with-effort | 4 of 9 |
| [`authenticate-as.credential.signing`](../../model/capabilities/authenticate-as.credential.signing/index.md) | Sign commits with the key it holds | tenant | no | 3 of 9 |
| [`create.record.world`](../../model/capabilities/create.record.world/index.md) | Publish packages, images or pages under the name it holds | world | no | 2 of 9 |
| [`write.budget.tenant`](../../model/capabilities/write.budget.tenant/index.md) | Spend money or tokens against an account it holds | tenant | no | 1 of 9 |
| [`create.schedule.host`](../../model/capabilities/create.schedule.host/index.md) | Create something that outlives the turn where it runs (a cron, a service) | host | yes | 4 of 9 |
| [`create.schedule.tenant`](../../model/capabilities/create.schedule.tenant/index.md) | Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | tenant | yes | 1 of 9 |
| [`read.record.browsing`](../../model/capabilities/read.record.browsing/index.md) | Read every page you visit | host | no | 1 of 9 |

## The rules that come with the set

- A specific path, host or mailbox is an instance of a primitive, never a new one.
- Reversibility sits on the primitive, not the instance, because it decides whether a gap is a nuisance or a loss - and this estate has settled that recoverability decides insurability.
- A grant containing irreversible primitives is a different object from one that does not, however many rows each has.
- The set is a starting set and will be wrong at the edges from the first week. A proposed primitive that is a specific thing is an instance; one that is a new verb, object class or reach needs a probe.
- A label never says 'your' or 'as you': what host, tenant and world mean is the profile's to say (reach_names), because for an agent in a vendor's container 'host' is the container and 'tenant' is a scoped token, not your machine and not your accounts.

[The capabilities as JSON](../../data/capabilities.json) · [The source bytes](../../data/upstream/primitives.json)

> **Provenance.** 21 of 99 capability rows on this page were measured, meaning seen directly on the thing itself. The other 78 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../../data/upstream/pack.json).

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/index.html)*
