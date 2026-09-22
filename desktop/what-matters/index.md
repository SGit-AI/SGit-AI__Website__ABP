# Step 2: what matters, and what does not

> Three prompts that produce the map of the machine in the person's words: the work, the not-yours, the credentials, the record, and what in it must never be reused.

*Source: <https://abp.sgit.ai/desktop/what-matters/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [On your machine](../../desktop/index.md) / Step 2

# Step 2: what matters, and what does not

**This is the page the walkthrough exists for.** An agent with the map decides better on its own. An agent without it guesses, reasonably, which is how the folder of client material ends up summarised into a shared document. Have it draft the map from what it can see, then correct the draft.

|  |  |
|---|---|
| **The objective** | Give it the map: the folder that is the work, the folders that are not yours to touch, where the credentials live, and what in the record must never be reused. |
| **Before this** | [Step 1: What it can reach on your machine](../../desktop/what-it-can-reach/index.md) |
| **Next** | [Step 3: Write the rules](../../desktop/write-the-rules/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

> **What you gain from this page.** A map in your words: what is the work, what is not yours to touch, where the credentials live, what is in the record, and what in all of it must never be reused. It is the mandate, and it is an importance list before it is a list of rules.

## Have it draft the map

**Prompt 4: The machine as you see it.** A draft map from what the agent can already see, in four groups.

```
From what you can see on this machine, draft a map of it in four groups. Do not open
anything you have not already opened to do this; use names, locations and what you
already know.

  THE WORK        the folders and files I am actually working on with you
  NOT MINE        folders that look like somebody else's material: clients, shared
                  drives, other people's projects, mail archives
  CREDENTIALS     places that look like they hold keys, tokens, passwords, certificates,
                  or configuration with secrets in it
  THE RECORD      our past conversations, and anything in them that looks like it should
                  not have been pasted

For each entry say why you put it there. Where you are not sure which group something
is in, put it in NOT MINE, and I will move it.
```

Now correct it. **The corrections are the map.** Every folder you move is a thing the agent would otherwise have guessed about.

## Then say what must never be reused

**Prompt 5: What in the record must never come back.** Finds what should not have been pasted, so it can be removed, without repeating it.

```
Look at our past conversations, if you can read them, and tell me which ones contain
something that looks like a secret: a key, a token, a password, a connection string, a
private document pasted in whole. For each, give me the conversation and the date, and
say what kind of thing it is. Do not repeat the secret itself, in any form, and do not
use any of them for anything. I am going to remove them.

If you cannot read past conversations, say so; that is a good answer.
```

> **This prompt is a read of the record, and it says so on purpose.** Finding a secret so it can be removed means something reads the record. Do it once, on demand, in a conversation you then close, rather than leaving it as a standing instruction.

## Then the three lists

**Prompt 6: Freely, ask first, never.** The map turned into a mandate, conservatively.

```
Using the map, sort everything you can reach on this machine into three lists.

  FREELY      things you may read or do without asking: name them by folder or tool
  ASK FIRST   things you may reach only after telling me what and waiting
  NEVER       things you must not reach, open, quote, run or send, whatever I say later
              in a conversation, unless I say it in a new message that names the thing

Put a thing in FREELY only if it is in THE WORK. Put every CREDENTIALS entry in NEVER.
Put NOT MINE in ASK FIRST unless I have said otherwise. Put THE RECORD in ASK FIRST,
with the secrets in it in NEVER. If FREELY is the longest list, do it again.
```

> **Where the numbers on this page come from.** The published profile for `anthropic/claude-desktop/default`, which is derived and not measured: **0 of 11 rows were seen on an instance**, and the rest were read from what a desktop application running as a user account architecturally is. Your deployment is not that one; the prompts on this page produce yours. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/claude-desktop/default.json).

|  |  |
|---|---|
| **The objective** | Give it the map: the folder that is the work, the folders that are not yours to touch, where the credentials live, and what in the record must never be reused. |
| **Before this** | [Step 1: What it can reach on your machine](../../desktop/what-it-can-reach/index.md) |
| **Next** | [Step 3: Write the rules](../../desktop/write-the-rules/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/desktop/what-matters/index.html)*
