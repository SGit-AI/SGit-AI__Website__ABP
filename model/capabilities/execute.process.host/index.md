# execute.process.host

> Run programs as the account. Reach host, undo with-effort. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/execute.process.host/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / execute.process.host

# `execute.process.host`

**Run programs as the account.** Its effect is **with-effort**: undone at a cost.

## What this id is made of

**This is not a string.** It is [`execute`](../../../model/lexicon/verbs/execute/index.md)`.`[`process`](../../../model/lexicon/objects/process/index.md)`.`[`host`](../../../model/lexicon/reaches/host/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`execute`](../../../model/lexicon/verbs/execute/index.md) | `has_verb` | this capability has the verb `execute` |
| [`process`](../../../model/lexicon/objects/process/index.md) | `acts_on` | this capability acts on `process` |
| [`host`](../../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
| [`process`](../../../model/lexicon/families/process/index.md) | `in_family` | this capability is in the `process` family |
| [`with-effort`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `with-effort` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `execute.process.host` is emerges from the edges traceable from it. The strongest case is [`host`](../../../model/lexicon/reaches/host/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 7 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | root inside the container: every process and file IN THE CONTAINER. The container is the host; your machine is not reachable |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | not stated |  |
| ◐ | Claude Code (the CLI, on your own machine) | setting (not a control) | derived | not stated |  |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived | not stated | run terminal commands as you |
| ● | A scheduled job running as a service account | none (not a control) | derived | not stated | as the service account, on a schedule |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | not stated | runs as uid 1001; passwordless escalation available (n1a) - programs run as this user and can escalate |
| ● | A self-hosted n8n instance, reached with an owner-scoped API key *(contributed by riskmandate.ai)* | none (not a control) | derived | organisation | a workflow can carry a code node that runs on the platform's own server. Not tested in the session; derived from what the platform is, and an open question below. |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A coding assistant on my machine, A coding assistant in a container on the web, A CI job on a hosted runner, A scheduled job under a service account |
| **refused** | The desktop app, with local tools switched on, Chat in the browser, nothing connected |
| **unstated** | Chat, with connectors switched on, A browser extension I installed, A reader on my mailbox, Find things in the inbox, draft replies, never send, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/execute.process.host`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/execute.process.host/index.html)*
