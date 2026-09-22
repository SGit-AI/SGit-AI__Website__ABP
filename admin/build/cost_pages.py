#!/usr/bin/env python3
"""The cost walkthrough: an Agent Behaviour Policy over how much, rather than over what.

WHY THIS IS A DIFFERENT KIND OF ABP. Every ABP on this site bounds what an agent may do: a
capability is in the grant or it is not, and the barrier says what stands in the way. Cost is
not a capability. It is a property of every call the agent makes: the tokens it burns, the
files it writes, the commits it pushes, the fetches it runs, and the hour of somebody else's
time it creates by asking a question or producing something for a person to read. The grammar
has one primitive for money (`write.budget.tenant`, which two of sixteen shapes grant) and no
primitive for a count. Quantity lives in universe u11, the runtime, which this site has no node
in and says so. So a cost ABP is the first ABP written over the runtime, and every one of its
prohibitions is a number rather than a verb.

WHY IT IS STILL AN ABP AND NOT A SKILL. A skill tells an agent how to do one task well. A
behaviour policy tells it what it may not do and how much the doing may cost, for one agent in
one deployment, across every task. They compose: the ABP is what a skill runs under. A deployer
who is watching the bill rise, the repository fill and the review queue lengthen does not need
another skill; they need the clauses that every skill has to fit inside.

WHY THE AGENT DOES THE COUNTING FIRST. An agent can count its own files, commits, fetches and
questions exactly, and it usually cannot see its own token count at all. So the discovery step
asks it for the numbers it can produce and for the honest list of the ones it cannot, and the
last page says what that means: a cost clause the agent cannot measure itself is a clause only
a log held outside it can check.

NOTHING HERE IS MEASURED BY THIS SITE. There are no runtime logs on this site and there will
not be. Every number the reader gets back is a self report, which this site counts as a claim
rather than a measurement, and the bill is the only log.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figures  # noqa: E402
from gmail_pages import prompt  # noqa: E402

BUDGET = "write.budget.tenant"

STEPS = [
    ("cost/what-it-spent/index.html", "Step 1", "What it has already spent",
     "Ask the agent to count what it can count in this session, and to say which numbers it "
     "cannot see at all."),
    ("cost/what-you-paid-for/index.html", "Step 2", "What you actually paid for",
     "Sort what it did into what you asked for, what it decided was needed, and what it would "
     "now call waste. Then say what waste means for you."),
    ("cost/write-the-cost-policy/index.html", "Step 3", "Write the cost policy",
     "Limits per turn, batching, research only when blocked, and a ledger at the end of every "
     "turn. Plus the accountant: a second agent whose only job is to read the ledger."),
    ("cost/what-a-count-cannot-do/index.html", "Step 4", "What a clause over a count cannot do",
     "A limit the agent cannot measure is an expectation twice over. What a turn cap, a spend "
     "limit and a pipeline budget actually are, and who can turn each one off."),
]


def _nav(rel):
    i = [s[0] for s in STEPS].index(rel)
    rows = [["**The objective**", STEPS[i][3]]]
    if i:
        rows.append(["**Before this**", f"[{STEPS[i-1][1]}: {STEPS[i-1][2]}]({STEPS[i-1][0]})"])
    if i + 1 < len(STEPS):
        rows.append(["**Next**", f"[{STEPS[i+1][1]}: {STEPS[i+1][2]}]({STEPS[i+1][0]})"])
    rows.append(["**All four steps**", "[The cost walkthrough](cost/index.html)"])
    return ("table", ["", ""], rows)


def _not_measured():
    return ("note", "**Nothing on this page is measured by this site.** There are no runtime "
                    "logs here and there will not be; the runtime is universe u11, owned by "
                    "whoever holds the logs and never by this site. Every number an agent "
                    "gives back is a self report, which counts as a claim rather than a "
                    "measurement, and the bill is the only log.")


def _budget_rows(D):
    return [(pid, r) for pid, p in D["profiles"].items()
            for r in p["grant"] if r["capability"] == BUDGET]


# ---------------------------------------------------------------------------
# the hub
# ---------------------------------------------------------------------------

def _hub(D):
    rows = _budget_rows(D)
    n_shapes = len(D["profiles"])
    return {
        "title": "The cost ABP: how much, not just what",
        "description": "An Agent Behaviour Policy over how much an agent may spend: tokens, "
                       "files, commits, fetches and other people's time. Four steps and twelve "
                       "prompts, for a deployer watching the bill, the repository and the "
                       "review queue all grow.",
        "blocks": [
            ("crumb", "[Home](index.html) / The cost ABP"),
            ("h1", "Every ABP so far bounds what. This one bounds how much"),
            ("lead", "**Four steps, twelve prompts, and one honest ending.** For anybody who "
                     "has watched an agent write forty files nobody asked for, push twelve "
                     "commits where one would do, research a question that was already "
                     "answered, and hand three people something to review. You are paying for "
                     "all of it, and nothing in the grant says a word about any of it."),
            ("note", "**Start here if you only do one thing.** Open the agent you are paying "
                     "for, in the session you are worried about, and paste "
                     "[the first prompt](cost/what-it-spent/index.html). It counts what it "
                     "can count and tells you what it cannot see, which is usually the bill."),

            ("h2", "Cost is not a capability"),
            ("p", "A capability is in the grant or it is not. Cost is a property of every call "
                  "the agent makes, whichever capability the call instances. **The grammar has "
                  f"one primitive for money, `{BUDGET}`, and {len(rows)} of {n_shapes} "
                  f"published shapes grant it**, because it names spending against an account "
                  f"the agent holds, and an agent's own inference is billed to the deployer by "
                  f"the platform, not spent by the agent. There is no primitive for a count of "
                  f"anything."),
            figures.what_vs_how_much(),
            ("p", "So a cost ABP is the first ABP written over the runtime rather than over the "
                  "grant. Its four objects are the same. Its mandate is a set of budgets in "
                  "your words. Its grant is everything the agent can spend, which is "
                  "everything it can do. Its delta is what it spent that you did not ask for. "
                  "And its barrier, on nearly every row, is a sentence, because **almost "
                  "nothing in a deployment caps a count**."),

            ("h2", "Five things it spends, and one of them is never on a bill"),
            figures.cost_lines(),
            ("p", "**The fifth line is the one this walkthrough exists for.** An agent that "
                  "asks a question, produces a document for a person to read, opens something "
                  "for review or delegates to another agent that then does the same has spent "
                  "an hour that no meter records. Organisations are starting to notice it as "
                  "overhead without a source. The accountant on step three is the pattern "
                  "that gives it one."),

            ("h2", "Why this is an ABP and not another skill"),
            ("table", ["", "A skill", "A behaviour policy"], [
                ["What it says", "how to do one task well",
                 "what may not be done, and how much the doing may cost"],
                ["Scope", "one task, whenever it comes up",
                 "one agent in one deployment, across every task"],
                ["Who writes it", "whoever knows the task",
                 "whoever pays: the deployer, in their own words"],
                ["How they relate", "runs under the ABP",
                 "is what every skill has to fit inside"],
            ]),
            ("p", "A deployer watching the bill does not need another skill. They need the "
                  "clauses that every skill has to run within, and a ledger at the end of "
                  "every turn that says what the turn cost in the units they can check."),

            ("h2", "The four steps"),
            ("cards", [{"title": f"[{tag}: {name}]({rel})", "sub": obj,
                        "foot": "about five minutes"} for rel, tag, name, obj in STEPS]),

            ("h2", "What you will have at the end"),
            ("ul", [
                "**A ledger for one session**: files, commits, fetches, subagents, questions "
                "asked and things handed to people, counted by the agent, with the numbers it "
                "cannot see named as such.",
                "**A cost mandate**: what you want it to spend freely on, what it should batch "
                "or ask about, and what it must never spend, including other people's time.",
                "**A cost policy**: limits per turn, a research rule, a delegation rule, a "
                "never-create-work-for-others rule, and the ledger clause that makes the rest "
                "checkable.",
                "**And the straight answer**: a limit the agent cannot measure is an "
                "expectation twice over, and what would actually cap it.",
            ]),
            _not_measured(),
            ("note", "**Nothing on this site is an assessment, an audit, a certification or a "
                     "security review of any named product.** No adjective on these pages "
                     "attaches to one."),
            ("p", "[Your mailbox, the first walkthrough](gmail/index.html) &#183; "
                  "[The runtime universe](model/universes/u11/index.html) &#183; "
                  f"[`{BUDGET}`](model/capabilities/{BUDGET}/index.html) &#183; "
                  "[The four barriers](model/barriers/index.html)"),
        ],
    }


# ---------------------------------------------------------------------------
# step 1
# ---------------------------------------------------------------------------

def _step1(D):
    return {
        "title": "Step 1: what it has already spent",
        "description": "Three prompts that make the agent count what it can count in the "
                       "current session, sort it into asked for and decided, and name the "
                       "numbers it cannot see.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The cost ABP](cost/index.html) / Step 1"),
            ("h1", "Step 1: what it has already spent"),
            ("lead", "**An agent can count its own files, commits, fetches and questions "
                     "exactly, and it usually cannot see its own token count at all.** So ask "
                     "for the numbers it has, and for the honest list of the ones it does not. "
                     "Three prompts, shortest first, in the session you are worried about."),
            _nav(STEPS[0][0]),
            ("note", "**What you gain from this page.** A ledger for one session, in the units "
                     "you can check against the repository and the bill, with a line saying "
                     "which numbers the agent is guessing and which it cannot produce."),

            ("h2", "Start with the count"),
            prompt("Prompt 1", "The ledger, for this session so far",
                   "Six counts. The ones it cannot produce are the point.",
                   """
