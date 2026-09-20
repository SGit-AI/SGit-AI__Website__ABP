# write.repository.project

> Commit to the repository it was pointed at. Reach project, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.repository.project/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.repository.project

# `write.repository.project`

**Commit to the repository it was pointed at.** Its effect is **with-effort**: undone at a cost.

## What this id is made of

**This is not a string.** It is [`write`](../../../model/lexicon/verbs/write/index.md)`.`[`repository`](../../../model/lexicon/objects/repository/index.md)`.`[`project`](../../../model/lexicon/reaches/project/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`write`](../../../model/lexicon/verbs/write/index.md) | `has_verb` | this capability has the verb `write` |
| [`repository`](../../../model/lexicon/objects/repository/index.md) | `acts_on` | this capability acts on `repository` |
| [`project`](../../../model/lexicon/reaches/project/index.md) | `reaches` | this capability reaches `project` |
| [`code`](../../../model/lexicon/families/code/index.md) | `in_family` | this capability is in the `code` family |
| [`with-effort`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `with-effort` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `write.repository.project` is emerges from the edges traceable from it. The strongest case is [`project`](../../../model/lexicon/reaches/project/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 4 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | a repository is attached and writable |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived |  |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived |  |
| ○ | Actions runner (a hosted CI job) | boundary | observed | the checked-out tree at this ref is writable by the job |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A coding assistant on my machine, A coding assistant in a container on the web |
| **refused** | none |
| **unstated** | The desktop app, with local tools switched on, Chat, with connectors switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| none needed for most work; a review before merge is the control | a reviewer's time | setting |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/write.repository.project`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.repository.project/index.html)*
