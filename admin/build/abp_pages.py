#!/usr/bin/env python3
"""Every page computed from the data: the model, the five examples, and the data layer's own page.

NOTHING ON THESE PAGES IS TYPED IN. Every number, every glyph, every row and every label field
is computed from `data/` at build time, which is what makes a merged pull request against a
JSON file change the site with no hand in between. It is also the only way the provenance line
can be trusted: a page that states 21 of 99 rows measured, and got that from a constant, is
asserting what the data is careful to qualify.

Three rules govern what these pages may show.

  · EVERY PROHIBITION CARRIES ITS BARRIER. A prohibition displayed without one is a claim the
    site cannot support, and at the first three barriers it is a sentence rather than a control.
  · EVERY PAGE WITH CAPABILITY ROWS CARRIES ITS PROVENANCE. How many measured, how many
    derived, and when. The published map does it and this site does not get to be less careful.
  · NO SCORE. Not a rating, not a traffic light, not a risk level, not a severity ranking. The
    one permitted ordering is irreversible first, stated as a property of the action.

The graph rule that shapes the page set is the third one: never render the whole graph, render
the result of a query. So there is no map of everything here. Each page answers ONE query --
this profile's grant, this mandate's delta, this capability across every profile -- and links
to the next.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402
import graph  # noqa: E402
import lexicon_pages  # noqa: E402
import shell  # noqa: E402
import universes  # noqa: E402

AS_AT = "11 September 2026"
# The second of the three clocks. An ABP is exactly as fresh as the twin, and
# this site has no twin connected to anything: the shapes here are published
# profiles rather than a synchronised environment. That is the honest value and
# it belongs on the label rather than in a footnote.
SYNCED = "no twin: these shapes are published profiles, not a synchronised environment"
MAP = "https://what-can-it-do.games.sgit.ai/map/index.html"
GRAPHS = "https://graphs.sgit.ai/"
TWINS = "https://twins.sgit.ai/"
RISKS = "https://risks.sgit.ai/"
CODING = "https://coding.sgit.ai/"
GUIDANCE = "https://sgit.ai/docs/guidance/index.html"
LTO = "https://sgit.ai/demos/vaults/licence-to-operate/index.html"

# The published glyph for each barrier, and the plain name this site uses in prose. The glyph
# is on every cell so that the reading never depends on colour.
# The literal glyph, not an HTML entity: the same string has to work in the page and in the
# markdown twin, and an entity renders as tag soup in the twin. These five characters are the
# only non-ASCII the release gate allows outside the promoted data, and they are allowed
# because they are DATA: the published enforcement model puts one on every cell so that the
# reading never depends on colour.
GLYPH = {"none": "●", "expectation": "◉", "setting": "◐",
         "boundary": "○", "absent": "·"}
UNDO_WORD = {"no": "cannot be undone", "with-effort": "undone at a cost", "yes": "undone"}

# The five, in the order the pack names them, with the reason each one is in the set. The
# third is the one to read first if only one gets read: one setting, two documents.
EXAMPLES = [
    ("chatgpt-web-no-connectors", "openai/chatgpt-web/default", "chat-no-connectors",
     "Chat in the browser, nothing connected",
     "The smallest grant in the set",
     "A reader who does not believe an agent can do much starts here, and finds that the "
     "delta is still not empty. It establishes the four objects with the fewest moving parts."),
    ("claude-code-cli-confirmations-enabled", "anthropic/claude-code/local-default",
     "coding-assistant-on-my-machine",
     "A coding agent on your own machine, confirmations on",
     "The confirmation is a barrier, and you can see which row it sits on",
     "This is where the barrier stops being a column and becomes the argument. A confirmation "
     "prompt is a setting the agent's own account could change, which is the third row, not "
     "the fourth."),
    ("claude-code-cli-confirmations-disabled", "anthropic/claude-code/local-confirmations-off",
     "coding-assistant-on-my-machine",
     "The same coding agent, confirmations off",
     "The same agent, one setting different",
     "Two documents for one agent, differing in one line. It makes the case that the ABP is "
     "about the deployment rather than the product in a way no paragraph can."),
    ("browser-extension-broad-host-permissions",
     "generic/browser-extension/broad-host-permissions", "browser-extension-i-installed",
     "A browser extension with broad host permissions",
     "Other people's data, and the mandate nobody wrote down",
     "The pages you visit were not all yours to hand over. This is where the mandate reaches "
     "further than your own material."),
    ("github-actions-hosted-runner", "github/actions-runner/ci", "ci-job",
     "A CI job on a hosted runner, under a service account",
     "Persistence, and reach beyond the turn",
     "A service account rather than a person, a push to a code host, and the irreversible "
     "class arriving in a deployment nobody thinks of as an agent."),
]


# ---------------------------------------------------------------------------
# shared blocks
# ---------------------------------------------------------------------------

def provenance_block(rows, extra="", scope="site"):
    """The line that is not optional. The published map states that 21 of its 99 rows were
    measured and the rest derived; a page that hides the ratio is asserting what the map is
    careful to qualify.

    Since v0.4.4 a page that carries rows from every shape (`scope="site"`) also carries
    the contributed rows' own line, because a reader is entitled to know which rows came
    from the map and which from a contributor, and the two were obtained differently. A
    page about one promoted shape (`scope="shape"`) carries only the map's line, because
    every row on it is the map's."""
    prov = load()["provenance"]
    text = (f"**Provenance.** {rows['measured']} of {rows['total']} capability rows "
            f"{'from the published map ' if scope == 'site' else 'on this page '}"
            f"were measured, meaning seen directly on the thing itself. The other "
            f"{rows['derived']} were derived from what the deployment architecturally is, or "
            f"from the vendor's published documentation. "
            f"{'Those rows trace' if scope == 'site' else 'Every row traces'} to "
            f"[the published capability map]({MAP}), retrieved "
            f"{shell.ascii_safe(prov['retrieved'])}, content hash "
            f"`{prov['content_hash'][:26]}`. "
            f"[The source bytes](data/upstream/pack.json).")
    c = prov.get("contributed")
    if scope == "site" and c and c["rows"]["total"]:
        text += (f" **A further {c['rows']['total']} rows across {c['shapes']} shapes were "
                 f"contributed by {c['contributor']}**, {c['rows']['measured']} of them at the "
                 f"contributor's measured tier and {c['rows']['derived']} read from vendor "
                 f"documentation on a date; this site did not observe any of them and keeps "
                 f"the tier as stated. Retrieved {shell.ascii_safe(c['retrieved'])}, content "
                 f"hash `{c['content_hash'][:26]}`. "
                 f"[The contributed bytes](data/contributed/riskmandate/manifest.json).")
    return ("note", text + (" " + extra if extra else ""))


def _lower_first(s):
    """A product name that starts with an article reads wrong after `for'. Only the first
    letter, and only when the second is lower case, so `ChatGPT' and `GitHub' keep their
    capitals."""
    return s[0].lower() + s[1:] if len(s) > 1 and s[1].islower() else s


def barrier_legend():
    D = load()
    rows = [[GLYPH[b["id"]], b["id"], shell.ascii_safe(b["published_meaning"]),
             "**yes**" if b["is_control"] else "no"]
            for b in D["barriers"]["barriers"]]
    return ("table", ["", "Barrier", "What stands in the way", "Is it a control"], rows)


_D = None


def load():
    global _D
    if _D is None:
        _D = abp.load()
    return _D


def cap_href(cap_id, ):
    return f"model/capabilities/{cap_id}/index.html"


def example_href(slug):
    return f"examples/{slug}/index.html"


def grant_table(profile, D, mandate=None, dlt=None):
    """The leaflet: every granted primitive with its barrier, its undo class, its provenance
    and, where there is a mandate, what the mandate said about it. Irreversible first."""
    head = ["", "Capability", "Undo", "Barrier", "Known by"]
    if mandate:
        head.append("The mandate")
    rows = []
    want, refused = set(mandate["want"]) if mandate else set(), \
        set(mandate["do_not_want"]) if mandate else set()
    for r in abp.order(profile["grant"], D):
        c = D["by_id"][r["capability"]]
        row = [GLYPH[r["barrier"]],
               f"[`{r['capability']}`]({cap_href(r['capability'])}) {c['gloss']}",
               f"{c['undo']}",
               f"{r['barrier']}" + ("" if D["is_control"][r["barrier"]] else " (not a control)"),
               r["evidence"]]
        if mandate:
            row.append("**authorised**" if r["capability"] in want else
                       ("**excess** (refused)" if r["capability"] in refused
                        else "**excess** (unstated)"))
        rows.append(row)
    return ("table", head, rows)


def label_block(profile, mandate, dlt, D):
    rows = [[k, f"**{v}**", note] for k, v, note in abp.label(profile, mandate, dlt, D, AS_AT)]
    return ("table", ["Field", "Value", "Meaning"], rows)


def prohibition_table(dlt, D):
    rows = []
    for p in abp.prohibitions(dlt, D):
        rows.append([
            GLYPH[p["barrier_today"]],
            p["sentence"] + f" [`{p['capability']}`]({cap_href(p['capability'])})",
            f"{p['barrier_today']}",
            "**enforced**" if p["enforced_today"] else "**not enforced** (a sentence, not a control)",
            ("already enforced above the grant" if p["enforced_today"]
             else shell.ascii_safe(p["layer_if_enforced"] or "no published reduction")),
        ])
    return ("table",
            ["", "Prohibition", "Barrier today", "Enforced today", "Layer a control would sit at"],
            rows)


# ---------------------------------------------------------------------------
# the examples
# ---------------------------------------------------------------------------

