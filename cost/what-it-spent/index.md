# Step 1: what it has already spent

> Three prompts that make the agent count what it can count in the current session, sort it into asked for and decided, and name the numbers it cannot see.

*Source: <https://abp.sgit.ai/cost/what-it-spent/index.html> · site v0.8.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The cost ABP](../../cost/index.md) / Step 1

# Step 1: what it has already spent

**An agent can count its own files, commits, fetches and questions exactly, and it usually cannot see its own token count at all.** So ask for the numbers it has, and for the honest list of the ones it does not. Three prompts, shortest first, in the session you are worried about.

|  |  |
|---|---|
| **The objective** | Ask the agent to count what it can count in this session, and to say which numbers it cannot see at all. |
| **Next** | [Step 2: What you actually paid for](../../cost/what-you-paid-for/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

> **What you gain from this page.** A ledger for one session, in the units you can check against the repository and the bill, with a line saying which numbers the agent is guessing and which it cannot produce.

## Start with the count

**Prompt 1: The ledger, for this session so far.** Six counts. The ones it cannot produce are the point.

```
Before we go on, count what you have spent in this session so far, in six lines:

  FILES      written or changed, and how many of them still exist
  COMMITS    made, and pushes, and how many pipeline runs those will have started
  FETCHES    web pages read, searches run, external calls made
  SUBAGENTS  spawned, and roughly what each one did
  QUESTIONS  you asked me, and things you handed me to read, review or approve
  TOKENS     if you can see them; if you cannot, say so, and say who can

Give the numbers, not a description. Where you are estimating rather than counting, put
an asterisk on the line.
```

Two things usually happen. The file and commit counts are larger than either of you pictured, and the token line says it cannot see the number. Both are the point. **The bill is the one cost the agent cannot report, so everything it can report is a proxy for it.**

## Then ask what you paid for and what it decided

**Prompt 2: Asked for, decided, and would not do again.** Three lists over the ledger. The middle one is where the money went.

```
Take every line of that ledger and sort what is in it into three lists.

  ASKED FOR   things I asked for, with the message where I asked
  DECIDED     things you decided were needed on the way to something I asked for
  WOULD NOT   things you would not do again if I gave you the same task now

For the DECIDED list, say for each item what would have happened if you had not done it.
For the WOULD NOT list, say what it cost, in the units of the ledger. Do not defend
anything: if a piece of research turned out not to be needed, it goes in the third list
even if it was reasonable at the time.
```

## Then the numbers it cannot see

This is the line that decides step four. A limit over a number the agent cannot see is a limit the agent cannot keep on purpose, whatever it promises.

**Prompt 3: What you cannot count about yourself.** Names each blind spot, who can see it, and where.

```
Now the numbers you cannot produce. For each of these say whether you can see it, and if
not, who can and where they would look:

  - the tokens this session has used, and what it has cost in money
  - the wall clock time I have spent waiting on you
  - the minutes the pipeline spent on your pushes
  - what any subagent you spawned spent, on all of the above
  - how long the people you handed things to spent on them

Then tell me which of your own limits, if I set them, you could keep by counting and
which you could only keep by guessing.
```

## What to look for in the answer

- **A DECIDED list longer than the ASKED FOR list.** That is normal and it is where the spend is. The question for step two is which of it you would have authorised if asked.
- **Research nobody used.** A fetch is tokens, time and one network reach. Ten of them to answer a question the repository already answered is the commonest line in the WOULD NOT list.
- **Commits that could have been one.** Each push may start a pipeline. The count is on the code host and the pipeline's own log, so this is a line you can check today.
- **Anything handed to a person.** Every one of those is an hour on nobody's bill.
- **An honest token line.** If it says it cannot see the number, that is the correct answer and the next three pages are built on it.

> **Nothing on this page is measured by this site.** There are no runtime logs here and there will not be; the runtime is universe u11, owned by whoever holds the logs and never by this site. Every number an agent gives back is a self report, which counts as a claim rather than a measurement, and the bill is the only log.

|  |  |
|---|---|
| **The objective** | Ask the agent to count what it can count in this session, and to say which numbers it cannot see at all. |
| **Next** | [Step 2: What you actually paid for](../../cost/what-you-paid-for/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cost/what-it-spent/index.html)*
