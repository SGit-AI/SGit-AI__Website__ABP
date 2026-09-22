# Marking Everything Read Destroys This User And Breaks Nothing: The Grant Cannot Tell Filing From Erasing A Task List, And The Control Is A Snapshot Rather Than A Prompt

> version v0.33.71 date 19 September 2026 from Human (project lead) to Strategy, the Agent Behaviour Policy team, the RiskMandate product owner, whoever takes the skills site

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.71__strategy-brief__marking-everything-read-destroys-this-user-and-breaks-nothing/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / Marking Everything Read Destroys This User And Breaks Nothing: The Grant Cannot Tell Filing From Erasing A Task List, And The Control Is A Snapshot Rather Than A Prompt

# Marking Everything Read Destroys This User And Breaks Nothing: The Grant Cannot Tell Filing From Erasing A Task List, And The Control Is A Snapshot Rather Than A Prompt

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.71__strategy-brief__marking-everything-read-destroys-this-user-and-breaks-nothing.md`](../../../docs/briefs/v0.33.71__strategy-brief__marking-everything-read-destroys-this-user-and-breaks-nothing.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.71 **date** 19 September 2026 **from** Human (project lead) **to** Strategy, the Agent Behaviour Policy team, the RiskMandate product owner, whoever takes the skills site

**type** Strategy brief

*Second of 19 September on the mailbox thread, following the brief on the consent dialog and written from a memo recorded after a conversation with a user. The memo makes one correction to the earlier document that changes the sales argument, narrows the scope to a single worked persona, introduces a concept the estate has not had a word for, and proposes a new site. Five things were checked against the platform's own reference before anything was written: how the read state is represented, what one call can change and what it returns, whether the state that would be destroyed is enumerable before the fact, what the published skill format requires, and what the estate already publishes at its own skills path. Limitations: the persona is one user described secondhand in a memo and no user research was conducted; the claim that filters are hard to use is the project lead's judgement and the platform's help page states no limits either way, so it is reported as opinion; the trust dynamics are cited from the human factors literature and were not measured here; and the skill specification at the end is a specification, not a tested artefact.*

## What This Is

One user, one catastrophe, and the correction that makes the whole line sellable: **the memo narrows the mailbox argument from a critique of platform scopes to the question that actually sells, which is what an assistant can do to a user while staying entirely inside permissions that user knowingly granted, and it supplies a persona simple enough to explain in a sentence, being somebody whose inbox is their task list, who processes every message and acts on it, who treats unread as work outstanding and read as done, and who keeps no other system because this one works; that user wants two modest things, removal of obvious unwanted mail and the surfacing of messages that slipped past them, which needs read access, the ability to archive or trash, and the ability to change read state, and per action approval is not merely uninformative here but infeasible, since a cleanup touching two hundred messages cannot be approved two hundred times, so the only workable answer the current design offers is to allow everything; inside that allowance the worst available action is not deletion, it is marking messages read in bulk, which destroys nothing the platform recognises as data, loses no message, breaches no confidentiality, and erases the entire working memory of this person's week; three platform facts checked here make the case concrete, first that the read flag is a system label manipulated by the same call and the same capability row as any other label, so the grant cannot distinguish filing from erasing a task list, second that one batch call may carry a thousand message identifiers and returns an empty body on success, so there is no receipt and nothing to compare against, and third that the set about to be destroyed is trivially enumerable in advance through the standard query syntax, which is what turns the problem from unfixable into cheap; that third fact yields the recommendation, which is that the control here is not a better prompt but a snapshot taken before the mutation, because marking read is a reversible operation over an unrecoverable state and recording the state converts it, and the same snapshot produces the explanation the user needs to keep trusting the thing and the summary the user asked for in the first place, so one mechanism serves the control, the trust repair and the feature; the design that follows is consent at the level of the plan rather than the action, where the assistant states what it will touch and how many, the user approves once, and a broker holds the assistant to it, which is both more informative and less frequent and therefore resolves the tension left open yesterday; and the concept the memo reaches for, that everybody has a way of managing information and that having none is itself one, is a required input to consequence that the model does not yet carry, because two users with identical grants over identical mailboxes face different catastrophes.** New contributions: **the read flag identified as the same capability row as filing; the split of reversibility into operation and state, with the snapshot as the conversion; the empty response body as the reason no record exists unless one is made; plan level consent as the resolution of the frequency and information tension; three inbox archetypes with different top rows under the same grant; the naming decision on the concept, argued against the standing ruling on coined nouns; the skills site placed against the second naming collision in one day and against a documented gap in how skills are distributed; and a specification for the first skill.**

## The Correction That Matters

**Yesterday's brief argued that the platform's scope catalogue is too coarse and that its sensitivity tiers sort by the wrong axis. Both hold. The memo says they are not the argument, and it is right.**

**The sellable question is what can happen inside a grant the user gave deliberately.** Not a blind spot in the platform. Not a gap in how any assistant maps its tools onto that platform. A user who reads every word of the consent screen, understands it, and agrees, because the tasks they want genuinely require those permissions. **The interesting risk is the interior of an authorised grant, and it is interesting precisely because nobody was tricked.**

**This reframing costs the estate its most dramatic finding and buys something better.** A conversation that opens with a platform's classification mistake invites the response that the platform will fix it. A conversation that opens with what your assistant can do to you today, with your knowing consent, has no such exit.

## The User, In One Paragraph

**This person's inbox is their task list.** Every message is processed and acted on. Unread means outstanding. Read means done. There is no second system, no tagged backlog, no external list. They rely on their own recall for the rest and it works.

**They want two things from an assistant.** Clear out the obviously unwanted. Surface anything that slipped past, meaning something marked read that should not have been.

**They have never used the platform's own filtering rules**, on the memo's account because creating them is fiddly and they are too literal to express what the user means. The platform's help page states no limits either way, so this stands as the project lead's judgement rather than a checked fact, but it is the ordinary experience and it is why an assistant that takes the instruction in plain language is attractive to this person at all.

**The permissions that follow are unremarkable**: read the mail, archive or trash, change read state. **Every one of them is necessary for the task the user asked for. There is nothing to refuse.**

## Per Action Approval Is Not Merely Uninformative Here, It Is Impossible

**Yesterday's brief showed that the prompt arrives at the moment of least information. This case adds the arithmetic.**

A cleanup pass over a fortnight of mail touches somewhere between dozens and hundreds of messages. **At one prompt per operation the user is asked to answer a question they cannot evaluate, several hundred times, about a task they already described in one sentence.** The design has exactly two stable outcomes: the user allows everything, or the user abandons the assistant.

**So allow all is not the user being careless. It is the only behaviour the interface leaves available**, and any analysis that treats it as a user error has misread the system. **The blame sits with a consent model that scales linearly with operations while the user's attention does not.**

## The Worst Thing That Can Happen Destroys No Data

**Ask what the most damaging action inside this grant is and the intuitive answers are wrong.** Deleting messages is recoverable from trash for a period. Archiving is recoverable by search. Reading is not destructive.

**The most damaging action is marking messages read in bulk, and its damage is invisible to every conventional measure.** No message is lost. No content is disclosed. Nothing leaves the account. Storage is unchanged. **And the user's entire working memory of what they still owe people is gone, with no way to reconstruct it.**

**The inverse is nearly as bad and the memo names it too.** Marking a large set unread, including messages the user processed weeks ago, manufactures a backlog that never existed and mixes it with the real one. **The user cannot tell the two apart, so the damage is not the false entries, it is that the whole queue stops being trustworthy.**

**Three facts from the platform reference make this concrete.**

**The read flag is a system label.** It sits in the same list as the inbox marker and the starred marker, it is manually applicable, and it is added and removed by the same call with the same two fields that apply and remove any user label.

**One batch call carries up to a thousand message identifiers and returns an empty body on success.** So a single request can change a thousand messages, and the response contains nothing at all. **There is no receipt. Nothing in the exchange records what the state was before.**

**And the set that is about to be destroyed is enumerable in advance.** The standard listing call accepts a query in the ordinary search syntax, and the reference's own worked example includes the unread term. Five hundred results per page, continued by token. **The thing that cannot be reconstructed afterwards can be written down beforehand, in a handful of calls, by anybody who thinks to do it.**

## The Grant Cannot Tell Filing From Erasing A Task List

**Mapped into the published capability grammar, the operation the user wants and the operation that ruins them are the same row.**

| What the user asked for | What it is | Capability |
|---|---|---|
| File this under Projects | Add a label to a message | `write.record.tenant` |
| Archive the junk | Remove the inbox label | `write.record.tenant` |
| Mark this as dealt with | Remove the unread label | `write.record.tenant` |
| Mark all two thousand as dealt with | Remove the unread label, in two calls | `write.record.tenant` |

**One row, one reach, four meanings, and the reach is the whole mailbox in every case.** There is no grant, no scope, no setting and no prompt in the current design that separates them, because at the interface they are not separate.

**This is the cleanest illustration the estate has produced of why a grant is not a description of risk.** The grant is complete, accurate, and tells you nothing about what this user stands to lose.

## Reversible Operation, Unrecoverable State

**The model carries undo classes and this case shows they are measuring two things that come apart.**

**The operation is reversible.** Marking a message unread is one call and puts the flag back exactly as it was.

**The state is unrecoverable**, because the set of which messages carried the flag existed only as the flag itself. Once cleared there is no copy anywhere. The operation can be inverted; the argument it would need has been destroyed.

**Compare the label case from yesterday.** Deleting a label is irreversible as an operation, since no interface recreates it. Here the operation is trivially reversible and the outcome is worse, because at least a destroyed label is obvious the moment the user looks. **A cleared unread set looks exactly like a completed week.**

**So the model wants two fields where it has one.** Whether the operation can be inverted, and whether the state it acted on can be reconstructed. **The second is the one that predicts harm, and it is the one that a control can change.**

## The Control Is A Snapshot, Not A Prompt

**This is the recommendation and it follows directly from the enumerability fact.**

**Before any mutation that could affect read state or inbox membership, record the affected set.** For this persona that is the unread set, which is one query and a few pages of identifiers. Store it. Then act.

**That single step does four things.**

**It converts the undo class.** An unrecoverable state becomes recoverable, because the argument the inverse operation needs now exists.

**It supplies the record that the interface refuses to give.** The batch call returns nothing, so without a snapshot neither the assistant nor the user can say afterwards what changed. With one, the difference is computable exactly.

**It produces the summary the user asked for anyway.** The memo wants the assistant to explain what it did. That explanation is the difference between the snapshot and the current state, which is to say the control and the feature are the same artefact.

**And it is the repair mechanism for trust.** The memo's claim that trust collapses after a couple of unexplained incidents is directionally supported by the human factors literature on reliance, which finds that trust falls sharply after failure, recovers slowly, and that appropriate reliance depends on the operator being able to understand what the automation did and why. **An incident with a full record is a recoverable incident. The same incident with no record ends the relationship, which is exactly what the memo predicts.**

**One mechanism, four returns, and it costs a query.** This is the cheapest genuine control the estate has found in this domain and it should be the first thing built.

## Consent At The Level Of The Plan

**Yesterday's brief left a tension open: a better prompt improves each decision and does nothing about the ninth one, because habituation is a property of frequency. This case resolves it, because the fix for the frequency is also the fix for the information.**

**The assistant states a plan before acting.** Not an action, a plan: the criteria in the user's own terms, the counts, and explicitly what it will not touch.

```
Plan for: clean up the last two weeks
  Archive        47 messages   matching  bulk sender list, none from known contacts
  Trash           6 messages   matching  obvious unwanted mail
  Mark read       0 messages
  Mark unread     3 messages   flagged as possibly missed, listed below
  Snapshot taken  1,284 unread message ids recorded before any change
  Will not touch  any message older than 30 days, any starred message, any label
