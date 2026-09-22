# U3: The grant and its evidence

> The grant and its evidence, one of the universes an ABP row crosses: owned by whoever observed, or the documentation that was read, with its own node types and verbs, sharing only the grammar. Status: one-edge.

*Source: <https://abp.sgit.ai/model/universes/u3/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The grant and its evidence

# U3: The grant and its evidence

**Owner** whoever observed, or the documentation that was read. **Centre of gravity** the observation. **Smallest node** one probe result on one instance on one date. **Level** across. **Status** one edge deep.

> Every granted row carries an evidence tier and the tier is a node. Nothing is behind the tier: no observation, no probe run, no date. The GrantedCapability node stays what it is, the node that carries the barrier, because the barrier is a property of a capability in a shape and never of the capability itself.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **GrantedCapability** | `[GrantedCapability] := a [Capability] with an inbound -grants-> from a [DeploymentShape], carrying a -bounded_by-> [Barrier] and a -known_by-> [EvidenceTier]` | **yes**, 118 matched |  |
| **EvidenceTier** | `a node that -evidences-> at least one [GrantedCapability]` | **yes** |  |
| **Observation** | `a node -observed_on-> an [Instance] on a date, -backed_by-> an [EvidenceFile], that -evidences-> at least one [GrantedCapability]` | not yet |  |
| **Instance** | `a running deployment of a [DeploymentShape] that somebody was entitled to run` | not yet | Named so that every observation states whose system it was and that we were entitled to run it. Never probe anybody's system. |
| **SelfReport** | `an [Observation] made by the agent about its own grant, from inside the shape; it stays a claim until a log held outside the agent agrees` | not yet |  |
| **EvidenceFile** | `a [SourceFile] in U0` | not yet |  |
| **Refusal** | `an [Observation] that a probe was stopped before it ran, by something above the session; a barrier the grant has no row for` | not yet |  |
| **Measured** | `a [GrantedCapability] with a -measured_by-> path to an [Observation] whose [Instance] was one we were entitled to run` | not yet | Measured today is a headline, 21 of 99, counted from the observed tier. With observations as nodes it becomes a query run on every build, per row, with a date. |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `known_by` | this granted capability is known by observation | `evidences` | observation evidences these granted capabilities | `GrantedCapability` | `EvidenceTier` | this site | live |
| `bounded_by` | this granted capability is bounded by this barrier | `bounds` | this barrier bounds these granted capabilities | `GrantedCapability` | `Barrier` | this site | live |
| `observed_on` | this observation was made on this instance | `hosted` | this instance hosted these observations | `Observation` | `Instance` | graphs.sgit.ai edge set | proposed |
| `backed_by` | this observation is backed by this file | `backs` | this file backs these observations | `Observation` | `EvidenceFile` | graphs.sgit.ai edge set | proposed |
| `measured_by` | this row was measured by this observation | `measures` | this observation measures these rows | `GrantedCapability` | `Observation` | graphs.sgit.ai edge set | proposed |
| `contradicts` | this observation contradicts that one | `contradicted_by` | that observation is contradicted by this one | `Observation` | `Observation` | proposed here | proposed |
| `stopped_by` | this probe was stopped by this enforcer | `stopped` | this enforcer stopped these probes | `Refusal` | `Enforcer` | proposed here | proposed |

## The edges that cross its boundary today

| Leaves along | Into |
|---|---|
| `bounded_by` | [The enforcement](../../../model/universes/u4/index.md) |
| `exceeds` | [The deployer](../../../model/universes/u5/index.md) |

## What the map adds here

Lab 07's grant check, eleven of fifteen rows seen present in ordinary work and two probe batches refused by the platform's own classifier, is a SelfReport and two Refusals, and both node types are named here because that check has already happened and had nowhere to go. The calibration loop on the delta page becomes an edge somebody adds rather than a paragraph.

[U2: The deployment shape](../../../model/universes/u2/index.md) · [All thirteen](../../../model/universes/index.md) · [U4: The enforcement](../../../model/universes/u4/index.md) · [This universe as JSON](../../../data/universes/u3.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u3/index.html)*
