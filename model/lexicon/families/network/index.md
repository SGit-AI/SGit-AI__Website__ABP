# network (family)

> The family network as a node: the 2 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/families/network/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / network

# `network`

endpoints and hosts

> **A node carries no inherent meaning.** What `network` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **2 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).



## The 2 primitives with this family

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`send.endpoint.allowed`](../../../../model/capabilities/send.endpoint.allowed/index.md) | Reach a permitted list of hosts | [`send`](../../../../model/lexicon/verbs/send/index.md)`.`[`network-endpoint`](../../../../model/lexicon/objects/network-endpoint/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | no | 1 of 9 |
| [`send.endpoint.world`](../../../../model/capabilities/send.endpoint.world/index.md) | Reach any host on the internet | [`send`](../../../../model/lexicon/verbs/send/index.md)`.`[`network-endpoint`](../../../../model/lexicon/objects/network-endpoint/index.md)`.`[`world`](../../../../model/lexicon/reaches/world/index.md) | no | 6 of 9 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `family_of` | `network` is the family of these 2 primitives | 2 capabilities |
| `in_family` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/families/network.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/families/network/index.html)*
