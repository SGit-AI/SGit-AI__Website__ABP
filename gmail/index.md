# Your mailbox, and what you gave it

> Four steps and thirteen prompts you paste into your own assistant, to find out what connecting it to your mailbox actually gave it, what you meant to give it, and how much of the difference you can write down.

*Source: <https://abp.sgit.ai/gmail/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Your mailbox

# You connected an assistant to your mailbox. What did that give it?

**Four steps, thirteen prompts, about twenty minutes.** You paste them into your own session, against your own mailbox. Nothing is collected here, no account is needed, and at the end you have a written account of what your assistant can reach, what you meant to authorise, and the gap between the two.

> **Start here if you only do one thing.** Open the assistant you have connected to your mail and paste [the first prompt](../gmail/what-it-can-do/index.md). It takes a minute and it changes the conversation, because almost nobody has seen the list before.

## Why ask the agent rather than read a table

An assistant is unusually good at describing its own tool surface, and it is the only party in the room that can see all of it at once. **It knows what it has already done in your mailbox, which no published table can.** So these pages do not hand you a list to read. They hand you prompts that make your own assistant produce the list, for your deployment, and then give you something to check it against.

> **What comes back is a self report, and this site counts that as a claim rather than a measurement.** An agent describing its own access is the cheapest evidence there is and the weakest: it stays a claim until a log held outside the agent agrees with it. That is why step one ends by asking it to mark every line it is inferring, and why the measured profile is published beside it.

## The four layers this is really about

Between a mail platform and what a person meant, there are four layers. The top two are somebody else's and they only ever grow. The bottom two are yours, and they are usually unwritten.

*[A figure here in the page: four layers stacked between a mailbox and what somebody meant. What the platform's scopes permit, which is fixed and coarse and cannot be bounded by label, correspondent, thread, topic or sensitivity. What the connector surfaces, which is attached to the account rather than to one conversation and is the union of everything ever consented. What you actually want, including how your mailbox is organised. And what your organisation and the law require. The top two are the grant, the bottom two are the mandate, and the gap between them is the delta]*

| Layer | Who owns it | What it does here |
|---|---|---|
| What the platform's scopes permit | the mail platform | Fixed and coarse. **No scope can be bounded by label, correspondent, thread, topic or sensitivity**, so every finer distinction you want has to be invented above the interface. |
| What the connector surfaces | the assistant's vendor | The tools you can actually reach, which is usually fewer than the scopes permit and grows as the product does. **It attaches to your account rather than to one conversation**, so what you consented to once applies in every session that has it attached. |
| What you want | you | The job, plus the way your mailbox is organised. The only layer that knows your unread set is a task list rather than a backlog. |
| What your organisation requires | your organisation, and the law | **Most of a mailbox was written by other people.** A grant you hold over their material is not a grant you may pass on. |

## What the published profile says about this shape

This site holds a measured profile for one common version of this: Claude with the Gmail connector enabled. **It reaches 6 of the 23 capability primitives**, through 22 tools named in the directory listing. Against a starting mandate written to be argued with, **5 of them are excess and 4 of those have nothing real in the way.**

Your deployment is not that one. The point of the walkthrough is to produce yours.

**[Step 1: What it can already do](../gmail/what-it-can-do/index.md)**: Ask your own assistant to enumerate its mailbox tools, what each one reaches, and which of them you could undo.
about five minutes

**[Step 2: What you actually asked for](../gmail/what-you-asked-for/index.md)**: Have it draft a mandate over its own tools, in three lists, and correct the draft. The correction is the whole exercise.
about five minutes

**[Step 3: Write the behaviour policy](../gmail/write-the-behaviour-policy/index.md)**: Turn the gap between the two into a document you can keep, from four lines to a full Agent Behaviour Policy.
about five minutes

**[Step 4: What a prompt cannot do](../gmail/what-a-prompt-cannot-do/index.md)**: What you have written down is an expectation rather than a control. Why it is still worth writing, and what would actually bound it.
about five minutes

## What you will have at the end

- **A grant**: every mailbox tool your assistant holds, what each reaches, and which of them you could undo.
- **A mandate**: the same list sorted into what you asked for, what you would refuse, and what you have never said either way. You will correct a draft rather than write one, which takes minutes.
- **A delta**: the gap, which is the finding. Almost everybody is surprised by the size of the third list, because unstated is not authorised.
- **And a straight answer about what that document is**: an expectation you can point at, not a control. Step four is the page that says so.

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product.** These pages describe published deployment shapes and give you prompts to run against your own. Every capability claim here carries a source, a date and whether it was measured or read.

> **Where the numbers on this page come from.** The published profile for `anthropic/gmail-connector/default`, which this site did not measure: it was contributed by riskmandate.ai, read from the two vendors' own pages and measured in one session on 16 September 2026. **4 of 6 rows were seen on the thing itself** and the rest were read from documentation. The evidence tier on every row is the contributor's and this site did not raise it. [The rows](../examples/index.md), [the profile as JSON](../data/profiles/anthropic/gmail-connector/default.json), [the contributed bytes](../data/contributed/riskmandate/manifest.json).

[The four objects an ABP is made of](../model/index.md) &#183; [The barrier](../model/barriers/index.md) &#183; [The worked examples](../examples/index.md) &#183; [This shape, rendered live from a vault by riskmandate.ai](https://riskmandate.ai/abp-vault-claude-gmail-connector.html)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/gmail/index.html)*
