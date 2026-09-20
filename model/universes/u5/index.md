# U5: The deployer

> The deployer, one of the universes an ABP row crosses: owned by the deployer, in their own words, and the named person who will correct the draft, with its own node types and verbs, sharing only the grammar. Status: partial.

*Source: <https://abp.sgit.ai/model/universes/u5/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The deployer

# U5: The deployer

**Owner** the deployer, in their own words, and the named person who will correct the draft. **Centre of gravity** the job. **Smallest node** one sentence somebody said about one capability on one date. **Level** across. **Status** partial.

> Eight starting mandates exist, each a want list, a refuse list and an unstated list over the 23 primitives, with a description and per capability notes in prose. The person, the job, the purpose and whose material are not nodes. This is the universe where customisation and consolidation are one mechanism: a customer's mandate is written in their vocabulary and attaches to the grammar by authorises and withholds and to nothing else.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **Mandate** | `[Mandate] := a node that -authorises-> at least one [Capability]` | **yes**, 8 matched |  |
| **Deployer** | `an [Organisation] or [Person] that -issued-> at least one [Mandate]` | not yet |  |
| **Owner** | `a [Person] that -corrected-> or -signed-> a [Mandate]; never a team and never a function` | not yet |  |
| **Job** | `a node a [Mandate] -is_for->, in the deployer's words: draft the reply, fix the build` | not yet |  |
| **Expectation** | `one row of a [Mandate]: a [Capability] with a stance of wanted, refused or unstated, -said_by-> a [Person] on a date` | not yet |  |
| **MaterialOverride** | `a node on a [Mandate] that -overrides-> the material value of one [Capability] from U1, with its authority recorded and the default kept visible` | not yet |  |
| **Correction** | `a [Mandate] that -supersedes-> an earlier one; the sale, on riskmandate.ai's own account` | not yet |  |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `authorises` | this mandate authorises this capability | `authorised_by` | this capability is authorised by this mandate | `Mandate` | `Capability` | this site | live |
| `withholds` | this mandate withholds this capability | `withheld_by` | this capability is withheld by this mandate | `Mandate` | `Capability` | this site | live |
| `falls_short_of` | this mandate falls short of this capability it asked for | `unmet_by` | this capability is unmet by this deployment shape | `Mandate` | `Capability` | this site | live |
| `is_for` | this mandate is for this job | `served_by` | this job is served by these mandates | `Mandate` | `Job` | proposed here | proposed |
| `issued` | this deployer issued this mandate | `issued_by` | this mandate was issued by this deployer | `Deployer` | `Mandate` | proposed here | proposed |
| `said_by` | this expectation was said by this person on this date | `said` | this person said these expectations | `Expectation` | `Person` | proposed here | proposed |
| `corrected` | this person corrected this mandate | `corrected_by` | this mandate was corrected by this person | `Person` | `Mandate` | proposed here | proposed |
| `overrides` | this mandate overrides whose material this capability reaches | `overridden_by` | this capability's material is overridden by this mandate | `MaterialOverride` | `Capability` | proposed here | proposed |
| `supersedes` | this claim supersedes that one | `superseded_by` | that claim is superseded by this one | `Node` | `Node` | graphs.sgit.ai, supersede never delete | live |

## The edges that cross its boundary today

| Leaves along | Into |
|---|---|
| `authorises` | [The grammar](../../../model/universes/u1/index.md) |
| `withholds` | [The grammar](../../../model/universes/u1/index.md) |
| `falls_short_of` | [The grammar](../../../model/universes/u1/index.md) |

| Arrives along | From |
|---|---|
| `exceeds` | [The grant and its evidence](../../../model/universes/u3/index.md) |

## What the map adds here

The interchange form lives here and nowhere else. The W3C rights expression vocabulary, with permission, prohibition and duty, constraints, a conflict strategy in which prohibitions win, and inheritance, is a projection of U5 and U6 written out in U7, and it is never claimed to enforce anything, because enforcement is U4. An ODRL Policy is a scoped term in this universe's lexicon; the instrument with bands, a ceiling and a premium on the licence to operate demonstration is a scoped term in U8's; the behaviour policy is the root.

[U4: The enforcement](../../../model/universes/u4/index.md) · [All thirteen](../../../model/universes/index.md) · [U6: The derivation](../../../model/universes/u6/index.md) · [This universe as JSON](../../../data/universes/u5.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u5/index.html)*
