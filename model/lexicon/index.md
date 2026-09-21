# The lexicon

> Every word in the capability grammar as a node with its own address, its own JSON and its own page: ten verbs, nine object classes, five reach classes and nine families.

*Source: <https://abp.sgit.ai/model/lexicon/index.html> · site v0.6.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The lexicon

# The lexicon

**`read.file.project` is not a string.** It is three nodes and three edges, and each of those nodes has an address, a JSON file and a page of its own. This is where they are.

## What changed, and why it mattered

> **Until v0.3.0 this site attached the meaning to the node.** A primitive was an identifier with a gloss beside it, and the gloss was the definition. That is schema-first thinking dressed in graph syntax: a self-describing node has smuggled the schema back in. Now the gloss is still there and it is no longer the definition. **What a primitive means is what its edges reach.**

### One primitive, spelled out

|  | Node | Edge | Reads as |
|---|---|---|---|
|  | [`read.record.browsing`](../../model/capabilities/read.record.browsing/index.md) |  | *Read every page you visit* |
|  | [`read`](../../model/lexicon/verbs/read/index.md) | `has_verb` | this capability has the verb `read` |
|  | [`record`](../../model/lexicon/objects/record/index.md) | `acts_on` | this capability acts on `record` |
|  | [`host`](../../model/lexicon/reaches/host/index.md) | `reaches` | this capability reaches `host` |
|  | [`browser`](../../model/lexicon/families/browser/index.md) | `in_family` | this capability is in the `browser` family |
|  | [`no`](../../model/undo/index.md) | `has_undo_class` | this capability has the undo class `no` |

**Each of those is a link because each of those is a node.** Follow [`host`](../../model/lexicon/reaches/host/index.md) and you get every primitive that reaches that far and, more usefully, what each deployment shape says that reach class actually means. They do not agree, and the page keeps the disagreement rather than averaging it.

## The words

**[The action half of a primitive](../../model/lexicon/index.md#verbs)**: Ten verbs. A verb on its own is a word: what `read' means here is whatever the primitives under it reach, which is why this page is a query rather than a definition.
[`authenticate-as`](../../model/lexicon/verbs/authenticate-as/index.md) · [`create`](../../model/lexicon/verbs/create/index.md) · [`delete`](../../model/lexicon/verbs/delete/index.md) · [`execute`](../../model/lexicon/verbs/execute/index.md) · [`grant`](../../model/lexicon/verbs/grant/index.md) · [`read`](../../model/lexicon/verbs/read/index.md) · [`receive`](../../model/lexicon/verbs/receive/index.md) · [`revoke`](../../model/lexicon/verbs/revoke/index.md) · [`send`](../../model/lexicon/verbs/send/index.md) · [`write`](../../model/lexicon/verbs/write/index.md)

**[What a primitive acts on](../../model/lexicon/index.md#objects)**: Nine object classes. The same verb against a different object class is a different primitive, and a different conversation.
[`budget`](../../model/lexicon/objects/budget/index.md) · [`credential`](../../model/lexicon/objects/credential/index.md) · [`file`](../../model/lexicon/objects/file/index.md) · [`message`](../../model/lexicon/objects/message/index.md) · [`network-endpoint`](../../model/lexicon/objects/network-endpoint/index.md) · [`process`](../../model/lexicon/objects/process/index.md) · [`record`](../../model/lexicon/objects/record/index.md) · [`repository`](../../model/lexicon/objects/repository/index.md) · [`schedule`](../../model/lexicon/objects/schedule/index.md)

**[How far a primitive reaches](../../model/lexicon/index.md#reaches)**: Five reach classes, and the most contested nodes in the model: what `host' and `tenant' MEAN is the deployment shape's to say, not the grammar's.
[`host`](../../model/lexicon/reaches/host/index.md) · [`project`](../../model/lexicon/reaches/project/index.md) · [`self`](../../model/lexicon/reaches/self/index.md) · [`tenant`](../../model/lexicon/reaches/tenant/index.md) · [`world`](../../model/lexicon/reaches/world/index.md)

**[A grouping of primitives for a reader](../../model/lexicon/index.md#families)**: Nine families. A family is an altitude device: it groups facts for a reader and carries none of its own.
[`browser`](../../model/lexicon/families/browser/index.md) · [`code`](../../model/lexicon/families/code/index.md) · [`communication`](../../model/lexicon/families/communication/index.md) · [`filesystem`](../../model/lexicon/families/filesystem/index.md) · [`identity`](../../model/lexicon/families/identity/index.md) · [`money`](../../model/lexicon/families/money/index.md) · [`network`](../../model/lexicon/families/network/index.md) · [`process`](../../model/lexicon/families/process/index.md) · [`schedule`](../../model/lexicon/families/schedule/index.md)

> **2 of these words have no primitive under them: `receive`, `revoke`. In this graph they mean nothing yet.** They are in the published grammar and they are kept and marked rather than dropped, because a node connected to nothing is literally meaningless and saying so is more useful than writing it a definition no edge supports. Adding a primitive that uses one would need a probe. **This is a finding about the vocabulary rather than a defect in it**, and it is the kind of gap that only becomes visible once the words are nodes.

## The rest of the grammar

| Address | What is there |
|---|---|
| [The edge vocabulary](../../model/graph/edges/index.md) | 22 edges, each a verb with a distinct inverse, a stated domain and range, and where it came from. The generic association edge is banned and there is none in this model. |
| [The node type formulas](../../model/graph/formulas/index.md) | 17 node types, each a required pattern of paths rather than a label. Run against the graph on every build. |
| [The three layers](../../model/graph/layers/index.md) | How a vault extends this vocabulary for one customer without merging anything, and without asking permission. |
| [The graph rules](../../model/graph/index.md) | The five published rules and what each forces on this model. |

[The lexicon as JSON](../../data/lexicon/index.json) · [The whole graph](../../data/graph/index.json) · [Meaning through connectivity](https://graphs.sgit.ai/)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/lexicon/index.html)*
