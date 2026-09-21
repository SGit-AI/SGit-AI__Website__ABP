# v0.4.4: Seven deployment shapes somebody else measured, promoted with their provenance intact

> A consumer of this data built seven shapes this site did not have, one of them from a dated probe of a live instance. Under the three layers those are facts owned by nobody, so they belong at the address every consumer reads. The bytes are held unchanged and the evidence tier stays the contributor's.

*Source: <https://abp.sgit.ai/articles/seven-shapes-somebody-else-measured/index.html> · site v0.6.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Articles](../../articles/index.md) / v0.4.4

# v0.4.4: Seven deployment shapes somebody else measured, promoted with their provenance intact

A consumer of this data built seven shapes this site did not have, one of them from a dated probe of a live instance. Under the three layers those are facts owned by nobody, so they belong at the address every consumer reads. The bytes are held unchanged and the evidence tier stays the contributor's.

> **This is the article for release v0.4.4, published 20 September 2026.** Every release of this site gets one, and it explains what that release changed and why rather than restating [v0.4.4's own release record](../../versions/v0.4.4/index.md). It is release 8 of 10 on this site. Every screenshot below was captured from a checkout of the `v0.4.4` tag, so it shows the site as it stood at that release and not as it stands today. Read on to [v0.5.0](../../articles/one-article-per-release/index.md), or back to [v0.4.3](../../articles/the-confirmations-flag-as-a-path/index.md).

## Somebody else did the work first

A commercial site that renders against this site's data had, by the middle of September, built seven deployment shapes this site did not hold: two Gmail scopes, a Drive scope, a Microsoft 365 connector, a Dropbox server, the Google Workspace servers, and a self-hosted automation platform measured on a live instance by an early user's agent.

It had also published a request asking this site to carry them, and marked that request as the one that unblocks a product. **Under the three layers the answer is not a favour, it is the architecture:** a deployment shape is a layer one fact, owned by nobody, and it belongs at the address every consumer reads rather than inside one consumer's vaults.

*[A figure here in the page: riskmandate.ai reads a vendor's pages or measures an instance it is entitled to run; the bytes are fetched and held unchanged with a hash per file and a hash over all of them; they are promoted into a profile and a mandate with nothing renamed and every id inside the grammar; and they are published at the address every consumer reads. The loop closes when the contributor's vault pins this site's version of the shape rather than holding its own copy]*

## The bytes are held, not copied

Twenty one files were fetched on 20 September from the contributor's public endpoint: a grant, a mandate and a vault record per shape. **They sit under `data/contributed/riskmandate/` exactly as they arrived**, with a hash per file and a hash over all of them, and both the build and the gate recompute the lot and refuse to proceed if a byte moved.

Each promoted profile then pins the hash of the one file it came from. So a byte that changes after the fetch fails the build in three places at once, which is the check being tested rather than trusted:

```
$ printf '\n' >> data/contributed/riskmandate/dropbox-mcp/grant.json
$ node admin/build/validate.js
validate: 3 error(s)
  x data/contributed/riskmandate/dropbox-mcp/grant.json hashes to 01884076f1c4...,
    the manifest says 90b9428222dc... -- the contributed bytes were edited
    after the fetch
  x data/contributed/riskmandate hashes to sha256:a059adc85761fd5..., its
    manifest says sha256:70d1a4609d27f69...
  x data/profiles/dropbox/mcp-server/default.json: pins sha256:90b9428222dc4a2...,
    the contributed file hashes to sha256:01884076f1c4ae2...
```

## What travels with a contributed shape

Promotion renames nothing and drops nothing. Every capability id has to be one of the twenty three, `is_bounded` is recomputed from the barrier and the undo class comes from the grammar. **Everything else the contributor wrote travels whole**, including three things this site had no field for.

| What the contributor carries | Why it is kept |
|---|---|
| Their own provenance block | the vendor pages read and quoted on a date, or a dated probe of an instance they were entitled to run. This site did not observe any of it |
| `contradictions` | where a product's advertised capability and its granted scope disagree, both quoted, both dated, published unresolved. That is the finding |
| `research_needed` | the questions a vendor page could not settle. A named absence beats a hidden one |
| `not_in_grammar` | what the shape can do that no primitive covers. A row that needs a new verb, object class or reach is a proposal to the grammar and needs a probe, so it is recorded rather than forced into a primitive that nearly fits |

## The counts stay apart

The site went from nine shapes to sixteen and from eight starting mandates to fifteen in one release. **The rows do not merge.**

*[A figure here in the page: one bar split into 9 shapes promoted from the published capability map, carrying 62 rows, and 7 shapes contributed by riskmandate.ai, carrying 37 rows. The two sets are counted beside each other and never folded together]*

![A provenance note stating the map's measured ratio and, beside it, the contributed rows with their own ratio and hash](../../assets/articles/v044-provenance-split.png)

*The map's twenty one of ninety nine stays the headline on every page that carries rows from every shape. A second sentence beside it says how many rows were contributed, how many sit at the contributor's measured tier, and where the bytes are. (abp.sgit.ai at v0.4.4, captured 20 September 2026 from a checkout of the v0.4.4 tag.)*

> **The tier is the contributor's and this site did not raise it.** Eleven of the thirty seven contributed rows are at a measured tier, from a dated probe of an instance an early user was entitled to run, with the write up held by the contributor as the evidence file. The rest were read from vendor documentation on a date and quoted. Nothing here was probed by this site, and the two sets are counted beside each other because they were obtained differently.

## The first rows that say whose material

The property declared one release earlier had no values in it. The contributed shapes arrived with thirty seven rows that state one, and the mailbox and drive shapes are where the value earns its place.

![One capability across fifteen of sixteen deployment shapes, each row with its barrier, evidence tier, whose material it reaches and a quoted note](../../assets/articles/v044-capability-rows.png)

*One query, not a map: this capability across every shape that has it, with the contributed ones marked as contributed. The material column is mostly mixed, and mixed is the value that cannot be made own by any setting any of these vendors documents. (abp.sgit.ai at v0.4.4, captured 20 September 2026 from a checkout of the v0.4.4 tag.)*

## A scope is not a tool

One node type arrived with the connector shapes. A coding agent reaches a capability through a tool it runs. **A connector reaches one through a scope a person consented to once**, in the vendor's own identifier, and the two are not the same kind of thing.

So `gmail.readonly` is a node in the vendor's word, never translated, joined to the shape by `scoped_by` and to what it reaches by `permits`. Nine of them matched at this release.

## What this release deliberately does not do

- **It does not import the contributor's nine vaults for this site's own shapes.** Those pin this site, and importing them would be a loop.
- **It gives the contributed shapes no example page.** Their ABPs exist as data, and the contributor renders each one live from its own vault. This site links to those by address rather than rebuilding them.
- **It does not raise anybody's evidence tier.** A row measured by a consumer's user is that user's observation, and this site holds the claim rather than restating it as its own.

![The data page section describing the contributed shapes, the intake path and the tier note](../../assets/articles/v044-contributed.png)

*The intake path is the same for anybody: a profile file and a mandate at an address the proposer publishes, held here as the bytes fetched with their hash, promoted without renaming, and every id inside the grammar. (abp.sgit.ai at v0.4.4, captured 20 September 2026 from a checkout of the v0.4.4 tag.)*

![The home page of abp.sgit.ai at v0.4.4](../../assets/articles/v044-home-hero.png)

*The same argument, four releases and one contributed intake later. The heading has not changed since v0.1.0, which is the point: the releases added evidence and mechanism underneath a claim that stayed still. (abp.sgit.ai at v0.4.4, captured 20 September 2026 from a checkout of the v0.4.4 tag.)*

[The data layer](../../data/index.md) &#183; [The contributed manifest](../../data/contributed/riskmandate/manifest.json) &#183; [The deployment shape universe](../../model/universes/u2/index.md) &#183; [v0.4.4's own release record](../../versions/v0.4.4/index.md)

## Read the sequence

| Direction | The release |
|---|---|
| **Older** | [v0.4.3: The home page has argued about one setting since v0.1.0, and now the build walks it](../../articles/the-confirmations-flag-as-a-path/index.md) |
| **Newer** | [v0.5.0: The releases get one article each, and the screenshots come from the tag rather than from today's site](../../articles/one-article-per-release/index.md) |
| **All of them** | [One article per release](../../articles/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/articles/seven-shapes-somebody-else-measured/index.html)*