def example_page(slug, profile_id, mandate_id, name, why, note, D):
    p = D["profiles"][profile_id]
    m = D["mandates"][mandate_id]
    dlt = abp.delta(p, m, D)
    pro = abp.prohibitions(dlt, D)
    n_sent = sum(1 for x in pro if not x["enforced_today"])
    reach = ", ".join(f"**{k}** means {shell.ascii_safe(v)}"
                      for k, v in p["reach_names"].items()) or None

    blocks = [
        ("crumb", "[Home](index.html) / [Examples](examples/index.html) / " + name),
        ("h1", name),
        ("p", f"**The deployment shape:** {shell.ascii_safe(p['product'])}, "
              f"variant `{p['variant']}`."),
        ("lead", f"{why}. {note}"),

        ("h2", "Before you scroll"),
        ("note", f"**Write down a number.** Of the {D['capabilities']['count']} capability "
                 f"primitives, how many do you think this deployment has? And of those, how "
                 f"many do you think the person who deployed it asked for? The page answers "
                 f"both below. Writing the guess down first is the one thing that makes a "
                 f"static page do any of the work [the game]({MAP}) does."),

        ("h2", "The label"),
        ("p", "One line, on the outside, for anybody. Two numbers matter: **excess** answers "
              "the question this document exists for, and **unbounded excess** is the only "
              "number on it that buying a control moves."),
        label_block(p, m, dlt, D),
        ("note", "**There is no score on this label, and there will not be one.** The same ABP "
                 "is dangerous in one deployment and harmless in the next and nothing about the "
                 "document changed. A policy cannot be dangerous; a deployment can. Risk is a "
                 f"function of the ABP, the assets, the consequences and the date, and only "
                 f"the first of those is here. The score belongs to [the risk work above "
                 f"it]({RISKS}), where the assets are known and a named person signs."),

        ("h2", "1. The shape"),
        ("p", shell.ascii_safe(p["description"])),
        ("p", f"Tools in this shape: {', '.join('`' + shell.ascii_safe(t) + '`' for t in p['tools'])}. "
              f"Profile version `{p['profile_version']}`, surface `{p['surface']}`."),
    ]
    if reach:
        blocks.append(("p", f"What the reach classes mean here, which is the profile's to say "
                            f"rather than the grammar's: {reach}."))
    if p["not_reachable"]:
        blocks += [("p", "**What it cannot reach, and why.** A grant is as much about the "
                         "boundaries that hold as the ones that do not."),
                   ("table", ["What", "Why", "Source"],
                    [[shell.ascii_safe(x["what"]), shell.ascii_safe(x["why"]),
                      f"`{shell.ascii_safe(x.get('source', ''))}`"] for x in p["not_reachable"]])]

    blocks += [
        ("h2", "2. The grant, measured"),
        ("p", f"Everything the agent can do: **{p['grant_size']} of "
              f"{D['capabilities']['count']}** primitives. Ordered irreversible first, then "
              f"weakest barrier first. **Reversibility is a property of the action, not a "
              f"severity**, and stating it as the reason is what keeps the ordering "
              f"descriptive."),
        grant_table(p, D, m, dlt),
        barrier_legend(),

        ("h2", "3. The mandate, elicited"),
        ("p", f"**{shell.ascii_safe(m['label'])}.** " + shell.ascii_safe(m["description"])),
        ("p", f"A mandate is elicited rather than measured, in minutes, because the deployer "
              f"already knows it. This one was not: it is a first draft written to be argued "
              f"with, authored {m['authored']} by {shell.ascii_safe(m['authored_by'])}. It "
              f"authorises **{len(m['want'])}** primitives, refuses **{len(m['do_not_want'])}** "
              f"and says nothing either way about **{len(m['unstated'])}**. "
              f"[Propose a change to it](data/index.html)."),
    ]
    if m["notes"]:
        blocks.append(("table", ["Capability", "What the mandate says about it"],
                       [[f"[`{k}`]({cap_href(k)})", shell.ascii_safe(v)]
                        for k, v in m["notes"].items()]))

    blocks += [
        ("h2", "4. The delta, derived"),
        ("note", f"**This delta is derived and never authored.** Nobody wrote it. It is the "
                 f"output of a computation over the grant and the mandate, stored at "
                 f"[`/data/deltas/{profile_id.replace('/', '__')}__{mandate_id}.json`]"
                 f"(data/deltas/{profile_id.replace('/', '__')}__{mandate_id}.json) with the "
                 f"version of both inputs pinned, the time it was computed and the version of "
                 f"the computation that produced it. **The release gate recomputes it on every "
                 f"build and fails on a single row of disagreement**, which is how a machine "
                 f"holds a rule that forbids the act rather than the artefact. "
                 f"[Why this changed this morning](model/delta/index.html)."),
        ("p", f"**Excess: {len(dlt['excess'])}.** In the grant and not in the mandate. That is "
              f"the published definition and it is wider than the set the mandate refused "
              f"outright: **{len(dlt['excess_refused'])}** were refused and "
              f"**{len(dlt['excess_unstated'])}** were never mentioned. A capability the "
              f"mandate never mentioned was not authorised, and hiding the split would be the "
              f"other kind of dishonesty."),
        ("p", f"**Unbounded excess: {len(dlt['unbounded_excess'])}.** The excess whose barrier "
              f"is one of the first three rows: nothing, a rule somebody wrote down, or a "
              f"setting the agent's own account could change. None of those bounds anything."
              + (f" Every one of the {len(dlt['excess'])} excess capabilities here is unbounded."
                 if dlt["excess"] and len(dlt["unbounded_excess"]) == len(dlt["excess"])
                 else "")),
        ("note", "**The delta on this shape is empty, and that is a result rather than a "
                 "failure.** Everything this deployment can do, the mandate asked for. An ABP "
                 "that could never come back with nothing to report would not be a description, "
                 "it would be a sales document, and the other four examples would be worth less "
                 "for it. Note what the grant still is, though: one capability, and a record "
                 "once read is exposure that cannot be unread, on the vendor's side.")
        if not dlt["excess"] else ("p", "The excess is listed as prohibitions below."),
        ("p", (f"**Shortfall: {len(dlt['shortfall'])}.** Asked for and cannot: "
               + ", ".join(f"[`{c}`]({cap_href(c)})" for c in dlt["shortfall"]) + ".")
         if dlt["shortfall"] else
         "**Shortfall: 0.** There is nothing the mandate asked for that this deployment cannot do."),

        ("h2", "The same facts, as a figure"),
        ("p", "The table above is complete and it is the wrong shape for the one question this "
              "document exists to answer, which is how much of the right hand side has nothing "
              "on the left. **A mark with no line reaching it is excess.**"),
        grant_against_mandate(p, m, dlt, D, name),

        ("h2", "5. The prohibitions"),
        ("p", "The enforceable projection of the delta: one sentence per excess capability, each "
              "carrying the layer it would be enforced at and whether it is enforced today."
              + (f" **{n_sent} of {len(pro)} are not enforced today.** They are sentences, not "
                 f"controls." if n_sent else
                 (" **Every one of them is enforced today.**" if pro else ""))),
        prohibition_table(dlt, D) if pro else
        ("note", "**There are no prohibitions on this ABP, because the delta is empty.** Nothing "
                 "this deployment can do sits outside what the mandate asked for. That does not "
                 "mean nothing is worth deciding: it means the decision was already taken when "
                 "the mandate was written."),
        ("note", "**Why the barrier is on every row.** A prohibition shown without its barrier "
                 "manufactures assurance. All four major model providers stated in their own "
                 "2026 words that an instruction at the prompt layer can be bypassed, and the "
                 "rule underneath is older than any of them: a control bounds a grant only if "
                 "it is enforced by something the grant does not include. The right hand column "
                 "is where a control would have to sit, not a recommendation that you buy one."),

        ("h2", "6. The provenance"),
        provenance_block(p["rows"], scope="shape"),
        ("p", "**No row here was obtained by probing anybody's system.** A row is measured only "
              "from a system we are entitled to run, or from the vendor's own published "
              "documentation. Causing a computer to output data intending unauthorised access "
              "is an offence with no damage requirement and no research defence."),

        ("h2", "7. What this is not"),
        ("note", abp.NOT_AN_ASSESSMENT),
        ("note", "**Validity.** " + abp.VALIDITY.format(as_at=AS_AT, synced=SYNCED)),
        ("p", "**Three clocks, and only the first is ours.** An ABP is exactly as fresh as the "
              "twin, and the twin is exactly as fresh as its connection to somebody else's "
              "systems. That is a parameter rather than a defect to hide, and the gap between "
              "the second clock and the third belongs to the risk layer, because how much it "
              "matters depends on the assets."),
        ("table", ["Clock", "What it measures", "Who controls it"],
         [[a, b, c] for a, b, c in abp.CLOCKS]),

        ("h2", "Follow one capability through the model"),
        ("p", "The fifth graph rule says a path should read as a sentence in the reader's own "
              "language, and it is the acceptance test for this model:"),
    ]
    lead_row = (abp.order(dlt["unbounded_excess"], D) or abp.order(dlt["excess"], D)
                or abp.order(p["grant"], D))[0]
    lc = D["by_id"][lead_row["capability"]]
    nine = universes.walk_row(p, m, abp.delta(p, m, D, computed_at=D["provenance"]["retrieved"]),
                              lead_row["capability"], D, graph.build(D))
    slug_id = f"{profile_id.replace('/', '__')}__{mandate_id}"
    blocks += [
        ("p", f"agent [`{slug}`]({example_href(slug)}) **is-granted** capability "
              f"[`{lc['id']}`]({cap_href(lc['id'])}) **bounded-by** barrier "
              f"[`{lead_row['barrier']}`](model/barriers/index.html) **which-exceeds** mandate "
              f"[`{m['id']}`](model/index.html) **and-is** undo "
              f"[`{lc['undo']}`](model/undo/index.html)."),
        ("h3", "The same row, across nine universes"),
        ("p", "That path stays inside one vocabulary. The same row also crosses nine worlds, "
              "each owned by a different party and each with its own ontology, and the fifth "
              "rule holds across them too. Built from this page's own data on every build; "
              "[what the universes are](model/universes/index.html)."),
        ("note", shell.ascii_safe(nine["sentence"][0].upper() + nine["sentence"][1:])),
        ("note", "**Every number on this page is a leaf assertion in one fact set**, at "
                 f"[`/data/facts/{slug_id}.json`](data/facts/{slug_id}.json), and the release "
                 "gate parses the label, the leaflet, the prohibitions and the figure back out "
                 "of this page's markdown twin and fails the build on a single one that "
                 "differs. The label and the leaflet are two renderings of one fact set, and "
                 "that is checked rather than asserted."),
        ("p", f"[The four objects](model/index.html) · "
              f"[The capability grammar](model/capabilities/index.html) · "
              f"[The barriers](model/barriers/index.html) · "
              f"[This shape as JSON](data/profiles/{profile_id}.json) · "
              f"[This mandate as JSON](data/mandates/{mandate_id}.json) · "
              f"[The fact set](data/facts/{slug_id}.json)"),
    ]
    return {
        "title": name,
        "description": f"An Agent Behaviour Policy for {_lower_first(shell.ascii_safe(p['product']))}: a grant "
                       f"of {p['grant_size']}, a mandate of {len(m['want'])}, an excess of "
                       f"{len(dlt['excess'])} and an unbounded excess of "
                       f"{len(dlt['unbounded_excess'])}. Derived from published data, with no score.",
        "blocks": blocks,
    }, dlt


