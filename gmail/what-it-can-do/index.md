# Step 1: what it can already do

> Four prompts that make your own assistant enumerate its mailbox tools, what each one reaches, which of them you could undo, and which lines it is inferring rather than reading.

*Source: <https://abp.sgit.ai/gmail/what-it-can-do/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Your mailbox](../../gmail/index.md) / Step 1

# Step 1: what it can already do

**You are going to ask it, rather than read a table.** Your assistant can see its own mailbox tools, and it is the only party here that knows what it has already done in your mail. Four prompts, shortest first, and about five minutes.

|  |  |
|---|---|
| **The objective** | Ask your own assistant to enumerate its mailbox tools, what each one reaches, and which of them you could undo. |
| **Next** | [Step 2: What you actually asked for](../../gmail/what-you-asked-for/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

> **What you gain from this page.** A written list of every mailbox tool your assistant holds, sorted with the hardest thing to undo at the top, with every line marked as read from a tool description or inferred. You will use that list on all three pages that follow, so keep the answer.

## Start with one line

Paste this into the assistant you have connected to your mail. If you do nothing else on this site, do this.

**Prompt 1: The tool list.** One question, ten seconds to read the answer. Most people have never seen this list.

```
List every tool you have available for my mail, by name, with one line each on what it
does. Mark any that can change something rather than only read.
```

Two things usually happen. The list is longer than expected, and some of the names on it are not things anybody asked for. Neither is a fault in the product: a connector is a bundle, and you took the bundle.

## Then ask what it has already done

This is the question a published table can never answer, and the reason this walkthrough is prompts rather than documentation. Part four matters most: what it cannot tell you about its own access is the part you have to go outside the chat to check.

**Prompt 2: Four parts, and the fourth is the point.** What it has done, what it could do now, what it cannot do and why, and what it cannot tell you.

```
Before we go further I want an account of your access to my mailbox, in four parts.

1. WHAT YOU HAVE ALREADY DONE. Every action you have taken in my mailbox in our
   conversations: what you read, what you wrote, what you changed. If you cannot see
   earlier sessions, say so plainly and tell me what you can see.

2. WHAT YOU COULD DO RIGHT NOW, without asking me for anything further.

3. WHAT YOU CANNOT DO, and for each one say whether it is because no tool exists, because
   the permission was never granted, or because you have decided not to.

4. WHAT YOU CANNOT TELL ME about your own access. This is the part I care most about.

Do not reassure me, and do not tell me what is typical. Where you are inferring rather
than reading a tool description, write INFERRED at the end of the line.
```

## Then the table you will keep

The columns are chosen so the answer can be argued with. **Reversibility is the one ordering this site permits**, because it is a property of the action rather than a judgement about it.

**Prompt 3: Every tool, with reach, undo and blast radius.** The long one. Keep the answer: steps two and three both build on it.

```
Now put every mail tool you have into one table, one row per tool, with these columns.

  TOOL          the name you call it by
  READS/WRITES  read only, or changes something
  REACH         only my own mailbox, anything in my whole account, or something that
                leaves for another person
  UNDO          can I put it back exactly as it was, and how long do I have
  BLAST RADIUS  the most a single call could touch, at the top end, not the typical case
  PERSISTS      does the effect stop when this chat ends, or keep running afterwards
  EVIDENCE      TOOL if you are reading a tool description, INFERRED if you are guessing

Sort the table so the hardest thing to undo is at the top. Do not rank the rows by how
serious you think each one is: I am not asking you for a verdict, I am asking you for the
properties.
```

**Prompt 4: Where to check the answer.** Separates what it read from what it guessed, and names the screens you can verify each line against.

```
Two more questions about that table.

1. Which rows did you fill in from a tool description you can actually see, and which did
   you fill in from what you know about mail systems in general? Separate the two lists.

2. What would I have to open outside this conversation to check your answer: a consent
   screen, an account settings page, an administration console, a log? Name the exact
   page for each thing you told me, and say what I should expect to find there.
```

## What to look for in the answer

- **A tool you did not know existed.** Filters, labels, spam marking and forwarding are all commonly in the bundle. Write down the ones that surprise you; they are the first entries in step two's third list.
- **A row where UNDO says no.** Sending is the obvious one. It is not the only one: a message marked as spam, a filter created, a label removed from four hundred threads.
- **A row where PERSISTS says the effect outlives the chat.** A filter keeps acting on mail that arrives next week. Nothing in the conversation reminds you it is there.
- **Any line marked INFERRED.** That is the assistant telling you where its own account of itself is a guess, which is exactly what you asked it for.
- **A refusal that turns out to be a preference.** If it says it will not do something, ask which of the four barriers is stopping it. Step three teaches the four names; step four explains why the difference decides everything.

## Something to check the answer against

This site publishes a measured profile for one common version of this shape, so you have a second account to compare yours with. It names **22 tools**, **6 of the 23 capability primitives**, **4 things it cannot reach**, and **5 places where the published sources disagree with each other**. It also records **4 capabilities the grammar has no word for** (drafts, labels, trash, and two tool names truncated in the listing) and **6 open questions** that were left open rather than filled in.

> **If your assistant's answer disagrees with the published profile, neither one is automatically right.** The profile was read on a date from two vendors' own pages and measured in one session; your deployment is a different date and possibly a different build. A disagreement is a thing to check on the consent screen, not an error to resolve in the chat.

[The rows, in full](../../examples/index.md) &#183; [The profile as JSON](../../data/profiles/anthropic/gmail-connector/default.json) &#183; [The same shape rendered live from a vault](https://riskmandate.ai/abp-vault-claude-gmail-connector.html)

> **Where the numbers on this page come from.** The published profile for `anthropic/gmail-connector/default`, which this site did not measure: it was contributed by riskmandate.ai, read from the two vendors' own pages and measured in one session on 16 September 2026. **4 of 6 rows were seen on the thing itself** and the rest were read from documentation. The evidence tier on every row is the contributor's and this site did not raise it. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/gmail-connector/default.json), [the contributed bytes](../../data/contributed/riskmandate/manifest.json).

|  |  |
|---|---|
| **The objective** | Ask your own assistant to enumerate its mailbox tools, what each one reaches, and which of them you could undo. |
| **Next** | [Step 2: What you actually asked for](../../gmail/what-you-asked-for/index.md) |
| **All four steps** | [The walkthrough](../../gmail/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/gmail/what-it-can-do/index.html)*
