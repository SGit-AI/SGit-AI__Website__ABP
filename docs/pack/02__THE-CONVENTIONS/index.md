# The Conventions

> Three sources govern how this site is built. Read all three before writing code. Where this pack and a source disagree, the source wins and you should say so.

*Source: <https://abp.sgit.ai/docs/pack/02__THE-CONVENTIONS/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The pack](../../../docs/index.md#pack) / The Conventions

# The Conventions

> **The source bytes.** This page is generated from [`docs/pack/02__THE-CONVENTIONS.md`](../../../docs/pack/02__THE-CONVENTIONS.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**Three sources govern how this site is built. Read all three before writing code. Where this pack and a source disagree, the source wins and you should say so.**

| Source | What it governs | Read |
|---|---|---|
| `sgit.ai/docs/guidance/index.html` | Vault and site building practice | 11 September 2026 |
| `sgit.ai/llms.txt` | What the platform site is and how it is organised | 11 September 2026 |
| `coding.sgit.ai` | The style guide, with measured compliance | 11 September 2026 |

## What the guidance requires, quoted

**The one minute version, verbatim:**

> Pick your surface first, it changes every other answer.

> Do not build what the platform already has: markdown, file trees, page layouts.

> Publish a read key, never a vault key.

> Version everything and show the version.

> Anything rendered must stay one click from the source bytes.

**On versioning, specifically.** Show the version in the app's chrome, small, in the top bar, always visible, **not** in a footer or an about box. Make it a link to that version's own details rather than a generic changelog. Give versions a home:

```
versions/index.json      { "current": "v0.1.0", "versions": [ newest first ] }
versions/v0.1.0.json     { version, date, commit, vault, reconstructed,
                           title, summary, changes[], basis[] }
```

**Record the commit**, because a version without it cannot be verified later. **Say when reconstructed**, because history assembled after the fact must be labelled. And the title is a sentence, not a label: *settings move into the right hand column*, never *UI improvements*.

**On architecture, the three properties this site must have:**

> Every page is reachable and machine-readable, each has a `.md` twin and appears in `llms.txt`.

> Indexes are generated from the data they index, so they cannot disagree with the source.

> Scope by domain and link across: one site says one thing properly and points elsewhere.

**On honesty**, which this site will lean on constantly: state the gap rather than papering over it, measured rather than guessed.

**On permissions**, if any part of this becomes a vault app: deny by default, declare the narrowest permission, and explain each grant. **That rule is the ABP's own argument applied to the site that describes it**, and it is worth saying so on the page.

## What the style guide requires

The style guide documents thirty one rules with measured compliance, and it is honest about its own enforcement: **zero linters, formatters or type checkers enforce them, and four structural guards in the pipeline are the only automated enforcement, one of which does not work.**

**Read it and follow it. Then note the two figures that bear directly on this repository.**

**File banners are at one hundred per cent compliance.** Every file gets one. Match the format used in the sibling repository you copy the pipeline from.

**Documents free of em dashes are at zero per cent compliance**, with the stated rule violated two hundred and forty eight times across eleven documents. **This repository should be the one that does not.** Every document in this pack is already free of them. Keep it that way, and consider adding it as a fifth structural guard, since it is the cheapest possible check and the estate has a measured record of failing it.

**Other conventions to carry:** one idea per file; one class per file, at ninety per cent compliance; empty package initialisers; no underscore prefixed private names; and the constrained primitive patterns where the code is Python.

## What to copy rather than invent

**You have access to the sibling repositories. Use them.** The pipeline, the tagging, the page build and the markdown rendering all exist and are working on live sites.

**Copy from one named sibling and say which one in the first commit message.** Then verify five things rather than assuming them:

1. **The tag is derived from the version file**, not typed by hand.
2. **The build fails when `llms.txt` does not list every page.** If the sibling does not check this, add it.
3. **The custom domain survives a rebuild**, meaning the `CNAME` or its equivalent is written by the build rather than committed once and forgotten.
4. **The markdown twin of every page is produced by the build**, not maintained alongside it.
5. **The version in the chrome comes from `versions/index.json`**, so it cannot drift from the tag.

**If any of those five is absent from the sibling, that is a finding and belongs in the first version's notes.** The estate's method is to record the gap rather than quietly fix it and move on.

## Publishing

Classify the credential before anything becomes public. **A read key may be published. A vault key may never be.** If any part of this site embeds a vault, escrow the write key before publishing and publish only the read key.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/pack/02__THE-CONVENTIONS/index.html)*