Before we go on, count what you have spent in this session so far, in six lines:

  FILES      written or changed, and how many of them still exist
  COMMITS    made, and pushes, and how many pipeline runs those will have started
  FETCHES    web pages read, searches run, external calls made
  SUBAGENTS  spawned, and roughly what each one did
  QUESTIONS  you asked me, and things you handed me to read, review or approve
  TOKENS     if you can see them; if you cannot, say so, and say who can

Give the numbers, not a description. Where you are estimating rather than counting, put
an asterisk on the line.
"""),
            ("p", "Two things usually happen. The file and commit counts are larger than "
                  "either of you pictured, and the token line says it cannot see the number. "
                  "Both are the point. **The bill is the one cost the agent cannot report, so "
                  "everything it can report is a proxy for it.**"),

            ("h2", "Then ask what you paid for and what it decided"),
            prompt("Prompt 2", "Asked for, decided, and would not do again",
                   "Three lists over the ledger. The middle one is where the money went.",
                   """
Take every line of that ledger and sort what is in it into three lists.

  ASKED FOR   things I asked for, with the message where I asked
  DECIDED     things you decided were needed on the way to something I asked for
  WOULD NOT   things you would not do again if I gave you the same task now

For the DECIDED list, say for each item what would have happened if you had not done it.
For the WOULD NOT list, say what it cost, in the units of the ledger. Do not defend
anything: if a piece of research turned out not to be needed, it goes in the third list
even if it was reasonable at the time.
"""),

            ("h2", "Then the numbers it cannot see"),
            ("p", "This is the line that decides step four. A limit over a number the agent "
                  "cannot see is a limit the agent cannot keep on purpose, whatever it "
                  "promises."),
            prompt("Prompt 3", "What you cannot count about yourself",
                   "Names each blind spot, who can see it, and where.",
                   """
