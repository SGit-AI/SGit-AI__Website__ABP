# send.message.world

> Send a message to anyone. Reach world, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/send.message.world/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / send.message.world

# `send.message.world`

**Send a message to anyone.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`send`](../../../model/lexicon/verbs/send/index.md)`.`[`message`](../../../model/lexicon/objects/message/index.md)`.`[`world`](../../../model/lexicon/reaches/world/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`send`](../../../model/lexicon/verbs/send/index.md) | `has_verb` | this capability has the verb `send` |
| [`message`](../../../model/lexicon/objects/message/index.md) | `acts_on` | this capability acts on `message` |
| [`world`](../../../model/lexicon/reaches/world/index.md) | `reaches` | this capability reaches `world` |
| [`communication`](../../../model/lexicon/families/communication/index.md) | `in_family` | this capability is in the `communication` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `send.message.world` is emerges from the edges traceable from it. The strongest case is [`world`](../../../model/lexicon/reaches/world/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 0 of 9 published shapes

No published shape in this set has it.

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
| **refused** | A coding assistant on my machine, Chat, with connectors switched on, Chat in the browser, nothing connected |
| **unstated** | A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| no mail or chat connector, or a connector that drafts and never sends | you press send | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/send.message.world/index.html)*
