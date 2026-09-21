# read.file.host

> Read any file the account can reach. Reach host, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.file.host/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.file.host

# `read.file.host`

**Read any file the account can reach.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`read`](../../../model/lexicon/verbs/read/index.md)`.`[`file`](../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../model/lexicon/reaches/host/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`read`](../../../model/lexicon/verbs/read/index.md) | `has_verb` | this capability has the verb `read` |
| [`file`](../../../model/lexicon/objects/file/index.md) | `acts_on` | this capability acts on `file` |
| [`host`](../../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
| [`filesystem`](../../../model/lexicon/families/filesystem/index.md) | `in_family` | this capability is in the `filesystem` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `read.file.host` is emerges from the edges traceable from it. The strongest case is [`host`](../../../model/lexicon/reaches/host/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 11 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | any file in the container - the attached clone, the harness's state, the system. Not your machine's files (the assess tree's 'home: boundary') |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated | everything your account can read, because a shell as you reads as you |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated | everything your account can read, because a shell as you reads as you |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived | not stated |  |
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | not stated | a drive connector: your other files, as scoped |
| ○ | Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams) *(contributed by riskmandate.ai)* | boundary | documented | mixed | "SharePoint search requires Sites.Read.All permission. Site-specific permissioning (using *.Selected permissions) is not supported because the underlying search is tenant-wide." Everything the user can already open, across the tenant. |
| ○ | The official Dropbox MCP server *(contributed by riskmandate.ai)* | boundary | documented | mixed | "Extract text from PDFs, Word documents, and other text representable files"; "Search files and folders by name or content". Everything the account can open, team folders included. |
| ● | A scheduled job running as a service account | none (not a control) | derived | not stated |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | not stated | the runner's user with passwordless escalation: every file on the ephemeral machine |
| ○ | An assistant connected to a personal Google Drive with drive.readonly *(contributed by riskmandate.ai)* | boundary | documented | mixed | drive.readonly - "View and download all your Drive files." The default corpus of a listing is "files owned by or shared to the user"; whether shared drives are included is open, below. |
| ○ | The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat) *(contributed by riskmandate.ai)* | boundary | documented | mixed | drive.readonly - "View and download all your Drive files." A Drive listing's default corpus is "files owned by or shared to the user": everything any colleague, client or counterparty ever shared. |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | Chat, with connectors switched on, A scheduled job under a service account, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading |
| **refused** | A coding assistant on my machine, Chat in the browser, nothing connected |
| **unstated** | A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed, A reader on my mailbox, Find things in the inbox, draft replies, never send, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/read.file.host`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.file.host/index.html)*
