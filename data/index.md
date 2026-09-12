# The data

> The capabilities, barriers, undo classes, deployment shapes and mandates an ABP is written in, as JSON at stable addresses with cross origin access, with the source bytes they were promoted from.

*Source: <https://abp.sgit.ai/data/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The data

# The data

The published vocabulary of the Agent Behaviour Policy: **23 capabilities**, **4 barriers**, **3 undo classes**, **9 deployment shapes** and **8 starting mandates**, at stable addresses with cross origin access.

> **Start at [`/data/index.json`](../data/index.json).** It names every other file, carries the counts and states the version to pin. This is `v0.3.0`.

## Where it came from, and what that obliges

**This site did not author this ontology.** It was published as a data pack the game at [what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai/map/index.html) reads, and the job here was to promote it out of a game's internals into a published schema the network can cite. Nothing was renamed.

| Field | Value |
|---|---|
| Source | `https://what-can-it-do.games.sgit.ai/data/` |
| Retrieved | `2026-09-11T13:00:37Z` |
| Pack version | `v0.8.0` |
| Content hash | `sha256:d6d4ba40f1fb1f93f660687e4787ac10c2e1835efeb3929a4c8ad62cee8897ef` |
| Files hashed | 27 |
| Licence | CC BY 4.0 |

**The bytes as fetched are served unchanged** under [`/data/upstream/`](../data/upstream/pack.json), and the build recomputes the hash on every run and refuses to write if it disagrees. Anything rendered stays one click from its source bytes.

## How much of it was measured

**21 of 99 capability rows** were measured, meaning seen directly on the thing itself. The other 78 were derived from what the deployment architecturally is, or from the vendor's published documentation. By tier: `derived` 45, `observed` 21, `documented` 13, `inferred` 1, `self-reported` 1.

> **A precision the headline loses.** A row at the `observed` tier: seen directly, on the thing itself. No row in this pack is at the `measured` tier, which the pack defines as a dated probe with an evidence file. The published headline of 21 of 99 counts the `observed` rows, and so does this site.

**No row here was obtained by probing anybody's system. A row is measured only from a system we are entitled to run, or from the vendor's own published documentation.**

## The files

| Address | What is in it |
|---|---|
| [`/data/capabilities.json`](../data/capabilities.json) | capabilities |
| [`/data/barriers.json`](../data/barriers.json) | barriers |
| [`/data/undo-classes.json`](../data/undo-classes.json) | undo classes |
| [`/data/evidence-tiers.json`](../data/evidence-tiers.json) | evidence tiers |
| [`/data/profiles/index.json`](../data/profiles/index.json) | profiles |
| [`/data/mandates/index.json`](../data/mandates/index.json) | mandates |
| [`/data/deltas/index.json`](../data/deltas/index.json) | deltas |
| [`/data/graph/index.json`](../data/graph/index.json) | graph |
| [`/data/lexicon/index.json`](../data/lexicon/index.json) | lexicon |
| [`/data/bridges/index.json`](../data/bridges/index.json) | bridges |
| [`/data/provenance.json`](../data/provenance.json) | provenance |
| [`/data/upstream/pack.json`](../data/upstream/pack.json) | upstream |

## The deltas, which are here on purpose

**9 stored deltas**, one per deployment shape and mandate pair, at [`/data/deltas/index.json`](../data/deltas/index.json). Derived and never authored. Stored under deltas/, each record pinning the version of both inputs and the time and code version that produced it. No field in one is writable by a person: change a grant or a mandate and recompute. Corrected from `computed and never stored` on 11 September 2026; the brief is in /docs/briefs/. [What that means and why it changed](../model/delta/index.md).

> **The release gate recomputes every stored delta on every build** from the profile and the mandate it names, and fails on a single row of disagreement. That is how a machine holds `never authored': the rule forbids the act rather than the artefact, and a hand edited delta is a fiction nothing downstream could detect.

## What is deliberately not in these files

| Not here | Why |
|---|---|
| **A score** | There is no score, rating, traffic light, risk level or severity in this pack or anywhere on this site. A score is a verdict and the ABP describes without judging. |
| **A consequence** | A delta crossing a threshold is a record. What follows from it is a policy somebody set in advance, and it is not in this pack. |

## Proposing a change

**The data files are the shared facts and they live in this repository so that people can propose changes.** The site and its data are the library; a cloned vault is the instance. Two rules come with that.

**A proposal carries evidence.** Every node taken from a third party site carries a source URL, a retrieval timestamp and a content hash. A proposal that changes a capability row without one is an assertion, and the release gate refuses it.

**A consumer pins a version.** Anything that computes from these files states which version it computed against. A clone that floats against the latest has no reproducible output.

> **One transform happens between these files and the pages.** The source prose carries em dashes, en dashes and curly quotes because it was written elsewhere, and this repository holds a rule that its documents are pure ASCII. Both survive: the JSON keeps the upstream strings exactly as they arrived, and every upstream string rendered into a page is transliterated at render time. The bytes are one click away either way.

[The schema, explained](../model/schema/index.md) · [The upstream pack manifest](../data/upstream/pack.json) · [The map this came from](https://what-can-it-do.games.sgit.ai/map/index.html)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/data/index.html)*
