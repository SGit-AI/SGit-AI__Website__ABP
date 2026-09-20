#!/usr/bin/env python3
"""The universes as pages: one query, the walk of one row, and one page per universe.

NEVER RENDER THE WHOLE GRAPH. The universes page is not a map of everything. It renders the
result of one query: follow one capability row in one deployment shape through every world
it crosses, and read what it is standing on in each. The thirteen universes are listed
underneath as the places that walk visits or names, and each has a page of its own that
renders ONE universe's ontology: its owner, its node types with the counts of the ones that
exist, its verbs, and the edges that leave it.

EVERYTHING HERE COMES FROM data/universes/, which the build writes from `universes.py` and
walks from the published data. The pages quote nothing; a number on them is a number in a
file.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shell  # noqa: E402
import universes as U  # noqa: E402

LEVEL_WORD = {"down": "down", "across": "across", "up": "up", "beside": "beside"}
STATUS_WORD = {
    "live": "**live**", "partial": "partial", "one-edge": "one edge deep",
    "outside": "outside: another site's", "gap": "a gap, named",
}


def href(uid):
    return f"model/universes/{uid}/index.html"


def _crumb(tail):
    return ("crumb", "[Home](index.html) / [The model](model/index.html) / "
                     "[The universes](model/universes/index.html) / " + tail)


def pages(D, g, cls):
    recs = U.records(cls)
    cross = [e for e in U.crossings() if e["crosses"]]
    walk = U.walk(D, g)
    out = {"model/universes/index.html": _index(recs, cross, walk, D)}
    for u in recs:
        out[href(u["id"])] = _universe(u, cross, recs)
    return out


def _index(recs, cross, walk, D):
    by = {u["id"]: u for u in recs}
    walk_rows = [[f"**{by[r['universe']]['n']}**",
                  f"[{by[r['universe']]['name']}]({href(r['universe'])})",
                  by[r["universe"]]["level"],
                  r["node"], r["edge_leaving"]] for r in walk["rows"]]
    universe_rows = [[str(u["n"]), f"[{u['name']}]({href(u['id'])})", u["level"],
                      shell.ascii_safe(u["owner"]), STATUS_WORD[u["status"]],
                      f"{u['node_types_today'] if 'node_types_today' in u else sum(1 for t in u['node_types'] if t['exists_today'])} of {len(u['node_types'])}",
                      str(len(u["verbs"]))] for u in recs]
    junction_rows = [[f"`{e['edge']}`", f"`{e['inverse']}`",
                      f"[{by[e['domain_universe']]['name']}]({href(e['domain_universe'])})",
                      f"[{by[e['range_universe']]['name']}]({href(e['range_universe'])})",
                      "this site", "live"] for e in cross]
    return {
        "title": "The universes",
        "description": "The ABP mapped onto Fractal Semantic Graphs: one capability row walked "
                       "through nine universes, from the source bytes to a licence condition, "
                       "each with its own owner and ontology, joined by named edges. Four more "
                       "named as gaps.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The universes"),
            ("h1", "The universes"),
            ("lead", "An ABP is a junction object. Its four objects are owned by four different "
                     "parties who speak four vocabularies, and one capability row in one "
                     "deployment shape is a path through all of them and beyond: from the bytes "
                     "a primitive was promoted from to the licence condition somebody will sign. "
                     "**Each world on that path is a universe**: it has its own owner, its own "
                     "node types and its own verbs, it is joined to its neighbours by named "
                     "edges, and it shares nothing with them except the grammar. That is what "
                     f"[Fractal Semantic Graphs]({U.FSG_PAGE}) means, applied to this document."),
            ("note", "**This page renders one query, not a map.** The third graph rule says "
                     "never render the whole graph, render the result of a query. The query "
                     "here is: follow one row through every world it crosses, and read what it "
                     "is standing on in each. Every cell below is built from the published data "
                     "on every build, so the walk cannot drift from the rows it is made of. "
                     f"[The brief that draws the map](docs/briefs/{U.BRIEF}/index.html)."),
            ("h2", "Three words, settled"),
            ("table", ["Word", "On this site"], [
                ["**Universe**", "A world with its own owner, its own node types and its own "
                                 "verbs, joined to its neighbours by named edges. The word is the "
                                 "Fractal Semantic Graphs page's own: *on one of those links you "
                                 "can jump into another universe*."],
                ["**Level**", "Position on the ladder, and only that: down towards the byte, up "
                              "towards the estate of agents, across for the worlds the four "
                              "objects open into, beside for the worlds that attach from outside. "
                              "**Levels run up and down. Universes run across.** The four objects "
                              "are neighbours and never a stack."],
                ["**Altitude**", "A rendering of the same facts for a different reader, as ruled "
                                 "on 20 August. It lives inside the projections universe and it is "
                                 "never a different world."],
            ]),
            ("h2", "One row, nine universes"),
            ("p", f"The row is `{walk['capability']}` in the shape `{walk['profile']}`, which is "
                  f"the shape this site is built from, against the mandate `{walk['mandate']}`. "
                  f"It was chosen because it is excess and bounded, so the path reaches a "
                  f"prohibition that is enforced today and a licence condition with an enforcer "
                  f"beside it."),
            ("table", ["", "Universe", "Level", "The node the walk is standing on",
                       "The edge that leaves it"], walk_rows),
            ("h3", "Read as one sentence"),
            ("note", shell.ascii_safe(walk["sentence"][0].upper() + walk["sentence"][1:])),
            ("p", "That is the fifth graph rule applied across nine vocabularies rather than "
                  "within one: every clause is a node this site holds or an edge somebody has "
                  "declared, and if the sentence stops reading as one, the edges are wrong and "
                  "the model changes rather than the renderer."),
            ("h2", "The thirteen universes"),
            ("p", "Nine the walk crosses and four it names. **A status is a claim the gate "
                  "checks**: live means the node types exist in the graph today; partial means "
                  "some do; one edge deep means an edge reaches into the world and finds no "
                  "vocabulary yet; outside means another site owns it and this one holds only "
                  "the anchor nodes its edges point at; a gap is named so the next release has "
                  "an address to write to, and nothing is behind the name."),
            ("table", ["", "Universe", "Level", "Owner", "Status", "Node types today", "Verbs"],
             universe_rows),
            ("h2", "The edges that cross a boundary today"),
            ("p", "**Computed, not declared.** An edge's universes are those of its domain and "
                  "range types, so this table cannot disagree with [the edge vocabulary]"
                  "(model/graph/edges/index.html). The brief names twenty two junctions in all; "
                  "these are the ones the graph holds today. There is no `relates_to` among "
                  "them and there will not be one."),
            ("table", ["Edge", "Inverse", "From", "To", "Owned by", "Status"], junction_rows),
            ("h2", "What must not change"),
            ("ul", [
                "**No score, anywhere.** A score is a node in the licence and acceptance "
                "universe and there is no edge to it from this site. The map makes that "
                "boundary an edge somebody else draws rather than a sentence this site keeps "
                "repeating.",
                "**The delta is derived and never authored.** The derivation universe has no "
                "authored field.",
                "**Every prohibition carries its barrier.** The projections universe renders "
                "nothing without an edge into the enforcement universe.",
                "**Nothing is merged.** Thirteen vocabularies, one grammar, and a scope per "
                f"universe in the lexicon, held the way [graphs.sgit.ai]({U.GRAPHS_LEXICON}) "
                "holds its own.",
                "**The grammar stays small.** It gains one property and no primitive.",
            ]),
            ("p", "[The universes as JSON](data/universes/index.json) · "
                  f"[The brief](docs/briefs/{U.BRIEF}/index.html) · "
                  "[The three layers](model/graph/layers/index.html) · "
                  f"[The definition, on sgit.ai]({U.FSG_PAGE})"),
        ],
    }


def _universe(u, cross, recs):
    by = {x["id"]: x for x in recs}
    type_rows = []
    for t in u["node_types"]:
        exists = ("**yes**" + (f", {t['matched']} matched" if t.get("matched") is not None else "")
                  if t["exists_today"] else "not yet")
        type_rows.append([f"**{t['name']}**", f"`{shell.ascii_safe(t['formula'])}`", exists,
                          shell.ascii_safe(t["note"] or "")])
    verb_rows = [[f"`{v['edge']}`", shell.ascii_safe(v["reads_as"]), f"`{v['inverse']}`",
                  shell.ascii_safe(v["inverse_reads_as"]), f"`{v['domain']}`", f"`{v['range']}`",
                  shell.ascii_safe(v["from"]), v["status"]] for v in u["verbs"]]
    leaving = [[f"`{e['edge']}`", f"[{by[e['range_universe']]['name']}]({href(e['range_universe'])})"]
               for e in cross if e["domain_universe"] == u["id"]]
    arriving = [[f"`{e['edge']}`", f"[{by[e['domain_universe']]['name']}]({href(e['domain_universe'])})"]
                for e in cross if e["range_universe"] == u["id"]]
    n_prev = by.get(f"u{u['n'] - 1}")
    n_next = by.get(f"u{u['n'] + 1}")
    blocks = [
        _crumb(u["name"]),
        ("h1", f"U{u['n']}: {u['name']}"),
        ("lead", f"**Owner** {shell.ascii_safe(u['owner'])}. **Centre of gravity** "
                 f"{shell.ascii_safe(u['centre'])}. **Smallest node** "
                 f"{shell.ascii_safe(u['smallest'])}. **Level** {u['level']}. "
                 f"**Status** {STATUS_WORD[u['status']]}."),
        ("note", shell.ascii_safe(u["status_note"])),
    ]
    if type_rows:
        blocks += [("h2", "Node types"),
                   ("p", "A node type is a required pattern of paths, not a label. The ones "
                         "marked yes are walked on every build and the count is what matched; "
                         "the rest are the vocabulary this universe needs and does not have."),
                   ("table", ["Type", "Formula", "Exists today", "Note"], type_rows)]
    else:
        blocks += [("h2", "Node types"),
                   ("note", "**None yet, on purpose.** This universe is named so that its owner "
                            "has an address to attach to. Its node types are theirs to write.")]
    blocks += [("h2", "Verbs"),
               ("p", "Each is a verb with a distinct inverse, a stated domain and range, and "
                     "the sentence it reads as. The ones marked live are in the edge "
                     "vocabulary today; the rest are proposed here, or declared by the universe's "
                     "owner elsewhere, and say so."),
               ("table", ["Edge", "Reads as", "Inverse", "Reads as", "Domain", "Range", "From",
                          "Status"], verb_rows)]
    if leaving or arriving:
        blocks += [("h2", "The edges that cross its boundary today")]
        if leaving:
            blocks.append(("table", ["Leaves along", "Into"], leaving))
        if arriving:
            blocks.append(("table", ["Arrives along", "From"], arriving))
    blocks += [("h2", "What the map adds here"),
               ("p", shell.ascii_safe(u["adds"])),
               ("p", " · ".join(x for x in [
                   f"[U{n_prev['n']}: {n_prev['name']}]({href(n_prev['id'])})" if n_prev else "",
                   "[All thirteen](model/universes/index.html)",
                   f"[U{n_next['n']}: {n_next['name']}]({href(n_next['id'])})" if n_next else "",
                   f"[This universe as JSON](data/universes/{u['id']}.json)",
                   f"[The brief](docs/briefs/{U.BRIEF}/index.html)"] if x))]
    return {
        "title": f"U{u['n']}: {u['name']}",
        "description": f"{u['name']}, one of the universes an ABP row crosses: owned by "
                       f"{shell.ascii_safe(u['owner'])}, with its own node types and verbs, "
                       f"sharing only the grammar. Status: {u['status']}.",
        "blocks": blocks,
    }
