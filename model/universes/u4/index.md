# U4: The enforcement

> The enforcement, one of the universes an ABP row crosses: owned by whoever set the control: the vendor, the platform, the deployer or nobody, with its own node types and verbs, sharing only the grammar. Status: one-edge.

*Source: <https://abp.sgit.ai/model/universes/u4/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The enforcement

# U4: The enforcement

**Owner** whoever set the control: the vendor, the platform, the deployer or nobody. **Centre of gravity** the enforcer. **Smallest node** one configuration line at one layer, set by one party, on one date. **Level** across. **Status** one edge deep.

> Four barriers, three enforcers, one Control formula that the gate walks on every build. The formula is the most important thing on the site and it lands in a world with three nodes. The dev brief of 11 September on the prohibition's two lives wrote most of this universe's vocabulary and it was never made into nodes.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **Barrier** | `[Barrier] := a node that -bounds-> at least one [GrantedCapability]` | **yes**, 4 matched |  |
| **Enforcer** | `a node that -enforces-> at least one [Barrier], -set_by-> a [Party], -at_layer-> a [Layer]` | **yes** | Three today, with only inside_the_grant on each. Party and Layer are the change. |
| **Control** | `[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include` | **yes**, 1 matched | Does not change, and gains a second reading: with Party and removable_by as nodes and edges, does not include becomes a path, walked one universe further. |
| **Layer** | `one of prompt, tool schema, client rule, gateway, sandbox; a node a [Layer] is -above-> or -below-> another` | not yet |  |
| **Party** | `the vendor, the platform, the deployer, the administrator, the agent's own account, or nobody` | not yet |  |
| **EvidencedControl** | `a [Control] whose [Enforcer] is -backed_by-> an [Observation] in U3` | not yet | The regulated customer's stricter formula from the three layers page, now writable beside ours without touching ours. |
| **CompiledRule** | `a node that a [Prohibition] in U7 -compiles_to->, in a named target language, that -passes-> a shadowed permit analysis` | not yet |  |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `enforced_by` | this barrier is enforced by something above the grant | `enforces` | this enforcer enforces these barriers | `Barrier` | `Enforcer` | this site | live |
| `set_by` | this enforcer was set by this party | `sets` | this party sets these enforcers | `Enforcer` | `Party` | proposed here | proposed |
| `at_layer` | this enforcer sits at the gateway layer | `layer_of` | the gateway layer is the layer of these enforcers | `Enforcer` | `Layer` | proposed here | proposed |
| `removable_by` | this enforcer can be removed by this party | `can_remove` | this party can remove these enforcers | `Enforcer` | `Party` | proposed here; the enforcer test as an edge | proposed |
| `expires_on` | this enforcer is good until this date, or has no stated expiry | `expiry_of` | this date is the expiry of these enforcers | `Enforcer` | `Date` | proposed here | proposed |
| `compiles_to` | this prohibition compiles to this rule | `compiled_from` | this rule is compiled from this prohibition | `Prohibition` | `CompiledRule` | proposed here | proposed |
| `defeated_by` | this barrier was defeated in this observation | `defeats` | this observation defeats this barrier | `Barrier` | `Observation` | graphs.sgit.ai edge set | proposed |

## The edges that cross its boundary today

| Arrives along | From |
|---|---|
| `bounded_by` | [The grant and its evidence](../../../model/universes/u3/index.md) |
| `moves` | [The deployment shape](../../../model/universes/u2/index.md) |

## What the map adds here

Lab 06 added the property the 11 September brief did not have: a barrier is perishable, and a classifier that refuses a probe today is a barrier with no row and no expiry. The five layers become nodes so that the leaflet's rightmost column, the layer a control would sit at, stops being a string.

[U3: The grant and its evidence](../../../model/universes/u3/index.md) · [All thirteen](../../../model/universes/index.md) · [U5: The deployer](../../../model/universes/u5/index.md) · [This universe as JSON](../../../data/universes/u4.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u4/index.html)*