# ---------------------------------------------------------------------------
# the model
# ---------------------------------------------------------------------------

def model_pages(D):
    pages = {}
    caps = D["capabilities"]
    prov = D["provenance"]

    pages["model/index.html"] = {
        "title": "The model",
        "description": "The four objects an ABP is made of, the grammar they are written in, "
                       "the barrier that decides whether anything is in the way, and the graph "
                       "rules that govern all of it.",
        "blocks": [
            ("crumb", "[Home](index.html) / The model"),
            ("h1", "The model"),
            ("lead", "An ABP is not a document. It is four objects, of which the document is a "
                     "rendering. The order they are produced in is the order this page teaches "
                     "them, because a grant without a mandate beside it is an inventory and "
                     "nobody acts on an inventory."),
            ("h2", "The four objects"),
            ("table", ["Object", "What it is", "How it is obtained"], [
                ["**The mandate**", "What the agent is authorised and expected to do",
                 "**Elicited.** In minutes, because the deployer already knows it"],
                ["**The grant**", "Everything the agent can do",
                 "**Measured.** From the deployment shape: the product, where it runs, with "
                 "what account, with what credentials"],
                ["**The delta**", "The difference. Excess where it can and you did not ask; "
                                  "shortfall where you asked and it cannot",
                 "**Derived.** Recomputed whenever the grant or the mandate changes, stored "
                 "with the versions of both, and never edited by hand"],
                ["**The barrier**", "What stands between the agent and each capability",
                 "**Recorded**, per capability, from one of four kinds"],
            ]),
            ("p", "**Three hundred and forty things is a shrug. Three hundred and forty things "
                  "and you authorised twelve is a finding.** The mandate is the edge that gives "
                  "the grant a shape, and it has to be captured even though it is already "
                  "known."),
            ("h2", "Why the delta is derived and never authored"),
            ("note", "**Nobody writes a delta.** It is only ever the output of a computation "
                     "over the grant and the mandate, and it is stored along with the versions "
                     "of both inputs and the time it was computed. That is what makes it "
                     "checkable rather than stale. [What follows from "
                     "that](model/delta/index.html), including why this site said the opposite "
                     "this morning."),
            ("h2", "The pieces"),
            ("cards", [
                {"title": "[The capability grammar](model/capabilities/index.html)",
                 "sub": f"`verb.object.reach`. {caps['count']} primitives, each with the undo "
                        f"class of its effect.",
                 "foot": "Promoted from the published map. Nothing renamed."},
                {"title": "[The barrier](model/barriers/index.html)",
                 "sub": "Four kinds, and only the fourth bounds anything.",
                 "foot": "The enforcer test, published as a glyph before it was named as a rule."},
                {"title": "[The undo class](model/undo/index.html)",
                 "sub": "Three classes, and the ordering on every rendering this site produces.",
                 "foot": "A property of the action. Not a severity."},
                {"title": "[The lexicon](model/lexicon/index.html)",
                 "sub": "Every word the grammar is spelled with, as a node with its own "
                        "address: ten verbs, nine object classes, five reach classes, nine "
                        "families.",
                 "foot": "`read.file.project` is three nodes, not a string."},
                {"title": "[The delta](model/delta/index.html)",
                 "sub": "Derived and never authored. Stored with its inputs pinned, recomputed "
                        "when either moves, and never edited by hand.",
                 "foot": "Corrected on 11 September, in the open."},
                {"title": "[The graph](model/graph/index.html)",
                 "sub": "Five rules that govern the model rather than the styling.",
                 "foot": "Rule five is the acceptance test and it is cheap to apply."},
                {"title": "[The universes](model/universes/index.html)",
                 "sub": "One capability row walked through nine worlds, from the source bytes "
                        "to a licence condition, each with its own owner and ontology.",
                 "foot": "An ABP is a junction object. This is Fractal Semantic Graphs "
                         "applied to it."},
                {"title": "[The schema](model/schema/index.html)",
                 "sub": "What is in the published files, and what a consumer has to state.",
                 "foot": "A consumer pins a version."},
                {"title": "[The five examples](examples/index.html)",
                 "sub": "Five ABPs, derived from the data rather than authored.",
                 "foot": "Each states which rows were measured and which derived."},
            ]),
            ("h2", "What is deliberately not modelled"),
            ("p", "**Quantity.** The primitives carry reach and not rate. "
                  "`send.endpoint.world` is the same primitive for one request and a million. "
                  "The temporal operators of a policy language, count-within and sum-within, "
                  "are the shape of the fix and they are not here yet."),
            ("p", "**Interaction between agents.** Two agents each within mandate can compose "
                  "into something neither was authorised to do. There is no primitive for it "
                  "and this is the only sentence about it on the site."),
            ("p", "**Consequence.** Deliberately, and it is the rule above every other rule on "
                  "this site. No assets, no consequences, no score. That is not modesty: **no "
                  "assets does not mean no consequence, it means no consequence to you.** An "
                  "agent with `send.endpoint.world` and `execute.process.host` in an empty "
                  "environment can still reach third parties."),
            provenance_block(prov["rows"]),
        ]}

    # --- capabilities ------------------------------------------------------
    fam = {}
    for c in caps["capabilities"]:
        fam.setdefault(c["family"], []).append(c)
    rows = []
    for f, members in fam.items():
        for c in members:
            holders = [p for p in D["profiles"].values()
                       if any(r["capability"] == c["id"] for r in p["grant"])]
            rows.append([f"[`{c['id']}`]({cap_href(c['id'])})", c["gloss"], c["reach"],
                         c["undo"], f"{len(holders)} of {len(D['profiles'])}"])
    pages["model/capabilities/index.html"] = {
        "title": "The capability grammar",
        "description": f"`verb.object.reach`: {caps['count']} capability primitives, each with "
                       f"its reach and the undo class of its effect. The action vocabulary for "
                       f"everything else on this site.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The capabilities"),
            ("h1", "The capability grammar"),
            ("lead", f"`verb.object.reach`. **{caps['count']} primitives**, "
                     f"{len(caps['verbs'])} verbs, {len(caps['object_classes'])} object classes "
                     f"and {len(caps['reaches'])} reach classes. This grammar is the action "
                     f"vocabulary for everything else on this site, and it was not invented "
                     f"here."),
            ("note", f"**This site did not author this.** The grammar, the {caps['count']} "
                     f"primitives and their published glosses come from [the capability "
                     f"map]({MAP}). Promoting an ontology means giving it an address, not a new "
                     f"vocabulary, so nothing here is renamed. A new primitive is a new verb, "
                     f"object class or reach, and it needs a probe; a specific path, host or "
                     f"mailbox is an **instance** of a primitive, never a new one."),
            ("h2", "The reach classes"),
            ("table", ["Reach", "What it means"],
             [[f"`{k}`", shell.ascii_safe(v)] for k, v in caps["reaches"].items()]),
            ("p", "**What host, tenant and world mean is the deployment's to say, not the "
                  "grammar's.** For an agent in a vendor's container, host is the container and "
                  "tenant is a scoped token: not your machine and not your accounts. Every "
                  "example page states its own reach names for this reason."),
            ("h2", f"The {caps['count']} primitives"),
            ("table", ["Primitive", "Published gloss", "Reach", "Undo", "In how many shapes"],
             rows),
            ("h2", "The rules that come with the set"),
            ("ul", [shell.ascii_safe(r) for r in caps["rules"]]),
            ("p", f"[The capabilities as JSON](data/capabilities.json) · "
                  f"[The source bytes](data/upstream/primitives.json)"),
            provenance_block(prov["rows"]),
        ]}

    for c in caps["capabilities"]:
        pages[f"model/capabilities/{c['id']}/index.html"] = _capability_page(c, D)

    # --- barriers ----------------------------------------------------------
    pages["model/barriers/index.html"] = {
        "title": "The barrier",
        "description": "Four kinds of thing that can stand between an agent and a capability, "
                       "and only the fourth bounds anything. The enforcer test, which this "
                       "estate published as a glyph before it named it as a rule.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The barrier"),
            ("h1", "The barrier: what is actually in the way"),
            ("lead", "For every capability in the grant, an ABP records what stands between the "
                     "agent and it. There are four kinds. **Only the fourth bounds anything**, "
                     "and that is not an opinion."),
            barrier_legend(),
            ("h2", "The enforcer test"),
            ("note", f"**{D['barriers']['enforcer_test']}**"),
            ("p", "Read the third and fourth rows together and the test falls out of them. A "
                  "setting the agent's own account could change is not a control, because the "
                  "grant includes the ability to remove the bound. A boundary enforced above it "
                  "that it cannot reach is a control, because it does not."),
            ("p", "**A rule somebody wrote down is the second row and it is where most "
                  "prohibitions sit today.** All four major model providers stated in their own "
                  "2026 words that an instruction at the prompt layer can be bypassed; one of "
                  "them puts it as *the deterministic boundary is what gets hit when everything "
                  "probabilistic misses*. One provider reports that users approved roughly "
                  "ninety three per cent of the permission prompts they were shown, which is "
                  "the third row failing in the other direction."),
            ("h2", "What follows for every page on this site"),
            ("p", "**Every prohibition rendered anywhere carries its barrier.** A prohibition "
                  "displayed without one is a claim the site cannot support, and it manufactures "
                  "assurance. The honest ABPs say, for most deployments today, that the barrier "
                  "is the second kind."),
            ("p", "**Unbounded excess is the only number on the label a buyer can move.** Every "
                  "real control put in place shifts one capability into the fourth row and the "
                  "number falls. The gap between excess and unbounded excess is the business "
                  "case for a control, and it contains no verdict."),
            ("h2", "Where the four came from"),
            ("p", f"The glyph system on [the published map]({MAP}) carried all four before "
                  f"anybody wrote the rule down: nothing, a rule somebody wrote down, a setting "
                  f"the agent's own account could change, and a boundary enforced above it that "
                  f"it cannot reach. This site added two fields to them, `is_control` and the "
                  f"reason, and marks both as its own reading rather than as the map's data."),
            ("p", "[The barriers as JSON](data/barriers.json) · "
                  "[The source bytes](data/upstream/vocabulary.json)"),
        ]}

    # --- undo --------------------------------------------------------------
    pages["model/undo/index.html"] = {
        "title": "The undo class",
        "description": "Three classes of reversibility, the ordering on every rendering this "
                       "site produces, and the one column that is not fully context free.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The undo class"),
            ("h1", "The undo class"),
            ("lead", "**A capability that cannot be undone is a different kind of thing from "
                     "one that can.** That is the whole of it, and it is the ordering on every "
                     "document this site produces."),
            ("table", ["Class", "What it means"],
             [[f"`{c['id']}`", shell.ascii_safe(c["published_meaning"])]
              for c in D["undo"]["classes"]]),
            ("h2", "Why it is the ordering"),
            ("p", "An ABP that lists prohibitions alphabetically has buried the only ones that "
                  "matter. **Irreversible and unbounded is the first row of every document this "
                  "site produces.**"),
            ("note", "**This is not a severity ranking and it is not a score.** Reversibility is "
                     "a property of the action rather than of the context, and stating it as the "
                     "reason is what keeps the ordering descriptive. The risk product reorders "
                     "by consequence, because it knows the consequence. This site does not."),
            ("h2", "The one column that is not fully context free"),
            ("p", "**Whether deleting a file is reversible depends on backups, snapshots and "
                  "retention, which are the deployment's and not the product's.** So `undo: no` "
                  "here is a claim about the product's published behaviour, and the deployment "
                  "can change it. Saying so is the difference between a document that holds no "
                  "contextual judgements and one that has smuggled one in."),
            ("p", "[The undo classes as JSON](data/undo-classes.json)"),
        ]}

    # --- the delta ---------------------------------------------------------
    didx = _deltas_index()
    pages["model/delta/index.html"] = {
        "title": "The delta",
        "description": "Derived and never authored: stored with the versions of its inputs, "
                       "recomputed when either moves, and never edited by hand. Reality is the "
                       "third input, the history is the business case, and there are three "
                       "clocks.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The delta"),
            ("h1", "The delta"),
            ("lead", "**The delta is derived and never authored.** Nobody writes a delta. It is "
                     "only ever the output of a computation over the grant and the mandate, and "
                     "it is stored along with the versions of both inputs and the time it was "
                     "computed."),

            ("h2", "This page corrects something this site said this morning"),
            ("note", "**The foundation document says, twice, that the delta is computed and "
                     "never stored.** The first half is right and the second half is wrong, and "
                     "the correction was issued on the same day by the project lead. It is "
                     "published here rather than applied quietly, because the method is to "
                     "record the gap: [the dev brief that makes the "
                     "correction](docs/briefs/" + _DELTA_BRIEF + "/index.html), and [the "
                     "foundation document as published](what-is-an-abp/index.html), which "
                     "otherwise stands in full."),
            ("table", ["Was", "Is"], [
                ["The delta. Computed. Never stored, because the deployment changes.",
                 "**The delta. Derived.** Recomputed whenever the grant or the mandate changes, "
                 "stored with the versions of both, and never edited by hand."],
                ["The delta is computed and never stored. A stored delta is a claim about "
                 "somebody's environment on a day that has passed.",
                 "**The delta is derived and never authored.** Nobody writes a delta. It is only "
                 "ever the output of a computation over the grant and the mandate, and it is "
                 "stored along with the versions of both inputs and the time it was computed. "
                 "**What must never happen is that somebody edits a delta**, because a hand "
                 "edited delta is a fiction about an environment, and nothing downstream could "
                 "tell."],
            ]),

            ("h2", "What the old rule was protecting, and what survives"),
            ("p", "The sentence being corrected was guarding against three real things, and all "
                  "three survive."),
            ("table", ["The fear", "Does the correction still handle it"], [
                ["A delta becomes a stale claim about somebody's environment",
                 "**Yes.** A stored delta carries the versions of its inputs and the time it "
                 "was computed, so its staleness is a fact rather than a surprise"],
                ["A delta gets hand edited into a fiction",
                 "**Yes, and more strongly.** Never authored is a harder rule than never "
                 "stored, because it forbids the act rather than the artefact"],
                ["A delta is treated as authoritative after the inputs move",
                 "**Yes.** It reacts. A recompute is cheap because the inputs are graphs"],
            ]),
            ("p", "**So the correction loses nothing and gains the history.** It is also the "
                  "fourth instance of a pattern already in force across this network, which is "
                  "why the corrected sentence is the one that fits and the old one was the odd "
                  "one out: indexes are generated from the data they index, prose is derived "
                  "from the graph and never hand edited, a bill of materials is generated from "
                  "the dependency files, and the delta is derived from the grant and the "
                  "mandate. **In every case the artefact is stored. What is forbidden is "
                  "writing it.**"),

            ("h2", "The word for this already exists"),
            ("p", "**A stored result of a computation over other data, refreshed when its "
                  "inputs change, never edited directly, is a materialised view.** The "
                  "vocabulary is decades old and it carries exactly the right properties: it "
                  "exists for use, it has a refresh policy, its staleness is knowable, and "
                  "writing to it directly is a category error rather than a permission "
                  "question."),
            ("p", "The grant and the mandate are the append only side: a history of what "
                  "changed and when. The delta is the read model computed from them. **The "
                  "delta is a projection of the ABP graph, and so is the label, and so is the "
                  "leaflet.**"),
            ("h3", "The stored record"),
            ("table", ["Field", "Why"], [
                ["`grant_version`", "The input, pinned"],
                ["`mandate_version`", "The input, pinned"],
                ["`pack_version`", "The published vocabulary it was computed against"],
                ["`computed_at`", "When"],
                ["`computed_by`", "Which version of the computation, because the computation is "
                                  "code and code changes"],
                ["`excess`", "Capabilities in the grant and not in the mandate"],
                ["`unbounded_excess`", "Excess whose barrier is one of the first three kinds"],
                ["`shortfall`", "Capabilities in the mandate and not in the grant"],
            ]),
            ("note", "**No field in that record is writable by a person. The way to change a "
                     "delta is to change a grant or a mandate.** So the release gate does not "
                     "take the stored records on trust: it **recomputes every one of them** "
                     "from the profile and the mandate it names and fails on a single row of "
                     "disagreement. That check is a few lines, because the computation is a set "
                     "difference, and it is a set difference because the grant and the mandate "
                     "are held as graphs with a schema rather than as prose. **That is the "
                     "underlying capability.** All of this can be done by hand today and almost "
                     "nobody does it."),
            ("p", f"**{didx['count']} stored deltas**, one per deployment shape and mandate "
                  f"pair: [`/data/deltas/index.json`](data/deltas/index.json)."),

            ("h2", "Reality is the third input"),
            ("p", "The grant is a model of what the agent can do. The mandate is a statement of "
                  "what somebody meant. **Both are interpretations, and both improve.** The "
                  "customer says what they actually meant, and the mandate sharpens. Somebody "
                  "discovers a capability nobody had listed, and the grant grows."),
            ("table", ["What is observed", "What it tells you"], [
                ["Something happened that is not in the grant",
                 "**The grant was incomplete.** Add the capability"],
                ["Something was blocked that the grant said was possible",
                 "**A barrier was missed**, or recorded at the wrong kind. Correct it"],
                ["Something in the mandate never happens",
                 "Either the mandate is aspirational, or the capability is missing and the "
                 "shortfall is real"],
                ["Something happens repeatedly that is in the grant and not in the mandate",
                 "**The mandate is wrong, or the deployment is.** This is the only row where "
                 "the observation does not say which"],
            ]),
            ("note", "**That last row is the one place a derived delta cannot resolve itself.** "
                     "An agent doing something outside its mandate, repeatedly, without anybody "
                     "complaining, means either that the mandate was written too narrowly or "
                     "that something is happening nobody authorised. **This site publishes the "
                     "observation. Which of the two it is belongs to the risk layer and to a "
                     "person.** Record, not verdict, again."),
            ("p", f"**And the calibration loop is the answer to this site's honest weakness.** "
                  f"{_prov()['rows']['measured']} of {_prov()['rows']['total']} capability rows "
                  f"are measured and the rest derived from documentation. Every deployment that "
                  f"runs and reports back moves a row from derived to measured, and because "
                  f"[the capability map]({MAP}) is shared and public, **it moves for "
                  f"everybody**. That is the reason the map belongs in an open repository "
                  f"rather than inside a product."),
            ("h3", "And the collection problem it creates"),
            ("note", "**A calibration loop needs observation, and the downloadable builds in "
                     "this estate are ruled never to transmit anything.** The resolution is "
                     "that calibration happens inside the customer's own instance: their "
                     "deployment observes, their grant improves, their delta recomputes, and "
                     "none of it leaves. **What comes back to the shared map is a contribution, "
                     "not telemetry**: a proposed correction to a capability row, carrying its "
                     "evidence, submitted deliberately through the same mechanism as any other "
                     "proposal, with a source, a timestamp and a hash. A person decides to send "
                     "it. Nothing phones home. **That is slower, and it is the only version "
                     "that is honest.**"),

            ("h2", "It reacts, and the trigger has a standard"),
            ("p", "Because the delta is derived, a change in either input propagates without "
                  "anybody touching the document. **A template cannot do that and a rendered "
                  "document cannot do that.** Three cases:"),
            ("table", ["What happens", "What the ABP does"], [
                ["**A weakness is disclosed in a tool the agent can call.**",
                 "Nothing about the deployment changed, but a capability recorded at the fourth "
                 "barrier is now at the first. The grant is the same and **the unbounded excess "
                 "jumps**. The ABP changed because the world did"],
                ["**A credential is quietly widened.**",
                 "Somebody adds a scope to a token to fix an unrelated problem. The grant grows, "
                 "the mandate does not, and the excess grows by exactly the capabilities that "
                 "scope carries. **Nobody involved thought they were changing a policy**"],
                ["**A control ships.**",
                 "A gateway is deployed with default deny. A set of capabilities move from the "
                 "second barrier to the fourth. **Unbounded excess falls, and the number it "
                 "falls by is what the project bought**"],
            ]),
            ("p", "**The trigger for a recompute already has a standard, so it is a receiver "
                  "rather than an invention.** The continuous access evaluation profile, "
                  "published on the standards track by the shared signals working group, "
                  "defines event types an identity provider transmits and a receiver consumes "
                  "so that access can be attenuated as things change."),
            ("table", ["Event type", "What it means for the ABP"], [
                ["**Credential Change**", "**The grant may have moved.** Recompute"],
                ["**Token Claims Change**", "**The grant may have moved.** Recompute"],
                ["**Assurance Level Change**", "A barrier may have moved"],
                ["**Device Compliance Change**", "A barrier may have moved"],
                ["**Risk Level Change**",
                 "**Not ours.** That is the risk layer's input, not the ABP's"],
                ["**Session Revoked, Established, Presented**",
                 "Session lifecycle, below the ABP's altitude"],
            ]),
            ("note", "**Nothing here is wired, and one caveat travels with the citation.** The "
                     "status of that specification could not be confirmed from its own page, "
                     "which said standards track rather than final while sitting at a final "
                     "address. It is named here because it is the right shape, and it should be "
                     "checked before anybody cites it as settled."),

            ("h2", "What hooks to it, and the hazard"),
            ("p", "Behaviours can be hooked to a derived delta: actions, the granting of a "
                  "licence to operate and the removal of one. **That is where an ABP stops "
                  "being a document.** It is also hazardous in a specific way: a computation "
                  "error would revoke a licence."),
            ("note", "**The delta crossing a threshold is a record. The consequence is a "
                     "verdict.** So this site publishes the crossing, with its inputs and its "
                     "computation version, and **the consequence is a policy the customer or "
                     "the underwriter set in advance**, never a judgement the ABP makes. That "
                     "keeps the ABP consequence agnostic while the automation is real, and it "
                     "means any automatic suspension is traceable to a threshold somebody chose "
                     "and a computation anybody can rerun."),

            ("h2", "The history is the business case, read rather than constructed"),
            ("p", "Store the series and the business case stops being a document somebody "
                  "writes. A control project has a date; the series has grants, mandates and "
                  "deltas with dates; so the value of the project is a subtraction:"),
            ("note", "On 14 March the gateway was deployed. **Unbounded excess fell from thirty "
                     "one to six. Excess was unchanged**, because the agent can still do the "
                     "same things; what changed is that twenty five of them are now bounded by "
                     "something it cannot reach."),
            ("p", "**That sentence contains no verdict, no score and no adjective**, and both "
                  "ends of it are stored records with their inputs pinned, so it is checkable."),
            ("table", ["Use of the series", "How soon it pays"], [
                ["**Justifying what was already bought**",
                 "The easiest, and the one every security team needs and cannot produce today"],
                ["**Pricing what to buy next**",
                 "The capabilities in unbounded excess, ordered by how many would move to the "
                 "fourth barrier per control, is a list with an effect size on each row"],
                ["**Evidencing a condition over time**",
                 "Asking whether a control was in place throughout a period is a question about "
                 "a series, not a snapshot. **A stored history answers it and a recomputed "
                 "present cannot.** This is the one the old wording made impossible"],
            ]),

            ("h2", "Three clocks, and the gap that is not ours"),
            ("table", ["Clock", "What it measures", "Who controls it"],
             [[a, b, c] for a, b, c in abp.CLOCKS]),
            ("p", "**So an ABP is exactly as fresh as the twin, and the twin is exactly as "
                  "fresh as its connection.** That is a parameter rather than a defect to hide, "
                  "and it belongs on the label as part of the validity statement: as at this "
                  "date, from a twin last synchronised at this date."),
            ("p", f"**And the gap between the second clock and the third is a risk that [the "
                  f"risk layer]({RISKS}) accounts for**, which is the correct home for it, "
                  f"because how much that gap matters depends on the assets, and the ABP does "
                  f"not know the assets. [The twin]({TWINS}) is the interface to the real "
                  f"environment."),

            ("h2", "Drift is a neighbouring measurement, and the difference is the mandate"),
            ("p", "The market has a word for a related phenomenon and it is drift. Products "
                  "announced in September 2026 compare an agent's runtime behaviour against its "
                  "authorised scope. **That is validation, and it sharpens the distinction "
                  "rather than blurring it.**"),
            ("table", ["", "What it compares", "When you learn"], [
                ["**Behaviour drift**",
                 "What the agent **did** against what it was allowed to do",
                 "**After the action**"],
                ["**Capability excess**",
                 "What the agent **can do** against what it was authorised to do",
                 "**Before any action**"],
            ]),
            ("p", "**You can only detect drift once an agent has drifted.** An ABP states that "
                  "the drift is possible before it happens, which is a different thing and an "
                  "earlier one in the sequence. **Both want a mandate, and the mandate is the "
                  "scarce input**, which is the strongest reason to make eliciting it cheap and "
                  "to publish the method."),
            ("note", "**No adjective is attached to any named product on this site, and none is "
                     "here.** Neither product was used or tested. One number from one of those "
                     "announcements is worth keeping because it is somebody else's figure "
                     "supporting this site's thesis: fifty seven per cent of enterprise "
                     "identity is described as unseen and unmanaged. *You do not know what it "
                     "can do*, said by somebody selling a different answer to it."),

            ("h2", "What is not settled"),
            ("ul", [
                "**What the recompute policy is**: on every event, on a schedule, on read, or a "
                "combination. It decides how much the receiver has to do.",
                "**Who sets the thresholds a consequence hooks to**: the customer, the "
                "underwriter, or a default published here. All three have different shapes.",
                "**How a calibration contribution is submitted without revealing the "
                "deployment**, since a correction to a capability row implies somebody runs "
                "that shape.",
                "**Whether the shortfall matters commercially.** Capabilities in the mandate and "
                "not in the grant are a real finding and nobody has proposed anything against "
                "them.",
                "**What happens to a stored delta whose computation version is superseded**: "
                "recomputed, marked, or left as the record of what was believed at the time. "
                "The third is the most honest and the least useful.",
            ]),
            ("p", f"[The full brief](docs/briefs/{_DELTA_BRIEF}/index.html) \u00b7 "
                  f"[The stored deltas](data/deltas/index.json) \u00b7 "
                  f"[The four objects](model/index.html)"),
        ]}

    # --- graph -------------------------------------------------------------
    pages["model/graph/index.html"] = {
        "title": "The graph",
        "description": "The five published graph rules, what they force on this model, and the "
                       "sentence test that decides whether the edges are right.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The graph"),
            ("h1", "The graph"),
            ("lead", f"An ABP is a graph and every document is a projection of it. The five "
                     f"rules that govern it are published at [graphs.sgit.ai]({GRAPHS}) and they "
                     f"govern the model rather than the styling. This page says what each one "
                     f"forces here."),
            ("table", ["Rule", "What it forces on this model"], [
                ["**Every edge is a verb with a distinct inverse.**",
                 "`is-granted` and `granted-to` are different edges with different fan out. The "
                 "inverse is not the same edge walked backwards."],
                ["**The generic association edge is banned.**",
                 "There is no `relates-to` anywhere in this model. It constrains nothing and "
                 "costs fan out."],
                ["**Never render the whole graph. Render the result of a query.**",
                 "There is no map of everything on this site. Each page answers one query: this "
                 "shape's grant, this mandate's delta, this capability across every shape."],
                ["**Rich nodes are acceptable.**",
                 "A capability node carries its verb, object, reach, undo class and gloss. The "
                 "blob is a rendering failure, not a modelling one."],
                ["**If a path does not read as a sentence in the reader's own language, the "
                 "edges are wrong.**",
                 "The acceptance test, below. If a path fails it, the model changes and not the "
                 "renderer."],
            ]),
            ("h2", "Where the rules landed"),
            ("table", ["Address", "What is there"], [
                ["[The lexicon](model/lexicon/index.html)",
                 "Every word the grammar is spelled with, as a node with its own address. "
                 "`read.file.project` is three nodes and three edges."],
                ["[The edge vocabulary](model/graph/edges/index.html)",
                 f"{len(__import__('graph').EDGES)} edges, each a verb with a distinct inverse, "
                 f"a stated domain and range. No generic association edge."],
                ["[The node type formulas](model/graph/formulas/index.html)",
                 "Classification as a required path pattern, run on every build, rather than a "
                 "label somebody applied."],
                ["[The three layers](model/graph/layers/index.html)",
                 "How a customer vault disagrees with this vocabulary without merging anything."],
                ["[The nine universes](docs/briefs/" + _FSG_BRIEF + "/index.html)",
                 "The map of the ABP onto Fractal Semantic Graphs: one capability row crosses "
                 "nine universes, each with its own owner and ontology, joined by named edges. "
                 "A brief at v0.4.0; the universes land one per release after it."],
            ]),
            ("h2", "The sentence test"),
            ("note", "agent `claude-code-cli-confirmations-disabled` **is-granted** capability "
                     "`execute.process.host` **bounded-by** barrier `a-rule-somebody-wrote-down` "
                     "**which-exceeds** mandate `ship-a-feature` **and-is** undo `no`"),
            ("p", "Every example page ends with that path, built from its own data, so the test "
                  "is applied on every build rather than asserted once here."),
            ("h2", "The five layers, and the tension in them"),
            ("p", "A five level compression hierarchy says a class name does not mean the same "
                  "thing two levels up. The variant rule says every rendering must produce the "
                  "same fact set, with an empty diff. Both are true, and the resolution is "
                  "precise:"),
            ("ul", [
                "**The fact set is the leaf assertions**: this shape has this capability, at "
                "this barrier, with this undo class; this mandate contains these capabilities; "
                "therefore this delta. **Identical in every rendering, and the diff is over "
                "these.**",
                "**The classes are how those facts are grouped for a reader.** An executive "
                "rendering groups by business consequence, an engineer's by reach and barrier. "
                "**Different at different altitudes, and that is correct rather than a defect.**",
            ]),
            ("p", "**So the fact diff is over leaf assertions, not over structure.** The label "
                  "and the leaflet on every example page are two renderings of one fact set, and "
                  "keeping them that way is why both are generated from the same call."),
            ("p", "**Altitude is for stakeholder, depth is for detail.** The layers here are "
                  "altitudes."),
            ("h2", "The interchange vocabulary"),
            ("p", "The W3C has had a rights expression vocabulary since 2018: a policy carries "
                  "permissions, prohibitions and duties, constraints cover time, purpose, count "
                  "and place, the conflict strategy says **prohibitions win**, and a policy "
                  "inherits from a parent, which is how a policy for an agent in an environment "
                  "extends a policy for an agent. Use it as the interchange form through a "
                  "profile that adds these capability primitives as actions."),
            ("note", "**Do not claim it enforces anything, because it does not.** It is a "
                     "vocabulary for expressing a policy, not a thing that stands in the way. In "
                     "the barrier's terms an interchange document is a rule somebody wrote down "
                     "until something above the grant compiles it and enforces it."),
        ]}

    # --- schema ------------------------------------------------------------
    man = _manifest(D)
    pages["model/schema/index.html"] = {
        "title": "The schema",
        "description": "What is in the published files, what this site added to the data it "
                       "promoted, and the two rules a consumer and a contributor each have to "
                       "follow.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The schema"),
            ("h1", "The schema"),
            ("lead", "The published vocabulary, file by file, at stable addresses with cross "
                     "origin access. It is promoted from a game's data pack rather than authored "
                     "here, and the difference between the two is written down below rather than "
                     "blurred."),
            ("table", ["Address", "Type", "What is in it"], [
                ["[`/data/index.json`](data/index.json)", "`abp/pack/v1`",
                 "The manifest. Start here: it names every other file, the counts, and the "
                 "version to pin."],
                ["[`/data/capabilities.json`](data/capabilities.json)", "`abp/capabilities/v1`",
                 f"The grammar and the {caps['count']} primitives, with reach, family, undo "
                 f"class and published gloss."],
                ["[`/data/barriers.json`](data/barriers.json)", "`abp/barriers/v1`",
                 "The four barriers, weakest first, each with `is_control` and the enforcer "
                 "test behind it."],
                ["[`/data/undo-classes.json`](data/undo-classes.json)", "`abp/undo-classes/v1`",
                 "The three undo classes and the ordering rule."],
                ["[`/data/evidence-tiers.json`](data/evidence-tiers.json)",
                 "`abp/evidence-tiers/v1`",
                 "The seven evidence tiers and which of them this site counts as measured."],
                ["[`/data/profiles/index.json`](data/profiles/index.json)",
                 "`abp/profiles-index/v1`",
                 f"The {len(D['profiles'])} deployment shapes. A shape is a product in a "
                 f"setting, not a product."],
                ["[`/data/mandates/index.json`](data/mandates/index.json)",
                 "`abp/mandates-index/v1`",
                 f"The {len(D['mandates'])} starting mandates, one per surface."],
                ["[`/data/provenance.json`](data/provenance.json)", "`abp/provenance/v1`",
                 "Where every row came from, how many were measured, and the content hash to "
                 "verify against."],
                ["[`/data/contributed/riskmandate/`](data/contributed/riskmandate/manifest.json)",
                 "`abp/contributed-manifest/v1`",
                 "Seven deployment shapes contributed by riskmandate.ai: the bytes as fetched, "
                 "unchanged, with a hash per file and a hash over all of them. Promoted into "
                 "`profiles/` and `mandates/` with their provenance, and counted beside the "
                 "map's rows rather than folded into them."],
                ["[`/data/upstream/`](data/upstream/pack.json)", "the source pack",
                 "The bytes as fetched, unchanged. Anything rendered stays one click from its "
                 "source bytes."],
            ]),
            ("h2", "What this site added, and what it did not"),
            ("p", "**Nothing was renamed.** Capability ids, barrier ids, undo classes and shape "
                  "ids are the published ones. Two field names changed and the provenance block "
                  "on each file says which."),
            ("p", "**Two fields are this site's own and are marked as such**: `is_control` on a "
                  "barrier, and the reason behind it. They are a reading of the published "
                  "wording, not data from the pack."),
            ("p", "**One derivation is this site's own**: where two tools in a shape reach the "
                  "same capability, the grant keeps the **weakest** barrier, because the agent "
                  "takes the easier path. Each profile's provenance block says so."),
            ("p", "**No delta is in the files, and no score is.** A delta is computed every "
                  "time it is needed. A score is a verdict and it does not live here at all."),
            ("h2", "The two rules"),
            ("note", "**A consumer pins a version.** Anything that computes from these files "
                     f"states which version it computed against. This is `{man['version']}`, "
                     f"content hash `{man['provenance']['content_hash'][:26]}`. A clone that "
                     f"floats against the latest has no reproducible output."),
            ("note", "**A proposal carries evidence.** Every node taken from a third party site "
                     "carries a source URL, a retrieval timestamp and a content hash. A proposal "
                     "that changes a capability row without one is an assertion, and this site "
                     "publishes capability claims about named commercial products."),
            ("p", f"[The data layer](data/index.html) · [The style rules these files "
                  f"follow]({CODING})"),
        ]}
    return pages


