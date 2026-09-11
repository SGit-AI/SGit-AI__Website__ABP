# read.message.tenant

> Read mail or chat it is connected to. Reach tenant, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.message.tenant/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.message.tenant

# `read.message.tenant`

**Read mail or chat it is connected to.** Verb `read`, object `message`, reach `tenant`, family `communication`. Its effect is **no**: cannot be undone.

## In 1 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | a mail or chat connector reads your mail |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | Chat, with connectors switched on |
| **refused** | Chat in the browser, nothing connected |
| **unstated** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a connector scoped to one folder or label, or none | the agent answers about less | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.message.tenant/index.html)*
