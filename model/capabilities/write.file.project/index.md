# write.file.project

> Change the project it is working on. Reach project, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.file.project/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.file.project

# `write.file.project`

**Change the project it is working on.** Verb `write`, object `file`, reach `project`, family `filesystem`. Its effect is **with-effort**: undone at a cost.

## In 5 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | the attached working tree is writable |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived |  |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived |  |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | derived |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | the checked-out tree at this ref is writable by the job |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner |
| **refused** | none |
| **unstated** | Chat, with connectors switched on, Chat in the browser, nothing connected, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a review before merge | a reviewer's time | setting |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.file.project/index.html)*