def _capability_page(c, D):
    """One capability, across every shape that has it. The third graph rule: this page is a
    query, not a map."""
    holders = []
    for pid, p in sorted(D["profiles"].items()):
        row = next((r for r in p["grant"] if r["capability"] == c["id"]), None)
        if row:
            holders.append([GLYPH[row["barrier"]],
                            f"{shell.ascii_safe(p['product'])}"
                            + (f" *(contributed by {p['contributed']['by']})*"
                               if p.get("contributed") else ""),
                            row["barrier"] + ("" if D["is_control"][row["barrier"]]
                                              else " (not a control)"),
                            row["evidence"],
                            row.get("material") or "not stated",
                            shell.ascii_safe(row.get("note") or "")])
    wants = [m for m in D["mandates"].values() if c["id"] in m["want"]]
    refuses = [m for m in D["mandates"].values() if c["id"] in m["do_not_want"]]
    unstated = [m for m in D["mandates"].values() if c["id"] in m["unstated"]]
    red = D["reductions"].get(c["id"])
    blocks = [
        ("crumb", "[Home](index.html) / [The model](model/index.html) / "
                  "[The capabilities](model/capabilities/index.html) / " + c["id"]),
        ("h1", f"`{c['id']}`"),
        ("lead", f"**{c['gloss']}.** Its effect is **{c['undo']}**: {UNDO_WORD[c['undo']]}."),
        ("h2", "What this id is made of"),
        ("p", f"**This is not a string.** It is "
              f"{lexicon_pages.spell(c['id'], D)}, three nodes joined by three edges, and each "
              f"of them has an address, a page and a JSON file. Follow any of them and you get "
              f"the query for that word rather than a definition of it."),
        ("table", ["Node", "Edge", "Reads as"], [
            [f"[`{c['verb']}`]({lexicon_pages.href('verbs', c['verb'])})", "`has_verb`",
             f"this capability has the verb `{c['verb']}`"],
            [f"[`{c['object']}`]({lexicon_pages.href('objects', c['object'])})", "`acts_on`",
             f"this capability acts on `{c['object']}`"],
            [f"[`{c['reach']}`]({lexicon_pages.href('reaches', c['reach'])})", "`reaches`",
             f"this capability reaches `{c['reach']}`"],
            [f"[`{c['family']}`]({lexicon_pages.href('families', c['family'])})", "`in_family`",
             f"this capability is in the `{c['family']}` family"],
            [f"[`{c['undo']}`](model/undo/index.html)", "`has_undo_class`",
             f"this capability has the undo class `{c['undo']}`"],
        ]),
        ("note", f"**The gloss above is a convenience, not the definition.** A node carries no "
                 f"inherent meaning: what `{c['id']}` is emerges from the edges traceable from "
                 f"it. The strongest case is "
                 f"[`{c['reach']}`]({lexicon_pages.href('reaches', c['reach'])}), where the "
                 f"deployment shapes that use it **do not agree** about what it means, and the "
                 f"page keeps the disagreement rather than averaging it."),
        ("h2", f"In {len(holders)} of {len(D['profiles'])} published shapes"),
        ("table", ["", "Deployment shape", "Barrier there", "Known by", "Whose material",
                   "Note"], holders)
        if holders else ("p", "No published shape in this set has it."),
        barrier_legend(),
        ("h2", "What the starting mandates say about it"),
        ("table", ["The mandate says", "Which mandates"], [
            ["**authorised**", ", ".join(shell.ascii_safe(m["label"]) for m in wants) or "none"],
            ["**refused**", ", ".join(shell.ascii_safe(m["label"]) for m in refuses) or "none"],
            ["**unstated**", ", ".join(shell.ascii_safe(m["label"]) for m in unstated) or "none"],
        ]),
        ("p", "**Unstated is not authorised.** A mandate that never mentioned a capability did "
              "not authorise it, and the delta on every example page counts it as excess and "
              "says which kind it was."),
    ]
    if red:
        blocks += [
            ("h2", "What would move it to the fourth barrier"),
            ("table", ["What", "What it costs", "The barrier afterwards"],
             [[shell.ascii_safe(red["setting"]), shell.ascii_safe(red["costs"]),
               shell.ascii_safe(red["tier_after"])]]),
            ("note", "**This is a published reduction, not a recommendation.** Whether it is "
                     "worth doing depends on the assets and the consequences, which are not in "
                     "this document and are not this site's to guess. Since v0.4.3 it is also a "
                     f"node, `setting/{c['id']}`, in [the deployment shape universe]"
                     "(model/universes/u2/index.html): it **narrows** this capability and "
                     "**moves** it to the barrier named in the third column, which is the path "
                     "the prohibitions table's last column is a projection of."),
        ]
    blocks.append(("p", f"[The capability grammar](model/capabilities/index.html) · "
                        f"[This primitive as JSON](data/capabilities.json)"))
    return {
        "title": c["id"],
        "description": f"{c['gloss']}. Reach `{c['reach']}`, undo `{c['undo']}`. Which published "
                       f"deployment shapes have it, at what barrier, and what the starting "
                       f"mandates say.",
        "blocks": blocks,
    }


