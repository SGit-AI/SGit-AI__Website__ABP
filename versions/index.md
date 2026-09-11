# Versions

> Every release of this site, with the commit it was built from and what it was built against. The version in the chrome links here.

*Source: <https://abp.sgit.ai/versions/index.html> · site v0.2.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Versions

# Versions

Every release of this site. **The badge in the top bar reads `current` from [`versions/index.json`](../versions/index.json) and links to that version's own details**, rather than to a generic changelog, which is what the guidance asks for.

| Version | Date | What changed |
|---|---|---|
| [v0.2.0](../versions/v0.2.0/index.md) | 2026-09-11 | the delta is derived and never authored, so it is stored with its inputs pinned and the gate recomputes it |
| [v0.1.0](../versions/v0.1.0/index.md) | 2026-09-11 | the ontology is promoted out of a game and the five examples are derived rather than written |

## How the version cannot drift

`admin/build/version.txt` owns the version. The tag is derived from it by CI, which refuses to tag unless the newest release commit's subject carries the same string and the bump is the next one. The build generates [`versions/index.json`](../versions/index.json) and a file per version from that same string, and the release gate fails if the badge, `llms.txt`, the twins or the version surface disagree with it.

**Each entry records the commit**, because a version without one cannot be verified later, and **says when it was reconstructed**, because history assembled after the fact has to be labelled.

[The machine readable index](../versions/index.json) · [The repository](https://github.com/SGit-AI/SGit-AI__Website__ABP)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/versions/index.html)*
