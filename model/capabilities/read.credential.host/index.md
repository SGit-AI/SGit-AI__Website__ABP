# read.credential.host

> Read credentials stored where it runs. Reach host, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.credential.host/index.html> · site v0.5.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.credential.host

# `read.credential.host`

**Read credentials stored where it runs.** Its effect is **no**: cannot be undone.

## What this id is made of

**This is not a string.** It is [`read`](../../../model/lexicon/verbs/read/index.md)`.`[`credential`](../../../model/lexicon/objects/credential/index.md)`.`[`host`](../../../model/lexicon/reaches/host/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`read`](../../../model/lexicon/verbs/read/index.md) | `has_verb` | this capability has the verb `read` |
| [`credential`](../../../model/lexicon/objects/credential/index.md) | `acts_on` | this capability acts on `credential` |
| [`host`](../../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
| [`identity`](../../../model/lexicon/families/identity/index.md) | `in_family` | this capability is in the `identity` family |
| [`no`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `read.credential.host` is emerges from the edges traceable from it. The strongest case is [`host`](../../../model/lexicon/reaches/host/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 10 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | not stated | the credential-shaped paths present are the SESSION'S OWN: its commit-signing key and its vault keystore. No user credential is in the container; presence cannot tell whose a key is, so this is the operator's account |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | not stated | a published read-only audit tool enumerates exactly this class in a home directory |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | not stated | a published read-only audit tool enumerates exactly this class in a home directory |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | documented | not stated |  |
| ● | Claude, with the Gmail connector enabled *(contributed by riskmandate.ai)* | none (not a control) | inferred | own | password resets, one-time codes, invitations and account-recovery mail arrive in a mailbox; reading messages reads those. Inferred, not documented - no tool or scope on either vendor's page separates them. |
| ● | Claude's Microsoft 365 connector (Outlook, SharePoint, OneDrive, Teams) *(contributed by riskmandate.ai)* | none (not a control) | inferred | organisation | a work mailbox carries password resets, MFA codes and shared credentials sent between colleagues; a SharePoint estate carries key files and configuration. Reading either reads those. Inferred, not documented. |
| ● | An assistant connected to a personal Google Drive with drive.readonly *(contributed by riskmandate.ai)* | none (not a control) | inferred | own | drives hold exported keys, service-account files, .env backups and password exports beside everything else. Reading all files reads those. Inferred, not documented. |
| ● | An assistant connected to a personal Gmail mailbox with gmail.readonly *(contributed by riskmandate.ai)* | none (not a control) | inferred | own | password resets, one-time codes, invitations and account-recovery mail arrive in this mailbox. Reading every message reads those. Inferred, not documented - and no scope separates them. |
| ● | The Google Workspace MCP servers (Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat) *(contributed by riskmandate.ai)* | none (not a control) | inferred | own | a mailbox carries password resets, one-time codes and invitations; a drive carries exported keys and configuration. Reading all of either reads those too, and no scope separates them. Inferred from the two read rows, not documented. |
| ● | A self-hosted n8n instance, reached with an owner-scoped API key *(contributed by riskmandate.ai)* | none (not a control) | measured | organisation | the identical operation was blocked through the REST path - by the measuring environment's own gateway, not the platform - and returned full credential metadata through the MCP interface. Metadata only; nothing was exported. The write-up's own lesson: the barrier class of a capability can depend on which door was used to ask. |

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
| **refused** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A reader on my mailbox, Find things in the inbox, draft replies, never send, A reader on my drive, Search our tenant, read-only, An assistant over my Workspace, reading, A sandbox: build and run one AI-agent workflow |
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, A browser extension I installed, A scheduled job under a service account, Find and read my files |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| keep credentials out of the account the agent runs as: a credential helper, a separate account, or a container without your home mounted | an afternoon, and re-authenticating where the agent needs a credential of its own | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/read.credential.host`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.credential.host/index.html)*