_FSG_BRIEF = ("v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-"
              "universes-and-each-keeps-its-own-ontology")
_DELTA_BRIEF = ("v0.33.70__dev-brief__the-delta-is-derived-and-never-authored-storing-it-is-"
                "the-point-and-the-history-is-the-business-case")


def _deltas_index():
    import json
    return json.loads((Path(__file__).resolve().parents[2] / "data/deltas/index.json").read_text())


def _prov():
    return load()["provenance"]


def _manifest(D):
    import json
    return json.loads((Path(__file__).resolve().parents[2] / "data/index.json").read_text())


# ---------------------------------------------------------------------------
# the examples index, with the cost of producing them
# ---------------------------------------------------------------------------

# How long each example took to produce, and what it cost. Recorded because nobody knows what
# an ABP costs to make and the store has to price one. The honest shape of the answer is that
# the FIRST one cost everything and the other four cost a build: they are derived from data
# that already passes through a published pipeline, so the work was the generator, the schema
# and the honesty line, not the research. A shape that is NOT in the published map would cost
# the measurement as well, and that number is not known yet.
COST = [
    ("chatgpt-web-no-connectors", "5 min", 0,
     "The smallest grant. Nothing new was needed once the generator existed."),
    ("claude-code-cli-confirmations-enabled", "5 min", 0,
     "The first one where the barrier column carries the argument."),
    ("claude-code-cli-confirmations-disabled", "5 min", 0,
     "Built second in importance and first in value. It is the same generator call against a "
     "different profile id."),
    ("browser-extension-broad-host-permissions", "5 min", 0,
     "Three capabilities, all three irreversible. The shortest page and not the mildest."),
    ("github-actions-hosted-runner", "5 min", 0,
     "A service account rather than a person. The only other shape in the set with measured "
     "rows."),
]
COST_NOTE = (
    "**The honest version of this table is the sentence underneath it.** The five examples took "
    "about four hours in total, and essentially all of it went into the generator, the promoted "
    "schema and the provenance line. The marginal cost of the sixth example, for a shape already "
    "in the published map, is one line in a list and a build. **That is not the number the store "
    "needs.** The number the store needs is what it costs to produce an ABP for a shape that is "
    "NOT in the map, where the grant has to be measured rather than looked up, and this site "
    "cannot tell you that yet because it has not done one. Nought questions had to be asked of "
    "a human for these five, which is the same finding from the other side: they were derived, "
    "not elicited.")


