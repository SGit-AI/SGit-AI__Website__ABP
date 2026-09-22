# v0.6.0: a walkthrough for somebody who has connected an assistant to their own mailbox: four pages, thirteen prompts, and a fourth page that says what a prompt cannot do

> Everything on this site so far was written for a reader who already believes the argument. This release adds the door: a section at /gmail/ for somebody who connected an assistant to their mail, has never seen the list of what that gave it, and can be handed one link. It does...

*Source: <https://abp.sgit.ai/versions/v0.6.0/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.6.0

# v0.6.0: a walkthrough for somebody who has connected an assistant to their own mailbox: four pages, thirteen prompts, and a fourth page that says what a prompt cannot do

Everything on this site so far was written for a reader who already believes the argument. This release adds the door: a section at /gmail/ for somebody who connected an assistant to their mail, has never seen the list of what that gave it, and can be handed one link. It does not give them a table to read. It gives them thirteen prompts to paste into their own session, because an assistant is the only party in the room that can see its whole tool surface at once and the only one that knows what it has already done in that mailbox. Step one enumerates the grant, step two elicits the mandate by having the assistant draft it so the reader can correct it, step three writes the behaviour policy, and step four says plainly that what they have written is an expectation rather than a control, which is the page the section would be dishonest without.

| Field | Value |
|---|---|
| Version | `v0.6.0` |
| Date | 2026-09-21 |
| Commit | **`git rev-list -n 1 v0.6.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.6.0:`. The hash is not written into [`versions/v0.6.0.json`](../../versions/v0.6.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.6.0.json`](../../versions/v0.6.0.json) |

## What changed

- Five pages at /gmail/: a hub and four steps. Each step opens with its objective and what the reader gains, carries the prompts to paste, says what to look for in the answer, and ends with the step before and the step after, so the sequence can be walked without going back to the hub.
- Thirteen prompts, ordered shortest first on every page. They run from one line listing the mailbox tools to a full Agent Behaviour Policy in the four object shape, and the last two ask the assistant to grade its own document against the four barriers and then say what would have to exist outside it for each expectation to become a boundary.
- A prompt block in the block vocabulary: a figure with a tag, a title, one line on what it produces, the text in a monospaced block, and a copy button. The markdown twin renders it as a fenced block, so an agent reading the twin gets the prompt rather than a description of it, and assets/copy.js is injected only on the pages that have one.
- Two figures: the four layers stacked between a mail platform's scopes and what a person meant, and what the approval prompt names at the moment it asks against what it leaves out. Both have described equivalents in the twin.
- Every number in the section is computed from the profile for anthropic/gmail-connector/default, which riskmandate.ai contributed and this site did not measure: the tool count, the grant size, the contradictions, the capabilities the grammar has no word for, the open questions, and the rows of the gap with nothing in the way. The provenance note on the hub and on the steps says how many rows were seen on the thing itself.
- The seven briefs from the mailbox pack, published under docs/briefs/ and rendered by the same docs path as everything else, so the section can cite the argument it rests on rather than restating it.

## What it was built against

- The measured profile contributed by riskmandate.ai and promoted at v0.4.4, which is why this section could be written as computed numbers rather than as prose.
- Two properties of the layer underneath, both from the pack: a connector attaches to the account rather than to the conversation, so what was consented to once holds in every session afterwards; and no mail scope separates drafting from sending, so the commonest rule anybody writes cannot be expressed as a permission at all.
- The rule that every prohibition carries its barrier, which is what forced step four to be a page rather than a footnote.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.6.0/index.html)*
