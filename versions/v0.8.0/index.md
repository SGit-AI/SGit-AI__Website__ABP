# v0.8.0: the cost ABP: a walkthrough over how much an agent may spend rather than what it may do, with a ledger every turn and an accountant to read it

> Every ABP on this site bounds what an agent may do. This release adds the one that bounds how much: tokens, files written, commits pushed, fetches run, and the hour of somebody else's time an agent spends by asking a question or handing over something to read. Cost is not a...

*Source: <https://abp.sgit.ai/versions/v0.8.0/index.html> · site v0.8.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.8.0

# v0.8.0: the cost ABP: a walkthrough over how much an agent may spend rather than what it may do, with a ledger every turn and an accountant to read it

Every ABP on this site bounds what an agent may do. This release adds the one that bounds how much: tokens, files written, commits pushed, fetches run, and the hour of somebody else's time an agent spends by asking a question or handing over something to read. Cost is not a capability. It is a property of every call, the grammar has one primitive for money and none for a count, and quantity lives in universe u11, the runtime, which this site has no node in. So the section says that first and puts the substance where it can live: twelve prompts that make the agent count what it can count and name what it cannot, a cost mandate in the deployer's units, a clause set every skill has to run inside, a ledger clause that makes the rest checkable, an accountant that reads the ledgers, and a fourth page that says a limit over a number the agent cannot see is an expectation twice over.