def examples_pages(D):
    pages, built = {}, []
    for slug, pid, mid, name, why, note in EXAMPLES:
        page, dlt = example_page(slug, pid, mid, name, why, note, D)
        pages[example_href(slug)] = page
        p, m = D["profiles"][pid], D["mandates"][mid]
        built.append((slug, name, p, m, dlt, why))

    rows = []
    for slug, name, p, m, dlt, why in built:
        rows.append([
            f"[{name}]({example_href(slug)})", f"*{why}*",
            str(p["grant_size"]), str(len(m["want"])), f"**{len(dlt['excess'])}**",
            f"**{len(dlt['unbounded_excess'])}**", str(len(p["irreversible"])),
            p["widest_reach"], f"{p['rows']['measured']} of {p['rows']['total']}"])
    total = D["provenance"]["rows"]

    pages["examples/index.html"] = {
        "title": "Five worked examples",
        "description": "Five Agent Behaviour Policies, one per deployment shape, derived from "
                       "published data rather than authored. Each states which of its rows were "
                       "measured and which were derived, and none carries a score.",
        "blocks": [
            ("crumb", "[Home](index.html) / Examples"),
            ("h1", "Five worked examples"),
            ("lead", "Five ABPs, from the smallest grant in the set to a service account that "
                     "outlives the turn. **They are derived rather than authored**: the rows come "
                     "from a published data pack, and the delta on each page is computed when "
                     "the page is built."),
            ("note", "**Before you read any of them, write down a number.** For a deployment you "
                     f"actually run, how many of the {D['capabilities']['count']} capability "
                     f"primitives do you think it has? Most people who have deployed an agent "
                     f"know what they asked it to do, and almost nobody knows what it can do. "
                     f"The gap between your number and the table below is the reason this "
                     f"document type exists."),
            ("h2", "The five, side by side"),
            ("table", ["Deployment shape", "Why this one", "Grant", "Mandate", "Excess",
                       "Unbounded excess", "Irreversible", "Widest reach", "Measured"], rows),
            ("p", "**No column here is a score.** Excess is a count of capabilities in the grant "
                  "and not in the mandate. Unbounded excess is how many of those sit at a "
                  "barrier that is not a control. Neither says whether any of it is acceptable, "
                  "because acceptability is not in the document."),
            ("h2", "Read the third one first"),
            ("p", "[Claude Code with confirmations on](examples/"
                  "claude-code-cli-confirmations-enabled/index.html) and [the same thing with "
                  "confirmations off](examples/claude-code-cli-confirmations-disabled/index.html) "
                  "are the same product, the same machine and the same account, with one setting "
                  "different. **Reading them side by side is the argument.**"),
            ("note", "**And the pair says something the foundation document does not.** The "
                     "foundation document says that turning confirmations off moves the barrier "
                     "on every capability in the delta by one row. In the published data it "
                     "moves exactly one barrier, on `execute.process.host`, and that capability "
                     "is inside the mandate rather than in the delta: the deployer asked for it. "
                     "So the label's numbers do not move at all and the document is still "
                     "materially different. That is a stronger argument for the leaflet and "
                     "against a headline number, and it is recorded as a disagreement in "
                     "[v0.1.0's notes](versions/v0.1.0/index.html) rather than quietly resolved."),
            ("h2", "What each one cost to make"),
            ("p", "Nobody knows what an ABP costs to produce, and the store has to price one. So "
                  "this is instrumented rather than estimated."),
            ("table", ["Example", "Time", "Questions asked of a human", "Note"],
             [[f"[{s}]({example_href(s)})", t, str(q), n] for s, t, q, n in COST]),
            ("note", COST_NOTE),
            ("h2", "What none of these is"),
            ("note", abp.NOT_AN_ASSESSMENT),
            provenance_block(total, scope="shape"),
        ]}
    return pages


