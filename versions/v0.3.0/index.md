# v0.3.0: read, file and project become nodes with their own addresses, and a node type stops being a label and becomes a formula

> The model pages were a projection of nothing. A capability was an identifier with a gloss beside it, which is a self-describing node, which is schema-first thinking dressed in graph syntax: the meaning was attached to the node rather than derived from its edges. This release...

*Source: <https://abp.sgit.ai/versions/v0.3.0/index.html> · site v0.7.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.3.0

# v0.3.0: read, file and project become nodes with their own addresses, and a node type stops being a label and becomes a formula

The model pages were a projection of nothing. A capability was an identifier with a gloss beside it, which is a self-describing node, which is schema-first thinking dressed in graph syntax: the meaning was attached to the node rather than derived from its edges. This release makes the ontology real. Every word the grammar is spelled with is now a node with an address, a JSON file and a page, `read.file.project` is three nodes joined by three edges, a node type is a formula over paths rather than a label somebody applied, and the three layer construction that lets a customer vault disagree with this vocabulary without merging anything is written down.

| Field | Value |
|---|---|
| Version | `v0.3.0` |
| Date | 2026-09-12 |
| Commit | **`git rev-list -n 1 v0.3.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.3.0:`. The hash is not written into [`versions/v0.3.0.json`](../../versions/v0.3.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.3.0.json`](../../versions/v0.3.0.json) |

## What changed

- A lexicon at /model/lexicon/ with a page and a JSON file per word: 10 verbs, 9 object classes, 5 reach classes and 9 families, 33 nodes that previously existed only as substrings of a capability id. A node with no address cannot be argued with, and being argued with is the point of publishing a vocabulary.
- The reach class pages carry the disagreement rather than resolving it: `host` means the machine you are sitting at in one deployment shape and an ephemeral container in another, and both rows are published, each owned by the shape that said it. Merging them would erase the finding, which is the ABP's own argument in one column.
- An edge vocabulary at /model/graph/edges/ with 15 edges, each a verb with a distinct and meaningfully named inverse, a stated domain and a stated range. Four are reused from the network's published edge set under their published names; eleven are proposed here and say so, in the same way that set marks nine of its own inverses as proposed there. There is no generic association edge in this model.
- Node type formulas at /model/graph/formulas/, run against the graph on every build. `is_control: true` on a barrier is gone: [Control] is now a barrier that is enforced_by an enforcer the grant does not include, walked rather than asserted, and exactly one of the four barriers matches. The release gate fails if that stops being true.
- The three layers at /model/graph/layers/: shared facts owned by nobody, per-party formulas, and declared bridges through anchor nodes. This is the page a customer vault needs, because it says how their vocabulary attaches to this one without either side asking permission and without anything being merged.
- data/graph/ carries the nodes, the edges, the edge vocabulary and the node type formulas; data/lexicon/ carries a file per word; data/bridges/ carries the declared bridges, starting with the one back to the vocabulary this was promoted from.

## What it was built against

- graphs.sgit.ai, read 12 September 2026: meaning through connectivity, a node carries no inherent meaning, classification is a query rather than a judgment, and vocabularies are bridged through anchor nodes rather than merged because merging erases the disagreement.
- The published edge set at graphs.sgit.ai/v1/grammar/edge-set.html, for the four edges reused unchanged and for the rule that extending the set needs a sentence, a different inverse sentence, a domain and a range.
- graphs.sgit.ai/v1/depth/, for the three layer construction and for node types as required path patterns rather than labels.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.3.0/index.html)*
