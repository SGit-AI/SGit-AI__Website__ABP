# authenticate-as.credential.signing

> Sign commits with the key it holds. Reach tenant, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/authenticate-as.credential.signing/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / authenticate-as.credential.signing

# `authenticate-as.credential.signing`

**Sign commits with the key it holds.** Verb `authenticate-as`, object `credential`, reach `tenant`, family `code`. Its effect is **no**: cannot be undone.

## In 3 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | commits are signed with the session's own key, registered as an agent identity in this site's registry (sha256-f9facb4c94da6c19) - not with yours |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | if commit signing is configured for the account, the agent signs as you |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | if commit signing is configured for the account, the agent signs as you |

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
| **refused** | A coding assistant on my machine, A coding assistant in a container on the web |
| **unstated** | The desktop app, with local tools switched on, Chat, with connectors switched on, Chat in the browser, nothing connected, A CI job on a hosted runner, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| a signing key of the agent's own, so its commits are signed as it and not as you (the registry's identity records exist for this) | an hour, and a second key to manage | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/authenticate-as.credential.signing/index.html)*
