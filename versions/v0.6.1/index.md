# v0.6.1: the mailbox walkthrough gets its article, with six figures captured from the v0.6.0 tag

> One article per release is the rule, so the release that added the walkthrough gets one. It covers why a section aimed at somebody who does not yet believe the argument had to be prompts rather than a table, why the prompt became a block in the vocabulary rather than raw markup...

*Source: <https://abp.sgit.ai/versions/v0.6.1/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.6.1

# v0.6.1: the mailbox walkthrough gets its article, with six figures captured from the v0.6.0 tag

One article per release is the rule, so the release that added the walkthrough gets one. It covers why a section aimed at somebody who does not yet believe the argument had to be prompts rather than a table, why the prompt became a block in the vocabulary rather than raw markup on four pages, and why the fourth page is the reason the other three are allowed to exist. Six screenshots, all captured from a checkout of the v0.6.0 tag on the day it shipped.

| Field | Value |
|---|---|
| Version | `v0.6.1` |
| Date | 2026-09-21 |
| Commit | **`git rev-list -n 1 v0.6.1`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.6.1:`. The hash is not written into [`versions/v0.6.1.json`](../../versions/v0.6.1.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.6.1.json`](../../versions/v0.6.1.json) |

## What changed

- An article for v0.6.0, the tenth in the section, with six screenshots and the two figures the walkthrough itself carries. It ends, as every article does, on what the release did not settle: nothing in the walkthrough is measured by this site, the published shape is one deployment on one date, and there is no way to check whether the document a reader writes was kept to.
- The screenshot helper takes the capture date rather than reading one module constant, because these figures were captured a day after the first eight releases' were and a caption that said otherwise would be the small lie the section exists to avoid.

## What it was built against

- The v0.6.0 tag, checked out into a detached worktree and served locally, which is the same method every other article's figures were captured with.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.6.1/index.html)*
