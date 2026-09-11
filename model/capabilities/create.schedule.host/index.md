# create.schedule.host

> Create something that outlives the turn where it runs (a cron, a service). Reach host, undo yes. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/create.schedule.host/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / create.schedule.host

# `create.schedule.host`

**Create something that outlives the turn where it runs (a cron, a service).** Verb `create`, object `schedule`, reach `host`, family `schedule`. Its effect is **yes**: undone.

## In 4 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ○ | Claude Code on the web (a remote session container) | boundary | observed | systemctl and /etc/cron.d exist, so a cron can be written - and dies with the container; the real scheduler is the platform's routines, on the harness row |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | a shell as you can write a crontab |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | a shell as you can write a crontab |
| ● | A scheduled job running as a service account | none (not a control) | derived | it is one |

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
| **refused** | A coding assistant on my machine |
| **unstated** | A coding assistant in a container on the web, The desktop app, with local tools switched on, Chat, with connectors switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| no scheduler in the agent's environment; anything that outlives the turn goes through a person | you create the routine | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/create.schedule.host/index.html)*
