# v0.5.1: the articles run newest first, carry their version in the title, and link to the release before and after them

> Four changes to the section added yesterday, all of them about making the sequence readable. The index lists the newest release first, because that is what a reader arriving at it wants, while the register underneath stays in release order because that is the order the older and...

*Source: <https://abp.sgit.ai/versions/v0.5.1/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.5.1

# v0.5.1: the articles run newest first, carry their version in the title, and link to the release before and after them

Four changes to the section added yesterday, all of them about making the sequence readable. The index lists the newest release first, because that is what a reader arriving at it wants, while the register underneath stays in release order because that is the order the older and newer links walk. Every article is titled with the version it is about, since one article per version is the whole idea and the title should say so. Every article opens with a note stating which release it is the article for and where it sits in the sequence, and closes with a table pointing at the release before it and the release after it. And v0.5.0, which added the section, now has an article of its own.

| Field | Value |
|---|---|
| Version | `v0.5.1` |
| Date | 2026-09-21 |
| Commit | **`git rev-list -n 1 v0.5.1`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.5.1:`. The hash is not written into [`versions/v0.5.1.json`](../../versions/v0.5.1.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.5.1.json`](../../versions/v0.5.1.json) |

## What changed

- The index renders the register reversed, newest release first, and says so in the heading. Each card carries how many releases back it is, computed rather than written. Underneath, two sentences name where to start for reading forwards and for reading backwards.
- Every article's title and page heading now begin with the version: an article about a release should be findable by the version number, in a tab strip and in a search result, without opening it.
- Every article opens with a note saying which release it is the article for, the date, where it sits in the sequence, that the screenshots came from that tag, and links to the neighbouring releases. The position is computed, because an article that called itself the latest would be wrong on the next push.
- Every article closes with an older and newer table, labelled by direction rather than numbered, so a reader can walk the sequence either way without guessing which of two links goes forwards.
- An article for v0.5.0, the release that added the section, with three screenshots captured from the v0.5.0 tag: the index and its chart, an article showing the v0.1.0 home page with its own version badge, and an article section carrying a diagram. It also records the two things the gate caught in that release's own work.

## What it was built against

- The section as it shipped at v0.5.0, read back as a reader rather than as its author, which is where the ordering and the missing navigation became obvious.
- The house rule that an index is generated from the data it indexes, which is why there is one register in one order and two renderings of it.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.5.1/index.html)*
