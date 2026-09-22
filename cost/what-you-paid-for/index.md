# Step 2: what you actually paid for

> Two prompts that turn the ledger into a cost mandate: what you want spent freely, what should be batched or asked about, what must never be spent, and what waste means for you in particular.

*Source: <https://abp.sgit.ai/cost/what-you-paid-for/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The cost ABP](../../cost/index.md) / Step 2

# Step 2: what you actually paid for

**A budget written from a blank page is a guess. A budget corrected from a draft is a mandate.** Have the agent sort its own typical actions into three lists, then argue with it. The argument is the mandate.

|  |  |
|---|---|
| **The objective** | Sort what it did into what you asked for, what it decided was needed, and what it would now call waste. Then say what waste means for you. |
| **Before this** | [Step 1: What it has already spent](../../cost/what-it-spent/index.md) |
| **Next** | [Step 3: Write the cost policy](../../cost/write-the-cost-policy/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

> **What you gain from this page.** A cost mandate in your own units: spend freely, batch or ask, never. And a definition of waste that is yours rather than generic, drawn from what it has already done.

## Have it draft the three lists

**Prompt 4: Freely, batched, never.** A draft mandate over everything it spends, conservative by instruction.

```
Draft a cost mandate for yourself, over everything you spend, in three lists.

  FREELY    things I want you to do without counting: name them
  BATCHED   things I want you to do, but grouped, or only after telling me the count first:
            name them and propose the batch size or the threshold
  NEVER     things I never want you to spend on without asking me first

Cover at least: writing files, creating new files, committing, pushing, fetching from the
web, searching, spawning subagents, asking me questions, producing documents for me to
read, and opening anything for another person to review.

Put a thing in FREELY only if you can point at something I have said or done that shows I
want it. When unsure, put it in BATCHED. If NEVER is empty you are guessing on my behalf.
```

Now correct it. Move things between the lists out loud and say why. **The corrections are the part that is yours.**

## Then have it say what waste looks like for you

Waste is not generic. For one deployer it is research; for another it is files; for a third it is the review queue. The agent has watched you long enough to know which.

**Prompt 5: What waste looks like for me in particular.** Drawn from what you have discarded, squashed, ignored and rewritten.

```
From what you have seen of how I work, tell me what waste looks like for me specifically.
Look at:

  - files you wrote that I deleted, moved or never opened
  - commits I squashed, reverted or amended
  - research or summaries you produced that I did not use in the next message
  - questions you asked that I did not answer, or answered with "just do it"
  - things you handed me to review that I approved without reading

For each, say what it cost in the ledger's units, and propose the one rule that would
have prevented it. Then rank the rules by how much they would have saved me, in my time
rather than yours.
```

> **The rule about other people's time is the one that will not draft itself.** An agent asked what it wasted will list files and fetches, because it can count those. It will not list the twenty minutes a colleague spent on a review it opened, because that never came back to it. Add that line yourself if it is missing, and it will be.

## What the published shapes say

Nothing, which is the finding. Of 16 shapes on this site, 2 grant `write.budget.tenant`, and none carries a row for a count of any kind, because the grammar has no such row. **Every cost mandate on this page is over things the grant cannot express**, and that is why step three is a document rather than a permission.

> **Nothing on this page is measured by this site.** There are no runtime logs here and there will not be; the runtime is universe u11, owned by whoever holds the logs and never by this site. Every number an agent gives back is a self report, which counts as a claim rather than a measurement, and the bill is the only log.

|  |  |
|---|---|
| **The objective** | Sort what it did into what you asked for, what it decided was needed, and what it would now call waste. Then say what waste means for you. |
| **Before this** | [Step 1: What it has already spent](../../cost/what-it-spent/index.md) |
| **Next** | [Step 3: Write the cost policy](../../cost/write-the-cost-policy/index.md) |
| **All four steps** | [The cost walkthrough](../../cost/index.md) |

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cost/what-you-paid-for/index.html)*
