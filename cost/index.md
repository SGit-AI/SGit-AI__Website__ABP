# The cost ABP: how much, not just what

> An Agent Behaviour Policy over how much an agent may spend: tokens, files, commits, fetches and other people's time. Four steps and twelve prompts, for a deployer watching the bill, the repository and the review queue all grow.

*Source: <https://abp.sgit.ai/cost/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The cost ABP

# Every ABP so far bounds what. This one bounds how much

**Four steps, twelve prompts, and one honest ending.** For anybody who has watched an agent write forty files nobody asked for, push twelve commits where one would do, research a question that was already answered, and hand three people something to review. You are paying for all of it, and nothing in the grant says a word about any of it.

> **Start here if you only do one thing.** Open the agent you are paying for, in the session you are worried about, and paste [the first prompt](../cost/what-it-spent/index.md). It counts what it can count and tells you what it cannot see, which is usually the bill.

## Cost is not a capability

A capability is in the grant or it is not. Cost is a property of every call the agent makes, whichever capability the call instances. **The grammar has one primitive for money, `write.budget.tenant`, and 2 of 16 published shapes grant it**, because it names spending against an account the agent holds, and an agent's own inference is billed to the deployer by the platform, not spent by the agent. There is no primitive for a count of anything.

*[A figure here in the page: two bands. The upper band is the ABP before the action, with its four objects, mandate, grant, delta and barrier. An arrow labelled every call is one instance of a capability leads to the lower band, the runtime, where quantity lives: calls in an interval, tokens seen by the platform, files, commits and fetches seen by the repository, and a person's hour, which nobody bills. Under it: a cost clause is a prohibition over a count; the grammar has one primitive for money and none for a count, so the clause carries what the grant cannot, and only a log outside the agent can say whether it was kept]*

So a cost ABP is the first ABP written over the runtime rather than over the grant. Its four objects are the same. Its mandate is a set of budgets in your words. Its grant is everything the agent can spend, which is everything it can do. Its delta is what it spent that you did not ask for. And its barrier, on nearly every row, is a sentence, because **almost nothing in a deployment caps a count**.

## Five things it spends, and one of them is never on a bill

*[A figure here in the page: a table of five things an agent spends. Tokens, paid by the account holder on the platform's bill, seen by the platform and usually not by the agent. Files written and changed, paid by the repository and whoever reads it next, seen exactly by the agent. Commits and pushes, paid by the pipeline per push, seen by the agent and the code host. Fetches and research, paid in tokens and time and one network reach each, seen by the agent and any proxy. And another person's hour, paid by a reviewer, an answerer or a reader, on nobody's bill and seen only by that person afterwards]*

**The fifth line is the one this walkthrough exists for.** An agent that asks a question, produces a document for a person to read, opens something for review or delegates to another agent that then does the same has spent an hour that no meter records. Organisations are starting to notice it as overhead without a source. The accountant on step three is the pattern that gives it one.

## Why this is an ABP and not another skill

|  | A skill | A behaviour policy |
|---|---|---|
| What it says | how to do one task well | what may not be done, and how much the doing may cost |
| Scope | one task, whenever it comes up | one agent in one deployment, across every task |
| Who writes it | whoever knows the task | whoever pays: the deployer, in their own words |
| How they relate | runs under the ABP | is what every skill has to fit inside |

A deployer watching the bill does not need another skill. They need the clauses that every skill has to run within, and a ledger at the end of every turn that says what the turn cost in the units they can check.

## The four steps

**[Step 1: What it has already spent](../cost/what-it-spent/index.md)**: Ask the agent to count what it can count in this session, and to say which numbers it cannot see at all.
about five minutes

**[Step 2: What you actually paid for](../cost/what-you-paid-for/index.md)**: Sort what it did into what you asked for, what it decided was needed, and what it would now call waste. Then say what waste means for you.
about five minutes

**[Step 3: Write the cost policy](../cost/write-the-cost-policy/index.md)**: Limits per turn, batching, research only when blocked, and a ledger at the end of every turn. Plus the accountant: a second agent whose only job is to read the ledger.
about five minutes

**[Step 4: What a clause over a count cannot do](../cost/what-a-count-cannot-do/index.md)**: A limit the agent cannot measure is an expectation twice over. What a turn cap, a spend limit and a pipeline budget actually are, and who can turn each one off.
about five minutes

## What you will have at the end

- **A ledger for one session**: files, commits, fetches, subagents, questions asked and things handed to people, counted by the agent, with the numbers it cannot see named as such.
- **A cost mandate**: what you want it to spend freely on, what it should batch or ask about, and what it must never spend, including other people's time.
- **A cost policy**: limits per turn, a research rule, a delegation rule, a never-create-work-for-others rule, and the ledger clause that makes the rest checkable.
- **And the straight answer**: a limit the agent cannot measure is an expectation twice over, and what would actually cap it.

> **Nothing on this page is measured by this site.** There are no runtime logs here and there will not be; the runtime is universe u11, owned by whoever holds the logs and never by this site. Every number an agent gives back is a self report, which counts as a claim rather than a measurement, and the bill is the only log.

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product.** No adjective on these pages attaches to one.

[Your mailbox, the first walkthrough](../gmail/index.md) &#183; [The runtime universe](../model/universes/u11/index.md) &#183; [`write.budget.tenant`](../model/capabilities/write.budget.tenant/index.md) &#183; [The four barriers](../model/barriers/index.md)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/cost/index.html)*
