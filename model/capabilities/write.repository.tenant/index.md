# write.repository.tenant

> Push to a code host (any branch it can reach). Reach tenant, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.repository.tenant/index.html> · site v0.4.2 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.repository.tenant

# `write.repository.tenant`

**Push to a code host (any branch it can reach).** Its effect is **with-effort**: undone at a cost.

## What this id is made of

**This is not a string.** It is [`write`](../../../model/lexicon/verbs/write/index.md)`.`[`repository`](../../../model/lexicon/objects/repository/index.md)`.`[`tenant`](../../../model/lexicon/reaches/tenant/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`write`](../../../model/lexicon/verbs/write/index.md) | `has_verb` | this capability has the verb `write` |
| [`repository`](../../../model/lexicon/objects/repository/index.md) | `acts_on` | this capability acts on `repository` |
| [`tenant`](../../../model/lexicon/reaches/tenant/index.md) | `reaches` | this capability reaches `tenant` |
| [`code`](../../../model/lexicon/families/code/index.md) | `in_family` | this capability is in the `code` family |
| [`with-effort`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `with-effort` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `write.repository.tenant` is emerges from the edges traceable from it. The strongest case is [`tenant`](../../../model/lexicon/reaches/tenant/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

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