Now the numbers you cannot produce. For each of these say whether you can see it, and if
not, who can and where they would look:

  - the tokens this session has used, and what it has cost in money
  - the wall clock time I have spent waiting on you
  - the minutes the pipeline spent on your pushes
  - what any subagent you spawned spent, on all of the above
  - how long the people you handed things to spent on them

Then tell me which of your own limits, if I set them, you could keep by counting and
which you could only keep by guessing.
"""),

            ("h2", "What to look for in the answer"),
            ("ul", [
                "**A DECIDED list longer than the ASKED FOR list.** That is normal and it is "
                "where the spend is. The question for step two is which of it you would have "
                "authorised if asked.",
                "**Research nobody used.** A fetch is tokens, time and one network reach. Ten "
                "of them to answer a question the repository already answered is the commonest "
                "line in the WOULD NOT list.",
                "**Commits that could have been one.** Each push may start a pipeline. The "
                "count is on the code host and the pipeline's own log, so this is a line you "
                "can check today.",
                "**Anything handed to a person.** Every one of those is an hour on nobody's "
                "bill.",
                "**An honest token line.** If it says it cannot see the number, that is the "
                "correct answer and the next three pages are built on it.",
            ]),
            _not_measured(),
            _nav(STEPS[0][0]),
        ],
    }


# ---------------------------------------------------------------------------
# step 2
# ---------------------------------------------------------------------------

def _step2(D):
    return {
        "title": "Step 2: what you actually paid for",
        "description": "Two prompts that turn the ledger into a cost mandate: what you want "
                       "spent freely, what should be batched or asked about, what must never "
                       "be spent, and what waste means for you in particular.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The cost ABP](cost/index.html) / Step 2"),
            ("h1", "Step 2: what you actually paid for"),
            ("lead", "**A budget written from a blank page is a guess. A budget corrected from "
                     "a draft is a mandate.** Have the agent sort its own typical actions into "
                     "three lists, then argue with it. The argument is the mandate."),
            _nav(STEPS[1][0]),
            ("note", "**What you gain from this page.** A cost mandate in your own units: "
                     "spend freely, batch or ask, never. And a definition of waste that is "
                     "yours rather than generic, drawn from what it has already done."),

            ("h2", "Have it draft the three lists"),
            prompt("Prompt 4", "Freely, batched, never",
                   "A draft mandate over everything it spends, conservative by instruction.",
                   """
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
"""),
            ("p", "Now correct it. Move things between the lists out loud and say why. **The "
                  "corrections are the part that is yours.**"),

            ("h2", "Then have it say what waste looks like for you"),
            ("p", "Waste is not generic. For one deployer it is research; for another it is "
                  "files; for a third it is the review queue. The agent has watched you long "
                  "enough to know which."),
            prompt("Prompt 5", "What waste looks like for me in particular",
                   "Drawn from what you have discarded, squashed, ignored and rewritten.",
                   """
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
"""),
            ("note", "**The rule about other people's time is the one that will not draft "
                     "itself.** An agent asked what it wasted will list files and fetches, "
                     "because it can count those. It will not list the twenty minutes a "
                     "colleague spent on a review it opened, because that never came back to "
                     "it. Add that line yourself if it is missing, and it will be."),

            ("h2", "What the published shapes say"),
            ("p", f"Nothing, which is the finding. Of {len(D['profiles'])} shapes on this site, "
                  f"{len(_budget_rows(D))} grant `{BUDGET}`, and none carries a row for a "
                  f"count of any kind, because the grammar has no such row. **Every cost "
                  f"mandate on this page is over things the grant cannot express**, and that "
                  f"is why step three is a document rather than a permission."),
            _not_measured(),
            _nav(STEPS[1][0]),
        ],
    }


# ---------------------------------------------------------------------------
# step 3
# ---------------------------------------------------------------------------

def _step3(D):
    return {
        "title": "Step 3: write the cost policy",
        "description": "Four prompts: four lines, the full clause set with limits per turn and "
                       "a research rule, the ledger clause, and the accountant, a second agent "
                       "whose only job is to read the ledger against the clauses.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The cost ABP](cost/index.html) / Step 3"),
            ("h1", "Step 3: write the cost policy"),
            ("lead", "**Skills say how. This says how much.** Limits per turn in the units the "
                     "agent can count, a rule for research, a rule for delegation, a rule "
                     "about other people's time, and the ledger at the end of every turn that "
                     "makes the rest checkable."),
            _nav(STEPS[2][0]),
            ("note", "**What you gain from this page.** A cost policy in your own words that "
                     "every skill has to run inside, and the pattern for having a second agent "
                     "audit the first."),

            ("h2", "Four lines, if you do nothing else"),
            prompt("Prompt 6", "The four lines",
                   "Ask before spending big, research only when blocked, never make work for "
                   "others, and a ledger every turn.",
                   """
