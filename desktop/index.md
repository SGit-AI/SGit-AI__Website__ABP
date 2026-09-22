# An assistant on your own machine

> Four steps and ten prompts for somebody running an assistant as their own user account on their own machine, with local files, commands, connectors and past conversations in reach. The same sequence as the mailbox and cost walkthroughs.

*Source: <https://abp.sgit.ai/desktop/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / On your machine

# You run an assistant on your own machine. What can it reach, and what on it matters?

**Four steps, ten prompts, the same sequence as the other two walkthroughs.** In the browser, host means the vendor's environment. On your machine it means your machine: the home directory with credentials in it, the folder that is the work, the folder that is somebody else's, and every past conversation the application kept. The agent cannot tell which of those matters. Step two is where you say.

> **Start here if you only do one thing.** Open the desktop assistant and paste [the first prompt](../desktop/what-it-can-reach/index.md). It lists what is switched on right now, which is usually more than was switched on when you installed it.

## What the published shape says

This site holds a derived profile for a desktop application with local tools: **10 of 23 capability primitives**, none measured on an instance. **4 of its rows sit at a setting**, the third barrier kind: a switch the account running the application can flip. That is the shape's whole character. Reading your files, changing them and running commands are each one switch away, and the switch is yours.

|  | Capability | Undo | Barrier | Known by |
|---|---|---|---|---|
| ● | [`authenticate-as.credential.tenant`](../model/capabilities/authenticate-as.credential.tenant/index.md) Act in accounts with the credentials it holds | no | none (not a control) | derived |
| ● | [`read.credential.host`](../model/capabilities/read.credential.host/index.md) Read credentials stored where it runs | no | none (not a control) | documented |
| ● | [`read.record.history`](../model/capabilities/read.record.history/index.md) Read a retained record: shell history, past sessions | no | none (not a control) | documented |
| ● | [`send.endpoint.world`](../model/capabilities/send.endpoint.world/index.md) Reach any host on the internet | no | none (not a control) | derived |
| ◐ | [`read.file.host`](../model/capabilities/read.file.host/index.md) Read any file the account can reach | no | setting (not a control) | derived |
| ● | [`write.file.project`](../model/capabilities/write.file.project/index.md) Change the project it is working on | with-effort | none (not a control) | derived |
| ◐ | [`execute.process.host`](../model/capabilities/execute.process.host/index.md) Run programs as the account | with-effort | setting (not a control) | derived |
| ◐ | [`write.file.host`](../model/capabilities/write.file.host/index.md) Change any file the account can reach | with-effort | setting (not a control) | derived |
| ● | [`read.file.project`](../model/capabilities/read.file.project/index.md) Read the project it is working on | yes | none (not a control) | derived |
| ◐ | [`grant.credential.self`](../model/capabilities/grant.credential.self/index.md) Change its own permission settings | yes | setting (not a control) | derived |

Two rows have no switch at all. `read.record.history`, the past conversations the application keeps, and `read.credential.host`, the credentials a home directory holds, are documented as reachable with nothing in the way. **If your past conversations contain secrets, those two rows are one row.**

## The concept this walkthrough is built on

**What you are giving the agent is context on what is important and what is not.** A permission says what is possible. A rule says what is forbidden. Neither says that the folder called `work` is the work, that the folder called `clients` is other people's, that the file in the home directory with the token in it must never be opened, or that the unread conversation from last month is the one with the password in it. An agent that has the map decides better on its own; one without it decides by guessing, and guesses reasonably, which is the problem.

| Layer | Who owns it | What it says |
|---|---|---|
| What the application can do | the vendor | local files, commands, connectors, the record, each behind a switch or not |
| What is switched on | you, one click at a time | the settings as they stand today, which is the union of everything you ever enabled |
| What matters on the machine | you, and nobody else can write it | the work, the not-yours, the credentials, the record |
| What your organisation requires | your organisation | whose material is on the machine, and what may leave it |

## The four steps

**[Step 1: What it can reach on your machine](../desktop/what-it-can-reach/index.md)**: Have the agent list its local tools, its connectors, and whether it can read past conversations, and say which of those are switched on right now.
about five minutes

**[Step 2: What matters, and what does not](../desktop/what-matters/index.md)**: Give it the map: the folder that is the work, the folders that are not yours to touch, where the credentials live, and what in the record must never be reused.
about five minutes

**[Step 3: Write the rules](../desktop/write-the-rules/index.md)**: Turn the map into a document the agent can decide against: what it may reach freely, what it asks about, what it never touches, and the report at the end of every turn.
about five minutes

**[Step 4: What a switch is, and is not](../desktop/what-a-switch-is/index.md)**: Four of the shape's rows sit at a setting you can flip. Why that is not a control, and what on a machine actually is one.
about five minutes

## What you will have at the end

- **A list of what is switched on**, from the inside, with what each switch reaches.
- **A map of what matters**: the work, the not-yours, the credentials, the record, in your words.
- **Rules the agent can decide against**, opening with the map rather than with prohibitions.
- **And the straight answer**: a switch you can flip is not a control, and the page that says what on a machine is one.

> **Where the numbers on this page come from.** The published profile for `anthropic/claude-desktop/default`, which is derived and not measured: **0 of 11 rows were seen on an instance**, and the rest were read from what a desktop application running as a user account architecturally is. Your deployment is not that one; the prompts on this page produce yours. [The rows](../examples/index.md), [the profile as JSON](../data/profiles/anthropic/claude-desktop/default.json).

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one.

[Your mailbox](../gmail/index.md) &#183; [The cost ABP](../cost/index.md) &#183; [The four barriers](../model/barriers/index.md) &#183; [A case with three surfaces of one product](../cases/estate-002/index.md)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/desktop/index.html)*
