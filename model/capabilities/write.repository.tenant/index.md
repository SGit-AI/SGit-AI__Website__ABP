# write.repository.tenant

> Push to a code host (any branch it can reach). Reach tenant, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.repository.tenant/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.repository.tenant

# `write.repository.tenant`

**Push to a code host (any branch it can reach).** Verb `write`, object `repository`, reach `tenant`, family `code`. Its effect is **with-effort**: undone at a cost.

## In 4 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ◐ | Claude Code on the web (a remote session container) | setting (not a control) | observed | the attached repository only (any branch it can reach); branch discipline is the clone's hooks, a setting; no rule at the host |
| ◉ | Claude Code (the CLI, on your own machine) | expectation (not a control) | derived |  |
| ◉ | Claude Code (the CLI, on your own machine) | expectation (not a control) | derived |  |
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | a code-host connector |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A coding assistant in a container on the web, A CI job on a hosted runner |
| **refused** | Chat, with connectors switched on, Chat in the browser, nothing connected |
| **unstated** | A coding assistant on my machine, The desktop app, with local tools switched on, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a branch protection rule at the host - the agent cannot edit it - and a pre-push hook in the clone for the earlier, cheaper refusal | minutes; and a review step before anything deploys | boundary (host rule) · setting (hook) |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.repository.tenant/index.html)*