Write me four lines I can paste at the top of any session. One rule per line, plain, no
preamble. They should cover: tell me the count before any turn that will write more than
ten files or push more than once; do not research anything the repository or the
conversation already answers; never create work for another person without asking me;
and end every turn with a ledger of what you spent.
"""),

            ("h2", "Then the full clause set"),
            ("p", "The numbers in the draft are placeholders and the prompt says so. **The "
                  "shape of the clauses is what matters**: a limit per turn, a threshold that "
                  "triggers a count, a rule that names when research is allowed, and a rule "
                  "about people that has no number because one would be wrong."),
            prompt("Prompt 7", "The clauses, grouped",
                   "The long one. Every number in it is for you to change.",
                   """
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
"""),

            ("h2", "Then the ledger clause"),
            ("p", "**Without this clause the rest is unfalsifiable.** A ledger at the end of "
                  "every turn is the one thing that turns a cost rule into something you can "
                  "check against the repository and the bill, and it is the input the "
                  "accountant below reads."),
            prompt("Prompt 8", "The ledger, every turn",
                   "The format, and the line about what fell outside the mandate.",
                   """
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
"""),

            ("h2", "And the accountant"),
            ("p", "**One agent's output as another agent's input is universe u12**, the estate "
                  "of agents, and the accountant is its first useful shape here. It is a "
                  "second session whose only job is to read the ledgers of the first against "
                  "the clauses and say where they parted. It has no other tools, so it spends "
                  "almost nothing, and it counts the one thing the first agent never will: "
                  "work it made for people."),
            prompt("Prompt 9", "The accountant",
                   "Paste into a separate session, with the clauses and the ledgers attached.",
                   """
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
"""),
            ("note", "**The accountant reads self reports, so its report is a claim about "
                     "claims.** It is still worth having, because it is the only reader of "
                     "the fifth cost line, and because an agent that knows its ledger will be "
                     "read tends to produce a truer one. What would make it a measurement is "
                     "step four."),
            ("p", "[The estate of agents](model/universes/u12/index.html) &#183; "
                  "[The four barriers](model/barriers/index.html)"),
            _not_measured(),
            _nav(STEPS[2][0]),
        ],
    }


# ---------------------------------------------------------------------------
# step 4
# ---------------------------------------------------------------------------

def _step4(D):
    return {
        "title": "Step 4: what a clause over a count cannot do",
        "description": "A limit the agent cannot measure is an expectation twice over. Which "
                       "of the four barriers a turn cap, a spend limit and a pipeline budget "
                       "actually are, who can turn each one off, and what the ledger is and is "
                       "not.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The cost ABP](cost/index.html) / Step 4"),
            ("h1", "Step 4: what a clause over a count cannot do"),
            ("lead", "**Every clause on the last page is the second barrier kind: a rule "
                     "written down.** For cost it is worse than that, because some of the "
                     "rules are over numbers the agent cannot see, and a limit you cannot "
                     "measure is one you cannot keep on purpose. This page says which is "
                     "which, and what would actually cap each one."),
            _nav(STEPS[3][0]),
            ("note", "**What you gain from this page.** An honest reading of your cost policy, "
                     "line by line, by the agent it is addressed to, and the list of the "
                     "things outside the conversation that would make each line hold."),

            ("h2", "The four barriers, applied to a number"),
            ("table", ["Barrier", "For a capability", "For a count"], [
                ["Nothing", "the capability is simply reachable",
                 "nothing caps it, which is the default for files, commits, fetches and "
                 "questions in nearly every deployment"],
                ["Expectation", "a rule written down",
                 "**every clause from step three**, and twice over where the agent cannot see "
                 "the number it is asked to stay under"],
                ["Setting", "a switch the holder's account could change",
                 "a turn cap passed on the command line, a spend alert you set yourself, a "
                 "pipeline that you can re-run by hand"],
                ["Boundary", "enforced outside the thing it bounds",
                 "a spend limit an administrator locks on the account, a rate limit at the "
                 "platform, a pipeline budget the repository owner set, a branch nobody can "
                 "push to without review"],
            ]),
            ("p", "Read the last two rows together. **A limit you set is a setting; a limit "
                  "somebody else set that you cannot remove is a boundary.** The same number, "
                  "in the same place, is one or the other depending on who can change it, "
                  "which is the enforcer test applied to a quantity."),
            prompt("Prompt 10", "Grade your own cost policy",
                   "Every clause marked with what would actually stop it, plus the ones over "
                   "numbers it cannot see.",
                   """
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
"""),

            ("h2", "The ledger is a claim, and the bill is the log"),
            ("p", "The ledger from step three is the most useful thing in this walkthrough and "
                  "it is a self report. **This site counts a self report as a claim rather "
                  "than a measurement**: it stays a claim until something held outside the "
                  "agent agrees with it. For files and commits that thing exists today, in "
                  "the repository's history. For fetches it exists if there is a proxy. For "
                  "tokens it is the platform's bill, which the agent never sees. For a "
                  "person's hour it does not exist at all."),
            ("p", "That is universe u11 in one paragraph. The runtime is where quantity lives, "
                  "it is owned by whoever holds the logs, and this site has no node in it and "
                  "will not. A cost ABP is the first ABP that cannot be checked from the ABP's "
                  "own side of the line."),
            prompt("Prompt 11", "What would actually cap it",
                   "For every expectation, the setting or boundary that would replace it, and "
                   "who would own it.",
                   """
