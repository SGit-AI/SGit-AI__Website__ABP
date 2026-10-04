# v0.12.0: a gaps and requests register: what a behaviour policy wants and a product cannot enforce or cannot express, who accepts the risk, and the request to close it; plus the article for v0.11.0

> Asked for by the RiskMandate agent team in a brief pack of 4 October: one page and one JSON file recording the gaps found in providers' products when writing behaviour policies, because when a product cannot enforce a rule somebody accepts the risk, usually silently and in the...

*Source: <https://abp.sgit.ai/versions/v0.12.0/index.html> · site v0.12.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.12.0

# v0.12.0: a gaps and requests register: what a behaviour policy wants and a product cannot enforce or cannot express, who accepts the risk, and the request to close it; plus the article for v0.11.0

Asked for by the RiskMandate agent team in a brief pack of 4 October: one page and one JSON file recording the gaps found in providers' products when writing behaviour policies, because when a product cannot enforce a rule somebody accepts the risk, usually silently and in the act of granting the connector. Nine provider entries from the brief, each with the rule it defeats, the barrier that is possible in the site's four words and the contributor's, the risk and who accepts it, the evidence and its tier, and the request. Three entries on our own policies, where an agent's reach exceeded its mandate and what was done about it, on the same page on purpose. Entries are files, one each, so adding one is a pull request. The release also carries the article for v0.11.0.

| Field | Value |
|---|---|
| Version | `v0.12.0` |
| Date | 2026-10-04 |
| Commit | **`git rev-list -n 1 v0.12.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.12.0:`. The hash is not written into [`versions/v0.12.0.json`](../../versions/v0.12.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.12.0.json`](../../versions/v0.12.0.json) |

## What changed

- data/gaps/entries/: twelve JSON files, nine provider gaps and three of our own, each naming who reported it and the evidence tier. The provider entries are self reported by the contributor and the page says this site did not test them; the own entries rest on the measured Gmail vault.
- data/gaps/index.json, generated from the files present, with the field list, the declared values for barrier and status, counts by kind and by provider, and the statement that a count is not a score.
- gaps/: the page. The register by provider, the mapping of the contributor's four words onto the four barriers with both kept, every entry as a table, the own section, and how to add one.
- The first entry is a gap where the rule cannot be written at all: a calendar invitation sends when the event is created, with no draft, so draft only, a person sends has no row. Two of nine provider gaps are of that kind.
- The article for v0.11.0, the fifteenth, with six screenshots from the v0.11.0 tag.

## What it was built against

- The brief pack of 4 October 2026 from the RiskMandate agent team, pasted by the editor of record; its items A and D are this release.
- The four barriers and the enforcer test, which the contributor's four words map onto without remainder.
- The measured Gmail vault at v0.11.0, which the three own entries rest on.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.12.0/index.html)*
