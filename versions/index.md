# Versions

> Every release of this site, with the commit it was built from and what it was built against. The version in the chrome links here.

*Source: <https://abp.sgit.ai/versions/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Versions

# Versions

Every release of this site. **The badge in the top bar reads `current` from [`versions/index.json`](../versions/index.json) and links to that version's own details**, rather than to a generic changelog, which is what the guidance asks for.

| Version | Date | What changed |
|---|---|---|
| [v0.7.0](../versions/v0.7.0/index.md) | 2026-09-21 | the first case: one person's estate of six deployments, the mandates elicited from an interview line by line, and the grants not yet measured |
| [v0.6.1](../versions/v0.6.1/index.md) | 2026-09-21 | the mailbox walkthrough gets its article, with six figures captured from the v0.6.0 tag |
| [v0.6.0](../versions/v0.6.0/index.md) | 2026-09-21 | a walkthrough for somebody who has connected an assistant to their own mailbox: four pages, thirteen prompts, and a fourth page that says what a prompt cannot do |
| [v0.5.1](../versions/v0.5.1/index.md) | 2026-09-21 | the articles run newest first, carry their version in the title, and link to the release before and after them |
| [v0.5.0](../versions/v0.5.0/index.md) | 2026-09-20 | the releases get one article each, with the screenshots taken from the tag each one names rather than from today's site |
| [v0.4.4](../versions/v0.4.4/index.md) | 2026-09-20 | seven shapes contributed by riskmandate.ai are promoted with their provenance, a vendor scope becomes a node, and the intake path is the same for anybody |
| [v0.4.3](../versions/v0.4.3/index.md) | 2026-09-20 | the product, the tool and the setting become nodes, derived from data already published, and whose material is declared on the grammar |
| [v0.4.2](../versions/v0.4.2/index.md) | 2026-09-20 | the fact set is data, the fact diff runs over every published page, and every example ends by crossing nine universes |
| [v0.4.1](../versions/v0.4.1/index.md) | 2026-09-20 | the universes become data with a page each, the walk of one row is built on every build, and the gate checks that every node type is owned |
| [v0.4.0](../versions/v0.4.0/index.md) | 2026-09-20 | the ABP is mapped onto Fractal Semantic Graphs: one row crosses nine universes and each keeps its own ontology |
| [v0.3.0](../versions/v0.3.0/index.md) | 2026-09-12 | read, file and project become nodes with their own addresses, and a node type stops being a label and becomes a formula |
| [v0.2.0](../versions/v0.2.0/index.md) | 2026-09-11 | the delta is derived and never authored, so it is stored with its inputs pinned and the gate recomputes it |
| [v0.1.0](../versions/v0.1.0/index.md) | 2026-09-11 | the ontology is promoted out of a game and the five examples are derived rather than written |

## How the version cannot drift

`admin/build/version.txt` owns the version. The tag is derived from it by CI, which refuses to tag unless the newest release commit's subject carries the same string and the bump is the next one. The build generates [`versions/index.json`](../versions/index.json) and a file per version from that same string, and the release gate fails if the badge, `llms.txt`, the twins or the version surface disagree with it.

**Each entry records the commit**, because a version without one cannot be verified later, and **says when it was reconstructed**, because history assembled after the fact has to be labelled.

[The machine readable index](../versions/index.json) · [The repository](https://github.com/SGit-AI/SGit-AI__Website__ABP)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/versions/index.html)*