```

**The user approves once, on a page that carries everything a decision needs.** The object counts, the criteria, the reversibility, the exclusions.

**Then a broker holds the assistant to the plan.** Anything outside it is refused, by something the assistant does not control. **This is the point at which the arrangement becomes a boundary under the enforcer test rather than an expectation, and it is why the plan has to be enforced by a broker rather than merely stated by the assistant.**

**It also answers the off piste case the memo raises, which is real.** An assistant that decides mid task to mark five hundred messages read is not talked out of it by an instruction. It is stopped by a plan that said forty seven, held by something that is not the assistant.

## Everybody Has A Way Of Working, Including The People Who Have None

**The memo reaches for a concept the estate has been missing, and the observation that carries it is the sharp one: even not having a system is a system.**

**Consider three users with identical grants over identical mailboxes.**

| How they work | What carries the state | Worst action inside the grant | Nearly harmless |
|---|---|---|---|
| Inbox as task list | The unread set and inbox membership | Bulk change of read state | Deleting a label, since there are few |
| Heavy filer | The label tree and its assignments | Deleting a label | Bulk change of read state |
| Search only, nothing filed | The archive itself, and nothing else | Permanent deletion | Labels and read state alike |

**Same grant. Same assets. Three different catastrophes, and each one is the safest action for one of the others.**

**This is a required input the model does not yet carry.** The brief of 16 September established that consequence cannot be derived from a grant alone and needs the declared assets. This case shows assets are not enough either, because these three users hold the same assets. **What differs is which asset is load bearing, and only the user knows.**

**The good news is that it is one question, not a questionnaire.** Ask what would ruin your week and the answer separates the three archetypes immediately. **That question is the whole of the capture, and it is short enough to put on a page.**

## What To Call It

**The memo calls it information design and then immediately looks for a better word, which is the correct instinct.**

**The standing ruling of 4 September is not to coin a noun and to name for the buyer's question.** Information design is a coined noun and it belongs to a different discipline already. A reader meets it and has to be taught it before they can use it.

**The buyer's question here is not what is my information design. It is what breaks if this goes wrong.** So the customer facing framing is the question, and the artefact answers it: what would ruin your week, what in your account carries that, and what in the grant can reach it.

**Keep a short internal term by all means, because the team needs one.** Working practice, or how you work your inbox, both survive contact with a customer better than a coinage. **The recommendation is that the coinage does not appear in anything a buyer reads, which is the same ruling the estate has applied six times already.**

## The Skills Site

**The memo proposes a site that turns these worked examples into skills people can copy and adapt, and hopes for contributions. Four checks bear on it.**

**The gap it addresses is real and documented.** Custom skills cannot be centrally published and do not sync between the assistant's own surfaces: one uploaded in the consumer product is not available through the interface, and neither is available to the coding tool, which reads them from the filesystem. **A site that hosts skill files for copying is therefore not a convenience, it is the distribution mechanism the format does not have.**

**Part of it already exists.** The estate publishes three skills at its own skills path today, with a stated posture that they ship verbatim from upstream and are ground truth rather than marketing. **So the question is whether the proposal is a new site or a section that grows, and the burden should sit with the new site.**

**The format constrains the authoring and it is worth knowing before anybody writes.** A skill is a file with a name of at most sixty four characters in lowercase letters, numbers and hyphens, and a description of at most one thousand and twenty four characters that must say both what the skill does and when it should be used, since the description is all that is loaded until the skill triggers. The body loads on trigger and should stay small, with anything larger held in bundled files read only when needed. **The description is the whole of the routing logic, and most poorly performing skills are poorly described rather than poorly written.**

**And the address collides with the same ruling as this morning.** The 10 September rule is that every site in the network is named for an argument rather than a function. Skills is a function word, as tools was. **This is the second collision in one day, which is the argument for settling the rule once rather than twice.**

**On whether they are one thing: a skill is the smallest tool.** The tool site proposed this morning shares the premise, the audience, the contribution model and the licensing question. **The recommendation is one site with two sections until there is evidence they need to diverge**, because two thin sites are worse than one that is used.

**Contributions need three things before they are invited**, and none is expensive: a licence that matches the rest of the estate, a provenance line naming the author and the version the skill was verified against, and a statement of what review a contribution gets. **An open invitation without those produces either nothing or a maintenance problem.**

## The First Skill, Specified

**The memo asks for something a user can copy today and that in principle solves the problem. Here is what it says.**

```
name: inbox-triage-without-touching-read-state
description: >
  Use when asked to clean up, triage, tidy or organise a mailbox where the
  user treats unread as their to-do list. Archives and trashes unwanted mail
  and reports what it found, and never changes the read state of any message.
  Snapshots the unread set before acting and reports the exact difference.
