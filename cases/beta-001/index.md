# Case beta-001: One person, two assistants, six deployments, one shared account

> One business user, two chat assistants, six deployments over five connectors, four of them sharing one Google account. The estate mapped, the mandates elicited, the grants not yet measured.

*Source: <https://abp.sgit.ai/cases/beta-001/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Cases](../../cases/index.md) / beta-001

# One person, two assistants, six deployments, one shared account

**An early beta user: a business user whose day runs in a mail, calendar and files suite, with two chat assistants connected to different parts of it and a third, out of scope here, handling text messages.** Two assistants, six deployments, and one Google account that four of them share. Everything below was elicited on 2026-09-21; nothing was measured.

> **Where the words on this page came from.** One interview, elicited by riskmandate.ai on 21 September 2026 and transcribed automatically. The transcript is not published; every quoted fragment was checked against it. **Nothing here is measured.** No grant was probed, no tool list was captured, and every delta is provisional against a published shape that is not this deployment. The deployer has not yet corrected the draft, and the correction is the mandate.

## The estate

*[A figure here in the page: one person at the top, connected to two assistants. ChatGPT, with allow all switched on, has four connectors: Gmail, Calendar, Drive and a meeting note taker. Claude has Slack. Under Gmail sits the inbox scout, dashed, holding the same grant with nobody present. Under mail, calendar, drive and the scout sits one Google account, the union of four grants. A dashed box to the side names a third assistant for text messages, connected to neither and not mapped]*

| Deployment | Consent | Nearest published shape | The mandate | Delta |
|---|---|---|---|---|
| [ChatGPT with the Gmail connector, allow all](../../cases/beta-001/chatgpt-gmail/index.md) | allow all | [`anthropic/gmail-connector/default`](../../examples/index.md) | 1 wanted, 3 refused, 19 unstated | 5 excess, 4 unbounded (provisional) |
| [ChatGPT with the Google Calendar connector, allow all](../../cases/beta-001/chatgpt-calendar/index.md) | allow all | **none published** | 0 wanted, 2 refused, 21 unstated | no shape to compute against |
| [ChatGPT with the Google Drive connector, allow all](../../cases/beta-001/chatgpt-drive/index.md) | allow all | [`google/drive/readonly-connector`](../../examples/index.md) | 1 wanted, 3 refused, 19 unstated | 2 excess, 1 unbounded (provisional) |
| [ChatGPT with a meeting note taker connected](../../cases/beta-001/chatgpt-granola/index.md) | allow all | **none published** | 1 wanted, 2 refused, 20 unstated | no shape to compute against |
| [The inbox scout: the same Gmail grant, running with nobody present](../../cases/beta-001/chatgpt-inbox-scout/index.md) | allow all | [`generic/scheduled-job/service-account`](../../examples/index.md) | 1 wanted, 6 refused, 16 unstated | 7 excess, 7 unbounded (provisional) |
| [Claude with the Slack connector](../../cases/beta-001/claude-slack/index.md) | not stated | **none published** | 1 wanted, 1 refused, 21 unstated | no shape to compute against |

## The account is the junction

Four deployments run over **one Google account**: mail, calendar, drive and the unattended scout. Each holds its own grant, each was consented to separately, and **the account's exposure is the union of the four**, which no single deployment's ABP can see. A connector attaches to the account rather than to a conversation, so each of these grants holds in every session that has it attached, and the account's exposure is the union of all four. A scheduled task holds the same grant with nobody in front of it.

This is the fractal claim made concrete rather than argued. One level down, each deployment is four objects over the grammar. One level up, the person is four objects again: one mandate, in their words, against the union of every grant they hold. Same shape, different ontology, and the account is the node where the levels meet.

## What they told us about how they work

- **Mail is unread counts, not labels.** "unreads, not so much labels, which I should use basically". About 314,000 unread messages, never purged. So the unread set is not a task list here, it is a backlog, and a change to it would go unnoticed for a long time. The one thing that would not: fifty messages flipping state in the part of the inbox they actually look at.
- **An auto prioritisation runs on the inbox.** "auto prioritisation that is also being done based on some P0, P1": a priority marking the deployer treats as the real task list. What produces it was not established (a Gmail feature, a filter, a third party, or the assistant) and it is the first open question below.
- **An assistant scouts the inbox unattended.** "I also have OpenAI that is scouting my inbox for high priority emails": a task that runs when the person is not in the conversation, over the same grant. It is listed as its own deployment below because a grant with nobody in front of it is a different shape from the same grant in a chat.
- **The calendar is the thing that matters most.** "my calendar runs my life". Some events carry detail and some do not; one to ones usually have titles; anything from a third party or a group meeting usually has an agenda. Asked to rank, the calendar sits above mail.
- **There is no backup of the calendar.** Asked whether any backup exists: none. As far as the deployer knows a deleted event is gone. The one trail that could rebuild some of it is the mailbox, because invitations, declines and cancellations arrive as mail. Which events could be rebuilt from that trail, and which could not, is a map nobody has drawn.
- **Some of what they hold must never leave.** Agreed without hesitation that the mailbox and the drive contain material received from others that must never be forwarded or passed on, which is an allow list and a deny list nobody has written.

