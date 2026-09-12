# filesystem (family)

> The family filesystem as a node: the 6 capability primitives it appears in, what they reach, and how it connects. Meaning from connectivity, not from a definition.

*Source: <https://abp.sgit.ai/model/lexicon/families/filesystem/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../../index.md) / [The model](../../../../model/index.md) / [The lexicon](../../../../model/lexicon/index.md) / filesystem

# `filesystem`

files and directories

> **A node carries no inherent meaning.** What `filesystem` means here emerges from the edges traceable from it, and confidence in that meaning is proportional to how richly it is connected. It is connected to **6 of 23 primitives** here. That, and not the sentence above, is what it means. [The discipline this follows](https://graphs.sgit.ai/).



## The 6 primitives with this family

| Primitive | Published gloss | Spelled out | Undo | In how many shapes |
|---|---|---|---|---|
| [`delete.file.host`](../../../../model/capabilities/delete.file.host/index.md) | Delete files anywhere the account can reach | [`delete`](../../../../model/lexicon/verbs/delete/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 4 of 9 |
| [`read.file.host`](../../../../model/capabilities/read.file.host/index.md) | Read any file the account can reach | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 7 of 9 |
| [`read.file.project`](../../../../model/capabilities/read.file.project/index.md) | Read the project it is working on | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`project`](../../../../model/lexicon/reaches/project/index.md) | yes | 7 of 9 |
| [`read.record.history`](../../../../model/capabilities/read.record.history/index.md) | Read a retained record: shell history, past sessions | [`read`](../../../../model/lexicon/verbs/read/index.md)`.`[`record`](../../../../model/lexicon/objects/record/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | no | 4 of 9 |
| [`write.file.host`](../../../../model/capabilities/write.file.host/index.md) | Change any file the account can reach | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`host`](../../../../model/lexicon/reaches/host/index.md) | with-effort | 6 of 9 |
| [`write.file.project`](../../../../model/capabilities/write.file.project/index.md) | Change the project it is working on | [`write`](../../../../model/lexicon/verbs/write/index.md)`.`[`file`](../../../../model/lexicon/objects/file/index.md)`.`[`project`](../../../../model/lexicon/reaches/project/index.md) | with-effort | 5 of 9 |

## How this node connects

| Edge | Reads as | To |
|---|---|---|
| `family_of` | `filesystem` is the family of these 6 primitives | 6 capabilities |
| `in_family` | the inverse, walked the other way, with different fan out | one capability at a time |

[This node as JSON](../../../../data/lexicon/families/filesystem.json) · [The lexicon](../../../../model/lexicon/index.md) · [The edge vocabulary](../../../../model/graph/edges/index.md)

---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/families/filesystem/index.html)*
