# U2: The deployment shape

> The deployment shape, one of the universes an ABP row crosses: owned by the vendor's published words, read on a date, with a hash, and never probed, with its own node types and verbs, sharing only the grammar. Status: partial.

*Source: <https://abp.sgit.ai/model/universes/u2/index.html> · site v0.8.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The deployment shape

# U2: The deployment shape

**Owner** the vendor's published words, read on a date, with a hash, and never probed. **Centre of gravity** the setting. **Smallest node** a scope, a flag or a line on a documentation page. **Level** across. **Status** partial.

> Since v0.4.3 the product, the tool a capability is reached through and the setting that moves a barrier are nodes, all derived from data that was already published: the tools in the vendor's words, the reductions the map publishes per capability, and the difference between two variants of one product. Since v0.4.4 seven shapes contributed by riskmandate.ai are promoted here with their provenance, their scopes are nodes in the vendor's own identifier, and material is valued on every row they state it on. Documentation pages and contradictions are carried as data on the profile and are not nodes yet. This is the first universe where the vocabulary is not this site's: a vendor speaks in scopes, tool names, flags, consent screens and administrator settings, and the ABP keeps them in the vendor's words and draws an edge from each to the primitive it exposes.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **Product** | `[Product] := a node that -has_variant-> at least one [DeploymentShape]` | **yes**, 15 matched |  |
| **DeploymentShape** | `[DeploymentShape] := a node that -grants-> at least one [Capability]` | **yes**, 16 matched |  |
| **Tool** | `[Tool] := a node that a [DeploymentShape] -runs_with-> and that -exposes-> at least one [Capability]` | **yes**, 64 matched | One node per shape, in the vendor's words, because what shell (Bash) reaches depends on where it runs. |
| **Scope** | `[Scope] := a node that a [DeploymentShape] is -scoped_by-> and that -permits-> at least one [Capability]` | **yes**, 9 matched | In the vendor's word, never translated. The connector shapes contributed by riskmandate.ai at v0.4.4 reach most of their rows through one. |
| **Setting** | `[Setting] := a node that -narrows-> at least one [Capability] and -moves-> it to at least one [Barrier]` | **yes**, 21 matched | Two kinds, both from published data: the reduction the map publishes per capability, and the setting that distinguishes two variants of one product, derived by diffing their grants. The confirmations flag is the second kind, and it is the path the home page's pair of examples was a sentence about. |
| **DocumentationPage** | `a [SourceFile] in U0 that a [Shape], [Tool], [Scope] or [Setting] is -documented_at->` | not yet |  |
| **Contradiction** | `a node where an -advertises-> claim and a -scoped_by-> scope on the same [Product] disagree, both quoted, both dated, published unresolved` | not yet | riskmandate.ai's Lab 01 holds four of these with verbatim quotes and URLs. |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `has_variant` | this product has this variant | `variant_of` | this variant is a variant of this product | `Product` | `DeploymentShape` | proposed here | live |
| `runs_with` | this shape runs with this tool | `run_by` | this tool is run by these shapes | `DeploymentShape` | `Tool` | proposed here | live |
| `exposes` | this tool exposes this capability | `exposed_by` | this capability is exposed by these tools | `Tool` | `Capability` | graphs.sgit.ai edge set | live |
| `scoped_by` | this shape is scoped by this vendor scope | `scopes` | this scope scopes these shapes | `DeploymentShape` | `Scope` | proposed here | live |
| `permits` | this scope permits this capability | `permitted_by` | this capability is permitted by these scopes | `Scope` | `Capability` | proposed here | live |
| `moves` | this setting moves a capability to this barrier | `moved_by` | this barrier is where these settings move a capability to | `Setting` | `Barrier` | proposed here | live |
| `narrows` | this setting narrows this capability | `narrowed_by` | this capability is narrowed by these settings | `Setting` | `Capability` | proposed here | live |
| `documented_at` | this tool is documented at this page, read on this date | `documents` | this page documents these tools | `Shape, Tool, Scope or Setting` | `DocumentationPage` | proposed here | proposed |
| `advertises` | this product's page advertises this capability | `advertised_by` | this capability is advertised by these products | `Product` | `Capability` | proposed here | proposed |
| `contradicts` | this advertised claim contradicts this granted scope | `contradicted_by` | this scope is contradicted by this claim | `Contradiction` | `Scope or Capability` | proposed here | proposed |
| `grants` | this deployment shape grants this capability | `granted_by` | this capability is granted by this deployment shape | `DeploymentShape` | `Capability` | graphs.sgit.ai edge set | live |

## The edges that cross its boundary today

| Leaves along | Into |
|---|---|
| `grants` | [The grammar](../../../model/universes/u1/index.md) |
| `exposes` | [The grammar](../../../model/universes/u1/index.md) |
| `moves` | [The enforcement](../../../model/universes/u4/index.md) |
| `narrows` | [The grammar](../../../model/universes/u1/index.md) |
| `permits` | [The grammar](../../../model/universes/u1/index.md) |

## What the map adds here

The position on a connector that is present and switched off, which is the most common state in any real estate. The enforcer test decides it: if the switch is inside the agent's grant, the capability is in the grant at barrier setting, one click away, and the label counts it; if the switch is outside the grant, the capability is not in the grant, and the estate in U9 records it as one setting away. No new barrier kind and no new label field. The seven shapes riskmandate.ai has already built are layer one facts and belong at this address, through an intake path that carries their provenance.

[U1: The grammar](../../../model/universes/u1/index.md) · [All thirteen](../../../model/universes/index.md) · [U3: The grant and its evidence](../../../model/universes/u3/index.md) · [This universe as JSON](../../../data/universes/u2.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u2/index.html)*