```

**Its instructions are five rules and they are all refusals or records.**

**Never add or remove the unread marker.** Not on one message, not on any. If the task appears to require it, stop and say so.

**Snapshot before acting.** Enumerate the unread set and record the identifiers. If the snapshot fails, do not proceed.

**Propose a plan and wait.** Criteria in the user's words, counts per operation, and an explicit list of what will not be touched.

**Prefer archive to trash, and never delete permanently.** Nothing in this task justifies the widest capability.

**Report the difference, not the intent.** Compare the snapshot against the current state and report what actually changed, since the batch interface returns nothing and the assistant's own account of its actions is not evidence.

**Two things this skill is not, and the site should say so on every page.** It is an expectation, not a control, because nothing but the assistant's cooperation enforces it. **And it is worth having anyway**, because most harm here is not adversarial, it is an assistant being helpful in a direction the user never wanted. **The site's honesty about that distinction is the thing that will make the estate's other claims credible.**

## What This Does Not Try To Be

**It is not user research.** One persona, described secondhand in a memo. The archetype table is a hypothesis with three cells and should be tested against actual users before it appears in a deck.

**It is not a broker design.** The broker is argued to be necessary and its shape is left to architecture, as it was yesterday.

**It is not a critique of the platform's filtering rules.** The claim that they are hard to use is reported as the project lead's judgement, because the help page states no limits and none was measured.

**It is not a skills site specification.** Four constraints are identified and the one site question is answered with a recommendation, not a plan.

**And it does not claim the first skill is a control.** It says twice that it is not.

## Honest Tensions

**The snapshot creates a copy of exactly the metadata the user might least want copied.** A list of which messages a person had not yet dealt with is a map of their obligations and their avoidance. It has to live somewhere, it has to expire, and the design has not addressed either. **A control that leaks is not an improvement.**

**Plan level consent moves the failure mode rather than removing it.** A user who approves nine plans without reading them is the same user who clicked nine prompts. Frequency is lower, which helps, and the plan is legible, which helps more, but habituation applies to anything shown repeatedly.

**The one question capture is fast and lossy.** What would ruin your week separates three archetypes and will not separate thirty. The moment the taxonomy grows, the capture grows with it, and the thing that made it sellable was that it was one question.

**A skill that is honest about being an expectation is a harder thing to publish than one that is not.** Every competitor in this space will publish the same file and call it a control. The estate's discipline is its position and it is also a marketing disadvantage, and somebody will propose softening it roughly once a month.

**And narrowing to the interior of an authorised grant gives up the finding with the most impact.** Yesterday's scope tier inversion is the kind of thing that gets repeated. The memo is right that the interior question sells better and is more honest, and the estate should be aware it is choosing the quieter argument on purpose.

## Open Questions

**Where does the snapshot live and how long does it survive?** In the session, in a vault, on the user's own device. Each has a different answer to the leak tension and the choice is not obvious.

**Is bulk change of read state detectable after the fact without a snapshot?** If the platform's own activity history records it in a usable form, the snapshot is a convenience rather than the only route, and that changes the pitch.

**How many archetypes are there really?** Three is a guess that fits three users. The number decides whether the capture stays one question.

**Does the plan need to be machine readable, and in what format?** If the broker enforces it, it does. That is a schema nobody has drafted.

**Should the first skill ship before the broker exists?** It is useful and it is not a control. Shipping it establishes the honest framing early, and it also puts an unenforced document into the world under the estate's name.

**And is the skills site one site with the tool site, or two?** The recommendation is one. The decision is the project lead's and it should be taken once, alongside the naming rule, rather than twice in two weeks.

## Relationship To Previous Briefs

| Date | Document | Relationship |
|---|---|---|
| 4 Sep | The ruling against coining a noun, and to name for the buyer's question | Applied here to reject the coinage in customer facing copy while keeping a working term internally |
| 10 Sep | The ruling that every site in the network is named for an argument rather than a function | Collided with for the second time in one day, which is the argument for settling it once |
| 16 Sep | The brief naming the asset as the missing node | Extended: assets are necessary and not sufficient, because three users with the same assets face different catastrophes |
| 19 Sep | The brief on the tool site and the state buffer | Shares the naming collision and the enforcer test reasoning, and is the reason one site is recommended rather than two |
| 19 Sep | The brief on the consent dialog, immediately prior | Corrected in scope by the memo, and its open tension between better prompts and fewer prompts is resolved here by plan level consent |

## Key Claims

| # | Claim |
|---|---|
| 1 | The sellable question is what an assistant can do inside a grant the user knowingly gave, not whether the platform's scopes are too coarse |
| 2 | For a user whose unread set is their task list, the most damaging action available destroys no data, discloses nothing and loses no message |
| 3 | The read flag is a system label changed by the same call and the same capability row as filing, so the grant cannot separate the two |
| 4 | One batch call carries up to a thousand identifiers and returns an empty body, so no record of what changed exists unless one is made first |
| 5 | The unread set is enumerable in advance through the ordinary query syntax, which is what makes the problem cheap to solve |
| 6 | Reversibility of the operation and recoverability of the state are different properties, and only the second predicts harm |
| 7 | A snapshot taken before the mutation converts the undo class, supplies the missing record, produces the summary the user wanted and is the trust repair mechanism |
| 8 | Per action approval is infeasible at cleanup scale, so allow all is the interface's only stable outcome and not a user error |
| 9 | Consent at the level of the plan is both more informative and less frequent, and becomes a boundary only when a broker enforces it |
| 10 | Three users with identical grants and identical assets have different worst actions, so how a person works is a required input to consequence |
| 11 | Custom skills cannot be centrally published and do not sync across surfaces, so a site hosting copyable skill files fills a documented gap |
| 12 | The estate already publishes three skills at its own skills path, so the burden sits with the proposal for a separate site rather than a section |

## Sources

- The platform's labels guide, read 19 September 2026 for the system label list and the confirmation that the unread marker is manually applicable. https://developers.google.com/workspace/gmail/api/guides/labels
- The batch modify reference, read for the thousand identifier limit, the add and remove fields, and the empty response body. https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/batchModify
- The message listing reference, read for the query parameter, its support for the ordinary search syntax including the unread term, the five hundred result maximum and the page token. https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- The published Agent Skills overview, read for the file format, the name and description constraints, the progressive disclosure levels, and the statement that custom skills are managed per surface and cannot be centrally published. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- The estate's own skills index, read for the three skills currently published and the stated posture that they ship verbatim and are ground truth rather than marketing. https://sgit.ai/skills/index.md
- John D. Lee and Katrina A. See, "Trust in Automation: Designing for Appropriate Reliance", Human Factors, for the dynamics of reliance after failure and the role of understanding in calibration. https://pubmed.ncbi.nlm.nih.gov/15151155/
- The platform's help page on filters, read to confirm that no limits on filter count, criteria or actions are published there. https://support.google.com/mail/answer/6579
- The project lead's voice memo of 19 September 2026, for the persona, the two tasks, the worst case and the skills site proposal

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.71__strategy-brief__marking-everything-read-destroys-this-user-and-breaks-nothing/index.html)*
