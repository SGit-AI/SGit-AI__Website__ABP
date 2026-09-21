# grant.credential.self

> Change its own permission settings. Reach self, undo yes. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/grant.credential.self/index.html> · site v0.7.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / grant.credential.self

# `grant.credential.self`

**Change its own permission settings.** Its effect is **yes**: undone.

## What this id is made of

**This is not a string.** It is [`grant`](../../../model/lexicon/verbs/grant/index.md)`.`[`credential`](../../../model/lexicon/objects/credential/index.md)`.`[`self`](../../../model/lexicon/reaches/self/index.md), three nodes joined by three edges, and each of them has an address, a page and a JSON file. Follow any of them and you get the query for that word rather than a definition of it.

| Node | Edge | Reads as |
|---|---|---|
| [`grant`](../../../model/lexicon/verbs/grant/index.md) | `has_verb` | this capability has the verb `grant` |
| [`credential`](../../../model/lexicon/objects/credential/index.md) | `acts_on` | this capability acts on `credential` |
| [`self`](../../../model/lexicon/reaches/self/index.md) | `reaches` | this capability reaches `self` |
| [`identity`](../../../model/lexicon/families/identity/index.md) | `in_family` | this capability is in the `identity` family |
| [`yes`](../../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `yes` |

> **The gloss above is a convenience, not the definition.** A node carries no inherent meaning: what `grant.credential.self` is emerges from the edges traceable from it. The strongest case is [`self`](../../../model/lexicon/reaches/self/index.md), where the deployment shapes that use it **do not agree** about what it means, and the page keeps the disagreement rather than averaging it.

## In 3 of 16 published shapes

|  | Deployment shape | Barrier there | Known by | Whose material | Note |
|---|---|---|---|---|---|
| ◐ | Claude Code (the CLI, on your own machine) | setting (not a control) | derived | not stated | anything running as you can rewrite the file that turns the prompt off |
| ◐ | Claude Code (the CLI, on your own machine) | setting (not a control) | derived | not stated | anything running as you can rewrite the file that turns the prompt off |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived | not stated |  |

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
| **refused** | A coding assistant on my machine, The desktop app, with local tools switched on |
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account, A reader on my mailbox, Find things in the inbox, draft replies, never send, A reader on my drive, Search our tenant, read-only, Find and read my files, An assistant over my Workspace, reading, A sandbox: build and run one AI-agent workflow |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| settings owned by a different user than the one the agent runs as, or set above the session by the platform | minutes, if the platform supports it; otherwise the separate account | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess. Since v0.4.3 it is also a node, `setting/grant.credential.self`, in [the deployment shape universe](../../../model/universes/u2/index.md): it **narrows** this capability and **moves** it to the barrier named in the third column, which is the path the prohibitions table's last column is a projection of.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/grant.credential.self/index.html)*
