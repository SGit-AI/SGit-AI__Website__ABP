# v0.8.0: the cost ABP: a walkthrough over how much an agent may spend rather than what it may do, with a ledger every turn and an accountant to read it

> Every ABP on this site bounds what an agent may do. This release adds the one that bounds how much: tokens, files written, commits pushed, fetches run, and the hour of somebody else's time an agent spends by asking a question or handing over something to read. Cost is not a...

*Source: <https://abp.sgit.ai/versions/v0.8.0/index.html> · site v0.10.0 · this file is generated from the same content
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

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.8.0/index.html)*
