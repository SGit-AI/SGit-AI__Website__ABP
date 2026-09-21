# read.message.tenant

> Read mail or chat it is connected to. Reach tenant, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.message.tenant/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.message.tenant

# `read.message.tenant`

**Read mail or chat it is connected to.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`read`](../../../model/lexicon/verbs/read/index.md)`.`[`message`](../../../model/lexicon/objects/message/index.md)`.`[`tenant`](../../../model/lexicon/reaches/tenant/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`read`](../../../model/lexicon/verbs/read/index.md) | `has_verb` | this capability has the verb `read` |
| [`message`](../../../model/lexicon/objects/message/index.md) | `acts_on` | this capability acts on `message` |
| [`tenant`](../../../model/lexicon/reaches/tenant/index.md) | `reaches` | this capability reaches `tenant` |
| [`communication`](../../../model/lexicon/families/communication/index.md) | `in_family` | this capability is in the `communication` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `read.message.tenant` is emerges from the edges traceable from it. The strongest case is [`tenant`](../../../model/lexicon/reaches/tenant/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 5 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | not stated | a mail or chat connector reads your mail |
| ○ | Claude, with the Gmail connector enabled *(contributed by riskmandate.ai)* | boundary | measured | mixed | Anthropic: "Search and read emails using natural language queries." "Access email metadata, including attachment metadata (not attachment content)." Google's reference: "Read data: Search emails, retrieve threads, and list labels." Read carries no per-action approval prompt on Anthropic's page; the prompt sentence sits under send, reply and forward. Measured 2026-09-16: asked to read the inbox and name the top messages, Claude returned ten threads with sender, subject and date, after "Loaded tools, used Gmail integration". |
| ○ | Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams) *(contributed by riskmandate.ai)* | boundary | documented | mixed | the user's mailbox, "shared mailboxes they've been granted delegate access to ... including full access and folder-level delegation", and Teams chats. Shared-mailbox access is stated as read-only via Mail.Read.Shared. |
| ○ | An assistant connected to a personal Gmail mailbox with gmail.readonly *(contributed by riskmandate.ai)* | boundary | documented | mixed | gmail.readonly - "View your email messages and settings." The only scope that excludes bodies, gmail.metadata, "cannot read a message". There is no scope that filters by sender, label or date. |
| ○ | The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat) *(contributed by riskmandate.ai)* | boundary | documented | mixed | gmail.readonly - "View your email messages and settings." Every message and the settings. No Gmail scope filters by sender, label or date; the only narrower one, gmail.metadata, cannot return a body. |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | Chat, with connectors switched on, A reader on my mailbox, Find things in the inbox, draft replies, never send, Search our tenant, read-only, An assistant over my Workspace, reading |
| **refused** | Chat in the browser, nothing connected |
| **unstated** | A coding assistant on my machine, A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my drive, Find and read my files, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a connector scoped to one folder or label, or none | the agent answers about less | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/read.message.tenant`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.message.tenant/index.html)*
