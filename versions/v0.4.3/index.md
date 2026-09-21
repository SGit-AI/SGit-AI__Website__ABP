# v0.4.3: the product, the tool and the setting become nodes, derived from data already published, and whose material is declared on the grammar

> The deployment shape universe, as far as published data takes it. A shape used to carry its tools as strings and nothing about what distinguishes one variant of a product from another. Now a product is a node with its variants, every tool a shape runs with is a node that exposes...

*Source: <https://abp.sgit.ai/versions/v0.4.3/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.4.3

# v0.4.3: the product, the tool and the setting become nodes, derived from data already published, and whose material is declared on the grammar

The deployment shape universe, as far as published data takes it. A shape used to carry its tools as strings and nothing about what distinguishes one variant of a product from another. Now a product is a node with its variants, every tool a shape runs with is a node that exposes the capabilities it reaches, and a setting is a node that narrows a capability and moves it to a barrier. All three are derived from data this site already held: the tools in the vendor's words, the reductions the map publishes per capability, and the difference between two variants of one product, found by diffing their grants. The confirmations flag, which the home page has described in a sentence since v0.1.0, is now a path the build walks. The material property riskmandate.ai asked for is declared on the grammar with its four values, placed on the granted row, and left null on the nine promoted shapes rather than guessed.

| Field | Value |
|---|---|
| Version | `v0.4.3` |
| Date | 2026-09-20 |
| Commit | **`git rev-list -n 1 v0.4.3`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.4.3:`. The hash is not written into [`versions/v0.4.3.json`](../../versions/v0.4.3.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.4.3.json`](../../versions/v0.4.3.json) |

## What changed

- Three node type formulas: [Product] has at least one variant; [Tool] is run by a shape and exposes at least one capability; [Setting] narrows at least one capability and moves it to at least one barrier. Walked on every build: 8 products, 17 tools and 21 settings matched at this release.
- Five edges: has_variant and variant_of, runs_with and run_by, exposes and exposed_by (reused from the network's published set), moves and moved_by, narrows and narrowed_by. Three of them cross a universe boundary and the universes index lists them: exposes and narrows into the grammar, moves into the enforcement.
- Twenty settings come from the reductions the map publishes, one per capability that has one, each carrying what it costs and the barrier it moves the capability to. One comes from diffing the two variants of the coding agent: the setting that distinguishes confirmations on from confirmations off narrows execute.process.host and moves it between setting and none. That is the argument of the home page as a path rather than a paragraph.
- A tool is one node per shape, in the vendor's words, because the same string in two shapes is two exposures: what shell (Bash) reaches depends on where it runs.
- data/capabilities.json declares material: whose material a capability reaches, with the values own, organisation, third_party and mixed, placed on the granted row, marked as this site's own and not the pack's, proposed by riskmandate.ai. Every granted row now carries the field; on the nine promoted shapes it is null, and the gate refuses any value outside the four.
- The capability pages say that the published reduction is now a setting node, and the deployment shape universe's page lists the three types as existing with their counts. Its status stays partial: scopes, documentation pages and contradictions are not nodes yet.

## What it was built against

- The v0.4.0 brief, for the deployment shape universe's node types and verbs, of which this release builds the three that published data can support.
- The reductions in the promoted pack, retrieved 11 September 2026, for twenty of the twenty one settings.
- riskmandate.ai's Lab 03 of 12 September 2026, for the material property and the lean towards the vocabulary with a per policy override, which this release places on the granted row because the vaults riskmandate.ai has since built put it there.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.4.3/index.html)*
