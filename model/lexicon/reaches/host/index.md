# host (reach)

> The reach host as a node: the 8 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/reaches/host/index.html> · site v0.9.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / host

# `host`

the machine, container or account it runs as

> **A node carries no inherent meaning.** What `host` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **8 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).

## What the shapes say `host` means, and they do not agree

> **These definitions are not merged, and that is the design.** Merging two vocabularies erases the disagreement, and the disagreement is the finding. Each row below is owned by the shape that said it. A reader deciding what `host` costs them has to read the row for the shape they run, not an average of the rows. [Why vocabularies are bridged rather than merged](https://graphs.sgit.ai/v1/depth/index.html).

| The shape | Variant | What `host` means there |
|---|---|---|
| [Claude Code on the web (a remote session container)](../../../../examples/index.md) | `ccr-container` | this container - ephemeral, the vendor's; not your machine |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-confirmations-off` | your machine, as your user account |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-default` | your machine, as your user account |
| [Claude Desktop (a desktop app with local tools)](../../../../examples/index.md) | `default` | your machine, as your user account |
| [Claude (in the browser, with connectors switched on)](../../../../examples/index.md) | `connectors-on` | what the drive connector is scoped to; not your machine |
| [Claude, with the Gmail connector enabled](../../../../examples/index.md) | `default` | the mailbox itself: every message and thread, labels, filters and saved drafts, and attachment metadata - never attachment content |
| [Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams)](../../../../examples/index.md) | `default` | SharePoint sites and OneDrive files the user can already open - searched tenant-wide |
| [The official Dropbox MCP server](../../../../examples/index.md) | `default` | the Dropbox account as a store - and for a team user, "the usage and quota for the entire team" |
| [A browser extension with broad host permissions](../../../../examples/index.md) | `broad-host-permissions` | your browser - every page, every logged-in site |
| [A scheduled job running as a service account](../../../../examples/index.md) | `service-account` | the server it runs on, as the service account |
| [Actions runner (a hosted CI job)](../../../../examples/index.md) | `ci` | the runner - destroyed after the job; not your machine |
| [An assistant connected to a personal Google Drive with drive.readonly](../../../../examples/index.md) | `readonly-connector` | the Drive as a store: every file owned by or shared to the user |
| [An assistant connected to a personal Gmail mailbox with gmail.readonly](../../../../examples/index.md) | `readonly-connector` | the mailbox itself, as a store: every message and the account's mail settings |
| [The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat)](../../../../examples/index.md) | `default` | the Google account's Drive and mailbox - every file owned by or shared to the user; not your machine |
| [A self-hosted n8n instance, reached with an owner-scoped API key](../../../../examples/index.md) | `owner-api-key` | the instance itself: its accounts, its credential store, its execution records |
| [ChatGPT (in the browser, no connectors)](../../../../examples/index.md) | `default` | the vendor's environment; not your machine |

**That is the ABP's own argument in one column.** The same word, the same grammar, and a materially different exposure depending on where the agent runs. It is why an ABP is about the deployment rather than the product.



## The 8 primitives with this reach

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`create.schedule.host`](../../../../model/capabilities/create.schedule.host/index.md) | Create something that outlives the turn where it runs (a cron, a service) | [`create`](../../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../../model/lexicon/objects/schedule/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | yes | 4 of 16 |
| [`delete.file.host`](../../../../model/capabilities/delete.file.host/index.md) | Delete files anywhere the account can reach | [`delete`](../../../../model/lexicon/verbs/delete/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 5 of 16 |
| [`execute.process.host`](../../../../model/capabilities/execute.process.host/index.md) | Run programs as the account | [`execute`](../../../../model/lexicon/verbs/execute/index.md)`.`[`process`](../../../../model/lexicon/objects/process/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | with-effort | 7 of 16 |
| [`read.credential.host`](../../../../model/capabilities/read.credential.host/index.md) | Read credentials stored where it runs | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 10 of 16 |
| [`read.file.host`](../../../../model/capabilities/read.file.host/index.md) | Read any file the account can reach | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 11 of 16 |
| [`read.record.browsing`](../../../../model/capabilities/read.record.browsing/index.md) | Read every page you visit | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`record`](../../../../model/lexicon/objects/record/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 1 of 16 |
| [`read.record.history`](../../../../model/capabilities/read.record.history/index.md) | Read a retained record: shell history, past sessions | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`record`](../../../../model/lexicon/objects/record/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 7 of 16 |
| [`write.file.host`](../../../../model/capabilities/write.file.host/index.md) | Change any file the account can reach | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | with-effort | 8 of 16 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `reachable_from` | `host` is the reach of these 8 primitives | 8 capabilities |
| `reaches` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/reaches/host.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/reaches/host/index.html)*
