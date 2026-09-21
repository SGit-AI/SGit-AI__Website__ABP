# The Consent Dialog Is An Accountability Transfer Rather Than A Decision: The User Is Asked At The Moment They Know Least, And The Irreversible Gmail Action Sits In Google's Least Guarded Tier

> version v0.33.71 date 19 September 2026 from Human (project lead) to Strategy, the Agent Behaviour Policy team, the RiskMandate product owner, whoever builds the first grant viewer

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.71__strategy-brief__the-consent-dialog-is-an-accountability-transfer-rather-than-a-decision/index.html> · site v0.7.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / The Consent Dialog Is An Accountability Transfer Rather Than A Decision: The User Is Asked At The Moment They Know Least, And The Irreversible Gmail Action Sits In Google's Least Guarded Tier

# The Consent Dialog Is An Accountability Transfer Rather Than A Decision: The User Is Asked At The Moment They Know Least, And The Irreversible Gmail Action Sits In Google's Least Guarded Tier

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.71__strategy-brief__the-consent-dialog-is-an-accountability-transfer-rather-than-a-decision.md`](../../../docs/briefs/v0.33.71__strategy-brief__the-consent-dialog-is-an-accountability-transfer-rather-than-a-decision.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.71 **date** 19 September 2026 **from** Human (project lead) **to** Strategy, the Agent Behaviour Policy team, the RiskMandate product owner, whoever builds the first grant viewer

**type** Strategy brief

*Written from a memo recorded while using an assistant to operate a live mailbox, in which the project lead was asked repeatedly to authorise label creation, message moves and label deletion, and observed that at the moment of asking he could not see which message, which thread or which topic the action concerned, so the only honest answers were allow and disallow and neither was a decision. Four things were checked rather than accepted before anything was written: Google's published Gmail scope list and its three sensitivity tiers, read on 19 September 2026; whether a deleted label can be recovered; the assistant vendor's own description of how the mailbox connector asks for approval; and the current state of the published Agent Behaviour Policy page, which has moved since it was last read here and now shows 16 example policies, 118 capability rows, 32 measured on the thing itself and 28 open questions. Limitations: the behaviour of the approval prompt is the project lead's direct observation and the vendor's documentation does not describe what the prompt displays, so the claim about what the user can see at that moment is testimony supported by the absence of any documented contrary mechanism rather than a reading of the interface's source; no interface was instrumented; the mapping of Gmail actions onto the capability grammar is derived here and has not been reviewed by the model's authors; and the commercial argument in the last two sections is an argument, not a forecast.*

## What This Is

A failure of consent design that the estate's existing model already explains, and the reason it is the fastest route to a customer this quarter: **the memo observes that an assistant operating a live mailbox asks for authorisation at exactly the moment the user has least information, since the prompt names an action class such as creating a label, moving a message or deleting a label but not the message, the thread, the correspondent, the topic or the count, so the user is choosing between allowing a category and refusing the task they just asked for, which is not a decision but a formality; the memo names the deeper problem precisely, that this is not oversight for the purpose of deciding, it is oversight for the purpose of locating somebody to blame, and the person located has neither the information nor the means to have chosen otherwise; three checks make the case sharper than the memo does, the first being that Google's scope catalogue offers no way to bound access by label, correspondent, thread, topic or sensitivity, so the grant is all or nothing across the whole mailbox and the assistant's approval prompt is the only thing standing between a broad grant and an arbitrary action; the second being that deleting a label cannot be undone and no route exists to recover one, while the messages survive, so the destruction is of the user's filing system rather than of their mail, which is years of information design and is precisely the asset the estate's own work has been calling the missing node; and the third, which is the finding that should lead any customer conversation, that Google classifies the scope permitting label edits as non sensitive, its lowest tier, while sending a single email is sensitive and reading mail is restricted, so the one irreversible action against the user's information architecture sits in the tier that attracts the least scrutiny from the platform; mapped into the capability grammar the estate publishes, the mailbox grant resolves to a handful of primitives at tenant reach, the approval prompt is a barrier in form and an expectation in effect because habituation removes its binding force, and the delta between what the connector can do and what the user intends is unusually cheap to produce because the grant side is machine readable from the scope strings; and the commercial consequence is that the estate can ship, this month, a description of a grant that every prospective customer already holds, produced automatically, carrying no verdict, which is the published method applied to the one system everybody has open.** New contributions: **the scope tier inversion as the headline fact; label deletion classified against the model's undo classes and against the asset work of 16 September; the approval prompt classified against the four barriers and the enforcer test; the moral crumple zone named with its literature and tied to the statutory language on automation bias; the specification of what a prompt would have to carry to be a decision, with the finding that most of it is available at prompt time; the placement of a mailbox behaviour policy on the right side of the enforcer test, which rules out the version that is easiest to build; and the why now argument stated as a derived artefact rather than as a new control.**

## The Prompt Arrives At The Moment Of Minimum Information

**The memo's core observation is an information ordering problem and it is worth stating precisely.** The user issues a task in natural language. The assistant decomposes it into operations against a mailbox. Each operation raises a prompt naming an action class. The user answers.

**At that moment the user knows the task they asked for and nothing about the operation.** Not which message, not which thread, not which correspondent, not how many items, not whether the label about to be removed holds four messages or four thousand, not whether the label is one created five minutes ago by this same session or one the user built in 2019.

**So the question the prompt actually poses is not the question it appears to pose.** It appears to ask whether this action, on this object, is acceptable. It in fact asks whether the user still wants the task they asked for thirty seconds ago. **That question has one answer, and a user who gives any other answer is abandoning the work rather than exercising judgement.**

**The vendor's own documentation is consistent with this and does not close it.** It states that approval is required before sending, replying and forwarding by default, and that on team and enterprise plans an owner may let members run those without asking each time. It does not describe what the prompt displays. **The absence is the point: nothing in the documented model promises the user the object of the action, because the approval is modelled per action class rather than per object.**

**And the option that looks like a fix makes it worse.** Turning approvals off removes a formality and changes nothing about the grant. Turning them on and clicking through, which is what actually happens, preserves the formality and creates a record that the user agreed.

## Google's Tiers Put The Irreversible Action In The Least Guarded Class

**This is the fact to lead with, and it was not in the memo.** Google sorts Gmail scopes into three sensitivity tiers, and the tier determines how much scrutiny an application faces before it may hold the scope.

| Scope | Google's description | Tier |
|---|---|---|
| `gmail.labels` | "See and edit your email labels." | **Non sensitive** |
| `gmail.send` | "Send email on your behalf." | Sensitive |
| `gmail.readonly` | "View your email messages and settings." | Restricted |
| `gmail.modify` | "Read, compose, and send emails from your Gmail account." | Restricted |
| `gmail.settings.basic` | "See, edit, create, or change your email settings and filters." | Restricted |
| The full mailbox scope, `mail.google.com/` | "Read, compose, send, and permanently delete all your email from Gmail." | Restricted |

**Deleting a label cannot be undone.** The action removes the label and strips it from every message that carried it, the messages themselves survive, and there is no recovery path. **So the single irreversible, unrecoverable action available against a user's own organisation of their mail is reachable through the lowest tier in the catalogue**, while sending one email that the recipient can read and delete sits a tier above it, and reading mail sits two tiers above.

**The reason for the inversion is visible once stated.** The tiers are sorted by exposure of message content, which is a privacy model. Label structure carries no message content, so it scores low. **But the harm here is not disclosure, it is destruction of the user's own work, and a privacy model does not see it at all.** This is the same gap the estate has been describing for months in other words: a grant classified by what it reveals rather than by what it can undo.

**Two further facts complete the picture and both were checked.** First, `gmail.modify` explicitly cannot permanently delete past the trash, which means the platform does model reversibility somewhere, just not for labels. Second, and this is the memo's own claim confirmed, **there is no scope in the catalogue that can be bounded by label, correspondent, thread, topic or sensitivity.** The grant is the whole mailbox or none of it. Every finer distinction the user might want has to be invented above the interface, because the interface offers no place to express it.

## What The Grant Says In The Model's Own Grammar

**The estate already has the vocabulary for this and the mapping is short.** Using the published capability grammar of verb, object class and reach, a mailbox connector at the common scope resolves to roughly this.

| Operation | Capability | Reach | Reversible |
|---|---|---|---|
| Read a message | `read.message.tenant` | The whole mailbox | Not applicable, and not undoable once read |
| Apply or remove a label on a message | `write.record.tenant` | The whole mailbox | Yes, if the prior state was recorded |
| Create a label | `create.record.tenant` | The whole mailbox | Yes, by deleting it |
| Delete a label | `delete.record.tenant` | The whole mailbox | **No. No recovery path exists** |
| Move to trash | `delete.message.tenant` | The whole mailbox | Yes, for a bounded period |
| Permanently delete | `delete.message.tenant` | The whole mailbox | **No**, and requires the broadest scope |
| Send | `send.message.world` | Anyone reachable by mail | No |

**Two things fall out that the memo did not have.**

**The reach column is constant.** Every row says the whole mailbox, because that is what the scope strings grant. In the published model a reach of tenant is already the second widest value available, and the mailbox case has no mechanism to narrow it. **A grant with a uniform reach is a grant with no internal structure, which is exactly why no useful prompt can be written against it.**

**And the reversibility column is not constant**, which is where the model earns its keep. The published policy carries undo classes for precisely this distinction, and the mailbox grant contains two rows at the severe end sitting beside five that are recoverable. **A consent design that treats those seven rows identically is not a consent design, it is a formality applied uniformly.**

## The Prompt Is A Boundary In Form And An Expectation In Effect

**The published model carries four barrier kinds and collapses three of them into one display bucket**, with a rule in prose, a setting and nothing at all grouped as unbounded excess, and only a boundary named as the control. **The approval prompt is the interesting case because it appears to be a boundary and behaves like the bucket above it.**

**In form it is a boundary.** The action does not proceed without the click. The enforcement sits in the host rather than in the agent, the agent cannot remove it, and by the estate's own enforcer test, that a control bounds a grant only if it is enforced by something the grant does not include, it qualifies.

**In effect it is an expectation**, because the information required to answer it is absent and the cost of refusing is the task. A gate whose only stable answer is yes is a gate in the way a turnstile with no ticket check is a turnstile. **The binding force of a barrier depends on the possibility of a no, and a no that abandons the user's own request is not available in practice.**

**This is a genuine gap in the published taxonomy and the brief recommends against patching it with a fifth barrier.** The four kinds describe what stands in the way. What is missing is orthogonal: whether the person or system at the barrier has what they need to act on it. **The cleaner fix is a second field on a boundary row recording whether the decision is informed, with the values being informed, uninformed and automatic**, which keeps the barrier taxonomy intact and makes the mailbox case describable without inventing a category.

## This Has A Name And A Literature

**The memo's sharpest sentence is that this is oversight for accountability rather than oversight for decision making, and that the human is being made answerable for something they do not control. That is a named phenomenon.**

**The moral crumple zone**, described by Madeleine Clare Elish, is the region of a human and machine system that absorbs responsibility when the system as a whole fails, protecting the integrity of the technical system at the expense of the nearest human operator. The human is positioned as the responsible party in a configuration that gives them neither the information nor the time to have acted otherwise. **A per action consent prompt with no object named is a textbook instance: the click is the crumple zone.**

**The statutory language has already moved to meet this.** The European regulation on artificial intelligence requires that oversight be effective, and specifically that the person overseeing be enabled to "properly understand the relevant capacities and limitations" of the system and to "remain aware of the possible tendency of automatically relying or over-relying on the output" of it, a tendency the text names as automation bias. **The requirement is not that a human clicks. It is that the human can oversee.** A consent flow that produces clicks without understanding satisfies the form of the requirement and fails its stated aim, and that distinction is now written into law rather than only into design commentary.

**And the habituation result closes it.** A warning shown often enough to become routine stops being read; the finding is old, repeatedly replicated, and describes a user who has answered nine identical prompts in one session precisely. **Nine prompts in a session is not nine decisions. It is one decision made at the first prompt and eight repetitions of it.**

## What A Prompt Would Have To Carry To Be A Decision

**The useful question is not whether prompts are bad. It is what a prompt would need to contain**, and the answer is short enough to be a specification.

**The object, named.** Not "create a label" but which label, and where it will sit in the existing tree.

**The blast radius, counted.** Not "delete a label" but that this label carries 412 messages going back to March 2019, and that the label will be stripped from all of them.

**The reversibility, stated plainly.** Whether the action can be undone, by what means, and for how long. This is the field the user most needs and the one no current prompt carries.

**The provenance of the object.** Whether the thing being modified was created by this session or predates it. **An agent deleting a label it created two minutes ago is tidying up. An agent deleting a label the user created in 2019 is destroying an asset. The same prompt is shown for both.**

**And the relation to the task.** Which part of the user's instruction this operation serves, so the user can see whether the decomposition matches their intent.

**The finding that matters commercially is that all five are available at prompt time.** The label name is in the call. The message count is one query. The reversibility is a property of the operation and is known in advance. The provenance is derivable from the session's own history. The relation to the task is the agent's own plan. **Nothing here requires new access, which means the gap is a design gap rather than a data gap, and design gaps are cheap to close and easy to demonstrate.**

## Where A Mailbox Behaviour Policy Can Live, And Where It Cannot

**The memo proposes that the user define what they want, that a document be generated, and that the assistant be asked to enforce it. The last step is where the estate's own rules bite, and they bite hard enough to determine the product.**

**A behaviour policy handed to the assistant as text in its session is an expectation.** The assistant is asked to comply and generally will. It is not enforced by anything the grant does not include, because the grant includes the assistant. By the enforcer test it is not a control, and the estate has spent months insisting on exactly this distinction in other people's products. **It cannot now sell the same thing to itself.**

**Three placements are available and only two of them are controls.**

| Placement | What enforces it | Barrier kind | Buildable now |
|---|---|---|---|
| Text in the assistant's session | The assistant's cooperation | Expectation | Yes, today |
| A broker between the assistant and the mail interface | The broker, which the assistant cannot bypass | Boundary | Yes, with work |
| Narrower scopes at authorisation | The platform | Boundary, but coarse | Only where a narrower scope exists, which for labels it does not |

**The third row is worth reading twice.** Even the platform's own enforcement cannot express most of what a user would want, because the catalogue has no scope for a subset of a mailbox. **So the broker is not one option among three. It is the only placement that can express a rule such as never touch labels created before this year, or never let a message from one correspondent group acquire a label belonging to another.**

**This produces the honest product sequence rather than the convenient one.** Version one describes. It does not enforce, it does not claim to, and it says so on its face. Version two brokers. **Selling version one as a control would be the single fastest way to lose the argument the estate has been winning.**

## Why Now, And What Ships First

**The memo asks the right commercial question, which is why anybody would buy this today rather than eventually, and the mailbox answers it better than anything else the estate has tried.**

**Everybody already has the grant.** There is no pilot to arrange, no integration to fund and no hypothetical to explain. The prospective customer connected an assistant to their mail this month and has been clicking prompts ever since.

**The grant side is machine readable.** The scope strings are published, the capability rows follow from them mechanically, and the estate has a standing ruling that the delta is derived and never authored. **For a mailbox, the derivation is complete: the grant column can be generated from the authorisation, and the only thing the human supplies is the mandate, which is the part they actually have opinions about.**

**And the artefact carries no verdict**, which is the method the estate already publishes. It says here is what your connector can do, here is what you said you intended, here is the gap, and here is what is actually enforcing each line, which for most lines is nothing. **No score, no grade, no adjective about the vendor. The record, published; the judgement, left with the reader.**

**So the first shippable thing is a grant viewer for a mailbox**, small enough to be a single page, produced from the scope strings the user can read off their own account settings, with the mandate captured through a short set of choices and the delta derived. It is the lowest rung of the existing ladder, it needs no broker, and it is true.

**The second thing is the object level prompt as a demonstration rather than a product.** Take the five fields above, render a prompt that carries them for one operation class, and put it beside the one the user sees today. **The comparison is the sales argument and it takes an afternoon.**

## The Policies Worth Writing First

**The memo names three and each maps onto a capability row, which is a good sign that the vocabulary fits.**

**Labels created before a given date are read only.** The single highest value rule available, because it bounds the only irreversible row in the grant and costs the user nothing they want.

**Correspondent groups do not cross.** The memo's example of multiple mail streams arriving in one mailbox that must not be mixed. This is a rule about which records may acquire which labels, and it is the one that most clearly cannot be expressed in any platform scope.

**Named topics are not read.** The hardest of the three, because enforcing it requires classifying a message before reading it, which a broker can only do on metadata. **Worth stating as an intent even where enforcement is partial, provided the artefact says which part is enforced and which part is an expectation.**

**A fourth is missing from the memo and belongs at the top of the list.** Bulk operations above a threshold are a different kind of act from single ones. A rule that any operation touching more than some number of messages requires an informed confirmation carrying the count is the cheapest real protection in the set, and it is the one that would have changed the session the memo was recorded during.

## What This Does Not Try To Be

**It is not a criticism of one vendor's connector.** The prompt design described here is close to universal across assistants and mail platforms, and the scope catalogue that makes it necessary is the platform's, not the assistant's.

**It is not a security assessment of any product.** No interface was instrumented, no traffic was captured, and the description of the prompt's contents rests on the project lead's direct observation.

**It is not a specification for the broker.** The broker is argued to be the only placement that can carry a real barrier, and its design is left to an architecture brief.

**It is not a legal opinion.** The statutory text is quoted because it names automation bias in the same terms the memo reaches for, not because a conclusion about any product's obligations follows.

**And it does not claim the description tier is a control.** It claims the opposite, twice, deliberately.

## Honest Tensions

**The most sellable version of this is the one the estate's own rules forbid.** A document handed to the assistant that makes it behave better is easy to build, demonstrates beautifully, and is an expectation. Every commercial instinct will push towards shipping it and calling it a policy layer with enforcement. The discipline of saying it describes rather than enforces will cost deals and is the reason the method is worth anything.

**An informed prompt is a better prompt and it is still a prompt.** Adding five fields raises the quality of each decision and does nothing about the ninth one in a session. Habituation is a property of frequency, not of content, so the design has to reduce the number of prompts as well as improve them, and the two goals pull against each other.

**Bounding labels by age protects the user's history and obstructs the tidying they asked for.** The rule that is most clearly right is also the one most likely to be switched off in week two, and a rule that gets switched off is worse than no rule because it leaves a record of a decision to disable it.

**The grant viewer's honesty is also its weakness as a first sale.** An artefact whose main finding is that almost nothing is enforcing almost anything is accurate, useful and slightly demoralising, and it invites the response that nothing can be done. The demonstration prompt exists to answer that response and has to ship alongside it.

**And the scope tier finding is an argument about Google's model that Google would defend.** Their tiers sort by content exposure and do so coherently. The claim here is that content exposure is the wrong axis for an agent that acts, not that the tiers are wrong for the purpose they were designed for, and the brief should be read that way when it is put in front of anybody.

## Open Questions

**Does any mail platform offer scope narrower than the mailbox?** The Gmail catalogue does not. Whether another does, and what its shape is, decides whether the broker is universal or a workaround for one platform.

**What does the approval prompt actually carry, field by field?** This should be captured from the interface rather than from memory before it appears in any customer facing document.

**Is a deleted label recoverable through any administrative or export route?** The user facing answer is no. Whether an enterprise administrator, a vault export or a takeout archive preserves label membership in a form that could be replayed has not been checked, and it changes the undo classification.

**Where does the broker sit, and what does it cost in latency?** A gate on every mail operation is a gate on the assistant's working speed, and if it is slow it will be removed.

**How is the mandate captured without asking the user forty questions?** The grant derives itself. The mandate does not, and the quality of the whole artefact depends on making that capture short.

**And does the informed field belong on the barrier row or on the operation?** The recommendation here is the barrier row. The counter argument is that informedness varies by object rather than by barrier, which would put it on the operation and make the model larger.

## Relationship To Previous Briefs

| Date | Document | Relationship |
|---|---|---|
| 8 Sep and earlier | The Agent Behaviour Policy model and its published page | Supplies the capability grammar, the four barrier kinds, the undo classes and the rule that a boundary is the only control; now at 118 capability rows with 32 measured, up from the figures last read here |
| 11 Sep | The ruling that the delta is derived and never authored | The mailbox is the cleanest case yet, since the grant column can be generated from the scope strings |
| 12 Sep | The brief establishing that every routable address is in the grant | Same argument one layer up: the grant is what the interface permits, not what the operator intends |
| 15 Sep | The four level offering | The grant viewer is a candidate for the lowest rung, since it is small, automatic and needs no engagement |
| 16 Sep | The brief naming the asset as the missing node | A label set is an asset, and label deletion is the case that shows why consequence cannot be derived without one |
| 19 Sep | The two briefs of this version on state and documentation | Share the enforcer test reasoning used here to place the behaviour policy |

## Key Claims

| # | Claim |
|---|---|
| 1 | The approval prompt arrives at the moment the user has least information, naming an action class without the object, the count, the provenance or the reversibility |
| 2 | Its only stable answer is yes, because refusing abandons the task the user just asked for, so it records agreement rather than eliciting a decision |
| 3 | Google classifies the scope permitting label edits as non sensitive, its lowest tier, while sending one email is sensitive and reading mail is restricted |
| 4 | Deleting a label cannot be undone and no recovery route exists, while the messages survive, so what is destroyed is the user's information design |
| 5 | The scope tiers sort by exposure of message content, which is a privacy model and cannot see destruction of the user's own work |
| 6 | No Gmail scope can be bounded by label, correspondent, thread, topic or sensitivity, so every finer distinction must be invented above the interface |
| 7 | Mapped to the published grammar, every mailbox row has the same reach and differing reversibility, and a consent design that treats them identically is a formality |
| 8 | The prompt is a boundary in form and an expectation in effect, which argues for an informed field on the barrier row rather than a fifth barrier kind |
| 9 | The configuration is a moral crumple zone, and the statutory text on human oversight already names the automation bias that makes it fail |
| 10 | The five fields a prompt would need are all available at prompt time, so this is a design gap rather than a data gap |
| 11 | A behaviour policy handed to the assistant as session text is an expectation and not a control, and only a broker can carry a boundary here |
| 12 | The first shippable artefact is a derived grant viewer that describes and does not enforce, and selling it as a control would forfeit the argument the estate has been winning |

## Sources

- Google's published Gmail API OAuth scope catalogue with its non sensitive, sensitive and restricted tiers and the verbatim scope descriptions, read 19 September 2026. https://developers.google.com/workspace/gmail/api/auth/scopes
- University of Michigan information technology knowledge base on Google Mail label deletion, for the statement that the action cannot be undone and that there is no way to recover a label after deletion. https://teamdynamix.umich.edu/TDClient/30/Portal/KB/Article/10854/Can-I-Recover-Deleted-Labels-in-Google-Mail
- The assistant vendor's help documentation on the Google Workspace connectors, read for the default approval behaviour and the team and enterprise override, and for the absence of any description of the prompt's contents. https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- The published Agent Behaviour Policy page, read 19 September 2026 for the capability grammar, the barrier display buckets, the rule that only a boundary is a control, and the current counts of policies, rows, measurements and open questions. https://riskmandate.ai/agent-behaviour-policy.html
- Madeleine Clare Elish, "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction", Engaging Science, Technology, and Society, for the concept of the human operator who absorbs responsibility for a system they could not have controlled. https://estsjournal.org/index.php/ests/article/view/260
- Article 14 of the European regulation on artificial intelligence, for the requirement of effective oversight and the naming of automation bias. https://artificialintelligenceact.eu/article/14/
- The project lead's voice memo of 19 September 2026, for the session in which the prompts were observed and for the three candidate policies

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.71__strategy-brief__the-consent-dialog-is-an-accountability-transfer-rather-than-a-decision/index.html)*
