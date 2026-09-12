#!/usr/bin/env python3
"""The lexicon: a page per word in the grammar, and the graph pages behind them.

Every page here renders THE RESULT OF ONE QUERY against the graph in `graph.py`. There is no
map of everything, because the third rule says never render the whole graph, and a page that
tried would be unreadable well before it was complete.

  /model/lexicon/verbs/read/     the query: what does `read' appear in, and how far does it go
  /model/lexicon/reaches/host/   the query: what reaches this far, and what do the shapes say
                                 `host' MEANS
  /model/graph/formulas/         the query: which nodes match each node type formula, run now

THE REACH PAGES ARE THE ONES TO READ. A reach class is the clearest case in this model of
meaning coming from connectivity rather than from a label: `host' means the machine you are
sitting at in one shape and an ephemeral container in another, and the two shapes disagree in
public on the same page. Merging those definitions would erase the finding. They are kept
intact and the disagreement is rendered.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402
import graph  # noqa: E402
import shell  # noqa: E402

GRAPHS = graph.GRAPHS
EDGE_SET = graph.EDGE_SET
ANCHORS = graph.ANCHORS
DEPTH = graph.DEPTH

KINDS = [
    ("verbs", "Verb", "verb", "The action half of a primitive",
     "Ten verbs. A verb on its own is a word: what `read' means here is whatever the "
     "primitives under it reach, which is why this page is a query rather than a definition."),
    ("objects", "ObjectClass", "object", "What a primitive acts on",
     "Nine object classes. The same verb against a different object class is a different "
     "primitive, and a different conversation."),
    ("reaches", "ReachClass", "reach", "How far a primitive reaches",
     "Five reach classes, and the most contested nodes in the model: what `host' and `tenant' "
     "MEAN is the deployment shape's to say, not the grammar's."),
    ("families", "Family", "family", "A grouping of primitives for a reader",
     "Nine families. A family is an altitude device: it groups facts for a reader and carries "
     "none of its own."),
]
SLUG = {"verbs": "verb", "objects": "object", "reaches": "reach", "families": "family"}


def href(kind, name):
    return f"model/lexicon/{kind}/{name}/index.html"


def cap_href(cap_id):
    return f"model/capabilities/{cap_id}/index.html"


def spell(cap, D):
    """A capability id, spelled out as the three nodes it is made of. This is the one line that
    the whole of v0.3.0 exists to make possible."""
    c = D["by_id"][cap]
    return (f"[`{c['verb']}`]({href('verbs', c['verb'])})`.`"
            f"[`{c['object']}`]({href('objects', c['object'])})`.`"
            f"[`{c['reach']}`]({href('reaches', c['reach'])})")


def pages(D, g, cls):
    out = {}
    out.update(_hub(D, g, cls))
    for kind, ntype, _, _, _ in KINDS:
        for n in sorted((n for n in g["nodes"].values() if n and n["type"] == ntype),
                        key=lambda n: n["label"]):
            out[href(kind, n["label"])] = _word_page(kind, ntype, n, D, g, cls)
    out.update(_graph_pages(D, g, cls))
    return out


# ---------------------------------------------------------------------------
# one word
# ---------------------------------------------------------------------------

def _word_page(kind, ntype, n, D, g, cls):
    name = n["label"]
    verb = {"verbs": "verb_of", "objects": "acted_on_by",
            "reaches": "reachable_from", "families": "family_of"}[kind]
    # The query: which capabilities point at this node.
    caps = sorted(e["from"].split("/", 1)[1]
                  for e in graph.in_edges(g, n["id"], {"verb_of": "has_verb",
                                                       "acted_on_by": "acts_on",
                                                       "reachable_from": "reaches",
                                                       "family_of": "in_family"}[verb]))
    rows = []
    for cap in caps:
        c = D["by_id"][cap]
        holders = [p for p in D["profiles"].values()
                   if any(r["capability"] == cap for r in p["grant"])]
        rows.append([f"[`{cap}`]({cap_href(cap)})", c["gloss"], spell(cap, D),
                     c["undo"], f"{len(holders)} of {len(D['profiles'])}"])

    blocks = [
        ("crumb", f"[Home](index.html) / [The model](model/index.html) / "
                  f"[The lexicon](model/lexicon/index.html) / {name}"),
        ("h1", f"`{name}`"),
        ("lead", n.get("gloss") or f"The {SLUG[kind]} `{name}`, and every primitive it appears "
                                   f"in. **This page is a query, not a definition.**"),
        ("note", f"**A node carries no inherent meaning.** What `{name}` means here emerges from the "
                 f"edges traceable from it, and confidence in that meaning is proportional to "
                 f"how richly it is connected. It is connected to **{len(caps)} of "
                 f"{D['capabilities']['count']} primitives** here. That, and not the sentence "
                 f"above, is what it means. [The discipline this follows]({GRAPHS})."),
    ]

    if kind == "reaches":
        blocks += _reach_disagreement(name, n, D)

    blocks += [
        ("note", f"**No capability primitive uses `{name}`, so in this graph it means "
                 f"nothing yet.** A node connected to nothing is literally meaningless, and "
                 f"the honest thing is to say so rather than to drop the word or to write it a "
                 f"definition that no edge supports. It is in the published grammar; a "
                 f"primitive using it would need a probe before it could be added. **This is a "
                 f"finding about the vocabulary rather than a defect in it.**")
        if not caps else ("p", ""),
        ("h2", f"The {len(caps)} primitives with this {SLUG[kind]}"),
        ("table", ["Primitive", "Published gloss", "Spelled out", "Undo", "In how many shapes"],
         rows) if rows else ("p", "None. The table below is what this node connects to, and it "
                                  "is empty, which is the whole of what can honestly be said."),
        ("h2", "How this node connects"),
        ("table", ["Edge", "Reads as", "To"],
         _edge_rows(kind, name, len(caps))),
        ("p", f"[This node as JSON](data/lexicon/{kind}/{name}.json) · "
              f"[The lexicon](model/lexicon/index.html) · "
              f"[The edge vocabulary](model/graph/edges/index.html)"),
    ]
    return {
        "title": f"{name} ({SLUG[kind]})",
        "description": f"The {SLUG[kind]} `{name}` as a node: the {len(caps)} capability "
                       f"primitives it appears in, what they reach, and how it connects. "
                       f"Meaning from connectivity, not from a definition.",
        "blocks": blocks,
    }


def _edge_rows(kind, name, n):
    inv = {"verbs": ("verb_of", "has_verb"), "objects": ("acted_on_by", "acts_on"),
           "reaches": ("reachable_from", "reaches"), "families": ("family_of", "in_family")}[kind]
    return [
        [f"`{inv[0]}`", f"`{name}` is the {SLUG[kind].replace('object', 'object class')} of "
                        f"these {n} primitives", f"{n} capabilities"],
        [f"`{inv[1]}`", f"the inverse, walked the other way, with different fan out",
         "one capability at a time"],
    ]


def _reach_disagreement(name, n, D):
    """What the shapes say this reach class MEANS, kept intact rather than merged.

    Merging is a destructive operation and what it destroys is the finding. So the definitions
    are not folded into one: they are listed, each owned by the shape that said it, and the
    disagreement is the content of the page."""
    said = []
    for pid, p in sorted(D["profiles"].items()):
        m = (p.get("reach_names") or {}).get(name)
        if m:
            said.append([f"[{shell.ascii_safe(p['product'])}](examples/index.html)",
                         f"`{p['variant']}`", shell.ascii_safe(m)])
    if not said:
        return []
    return [
        ("h2", f"What the shapes say `{name}` means, and they do not agree"),
        ("note", "**These definitions are not merged, and that is the design.** Merging two "
                 "vocabularies erases the disagreement, and the disagreement is the finding. "
                 f"Each row below is owned by the shape that said it. A reader deciding what "
                 f"`{name}` costs them has to read the row for the shape they run, not an "
                 f"average of the rows. [Why vocabularies are bridged rather than "
                 f"merged]({DEPTH})."),
        ("table", ["The shape", "Variant", f"What `{name}` means there"], said),
        ("p", f"**That is the ABP's own argument in one column.** The same word, the same "
              f"grammar, and a materially different exposure depending on where the agent "
              f"runs. It is why an ABP is about the deployment rather than the product."),
    ]


# ---------------------------------------------------------------------------
# the hub
# ---------------------------------------------------------------------------

def _hub(D, g, cls):
    cards = []
    for kind, ntype, _, heading, blurb in KINDS:
        names = sorted(n["label"] for n in g["nodes"].values() if n and n["type"] == ntype)
        cards.append({"title": f"[{heading}](model/lexicon/index.html#{kind})",
                      "sub": blurb,
                      "foot": " · ".join(f"[`{x}`]({href(kind, x)})" for x in names)})
    example = D["by_id"]["read.record.browsing"]
    return {"model/lexicon/index.html": {
        "title": "The lexicon",
        "description": "Every word in the capability grammar as a node with its own address, "
                       "its own JSON and its own page: ten verbs, nine object classes, five "
                       "reach classes and nine families.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / The lexicon"),
            ("h1", "The lexicon"),
            ("lead", "**`read.file.project` is not a string.** It is three nodes and three "
                     "edges, and each of those nodes has an address, a JSON file and a page of "
                     "its own. This is where they are."),
            ("h2", "What changed, and why it mattered"),
            ("note", "**Until v0.3.0 this site attached the meaning to the node.** A primitive "
                     "was an identifier with a gloss beside it, and the gloss was the "
                     "definition. That is schema-first thinking dressed in graph syntax: a "
                     "self-describing node has smuggled the schema back in. Now the gloss is "
                     "still there and it is no longer the definition. **What a primitive means "
                     "is what its edges reach.**"),
            ("h3", "One primitive, spelled out"),
            ("table", ["", "Node", "Edge", "Reads as"], [
                ["", f"[`read.record.browsing`]({cap_href('read.record.browsing')})", "",
                 f"*{example['gloss']}*"],
                ["", f"[`{example['verb']}`]({href('verbs', example['verb'])})", "`has_verb`",
                 f"this capability has the verb `{example['verb']}`"],
                ["", f"[`{example['object']}`]({href('objects', example['object'])})",
                 "`acts_on`", f"this capability acts on `{example['object']}`"],
                ["", f"[`{example['reach']}`]({href('reaches', example['reach'])})", "`reaches`",
                 f"this capability reaches `{example['reach']}`"],
                ["", f"[`{example['family']}`]({href('families', example['family'])})",
                 "`in_family`", f"this capability is in the `{example['family']}` family"],
                ["", f"[`{example['undo']}`](model/undo/index.html)", "`has_undo_class`",
                 f"this capability has the undo class `{example['undo']}`"],
            ]),
            ("p", "**Each of those is a link because each of those is a node.** Follow "
                  f"[`{example['reach']}`]({href('reaches', example['reach'])}) and you get "
                  f"every primitive that reaches that far and, more usefully, what each "
                  f"deployment shape says that reach class actually means. They do not agree, "
                  f"and the page keeps the disagreement rather than averaging it."),
            ("h2", "The words"),
            ("cards", cards),
            ("note", _unused_note(g)),
            ("h2", "The rest of the grammar"),
            ("table", ["Address", "What is there"], [
                [f"[The edge vocabulary](model/graph/edges/index.html)",
                 f"{len(graph.EDGES)} edges, each a verb with a distinct inverse, a stated "
                 f"domain and range, and where it came from. The generic association edge is "
                 f"banned and there is none in this model."],
                ["[The node type formulas](model/graph/formulas/index.html)",
                 f"{len(graph.NODE_TYPES)} node types, each a required pattern of paths rather "
                 f"than a label. Run against the graph on every build."],
                ["[The three layers](model/graph/layers/index.html)",
                 "How a vault extends this vocabulary for one customer without merging "
                 "anything, and without asking permission."],
                ["[The graph rules](model/graph/index.html)",
                 "The five published rules and what each forces on this model."],
            ]),
            ("p", f"[The lexicon as JSON](data/lexicon/index.json) · "
                  f"[The whole graph](data/graph/index.json) · "
                  f"[Meaning through connectivity]({GRAPHS})"),
        ]}}


# ---------------------------------------------------------------------------
# the grammar pages
# ---------------------------------------------------------------------------

def _graph_pages(D, g, cls):
    pages = {}

    reused = [e for e in graph.edge_records() if not e["from"].startswith("proposed")]
    proposed = [e for e in graph.edge_records() if e["from"].startswith("proposed")]
    pages["model/graph/edges/index.html"] = {
        "title": "The edge vocabulary",
        "description": f"The {len(graph.EDGES)} edges this model is written in, each a verb "
                       f"with a distinct inverse, a stated domain and range, and the sentence "
                       f"it reads as.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / "
                      "[The graph](model/graph/index.html) / The edges"),
            ("h1", "The edge vocabulary"),
            ("lead", f"**{len(graph.EDGES)} edges.** Every one is a verb with a distinct, "
                     f"meaningfully named inverse, and the inverse is not the same edge walked "
                     f"backwards: `grants` and `granted_by` have different fan out, and that "
                     f"asymmetry is what stops the graph exploding."),
            ("note", "**The generic association edge is banned, and there is none in this "
                     "model.** It constrains nothing and costs fan out. If you find yourself "
                     "wanting `relates_to`, the honest move is a new edge with a sentence, a "
                     "different sentence for its inverse, and a stated domain and range."),
            ("h2", f"Reused from the published set, unchanged"),
            ("p", f"These are not this site's to rename. They are published at [the network's "
                  f"edge set]({EDGE_SET}) and reused under their published names."),
            ("table", ["Edge", "Inverse", "Domain", "Range", "Reads as"],
             [[f"`{e['edge']}`", f"`{e['inverse']}`", f"`{e['domain']}`", f"`{e['range']}`",
               e["reads_as"]] for e in reused]),
            ("h2", f"Proposed here"),
            ("p", "**Each one carries a sentence, a different sentence for its inverse, and a "
                  "stated domain and range**, which is the published rule for extending the "
                  "set. They are marked as proposed here rather than quoted, in the same way "
                  "the network's own edge set marks nine of its inverses as proposed there."),
            ("table", ["Edge", "Reads as", "Inverse", "Reads as", "Domain", "Range"],
             [[f"`{e['edge']}`", e["reads_as"], f"`{e['inverse']}`", e["inverse_reads_as"],
               f"`{e['domain']}`", f"`{e['range']}`"] for e in proposed]),
            ("h2", "The sentence test"),
            ("p", "**If a path does not read as a sentence in the reader's own language, the "
                  "edges are wrong** and the model changes rather than the renderer. Every "
                  "example page ends with a path built from its own data so the test is applied "
                  "on every build rather than asserted once here:"),
            ("note", "deployment shape `claude-code local-confirmations-off` **grants** "
                     "capability `execute.process.host` which **has_verb** `execute` and "
                     "**reaches** `host`, **bounded_by** barrier `none`, which **exceeds** "
                     "mandate `a coding assistant on my machine`, and **has_undo_class** "
                     "`with-effort`."),
            ("p", f"[The edges as JSON](data/graph/edges.json) · "
                  f"[The node type formulas](model/graph/formulas/index.html)"),
        ]}

    rows = []
    for name, gloss, formula, note in graph.NODE_TYPES:
        n = len(cls.get(name, []))
        rows.append([f"**{name}**", gloss, f"`{formula}`", str(n) if name in cls else "-"])
    pages["model/graph/formulas/index.html"] = {
        "title": "The node type formulas",
        "description": "A node type is a required pattern of typed, directed paths that a node "
                       "either matches or does not. Not a label somebody applied. Run against "
                       "the graph on every build.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / "
                      "[The graph](model/graph/index.html) / The formulas"),
            ("h1", "The node type formulas"),
            ("lead", "**The content of a node does not decide its type. Its paths do.** Two "
                     "nodes with identical text can be different types because their edges "
                     "differ, and the clearest case in this model is that the same capability "
                     "is excess on one deployment and authorised on the next, with nothing "
                     "about the capability changed."),
            ("h2", "The formulas, and what matched when this page was built"),
            ("table", ["Type", "What it is", "The formula", "Matched"], rows),
            ("h2", "The one that carries the argument"),
            ("note", "**`[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the "
                     "[Grant] does not include.`** Until v0.3.0 this was `is_control: true` on "
                     "a barrier, which is a label somebody applied. It is now a path the build "
                     "walks, and **exactly one of the four barriers matches**. The release gate "
                     "fails if that stops being true, because every page on this site is "
                     "written against it."),
            ("table", ["Barrier", "Enforced by", "Inside the grant", "A control"],
             [[f"`{b['id']}`",
               (g["nodes"][graph.out_edges(g, f"barrier/{b['id']}", 'enforced_by')[0]["to"]]
                ["label"] if graph.out_edges(g, f"barrier/{b['id']}", "enforced_by") else "-"),
               ("yes" if graph.out_edges(g, f"barrier/{b['id']}", "enforced_by")
                and g["nodes"][graph.out_edges(g, f"barrier/{b['id']}", "enforced_by")[0]["to"]]
                ["inside_the_grant"] else ("-" if not graph.out_edges(g, f"barrier/{b['id']}", "enforced_by") else "no")),
               "**yes**" if f"barrier/{b['id']}" in cls["Control"] else "no"]
              for b in D["barriers"]["barriers"]]),
            ("h2", "Judgment does not disappear"),
            ("p", "That is the usual objection and it deserves a direct answer. **Somebody "
                  "still decided that a control must be enforced from outside the grant.** What "
                  "changes is where that decision lives: out of a classifier's head and into a "
                  "formula that is visible, versioned, inspectable and arguable. **You can now "
                  "disagree with a classification by pointing at a line**, which you could not "
                  "do before."),
            ("note", graph.NOT_A_NODE),
            ("p", f"[The formulas as JSON](data/graph/node-types.json) · "
                  f"[Why classification is a query]({DEPTH})"),
        ]}

    pages["model/graph/layers/index.html"] = _layers_page(D, g, cls)
    return pages


def _layers_page(D, g, cls):
    """How a vault extends this vocabulary for one customer.

    THIS IS THE PAGE THE VAULTS NEED. The published position is that ontologies are not folded
    into a single shared definition, because that erases the disagreement: they are kept intact
    and connected through anchor nodes. The construction is three layers and the separation
    between them is the whole design."""
    return {
        "title": "The three layers",
        "description": "How a customer vault extends this vocabulary without merging anything: "
                       "shared facts owned by nobody, per-party formulas, and declared bridges. "
                       "Parties can disagree about meaning while still agreeing about facts.",
        "blocks": [
            ("crumb", "[Home](index.html) / [The model](model/index.html) / "
                      "[The graph](model/graph/index.html) / The three layers"),
            ("h1", "The three layers"),
            ("lead", "**A customer will disagree with some of this vocabulary, and they will "
                     "often be right about their own estate.** The wrong response is to merge "
                     "their definitions into these, because merging is a destructive operation "
                     "and what it destroys is the finding. The right response is three layers."),

            ("h2", "Layer 1: shared facts, owned by nobody"),
            ("p", f"The factual graph, published here: **{len(cls['Capability'])} capability "
                  f"primitives**, **{len(cls['Verb'])} verbs**, **{len(cls['ObjectClass'])} "
                  f"object classes**, **{len(cls['ReachClass'])} reach classes**, "
                  f"**{len(cls['Barrier'])} barriers**, **{len(cls['DeploymentShape'])} "
                  f"deployment shapes** and what each one grants. **Nobody has to agree about "
                  f"what any of it means to agree that it is the case.**"),
            ("note", "**This layer is free, public, versioned and hash verified, and it stays "
                     "that way.** It lives at [`/data/`](data/index.html) with cross origin "
                     "access, so a vault reads it over the network rather than forking it. A "
                     "consumer pins a version, because a clone that floats against the latest "
                     "has no reproducible output."),

            ("h2", "Layer 2: per-party formulas"),
            ("p", "**Each party classifies those shared nodes with its own rules.** A node type "
                  "here is [a formula rather than a label](model/graph/formulas/index.html), "
                  "which is exactly what makes this possible: a customer does not need us to "
                  "change a field, they write their own formula over the same facts."),
            ("table", ["The formula here", "A customer's version, and why"], [
                ["`[Control] := a [Barrier] -enforced_by-> an [Enforcer] the [Grant] does not "
                 "include`",
                 "A regulated customer may require a control to be **evidenced as well as "
                 "enforced**: `... and -backed_by-> [Evidence] -observed_on-> [System]`. Their "
                 "unbounded excess is then higher than ours, on the same facts, and both "
                 "numbers are correct."],
                ["`[Excess] := a [GrantedCapability] with no -authorised_by-> path`",
                 "A customer whose mandates are written per role rather than per deployment "
                 "computes the same delta against a different mandate node. The capability rows "
                 "do not move."],
                ["The five reach classes",
                 "An estate with a hard tenancy boundary may split `tenant` into two nodes. "
                 "**They add nodes in their own vault; ours are untouched.**"],
            ]),
            ("p", "**Three different answers over one set of facts, each internally consistent, "
                  "each inspectable.** None of them requires this site to change."),

            ("h2", "Layer 3: declared bridges"),
            ("p", "**Explicit edges connecting the two vocabularies at specific points**, owned "
                  "by whoever declared them and revisable without renegotiating anything. The "
                  "edge is `similar_to`, it is symmetric, and it is partial on purpose."),
            ("note", "our [`read.record.browsing`](model/capabilities/read.record.browsing/"
                     "index.html) **similar_to** their `PII.access.browser`\n\n"
                     "Partial. Traversable. Arguable. And crucially: **a third party can add "
                     "that edge without touching either node.** You do not need our "
                     "permission, and we do not need yours. [Why anchor nodes rather than "
                     "conformance claims](" + ANCHORS + ")."),
            ("p", "**The wrong move is a conformance claim**: *we are compliant with vocabulary "
                  "X*. That is all or nothing, and it is usually a lie by the second field. "
                  "**Partial mapping is the normal case, not a defect.**"),

            ("h2", "What a vault actually holds"),
            ("p", "A customer vault is layers 2 and 3, pointing at layer 1 by address, version "
                  "and hash. It does not fork the facts."),
            ("table", ["In the vault", "Not in the vault"], [
                ["Their mandates, in their own words",
                 "The capability primitives, which are read from here"],
                ["Their formulas, including their own definition of a control",
                 "Our formulas, which are read from here"],
                ["Their bridges to our vocabulary, and to any other",
                 "Any merged vocabulary, because there is none"],
                ["Their deployment shapes, measured from their own estate",
                 "The nine published shapes, which are read from here"],
                ["Their stored deltas, derived and never authored",
                 "Anything they authored by hand into a delta"],
            ]),
            ("note", "**And the version they pinned.** Anything computing from these files "
                     "states which version it computed against, so a delta produced in the "
                     "vault in March can be recomputed in September and the difference "
                     "attributed to the right side. That is the same rule the [stored "
                     "deltas](model/delta/index.html) follow here."),

            ("h2", "Why this is one mechanism rather than two"),
            ("p", "**Customisation and consolidation are the same operation.** Do not store a "
                  "consolidated text and maintain it; hold the base plus the amendments and "
                  "compute the result. A customer's vocabulary is the base plus their "
                  "amendments, and so is ours, and so is the next customer's. There is no "
                  "special case for the customer who disagrees, which is the test of whether "
                  "the model is actually fractal: **if zooming into a node needs a new format "
                  "or a special case, the system is hierarchical rather than fractal.**"),
            ("note", "**The claim that carries this whole page.** Parties can disagree about "
                     "meaning while still agreeing about facts, **which is the only stable "
                     "basis for working together.** A customer who cannot accept our definition "
                     "of a control can still accept that their agent can read every file the "
                     "account can reach, and that is the sentence the ABP needed them to reach."),
            ("p", f"[The declared bridges as JSON](data/bridges/index.json) · "
                  f"[The lexicon](model/lexicon/index.html) · "
                  f"[Why vocabularies are bridged rather than merged]({DEPTH})"),
        ]}


def _unused_note(g):
    """The gap, on the hub, rather than only on the two pages nobody will click."""
    dead = sorted(n["label"] for n in g["nodes"].values()
                  if n and n["type"] in ("Verb", "ObjectClass", "ReachClass", "Family")
                  and not graph.in_edges(g, n["id"]))
    if not dead:
        return "**Every word in the grammar has at least one primitive under it.**"
    return (f"**{len(dead)} of these words have no primitive under them: "
            + ", ".join(f"`{d}`" for d in dead)
            + ". In this graph they mean nothing yet.** They are in the published grammar and "
              "they are kept and marked rather than dropped, because a node connected to "
              "nothing is literally meaningless and saying so is more useful than writing it a "
              "definition no edge supports. Adding a primitive that uses one would need a "
              "probe. **This is a finding about the vocabulary rather than a defect in it**, "
              "and it is the kind of gap that only becomes visible once the words are nodes.")
