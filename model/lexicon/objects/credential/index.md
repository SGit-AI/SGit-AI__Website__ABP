# credential (object)

> The object credential as a node: the 4 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/objects/credential/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / credential

# `credential`

The object `credential`, and every primitive it appears in. **This page is a query, not a definition.**

> **A node carries no inherent meaning.** What `credential` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **4 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).



## The 4 primitives with this object

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`authenticate-as.credential.signing`](../../../../model/capabilities/authenticate-as.credential.signing/index.md) | Sign commits with the key it holds | [`authenticate-as`](../../../../model/lexicon/verbs/authenticate-as/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 3 of 17 |
| [`authenticate-as.credential.tenant`](../../../../model/capabilities/authenticate-as.credential.tenant/index.md) | Act in accounts with the credentials it holds | [`authenticate-as`](../../../../model/lexicon/verbs/authenticate-as/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 15 of 17 |
| [`grant.credential.self`](../../../../model/capabilities/grant.credential.self/index.md) | Change its own permission settings | [`grant`](../../../../model/lexicon/verbs/grant/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`self`](../../../../model/lexicon/reaches/self/index.md) | yes | 3 of 17 |
| [`read.credential.host`](../../../../model/capabilities/read.credential.host/index.md) | Read credentials stored where it runs | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`credential`](../../../../model/lexicon/objects/credential/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 11 of 17 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `acted_on_by` | `credential` is the object class of these 4 primitives | 4 capabilities |
| `acts_on` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/objects/credential.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/objects/credential/index.html)*
