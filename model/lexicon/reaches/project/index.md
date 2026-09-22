# project (reach)

> The reach project as a node: the 3 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/reaches/project/index.html> · site v0.8.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / project

# `project`

the working tree or workspace it was pointed at

> **A node carries no inherent meaning.** What `project` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **3 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).

## What the shapes say `project` means, and they do not agree

> **These definitions are not merged, and that is the design.** Merging two vocabularies erases the disagreement, and the disagreement is the finding. Each row below is owned by the shape that said it. A reader deciding what `project` costs them has to read the row for the shape they run, not an average of the rows. [Why vocabularies are bridged rather than merged](https://graphs.sgit.ai/v1/depth/index.html).

| The shape | Variant | What `project` means there |
|---|---|---|
| [A self-hosted n8n instance, reached with an owner-scoped API key](../../../../examples/index.md) | `owner-api-key` | the workflows on the instance - the thing the key was given to build |

**That is the ABP's own argument in one column.** The same word, the same grammar, and a materially different exposure depending on where the agent runs. It is why an ABP is about the deployment rather than the product.



## The 3 primitives with this reach

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`read.file.project`](../../../../model/capabilities/read.file.project/index.md) | Read the project it is working on | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`project`](../../../../model/lexicon/reaches/project/index.md) | yes | 7 of 16 |
| [`write.file.project`](../../../../model/capabilities/write.file.project/index.md) | Change the project it is working on | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`project`](../../../../model/lexicon/reaches/project/index.md) | with-effort | 6 of 16 |
| [`write.repository.project`](../../../../model/capabilities/write.repository.project/index.md) | Commit to the repository it was pointed at | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`repository`](../../../../model/lexicon/objects/repository/index.md)`.`[`project`](../../../../model/lexicon/reaches/project/index.md) | with-effort | 4 of 16 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `reachable_from` | `project` is the reach of these 3 primitives | 3 capabilities |
| `reaches` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/reaches/project.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/reaches/project/index.html)*
