# U7: The projections

> The projections, one of the universes an ABP row crosses: owned by the renderer, and the fact diff that has to check it, with its own node types and verbs, sharing only the grammar. Status: partial.

*Source: <https://abp.sgit.ai/model/universes/u7/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The projections

# U7: The projections

**Owner** the renderer, and the fact diff that has to check it. **Centre of gravity** the fact set. **Smallest node** one rendered sentence that traces to one node. **Level** across. **Status** partial.

> The label, the leaflet and the prohibitions exist and are generated from one call. AGENTS.md, SKILL.md and LICENCE-TO-OPERATE.md exist in riskmandate.ai's vaults. Since v0.4.2 the fact set is a file per stored delta under data/facts/ and the fact diff runs in the release gate: it parses the label, the leaflet, the prohibitions and the figure back out of each example's published twin and fails the build on a single leaf assertion that differs. Neither is a node in the graph yet, which is why the status stays partial. This is the universe where altitude in the 20 August sense lives: every projection renders the same fact set for a different reader, and the diff over leaf assertions between any two must be empty.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **FactSet** | `the leaf assertions of one [DeltaRecord]: this shape grants this capability at this barrier with this undo class; this mandate authorises these; therefore this excess. Computed, never authored` | not yet | Exists as a file per stored delta under data/facts/ since v0.4.2, and not yet as a node. |
| **Projection** | `a node -projects-> one [FactSet], -rendered_for-> one [Audience], with every sentence -traces_to-> a node` | not yet |  |
| **Audience** | `a decision maker, an engineer, an auditor, an underwriter, an agent; the altitude axis` | not yet |  |
| **Label** | `a [Projection] with nine fields and no score` | not yet |  |
| **Leaflet** | `a [Projection] with every row` | not yet |  |
| **Prohibition** | `a [Projection] of one [Excess] row as a sentence, carrying its barrier today and the layer a control would sit at; -compiles_to-> a [CompiledRule] in U4` | not yet |  |
| **AgentFile** | `a [Projection] -rendered_for-> the agent itself: AGENTS.md, SKILL.md; honest on its own face that it is a rule in prose, the second barrier, and bounds nothing` | not yet |  |
| **InterchangeDocument** | `a [Projection] in the W3C vocabulary through the agent profile; a rule somebody wrote down until U4 compiles it` | not yet |  |
| **FactDiff** | `a node that -compares-> two [Projection]s over their [FactSet]s and is empty or names the row` | not yet | Runs as the release gate's fifteenth check since v0.4.2, over the published twin of every example, and is not yet a node. |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `projects` | this rendering projects this fact set | `projected_as` | this fact set is projected as these renderings | `Projection` | `FactSet` | proposed here | proposed |
| `rendered_for` | this rendering is for this reader | `reads` | this reader reads these renderings | `Projection` | `Audience` | proposed here | proposed |
| `traces_to` | this sentence traces to this node | `rendered_in` | this node is rendered in these sentences | `Sentence` | `Node` | proposed here | proposed |
| `compares` | this diff compares these two renderings | `compared_by` | these renderings are compared by this diff | `FactDiff` | `Projection` | proposed here | proposed |

## What the map adds here

With FactSet as a node and every Projection carrying a projects edge to it, the diff is a set comparison over one node's edges, and the gate can run it on every build across the label, the leaflet, the prohibitions and the agent files. The multi audience promise on the store becomes printable the release this ships.

[U6: The derivation](../../../model/universes/u6/index.md) · [All thirteen](../../../model/universes/index.md) · [U8: The licence, the acceptance and the risk](../../../model/universes/u8/index.md) · [This universe as JSON](../../../data/universes/u7.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u7/index.html)*
