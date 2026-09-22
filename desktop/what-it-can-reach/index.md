# Step 1: what it can reach on your machine

> Three prompts that make the desktop assistant list its local tools, connectors and past conversations, say which are switched on, and name what it cannot see about its own reach.

*Source: <https://abp.sgit.ai/desktop/what-it-can-reach/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [On your machine](../../desktop/index.md) / Step 1

# Step 1: what it can reach on your machine

**The application knows what is switched on and you probably do not.** Settings accumulate. A local tool enabled for one task in June is enabled today. So ask, and ask for the switch on every line.

|  |  |
|---|---|
| **The objective** | Have the agent list its local tools, its connectors, and whether it can read past conversations, and say which of those are switched on right now. |
| **Next** | [Step 2: What matters, and what does not](../../desktop/what-matters/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

> **What you gain from this page.** A list of everything the assistant can reach on the machine right now, with each line saying whether it asks you first, whether it is on, and whether the agent is reading a tool description or guessing.

## Start with what is on

**Prompt 1: What is switched on right now.** One list, one line each, with the switch state.

```
List everything you can reach on this machine and through this application, one line
each: local files, running commands, each connector, each external tool or server, and
our past conversations. For each line say whether it is switched ON or OFF right now,
whether it asks me before acting, and whether you are reading that from a tool
description or guessing. Mark guesses INFERRED.
```

The line to look at is the one you did not expect to be on. There is nearly always one.

## Then what it has already done here

**Prompt 2: What you have already reached.** Files opened, commands run, connectors used, conversations read.

```
In our conversations on this machine, as far as you can see:

  1. Which files or folders have you opened, and which have you changed?
  2. Which commands have you run?
  3. Which connectors or external tools have you used?
  4. Have you read a past conversation, and which one?

If you cannot see earlier sessions, say so and say what you can see. Do not summarise;
list.
```

## Then what it cannot tell you

**Prompt 3: What you cannot see about yourself.** The blind spots, and where each one could be checked.

```
What can you not tell me about your own reach on this machine? For each of these say
whether you can see it, and if not, who could and where:

  - what a command you run could touch, at the top end, as my user account
  - whether a folder you can read is mine or somebody else's
  - whether a file you can read holds a credential
  - whether our past conversations contain a secret
  - what a connector has done when I was not watching

Then tell me which of these you would need me to tell you, because nothing on the
machine says.
```

## What to look for in the answer

- **A local tool that is on.** Reading files and running commands as you are each one switch, and each reaches everything your account reaches.
- **A connector you forgot.** It attaches to the account, and it is on in every session.
- **The past conversations line.** If it can read them, and they contain a secret, the credentials row and the record row are the same row.
- **The list of things it needs you to tell it.** That is step two, and the agent has just written its own agenda for it.

> **Where the numbers on this page come from.** The published profile for `anthropic/claude-desktop/default`, which is derived and not measured: **0 of 11 rows were seen on an instance**, and the rest were read from what a desktop application running as a user account architecturally is. Your deployment is not that one; the prompts on this page produce yours. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/claude-desktop/default.json).

|  |  |
|---|---|
| **The objective** | Have the agent list its local tools, its connectors, and whether it can read past conversations, and say which of those are switched on right now. |
| **Next** | [Step 2: What matters, and what does not](../../desktop/what-matters/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/desktop/what-it-can-reach/index.html)*