# ---------------------------------------------------------------------------
# the data layer's own page
# ---------------------------------------------------------------------------

def data_page(D):
    man = _manifest(D)
    prov = D["provenance"]
    tiers = ", ".join(f"`{k}` {v}" for k, v in sorted(prov["by_tier"].items(),
                                                      key=lambda kv: -kv[1]))
    return {"data/index.html": {
        "title": "The data",
        "description": "The capabilities, barriers, undo classes, deployment shapes and mandates "
                       "an ABP is written in, as JSON at stable addresses with cross origin "
                       "access, with the source bytes they were promoted from.",
        "blocks": [
            ("crumb", "[Home](index.html) / The data"),
            ("h1", "The data"),
            ("lead", "The published vocabulary of the Agent Behaviour Policy: "
                     f"**{man['counts']['capabilities']} capabilities**, "
                     f"**{man['counts']['barriers']} barriers**, "
                     f"**{man['counts']['undo_classes']} undo classes**, "
                     f"**{man['counts']['profiles']} deployment shapes** and "
                     f"**{man['counts']['mandates']} starting mandates**, at stable addresses "
                     f"with cross origin access."),
            ("note", f"**Start at [`/data/index.json`](data/index.json).** It names every other "
                     f"file, carries the counts and states the version to pin. This is "
                     f"`{man['version']}`."),
            ("h2", "Where it came from, and what that obliges"),
            ("p", f"**This site did not author this ontology.** It was published as a data pack "
                  f"the game at [what-can-it-do.games.sgit.ai]({MAP}) reads, and the job here "
                  f"was to promote it out of a game's internals into a published schema the "
                  f"network can cite. Nothing was renamed."),
            ("table", ["Field", "Value"], [
                ["Source", f"`{prov['source']}`"],
                ["Retrieved", f"`{prov['retrieved']}`"],
                ["Pack version", f"`{prov['pack_version']}`"],
                ["Content hash", f"`{prov['content_hash']}`"],
                ["Files hashed", str(prov["files_hashed"])],
                ["Licence", "CC BY 4.0"],
            ]),
            ("p", "**The bytes as fetched are served unchanged** under "
                  "[`/data/upstream/`](data/upstream/pack.json), and the build recomputes the "
                  "hash on every run and refuses to write if it disagrees. Anything rendered "
                  "stays one click from its source bytes."),
            ("h2", "How much of it was measured"),
            ("p", f"**{prov['rows']['measured']} of {prov['rows']['total']} capability rows** "
                  f"were measured, meaning seen directly on the thing itself. The other "
                  f"{prov['rows']['derived']} were derived from what the deployment "
                  f"architecturally is, or from the vendor's published documentation. By tier: "
                  f"{tiers}."),
            ("note", f"**A precision the headline loses.** {prov['measured_means']}"),
            ("p", f"**{prov['never_tested']}**"),
            ("h2", "The files"),
            ("table", ["Address", "What is in it"],
             [[f"[`/data/{v}`](data/{v})", k.replace("_", " ")]
              for k, v in man["files"].items() if not v.endswith("/")]),
            ("h2", "The deltas, which are here on purpose"),
            ("p", f"**{_deltas_index()['count']} stored deltas**, one per deployment shape and "
                  f"mandate pair, at [`/data/deltas/index.json`](data/deltas/index.json). "
                  f"{shell.ascii_safe(man['the_delta'])} "
                  f"[What that means and why it changed](model/delta/index.html)."),
            ("note", "**The release gate recomputes every stored delta on every build** from "
                     "the profile and the mandate it names, and fails on a single row of "
                     "disagreement. That is how a machine holds `never authored': the rule "
                     "forbids the act rather than the artefact, and a hand edited delta is a "
                     "fiction nothing downstream could detect."),
            ("h2", "What is deliberately not in these files"),
            ("table", ["Not here", "Why"], [
                ["**A score**", shell.ascii_safe(man["not_here"]["score"])],
                ["**A consequence**", shell.ascii_safe(man["not_here"]["consequence"])],
            ]),
            ("h2", "The contributed shapes, and the intake path"),
            ("p", f"**{prov['contributed']['shapes']} deployment shapes were contributed by "
                  f"{prov['contributed']['contributor']}** and promoted here at v0.4.4, which "
                  f"is the answer to the second of the three requests it published against "
                  f"this site: under the three layers a shape is a layer one fact, owned by "
                  f"nobody, and it belongs at the address every consumer reads. The bytes as "
                  f"fetched sit under [`/data/contributed/riskmandate/`]"
                  f"(data/contributed/riskmandate/manifest.json), never edited, with a hash "
                  f"per file and a hash over all of them that the build and the gate both "
                  f"recompute. Each promoted profile pins the hash of the one file it came "
                  f"from, carries the contributor's own provenance block whole, and keeps "
                  f"the contributor's contradictions, research needed and what the grammar "
                  f"cannot say, because those are the finding."),
            ("table", ["Shape", "Rows", "Measured", "Widest reach", "The contributor's page"],
             [[f"`{p['id']}`", str(p["grant_size"]),
               f"{p['rows']['measured']} of {p['rows']['total']}", p["widest_reach"] or "none",
               f"[{p['contributed']['vault_page'].rsplit('/', 1)[-1]}]({p['contributed']['vault_page']})"]
              for p in D["profiles"].values() if p.get("contributed")]),
            ("note", "**The tier is the contributor's and this site did not raise it.** "
                     f"{prov['contributed']['rows']['measured']} of "
                     f"{prov['contributed']['rows']['total']} contributed rows are at the "
                     f"contributor's measured tier, from a dated probe of an instance an early "
                     f"user was entitled to run, with the write up held by the contributor as "
                     f"the evidence file. The rest were read from vendor documentation on a "
                     f"date and quoted. Nothing was probed by this site, and the rows are "
                     f"counted beside the map's {prov['rows']['total']} rather than folded "
                     f"into them, because the two were obtained differently."),
            ("p", "**The intake path is the same for anybody.** A proposed shape is a "
                  "`abp/profile/v1` file and a mandate that applies to it, fetched from an "
                  "address the proposer publishes, held here as the bytes fetched with their "
                  "hash, and promoted without renaming anything. Every capability id has to "
                  "be one of the 23; a row that needs a new verb, object class or reach is a "
                  "proposal to the grammar and needs a probe, and the contributor's "
                  "`not_in_grammar` field is where that is recorded rather than forced."),
            ("h2", "Proposing a change"),
            ("p", "**The data files are the shared facts and they live in this repository so "
                  "that people can propose changes.** The site and its data are the library; a "
                  "cloned vault is the instance. Two rules come with that."),
            ("p", "**A proposal carries evidence.** Every node taken from a third party site "
                  "carries a source URL, a retrieval timestamp and a content hash. A proposal "
                  "that changes a capability row without one is an assertion, and the release "
                  "gate refuses it."),
            ("p", "**A consumer pins a version.** Anything that computes from these files states "
                  "which version it computed against. A clone that floats against the latest has "
                  "no reproducible output."),
            ("note", "**One transform happens between these files and the pages.** The source "
                     "prose carries em dashes, en dashes and curly quotes because it was written "
                     "elsewhere, and this repository holds a rule that its documents are pure "
                     "ASCII. Both survive: the JSON keeps the upstream strings exactly as they "
                     "arrived, and every upstream string rendered into a page is transliterated "
                     "at render time. The bytes are one click away either way."),
            ("p", f"[The schema, explained](model/schema/index.html) · "
                  f"[The upstream pack manifest](data/upstream/pack.json) · "
                  f"[The map this came from]({MAP})"),
        ]}}


