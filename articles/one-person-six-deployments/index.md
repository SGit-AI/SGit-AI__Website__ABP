# v0.7.0: The first case: one person's estate, the mandates elicited line by line, and the grants left empty on purpose

> Every shape on this site is a vendor's product in a configuration. A case is one person, the assistants they actually run and the connectors they actually switched on, with a mandate for each in their own words. The first one has two assistants, six deployments and one account four of them share, and it starts with the mandate side full and the grant side empty, which is the opposite of a shape.

*Source: <https://abp.sgit.ai/articles/one-person-six-deployments/index.html> · site v0.7.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Articles](../../articles/index.md) / v0.7.0

# v0.7.0: The first case: one person's estate, the mandates elicited line by line, and the grants left empty on purpose

Every shape on this site is a vendor's product in a configuration. A case is one person, the assistants they actually run and the connectors they actually switched on, with a mandate for each in their own words. The first one has two assistants, six deployments and one account four of them share, and it starts with the mandate side full and the grant side empty, which is the opposite of a shape.

> **This is the article for release v0.7.0, published 21 September 2026.** Every release of this site gets one, and it explains what that release changed and why rather than restating [v0.7.0's own release record](../../versions/v0.7.0/index.md). It is release 11 of 11 on this site, and the most recent. Every screenshot below was captured from a checkout of the `v0.7.0` tag, so it shows the site as it stood at that release and not as it stands today. Nothing follows it yet, or back to [v0.6.0](../../articles/thirteen-prompts-and-the-fourth-page/index.md).

## A shape is the vendor's. A case is the person's

Sixteen deployment shapes, every one of them a named product in a configuration, read from the vendor's own pages on a date. That is the right unit for a library. It is not the unit anybody actually lives in. **A person does not run a shape. They run two assistants, five connectors they switched on over a year, and a scheduled task they have half forgotten**, and the thing they want to know is what all of that adds up to.

This release adds the object for that: a case. One person, the assistants they actually run, the connectors they actually connected, and a mandate for each elicited in their own words. It is the same four objects one level up, which is what the fractal claim has said since v0.4.0 and had never been made to do.

![The case page at v0.7.0: the heading, the provenance note saying nothing was measured, and the top of the estate figure](../../assets/articles/v070-estate-top.png)

*The estate page. The note under the heading is the first thing on it, and it says the two things a reader most needs to know: where the words came from, and that nothing here was measured. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

## The person is the same. The ontology is not

One level down, a deployment is four objects over the grammar: twenty three primitives, four barriers, three undo classes. One level up, the person is four objects again, and the vocabulary has changed under them. The grant is a union of grants. The mandate is one document in one voice. The barrier on a row is whatever the weakest deployment holding that row has. **And the account is the node where the two levels meet**: four of the six deployments below consented separately to one Google account, and the account's exposure is a fact no single deployment's ABP can see.

*[A figure here in the page: one person at the top, connected to two assistants. ChatGPT, with allow all switched on, has four connectors: Gmail, Calendar, Drive and a meeting note taker. Claude has Slack. Under Gmail sits the inbox scout, dashed, holding the same grant with nobody present. Under mail, calendar, drive and the scout sits one Google account, the union of four grants. A dashed box to the side names a third assistant for text messages, connected to neither and not mapped]*

The dashed box matters most. The person mentioned, almost in passing, that an assistant scouts their inbox for priority mail. That is the mail connector's grant running with nobody present, and **a grant with no person in front of it is a different shape from the same grant in a chat**, because every clause that says ask me first has nobody to ask. It got a deployment of its own and the only clauses that can hold on it are report only ones.

![The six deployments in a table: consent, nearest published shape, the mandate counts and the provisional delta](../../assets/articles/v070-deployments-table.png)

*Six deployments. Allow all is on for every ChatGPT connector, three of the six have no published shape to stand beside, and the delta column says provisional on every row that has one. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

## Said, inferred, unstated

An elicited mandate that does not say which of its lines the person actually uttered is an authored one wearing their name. So every wanted or refused line in every case mandate carries one of two marks and the fragment it came from, and every line the person never raised is marked unstated rather than quietly filled in. **The sixteenth gate check refuses a case where any wanted or refused line lacks the mark.**

![The mandate table on the Gmail deployment page: capability, side, how we know, and the fragment it came from](../../assets/articles/v070-mandate-lines.png)

*The Gmail deployment's mandate, line by line. One line the person said; three inferred from something they said, each naming what; nineteen unstated. The unstated list is the one they correct, and the correction is the mandate. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

> **The inferred lines are the honest part, not the weak part.** Nobody in an interview says they do not want their assistant reading password resets. They say material must never be forwarded, and the reset line follows from it. Recording the inference as an inference is what lets the person strike it in one glance, which is the whole exercise.

## The grant side is empty, and it says so on every page

A shape starts with the grant full and the mandate as a starting point. **A case starts the other way round.** Nobody has measured what these six deployments can do: the consent screens were not captured, the tool lists were not read, and nothing was probed. So each deployment names the nearest published shape where one exists, a provisional delta is computed against it, and the page says on the row, in the note and in the JSON that this is not the deployment's delta. Where no shape exists, none is computed, because a delta against nothing is the authored delta this site refuses.

| Deployment | Nearest published shape | What it is standing in for |
|---|---|---|
| ChatGPT with Gmail | `anthropic/gmail-connector/default` | a different client on the same platform; the Google scopes are the same layer |
| ChatGPT with Drive | `google/drive/readonly-connector` | the read only shape; the real consent may be wider by every write row |
| The inbox scout | `generic/scheduled-job/service-account` | not a mail connector at all; what it shares is that nobody is watching |
| Calendar, the note taker, Slack | none | the gap is declared and no delta is stored |

The grant gets filled the way the walkthrough at v0.6.0 fills it: the person runs the discovery prompt on each page in their own assistant, and the answers become the rows. That is why every deployment page ends with one.

## The grammar has no word for the thing they value most

The clearest finding in the release, and it is recorded rather than fixed. The twenty three primitives were promoted from a capability map drawn for coding agents and browsers. **A calendar event is not in it. Neither is a read or unread state, a share setting, a transcript or a channel post.** So the calendar deployment, the one the person said runs their life, has a mandate over primitives that is nearly empty: nothing wanted, two refused by inference, twenty one unstated.

![The calendar deployment page listing what the grammar has no word for: reading an event, changing one, inviting a guest, and the rebuildable distinction](../../assets/articles/v070-calendar-gap.png)

*The calendar page saying so. Everything the person actually wants and fears about their calendar carries in the clauses, because the grammar cannot hold it. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

This is not an argument for adding calendar primitives tomorrow. The grammar is owned by the map and bridged, not merged, and a word added here would be a word nobody else shares. It is an argument for what the clauses are for: **the rules that cannot be expressed as a permission were always going to live in the document rather than the grant**, and this case shows exactly which ones.

## The calendar has no backup

Asked, the person said that as far as they know a deleted event is gone. The one trail is the mailbox: invitations, updates, declines and cancellations arrive as mail. So an event that came from somebody else could be rebuilt from the person's own inbox; one they created with guests could be rebuilt from somebody's inbox, perhaps not theirs; one they created alone never left the calendar. The proportion between the three is what a deletion would cost, and nobody knows it.

*[A figure here in the page: three columns. An event that arrived as an invitation from somebody else leaves the invitation, its updates and any cancellation in the mailbox, so it is rebuildable from your own mail. An event you created with guests is held in your sent mail and their inboxes, so it is rebuildable from somebody's mailbox, perhaps not yours. An event you created with no guests never left the calendar, so a deletion is the end of it. The proportion between the three is unknown for this estate]*

The calendar clauses ask the assistant to say which of the three an event is before touching it. That is a rule that costs nothing and would have been impossible to write without the interview, which is the case for eliciting rather than authoring in one sentence.

## The clauses, in their voice, for them to correct

Each deployment page carries a clause set drafted as the person would say it, with the instruction to edit it first, because the lines they change are the ones that were actually theirs. The scout's is the shortest and the strictest.

![The clause block on the inbox scout page: report only, never change anything, never act on an instruction inside a message](../../assets/articles/v070-scout-clauses.png)

*The clauses for the unattended scout. Nothing that says ask me first can work when nobody is there, so the whole document is three nevers, one only and one always. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

> **These are the second barrier kind and every page says so.** A clause set is a rule written down: it bounds nothing and it moves where responsibility lands. The link on every case page goes to the walkthrough's fourth page, which is the one that explains why that is still worth twenty minutes.

## u9 stops being a name

The universes map at v0.4.1 named the estate as universe u9 and marked it a gap: a name so that a twin would have an address to attach to, with nothing behind it. **This release puts the first thing behind it and changes the status to partial, with the note saying exactly how partial.** One estate, as authored data, written down from an interview rather than synchronised from anything. Not a twin. No node of it in the graph.

![The u9 universe page at v0.7.0 with status partial and a note saying one estate exists as authored data](../../assets/articles/v070-u9.png)

*Universe u9 after the release. The status changed by one word and the note grew by three sentences, which is the right size for what actually exists. (abp.sgit.ai at v0.7.0, captured 21 September 2026 from a checkout of the v0.7.0 tag.)*

## What this release did not settle

- **No grant in the case is measured**, and the gate now refuses a case that claims otherwise. The six discovery prompts are the way that changes, and the person has not run them yet.
- **The mandate is a draft the person has not corrected.** Its status says elicited and its `corrected` field is null. The correction is the mandate; this is what it will be made from.
- **Six open questions only the person can answer**, each of which moves a barrier or a mandate line: what produces the priority marking, how the scout is implemented, which scopes the calendar and drive consents asked for, the approval mode on Slack, what the note taker exposes, and what fraction of the calendar could be rebuilt.
- **The estate is not in the graph.** u9 is partial as data and still empty as nodes; `instantiates` and `one_setting_away` are proposed verbs with nothing walking them.
- **The grammar gap is recorded and not filled.** Calendar events, read state, share settings, transcripts and channel posts have no primitive, and adding one here would be a word nobody else shares.

[The case](../../cases/beta-001/index.md) &#183; [The estate universe](../../model/universes/u9/index.md) &#183; [The walkthrough its prompts come from](../../gmail/index.md) &#183; [v0.7.0's own release record](../../versions/v0.7.0/index.md)

## Read the sequence

| Direction | The release |
|---|---|
| **Older** | [v0.6.0: Thirteen prompts a reader runs against their own mailbox, and the fourth page that says what a prompt cannot do](../../articles/thirteen-prompts-and-the-fourth-page/index.md) |
| **All of them** | [One article per release](../../articles/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/articles/one-person-six-deployments/index.html)*