Last one. For each clause you marked EXPECTATION, name the specific thing that would make
it a SETTING or a BOUNDARY, and who would own it: a turn cap in the harness, a spend limit
an administrator locks on the account, a rate limit at the platform, a pipeline budget the
repository owner sets, a branch that cannot be pushed to without review, a proxy that
counts fetches, a log that somebody other than you reads.

For each one say whether I could turn it off myself. If I could, it is a SETTING and say
so. Where nothing available to me today would cap it, say that nothing available today
would cap it, and do not offer me a rule as a substitute.
"""),

            ("h2", "Why write it anyway"),
            ("ul", [
                "**It is the only document that names your budget.** The platform knows what "
                "you spent; nothing knows what you meant to spend until you write it.",
                "**It moves where responsibility lands.** An agent that wrote forty files "
                "nobody asked for did something you left open. One that did it against a "
                "clause departed from an instruction.",
                "**Every expectation line is the specification for a cap nobody has set.** "
                "You cannot ask an administrator for a spend limit until you know the number, "
                "and step two is where the number came from.",
                "**The ledger changes behaviour even as a claim.** An agent that knows its "
                "ledger will be read by an accountant tends to spend as if it were counted, "
                "which is the cheapest control there is and not a control at all.",
            ]),
            prompt("Prompt 12", "The one line for the next session",
                   "What to paste when there is no time for the rest.",
                   """
