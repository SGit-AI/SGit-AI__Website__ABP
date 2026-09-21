# send.message.world

> Send a message to anyone. Reach world, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/send.message.world/index.html> · site v0.6.0 · this file is generated from the same content
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

## In 3 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ◐ | Claude, with the Gmail connector enabled *(contributed by riskmandate.ai)* | setting (not a control) | measured | third_party | Anthropic: "Send, reply to, and forward emails from Gmail." and "During authentication, Google's OAuth screen mentions email sending permissions... Claude can send, reply to, and forward emails, but only does so with your explicit approval by default." The directory listing names reply and forward; Google's own reference for the same server (2026-07-21) names no tool that sends - see contradictions. The credential is the grant; the approval prompt is the barrier, and by the enforcer test it is a setting - the grant includes the ability to remove it. Measured 2026-09-16: one message sent to an address the deployer named for the purpose, after "Allow once"; Claude confirmed the send and the sending address. The message as sent carries no header naming the client: no X-Mailer, no User-Agent; the Received line says "by gmailapi.google.com with HTTPREST" from a numeric sender that is the OAuth client's Google Cloud project number, and the body is signed with the account holder's name. To the recipient it is the account holder's mail (evidence/09). |
| ○ | Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams) *(contributed by riskmandate.ai)* | boundary | documented | third_party | outlook_send_mail - "Send an email as the user." To any address. Listed under Write tools on the same page whose read section says the connector "provides read-only access to" its sources. |
| ○ | The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat) *(contributed by riskmandate.ai)* | boundary | documented | third_party | gmail.compose - "Manage drafts and send emails." The setup page advertises "create draft emails"; the scope it asks for also sends. Whether the server exposes a tool that sends is open, below. |

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
| **refused** | A coding assistant on my machine, Chat, with connectors switched on, Chat in the browser, nothing connected, A reader on my mailbox, Find things in the inbox, draft replies, never send, Search our tenant, read-only, An assistant over my Workspace, reading |
| **unstated** | A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my drive, Find and read my files, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| no mail or chat connector, or a connector that drafts and never sends | you press send | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/send.message.world`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/send.message.world/index.html)*
