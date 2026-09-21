# The schema

> What is in the published files, what this site added to the data it promoted, and the two rules a consumer and a contributor each have to follow.

*Source: <https://abp.sgit.ai/model/schema/index.html> · site v0.6.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The schema

# The schema

The published vocabulary, file by file, at stable addresses with cross origin access. It is promoted from a game's data pack rather than authored here, and the difference between the two is written down below rather than blurred.

| Address | Type | What is in it |
|---|---|---|
| [`/data/index.json`](../../data/index.json) | `abp/pack/v1` | The manifest. Start here: it names every other file, the counts, and the version to pin. |
| [`/data/capabilities.json`](../../data/capabilities.json) | `abp/capabilities/v1` | The grammar and the 23 primitives, with reach, family, undo class and published gloss. |
| [`/data/barriers.json`](../../data/barriers.json) | `abp/barriers/v1` | The four barriers, weakest first, each with `is_control` and the enforcer test behind it. |
| [`/data/undo-classes.json`](../../data/undo-classes.json) | `abp/undo-classes/v1` | The three undo classes and the ordering rule. |
| [`/data/evidence-tiers.json`](../../data/evidence-tiers.json) | `abp/evidence-tiers/v1` | The seven evidence tiers and which of them this site counts as measured. |
| [`/data/profiles/index.json`](../../data/profiles/index.json) | `abp/profiles-index/v1` | The 16 deployment shapes. A shape is a product in a setting, not a product. |
| [`/data/mandates/index.json`](../../data/mandates/index.json) | `abp/mandates-index/v1` | The 15 starting mandates, one per surface. |
| [`/data/provenance.json`](../../data/provenance.json) | `abp/provenance/v1` | Where every row came from, how many were measured, and the content hash to verify against. |
| [`/data/contributed/riskmandate/`](../../data/contributed/riskmandate/manifest.json) | `abp/contributed-manifest/v1` | Seven deployment shapes contributed by riskmandate.ai: the bytes as fetched, unchanged, with a hash per file and a hash over all of them. Promoted into `profiles/` and `mandates/` with their provenance, and counted beside the map's rows rather than folded into them. |
| [`/data/upstream/`](../../data/upstream/pack.json) | the source pack | The bytes as fetched, unchanged. Anything rendered stays one click from its source bytes. |

## What this site added, and what it did not

**Nothing was renamed.** Capability ids, barrier ids, undo classes and shape ids are the published ones. Two field names changed and the provenance block on each file says which.

**Two fields are this site's own and are marked as such**: `is_control` on a barrier, and the reason behind it. They are a reading of the published wording, not data from the pack.

**One derivation is this site's own**: where two tools in a shape reach the same capability, the grant keeps the **weakest** barrier, because the agent takes the easier path. Each profile's provenance block says so.

**No delta is in the files, and no score is.** A delta is computed every time it is needed. A score is a verdict and it does not live here at all.

## The two rules

> **A consumer pins a version.** Anything that computes from these files states which version it computed against. This is `v0.6.1`, content hash `sha256:d6d4ba40f1fb1f93f66`. A clone that floats against the latest has no reproducible output.

> **A proposal carries evidence.** Every node taken from a third party site carries a source URL, a retrieval timestamp and a content hash. A proposal that changes a capability row without one is an assertion, and this site publishes capability claims about named commercial products.

[The data layer](../../data/index.md) · [The style rules these files follow](https://coding.sgit.ai/)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/schema/index.html)*