| Field | Value |
|---|---|
| Version | `v0.8.0` |
| Date | 2026-09-22 |
| Commit | **`git rev-list -n 1 v0.8.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.8.0:`. The hash is not written into [`versions/v0.8.0.json`](../../versions/v0.8.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.8.0.json`](../../versions/v0.8.0.json) |

## What changed

- Five pages at /cost/: a hub and four steps, in the same shape as the mailbox walkthrough, with the objective, what the reader gains, the prompts shortest first, and the step before and after on every page.
- Twelve prompts: the six line ledger for one session; asked for, decided and would not do again; the numbers it cannot see; freely, batched and never; what waste looks like for this deployer; four lines; the full clause set with limits per turn, a research rule, a delegation rule and a rule about other people's time that has no number on purpose; the ledger clause; the accountant; the grading of every clause against the four barriers; what would actually cap each one; and one line for a session with no time for the rest.
- Two figures: the four objects before the action over the runtime after it, and the five things an agent spends with who pays and who can see the number, the fifth dashed because it is on nobody's bill.
- The distinction from a skill, in a table: a skill says how to do one task; a behaviour policy says what may not be done and how much it may cost, for one agent across every task, and is what every skill runs inside.
- The accountant as the first useful shape in universe u12: a second session with no tools whose only job is to read the first agent's ledgers against its clauses and count the work it made for people.
- The honest line on every page: nothing here is measured by this site, there are no runtime logs here and there will not be, every number an agent returns is a claim, and the bill is the only log.

## What it was built against

- The foundation document's first named gap, quantity, and the runtime universe u11 as mapped at v0.4.1: counts within an interval, sums within an interval, and the per turn cost of the licence to operate simulation.
- The mailbox walkthrough at v0.6.0, whose four step shape and prompt block this section reuses without change.
- A deployer's own account of agents writing too many files, committing too often, creating too much traffic, researching what did not need researching, and offloading work to people; and the accountant role one of their projects already had to invent to notice the last of those.

## The five verifications against the sibling

The pipeline, the release gate and the page shell were copied from [SGit-AI__Website__Game__What-Can-It-Do](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do) at its v0.8.0. The conventions ask for five things to be verified rather than assumed, and **an absent one is a finding that belongs in the first version's notes** rather than a thing to fix quietly.

| Verification | The sibling | What this repository does |
|---|---|---|
| The tag is derived from the version file, not typed by hand | **holds** | `admin/build/version.txt` owns the version. CI reads it, refuses to tag if the newest release commit's subject disagrees, refuses if the tag already exists on an earlier commit, and refuses if the bump is not the next minor or a deliberate major. Copied unchanged. |
| The build fails when `llms.txt` does not list every page | **did not hold** | The sibling generates `llms.txt` from its page list, so it cannot miss a page the generator knows about, and nothing fails if a page exists in the tree that the generator does not. Check 11 here walks the tree and fails on any `.html` page missing from `llms.txt`. |
| The custom domain survives a rebuild | **did not hold** | The sibling commits `CNAME` once. Here the build writes it from `SITE['host']`, and the canonical check reads the same file, so a domain change is one edit in one place. |
| The markdown twin of every page is produced by the build | **holds** | `shell.write_site` emits the `.html` and the `.md` from the same block list, and gate check 7 fails on a page without a twin. Copied unchanged, and it is the reason the twins cannot drift. |
| The version in the chrome comes from `versions/index.json` | **did not hold** | The sibling has no `versions/index.json` at all: the badge reads `version.txt` and links to a hand-maintained history page. Here the build generates `versions/index.json`, a file and a page per version, from the same string the tag is derived from, and the badge links to that version's own details. The published pipeline still owns the tag, so the two cannot disagree. |

**Two of the three that did not hold are one-line fixes and the third is a surface that did not exist.** None of them is a criticism of a site that has been publishing for weeks: they are the cost of a pipeline growing by copy, which is exactly what the five verifications are for.

## Where the sources disagree

The published source wins and the disagreement is recorded. **The estate's method is to record the gap, not to quietly resolve it.**

| The disagreement | What each says | What this site did |
|---|---|---|
| SETTLED IN v0.2.0. The foundation document and the project lead, on whether a delta is stored | v0.1.0 built to the foundation document's rule that the delta is computed and NEVER STORED, and put a check in the release gate refusing any file that carried one. The project lead's correction, issued the same day, is that the second half was an error: the delta belongs in a vault along with the history of the grants and mandates that produced it. | v0.2.0 stores the deltas with their inputs pinned and inverts the check, so the gate now recomputes every one of them. **Never authored** is the rule that replaced it, and it is harder than the one it replaced. See [the delta](../../model/delta/index.md). |
| The foundation document and the published data, on what changes when confirmations go off | The foundation document says that turning confirmations off moves the barrier on **every capability in the delta** by one row. In the published pack it moves exactly one barrier, on `execute.process.host`, and that capability is **inside the mandate**: the deployer asked for it. So the label's numbers do not move at all and the two documents still differ materially. | The data wins on the fact and the foundation document wins on the wording, so both example pages state what actually changes. It makes the pair a **better** argument, not a worse one: identical headline numbers, a materially different document, which is the case for the leaflet and against any single number. |
| The pack and the sibling, on where the version lives | The conventions ask for `versions/index.json` as the home of the version. The sibling's working pipeline derives the tag from `admin/build/version.txt` and has no `versions/index.json`. | Both. `version.txt` still owns the tag, because that is the published pipeline and it wins; `versions/index.json` is generated from the same string, so the surface the guidance asks for exists and cannot drift from the tag. The gate checks the agreement. |
| The pack and the published data, on whether the smallest grant has an empty delta | The pack says the smallest shape in the set is where a reader who does not believe an agent can do much *finds the delta is still not empty*. In the published data that shape's grant is one capability and the starting mandate asks for exactly it, so **the delta is empty**. | The example says so, plainly, and says why an empty delta is a result rather than a failure: a method that could never report nothing would be a sales document, and the other four examples would be worth less for it. Changing the mandate to manufacture a delta would have been the dishonest fix. |
| The published headline and the pack's own vocabulary, on what `measured' means | The map's headline says 21 of 99 rows were measured. The pack's vocabulary defines `measured` as a dated probe with an evidence file, and **no row in the pack is at that tier**: the 21 are at `observed`, which is seen directly on the thing itself. | The site counts `observed` as measured, which reproduces the published figure, and says so in `data/provenance.json` and on the data page. Reproducing the number without the note would have been less careful than the map. |
| The hard rules and the published data, on em dashes and pure ASCII | Every document in this repository is to be pure ASCII, with zero em dashes and zero en dashes. The data promoted from the capability map carries all three, because it was written elsewhere and this site does not get to edit somebody else's bytes. | Both. The JSON keeps the upstream strings exactly as they arrived and `data/` is exempt from the guard for that reason; every upstream string rendered into a page is transliterated at render time; and the bytes are one click away under `/data/upstream/`. The guard is in the pipeline and fails the build everywhere else. |
| The guidance and the docs section, on rebuilding the markdown renderer | The guidance forbids rebuilding markdown viewing, file trees and page layouts, because the platform provides them. The docs section has to turn eleven markdown documents into pages. | `admin/build/docs_pages.py` translates a markdown document into the same small block vocabulary every other page here is written in, at build time. No viewer is shipped to a browser, no file tree and no layout engine, and the source bytes are served beside every rendered document. It is a judgement call and it is recorded as one rather than assumed. |

## What is not built yet, stated plainly

- **No view across the nine shapes.** Each example carries a grant-against-mandate figure, and there is no figure that puts one capability across every deployment shape at once. The third graph rule says render the result of a query rather than the whole graph, so that would be another query rather than a map.
- **No ABP for a shape outside the published map**, which means the cost of producing one where the grant has to be measured rather than looked up is still unknown, and that is the number the store needs.
- **No interchange form emitted.** The W3C vocabulary is described on [the graph page](../../model/graph/index.md) and nothing on this site serialises to it yet.
- **Quantity and agent-to-agent interaction are not modelled**, as the model page says. They are gaps in the ontology rather than in this site.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.8.0/index.html)*
