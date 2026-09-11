# read.file.host

> Read any file the account can reach. Reach host, undo no. Which published deployment shapes have it, at what barrier, and what the starting mandates say.

*Source: <https://abp.sgit.ai/model/capabilities/read.file.host/index.html> · site v0.1.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The capabilities](../../../model/capabilities/index.md) / read.file.host

# `read.file.host`

**Read any file the account can reach.** Verb `read`, object `file`, reach `host`, family `filesystem`. Its effect is **no**: cannot be undone.

## In 7 of 9 published shapes

|  | Deployment shape | Barrier there | Known by | Note |
|---|---|---|---|---|
| ● | Claude Code on the web (a remote session container) | none (not a control) | observed | any file in the container - the attached clone, the harness's state, the system. Not your machine's files (the assess tree's 'home: boundary') |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | everything your account can read, because a shell as you reads as you |
| ● | Claude Code (the CLI, on your own machine) | none (not a control) | derived | everything your account can read, because a shell as you reads as you |
| ◐ | Claude Desktop (a desktop app with local tools) | setting (not a control) | derived |  |
| ○ | Claude (in the browser, with connectors switched on) | boundary | derived | a drive connector: your other files, as scoped |
| ● | A scheduled job running as a service account | none (not a control) | derived |  |
| ● | Actions runner (a hosted CI job) | none (not a control) | observed | the runner's user with passwordless escalation: every file on the ephemeral machine |

|  | Barrier | What stands in the way | Is it a control |
|---|---|---|---|
| ● | none | nothing in the way | no |
| ◉ | expectation | a rule in prose, enforced by nobody | no |
| ◐ | setting | a switch the agent's own account can flip | no |
| ○ | boundary | enforced above the grant, out of the agent's reach | **yes** |

## What the starting mandates say about it

| The mandate says | Which mandates |
|---|---|
| **authorised** | Chat, with connectors switched on, A scheduled job under a service account |
| **refused** | A coding assistant on my machine, Chat in the browser, nothing connected |
| **unstated** | A coding assistant in a container on the web, The desktop app, with local tools switched on, A CI job on a hosted runner, A browser extension I installed |

**Unstated is not authorised.** A mandate that never mentioned a capability did not authorise it, and the delta on every example page counts it as excess and says which kind it was.

## What would move it to the fourth barrier

| What | What it costs | The barrier afterwards |
|---|---|---|
| run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |

> **This is a published reduction, not a recommendation.** Whether it is worth doing depends on the assets and the consequences, which are not in this document and are not this site's to guess.

[The capability grammar](../../../model/capabilities/index.md) · [This primitive as JSON](../../../data/capabilities.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/capabilities/read.file.host/index.html)*
