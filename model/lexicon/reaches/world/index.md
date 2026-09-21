# world (reach)

> The reach world as a node: the 3 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/reaches/world/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / world

# `world`

anything on the internet

> **A node carries no inherent meaning.** What `world` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **3 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).

## What the shapes say `world` means, and they do not agree

> **These definitions are not merged, and that is the design.** Merging two vocabularies erases the disagreement, and the disagreement is the finding. Each row below is owned by the shape that said it. A reader deciding what `world` costs them has to read the row for the shape they run, not an average of the rows. [Why vocabularies are bridged rather than merged](https://graphs.sgit.ai/v1/depth/index.html).

| The shape | Variant | What `world` means there |
|---|---|---|
| [Claude Code on the web (a remote session container)](../../../../examples/index.md) | `ccr-container` | the hosts the proxy allows |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-confirmations-off` | the internet |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-default` | the internet |
| [Claude Desktop (a desktop app with local tools)](../../../../examples/index.md) | `default` | the internet |
| [Claude (in the browser, with connectors switched on)](../../../../examples/index.md) | `connectors-on` | the vendor's egress |
| [Claude, with the Gmail connector enabled](../../../../examples/index.md) | `default` | anyone Claude replies to or forwards a message to |
| [Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams)](../../../../examples/index.md) | `default` | anyone reachable by mail from the user's address |
| [The official Dropbox MCP server](../../../../examples/index.md) | `default` | anyone who holds a shared link or a file-request URL |
| [A browser extension with broad host permissions](../../../../examples/index.md) | `broad-host-permissions` | the internet, from your browser |
| [A scheduled job running as a service account](../../../../examples/index.md) | `service-account` | the internet, from the server |
| [Actions runner (a hosted CI job)](../../../../examples/index.md) | `ci` | the internet, unrestricted |
| [An assistant connected to a personal Google Drive with drive.readonly](../../../../examples/index.md) | `readonly-connector` | not granted by this scope |
| [An assistant connected to a personal Gmail mailbox with gmail.readonly](../../../../examples/index.md) | `readonly-connector` | not granted by this scope |
| [The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat)](../../../../examples/index.md) | `default` | anyone reachable by mail from that account |
| [A self-hosted n8n instance, reached with an owner-scoped API key](../../../../examples/index.md) | `owner-api-key` | any host an outbound node can be pointed at - accepted on creation; what the platform's own server can reach was not tested |
| [ChatGPT (in the browser, no connectors)](../../../../examples/index.md) | `default` | the vendor's egress, if browsing is on |

**That is the ABP's own argument in one column.** The same word, the same grammar, and a materially different exposure depending on where the agent runs. It is why an ABP is about the deployment rather than the product.



## The 3 primitives with this reach

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`create.record.world`](../../../../model/capabilities/create.record.world/index.md) | Publish packages, images or pages under the name it holds | [`create`](../../../../model/lexicon/verbs/create/index.md)`.`[`record`](../../../../model/lexicon/objects/record/index.md)`.`[`world`](../../../../model/lexicon/reaches/world/index.md) | no | 3 of 16 |
| [`send.endpoint.world`](../../../../model/capabilities/send.endpoint.world/index.md) | Reach any host on the internet | [`send`](../../../../model/lexicon/verbs/send/index.md)`.`[`network-endpoint`](../../../../model/lexicon/objects/network-endpoint/index.md)`.`[`world`](../../../../model/lexicon/reaches/world/index.md) | no | 7 of 16 |
| [`send.message.world`](../../../../model/capabilities/send.message.world/index.md) | Send a message to anyone | [`send`](../../../../model/lexicon/verbs/send/index.md)`.`[`message`](../../../../model/lexicon/objects/message/index.md)`.`[`world`](../../../../model/lexicon/reaches/world/index.md) | no | 3 of 16 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `reachable_from` | `world` is the reach of these 3 primitives | 3 capabilities |
| `reaches` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/reaches/world.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/reaches/world/index.html)*
