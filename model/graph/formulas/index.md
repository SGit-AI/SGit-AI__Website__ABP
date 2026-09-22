# The node type formulas

> A node type is a required pattern of typed, directed paths that a node either matches or does not. Not a label somebody applied. Run against the graph on every build.

*Source: <https://abp.sgit.ai/model/graph/formulas/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The graph](../../../model/graph/index.md) / The formulas

# The node type formulas

**The content of a node does not decide its type. Its paths do.** Two nodes with identical text can be different types because their edges differ, and the clearest case in this model is that the same capability is excess on one deployment and authorised on the next, with nothing about the capability changed.

## The formulas, and what matched when this page was built

| Type | What it is | The formula | Matched |
|---|---|---|---|
| **Verb** | The action half of a primitive, on its own. | `[Verb] := a node that is the -verb_of-> at least one [Capability]` | 10 |
| **ObjectClass** | What a primitive acts on. | `[ObjectClass] := a node that is -acted_on_by-> at least one [Capability]` | 9 |
| **ReachClass** | How far a primitive reaches. | `[ReachClass] := a node that is -reachable_from-> at least one [Capability]` | 5 |
| **Family** | A grouping of primitives for a reader. | `[Family] := a node that is the -family_of-> at least one [Capability]` | 9 |
| **Capability** | A primitive in the grammar. | `[Capability] := a node with a -has_verb-> [Verb] and an -acts_on-> [ObjectClass] and a -reaches-> [ReachClass]` | 23 |
| **DeploymentShape** | A product in a setting. | `[DeploymentShape] := a node that -grants-> at least one [Capability]` | 17 |
| **GrantedCapability** | A capability in a particular shape's grant. | `[GrantedCapability] := a [Capability] with an inbound -grants-> from a [DeploymentShape], carrying a -bounded_by-> [Barrier] and a -known_by-> [EvidenceTier]` | 123 |
| **Barrier** | What stands between the agent and a capability. | `[Barrier] := a node that -bounds-> at least one [GrantedCapability]` | 4 |
| **Control** | A barrier that actually bounds anything. | `[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include` | 1 |
| **Mandate** | What a deployer authorised. | `[Mandate] := a node that -authorises-> at least one [Capability]` | 16 |
| **Excess** | The finding. | `[Excess] := a [GrantedCapability] with NO -authorised_by-> path to the [Mandate] in scope` | 82 |
| **UnboundedExcess** | The business case. | `[UnboundedExcess] := an [Excess] whose -bounded_by-> [Barrier] is not a [Control]` | 64 |
| **Shortfall** | Asked for and cannot. | `[Shortfall] := a [Capability] that a [Mandate] -authorises-> and no [DeploymentShape] in scope -grants->` | 2 |
| **Product** | A vendor's product, which is not a shape. | `[Product] := a node that -has_variant-> at least one [DeploymentShape]` | 15 |
| **Tool** | What a shape reaches a capability through. | `[Tool] := a node that a [DeploymentShape] -runs_with-> and that -exposes-> at least one [Capability]` | 76 |
| **Scope** | A vendor's own identifier for what a consent permits. | `[Scope] := a node that a [DeploymentShape] is -scoped_by-> and that -permits-> at least one [Capability]` | 9 |
| **Setting** | What moves a barrier. | `[Setting] := a node that -narrows-> at least one [Capability] and -moves-> it to at least one [Barrier]` | 22 |

## The one that carries the argument

> **`[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include.`** Until v0.3.0 this was `is_control: true` on a barrier, which is a label somebody applied. It is now a path the build walks, and **exactly one of the four barriers matches**. The release gate fails if that stops being true, because every page on this site is written against it.

| Barrier | Enforced by | Inside the grant | A control |
|---|---|---|---|
| `none` | - | - | no |
| `expectation` | the agent reading it | yes | no |
| `setting` | the agent's own account | yes | no |
| `boundary` | something above the grant | no | **yes** |

## Judgment does not disappear

That is the usual objection and it deserves a direct answer. **Somebody still decided that a control must be enforced from outside the grant.** What changes is where that decision lives: out of a classifier's head and into a formula that is visible, versioned, inspectable and arguable. **You can now disagree with a classification by pointing at a line**, which you could not do before.

> **A score is not a node and there is no edge to one.** Not a rating, not a risk level, not a severity. Adding one would not be a modelling choice, it would be a verdict, and the same ABP is dangerous in one deployment and harmless in the next. The risk work above this holds the assets, and that is where a score can exist.

[The formulas as JSON](../../../data/graph/node-types.json) · [Why classification is a query](https://graphs.sgit.ai/v1/depth/index.html)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/graph/formulas/index.html)*
