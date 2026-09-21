# Step 4: what a prompt cannot do

> The document you wrote in step three is an expectation rather than a control. Why that is the honest reading, why it is still worth writing, and what would actually bound the behaviour.

*Source: <https://abp.sgit.ai/gmail/what-a-prompt-cannot-do/index.html> · site v0.7.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Your mailbox](../../gmail/index.md) / Step 4

# Step 4: what a prompt cannot do

**A walkthrough that ended at step three would be selling you an expectation as a control.** So this page is not a disclaimer at the bottom of the last one. It is the page that says what you have got, what you have not, and what the difference is made of.

|  |  |
|---|---|
| **The objective** | What you have written down is an expectation rather than a control. Why it is still worth writing, and what would actually bound it. |
| **Before this** | [Step 3: Write the behaviour policy](../../gmail/write-the-behaviour-policy/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

> **What you gain from this page.** An honest reading of your own document, produced by the assistant it is addressed to, plus the list of what would have to exist outside the conversation for each line of it to hold.

## The four barriers, and only one of them is a control

This is the whole model, and it is one sentence: **a control bounds what something can do only if it is enforced by something that thing's own access does not include.** Walk the test rather than reading it off a label.

*[A figure here in the page: the four barriers, each with an enforced_by edge to what enforces it. Nothing is enforced by nothing; an expectation by the agent reading it; a setting by the agent's own account; and a boundary by something above the grant. The first three enforcers are inside the grant and bound nothing. Only the boundary is outside it]*

| Barrier | What it is | Where your document lands |
|---|---|---|
| Nothing | no obstacle at all | the capability is simply there and reachable |
| Expectation | a rule somebody wrote down | **this is where a rule typed into a prompt lands**, along with a handbook, a guideline and an acceptable use clause |
| Setting | a switch that is on, which the holder's own account could change | an approval prompt that can be turned off by the account it protects is this, not the row below |
| Boundary | enforced outside the thing it bounds, and not removable by asking | a permission never granted, an administrator lock somebody else owns, a step another party has to take |

So the document you wrote in step three is the second row. It is a real thing, it changes behaviour most of the time, and **it is not what stops the action**. Anyone who tells you otherwise is selling you the fourth row at the price of the second.

**Prompt 12: Grade your own document.** Have the assistant mark every clause with the one thing that would actually stop it, and answer three questions without softening them.

```
Take the document we wrote and mark every clause in it with the one thing that would
actually stop you from breaking it, using the four names: NOTHING, EXPECTATION, SETTING,
BOUNDARY.

Then answer three questions, without softening them.

  1. How many clauses are held by nothing except your own compliance?
  2. Which clauses would survive a message written specifically to talk you out of them?
  3. If you broke a clause, what record would exist outside this conversation that I
     could find it in?
```

## Why it is still worth writing

- **It is the only artefact that names your intent.** The permissions are the vendor's, the tools are the vendor's, the scopes are the platform's. The sentence that says you did not want mail sent as you is yours and exists nowhere else.
- **It moves where responsibility lands.** Unstated is not authorised, but it is also not refused. An instruction given and departed from is a different situation from one that was never given.
- **It is the specification for the control you have not bought yet.** Every EXPECTATION line is a statement of what a boundary would have to enforce. You cannot buy or configure one until somebody has written that line.
- **It survives the session.** The conversation does not, and the next one starts with the same grant and none of the context.

## Three things about the layer underneath

### What you consented to once applies everywhere afterwards

A connector attaches to your account rather than to one conversation. **The permission set is the union of everything you have ever agreed to**, and consent screens are written to be agreed to once. There is no per conversation narrowing to go back to: a session that only needed to read your mail holds whatever the widest moment held.

*[A figure here in the page: on the left, what an approval prompt tells you, being the class of action, that something is about to happen, and a yes and a no. On the right, what it does not tell you: which message or thread, how many items, who the correspondent is, whether you can undo it, whether the label is one you built years ago, and whether this is one step of forty. So it appears to ask whether this action on this object is acceptable, and it actually asks whether you still want the thing you asked for thirty seconds ago, which has one answer. All six of the missing items are available to the software at the moment it asks]*

The approval prompt in front of an action names the class of action and that something is about to happen. It does not usually name which message, how many, whose, whether you can undo it, or whether this is one step of forty. It is a decision point that carries **the responsibility of a decision and the information of a notification**.

### The scopes are coarser than any rule you would write

No mail scope can be bounded by label, correspondent, thread, topic or sensitivity. Every finer distinction you want has to be invented above the interface, which is exactly what step three was. And the tiers do not line up with the distinctions people care about: **there is no scope that lets an assistant draft without also letting it send**, so the commonest rule anybody writes cannot be expressed as a permission at all.

### A setting is not a boundary, and this shape has 2 of them

In the measured profile for this shape, **2 of 6 capabilities are held by a setting rather than by a boundary**, and the approval prompt is one of them: the vendor's own documentation says it is on by default and can be turned off. **4 capabilities in the gap have nothing in the way that counts as a control**, out of 5 in the gap altogether. That number is the only one on the label a buyer can move, and it moves by one for every capability that gains a real boundary.

> **None of this is an assessment of any named product, and no adjective on this page attaches to one.** The rows above are a published deployment shape read from two vendors' own pages on a date, with the barrier on each row recorded by walking the enforcer test rather than by judging the product. Where the sources disagree with each other, the disagreement is published rather than resolved.

**Prompt 13: What would actually bound it.** The last one. Turns every expectation into a statement of the control it would take, and names who would have to run it.

```
Last one. If I wanted each of the EXPECTATION clauses in that document to become a
BOUNDARY, what would have to exist, and who would have to run it?

For each clause, name the specific thing: a permission that is never granted, a setting
an administrator locks so I cannot change it back, an approval step that somebody other
than me owns, a log kept outside you that somebody else reads. Where nothing available to
me today would do it, say that nothing available today would do it, and do not offer me a
rule as a substitute.
```

## Where to go from here

**[The four objects](../../model/index.md)**: The mandate, the grant, the gap and the barrier, defined.
the model

**[The four barriers](../../model/barriers/index.md)**: The enforcer test, walked, with the one row that is a control.
the model

**[The worked examples](../../examples/index.md)**: Every measured shape on this site, row by row, with its evidence.
the data

**[This shape, live from a vault](https://riskmandate.ai/abp-vault-claude-gmail-connector.html)**: The same profile rendered by riskmandate.ai from the vault it came from.
riskmandate.ai

The briefs behind this section: [no mail scope lets an agent draft without letting it send](../../docs/briefs/v0.33.71__arch-brief__no-gmail-scope-lets-an-agent-draft-without-letting-it-send/index.md) &#183; [the consent dialog is an accountability transfer rather than a decision](../../docs/briefs/v0.33.71__strategy-brief__the-consent-dialog-is-an-accountability-transfer-rather-than-a-decision/index.md) &#183; [all seven](../../docs/index.md#briefs)

> **Where the numbers on this page come from.** The published profile for `anthropic/gmail-connector/default`, which this site did not measure: it was contributed by riskmandate.ai, read from the two vendors' own pages and measured in one session on 16 September 2026. **4 of 6 rows were seen on the thing itself** and the rest were read from documentation. The evidence tier on every row is the contributor's and this site did not raise it. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/gmail-connector/default.json), [the contributed bytes](../../data/contributed/riskmandate/manifest.json).

|  |  |
|---|---|
| **The objective** | What you have written down is an expectation rather than a control. Why it is still worth writing, and what would actually bound it. |
| **Before this** | [Step 3: Write the behaviour policy](../../gmail/write-the-behaviour-policy/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/gmail/what-a-prompt-cannot-do/index.html)*