def pages(D=None):
    """Every generated page. Returns {rel: page}."""
    D = D or load()
    out = {}
    out.update(model_pages(D))
    out.update(examples_pages(D))
    out.update(data_page(D))
    return out


# ---------------------------------------------------------------------------
# one grant against mandate view that is not a table
# ---------------------------------------------------------------------------

# WHY A FIGURE AT ALL, given that the leaflet already says everything.
#
# The table is complete and it is the wrong shape for the one question the ABP exists to
# answer. A reader scanning rows cannot see, without counting, how much of the right hand side
# has nothing on the left. This figure makes that one thing visible and says nothing else: two
# columns, the mandate and the grant, with a line joining every capability that appears in
# both. An excess capability is a mark on the right with NO LINE REACHING IT. That is the whole
# encoding.
#
# THREE RULES IT KEEPS.
#   · Colour is never the only channel. Every mark carries its published barrier glyph and its
#     label, and the figure is readable with the fill removed.
#   · It carries no score. There is no axis of severity, no ranking and no size encoding
#     standing in for consequence. The only ordering is irreversible first, which is a property
#     of the action.
#   · It has a markdown equivalent rather than being dropped from the twin: the `both' block
#     gives the twin the same facts in prose, because the fact set has to be identical across
#     renderings even where the rendering is not.
_FILL = {"none": "#b91c1c", "expectation": "#b45309", "setting": "#a16207", "boundary": "#0f766e"}


def grant_against_mandate(profile, mandate, dlt, D, name):
    rows = abp.order(profile["grant"], D)
    want = [c for c in mandate["want"]]
    n = max(len(rows), len(want))
    top, step, h = 58, 22, 0
    h = top + n * step + 56
    lx, rx = 200, 470
    ys = {r["capability"]: top + i * step for i, r in enumerate(rows)}
    # The mandate column keeps the grant's order where it can, so a line is a short hop rather
    # than a crossing: a figure whose lines cross for no reason reads as complexity that is not
    # in the data.
    wsorted = [c for c in (r["capability"] for r in rows) if c in want] + \
              [c for c in want if c not in ys]
    wy = {c: top + i * step for i, c in enumerate(wsorted)}

    out = [f'<svg class="gam" viewBox="0 0 770 {h}" role="img" '
           f'aria-label="The mandate on the left, the grant on the right. '
           f'{len(dlt["excess"])} capabilities on the right have no line reaching them.">',
           f'<text x="0" y="20" class="gam-h">The mandate</text>',
           f'<text x="0" y="36" class="gam-s">{len(want)} authorised</text>',
           f'<text x="{rx}" y="20" class="gam-h">The grant</text>',
           f'<text x="{rx}" y="36" class="gam-s">{profile["grant_size"]} of '
           f'{D["capabilities"]["count"]} primitives</text>']
    for c in wsorted:
        y = wy[c]
        cls = "gam-line" if c in ys else "gam-line gam-short"
        if c in ys:
            out.append(f'<path class="{cls}" d="M {lx} {y} C {lx + 60} {y}, {rx - 70} '
                       f'{ys[c]}, {rx - 10} {ys[c]}"/>')
        out.append(f'<text x="{lx - 6}" y="{y + 4}" class="gam-l">{_short(c)}</text>')
        if c not in ys:
            out.append(f'<text x="{lx + 6}" y="{y + 4}" class="gam-x">asked for, cannot</text>')
    for r in rows:
        y, c = ys[r["capability"]], r["capability"]
        excess = c not in want
        dim = "" if excess else ' fill-opacity="0.3"'
        out.append(f'<circle cx="{rx - 4}" cy="{y}" r="4.5" '
                   f'fill="{_FILL[r["barrier"]]}"{dim}/>')
        out.append(f'<text x="{rx + 8}" y="{y + 4}" class="gam-r{" gam-e" if excess else ""}">'
                   f'{GLYPH[r["barrier"]]} {_short(c)}'
                   f'{" *" if D["by_id"][c]["undo"] == "no" else ""}</text>')
    # Three short lines rather than two long ones: the viewBox is 680 wide and SVG text does
    # not wrap, so a sentence that overflows is simply cut off, which is how a figure comes to
    # state half of a caveat.
    key = [f'A line means the mandate asked for it. A mark with no line is excess: '
           f'{len(dlt["excess"])} here, of which {len(dlt["unbounded_excess"])} sit at a '
           f'barrier that is not a control.',
           'The glyph is the barrier. An asterisk means the effect cannot be undone.',
           'There is no score in this figure, and no axis of consequence.']
    for i, line in enumerate(key):
        out.append(f'<text x="0" y="{h - 38 + i * 15}" class="gam-k">{line}</text>')
    out.append("</svg>")

    md = (f"*[A figure here in the page: the mandate in one column and the grant in the other, "
          f"with a line joining every capability that is in both. "
          f"**{len(dlt['excess'])} marks on the grant side have no line reaching them**, of "
          f"which {len(dlt['unbounded_excess'])} sit at a barrier that is not a control"
          + (f", and {len(dlt['shortfall'])} on the mandate side reach nothing"
             if dlt["shortfall"] else "")
          + f". The table below the figure carries the same facts, row by row.]*")
    return ("both", f'<figure class="gamwrap">{"".join(out)}'
                    f'<figcaption>{name}: the mandate against the grant. Every fact in this '
                    f'figure is in the table above it.</figcaption></figure>', md)


def _short(cap_id):
    """A capability id is the label. It is long, and shortening it to a gloss would make the
    figure say something the id does not."""
    return cap_id
