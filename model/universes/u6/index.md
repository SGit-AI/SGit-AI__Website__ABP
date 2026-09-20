# U6: The derivation

> The derivation, one of the universes an ABP row crosses: owned by the computation, and never a person, with its own node types and verbs, sharing only the grammar. Status: partial.

*Source: <https://abp.sgit.ai/model/universes/u6/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The derivation

# U6: The derivation

**Owner** the computation, and never a person. **Centre of gravity** the pinned input. **Smallest node** one stored record with its inputs, its time and the version of the code that produced it. **Level** across. **Status** partial.

> Nine stored deltas, each pinning the profile version, the mandate version, the pack version, the time and abp.delta/v1, recomputed by the gate on every build. What is missing is the series, the trigger and the crossing. No field on any node here is authored: a Trigger is received, a Crossing is computed, a Series is appended.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **Excess** | `[Excess] := a [GrantedCapability] with NO -authorised_by-> path to the [Mandate] in scope` | **yes**, 53 matched |  |
| **UnboundedExcess** | `[UnboundedExcess] := an [Excess] whose -bounded_by-> [Barrier] is not a [Control]` | **yes**, 48 matched |  |
| **Shortfall** | `[Shortfall] := a [Capability] that a [Mandate] -authorises-> and no [DeploymentShape] in scope -grants->` | **yes**, 2 matched |  |
| **DeltaRecord** | `a node -derived_from-> exactly one [GrantVersion] and exactly one [MandateVersion], -computed_by-> one [Computation], with an excess, an unbounded excess and a shortfall set; no field writable by a person` | not yet | Exists as a file under data/deltas/ and not yet as a node in the graph. |
| **Computation** | `a version of the code: abp.delta/v1 today` | not yet |  |
| **Series** | `the ordered set of [DeltaRecord]s for one shape and one mandate, each -supersedes-> the last` | not yet |  |
| **Trigger** | `an event that -causes_recompute-> of a [Series]: a credential change, a token claims change, an assurance level change, a device compliance change; a new observation in U3; a corrected mandate in U5; a new pack version in U1` | not yet |  |
| **Crossing** | `a [DeltaRecord] whose count -crosses-> a [Threshold] somebody set in advance; a record, never a verdict` | not yet |  |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `exceeds` | this granted capability exceeds this mandate | `exceeded_by` | this mandate is exceeded by these granted capabilities | `GrantedCapability` | `Mandate` | this site | live |
| `derived_from` | this record was derived from these pinned inputs | `derived_into` | these inputs were derived into this record | `DeltaRecord` | `GrantVersion or MandateVersion` | proposed here | proposed |
| `computed_by` | this record was computed by this version of the code | `computed` | this version of the code computed these records | `DeltaRecord` | `Computation` | proposed here | proposed |
| `causes_recompute` | this event caused this series to recompute | `recomputed_on` | this series was recomputed on this event | `Trigger` | `Series` | proposed here | proposed |
| `crosses` | this record crosses this threshold | `crossed_by` | this threshold is crossed by these records | `DeltaRecord` | `Threshold` | proposed here | proposed |

## What the map adds here

The gate's twelfth check, which recomputes every stored delta from its pinned inputs, extends to the series without a new idea: every record in a series recomputes, and a series with a gap in its supersedes chain fails the build. Lab 07's history folder, one entry per recompute, is the live instance of Series and it exists in riskmandate.ai's vault today.

[U5: The deployer](../../../model/universes/u5/index.md) · [All thirteen](../../../model/universes/index.md) · [U7: The projections](../../../model/universes/u7/index.md) · [This universe as JSON](../../../data/universes/u6.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u6/index.html)*
