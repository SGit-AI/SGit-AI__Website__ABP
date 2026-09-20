# send.endpoint.world

> Reach any host on the internet. Reach world, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/send.endpoint.world/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / send.endpoint.world

# `send.endpoint.world`

**Reach any host on the internet.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`send`](../../../model/lexicon/verbs/send/index.md)`.`[`network-endpoint`](../../../model/lexicon/objects/network-endpoint/index.md)`.`[`world`](../../../model/lexicon/reaches/world/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`send`](../../../model/lexicon/verbs/send/index.md) | `has_verb` | this capability has the verb `send` |
| [`network-endpoint`](../../../model/lexicon/objects/network-endpoint/index.md) | `acts_on` | this capability acts on `network-endpoint` |
| [`world`](../../../model/lexicon/reaches/world/index.md) | `reaches` | this capability reaches `world` |
| [`network`](../../../model/lexicon/families/network/index.md) | `in_family` | this capability is in the `network` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `send.endpoint.world` is emerges from the edges traceable from it. The strongest case is [`world`](../../../model/lexicon/reaches/world/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 6 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | curl reaches the world unless something above the account stops it |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | curl reaches the world unless something above the account stops it |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | derived |  |
| ● | A browser extension with broad host permissions | none (not a control) | documented | host permissions |
| ● | A scheduled job running as a service account | none (not a control) | derived |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | github.com 200, pypi.org 200, example.com 200 - UNRESTRICTED egress, no proxy |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A CI job on a hosted runner |
| **refused** | Chat in the browser, nothing connected, A browser extension I installed, A scheduled job under a service account |
| **unstated** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, Chat, with connectors switched on |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| route outbound traffic through an allow-list - the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/send.endpoint.world`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/send.endpoint.world/index.html)*
