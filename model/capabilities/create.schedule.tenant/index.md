# create.schedule.tenant

> Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session). Reach tenant, undo yes. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/create.schedule.tenant/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / create.schedule.tenant

# `create.schedule.tenant`

**Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session).** Its effect is **yes**: undone.

## What this id is made of

**This is not a string.** It is [`create`](../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../model/lexicon/objects/schedule/index.md)`.`[`tenant`](../../../model/lexicon/reaches/tenant/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`create`](../../../model/lexicon/verbs/create/index.md) | `has_verb` | this capability has the verb `create` |
| [`schedule`](../../../model/lexicon/objects/schedule/index.md) | `acts_on` | this capability acts on `schedule` |
| [`tenant`](../../../model/lexicon/reaches/tenant/index.md) | `reaches` | this capability reaches `tenant` |
| [`schedule`](../../../model/lexicon/families/schedule/index.md) | `in_family` | this capability is in the `schedule` family |
| [`yes`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `yes` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `create.schedule.tenant` is emerges from the edges traceable from it. The strongest case is [`tenant`](../../../model/lexicon/reaches/tenant/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 1 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ◐ | Claude Code on the web (a remote session container) | setting (not a control) | self-reported | a routine or a scheduled trigger resumes this session or spawns another later: it outlives the container |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | none |
| **refused** | A coding assistant in a container on the web, Chat in the browser, nothing connected |
| **unstated** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat, with connectors switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/create.schedule.tenant/index.html)*
