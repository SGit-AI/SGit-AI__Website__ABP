# authenticate-as.credential.tenant

> Act in accounts with the credentials it holds. Reach tenant, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/authenticate-as.credential.tenant/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / authenticate-as.credential.tenant

# `authenticate-as.credential.tenant`

**Act in accounts with the credentials it holds.** Verb `authenticate-as`, object `credential`, reach `tenant`, family `identity`. Its effect is **no**: cannot be undone.

## In 7 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ○ | Claude Code on the web (a remote session container) | boundary | inferred | five key-shaped variables and a code-host token - the platform's, scoped to in-scope repositories; it acts as the platform's app, never as you |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | inferred from the credentials the account holds |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | inferred from the credentials the account holds |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | derived |  |
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | a cloud connector acts as you |
| ◐ | A browser extension with broad host permissions | setting (not a control) | documented | acts inside sites where you have a session, as you |
| ● | A scheduled job running as a service account | none (not a control) | derived | a service-account credential, rarely rotated |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | A scheduled job under a service account |
| **refused** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat in the browser, nothing connected, A browser extension I installed |
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, A CI job on a hosted runner |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/authenticate-as.credential.tenant/index.html)*
