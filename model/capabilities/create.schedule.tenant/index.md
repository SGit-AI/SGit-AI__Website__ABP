# create.schedule.tenant

> Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session). Reach tenant, undo yes. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/create.schedule.tenant/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / create.schedule.tenant

# `create.schedule.tenant`

**Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session).** Its effect is **yes**: undone.

## What this id is made of

**This is not a string.** It is [`create`](../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../model/lexicon/objects/schedule/index.md)`.`[`tenant`](../../../model/lexicon/reaches/tenant/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`create`](../../../model/lexicon/verbs/create/index.md) | `has_verb` | this capability has the verb `create` |
| [`schedule`](../../../model/lexicon/objects/schedule/index.md) | `acts_on` | this capability acts on `schedule` |
| [`tenant`](../../../model/lexicon/reaches/tenant/index.md) | `reaches` | this capability reaches `tenant` |
| [`schedule`](../../../model/lexicon/families/schedule/index.md) | `in_family` | this capability is in the `schedule` family |
| [`yes`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `yes` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `create.schedule.tenant` is emerges from the edges traceable from it. The strongest case is [`tenant`](../../../model/lexicon/reaches/tenant/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 3 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ◐ | Claude Code on the web (a remote session container) | setting (not a control) | self-reported | not stated | a routine or a scheduled trigger resumes this session or spawns another later: it outlives the container |
| ◐ | Claude, with the Gmail connector enabled *(contributed by riskmandate.ai)* | setting (not a control) | documented | mixed | a Gmail filter is a standing rule that acts on every future message without the agent present - labelling, archiving, forwarding - which is what this primitive names: "something that outlives the session, on the platform". The tool is on the directory listing (captured 2026-09-16); it is not on Google's reference page for the server (2026-07-21), and the scope that filters need, gmail.settings.basic - "See, edit, create, or change your email settings and filters in Gmail." - is not among the three lines on the consent screen. Whether the tool works under the consented scopes is open; the row records what is listed. Asked in the measured session, Claude said: "the Gmail connector I have access to only exposes labels/messages, not account-level settings like forwarding rules, filters, vacation responder, IMAP/POP config, or signatures" - self-reported, and against the listing. |
| ● | A self-hosted n8n instance, reached with an owner-scoped API key *(contributed by riskmandate.ai)* | none (not a control) | measured | organisation | a webhook-triggered workflow was built, activated and executed. Activation is refused for a workflow with no trigger - a check on shape, not on risk - so the platform bounds nothing about what an activated workflow does. |

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
| **refused** | A coding assistant in a container on the web, Chat in the browser, nothing connected, Find things in the inbox, draft replies, never send |
| **unstated** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat, with connectors switched on, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my mailbox, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/create.schedule.tenant/index.html)*
