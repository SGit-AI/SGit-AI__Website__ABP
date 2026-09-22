# write.file.project

> Change the project it is working on. Reach project, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.file.project/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.file.project

# `write.file.project`

**Change the project it is working on.** Its effect is **with-effort**: undone at a cost.

## What this id is made of

**This is not a string.** It is [`write`](../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../model/lexicon/objects/file/index.md)`.`[`project`](../../../model/lexicon/reaches/project/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`write`](../../../model/lexicon/verbs/write/index.md) | `has_verb` | this capability has the verb `write` |
| [`file`](../../../model/lexicon/objects/file/index.md) | `acts_on` | this capability acts on `file` |
| [`project`](../../../model/lexicon/reaches/project/index.md) | `reaches` | this capability reaches `project` |
| [`filesystem`](../../../model/lexicon/families/filesystem/index.md) | `in_family` | this capability is in the `filesystem` family |
| [`with-effort`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `with-effort` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `write.file.project` is emerges from the edges traceable from it. The strongest case is [`project`](../../../model/lexicon/reaches/project/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 6 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | the attached working tree is writable |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated |  |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated |  |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | derived | not stated |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | not stated | the checked-out tree at this ref is writable by the job |
| ● | A self-hosted n8n instance, reached with an owner-scoped API key *(contributed by riskmandate.ai)* | none (not a control) | measured | organisation | full create-change-delete confirmed: created, deactivated and deleted one real test workflow in the session. The write-up records the API key as "the technical gate - broad, but a real gate, not a prose rule"; in this vocabulary a key that permits a thing is the grant, not a barrier, so the row stands at none. |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A sandbox: build and run one AI-agent workflow |
| **refused** | none |
| **unstated** | Chat, with connectors switched on, Chat in the browser, nothing connected, A browser extension I installed, A scheduled job under a service account, A reader on my mailbox, Find things in the inbox, draft replies, never send, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a review before merge | a reviewer's time | setting |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/write.file.project`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.file.project/index.html)*
