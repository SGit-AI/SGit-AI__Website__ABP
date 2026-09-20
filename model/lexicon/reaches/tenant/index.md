# tenant (reach)

> The reach tenant as a node: the 7 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/reaches/tenant/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / tenant

# `tenant`

the organisation's accounts, repositories and services

> **A node carries no inherent meaning.** What `tenant` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **7 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).

## What the shapes say `tenant` means, and they do not agree

> **These definitions are not merged, and that is the design.** Merging two vocabularies erases the disagreement, and the disagreement is the finding. Each row below is owned by the shape that said it. A reader deciding what `tenant` costs them has to read the row for the shape they run, not an average of the rows. [Why vocabularies are bridged rather than merged](https://graphs.sgit.ai/v1/depth/index.html).

| The shape | Variant | What `tenant` means there |
|---|---|---|
| [Claude Code on the web (a remote session container)](../../../../examples/index.md) | `ccr-container` | the attached repository and the platform's scoped tokens; not your accounts |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-confirmations-off` | your accounts, with the credentials in your home directory |
| [Claude Code (the CLI, on your own machine)](../../../../examples/index.md) | `local-default` | your accounts, with the credentials in your home directory |
| [Claude Desktop (a desktop app with local tools)](../../../../examples/index.md) | `default` | your accounts |
| [Claude (in the browser, with connectors switched on)](../../../../examples/index.md) | `connectors-on` | the accounts you connected, as you scoped them |
| [A browser extension with broad host permissions](../../../../examples/index.md) | `broad-host-permissions` | the sites you are logged into, as you |
| [A scheduled job running as a service account](../../../../examples/index.md) | `service-account` | whatever the service account's credential opens |
| [Actions runner (a hosted CI job)](../../../../examples/index.md) | `ci` | the repository, with the workflow's token |
| [ChatGPT (in the browser, no connectors)](../../../../examples/index.md) | `default` | nothing of yours |

**That is the ABP's own argument in one column.** The same word, the same grammar, and a materially different exposure depending on where the agent runs. It is why an ABP is about the deployment rather than the product.



## The 7 primitives with this reach

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`authenticate-as.credential.signing`](../../../../model/capabilities/authenticate-as.credential.signing/index.md) | Sign commits with the key it holds | [`authenticate-as`](../../../../model/lexicon/verbs/authenticate-as/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 3 of 9 |
| [`authenticate-as.credential.tenant`](../../../../model/capabilities/authenticate-as.credential.tenant/index.md) | Act in accounts with the credentials it holds | [`authenticate-as`](../../../../model/lexicon/verbs/authenticate-as/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 7 of 9 |
| [`create.schedule.tenant`](../../../../model/capabilities/create.schedule.tenant/index.md) | Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | [`create`](../../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../../model/lexicon/objects/schedule/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | yes | 1 of 9 |
| [`read.message.tenant`](../../../../model/capabilities/read.message.tenant/index.md) | Read mail or chat it is connected to | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`message`](../../../../model/lexicon/objects/message/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 1 of 9 |
| [`send.endpoint.allowed`](../../../../model/capabilities/send.endpoint.allowed/index.md) | Reach a permitted list of hosts | [`send`](../../../../model/lexicon/verbs/send/index.md)`.`[`network-endpoint`](../../../../model/lexicon/objects/network-endpoint/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 1 of 9 |
| [`write.budget.tenant`](../../../../model/capabilities/write.budget.tenant/index.md) | Spend money or tokens against an account it holds | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`budget`](../../../../model/lexicon/objects/budget/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 1 of 9 |
| [`write.repository.tenant`](../../../../model/capabilities/write.repository.tenant/index.md) | Push to a code host (any branch it can reach) | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`repository`](../../../../model/lexicon/objects/repository/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | with-effort | 4 of 9 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `reachable_from` | `tenant` is the reach of these 7 primitives | 7 capabilities |
| `reaches` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/reaches/tenant.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/reaches/tenant/index.html)*
