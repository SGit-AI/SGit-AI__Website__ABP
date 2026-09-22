# The edge vocabulary

> The 22 edges this model is written in, each a verb with a distinct inverse, a stated domain and range, and the sentence it reads as.

*Source: <https://abp.sgit.ai/model/graph/edges/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The graph](../../../model/graph/index.md) / The edges

# The edge vocabulary

**22 edges.** Every one is a verb with a distinct, meaningfully named inverse, and the inverse is not the same edge walked backwards: `grants` and `granted_by` have different fan out, and that asymmetry is what stops the graph exploding.

> **The generic association edge is banned, and there is none in this model.** It constrains nothing and costs fan out. If you find yourself wanting `relates_to`, the honest move is a new edge with a sentence, a different sentence for its inverse, and a stated domain and range.

## Reused from the published set, unchanged

These are not this site's to rename. They are published at [the network's edge set](https://graphs.sgit.ai/v1/grammar/edge-set.html) and reused under their published names.

| Edge | Inverse | Domain | Range | Reads as |
|---|---|---|---|---|
| `grants` | `granted_by` | `DeploymentShape` | `Capability` | this deployment shape grants this capability |
| `reaches` | `reachable_from` | `Capability` | `ReachClass` | this capability reaches this reach class |
| `similar_to` | `similar_to` | `Node` | `Node` | our node is similar to their node |
| `supersedes` | `superseded_by` | `Node` | `Node` | this claim supersedes that one |
| `exposes` | `exposed_by` | `Tool` | `Capability` | this tool exposes this capability |

## Proposed here

**Each one carries a sentence, a different sentence for its inverse, and a stated domain and range**, which is the published rule for extending the set. They are marked as proposed here rather than quoted, in the same way the network's own edge set marks nine of its inverses as proposed there.

| Edge | Reads as | Inverse | Reads as | Domain | Range |
|---|---|---|---|---|---|
| `has_verb` | this capability has the verb read | `verb_of` | read is the verb of these capabilities | `Capability` | `Verb` |
| `acts_on` | this capability acts on files | `acted_on_by` | files are acted on by these capabilities | `Capability` | `ObjectClass` |
| `in_family` | this capability is in the filesystem family | `family_of` | the filesystem family is the family of these capabilities | `Capability` | `Family` |
| `has_undo_class` | this capability has the undo class no | `undo_class_of` | undo class no is the undo class of these capabilities | `Capability` | `UndoClass` |
| `bounded_by` | this granted capability is bounded by this barrier | `bounds` | this barrier bounds these granted capabilities | `GrantedCapability` | `Barrier` |
| `enforced_by` | this barrier is enforced by something above the grant | `enforces` | this enforcer enforces these barriers | `Barrier` | `Enforcer` |
| `authorises` | this mandate authorises this capability | `authorised_by` | this capability is authorised by this mandate | `Mandate` | `Capability` |
| `withholds` | this mandate withholds this capability | `withheld_by` | this capability is withheld by this mandate | `Mandate` | `Capability` |
| `exceeds` | this granted capability exceeds this mandate | `exceeded_by` | this mandate is exceeded by these granted capabilities | `GrantedCapability` | `Mandate` |
| `falls_short_of` | this mandate falls short of this capability it asked for | `unmet_by` | this capability is unmet by this deployment shape | `Mandate` | `Capability` |
| `known_by` | this granted capability is known by observation | `evidences` | observation evidences these granted capabilities | `GrantedCapability` | `EvidenceTier` |
| `has_variant` | this product has this variant | `variant_of` | this variant is a variant of this product | `Product` | `DeploymentShape` |
| `runs_with` | this shape runs with this tool | `run_by` | this tool is run by these shapes | `DeploymentShape` | `Tool` |
| `moves` | this setting moves a capability to this barrier | `moved_by` | this barrier is where these settings move a capability to | `Setting` | `Barrier` |
| `narrows` | this setting narrows this capability | `narrowed_by` | this capability is narrowed by these settings | `Setting` | `Capability` |
| `scoped_by` | this shape is scoped by this vendor scope | `scopes` | this scope scopes these shapes | `DeploymentShape` | `Scope` |
| `permits` | this scope permits this capability | `permitted_by` | this capability is permitted by these scopes | `Scope` | `Capability` |

## The sentence test

**If a path does not read as a sentence in the reader's own language, the edges are wrong** and the model changes rather than the renderer. Every example page ends with a path built from its own data so the test is applied on every build rather than asserted once here:

> deployment shape `claude-code local-confirmations-off` **grants** capability `execute.process.host` which **has_verb** `execute` and **reaches** `host`, **bounded_by** barrier `none`, which **exceeds** mandate `a coding assistant on my machine`, and **has_undo_class** `with-effort`.

[The edges as JSON](../../../data/graph/edges.json) · [The node type formulas](../../../model/graph/formulas/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/graph/edges/index.html)*
