# v0.2.0: the delta is derived and never authored, so it is stored with its inputs pinned and the gate recomputes it

> A correction to a rule this site published nine hours earlier, applied in the open. The foundation document says, twice, that the delta is computed and never stored. The first half is right and the second half is wrong: the delta is stored, and storing it is most of what makes...

*Source: <https://abp.sgit.ai/versions/v0.2.0/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.2.0

# v0.2.0: the delta is derived and never authored, so it is stored with its inputs pinned and the gate recomputes it

A correction to a rule this site published nine hours earlier, applied in the open. The foundation document says, twice, that the delta is computed and never stored. The first half is right and the second half is wrong: the delta is stored, and storing it is most of what makes it useful, because a question about whether a control held throughout a period is a question about a series that a recomputed present cannot answer. The corrected rule is that the delta is DERIVED AND NEVER AUTHORED, which is the harder rule, because it forbids the act rather than the artefact. The release gate's check is inverted to match: it refused any stored delta and now recomputes every one of them.

| Field | Value |
|---|---|
| Version | `v0.2.0` |
| Date | 2026-09-11 |
| Commit | **`git rev-list -n 1 v0.2.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.2.0:`. The hash is not written into [`versions/v0.2.0.json`](../../versions/v0.2.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.2.0.json`](../../versions/v0.2.0.json) |

## What changed

- data/deltas/ carries 9 stored deltas, one per deployment shape and mandate pair. Each record pins the version of both inputs, the published vocabulary it was computed against, the time it was computed and the version of the computation that produced it, so it can be recomputed and compared rather than taken on trust. No field in one is writable by a person.
- The release gate's twelfth check is inverted. It refused any file carrying a delta; it now recomputes every stored delta from the profile and the mandate it names and fails on a single row of disagreement, including the ordering. That check is a few lines because the computation is a set difference, and it is a set difference because the grant and the mandate are held as graphs with a schema rather than as prose.
- A new page at /model/delta/ carries the correction with both passages quoted and both replacements given, what the old rule was protecting and why all of it survives, the materialised view the pattern already had a name for, reality as the third input and the calibration loop it creates, the recompute trigger mapped onto an existing event standard, the rule that a threshold crossing is a record and the consequence is a policy somebody set in advance, the history as a business case read rather than constructed, the three clocks, and the distinction from behaviour drift.
- The validity statement on every example gains the second clock: as at this date, from a twin last synchronised at this date. This site has no twin connected to anything and the label says so rather than leaving the field out.
- The dev brief that makes the correction is published in /docs/briefs/ and appears in the index, in llms.txt and in the sitemap without a second edit, because the index is generated from the files present.
- The foundation document is NOT rewritten. Both corrected passages stand as published, with a correction notice above them pointing at the brief and at /model/delta/. Everything else in that document stands.

## What it was built against

- The dev brief of 11 September 2026, the delta is derived and never authored, which is the fifth document of that day and the first written to correct one already pushed.
- The foundation document of 11 September 2026, which the brief corrects in two passages and leaves standing in every other.
- The site building guidance, for the rule that indexes are generated from the data they index, which the brief records this as the fourth instance of.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.2.0/index.html)*
