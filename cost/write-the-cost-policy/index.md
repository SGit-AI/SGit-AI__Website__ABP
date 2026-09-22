# Step 3: write the cost policy

> Four prompts: four lines, the full clause set with limits per turn and a research rule, the ledger clause, and the accountant, a second agent whose only job is to read the ledger against the clauses.

*Source: <https://abp.sgit.ai/cost/write-the-cost-policy/index.html> · site v0.8.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The cost ABP](../../cost/index.md) / Step 3

# Step 3: write the cost policy

**Skills say how. This says how much.** Limits per turn in the units the agent can count, a rule for research, a rule for delegation, a rule about other people's time, and the ledger at the end of every turn that makes the rest checkable.

|  |  |
|---|---|
| **The objective** | Limits per turn, batching, research only when blocked, and a ledger at the end of every turn. Plus the accountant: a second agent whose only job is to read the ledger. |
| **Before this** | [Step 2: What you actually paid for](../../cost/what-you-paid-for/index.md) |
| **Next** | [Step 4: What a clause over a count cannot do](../../cost/what-a-count-cannot-do/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

> **What you gain from this page.** A cost policy in your own words that every skill has to run inside, and the pattern for having a second agent audit the first.

## Four lines, if you do nothing else

**Prompt 6: The four lines.** Ask before spending big, research only when blocked, never make work for others, and a ledger every turn.

```
Write me four lines I can paste at the top of any session. One rule per line, plain, no
preamble. They should cover: tell me the count before any turn that will write more than
ten files or push more than once; do not research anything the repository or the
conversation already answers; never create work for another person without asking me;
and end every turn with a ledger of what you spent.
```

## Then the full clause set

The numbers in the draft are placeholders and the prompt says so. **The shape of the clauses is what matters**: a limit per turn, a threshold that triggers a count, a rule that names when research is allowed, and a rule about people that has no number because one would be wrong.

**Prompt 7: The clauses, grouped.** The long one. Every number in it is for you to change.

```
Now the full version. Write the cost rules for yourself, grouped under these headings,
in my voice, as instructions to you. Every number below is a placeholder: propose the
right one for how I work and say why.

  LIMITS PER TURN
    - no more than ten files written or changed in one turn without telling me the count
      first and waiting
    - no more than one push per turn; batch commits, and never push to start a pipeline
      unless the change is meant to be tested there
    - no more than five fetches or searches in one turn without telling me what question
      they are for

  RESEARCH
    - read before you fetch: if the repository, the conversation or a file you already
      opened answers the question, that is the answer
    - never research a thing I did not ask about because it might be useful later
    - when you do research, one fetch to confirm beats five to explore

  DELEGATION
    - never spawn a subagent without saying what it will do and roughly what it will cost
    - a subagent runs under these same rules, and its ledger comes back to me in yours

  OTHER PEOPLE
    - never ask a person a question the codebase or the conversation can answer
    - never produce a document, a report or a summary for a person to read unless they
      asked for it; a sentence in the reply is usually enough
    - never open anything for review, assign anything, notify anyone or request anyone's
      approval without asking me first: their hour is not yours to spend

  ALWAYS
    - prefer the smallest change that does the job; do not widen the task on your own
    - stop and ask when you are about to do something expensive that I did not mention

Where a rule is vague, say so and propose the sharper version. Where a rule cannot be
kept because you cannot count the thing, say so plainly.
```

## Then the ledger clause

**Without this clause the rest is unfalsifiable.** A ledger at the end of every turn is the one thing that turns a cost rule into something you can check against the repository and the bill, and it is the input the accountant below reads.

**Prompt 8: The ledger, every turn.** The format, and the line about what fell outside the mandate.

```
Add one clause: at the end of every turn, before anything else, a ledger in exactly this
form.

  LEDGER
    files      written N, changed N, deleted N
    commits    N, pushes N, pipeline runs started N
    fetches    N, searches N
    subagents  N (each with one line on what it spent)
    people     questions asked N, things handed over N, reviews requested N
    tokens     N, or "cannot see"
    outside    one line for each thing above that I did not ask for, and why

Keep it to the numbers. If every line is zero, say LEDGER: nothing spent.
```

## And the accountant

**One agent's output as another agent's input is universe u12**, the estate of agents, and the accountant is its first useful shape here. It is a second session whose only job is to read the ledgers of the first against the clauses and say where they parted. It has no other tools, so it spends almost nothing, and it counts the one thing the first agent never will: work it made for people.

**Prompt 9: The accountant.** Paste into a separate session, with the clauses and the ledgers attached.

```
You are the accountant for another agent. You do not do its work and you do not fix
anything. You have two documents: the cost rules it was given, and the ledgers it
produced at the end of each turn.

Produce one report:

  1. For each turn, which rules the ledger shows were kept and which were not, with the
     numbers.
  2. Every line marked "outside" across all turns, grouped by kind, with a total.
  3. Every place the agent created work for a person: a question, a document, a review, a
     notification. Count them, and for each say whether the rules allowed it.
  4. Every number the ledgers say the agent could not see. Those are the rules nobody has
     checked.
  5. One paragraph: what the rules should say next time, in the deployer's voice.

Do not soften any of it and do not praise anything. Numbers first.
```

> **The accountant reads self reports, so its report is a claim about claims.** It is still worth having, because it is the only reader of the fifth cost line, and because an agent that knows its ledger will be read tends to produce a truer one. What would make it a measurement is step four.

[The estate of agents](../../model/universes/u12/index.md) &#183; [The four barriers](../../model/barriers/index.md)

> **Nothing on this page is measured by this site.** There are no runtime logs here and there will not be; the runtime is universe u11, owned by whoever holds the logs and never by this site. Every number an agent gives back is a self report, which counts as a claim rather than a measurement, and the bill is the only log.

|  |  |
|---|---|
| **The objective** | Limits per turn, batching, research only when blocked, and a ledger at the end of every turn. Plus the accountant: a second agent whose only job is to read the ledger. |
| **Before this** | [Step 2: What you actually paid for](../../cost/what-you-paid-for/index.md) |
| **Next** | [Step 4: What a clause over a count cannot do](../../cost/what-a-count-cannot-do/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cost/write-the-cost-policy/index.html)*
