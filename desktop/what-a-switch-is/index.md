# Step 4: what a switch is, and is not

> Four of the shape's rows sit at a setting the account can flip. Why a switch you can turn off is not a control, what on a machine actually is one, and the two prompts that grade the rules and name the caps.

*Source: <https://abp.sgit.ai/desktop/what-a-switch-is/index.html> · site v0.11.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [On your machine](../../desktop/index.md) / Step 4

# Step 4: what a switch is, and is not

**The document you wrote is the second barrier kind, a rule written down, and the switches in the application are the third.** Neither is a control. This page says why, and what on a machine is.

|  |  |
|---|---|
| **The objective** | Four of the shape's rows sit at a setting you can flip. Why that is not a control, and what on a machine actually is one. |
| **Before this** | [Step 3: Write the rules](../../desktop/write-the-rules/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

> **What you gain from this page.** An honest reading of your rules by the agent they are addressed to, and the short list of things on a machine that would actually bound it.

## The enforcer test, applied to a switch

**A control bounds what something can do only if it is enforced by something that thing's own access does not include.** An application running as your user account can change its own settings, because you can, and it is you. So a switch in the application is not a control on the application. It is a setting, and the published shape says so on **4 of its 10 rows**: `read.file.host`, `execute.process.host`, `write.file.host`, `grant.credential.self`.

| Barrier | On a machine | Example |
|---|---|---|
| Nothing | reachable, nothing in the way | the home directory, as your account |
| Expectation | a rule written down | **every line of the document from step three** |
| Setting | a switch the account can flip | the local files toggle, the commands toggle, the per action prompt, the file that turns the prompt off |
| Boundary | enforced by something the account does not include | a second account with no rights to the folder, a disk the account cannot mount, a device policy an administrator locks, a sandbox the application cannot leave |

Read the last two rows together. **The same switch is a setting on your own laptop and a boundary on a managed one**, because on the managed one somebody else holds it and you cannot flip it back. Which one you have is a fact about the deployment and not about the product.

**Prompt 9: Grade your own rules.** Every rule marked with the one thing that would actually stop it.

```
Take the rules we wrote and mark every one with the one thing that would actually stop
you breaking it, using exactly these names: NOTHING, EXPECTATION, SETTING, BOUNDARY.

Then answer three questions without softening them:
  1. How many rules are held by nothing except your own compliance?
  2. Which of the switches in this application could you, running as my account, turn
     back on if a task seemed to need it?
  3. Which rules would survive a file on this machine written to talk you out of them?
```

**Prompt 10: What on this machine would actually bound you.** For each expectation, the boundary that would replace it, and who owns it.

```
For each rule you marked EXPECTATION or SETTING, name the specific thing on this machine
or above it that would make it a BOUNDARY, and who would own it: a separate account for
the work with no rights to the rest, a folder my account cannot read, a device policy an
administrator locks, a sandbox, a proxy that counts what leaves, a log somebody else
reads. Where nothing available to me today would do it, say that nothing available today
would do it, and do not offer me a rule as a substitute.
```

## Why write it anyway

- **It is the only document that names what matters.** The application knows what is possible and what is switched on. Nothing knows that the folder called `clients` is other people's until you write it.
- **It moves where responsibility lands.** An agent that summarised a client folder into a shared document did something you left open; one that did it against the map departed from an instruction.
- **It is the specification for the boundary you have not built.** A second account for the work is a two line task once the map says what the work is.

## Where to go from here

**[The four barriers](../../model/barriers/index.md)**: The enforcer test, walked, with the one row that is a control.
the model

**[The confirmations pair](../../examples/index.md)**: One setting, two documents: the same agent on the same machine with the prompt on and off.
the worked examples

**[Three surfaces of one product](../../cases/estate-002/index.md)**: A deployer who runs the assistant in the browser, as a coding agent and on the desktop, over one record.
a case

**[Your mailbox](../../gmail/index.md)**: The same four steps over a connector rather than a machine.
the first walkthrough

> **Where the numbers on this page come from.** The published profile for `anthropic/claude-desktop/default`, which is derived and not measured: **0 of 11 rows were seen on an instance**, and the rest were read from what a desktop application running as a user account architecturally is. Your deployment is not that one; the prompts on this page produce yours. [The rows](../../examples/index.md), [the profile as JSON](../../data/profiles/anthropic/claude-desktop/default.json).

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one.

|  |  |
|---|---|
| **The objective** | Four of the shape's rows sit at a setting you can flip. Why that is not a control, and what on a machine actually is one. |
| **Before this** | [Step 3: Write the rules](../../desktop/write-the-rules/index.md) |
| **All four steps** | [The desktop walkthrough](../../desktop/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/desktop/what-a-switch-is/index.html)*
