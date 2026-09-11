# grant.credential.self

> Change its own permission settings. Reach self, undo yes. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/grant.credential.self/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / grant.credential.self

# `grant.credential.self`

**Change its own permission settings.** Verb `grant`, object `credential`, reach `self`, family `identity`. Its effect is **yes**: undone.

## In 3 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ◐ | Claude Code (the CLI, on your own machine) | setting (not a control) | derived | anything running as you can rewrite the file that turns the prompt off |
| ◐ | Claude Code (the CLI, on your own machine) | setting (not a control) | derived | anything running as you can rewrite the file that turns the prompt off |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived |  |

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
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| settings owned by a different user than the one the agent runs as, or set above the session by the platform | minutes, if the platform supports it; otherwise the separate account | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/grant.credential.self/index.html)*