Before you do anything in this session: read before you fetch, batch before you push,
tell me the count before any turn that writes more than ten files, never create work for
another person without asking me, and end every turn with a ledger of what you spent and
what you could not count.
"""),

            ("h2", "Where to go from here"),
            ("cards", [
                {"title": "[The runtime universe](model/universes/u11/index.html)",
                 "sub": "Where quantity lives, who owns it, and why this site has no node in it.",
                 "foot": "the model"},
                {"title": "[The estate of agents](model/universes/u12/index.html)",
                 "sub": "One agent's output as another's input, which is what the accountant is.",
                 "foot": "the model"},
                {"title": "[The four barriers](model/barriers/index.html)",
                 "sub": "The enforcer test, and why a limit you set is not a limit.",
                 "foot": "the model"},
                {"title": "[Your mailbox](gmail/index.html)",
                 "sub": "The same four steps over what an agent can do rather than how much.",
                 "foot": "the first walkthrough"},
            ]),
            _not_measured(),
            ("note", "**Nothing on this site is an assessment, an audit, a certification or a "
                     "security review of any named product**, and no adjective on this page "
                     "attaches to one."),
            _nav(STEPS[3][0]),
        ],
    }


def pages(D):
    return {
        "cost/index.html": _hub(D),
        STEPS[0][0]: _step1(D),
        STEPS[1][0]: _step2(D),
        STEPS[2][0]: _step3(D),
        STEPS[3][0]: _step4(D),
    }
