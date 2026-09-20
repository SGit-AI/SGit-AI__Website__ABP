# write.budget.tenant

> Spend money or tokens against an account it holds. Reach tenant, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.budget.tenant/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.budget.tenant

# `write.budget.tenant`

**Spend money or tokens against an account it holds.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`write`](../../../model/lexicon/verbs/write/index.md)`.`[`budget`](../../../model/lexicon/objects/budget/index.md)`.`[`tenant`](../../../model/lexicon/reaches/tenant/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`write`](../../../model/lexicon/verbs/write/index.md) | `has_verb` | this capability has the verb `write` |
| [`budget`](../../../model/lexicon/objects/budget/index.md) | `acts_on` | this capability acts on `budget` |
| [`tenant`](../../../model/lexicon/reaches/tenant/index.md) | `reaches` | this capability reaches `tenant` |
| [`money`](../../../model/lexicon/families/money/index.md) | `in_family` | this capability is in the `money` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `write.budget.tenant` is emerges from the edges traceable from it. The strongest case is [`tenant`](../../../model/lexicon/reaches/tenant/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 1 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | A scheduled job running as a service account | none (not a control) | derived | if the credential is billed |

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
| **refused** | Chat in the browser, nothing connected, A scheduled job under a service account |
| **unstated** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, Chat, with connectors switched on, A CI job on a hosted runner, A browser extension I installed |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a spend cap at the supplier, set by somebody other than the agent - the supplier has a reason to refuse: it is paying | the work stops when the cap is reached, which is the point | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.budget.tenant/index.html)*
