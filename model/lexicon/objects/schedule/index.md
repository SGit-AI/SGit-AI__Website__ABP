# schedule (object)

> The object schedule as a node: the 2 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/objects/schedule/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / schedule

# `schedule`

The object `schedule`, and every primitive it appears in. **This page is a query, not a definition.**

> **A node carries no inherent meaning.** What `schedule` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **2 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).



## The 2 primitives with this object

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`create.schedule.host`](../../../../model/capabilities/create.schedule.host/index.md) | Create something that outlives the turn where it runs (a cron, a service) | [`create`](../../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../../model/lexicon/objects/schedule/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | yes | 4 of 16 |
| [`create.schedule.tenant`](../../../../model/capabilities/create.schedule.tenant/index.md) | Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | [`create`](../../../../model/lexicon/verbs/create/index.md)`.`[`schedule`](../../../../model/lexicon/objects/schedule/index.md)`.`[`tenant`](../../../../model/lexicon/reaches/tenant/index.md) | yes | 3 of 16 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `acted_on_by` | `schedule` is the object class of these 2 primitives | 2 capabilities |
| `acts_on` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/objects/schedule.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/objects/schedule/index.html)*