## The calendar has no backup, and the mailbox is the only trail

The thing the deployer values most is the thing with no backup. Asked, the answer was that as far as they know a deleted event is gone. But some of a calendar arrives as mail: invitations, updates, declines and cancellations all land in the inbox, and from that trail some events could be rebuilt. Which ones is a map nobody has drawn, and it decides what a deletion would actually cost.

*[A figure here in the page: three columns. An event that arrived as an invitation from somebody else leaves the invitation, its updates and any cancellation in the mailbox, so it is rebuildable from your own mail. An event you created with guests is held in your sent mail and their inboxes, so it is rebuildable from somebody's mailbox, perhaps not yours. An event you created with no guests never left the calendar, so a deletion is the end of it. The proportion between the three is unknown for this estate]*

## Open questions the deployer can answer

Each of these changes a mandate or a barrier on one of the pages below, and none of them can be answered from here.

1. **What produces the P0 and P1 marking?** If it is a Gmail feature or a filter, it is a setting in the account. If it is the assistant, it is the scout below acting on mail rather than only reading it, which changes that deployment's mandate.
2. **How is the inbox scout implemented?** A scheduled task inside the assistant, a recurring prompt the person runs, or a third party with its own grant. Each is a different shape and only the first is covered by the nearest shape named below.
3. **Which scopes did the calendar and drive consents ask for?** The consent screens were not captured. Read only and full access are different grants and the same allow all click sits in front of both.
4. **What is the approval mode on the Slack connector?** Not asked. Per action or allow all decides the barrier on every row.
5. **What does the meeting note taker's connector expose?** Transcripts of other people's speech, summaries, or both, and whether the connector can write back. Not documented anywhere this site has read.
6. **Which calendar events could be rebuilt from mail?** Events that arrived as invitations leave a trail in the mailbox; events the person created with no guests leave none. The proportion is unknown and it decides how much of the calendar a deletion would actually cost.

## The first prompt, for both assistants

Before any of the six pages, one prompt to paste into each assistant separately. Two answers, one account, and the comparison is the point.

**Prompt A: The connectors, from the inside.** Run it in ChatGPT and in Claude. The two lists together are the estate.

```
List every connector and every external tool you have on my account, by name. For each
one say:

  - whether each action needs my approval, or whether I have allowed all
  - what you have already done through it in our conversations, as far as you can see,
    and say plainly if you cannot see earlier sessions
  - whether it can only read, or can also change or send something
  - whether anything runs through it on a schedule, when I am not here

Then tell me which of these connectors share one underlying account, because a grant on
one of them is a grant on the account.
```

## The 6 deployments

**[ChatGPT with the Gmail connector, allow all](../../cases/beta-001/chatgpt-gmail/index.md)**: a different client on the same platform: the measured profile for a chat assistant with a Gmail connector, 4 of 6 rows seen on the thing itself. The Google scopes are the same layer; the tool list is not this product's.
1 said, 3 inferred, 19 unstated

**[ChatGPT with the Google Calendar connector, allow all](../../cases/beta-001/chatgpt-calendar/index.md)**: no published shape. A calendar connector for a chat assistant is on riskmandate.ai's list of shapes asked for and not yet published, and the grammar this site is written in has no word for a calendar event at all, which is the finding on this page.
0 said, 2 inferred, 21 unstated

**[ChatGPT with the Google Drive connector, allow all](../../cases/beta-001/chatgpt-drive/index.md)**: the read only shape, derived and not measured. This deployment's consent was not captured and may be the full drive scope, in which case the nearest shape understates the grant by every write and delete row.
1 said, 3 inferred, 19 unstated

**[ChatGPT with a meeting note taker connected](../../cases/beta-001/chatgpt-granola/index.md)**: no published shape, and nothing this site has read documents what the connector exposes: transcripts, summaries, or both, and whether it can write. Everything in it is other people's speech.
1 said, 2 inferred, 20 unstated

**[The inbox scout: the same Gmail grant, running with nobody present](../../cases/beta-001/chatgpt-inbox-scout/index.md)**: the derived shape for a job that runs when nobody is watching. It is not a mail connector, so the primitives differ; what it shares with this deployment is the one property that matters: no person's judgement stands in front of any action.
1 said, 6 inferred, 16 unstated

**[Claude with the Slack connector](../../cases/beta-001/claude-slack/index.md)**: no published shape. A Slack connector for a chat assistant is on riskmandate.ai's list of shapes asked for and not yet published, with the note that channels are mostly other people's writing.
1 said, 1 inferred, 21 unstated

## Out of scope

- A third assistant that handles text messages and WhatsApp. It is connected to neither of the two above and was not mapped.
- Tasks and notes in the suite: named as present and not connected to either assistant.

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one. A case describes one person's deployments in their own words and against published shapes with their sources and dates.

[The case as JSON](../../data/cases/beta-001/case.json) &#183; [The walkthroughs the prompts come from](../../gmail/index.md) &#183; [The estate universe](../../model/universes/u9/index.md)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cases/beta-001/index.html)*
