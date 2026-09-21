# v0.5.0: the releases get one article each, with the screenshots taken from the tag each one names rather than from today's site

> The version surface says what changed, in the release's own words, and it is deliberately terse. Nothing on this site said why. This release adds an articles section: one article per release from v0.1.0 to v0.4.4, each explaining what the release changed, what it cost, and what...

*Source: <https://abp.sgit.ai/versions/v0.5.0/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.5.0

# v0.5.0: the releases get one article each, with the screenshots taken from the tag each one names rather than from today's site

The version surface says what changed, in the release's own words, and it is deliberately terse. Nothing on this site said why. This release adds an articles section: one article per release from v0.1.0 to v0.4.4, each explaining what the release changed, what it cost, and what it did not settle. Every screenshot in them was captured from a checkout of the tag it names, so an article about the eleventh of September shows the site as it stood on the eleventh of September, badge and all. Ten diagrams carry the mechanisms a screenshot cannot show, and one chart carries the four measures across the eight releases.

| Field | Value |
|---|---|
| Version | `v0.5.0` |
| Date | 2026-09-20 |
| Commit | **`git rev-list -n 1 v0.5.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.5.0:`. The hash is not written into [`versions/v0.5.0.json`](../../versions/v0.5.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.5.0.json`](../../versions/v0.5.0.json) |

## What changed

- Nine pages at /articles/: an index generated from the article register, and eight articles, one per release. Each states its version and date, links to that version's own record, and ends with the pages it is about rather than restating them.
- Twenty seven screenshots under assets/articles/, every one captured from a detached worktree of the tag it names and carrying that version and the capture date in its own caption. Nothing was retouched or staged, and the method is four commands, so the figures are reproducible rather than trusted.
- Ten figures in admin/build/figures.py, each with a described equivalent for the markdown twin so a reader of the twin is not sent to the page to find out what the picture said. Nine are diagrams of a mechanism: the four objects, the enforcer test, a string becoming three nodes, the zoom test in two halves, the nine universes, the fact diff, the confirmations flag as a path, the intake path, and where the sixteen shapes came from.
- One chart, as small multiples: pages, nodes, edges and gate checks across the eight releases, one series per panel because the four measures have different scales and a single axis carrying two of them would say something untrue about both. Its two colours were chosen by a validator rather than by eye and pass the lightness band, the chroma floor, colour-vision separation, the normal-vision floor and contrast against both surfaces; the house teal failed the chroma floor and was snapped to the nearest passing step.
- The articles are held to every rule the rest of the site is: no score, no adjective about a named product, pure ASCII, and the same forbidden words. Two of them were caught by the gate while this release was being written, one of them a stray non-ASCII character in a figure.

## What it was built against

- The eight release tags in this repository, which are what the screenshots were taken from and what the chart's numbers were counted from.
- The version records under versions/, which the articles explain rather than restate, and which win where an article and a record disagree.
- The visualisation guidance this estate follows for charts: pick the form before the colour, never two y axes, validate a categorical palette with a runnable check rather than by eye, and label selectively.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.5.0/index.html)*
