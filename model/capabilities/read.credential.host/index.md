# read.credential.host

> Read credentials stored where it runs. Reach host, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.credential.host/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.credential.host

# `read.credential.host`

**Read credentials stored where it runs.** Verb `read`, object `credential`, reach `host`, family `identity`. Its effect is **no**: cannot be undone.

## In 4 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | the credential-shaped paths present are the SESSION'S OWN: its commit-signing key and its vault keystore. No user credential is in the container; presence cannot tell whose a key is, so this is the operator's account |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | a published read-only audit tool enumerates exactly this class in a home directory |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | documented | a published read-only audit tool enumerates exactly this class in a home directory |
| ● | Claude Desktop (a desktop app with local tools) | none (not a control) | documented |  |

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
| **refused** | A coding assistant on my machine, The desktop app, with local tools switched on, Chat in the browser, nothing connected, A CI job on a hosted runner |
| **unstated** | A coding assistant in a container on the web, Chat, with connectors switched on, A browser extension I installed, A scheduled job under a service account |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| keep credentials out of the account the agent runs as: a credential helper, a separate account, or a container without your home mounted | an afternoon, and re-authenticating where the agent needs a credential of its own | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.credential.host/index.html)*
