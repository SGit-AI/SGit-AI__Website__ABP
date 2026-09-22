# v0.4.3: The home page has argued about one setting since v0.1.0, and now the build walks it

> A product, a tool and a setting became node types with formulas, derived from data the site already held. The setting that distinguishes confirmations on from confirmations off was found by diffing two grants, and whose material a capability reaches was declared without being guessed.

*Source: <https://abp.sgit.ai/articles/the-confirmations-flag-as-a-path/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Articles](../../articles/index.md) / v0.4.3

# v0.4.3: The home page has argued about one setting since v0.1.0, and now the build walks it

A product, a tool and a setting became node types with formulas, derived from data the site already held. The setting that distinguishes confirmations on from confirmations off was found by diffing two grants, and whose material a capability reaches was declared without being guessed.

> **This is the article for release v0.4.3, published 20 September 2026.** Every release of this site gets one, and it explains what that release changed and why rather than restating [v0.4.3's own release record](../../versions/v0.4.3/index.md). It is release 7 of 13 on this site. Every screenshot below was captured from a checkout of the `v0.4.3` tag, so it shows the site as it stood at that release and not as it stands today. Read on to [v0.4.4](../../articles/seven-shapes-somebody-else-measured/index.md), or back to [v0.4.2](../../articles/the-fact-diff-reads-the-published-page/index.md).

## An argument that had been a sentence since the first release

The clearest demonstration this site has is a pair of example pages: the same coding agent, the same machine, the same account, with the confirmation prompt on in one and off in the other. **The grant does not change. The mandate does not change. The delta does not change. One barrier moves.**

For three releases that was a paragraph. A reader had to take it on trust that something in the data connected the two shapes, because nothing did: a shape carried its tools as strings and carried nothing at all about what distinguished one variant of a product from another.

*[A figure here in the page: the product Claude Code has two variants, local-default and local-confirmations-off. The setting that distinguishes them is a node derived by diffing their grants. It narrows the capability execute.process.host and moves it between the barriers setting and none. The grant, the mandate and the delta are identical in both variants: one barrier moves and not one number on the label]*

## Three node types, and nothing typed in

This release adds a product, a tool and a setting as node types with formulas the build walks. **All three are derived from data the site already held.**

| Type | Where it comes from | Matched |
|---|---|---|
| `Product` | the two segments of a shape id that are not the variant, so two shapes with the same product are the same thing in a different setting | 8 |
| `Tool` | the tools a profile already listed, in the vendor's own words, one node per shape because what `shell (Bash)` reaches depends on where it runs | 17 |
| `Setting` | twenty from the reductions the capability map publishes per capability, and one from diffing the grants of two variants of one product | 21 |

![The deployment shape universe page listing its node types, which exist and which are still needed](../../assets/articles/v043-u2-types.png)

*The universe page reports its own state: three types now walked on every build with their counts, and four the world still needs. A status of partial is a claim the gate checks rather than a hedge. (abp.sgit.ai at v0.4.3, captured 20 September 2026 from a checkout of the v0.4.3 tag.)*

## The setting nobody wrote

The interesting node of the three is the last one. **The setting that distinguishes confirmations on from confirmations off was not authored.** The build takes the two variants of one product, diffs their grants, and whatever barrier moved between them is what the setting moves.

For this pair exactly one capability moves: `execute.process.host` sits at a setting in one variant and at nothing in the other. So the node carries one `narrows` edge to that capability and two `moves` edges, one to each barrier. **The home page's paragraph is now a path with two nodes and two edges in it**, walked on every build, and it would fail the build if it stopped being true.

![A capability page showing the published reduction that would move it to the fourth barrier, now also a node](../../assets/articles/v043-setting-node.png)

*The other twenty settings come from the capability map's published reductions: for each capability, the specific configuration that narrows it, what it costs, and the barrier it reaches afterwards. This is a published reduction, not a recommendation, because whether it is worth doing depends on assets this document does not hold. (abp.sgit.ai at v0.4.3, captured 20 September 2026 from a checkout of the v0.4.3 tag.)*

## Whose material, declared without being guessed

The other half of the release answers the first of three requests a consumer of this data published against this site. **Reach answers how far a capability goes. It does not answer whose material it touches.**

`read.message.tenant` says the agent can read a mailbox. It does not say the mailbox is full of other people's correspondence, and no setting any of the four vendors documents makes a mailbox anything else.

| Value | What it means |
|---|---|
| `own` | the deployer's own material |
| `organisation` | the deployer's organisation's material |
| `third_party` | other people's material |
| `mixed` | other people's material mixed with the deployer's, and no setting the vendor documents makes it otherwise |

> **A property on a granted row, never a fourth element of the grammar.** A fourth element multiplies the primitives and the vocabulary has to stay readable by address. And the nine shapes promoted from the capability map do not state it, so their rows say nothing rather than guessing: the field is null and the gate refuses any value outside the four. The first rows to carry a value arrived in the next release, from somebody who had read the vendor pages and written it down.

**A grant you hold over other people's material is not a grant you may pass on.** That sentence is in the foundation document and it had nowhere to live in the data until this release.

[The deployment shape universe](../../model/universes/u2/index.md) &#183; [The capability grammar](../../model/capabilities/index.md) &#183; [v0.4.3's own release record](../../versions/v0.4.3/index.md)

## Read the sequence

| Direction | The release |
|---|---|
| **Older** | [v0.4.2: The fact diff was named as a blocker on four consecutive days, and it reads the published page](../../articles/the-fact-diff-reads-the-published-page/index.md) |
| **Newer** | [v0.4.4: Seven deployment shapes somebody else measured, promoted with their provenance intact](../../articles/seven-shapes-somebody-else-measured/index.md) |
| **All of them** | [One article per release](../../articles/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/articles/the-confirmations-flag-as-a-path/index.html)*
