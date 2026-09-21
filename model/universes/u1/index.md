# U1: The grammar

> The grammar, one of the universes an ABP row crosses: owned by abp.sgit.ai, promoted from what-can-it-do.games.sgit.ai and bridged back to it, with its own node types and verbs, sharing only the grammar. Status: live.

*Source: <https://abp.sgit.ai/model/universes/u1/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The grammar

# U1: The grammar

**Owner** abp.sgit.ai, promoted from what-can-it-do.games.sgit.ai and bridged back to it. **Centre of gravity** the primitive. **Smallest node** the word. **Level** down. **Status** **live**.

> Complete for what it is: 10 verbs, 9 object classes, 5 reach classes, 9 families, 3 undo classes, 23 primitives, 33 word nodes with their own addresses. Nothing is added to it by the map except one property, material, and that is deliberate: the grammar is the shared layer that everybody reads by address and nobody forks, so it has to stay small.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **Verb** | `[Verb] := a node that is the -verb_of-> at least one [Capability]` | **yes**, 10 matched |  |
| **ObjectClass** | `[ObjectClass] := a node that is -acted_on_by-> at least one [Capability]` | **yes**, 9 matched |  |
| **ReachClass** | `[ReachClass] := a node that is -reachable_from-> at least one [Capability]` | **yes**, 5 matched |  |
| **Family** | `[Family] := a node that is the -family_of-> at least one [Capability]` | **yes**, 9 matched |  |
| **UndoClass** | `a node that is the -undo_class_of-> at least one [Capability]` | **yes** |  |
| **Capability** | `[Capability] := a node with a -has_verb-> [Verb] and an -acts_on-> [ObjectClass] and a -reaches-> [ReachClass]` | **yes**, 23 matched | Gains one property, material, with the values own, organisation, third_party and mixed: whose material a capability reaches. A property, never a fourth element of the grammar. The default lives here; the override lives on the mandate in U5. |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `has_verb` | this capability has the verb read | `verb_of` | read is the verb of these capabilities | `Capability` | `Verb` | this site | live |
| `acts_on` | this capability acts on files | `acted_on_by` | files are acted on by these capabilities | `Capability` | `ObjectClass` | this site | live |
| `reaches` | this capability reaches this reach class | `reachable_from` | this reach class is reachable from this capability | `Capability` | `ReachClass` | graphs.sgit.ai edge set | live |
| `in_family` | this capability is in the filesystem family | `family_of` | the filesystem family is the family of these capabilities | `Capability` | `Family` | this site | live |
| `has_undo_class` | this capability has the undo class no | `undo_class_of` | undo class no is the undo class of these capabilities | `Capability` | `UndoClass` | this site | live |
| `similar_to` | our node is similar to their node | `similar_to` | symmetric, and partial on purpose | `Node` | `Node` | graphs.sgit.ai anchor nodes | live |

## The edges that cross its boundary today

| Arrives along | From |
|---|---|
| `grants` | [The deployment shape](../../../model/universes/u2/index.md) |
| `authorises` | [The deployer](../../../model/universes/u5/index.md) |
| `withholds` | [The deployer](../../../model/universes/u5/index.md) |
| `falls_short_of` | [The deployer](../../../model/universes/u5/index.md) |
| `exposes` | [The deployment shape](../../../model/universes/u2/index.md) |
| `narrows` | [The deployment shape](../../../model/universes/u2/index.md) |
| `permits` | [The deployment shape](../../../model/universes/u2/index.md) |

## What the map adds here

Two verbs in it, receive and revoke, have nothing under them and are kept as named absences. The grammar is the fixed point of the whole map: what every other universe attaches to by address, and what none of them may change.

[U0: The source bytes](../../../model/universes/u0/index.md) · [All thirteen](../../../model/universes/index.md) · [U2: The deployment shape](../../../model/universes/u2/index.md) · [This universe as JSON](../../../data/universes/u1.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u1/index.html)*
