#!/usr/bin/env python3
"""The articles: one per release, with the screenshots taken from the tag each one names.

WHY THIS SECTION EXISTS. The version surface says what changed in a release, in the release's
own words, and it is deliberately terse: a title that is a sentence, a summary, a list of
changes and the basis they were built against. It does not explain anything. These articles do
the explaining, one per release, and they do it with the site as it stood at that release
rather than as it stands now, because a screenshot of today's page illustrating a claim about
September the eleventh is a small lie that nobody would ever catch.

HOW THE SCREENSHOTS WERE TAKEN, so that anybody can take them again. For each of the eight
release tags, `git worktree add --detach` produced a checkout of that exact commit, a static
server served it on a local port, and a headless browser captured the named section of the
named page. Every figure caption states the version it came from and the date it was captured.
Nothing was retouched, nothing was staged, and no screenshot shows a page that was not built
by the generator in that tag.

WHAT A FIGURE IS FOR HERE. A screenshot shows what a reader would have seen. A diagram shows a
mechanism that no screenshot can: an edge, a formula, a loop, a thing that does not happen. If
a figure would only repeat the sentence beside it, it is not here. The diagrams live in
`figures.py` and each one carries a described equivalent for the markdown twin, so a reader of
the twin is not sent to the page to find out what the picture said.

THE RULES DO NOT RELAX FOR AN ARTICLE. No score, no verdict about a named product, every
capability claim with its provenance, `agent` and never the other word, and the ABP is never
shortened to two words the estate already uses for the thing an underwriter sells.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figures  # noqa: E402
import shell  # noqa: E402

CAPTURED = "20 September 2026"


def shot(up, name, alt, caption, version):
    """A screenshot of this site at one release, with the version it came from on its face."""
    src = f"{up}assets/articles/{name}.png"
    html = (f'<figure class="shot"><img src="{src}" alt="{shell.ascii_safe(alt)}" '
            f'loading="lazy" decoding="async">'
            f'<figcaption>{shell.ascii_safe(caption)}'
            f'<span class="attr">abp.sgit.ai at {version}, captured {CAPTURED} from a '
            f'checkout of the {version} tag. Unretouched.</span></figcaption></figure>')
    md = (f"![{shell.ascii_safe(alt)}]({src})\n\n"
          f"*{shell.ascii_safe(caption)} (abp.sgit.ai at {version}, captured {CAPTURED} from a "
          f"checkout of the {version} tag.)*")
    return ("both", html, md)


def vlink(v):
    return f"[{v}'s own release record](versions/{v}/index.html)"


# ---------------------------------------------------------------------------
# the register: one row per article, and the index is generated from it
# ---------------------------------------------------------------------------

ARTICLES = [
    ("an-ontology-that-already-existed", "v0.1.0", "11 September 2026",
     "The ontology already existed, so the first release promoted it instead of writing one",
     "Twenty three capability primitives, nine deployment shapes and four barriers were "
     "already published as the data pack a game reads. The first release gave them an address "
     "and derived five worked ABPs from them, and the thing that took the time was the "
     "honesty line rather than the research."),
    ("a-rule-corrected-nine-hours-later", "v0.2.0", "11 September 2026",
     "A rule this site published in the morning was wrong by the afternoon, and the correction "
     "is on the page",
     "The foundation document says twice that the delta is computed and never stored. Half of "
     "that was right. The corrected rule is harder, the passages were not rewritten, and the "
     "check that enforced the old rule was inverted to enforce the new one."),
    ("three-nodes-and-three-edges", "v0.3.0", "12 September 2026",
     "read.file.project was a string with a gloss beside it, which is schema-first thinking in "
     "graph syntax",
     "Thirty three words that existed only as substrings got a node, a file and a page each. A "
     "node type stopped being a label and became a formula the build walks. And the reach "
     "pages started keeping nine disagreeing definitions of one word instead of averaging "
     "them."),
    ("an-abp-is-a-junction-object", "v0.4.0", "20 September 2026",
     "An ABP is a junction object, which is what Fractal Semantic Graphs is for",
     "Applying the zoom test to this site's own graph returns an uncomfortable answer: it "
     "decomposes one vocabulary very well and crosses into another in exactly two places. The "
     "map names the nine worlds one capability row actually crosses, and who owns each."),
    ("nine-universes-as-data", "v0.4.1", "20 September 2026",
     "The map became files, pages and a gate check, and the walk is rebuilt on every build",
     "A map in prose is a claim. Thirteen universes as data with a page each, a walk computed "
     "from the published rows, and a fourteenth check that refuses to publish a world nobody "
     "owns. The walk immediately found an error in the brief that drew it."),
    ("the-fact-diff-reads-the-published-page", "v0.4.2", "20 September 2026",
     "The fact diff was named as a blocker on four consecutive days, and it reads the "
     "published page",
     "Every projection renders the same fact set with an empty diff. That rule had no "
     "mechanism behind it for a month. The mechanism parses the label, the leaflet, the "
     "prohibitions and the figure back out of the page that shipped, because a diff that "
     "trusts the generator checks nothing."),
    ("the-confirmations-flag-as-a-path", "v0.4.3", "20 September 2026",
     "The home page has argued about one setting since v0.1.0, and now the build walks it",
     "A product, a tool and a setting became node types with formulas, derived from data the "
     "site already held. The setting that distinguishes confirmations on from confirmations "
     "off was found by diffing two grants, and whose material a capability reaches was "
     "declared without being guessed."),
    ("seven-shapes-somebody-else-measured", "v0.4.4", "20 September 2026",
     "Seven deployment shapes somebody else measured, promoted with their provenance intact",
     "A consumer of this data built seven shapes this site did not have, one of them from a "
     "dated probe of a live instance. Under the three layers those are facts owned by nobody, "
     "so they belong at the address every consumer reads. The bytes are held unchanged and "
     "the evidence tier stays the contributor's."),
    ("one-article-per-release", "v0.5.0", "20 September 2026",
     "The releases get one article each, and the screenshots come from the tag rather than "
     "from today's site",
     "A release record says what changed and is deliberately terse. Nothing said why. This "
     "release adds the section you are reading, and the rule that makes it worth reading: a "
     "figure about the eleventh of September shows the site as it stood on the eleventh of "
     "September, version badge and all."),
]

BY_SLUG = {a[0]: a for a in ARTICLES}

# THE REGISTER IS CHRONOLOGICAL AND THE INDEX IS NOT. The list above is in the order the
# releases happened, because that is the order the story makes sense in and the order the
# older/newer links walk. A reader arriving at the index wants the most recent release
# first, so the index reverses it. One list, two orders, and neither is maintained by hand.
NEWEST_FIRST = list(reversed(ARTICLES))


def neighbours(slug):
    """The release before this one and the release after it, in release order."""
    i = [a[0] for a in ARTICLES].index(slug)
    older = ARTICLES[i - 1] if i > 0 else None
    newer = ARTICLES[i + 1] if i + 1 < len(ARTICLES) else None
    return older, newer


def href(slug):
    return f"articles/{slug}/index.html"


# ---------------------------------------------------------------------------
# the index
# ---------------------------------------------------------------------------

def _index():
    up = "../"
    return {
        "title": "The articles",
        "description": "One article per release, explaining what changed and why, with the "
                       "screenshots taken from the tag each one names and diagrams of the "
                       "mechanisms a screenshot cannot show.",
        "blocks": [
            ("crumb", "[Home](index.html) / Articles"),
            ("h1", "One article per release"),
            ("lead", "The version surface says what changed, in the release's own words, and "
                     "it is deliberately terse. **These articles say why**, one per release, "
                     "and they show the site as it stood at that release rather than as it "
                     "stands now."),
            ("h2", "Eight releases, four measures"),
            figures.evolution(),
            ("h2", "The articles, newest release first"),
            ("p", "**One article per release, and the article is the release.** Each one is "
                  "titled with the version it is about, says what that release changed and "
                  "what it did not settle, and links to the release before it and the release "
                  "after it, so the sequence can be read in either direction."),
            ("cards", [{"title": f"[{v}: {t}]({href(s)})", "sub": lead,
                        "foot": f"{d} &#183; " + ("the current release" if i == 0 else
                                                  f"{i} release{'s' if i > 1 else ''} back")}
                       for i, (s, v, d, t, lead) in enumerate(NEWEST_FIRST)]),
            ("p", "**Reading forwards** starts at "
                  f"[{ARTICLES[0][1]}]({href(ARTICLES[0][0])}), the first release, and follows "
                  f"the newer link at the foot of each article. **Reading backwards** starts at "
                  f"[{ARTICLES[-1][1]}]({href(ARTICLES[-1][0])}) and follows the older link."),
            ("h2", "How the screenshots were taken"),
            ("p", "**Every screenshot in these articles came from the tag it names, not from "
                  "today's site.** For each of the eight release tags, a detached worktree "
                  "produced a checkout of that exact commit, a static server served it on a "
                  "local port, and a headless browser captured the named section of the named "
                  "page. Every caption states the version and the capture date on its face."),
            ("note", "**Why that is worth the trouble.** A screenshot of today's page "
                     "illustrating a claim about the eleventh of September is a small lie, and "
                     "it is the kind nobody ever catches, because the page looks right and the "
                     "claim sounds right. The tags are in the repository and the method is "
                     "four commands, so the figures are reproducible rather than trusted."),
            ("h2", "What these articles do not do"),
            ("ul", [
                "**They carry no score.** Not a rating and not a level, here or anywhere else "
                "on this site. That rule is the reason the site exists in the shape it does.",
                "**They make no claim about a named product.** Where an article names one, it "
                "names it as a deployment shape with a source, a date and a measured ratio, "
                "and attaches no adjective to it.",
                "**They do not restate the model.** Where an article describes a rule, it "
                "links to the page that owns it. If the two ever disagree, the model page is "
                "right and this is an article that needs correcting.",
            ]),
            ("p", "[The version surface](versions/index.html) &#183; "
                  "[The model](model/index.html) &#183; [The data](data/index.html)"),
        ],
    }


def _nav_block(slug, where):
    """Older and newer, named rather than numbered, so the direction is never in doubt."""
    older, newer = neighbours(slug)
    rows = []
    if older:
        rows.append(["**Older**", f"[{older[1]}: {older[3]}]({href(older[0])})"])
    if newer:
        rows.append(["**Newer**", f"[{newer[1]}: {newer[3]}]({href(newer[0])})"])
    rows.append(["**All of them**", "[One article per release](articles/index.html)"])
    return [("h2", where), ("table", ["Direction", "The release"], rows)]


def pages():
    out = {"articles/index.html": _index()}
    n = len(ARTICLES)
    for i, (slug, v, date, title, lead) in enumerate(ARTICLES):
        body = BODIES[slug]("../../")
        older, newer = neighbours(slug)
        # The position is computed rather than written, so it cannot go stale when a release
        # is added: an article that said `the latest' would be wrong on the next push.
        place = (f"It is release {i + 1} of {n} on this site"
                 + (", and the most recent" if not newer else ""))
        out[href(slug)] = {
            "title": f"{v}: {title}",
            "description": shell.strip(lead),
            "blocks": [
                ("crumb", f"[Home](index.html) / [Articles](articles/index.html) / {v}"),
                ("h1", f"{v}: {title}"),
                ("lead", lead),
                ("note", f"**This is the article for release {v}, published {date}.** Every "
                         f"release of this site gets one, and it explains what that release "
                         f"changed and why rather than restating "
                         + vlink(v) + f". {place}. Every screenshot below was captured from a "
                         f"checkout of the `{v}` tag, so it shows the site as it stood at that "
                         f"release and not as it stands today. "
                         + (f"Read on to [{newer[1]}]({href(newer[0])})"
                            if newer else "Nothing follows it yet")
                         + (f", or back to [{older[1]}]({href(older[0])})." if older
                            else ", and it is where the sequence starts.")),
            ] + body + _nav_block(slug, "Read the sequence"),
        }
    return out


# ---------------------------------------------------------------------------
# v0.1.0
# ---------------------------------------------------------------------------

def _v010(up):
    return [
        ("h2", "The gap the document exists for"),
        ("p", "**You know what you asked for.** Draft the reply, fix the build, summarise the "
              "ticket. That is the mandate, and the person who deployed the agent already "
              "holds it, whether or not anybody wrote it down."),
        ("p", "**You do not know what it can do.** The agent runs with an account, on a "
              "machine, in a container or on a desktop, with credentials and network access "
              "and a set of tools. Everything those permit is the grant. It is almost never "
              "enumerated, and when it is, it is larger than the person who deployed it "
              "expected. The Agent Behaviour Policy is the document that puts the two on one "
              "page."),
        shot(up, "v010-home-hero",
             "The home page of abp.sgit.ai at v0.1.0, with the thesis line as the heading",
             "The first release's home page. The argument is the heading, and the version "
             "badge in the chrome links to that version's own record rather than to a generic "
             "changelog, which is one of the five things the house conventions ask a site to "
             "verify rather than assume.", "v0.1.0"),

        ("h2", "The finding that changed the plan"),
        ("p", "The build pack written before this site existed contains one sentence that "
              "changed what the first release was: **the ontology the ABP needs already "
              "exists, published, and the first job is not to author one.** A game about agent "
              "permissions had published its data pack at a stable address: twenty three "
              "capability primitives in a `verb.object.reach` grammar, nine named deployment "
              "shapes, a barrier glyph on every cell, an undo class on every capability, and "
              "an honest measurement note saying that of ninety nine rows, twenty one were "
              "measured and the rest derived."),
        ("note", "**Promoting an ontology means giving it an address, not a new vocabulary.** "
                 "Nothing was renamed. Capability ids, barrier ids, undo classes and shape ids "
                 "are the published ones, the bytes as fetched are served unchanged under "
                 "`data/upstream/`, and both the build and the gate recompute their hash and "
                 "refuse to proceed if it disagrees. Two field names changed and the provenance "
                 "block on each file says which."),

        ("h2", "Four objects, and only one of them is written by anybody"),
        ("p", "An ABP is not a document. It is four objects, of which the document is a "
              "rendering, and the order they are produced in is the order "
              "[the model page](model/index.html) teaches them."),
        figures.four_objects(),
        ("p", "**The mandate has to be captured even though it is already known**, because a "
              "grant on its own is an inventory and nobody acts on an inventory. That is the "
              "whole reason the cheapest object to collect is the one that makes the other "
              "three mean something."),

        ("h2", "The barrier, which is where the argument actually is"),
        ("p", "For every capability in the grant, an ABP records what stands between the agent "
              "and it. There are four kinds, and three of them bound nothing. That is not an "
              "opinion about the four rows: it follows from what each one is."),
        figures.barrier_ladder(),
        ("p", "**The estate published this as a glyph before it named it as a rule.** The "
              "game's map already carried all four kinds on every cell, and reading the third "
              "and fourth rows together gives you the test: a setting the agent's own account "
              "could change is not a control, because the grant includes the ability to remove "
              "the bound. [The barrier page](model/barriers/index.html) carries the four with "
              "their published wording."),

        ("h2", "Five examples, derived rather than authored"),
        ("p", "The five worked ABPs in the first release were not written. Every number, every "
              "glyph and every row on them is computed from the promoted data at build time, "
              "which is what makes the provenance line trustworthy: a page that states twenty "
              "one of ninety nine rows measured, and got that from a constant somebody typed, "
              "is asserting exactly what the map is careful to qualify."),
        shot(up, "v010-examples-table",
             "A table of the five worked examples with their grant, mandate, excess and "
             "unbounded excess counts",
             "The five examples at v0.1.0, side by side. No column here is a score: excess is "
             "a count of capabilities in the grant and not in the mandate, and unbounded "
             "excess is how many of those sit at a barrier that is not a control. Neither says "
             "whether any of it is acceptable.", "v0.1.0"),
        ("p", "**Read the third one beside the second.** They are the same product, the same "
              "machine and the same account, with one setting different. That pair is the "
              "argument that an ABP is about the deployment rather than the product, and it is "
              "the release's cheapest demonstration: one line in a list and a build."),

        ("h2", "The label, and the only number a buyer can move"),
        shot(up, "v010-label",
             "The nine field label for a coding agent with confirmations off",
             "Nine fields, computed, and no score anywhere on them. Excess answers the "
             "question the document exists for. Unbounded excess is the only field a control "
             "purchase moves, and the gap between the two is the business case for one.",
             "v0.1.0"),
        ("p", "**Two numbers matter and the label says which.** Every real control put in "
              "place shifts one capability into the fourth barrier row and the second number "
              "falls. The first one does not move, because the agent can still do the same "
              "things: what changed is that some of them are now bounded by something it "
              "cannot reach."),

        ("h2", "One figure, answering one question"),
        ("p", "The leaflet is complete and it is the wrong shape for the question the document "
              "exists to answer, which is how much of the grant has nothing on the mandate "
              "side. A reader scanning rows cannot see that without counting."),
        shot(up, "v010-figure",
             "The mandate in one column and the grant in the other, with lines joining the "
             "capabilities that appear in both",
             "The whole encoding is one rule: a mark with no line reaching it is excess. The "
             "glyph on every mark is the published barrier, so the figure is readable with the "
             "fill removed, and there is no size encoding and no axis of consequence in it.",
             "v0.1.0"),

        ("h2", "The prohibitions, each carrying its barrier"),
        ("p", "The enforceable projection of the delta is one sentence per excess capability. "
              "**Every one of them carries the barrier it sits at today**, because a "
              "prohibition shown without its barrier manufactures assurance."),
        shot(up, "v010-prohibitions",
             "A table of prohibitions, each with its barrier today, whether it is enforced, "
             "and the layer a control would sit at",
             "Twelve of twelve not enforced today. They are sentences, not controls. The right "
             "hand column is where a control would have to sit, which is a statement about "
             "where enforcement lives and not a recommendation to buy one.", "v0.1.0"),

        ("h2", "What the release cost, and the number it could not produce"),
        ("p", "The examples were instrumented rather than estimated, because the store has to "
              "price an ABP and nobody knew what one costs. The published table says five "
              "minutes each and nought questions asked of a human."),
        ("note", "**That is the wrong number and the page says so.** The five examples took "
                 "about four hours in total and essentially all of it went into the generator, "
                 "the promoted schema and the provenance line. The marginal cost of the sixth, "
                 "for a shape already in the map, is one line and a build. The number the store "
                 "needs is what it costs to produce an ABP for a shape that is **not** in the "
                 "map, where the grant has to be measured rather than looked up, and this site "
                 "could not tell you that because it had not done one."),

        ("h2", "A disagreement recorded rather than resolved"),
        ("p", "The foundation document says that turning confirmations off moves the barrier "
              "on every capability in the delta by one row. **In the published data it moves "
              "exactly one barrier**, on `execute.process.host`, and that capability is inside "
              "the mandate rather than in the delta, because the deployer asked for it. So the "
              "label's numbers do not move at all, and the two documents are still materially "
              "different."),
        ("p", "That is a stronger argument for the leaflet and against a headline number than "
              "the original wording was, and it is recorded in "
              "[v0.1.0's notes](versions/v0.1.0/index.html) rather than quietly fixed. The "
              "method is to record the gap."),
        ("p", "[The five examples](examples/index.html) &#183; "
              "[The capability grammar](model/capabilities/index.html) &#183; "
              "[The barrier](model/barriers/index.html) &#183; "
              + vlink("v0.1.0")),
    ]


# ---------------------------------------------------------------------------
# v0.2.0
# ---------------------------------------------------------------------------

def _v020(up):
    return [
        ("h2", "The rule that was wrong by lunchtime"),
        ("p", "The foundation document was published on the morning of 11 September. It says, "
              "twice, that **the delta is computed and never stored**. Nine hours later the "
              "project lead corrected it, and v0.2.0 is that correction applied in the open."),
        ("p", "The first half was right and the second half was wrong. The corrected rule is "
              "that **the delta is derived and never authored**, which is the harder rule, "
              "because it forbids the act rather than the artefact."),
        shot(up, "v020-delta-correction",
             "A two column table showing the old wording beside the corrected wording",
             "The correction, on the page, with both passages quoted in full. A document "
             "corrected by silently editing it is a document nobody can trust, so the old "
             "wording is not deleted: it is shown beside what replaced it.", "v0.2.0"),

        ("h2", "What the old rule was protecting, and why all of it survives"),
        ("p", "The sentence being corrected was guarding against three real things, and the "
              "correction loses none of them."),
        ("table", ["The fear", "Does the correction still handle it"], [
            ["A stored delta becomes a stale claim about somebody's environment",
             "**Yes.** It carries the versions of its inputs and the time it was computed, so "
             "its staleness is a fact rather than a surprise"],
            ["A delta gets hand edited into a fiction",
             "**Yes, and more strongly.** Never authored forbids the act; never stored only "
             "forbade the artefact"],
            ["A delta is treated as authoritative after the inputs move",
             "**Yes.** It reacts. A recompute is cheap because the inputs are graphs with a "
             "schema rather than prose"],
        ]),
        ("p", "**And the correction gains the history**, which the old rule made impossible. "
              "Asking whether a control was in place throughout a period is a question about a "
              "series, and a recomputed present cannot answer it."),

        ("h2", "The word for this already existed"),
        ("p", "A stored result of a computation over other data, refreshed when its inputs "
              "change, never edited directly, is a **materialised view**. The vocabulary is "
              "decades old and it carries exactly the right properties: it exists for use, it "
              "has a refresh policy, its staleness is knowable, and writing to it directly is a "
              "category error rather than a permission question."),
        ("note", "**It is the fourth instance of a pattern already in force here.** Indexes are "
                 "generated from the data they index. Prose is derived from the graph and never "
                 "hand edited. A bill of materials is generated from the dependency files. And "
                 "the delta is derived from the grant and the mandate. In every case the "
                 "artefact is stored, and what is forbidden is writing it."),
        shot(up, "v020-stored-record",
             "The fields of a stored delta record: the pinned input versions, when it was "
             "computed and by which version of the computation",
             "Eight fields, none of them writable by a person. `computed_by` is the version of "
             "the code, because the code changes and a record that does not say what computed "
             "it cannot be compared with one produced later.", "v0.2.0"),

        ("h2", "The check was inverted rather than removed"),
        ("p", "Until this release the release gate refused **any** file carrying a delta, which "
              "is how a machine holds a rule that says never stored. The corrected rule needs "
              "the opposite check, and it is the more useful one."),
        ("pre", "validate: OK -- v0.2.0 on abp.sgit.ai, 55 pages, links resolve,\n"
                "  every page has a twin and is in llms.txt, no score vocabulary,\n"
                "  no forbidden word, no em dash outside the promoted data,\n"
                "  the upstream bytes hash to their manifest, and\n"
                "  EVERY STORED DELTA RECOMPUTES FROM ITS OWN PINNED INPUTS."),
        ("p", "**The gate does not take a stored record on trust.** It recomputes every one of "
              "them from the profile and the mandate it names and fails on a single row of "
              "disagreement, including the ordering. That check is a few lines, because the "
              "computation is a set difference, and it is a set difference because the grant "
              "and the mandate are held as graphs with a schema rather than as prose. **That "
              "is the underlying capability.** All of it can be done by hand today and almost "
              "nobody does it."),

        ("h2", "Reality is the third input"),
        ("p", "The grant is a model of what the agent can do and the mandate is a statement of "
              "what somebody meant. Both are interpretations and both improve. A capability "
              "nobody had listed turns up; a barrier was recorded at the wrong kind; something "
              "in the mandate never happens."),
        ("note", "**One row of that table cannot resolve itself.** An agent doing something "
                 "outside its mandate, repeatedly, without anybody complaining, means either "
                 "that the mandate was written too narrowly or that something is happening "
                 "nobody authorised. This site publishes the observation. Which of the two it "
                 "is belongs to the risk layer and to a person."),
        shot(up, "v020-three-clocks",
             "A table of three clocks: the ABP's, the twin's, and reality's",
             "An ABP is exactly as fresh as the twin, and the twin is exactly as fresh as its "
             "connection. That is a parameter rather than a defect to hide, and it went onto "
             "the validity statement on every example page in this release.", "v0.2.0"),

        ("h2", "The document was not rewritten"),
        ("p", "The foundation document is the definition the rest of the site stands on, and "
              "it is the document being put in front of people for feedback. **Both corrected "
              "passages stand exactly as published**, each with its correction rendered "
              "immediately above it."),
        shot(up, "v020-foundation-note",
             "A correction notice rendered above the passage it corrects",
             "The correction is attached to the passage rather than applied to it. The "
             "generator refuses to build if a correction finds no passage to attach to, "
             "because a correction that silently fails to render is worse than no correction.",
             "v0.2.0"),

        ("h2", "What this release did not settle"),
        ("ul", [
            "**What the recompute policy is**: on every event, on a schedule, on read, or a "
            "combination. It decides how much a receiver has to do.",
            "**Who sets the thresholds a consequence hooks to**: the customer, the "
            "underwriter, or a default published here. All three have different shapes, and a "
            "threshold crossing is a record while the consequence is something somebody set "
            "in advance.",
            "**How a calibration contribution is submitted without revealing the deployment**, "
            "since a correction to a capability row implies somebody runs that shape.",
            "**What happens to a stored delta whose computation version is superseded**: "
            "recomputed, marked, or left as the record of what was believed at the time. The "
            "third is the most honest and the least useful.",
        ]),
        ("p", "[The delta](model/delta/index.html) &#183; "
              "[The stored deltas as JSON](data/deltas/index.json) &#183; "
              + vlink("v0.2.0")),
    ]


# ---------------------------------------------------------------------------
# v0.3.0
# ---------------------------------------------------------------------------

def _v030(up):
    return [
        ("h2", "The model pages were a projection of nothing"),
        ("p", "For two releases this site said, on the graph page, that an ABP is a graph and "
              "every document is a projection of it. It was not. A capability was an "
              "identifier with a gloss beside it, and the gloss was the definition."),
        ("note", "**That is a self-describing node, which is schema-first thinking dressed in "
                 "graph syntax.** The meaning was attached to the node rather than derived from "
                 "its edges. `read.file.project` was a string, so `read`, `file` and `project` "
                 "were unaddressable: nothing could link to them, nothing could disagree with "
                 "them, and a customer vault had nowhere to attach a bridge."),
        figures.string_vs_nodes(),
        shot(up, "v030-lexicon-spelled",
             "A table spelling out one primitive as five nodes joined by five named edges",
             "One primitive, spelled out. Each of those is a link because each of those is a "
             "node with an address, a JSON file and a page of its own.", "v0.3.0"),

        ("h2", "The page that carries the disagreement"),
        ("p", "The reach class pages are the ones to read, and `host` is the clearest case in "
              "the model. **The nine deployment shapes do not agree about what it means**, and "
              "the page keeps the disagreement rather than averaging it."),
        shot(up, "v030-host-disagreement",
             "Nine rows, one per deployment shape, each with that shape's own definition of "
             "the word host",
             "Nine definitions of one word, none of them merged, each owned by the shape that "
             "said it. A reader deciding what `host` costs them has to read the row for the "
             "shape they run, not an average of the rows.", "v0.3.0"),
        ("p", "**That is the ABP's own argument in one column.** The same word, the same "
              "grammar, and a materially different exposure depending on where the agent runs. "
              "It is also the first place on this site where zooming into a node lands you "
              "somewhere with its own vocabulary, which is the property the releases six "
              "months of releases later would be named after."),

        ("h2", "Classification stopped being a label"),
        ("p", "Until this release a barrier carried `is_control: true`, which is a label "
              "somebody applied. A node type is now a **required pattern of typed, directed "
              "paths** that a node either matches or does not, and the build walks it."),
        shot(up, "v030-formulas-table",
             "Thirteen node types, each with a formula and the count of nodes that matched",
             "Thirteen formulas, walked against the graph on every build. The counts are the "
             "result of running them rather than fields anybody set, which is why a formula "
             "that stops matching is a finding rather than a cosmetic change.", "v0.3.0"),
        shot(up, "v030-control-formula",
             "The Control formula, with a table showing which of the four barriers matches it",
             "The one that carries the argument. Exactly one of the four barriers matches, and "
             "the release gate fails if that stops being true, because every page on this site "
             "is written against it.", "v0.3.0"),
        ("p", "**Judgment does not disappear**, and that objection deserves a direct answer. "
              "Somebody still decided that a control must be enforced from outside the grant. "
              "What changes is where that decision lives: out of a classifier's head and into "
              "a formula that is visible, versioned, inspectable and arguable. You can now "
              "disagree with a classification by pointing at a line, which you could not do "
              "before."),

        ("h2", "Fifteen edges, and no generic one"),
        ("p", "The edge vocabulary arrived in the same release: fifteen edges, each a verb "
              "with a distinct and meaningfully named inverse, a stated domain and a stated "
              "range. **The inverse is not the same edge walked backwards**: `grants` and "
              "`granted_by` have different fan out, and that asymmetry is what stops a "
              "traversal exploding."),
        ("note", "**There is no generic association edge in this model and there will not be "
                 "one.** It constrains nothing and costs fan out. If you find yourself wanting "
                 "one, the honest move is a new edge with a sentence, a different sentence for "
                 "its inverse, and a stated domain and range. Four of the fifteen are reused "
                 "from the network's published edge set under their published names; eleven "
                 "are proposed here and say so."),

        ("h2", "The construction a customer vault needs"),
        ("p", "A customer will disagree with some of this vocabulary, and they will often be "
              "right about their own estate. **The wrong response is to merge their definitions "
              "into these**, because merging is destructive and what it destroys is the "
              "finding."),
        shot(up, "v030-layers",
             "A table of this site's formulas beside a customer's stricter versions of them",
             "Layer two: each party classifies the same shared nodes with its own rules. A "
             "regulated customer who requires a control to be evidenced as well as enforced "
             "writes their own formula over the same facts, and both numbers are correct.",
             "v0.3.0"),
        ("p", "**Parties can disagree about meaning while still agreeing about facts**, which "
              "is the only stable basis for working together. A customer who cannot accept "
              "this site's definition of a control can still accept that their agent can read "
              "every file the account can reach, and that is the sentence the ABP needed them "
              "to reach."),

        ("h2", "What the gate found on its first run"),
        ("p", "A thirteenth check arrived with the graph, and it found something immediately: "
              "**`receive` and `revoke` are in the published verb list and no primitive uses "
              "them.**"),
        ("note", "**They are kept and marked rather than dropped.** A node connected to nothing "
                 "is literally meaningless, so those two words mean nothing in this graph yet, "
                 "and saying so is more useful than writing them a definition no edge supports. "
                 "It is a finding about the vocabulary rather than a defect in it, and it is "
                 "the kind of gap that only becomes visible once the words are nodes."),
        ("p", "[The lexicon](model/lexicon/index.html) &#183; "
              "[The edge vocabulary](model/graph/edges/index.html) &#183; "
              "[The node type formulas](model/graph/formulas/index.html) &#183; "
              "[The three layers](model/graph/layers/index.html) &#183; " + vlink("v0.3.0")),
    ]


# ---------------------------------------------------------------------------
# v0.4.0
# ---------------------------------------------------------------------------

def _v040(up):
    return [
        ("h2", "A test this site had been quoting backwards"),
        ("p", "The network's graph site defines a property it calls fractal, and this site's "
              "graph module quoted its first edition: *if zooming into a node needs a new "
              "format or a special case, the system is hierarchical rather than fractal.* "
              "**That wording scores decomposition as a pass**, and it was corrected at the "
              "source in August and propagated in September."),
        ("p", "The corrected test is in two halves. What survives every zoom is the "
              "**grammar**: every edge a verb with an inverse, meaning in connectivity, "
              "supersede never delete, provenance kept. The **ontology** is meant to change. A "
              "system whose types and verbs are identical all the way down is a hierarchy."),
        figures.zoom_test(),

        ("h2", "Applying it to this site, and not liking the answer"),
        ("p", "Run that test against the graph this site held at v0.3.0, zoom by zoom, and the "
              "result is uncomfortable."),
        ("table", ["Zoom", "What you land in", "Verdict"], [
            ["A capability into its verb, object and reach",
             "three nodes in the same lexicon", "**Decomposition** in one vocabulary"],
            ["A deployment shape into its grant",
             "granted capability nodes, same vocabulary", "**Decomposition**"],
            ["A mandate into what it authorises", "capability nodes", "**Decomposition**"],
            ["A reach class into what each shape says it means",
             "nine rows, each owned by the shape that said it",
             "**Fractal.** The first one on the site"],
            ["This vocabulary into the game's", "one declared bridge, partial on purpose",
             "**Fractal**, and honest that the bridge is total today"],
            ["A barrier into what enforces it", "three enforcer nodes and no vocabulary",
             "One edge deep, then it stops"],
            ["A granted row into how it is known", "an evidence tier and nothing behind it",
             "One edge deep, then it stops"],
        ]),
        ("note", "**That is not a defect in v0.3.0.** It passes the grammar half everywhere, "
                 "which is the half a validator, a query engine and a provenance rule care "
                 "about. It is fractal in exactly two places, and in three more it takes one "
                 "step into another world and finds it empty. What a map has to add is not more "
                 "nodes in the grammar: it is the worlds the existing edges already point at."),

        ("h2", "An ABP is a junction object"),
        ("p", "Here is the finding the map is built on. **The four objects of an ABP are owned "
              "by four different parties who speak four different vocabularies.** The grant is "
              "the vendor's published words. The evidence for it belongs to whoever observed. "
              "The barrier belongs to whoever set the control, who is often neither. The "
              "mandate is the deployer's own sentence about a job. And the licence that sits "
              "above all of it belongs to a different site entirely."),
        ("p", "That is precisely the case Fractal Semantic Graphs exists for, so the right "
              "model is not one bigger ontology. It is nine small ones joined by named edges, "
              "with the grammar shared and nothing else."),
        figures.nine_universes(),

        ("h2", "Three words, and one ruling that keeps the map from collapsing"),
        ("p", "This site and the network's definition page use the word **altitude** for "
              "different things, and the map could not be drawn until that was settled."),
        ("table", ["Word", "The ruling"], [
            ["**Altitude**", "Keeps its 20 August sense here: a rendering of the same facts "
             "for a different reader. It lives inside the projections universe and is never a "
             "different world."],
            ["**Universe**", "Adopted from the definition page's own sentence, that on one of "
             "those links you can jump into another universe. A world with its own owner, node "
             "types and verbs."],
            ["**Level**", "Position on the ladder only: down towards the byte, up towards the "
             "estate of agents."],
        ]),
        ("note", "**Levels run up and down. Universes run across.** The four objects are not a "
                 "stack: the mandate is not above the grant and the delta is not below the "
                 "barrier. They sit side by side and each opens into a different world. A map "
                 "that stacks them is a hierarchy with the wrong shape, which is the mistake "
                 "the whole exercise is trying to avoid."),

        ("h2", "The release that publishes a map and builds nothing"),
        ("p", "v0.4.0 is a brief and two corrections. It adds no data, no formula and no page "
              "beyond the brief itself and a pointer to it from "
              "[the graph page](model/graph/index.html)."),
        shot(up, "v040-graph-landed",
             "The graph page listing where each published rule landed, with the map added as a "
             "new row",
             "The map is reachable from the model rather than only from the docs index. The "
             "four rows above it are what v0.3.0 built; the fifth is a brief that says what "
             "the releases after it would build, one universe at a time.", "v0.4.0"),
        ("p", "**Naming the gaps is the point of publishing a map before building it.** Four "
              "of the thirteen universes are named with an owner and nothing behind them: the "
              "twin, the obligations, the runtime and the estate of agents. Named gaps get "
              "filled and unnamed ones do not."),
        ("p", "[The map](model/universes/index.html) &#183; "
              "[The graph rules](model/graph/index.html) &#183; " + vlink("v0.4.0")),
    ]


# ---------------------------------------------------------------------------
# v0.4.1
# ---------------------------------------------------------------------------

def _v041(up):
    return [
        ("h2", "A map in prose is a claim"),
        ("p", "v0.4.0 drew the map in a brief. A brief is a document, and a document cannot be "
              "checked. **This release turns the map into files the build reads, pages that "
              "render one query, and a check that refuses to publish a world nobody owns.**"),
        ("p", "Thirteen universes are authored once, in one module, each with its owner, its "
              "centre of gravity, its smallest node, its status, its node types and its verbs. "
              "The build writes one file per universe and an index that carries the walk."),

        ("h2", "The walk is computed, not written"),
        ("p", "The index carries one capability row walked through nine universes. Every cell "
              "of it is built from the published profile, the published mandate and the stored "
              "delta on every build, **so the sentence it reads as cannot drift from the rows "
              "it is made of.**"),
        shot(up, "v041-walk",
             "A nine row table following one capability through nine universes, and the same "
             "walk written out as one sentence",
             "One row, nine worlds, and the fifth graph rule applied across nine vocabularies "
             "rather than within one. Every clause of the sentence underneath is a node this "
             "site holds or an edge somebody has declared.", "v0.4.1"),
        ("note", "**The walk found an error in the brief that drew it, on its first run.** The "
                 "brief walked `send.endpoint.world` through the container shape. That shape "
                 "does not grant it: it grants `send.endpoint.allowed`, and the mandate asked "
                 "for it, so the path would never have reached a prohibition at all. The data "
                 "walks `authenticate-as.credential.tenant`, which is excess and bounded. The "
                 "correction is recorded in the brief, above the table it corrects, rather than "
                 "applied quietly."),

        ("h2", "Thirteen worlds, and a status that is a claim"),
        shot(up, "v041-thirteen",
             "Thirteen universes with their level, owner, status, node types and verb counts",
             "Nine the walk crosses and four it names. A status is not a label here: live "
             "means every node type the universe declares exists in the graph today, and a gap "
             "must declare none.", "v0.4.1"),
        ("table", ["Status", "What it claims", "What the gate checks"], [
            ["`live`", "its node types exist in the graph today",
             "every declared type is in the graph, or the build fails"],
            ["`partial`", "some of them do", "the ones marked as existing really do"],
            ["`one-edge`", "an edge reaches in and finds no vocabulary yet", "the same"],
            ["`outside`", "another site owns it; this one holds the anchors",
             "it claims no node types of its own"],
            ["`gap`", "named so the next release has an address", "it declares none"],
        ]),
        ("p", "**Two statuses moved during this release because the status became a check.** "
              "The source bytes and the derivation were written down as live in the brief. The "
              "gate disagreed: provenance is per file rather than per node, and a delta record "
              "is a file rather than a node in the graph. Both are `partial`, and the prose in "
              "the brief stands as written with the data as the record."),

        ("h2", "A junction is computed rather than declared"),
        ("p", "The property that turns a set of graphs into a fractal rather than a pile is "
              "the edge that crosses from one world into another. **This site does not declare "
              "which edges those are.** Every node type names its universe, every edge names "
              "the universes of its domain and range, and an edge crosses when the two differ."),
        shot(up, "v041-junctions",
             "Six edges that cross a universe boundary, each with its inverse, the world it "
             "leaves and the world it enters",
             "Computed from the edge vocabulary, so this table cannot disagree with it. The "
             "brief names twenty two junctions in all; these are the ones the graph held at "
             "this release.", "v0.4.1"),

        ("h2", "One page per world"),
        shot(up, "v041-u4",
             "The enforcement universe page: its owner, centre of gravity, smallest node and "
             "status, with the node types it has and the ones it needs",
             "Each universe renders its own ontology. The formula column separates what is "
             "walked on every build from what the world needs and does not have, which is the "
             "honest shape of a world that is one edge deep.", "v0.4.1"),

        ("h2", "The fourteenth check, and proving it bites"),
        ("p", "A check that has never failed is a check nobody has tested. Before this release "
              "was committed the index was corrupted three ways on purpose, and the gate named "
              "each one."),
        ("pre",
         "$ node admin/build/validate.js\n"
         "validate: 3 error(s)\n"
         "  x data/universes/index.json: u3 has no owner -- a world nobody owns is a\n"
         "    merge waiting to happen\n"
         "  x data/universes/index.json: grants crosses from u2 to u1 and is not listed\n"
         "    as a junction\n"
         "  x data/universes/index.json: the walk stands on send.endpoint.world, which\n"
         "    anthropic/claude-code-remote/ccr-container does not grant"),

        ("h2", "And a reading of the prior work, published as received"),
        ("p", "The same release carries something that is not this site's: an external review "
              "of the Fractal Semantic Graphs claim against the research it sits beside. "
              "Distributed description logics and their bridge rules, E-connections, "
              "distributed first order logic, named graphs, ontology alignment, federated "
              "query, engineering lifecycle integration, data mesh, machine readable control "
              "catalogues and two formal accounts of provenance."),
        shot(up, "v041-research-refs",
             "A table of twenty four references with the address each was resolved at and its "
             "status",
             "The review arrived with its citation markers stripped by the paste, so every "
             "reference was located and fetched on the day. Three resolved to a publisher that "
             "refused an unauthenticated fetch, which is a fact about the publisher; one vendor "
             "page had moved; one paper could not be located at all, and the table says so.",
             "v0.4.1"),
        ("note", "**The review's sharpest point is taken and is not yet built.** A bridge that "
                 "says *same individual* is not a bridge that says *approximate match*, and a "
                 "client that follows an edge without knowing which of those it is has not "
                 "interpreted it. Every junction and every declared bridge should carry a kind. "
                 "That is written down as the next change rather than quietly added to the "
                 "data, because the map is published and changing it silently is the thing this "
                 "site keeps refusing to do."),
        ("p", "[The universes](model/universes/index.html) &#183; "
              "[The universes as JSON](data/universes/index.json) &#183; "
              "[The research note](docs/index.html#research) &#183; " + vlink("v0.4.1")),
    ]


# ---------------------------------------------------------------------------
# v0.4.2
# ---------------------------------------------------------------------------

def _v042(up):
    return [
        ("h2", "A rule with no mechanism behind it"),
        ("p", "**Every projection renders the same fact set, and the diff must be empty.** "
              "That rule has been in force across this estate since August. It is the thing "
              "that makes a document rendered for a decision maker and a document rendered for "
              "an engineer two views of one set of facts rather than two documents that happen "
              "to be about the same agent."),
        ("p", "It was named as the blocker on four consecutive days in September, because **the "
              "diff did not exist.** A promise that cannot be checked is a promise that may be "
              "described and may not be printed, and the store's multi format offer sat behind "
              "exactly that line."),

        ("h2", "What the diff is over"),
        ("p", "The specification was precise and it is worth restating, because it is the "
              "thing that makes the check cheap. **The facts are the leaf assertions.** The "
              "classes are how a reader groups them, and they differ by altitude, which is "
              "correct rather than a defect."),
        figures.fact_diff(),
        ("p", "So a fact set is written for every stored delta: what the shape grants, at what "
              "barrier, with what undo class and what evidence tier; the stance the mandate "
              "takes on all twenty three primitives; and the excess, unbounded excess, aligned "
              "set and shortfall that follow. It pins the same inputs the delta pins, and no "
              "field in it is writable by a person."),

        ("h2", "Why it reads the published page"),
        ("p", "This is the decision that makes the check worth having. **The gate does not "
              "compare the generator's intermediate values.** It opens each example's "
              "published markdown twin, parses the label, the leaflet, the prohibitions and "
              "the figure back out of the rendered text, and compares each leaf assertion with "
              "the fact set, in both directions."),
        ("note", "**A diff that trusted the generator would be a diff over nothing.** The label "
                 "and the leaflet are produced from one call, so they could only disagree with "
                 "the fact set if that call disagreed with itself. Parsing the artefact is what "
                 "makes them two renderings that are checked to carry the same facts rather "
                 "than asserted to."),
        ("pre",
         "$ node admin/build/validate.js\n"
         "validate: 4 error(s)\n"
         "  x examples/claude-code-cli-confirmations-disabled/index.md: the label says\n"
         "    Excess is \"11\", the fact set says \"12\"\n"
         "  x examples/claude-code-cli-confirmations-disabled/index.md: the leaflet says\n"
         "    authenticate-as.credential.signing is at barrier \"boundary\", the fact set\n"
         "    says \"none\"\n"
         "  x examples/chatgpt-web-no-connectors/index.md: the leaflet says the mandate's\n"
         "    stance on read.file.project is \"wanted\", the fact set says \"refused\""),
        ("p", "That is the check being tested rather than trusted: a label number, a leaflet "
              "barrier and a fact set stance were each corrupted on purpose, and the gate named "
              "all three before the release was committed."),

        ("h2", "The same row, across nine universes"),
        ("p", "The other half of the release is smaller and it closes a loop opened two "
              "versions earlier. Every example page already ended with one capability followed "
              "through the model as a sentence, which is the fifth graph rule as an acceptance "
              "test. **That path stays inside one vocabulary.**"),
        shot(up, "v042-nine-on-example",
             "An example page ending with the same capability walked across nine universes as "
             "one sentence",
             "Every example now ends with its lead row crossed through nine worlds, built from "
             "that page's own profile, mandate and delta. The note underneath names the fact "
             "set every number on the page is a leaf assertion in.", "v0.4.2"),
        ("p", "**The two sentences are doing different work.** The first says the edges inside "
              "the model read correctly. The second says the edges between the model and eight "
              "other worlds do, including two this site does not own."),
        ("p", "[The fact sets](data/facts/index.json) &#183; "
              "[An example](examples/github-actions-hosted-runner/index.html) &#183; "
              + vlink("v0.4.2")),
    ]


# ---------------------------------------------------------------------------
# v0.4.3
# ---------------------------------------------------------------------------

def _v043(up):
    return [
        ("h2", "An argument that had been a sentence since the first release"),
        ("p", "The clearest demonstration this site has is a pair of example pages: the same "
              "coding agent, the same machine, the same account, with the confirmation prompt "
              "on in one and off in the other. **The grant does not change. The mandate does "
              "not change. The delta does not change. One barrier moves.**"),
        ("p", "For three releases that was a paragraph. A reader had to take it on trust that "
              "something in the data connected the two shapes, because nothing did: a shape "
              "carried its tools as strings and carried nothing at all about what "
              "distinguished one variant of a product from another."),
        figures.setting_path(),

        ("h2", "Three node types, and nothing typed in"),
        ("p", "This release adds a product, a tool and a setting as node types with formulas "
              "the build walks. **All three are derived from data the site already held.**"),
        ("table", ["Type", "Where it comes from", "Matched"], [
            ["`Product`", "the two segments of a shape id that are not the variant, so two "
             "shapes with the same product are the same thing in a different setting", "8"],
            ["`Tool`", "the tools a profile already listed, in the vendor's own words, one "
             "node per shape because what `shell (Bash)` reaches depends on where it runs",
             "17"],
            ["`Setting`", "twenty from the reductions the capability map publishes per "
             "capability, and one from diffing the grants of two variants of one product",
             "21"],
        ]),
        shot(up, "v043-u2-types",
             "The deployment shape universe page listing its node types, which exist and "
             "which are still needed",
             "The universe page reports its own state: three types now walked on every build "
             "with their counts, and four the world still needs. A status of partial is a "
             "claim the gate checks rather than a hedge.", "v0.4.3"),

        ("h2", "The setting nobody wrote"),
        ("p", "The interesting node of the three is the last one. **The setting that "
              "distinguishes confirmations on from confirmations off was not authored.** The "
              "build takes the two variants of one product, diffs their grants, and whatever "
              "barrier moved between them is what the setting moves."),
        ("p", "For this pair exactly one capability moves: `execute.process.host` sits at a "
              "setting in one variant and at nothing in the other. So the node carries one "
              "`narrows` edge to that capability and two `moves` edges, one to each barrier. "
              "**The home page's paragraph is now a path with two nodes and two edges in it**, "
              "walked on every build, and it would fail the build if it stopped being true."),
        shot(up, "v043-setting-node",
             "A capability page showing the published reduction that would move it to the "
             "fourth barrier, now also a node",
             "The other twenty settings come from the capability map's published reductions: "
             "for each capability, the specific configuration that narrows it, what it costs, "
             "and the barrier it reaches afterwards. This is a published reduction, not a "
             "recommendation, because whether it is worth doing depends on assets this "
             "document does not hold.", "v0.4.3"),

        ("h2", "Whose material, declared without being guessed"),
        ("p", "The other half of the release answers the first of three requests a consumer of "
              "this data published against this site. **Reach answers how far a capability "
              "goes. It does not answer whose material it touches.**"),
        ("p", "`read.message.tenant` says the agent can read a mailbox. It does not say the "
              "mailbox is full of other people's correspondence, and no setting any of the "
              "four vendors documents makes a mailbox anything else."),
        ("table", ["Value", "What it means"], [
            ["`own`", "the deployer's own material"],
            ["`organisation`", "the deployer's organisation's material"],
            ["`third_party`", "other people's material"],
            ["`mixed`", "other people's material mixed with the deployer's, and no setting the "
             "vendor documents makes it otherwise"],
        ]),
        ("note", "**A property on a granted row, never a fourth element of the grammar.** A "
                 "fourth element multiplies the primitives and the vocabulary has to stay "
                 "readable by address. And the nine shapes promoted from the capability map do "
                 "not state it, so their rows say nothing rather than guessing: the field is "
                 "null and the gate refuses any value outside the four. The first rows to carry "
                 "a value arrived in the next release, from somebody who had read the vendor "
                 "pages and written it down."),
        ("p", "**A grant you hold over other people's material is not a grant you may pass "
              "on.** That sentence is in the foundation document and it had nowhere to live in "
              "the data until this release."),
        ("p", "[The deployment shape universe](model/universes/u2/index.html) &#183; "
              "[The capability grammar](model/capabilities/index.html) &#183; "
              + vlink("v0.4.3")),
    ]


# ---------------------------------------------------------------------------
# v0.4.4
# ---------------------------------------------------------------------------

def _v044(up):
    return [
        ("h2", "Somebody else did the work first"),
        ("p", "A commercial site that renders against this site's data had, by the middle of "
              "September, built seven deployment shapes this site did not hold: two Gmail "
              "scopes, a Drive scope, a Microsoft 365 connector, a Dropbox server, the Google "
              "Workspace servers, and a self-hosted automation platform measured on a live "
              "instance by an early user's agent."),
        ("p", "It had also published a request asking this site to carry them, and marked that "
              "request as the one that unblocks a product. **Under the three layers the answer "
              "is not a favour, it is the architecture:** a deployment shape is a layer one "
              "fact, owned by nobody, and it belongs at the address every consumer reads "
              "rather than inside one consumer's vaults."),
        figures.intake_path(),

        ("h2", "The bytes are held, not copied"),
        ("p", "Twenty one files were fetched on 20 September from the contributor's public "
              "endpoint: a grant, a mandate and a vault record per shape. **They sit under "
              "`data/contributed/riskmandate/` exactly as they arrived**, with a hash per file "
              "and a hash over all of them, and both the build and the gate recompute the lot "
              "and refuse to proceed if a byte moved."),
        ("p", "Each promoted profile then pins the hash of the one file it came from. So a "
              "byte that changes after the fetch fails the build in three places at once, "
              "which is the check being tested rather than trusted:"),
        ("pre",
         "$ printf '\\n' >> data/contributed/riskmandate/dropbox-mcp/grant.json\n"
         "$ node admin/build/validate.js\n"
         "validate: 3 error(s)\n"
         "  x data/contributed/riskmandate/dropbox-mcp/grant.json hashes to 01884076f1c4...,\n"
         "    the manifest says 90b9428222dc... -- the contributed bytes were edited\n"
         "    after the fetch\n"
         "  x data/contributed/riskmandate hashes to sha256:a059adc85761fd5..., its\n"
         "    manifest says sha256:70d1a4609d27f69...\n"
         "  x data/profiles/dropbox/mcp-server/default.json: pins sha256:90b9428222dc4a2...,\n"
         "    the contributed file hashes to sha256:01884076f1c4ae2..."),

        ("h2", "What travels with a contributed shape"),
        ("p", "Promotion renames nothing and drops nothing. Every capability id has to be one "
              "of the twenty three, `is_bounded` is recomputed from the barrier and the undo "
              "class comes from the grammar. **Everything else the contributor wrote travels "
              "whole**, including three things this site had no field for."),
        ("table", ["What the contributor carries", "Why it is kept"], [
            ["Their own provenance block",
             "the vendor pages read and quoted on a date, or a dated probe of an instance they "
             "were entitled to run. This site did not observe any of it"],
            ["`contradictions`",
             "where a product's advertised capability and its granted scope disagree, both "
             "quoted, both dated, published unresolved. That is the finding"],
            ["`research_needed`",
             "the questions a vendor page could not settle. A named absence beats a hidden one"],
            ["`not_in_grammar`",
             "what the shape can do that no primitive covers. A row that needs a new verb, "
             "object class or reach is a proposal to the grammar and needs a probe, so it is "
             "recorded rather than forced into a primitive that nearly fits"],
        ]),

        ("h2", "The counts stay apart"),
        ("p", "The site went from nine shapes to sixteen and from eight starting mandates to "
              "fifteen in one release. **The rows do not merge.**"),
        figures.shapes_split(),
        shot(up, "v044-provenance-split",
             "A provenance note stating the map's measured ratio and, beside it, the "
             "contributed rows with their own ratio and hash",
             "The map's twenty one of ninety nine stays the headline on every page that "
             "carries rows from every shape. A second sentence beside it says how many rows "
             "were contributed, how many sit at the contributor's measured tier, and where the "
             "bytes are.", "v0.4.4"),
        ("note", "**The tier is the contributor's and this site did not raise it.** Eleven of "
                 "the thirty seven contributed rows are at a measured tier, from a dated probe "
                 "of an instance an early user was entitled to run, with the write up held by "
                 "the contributor as the evidence file. The rest were read from vendor "
                 "documentation on a date and quoted. Nothing here was probed by this site, and "
                 "the two sets are counted beside each other because they were obtained "
                 "differently."),

        ("h2", "The first rows that say whose material"),
        ("p", "The property declared one release earlier had no values in it. The contributed "
              "shapes arrived with thirty seven rows that state one, and the mailbox and drive "
              "shapes are where the value earns its place."),
        shot(up, "v044-capability-rows",
             "One capability across fifteen of sixteen deployment shapes, each row with its "
             "barrier, evidence tier, whose material it reaches and a quoted note",
             "One query, not a map: this capability across every shape that has it, with the "
             "contributed ones marked as contributed. The material column is mostly mixed, and "
             "mixed is the value that cannot be made own by any setting any of these vendors "
             "documents.", "v0.4.4"),

        ("h2", "A scope is not a tool"),
        ("p", "One node type arrived with the connector shapes. A coding agent reaches a "
              "capability through a tool it runs. **A connector reaches one through a scope a "
              "person consented to once**, in the vendor's own identifier, and the two are not "
              "the same kind of thing."),
        ("p", "So `gmail.readonly` is a node in the vendor's word, never translated, joined to "
              "the shape by `scoped_by` and to what it reaches by `permits`. Nine of them "
              "matched at this release."),

        ("h2", "What this release deliberately does not do"),
        ("ul", [
            "**It does not import the contributor's nine vaults for this site's own shapes.** "
            "Those pin this site, and importing them would be a loop.",
            "**It gives the contributed shapes no example page.** Their ABPs exist as data, "
            "and the contributor renders each one live from its own vault. This site links to "
            "those by address rather than rebuilding them.",
            "**It does not raise anybody's evidence tier.** A row measured by a consumer's "
            "user is that user's observation, and this site holds the claim rather than "
            "restating it as its own.",
        ]),
        shot(up, "v044-contributed",
             "The data page section describing the contributed shapes, the intake path and "
             "the tier note",
             "The intake path is the same for anybody: a profile file and a mandate at an "
             "address the proposer publishes, held here as the bytes fetched with their hash, "
             "promoted without renaming, and every id inside the grammar.", "v0.4.4"),
        shot(up, "v044-home-hero",
             "The home page of abp.sgit.ai at v0.4.4",
             "The same argument, four releases and one contributed intake later. The heading "
             "has not changed since v0.1.0, which is the point: the releases added evidence "
             "and mechanism underneath a claim that stayed still.", "v0.4.4"),
        ("p", "[The data layer](data/index.html) &#183; "
              "[The contributed manifest](data/contributed/riskmandate/manifest.json) &#183; "
              "[The deployment shape universe](model/universes/u2/index.html) &#183; "
              + vlink("v0.4.4")),
    ]


BODIES = {
    "an-ontology-that-already-existed": _v010,
    "a-rule-corrected-nine-hours-later": _v020,
    "three-nodes-and-three-edges": _v030,
    "an-abp-is-a-junction-object": _v040,
    "nine-universes-as-data": _v041,
    "the-fact-diff-reads-the-published-page": _v042,
    "the-confirmations-flag-as-a-path": _v043,
    "seven-shapes-somebody-else-measured": _v044,
}


# ---------------------------------------------------------------------------
# v0.5.0
# ---------------------------------------------------------------------------

def _v050(up):
    return [
        ("h2", "A release record is not an explanation"),
        ("p", "This site has had a version surface since its first release. Every version has "
              "a title that is a sentence rather than a label, a summary, a list of what "
              "moved and a list of what it was built against. **It is deliberately terse, and "
              "it explains nothing.**"),
        ("p", "That is the right shape for a record and the wrong shape for a reader who wants "
              "to know why a decision was made, what it cost, or what it failed to settle. "
              "This release adds the section you are reading: one article per release, and "
              "the article is the release."),
        shot(up, "v050-articles-index",
             "The articles index with a four panel chart of pages, nodes, edges and gate "
             "checks across eight releases",
             "The index opens with the four measures across the releases. It is small "
             "multiples rather than one chart with two y axes, because the four numbers have "
             "different scales and a single axis carrying two of them would say something "
             "untrue about both.", "v0.5.0"),

        ("h2", "The rule that makes the figures worth having"),
        ("p", "**Every screenshot in an article was captured from the tag that article names**, "
              "not from the site as it stands today. For each release tag a detached worktree "
              "produced a checkout of that exact commit, a static server served it, and a "
              "headless browser captured the named section of the named page."),
        shot(up, "v050-shot-caption",
             "An article showing the v0.1.0 home page, with a caption naming the version and "
             "the capture date",
             "The first release's home page, inside an article written nine days later. The "
             "version badge in the captured chrome reads v0.1.0, which is the whole point: the "
             "figure is evidence of what the site said, not an illustration of what it says "
             "now.", "v0.5.0"),
        ("note", "**A screenshot of today's page illustrating a claim about a fortnight ago is "
                 "a small lie, and it is the kind nobody catches**, because the page looks "
                 "right and the claim sounds right. The tags are in the repository and the "
                 "method is four commands, so the figures are reproducible rather than "
                 "trusted. Every caption carries the version, the capture date and the word "
                 "unretouched."),

        ("h2", "What a diagram is for, and what it is not for"),
        ("p", "A screenshot shows what a reader would have seen. **A diagram shows a mechanism "
              "no screenshot can**: an edge, a formula, a loop, a thing that does not happen. "
              "Ten figures were written for this release, and the rule applied to each was "
              "that a figure which only repeats the sentence beside it does not get made."),
        shot(up, "v050-article-diagram",
             "An article section with a two column diagram contrasting a hierarchy with a "
             "fractal zoom",
             "The zoom test as a figure. The left column is one vocabulary all the way down "
             "and the right is a new ontology at every step joined by a named edge, which is a "
             "distinction that survives being drawn and does not survive being described in a "
             "sentence.", "v0.5.0"),
        ("p", "**Each diagram carries a described equivalent for the markdown twin**, in the "
              "same form the grant-against-mandate figure has used since v0.1.0. A reader of "
              "the twin gets the figure's content in words rather than being sent to the page "
              "to find out what the picture said."),

        ("h2", "The chart had to be argued with before it could be drawn"),
        ("p", "The four measures on the index are pages, nodes, edges and checks in the "
              "release gate. They span 10 to 993, so the temptation is one chart with two y "
              "axes, and that is the single most common way a chart lies."),
        ("table", ["The decision", "Why"], [
            ["Small multiples, one series per panel",
             "four scales, four panels, each with its own axis. No panel implies a comparison "
             "the numbers do not support"],
            ["No label on the top gridline",
             "it sits at the maximum, the maximum is the last value in every panel, and the "
             "last value is already labelled at the dot. The same number twice is a "
             "reconciliation the reader does for nothing"],
            ["A dashed run before v0.3.0 on two panels",
             "there was no graph before that release. Plotting zero would claim the graph "
             "existed and was empty, which is a different and untrue statement"],
            ["The two colours were validated, not chosen",
             "the house teal failed the chroma floor and reads as grey. It was snapped to the "
             "nearest step that passes the lightness band, the chroma floor, colour vision "
             "separation, the normal vision floor and contrast against both surfaces"],
            ["No text inside a bar fill",
             "white on either segment is under contrast for small text, and an interior "
             "segment has no free end to put a label beside. The legend carries the values"],
        ]),

        ("h2", "The gate caught two things in this release's own work"),
        ("p", "The articles are held to every rule the rest of the site is: no score, no "
              "adjective about a named product, pure ASCII, the same forbidden words. Writing "
              "them tripped the gate twice."),
        ("pre", "$ node admin/build/validate.js\n"
                "validate: 4 error(s)\n"
                "  x figtest.html: no canonical link\n"
                "  x figtest.md is a page in the tree and is not listed in llms.txt\n"
                "  x admin/build/figures.py:515: non-ASCII \"a\" (U+430) outside the declared\n"
                "    glyph set"),
        ("p", "A scratch file used to preview a figure had been copied into the repository, "
              "and a Cyrillic character had reached a diagram through a careless edit. Neither "
              "is interesting on its own. **What is interesting is that a site about what a "
              "control is could not publish a page that broke its own rules**, which is the "
              "only honest demonstration of a control there is."),

        ("h2", "What this release does not do"),
        ("ul", [
            "**It does not restate the model.** Where an article describes a rule it links to "
            "the page that owns it, and where the two disagree the model page is right and "
            "the article needs correcting.",
            "**It adds no data and no formula.** The chart counts what the tags already held; "
            "the articles explain releases that had already shipped.",
            "**It does not make the site's argument twice.** An article is about a release, "
            "not about the Agent Behaviour Policy. The argument lives on the model pages.",
        ]),
        ("p", "[One article per release](articles/index.html) &#183; "
              "[The version surface](versions/index.html) &#183; " + vlink("v0.5.0")),
    ]

BODIES["one-article-per-release"] = _v050
