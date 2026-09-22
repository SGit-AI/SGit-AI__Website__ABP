# Step 2: what you actually asked for

> Three prompts that make the assistant draft your mandate over its own tools in three lists, describe your mailbox as you actually use it, and derive the gap. Correcting the draft is the exercise.

*Source: <https://abp.sgit.ai/gmail/what-you-asked-for/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Your mailbox](../../gmail/index.md) / Step 2

# Step 2: what you actually asked for

**Writing down what you wanted from a blank page is slow and you will miss things.** Correcting a draft somebody else wrote takes minutes and you will catch everything. So have the assistant draft it, then argue with the draft. The argument is the mandate.

|  |  |
|---|---|
| **The objective** | Have it draft a mandate over its own tools, in three lists, and correct the draft. The correction is the whole exercise. |
| **Before this** | [Step 1: What it can already do](../../gmail/what-it-can-do/index.md) |
| **Next** | [Step 3: Write the behaviour policy](../../gmail/write-the-behaviour-policy/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

> **What you gain from this page.** Your own three lists, over the tool table from step one: what you asked for, what you would refuse, and what you have never said either way. Plus the gap between that and the grant, which is the finding almost everybody is surprised by.

## Have it draft the three lists

A mandate is elicited rather than authored. **The third list is the one to watch**: if it is short, the assistant has been guessing on your behalf, and the prompt says so out loud to stop it.

**Prompt 5: Wanted, refused, unstated.** Sorts every tool from step one into three lists, conservatively, and tells you when the answer looks wrong.

```
Take the table of mail tools you just produced and sort every tool into exactly three
lists.

  WANTED    things I have actually asked you to do, and where I asked for them
  REFUSED   things you believe I would say no to if somebody asked me right now
  UNSTATED  everything else: you can do it, and I have never said either way

Rules for this. Put a tool in WANTED only if you can point at something I actually said.
Do not infer it from the fact that the tool exists, and do not infer it from what a
reasonable person would want. When you are unsure, put it in UNSTATED.

UNSTATED should be the longest of the three lists. If it is not, you have been deciding
on my behalf, so do it again.
```

Now correct it. Move things between the lists, out loud, and say why. **The corrections are the part that is yours**, and they are the reason this is a mandate rather than a summary of the product.

## Then have it describe your mailbox as you actually use it

The layer nobody writes down. Your unread count might be a task list or a backlog; a label might be a topic or a stage in a workflow. **An assistant that does not know which is which can destroy a working system without breaking a single rule.**

**Prompt 6: How you actually run your mail.** The information architecture layer: what your labels mean, what unread means, and where a change would go unnoticed.

```
Now describe my mailbox as I appear to use it, not as the product ships it.

  - Which labels do I use, and what does each one appear to mean in my system? Where a
    label looks like a stage in a workflow rather than a topic, say so.
  - What does unread appear to mean to me: a task list, a backlog, or nothing at all?
  - Which conversations look like they run with the same people over months, and which
    are one-off?
  - Where would a change made by you be invisible to me for weeks?

Then tell me the three changes you could make that would be hardest for me to notice and
hardest to reverse. Not the largest ones. The quietest ones.
```

> **Marking everything as read is the example worth sitting with.** It breaks no rule, needs no permission beyond the one already granted, is a single call, and for somebody whose unread set is their task list it destroys the day's work with nothing to put it back from. It is in the briefs: [marking everything read destroys this user and breaks nothing](../../docs/briefs/v0.33.71__strategy-brief__marking-everything-read-destroys-this-user-and-breaks-nothing/index.md).

## Then derive the gap

**The gap is derived and never authored.** It is the grant minus the mandate, which is wider than the list of things you refused, because a tool you never mentioned was never authorised.

**Prompt 7: The gap, and what stands in the way of each line.** Introduces the four barriers by name, and makes the assistant count the rows where nothing real is in the way.

```
Put the two together and give me the gap, in this order.

1. Everything you can reach that is NOT in my WANTED list. All of it, not just the things
   I refused: a tool I never mentioned was never authorised.

2. For each one, what stands in the way today if I do not ask for it. Use exactly these
   four names and pick one per row:
     NOTHING       nothing is in the way
     EXPECTATION   a rule written down somewhere, including anything I told you in a chat
     SETTING       a switch that is on, which somebody with my account could turn off
     BOUNDARY      something enforced outside you, that you cannot turn off by asking

3. Count the rows whose answer is not BOUNDARY, and give me that number on its own line.
   Then tell me plainly which of the four a rule I type into a prompt lands in.
```

## What the published shape does here

Against a starting mandate written to be argued with, the measured profile for this shape puts **5 capabilities in the gap**, of which **3 were refused outright** and the rest were never mentioned. **4 of them have nothing in the way that counts as a control.** The mandate is published beside the profile, with its author named as the site and its status as a starting point, because a mandate nobody can argue with is not a mandate.

[The worked example, with every row](../../examples/index.md) &#183; [The mandate as JSON](../../data/mandates/read-and-draft-never-send.json) &#183; [Why a mandate is elicited rather than authored](../../model/index.md)

> **Where the numbers on this page come from.** The published profile for `anthropic/gmail-connector/default`, which this site did not measure: it was contributed by riskmandate.ai, read from the two vendors' own pages and measured in one session on 16 September 2026. **4 of 6 rows were seen on the thing itself** and the rest were read from documentation. The evidence tier on every row is the contributor's and this site did not raise it. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/gmail-connector/default.json), [the contributed bytes](../../data/contributed/riskmandate/manifest.json).

|  |  |
|---|---|
| **The objective** | Have it draft a mandate over its own tools, in three lists, and correct the draft. The correction is the whole exercise. |
| **Before this** | [Step 1: What it can already do](../../gmail/what-it-can-do/index.md) |
| **Next** | [Step 3: Write the behaviour policy](../../gmail/write-the-behaviour-policy/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/gmail/what-you-asked-for/index.html)*
