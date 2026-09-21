# write.file.host

> Change any file the account can reach. Reach host, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/write.file.host/index.html> · site v0.5.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / write.file.host

# `write.file.host`

**Change any file the account can reach.** Its effect is **with-effort**: undone at a cost.

## What this id is made of

**This is not a string.** It is [`write`](../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../model/lexicon/reaches/host/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`write`](../../../model/lexicon/verbs/write/index.md) | `has_verb` | this capability has the verb `write` |
| [`file`](../../../model/lexicon/objects/file/index.md) | `acts_on` | this capability acts on `file` |
| [`host`](../../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
| [`filesystem`](../../../model/lexicon/families/filesystem/index.md) | `in_family` | this capability is in the `filesystem` family |
| [`with-effort`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `with-effort` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `write.file.host` is emerges from the edges traceable from it. The strongest case is [`host`](../../../model/lexicon/reaches/host/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 8 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | a zero-byte file was created and removed in /etc: system configuration of the container is writable |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated |  |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated |  |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived | not stated |  |
| ○ | The official Dropbox MCP server *(contributed by riskmandate.ai)* | boundary | documented | mixed | Copy "can recreate a deleted file or replace an existing file at the destination path"; Move renames or moves files and folders; CreateFile writes up to 5 MB of inline content. |
| ● | A scheduled job running as a service account | none (not a control) | derived | not stated |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | not stated | the runner's user with passwordless escalation: every file on the ephemeral machine |
| ○ | The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat) *(contributed by riskmandate.ai)* | boundary | documented | mixed | drive.file creates new files or modifies files the user opened with the app; the Docs, Sheets and Slides servers each ask for the full write scope for their document type beside the read-only one. What "full" includes is open, below. |

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
| **refused** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat in the browser, nothing connected, A reader on my drive, Find and read my files, An assistant over my Workspace, reading |
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my mailbox, Find things in the inbox, draft replies, never send, Search our tenant, read-only, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/write.file.host`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/write.file.host/index.html)*
