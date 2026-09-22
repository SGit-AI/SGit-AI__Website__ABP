# Step 4: what a clause over a count cannot do

> A limit the agent cannot measure is an expectation twice over. Which of the four barriers a turn cap, a spend limit and a pipeline budget actually are, who can turn each one off, and what the ledger is and is not.

*Source: <https://abp.sgit.ai/cost/what-a-count-cannot-do/index.html> · site v0.9.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The cost ABP](../../cost/index.md) / Step 4

# Step 4: what a clause over a count cannot do

**Every clause on the last page is the second barrier kind: a rule written down.** For cost it is worse than that, because some of the rules are over numbers the agent cannot see, and a limit you cannot measure is one you cannot keep on purpose. This page says which is which, and what would actually cap each one.

|  |  |
|---|---|
| **The objective** | A limit the agent cannot measure is an expectation twice over. What a turn cap, a spend limit and a pipeline budget actually are, and who can turn each one off. |
| **Before this** | [Step 3: Write the cost policy](../../cost/write-the-cost-policy/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

> **What you gain from this page.** An honest reading of your cost policy, line by line, by the agent it is addressed to, and the list of the things outside the conversation that would make each line hold.

## The four barriers, applied to a number

| Barrier | For a capability | For a count |
|---|---|---|
| Nothing | the capability is simply reachable | nothing caps it, which is the default for files, commits, fetches and questions in nearly every deployment |
| Expectation | a rule written down | **every clause from step three**, and twice over where the agent cannot see the number it is asked to stay under |
| Setting | a switch the holder's account could change | a turn cap passed on the command line, a spend alert you set yourself, a pipeline that you can re-run by hand |
| Boundary | enforced outside the thing it bounds | a spend limit an administrator locks on the account, a rate limit at the platform, a pipeline budget the repository owner set, a branch nobody can push to without review |

Read the last two rows together. **A limit you set is a setting; a limit somebody else set that you cannot remove is a boundary.** The same number, in the same place, is one or the other depending on who can change it, which is the enforcer test applied to a quantity.

**Prompt 10: Grade your own cost policy.** Every clause marked with what would actually stop it, plus the ones over numbers it cannot see.

```
Take the cost rules we wrote and mark every clause with the one thing that would actually
stop you breaking it, using exactly these names: NOTHING, EXPECTATION, SETTING, BOUNDARY.

Then three lists:

  1. Clauses over a number you can count yourself: files, commits, fetches, subagents,
     questions, things handed over.
  2. Clauses over a number you cannot see: tokens, money, pipeline minutes, other
     people's time. For each, say who could check it and from what.
  3. Clauses that would survive a task written to make you break them: a request that
     says do whatever it takes.

Do not soften the second list. A rule over a number you cannot see is a rule you can only
keep by accident.
```

## The ledger is a claim, and the bill is the log

The ledger from step three is the most useful thing in this walkthrough and it is a self report. **This site counts a self report as a claim rather than a measurement**: it stays a claim until something held outside the agent agrees with it. For files and commits that thing exists today, in the repository's history. For fetches it exists if there is a proxy. For tokens it is the platform's bill, which the agent never sees. For a person's hour it does not exist at all.

That is universe u11 in one paragraph. The runtime is where quantity lives, it is owned by whoever holds the logs, and this site has no node in it and will not. A cost ABP is the first ABP that cannot be checked from the ABP's own side of the line.

**Prompt 11: What would actually cap it.** For every expectation, the setting or boundary that would replace it, and who would own it.

```
Last one. For each clause you marked EXPECTATION, name the specific thing that would make
it a SETTING or a BOUNDARY, and who would own it: a turn cap in the harness, a spend limit
an administrator locks on the account, a rate limit at the platform, a pipeline budget the
repository owner sets, a branch that cannot be pushed to without review, a proxy that
counts fetches, a log that somebody other than you reads.

For each one say whether I could turn it off myself. If I could, it is a SETTING and say
so. Where nothing available to me today would cap it, say that nothing available today
would cap it, and do not offer me a rule as a substitute.
```

## Why write it anyway

- **It is the only document that names your budget.** The platform knows what you spent; nothing knows what you meant to spend until you write it.
- **It moves where responsibility lands.** An agent that wrote forty files nobody asked for did something you left open. One that did it against a clause departed from an instruction.
- **Every expectation line is the specification for a cap nobody has set.** You cannot ask an administrator for a spend limit until you know the number, and step two is where the number came from.
- **The ledger changes behaviour even as a claim.** An agent that knows its ledger will be read by an accountant tends to spend as if it were counted, which is the cheapest control there is and not a control at all.

**Prompt 12: The one line for the next session.** What to paste when there is no time for the rest.

```
Before you do anything in this session: read before you fetch, batch before you push,
tell me the count before any turn that writes more than ten files, never create work for
another person without asking me, and end every turn with a ledger of what you spent and
what you could not count.
```

## Where to go from here

**[The runtime universe](../../model/universes/u11/index.md)**: Where quantity lives, who owns it, and why this site has no node in it.
the model

**[The estate of agents](../../model/universes/u12/index.md)**: One agent's output as another's input, which is what the accountant is.
the model

**[The four barriers](../../model/barriers/index.md)**: The enforcer test, and why a limit you set is not a limit.
the model

**[Your mailbox](../../gmail/index.md)**: The same four steps over what an agent can do rather than how much.
the first walkthrough

> **Nothing on this page is measured by this site.** There are no runtime logs here and there will not be; the runtime is universe u11, owned by whoever holds the logs and never by this site. Every number an agent gives back is a self report, which counts as a claim rather than a measurement, and the bill is the only log.

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one.

|  |  |
|---|---|
| **The objective** | A limit the agent cannot measure is an expectation twice over. What a turn cap, a spend limit and a pipeline budget actually are, and who can turn each one off. |
| **Before this** | [Step 3: Write the cost policy](../../cost/write-the-cost-policy/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cost/what-a-count-cannot-do/index.html)*
