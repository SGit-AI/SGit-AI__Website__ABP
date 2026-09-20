# read.record.history

> Read a retained record: shell history, past sessions. Reach host, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.record.history/index.html> · site v0.4.4 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.record.history

# `read.record.history`

**Read a retained record: shell history, past sessions.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`read`](../../../model/lexicon/verbs/read/index.md)`.`[`record`](../../../model/lexicon/objects/record/index.md)`.`[`host`](../../../model/lexicon/reaches/host/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`read`](../../../model/lexicon/verbs/read/index.md) | `has_verb` | this capability has the verb `read` |
| [`record`](../../../model/lexicon/objects/record/index.md) | `acts_on` | this capability acts on `record` |
| [`host`](../../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
| [`filesystem`](../../../model/lexicon/families/filesystem/index.md) | `in_family` | this capability is in the `filesystem` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `read.record.history` is emerges from the edges traceable from it. The strongest case is [`host`](../../../model/lexicon/reaches/host/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 7 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | the harness's project directory holds this session's own earlier tool outputs; no user shell history exists here |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | not stated | shell history and the harness's own transcripts |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | not stated | shell history and the harness's own transcripts |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | documented | not stated |  |
| ● | Claude, with the Gmail connector enabled *(contributed by riskmandate.ai)* | none (not a control) | measured | mixed | a mailbox is a retained record of years, and the consent line is "View your email messages and settings." Measured 2026-09-16: asked for the account's settings, Claude returned the label structure with thread and unread counts for every system and custom label (an inventory of the mailbox's shape), and said it had no tool for forwarding rules, filters, the vacation responder or signatures. Nothing separates this from reading messages, so the barrier is the same as the row above: none beyond the consent itself. |
| ● | An assistant connected to a personal Gmail mailbox with gmail.readonly *(contributed by riskmandate.ai)* | none (not a control) | inferred | mixed | a mailbox is a retained record of years: "settings" in the scope text includes filters and forwarding addresses. Whether the assistant reads settings is open, below. |
| ● | A self-hosted n8n instance, reached with an owner-scoped API key *(contributed by riskmandate.ai)* | none (not a control) | measured | organisation | execution records read: the zero-execution baseline, then the one real execution with its status and the model's response. |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A sandbox: build and run one AI-agent workflow |
| **refused** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, Chat in the browser, nothing connected |
| **unstated** | Chat, with connectors switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my mailbox, Find things in the inbox, draft replies, never send, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| history off, or a fresh environment per task, so the grant is a tree over the present rather than a union over every prior turn | the agent forgets between tasks | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/read.record.history`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.record.history/index.html)*
