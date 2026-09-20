#!/usr/bin/env python3
"""The ABP as a graph: the edge vocabulary, the node type formulas, and the lexicon.

MEANING THROUGH CONNECTIVITY. A node carries no inherent meaning. What a thing IS emerges from
the edges traceable from it, and confidence in that meaning is proportional to how richly it is
connected. Properties are just words; connections are meaning. That is the discipline published
at graphs.sgit.ai and this module is the ABP obeying it.

WHAT THIS MODULE EXISTS TO FIX. Until v0.3.0 this site treated `read.file.project` as a string
with a gloss beside it. That is a self-describing node, which is schema-first thinking dressed
in graph syntax: the meaning was attached to the node rather than derived from its edges. So
`read`, `file` and `project` are now three nodes, each with an address, a JSON file and a page,
and `read.file.project` is what you get by walking three edges from them. The gloss did not go
away; it stopped being the definition.

  [read.file.project] -has_verb->  [read]
                      -acts_on->   [file]
                      -reaches->   [project]

THE FRACTAL TEST, and it is testable rather than decorative. CORRECTED at v0.4.0 to the wording
graphs.sgit.ai took at v0.6.21: what survives every zoom is the GRAMMAR (every edge a verb with
an inverse, meaning in connectivity, supersede never delete, provenance kept), and the ONTOLOGY
is meant to change at every altitude. If zooming in lands you in the same types, the same verbs
and the same vocabulary all the way down, you have a hierarchy; if it needs a different grammar,
the claim is false; every zoom that opens a new ontology joined by a named edge to the last is
the claim working. Until v0.4.0 this docstring stated the first edition's version, one format
and one schema everywhere, which scores decomposition as fractal. By the corrected test the
graph this module builds decomposes one vocabulary very well and crosses into another in two
places (the reach class disagreement and the bridge to the game); the universes its other
edges point at are mapped in docs/briefs/ and are the work of the releases after this one.

CLASSIFICATION IS A QUERY, NOT A JUDGMENT. Until v0.3.0 a barrier carried `is_control: true`,
which is a label somebody applied. It is now a FORMULA over paths, in `node-types.json`, and the
boolean is derived from it rather than asserted:

  [Control] := a [Barrier] that -enforced_by-> something the [Grant] does not -includes->

Judgment does not disappear. Somebody still decided that a control must be enforced from
outside the grant. What changes is where that decision lives: out of the classifier's head and
into a formula that is visible, versioned, inspectable and arguable. You can now disagree with
a classification by pointing at a line.

NEVER RENDER THE WHOLE GRAPH. Every page built from this module renders the result of ONE
query: this verb's primitives, this reach class's capabilities, this shape's grant. There is no
map of everything and there will not be one.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

GRAPHS = "https://graphs.sgit.ai/"
EDGE_SET = "https://graphs.sgit.ai/v1/grammar/edge-set.html"
ANCHORS = "https://graphs.sgit.ai/v1/grammar/index.html#anchor-nodes"
DEPTH = "https://graphs.sgit.ai/v1/depth/index.html"

# ---------------------------------------------------------------------------
# the edge vocabulary
# ---------------------------------------------------------------------------
# EVERY EDGE IS A VERB WITH A DISTINCT, MEANINGFULLY NAMED INVERSE, and the inverse is not the
# same edge walked backwards: `granted_by' and `grants' have different fan out, and that
# asymmetry is what stops the graph exploding. THE GENERIC ASSOCIATION EDGE IS BANNED, because
# it constrains nothing and costs fan out: there is no `relates_to' anywhere in this model.
#
# The extension rule from the published grammar is followed exactly: a new edge needs a
# sentence, its inverse needs a DIFFERENT sentence, and both need a stated domain and range.
# Where an edge is already in the published set it is reused under its published name rather
# than renamed, and `from` records that. Where this site proposes one, it says so, in the same
# way the published edge set marks nine of its own inverses as proposed there rather than
# quoted from the corpus.
EDGES = [
    # published, reused unchanged
    ("grants", "granted_by", "DeploymentShape", "Capability",
     "this deployment shape grants this capability",
     "this capability is granted by this deployment shape",
     "graphs.sgit.ai edge set"),
    ("reaches", "reachable_from", "Capability", "ReachClass",
     "this capability reaches this reach class",
     "this reach class is reachable from this capability",
     "graphs.sgit.ai edge set"),
    ("similar_to", "similar_to", "Node", "Node",
     "our node is similar to their node",
     "symmetric, and partial on purpose",
     "graphs.sgit.ai anchor nodes"),
    ("supersedes", "superseded_by", "Node", "Node",
     "this claim supersedes that one",
     "that claim is superseded by this one",
     "graphs.sgit.ai, supersede never delete"),
    # proposed here, each with a sentence, a different inverse sentence, a domain and a range
    ("has_verb", "verb_of", "Capability", "Verb",
     "this capability has the verb read",
     "read is the verb of these capabilities",
     "proposed here"),
    ("acts_on", "acted_on_by", "Capability", "ObjectClass",
     "this capability acts on files",
     "files are acted on by these capabilities",
     "proposed here"),
    ("in_family", "family_of", "Capability", "Family",
     "this capability is in the filesystem family",
     "the filesystem family is the family of these capabilities",
     "proposed here"),
    ("has_undo_class", "undo_class_of", "Capability", "UndoClass",
     "this capability has the undo class no",
     "undo class no is the undo class of these capabilities",
     "proposed here"),
    ("bounded_by", "bounds", "GrantedCapability", "Barrier",
     "this granted capability is bounded by this barrier",
     "this barrier bounds these granted capabilities",
     "proposed here"),
    ("enforced_by", "enforces", "Barrier", "Enforcer",
     "this barrier is enforced by something above the grant",
     "this enforcer enforces these barriers",
     "proposed here"),
    ("authorises", "authorised_by", "Mandate", "Capability",
     "this mandate authorises this capability",
     "this capability is authorised by this mandate",
     "proposed here"),
    ("withholds", "withheld_by", "Mandate", "Capability",
     "this mandate withholds this capability",
     "this capability is withheld by this mandate",
     "proposed here"),
    ("exceeds", "exceeded_by", "GrantedCapability", "Mandate",
     "this granted capability exceeds this mandate",
     "this mandate is exceeded by these granted capabilities",
     "proposed here"),
    ("falls_short_of", "unmet_by", "Mandate", "Capability",
     "this mandate falls short of this capability it asked for",
     "this capability is unmet by this deployment shape",
     "proposed here"),
    ("known_by", "evidences", "GrantedCapability", "EvidenceTier",
     "this granted capability is known by observation",
     "observation evidences these granted capabilities",
     "proposed here"),
    # THE DEPLOYMENT SHAPE UNIVERSE, v0.4.3. A shape used to carry its tools as strings and
    # nothing about what distinguishes one variant of a product from another. Now the product,
    # the tool a capability is reached through, and the setting that moves a barrier are nodes,
    # so that `the confirmations flag moves one barrier and not one number` is a path rather
    # than a sentence on the home page.
    ("has_variant", "variant_of", "Product", "DeploymentShape",
     "this product has this variant",
     "this variant is a variant of this product",
     "proposed here"),
    ("runs_with", "run_by", "DeploymentShape", "Tool",
     "this shape runs with this tool",
     "this tool is run by these shapes",
     "proposed here"),
    ("exposes", "exposed_by", "Tool", "Capability",
     "this tool exposes this capability",
     "this capability is exposed by these tools",
     "graphs.sgit.ai edge set"),
    ("moves", "moved_by", "Setting", "Barrier",
     "this setting moves a capability to this barrier",
     "this barrier is where these settings move a capability to",
     "proposed here"),
    ("narrows", "narrowed_by", "Setting", "Capability",
     "this setting narrows this capability",
     "this capability is narrowed by these settings",
     "proposed here"),
    # v0.4.4: a connector shape reaches a capability through a scope in the vendor's own
    # identifier, gmail.readonly, drive.file, which is not a tool. It is kept in the
    # vendor's word and given its own node type rather than filed as a tool.
    ("scoped_by", "scopes", "DeploymentShape", "Scope",
     "this shape is scoped by this vendor scope",
     "this scope scopes these shapes",
     "proposed here"),
    ("permits", "permitted_by", "Scope", "Capability",
     "this scope permits this capability",
     "this capability is permitted by these scopes",
     "proposed here"),
]

# ---------------------------------------------------------------------------
# node type formulas
# ---------------------------------------------------------------------------
# A NODE TYPE IS A REQUIRED PATTERN OF TYPED, DIRECTED PATHS that a node either matches or does
# not. The content of the node does not decide its type; its paths do. Two nodes with identical
# text can be different types because their edges differ, and the clearest case in this model
# is that the SAME capability is an excess on one deployment and authorised on the next, with
# nothing about the capability changed.
#
# Each formula below is executable: `test` is evaluated by `classify()` against the real graph
# on every build, and the counts on the site are the result of running them rather than fields
# somebody set.
NODE_TYPES = [
    ("Verb", "The action half of a primitive, on its own.",
     "[Verb] := a node that is the -verb_of-> at least one [Capability]",
     "A verb with no capability under it is a word, not a node in this graph."),
    ("ObjectClass", "What a primitive acts on.",
     "[ObjectClass] := a node that is -acted_on_by-> at least one [Capability]", None),
    ("ReachClass", "How far a primitive reaches.",
     "[ReachClass] := a node that is -reachable_from-> at least one [Capability]",
     "What host, tenant and world MEAN is the deployment shape's to say, not the grammar's, "
     "which is why a reach class node carries the shapes that name it rather than a definition."),
    ("Family", "A grouping of primitives for a reader.",
     "[Family] := a node that is the -family_of-> at least one [Capability]",
     "A family is an altitude device: it groups facts for a reader and carries none of its own."),
    ("Capability", "A primitive in the grammar.",
     "[Capability] := a node with a -has_verb-> [Verb] and an -acts_on-> [ObjectClass] and a "
     "-reaches-> [ReachClass]",
     "All three, or it is not a primitive. A specific path, host or mailbox is an INSTANCE of a "
     "primitive and never a new one."),
    ("DeploymentShape", "A product in a setting.",
     "[DeploymentShape] := a node that -grants-> at least one [Capability]",
     "Not a product. Two shapes here are the same product with one setting different."),
    ("GrantedCapability", "A capability in a particular shape's grant.",
     "[GrantedCapability] := a [Capability] with an inbound -grants-> from a [DeploymentShape], "
     "carrying a -bounded_by-> [Barrier] and a -known_by-> [EvidenceTier]",
     "THE NODE THAT CARRIES THE BARRIER. The barrier is a property of the capability IN A "
     "SHAPE, never of the capability itself, which is the whole reason the ABP is about the "
     "deployment rather than the product."),
    ("Barrier", "What stands between the agent and a capability.",
     "[Barrier] := a node that -bounds-> at least one [GrantedCapability]", None),
    ("Control", "A barrier that actually bounds anything.",
     "[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include",
     "THE ENFORCER TEST, AS A FORMULA RATHER THAN A FIELD. Until v0.3.0 this was `is_control: "
     "true' on a barrier, which is a label somebody applied. Now it is a path pattern, so you "
     "can disagree with the classification by pointing at a line. Exactly one of the four "
     "barriers matches, and the site fails to build if that stops being true."),
    ("Mandate", "What a deployer authorised.",
     "[Mandate] := a node that -authorises-> at least one [Capability]", None),
    ("Excess", "The finding.",
     "[Excess] := a [GrantedCapability] with NO -authorised_by-> path to the [Mandate] in scope",
     "A capability the mandate never mentioned was not authorised. Unstated is not permission."),
    ("UnboundedExcess", "The business case.",
     "[UnboundedExcess] := an [Excess] whose -bounded_by-> [Barrier] is not a [Control]",
     "The only number on the label a buyer can move. Every control bought moves one capability "
     "into the fourth barrier and the count falls by one."),
    ("Shortfall", "Asked for and cannot.",
     "[Shortfall] := a [Capability] that a [Mandate] -authorises-> and no [DeploymentShape] in "
     "scope -grants->", None),
    # the deployment shape universe
    ("Product", "A vendor's product, which is not a shape.",
     "[Product] := a node that -has_variant-> at least one [DeploymentShape]",
     "The ABP is about the deployment, not the product. A product is the node two shapes "
     "share when they differ by one setting, and nothing on this site is a claim about one."),
    ("Tool", "What a shape reaches a capability through.",
     "[Tool] := a node that a [DeploymentShape] -runs_with-> and that -exposes-> at least one "
     "[Capability]",
     "In the vendor's own words: shell (Bash), the assistant's Gmail connector, REST API: "
     "workflows. A tool that exposes nothing is a name and not a node here."),
    ("Scope", "A vendor's own identifier for what a consent permits.",
     "[Scope] := a node that a [DeploymentShape] is -scoped_by-> and that -permits-> at least "
     "one [Capability]",
     "In the vendor's word, never translated: gmail.readonly is the node, and what it "
     "permits is the edge. The connector shapes contributed by riskmandate.ai reach most of "
     "their rows this way."),
    ("Setting", "What moves a barrier.",
     "[Setting] := a node that -narrows-> at least one [Capability] and -moves-> it to at "
     "least one [Barrier]",
     "Two kinds today, both from published data: the reduction the map publishes per "
     "capability, and the setting that distinguishes two variants of one product, derived by "
     "diffing their grants. The confirmations flag is the second kind."),
]

# The one thing in the model that is not a node and must not become one. Stated here because a
# reader who has understood the rest will reach for it.
NOT_A_NODE = (
    "**A score is not a node and there is no edge to one.** Not a rating, not a risk level, not "
    "a severity. Adding one would not be a modelling choice, it would be a verdict, and the "
    "same ABP is dangerous in one deployment and harmless in the next. The risk work above this "
    "holds the assets, and that is where a score can exist.")


def edge_records():
    return [{"edge": e, "inverse": i, "domain": d, "range": r,
             "reads_as": s, "inverse_reads_as": si, "from": src}
            for e, i, d, r, s, si, src in EDGES]


# ---------------------------------------------------------------------------
# building the graph
# ---------------------------------------------------------------------------

def build(D):
    """Every node and every edge, from the published data. Nothing here is typed in.

    The graph is built ONCE and every page is a query against it, which is the third rule:
    never render the whole graph, render the result of a query."""
    nodes, edges = {}, []

    def node(nid, ntype, label, **extra):
        nodes.setdefault(nid, {"id": nid, "type": ntype, "label": label, **extra})
        return nid

    def edge(src, verb, dst):
        edges.append({"from": src, "edge": verb, "to": dst})

    caps = D["capabilities"]

    # --- the lexicon: the words a primitive is spelled with -------------------
    for v in caps["verbs"]:
        node(f"verb/{v}", "Verb", v)
    for o in caps["object_classes"]:
        node(f"object/{o}", "ObjectClass", o)
    for r, gloss in caps["reaches"].items():
        node(f"reach/{r}", "ReachClass", r, gloss=gloss)
    for f, gloss in caps["families"].items():
        node(f"family/{f}", "Family", f, gloss=gloss)
    for u in D["undo"]["classes"]:
        node(f"undo/{u['id']}", "UndoClass", u["id"], gloss=u["published_meaning"])
    for t in D["evidence"]["tiers"]:
        node(f"evidence/{t['id']}", "EvidenceTier", t["id"], gloss=t["published_meaning"])

    # --- the barriers, and the enforcer they do or do not have ---------------
    # The enforcer is what makes the Control formula executable. Three of the four barriers
    # are enforced by something INSIDE the grant, which is why they bound nothing.
    ENFORCER = {
        "none": (None, "Nothing enforces it."),
        "expectation": ("enforcer/the-agent-reading-it",
                        "A rule in prose is enforced by the thing it is addressed to."),
        "setting": ("enforcer/the-agents-own-account",
                    "A setting the agent's own account could change is enforced by that "
                    "account, which the grant includes."),
        "boundary": ("enforcer/above-the-grant",
                     "A sandbox, a gateway, a tool that is not exposed, a network it cannot "
                     "see: enforced by something the grant does not include."),
    }
    node("enforcer/the-agent-reading-it", "Enforcer", "the agent reading it",
         inside_the_grant=True)
    node("enforcer/the-agents-own-account", "Enforcer", "the agent's own account",
         inside_the_grant=True)
    node("enforcer/above-the-grant", "Enforcer", "something above the grant",
         inside_the_grant=False)
    for b in D["barriers"]["barriers"]:
        node(f"barrier/{b['id']}", "Barrier", b["id"], gloss=b["published_meaning"],
             glyph=b["glyph"])
        enf, why = ENFORCER[b["id"]]
        if enf:
            edge(f"barrier/{b['id']}", "enforced_by", enf)
        nodes[f"barrier/{b['id']}"]["enforcement"] = why

    # --- the capabilities, decomposed ----------------------------------------
    for c in caps["capabilities"]:
        cid = f"capability/{c['id']}"
        node(cid, "Capability", c["id"], gloss=c["gloss"])
        edge(cid, "has_verb", f"verb/{c['verb']}")
        edge(cid, "acts_on", f"object/{c['object']}")
        edge(cid, "reaches", f"reach/{c['reach']}")
        edge(cid, "in_family", f"family/{c['family']}")
        edge(cid, "has_undo_class", f"undo/{c['undo']}")

    # --- the deployment shapes and what they grant ---------------------------
    for pid, p in D["profiles"].items():
        sid = f"shape/{pid}"
        node(sid, "DeploymentShape", p["product"], variant=p["variant"],
             surface=p["surface"], version=p["profile_version"])
        for r in p["grant"]:
            gid = f"granted/{pid}#{r['capability']}"
            node(gid, "GrantedCapability", f"{r['capability']} in {p['variant']}",
                 shape=pid, capability=r["capability"])
            edge(sid, "grants", f"capability/{r['capability']}")
            edge(gid, "bounded_by", f"barrier/{r['barrier']}")
            edge(gid, "known_by", f"evidence/{r['evidence']}")
        for rn, meaning in (p.get("reach_names") or {}).items():
            # A reach class means what the SHAPE says it means. That is an edge from the shape
            # to the class, not a property of the class, because two shapes disagree about
            # what `host' is and the disagreement is data rather than a defect.
            nodes.setdefault(f"reach/{rn}", None)
            if nodes.get(f"reach/{rn}"):
                nodes[f"reach/{rn}"].setdefault("named_by", []).append(
                    {"shape": pid, "means": meaning})

    # --- the deployment shape universe: products, tools, settings ----------------
    # A product is the two segments of a shape id that are not the variant. Two shapes with
    # the same product are the same thing in a different setting, which is the argument.
    by_product = {}
    for pid, p in D["profiles"].items():
        prod = "/".join(pid.split("/")[:2])
        by_product.setdefault(prod, []).append(pid)
        node(f"product/{prod}", "Product", p["product"].split(" (")[0], vendor=p.get("vendor"))
        edge(f"product/{prod}", "has_variant", f"shape/{pid}")
        # The tools, in the vendor's words, one node per shape: the same string in two shapes
        # is two exposures, because what `shell (Bash)` reaches depends on where it runs.
        tools = {}
        for t in p.get("tools", []):
            tid = f"tool/{pid}#{_slug(t)}"
            tools[t] = node(tid, "Tool", t, shape=pid)
            edge(f"shape/{pid}", "runs_with", tid)
        scopes = {}
        for r in p["grant"]:
            for v in r.get("via") or []:
                if v in tools:
                    edge(tools[v], "exposes", f"capability/{r['capability']}")
                elif " " not in v:
                    # A route with no space in it is a scope in the vendor's identifier,
                    # gmail.readonly or drive.file, and not a tool.
                    if v not in scopes:
                        sid = f"scope/{pid}#{_slug(v)}"
                        scopes[v] = node(sid, "Scope", v, shape=pid)
                        edge(f"shape/{pid}", "scoped_by", sid)
                    edge(scopes[v], "permits", f"capability/{r['capability']}")
                else:
                    tid = f"tool/{pid}#{_slug(v)}"
                    tools[v] = node(tid, "Tool", v, shape=pid)
                    edge(f"shape/{pid}", "runs_with", tid)
                    edge(tools[v], "exposes", f"capability/{r['capability']}")
    # The reductions the map publishes: for each capability, the setting that narrows it and
    # the barrier it moves to. A reduction that says `none` is not a setting.
    for cap, red in D["reductions"].items():
        if not red.get("setting") or red["setting"].startswith("none") \
                or f"capability/{cap}" not in nodes:
            continue
        sid = node(f"setting/{cap}", "Setting", red["setting"], costs=red.get("costs"),
                   tier_after=red.get("tier_after"), kind="published reduction")
        edge(sid, "narrows", f"capability/{cap}")
        for b in sorted(set(re.findall(r"\b(none|expectation|setting|boundary)\b",
                                       red.get("tier_after") or ""))):
            edge(sid, "moves", f"barrier/{b}")
    # The setting that distinguishes two variants of one product: derived by diffing their
    # grants. Whatever moved between them is what the setting moves.
    for prod, pids in by_product.items():
        for i, a in enumerate(sorted(pids)):
            for b in sorted(pids)[i + 1:]:
                ga = {r["capability"]: r["barrier"] for r in D["profiles"][a]["grant"]}
                gb = {r["capability"]: r["barrier"] for r in D["profiles"][b]["grant"]}
                moved = sorted(c for c in ga if c in gb and ga[c] != gb[c])
                if not moved:
                    continue
                va, vb = a.split("/")[-1], b.split("/")[-1]
                sid = node(f"setting/{prod}/{va}~{vb}", "Setting",
                           f"the setting that distinguishes {va} from {vb}",
                           kind="variant difference", between=[a, b])
                for c in moved:
                    edge(sid, "narrows", f"capability/{c}")
                    edge(sid, "moves", f"barrier/{ga[c]}")
                    edge(sid, "moves", f"barrier/{gb[c]}")

    # --- the mandates --------------------------------------------------------
    for mid, m in D["mandates"].items():
        nid = f"mandate/{mid}"
        node(nid, "Mandate", m["label"], surface=m["surface"])
        for c in m["want"]:
            edge(nid, "authorises", f"capability/{c}")
        for c in m["do_not_want"]:
            edge(nid, "withholds", f"capability/{c}")

    # --- the delta edges, derived ---------------------------------------------
    for mid, m in D["mandates"].items():
        for pid in m["applies_to"]:
            p = D["profiles"].get(pid)
            if not p:
                continue
            want = set(m["want"])
            for r in p["grant"]:
                if r["capability"] not in want:
                    edge(f"granted/{pid}#{r['capability']}", "exceeds", f"mandate/{mid}")
            for c in want - {r["capability"] for r in p["grant"]}:
                edge(f"mandate/{mid}", "falls_short_of", f"capability/{c}")

    return {"nodes": nodes, "edges": edges}


# ---------------------------------------------------------------------------
# the formulas, executed
# ---------------------------------------------------------------------------

def classify(g):
    """Run every node type formula against the graph and return what matched.

    THE COUNTS ON THE SITE ARE THE RESULT OF THIS FUNCTION, not fields anybody set. A formula
    that stops matching is a finding rather than a cosmetic change, which is why the release
    gate checks the one that carries the argument: exactly one barrier may be a Control."""
    out = {}
    by_type = lambda t: [n for n in g["nodes"].values() if n and n["type"] == t]
    out["Verb"] = [n["id"] for n in by_type("Verb")]
    out["ObjectClass"] = [n["id"] for n in by_type("ObjectClass")]
    out["ReachClass"] = [n["id"] for n in by_type("ReachClass")]
    out["Family"] = [n["id"] for n in by_type("Family")]
    out["Capability"] = [n["id"] for n in by_type("Capability")]
    out["DeploymentShape"] = [n["id"] for n in by_type("DeploymentShape")]
    out["GrantedCapability"] = [n["id"] for n in by_type("GrantedCapability")]
    out["Barrier"] = [n["id"] for n in by_type("Barrier")]
    out["Mandate"] = [n["id"] for n in by_type("Mandate")]

    # [Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include.
    # Walked, not asserted.
    enforced = {e["from"]: e["to"] for e in g["edges"] if e["edge"] == "enforced_by"}
    out["Control"] = [b["id"] for b in by_type("Barrier")
                      if b["id"] in enforced
                      and g["nodes"][enforced[b["id"]]]["inside_the_grant"] is False]

    # [Excess] := a [GrantedCapability] with an -exceeds-> path to the [Mandate] in scope.
    out["Excess"] = sorted({e["from"] for e in g["edges"] if e["edge"] == "exceeds"})
    bounded = {e["from"]: e["to"] for e in g["edges"] if e["edge"] == "bounded_by"}
    controls = set(out["Control"])
    out["UnboundedExcess"] = [x for x in out["Excess"] if bounded.get(x) not in controls]
    out["Shortfall"] = sorted({e["to"] for e in g["edges"] if e["edge"] == "falls_short_of"})

    # the deployment shape universe
    has_variant = {e["from"] for e in g["edges"] if e["edge"] == "has_variant"}
    out["Product"] = [n["id"] for n in by_type("Product") if n["id"] in has_variant]
    run_by = {e["to"] for e in g["edges"] if e["edge"] == "runs_with"}
    exposes = {e["from"] for e in g["edges"] if e["edge"] == "exposes"}
    out["Tool"] = [n["id"] for n in by_type("Tool") if n["id"] in run_by and n["id"] in exposes]
    scoped = {e["to"] for e in g["edges"] if e["edge"] == "scoped_by"}
    permits = {e["from"] for e in g["edges"] if e["edge"] == "permits"}
    out["Scope"] = [n["id"] for n in by_type("Scope") if n["id"] in scoped and n["id"] in permits]
    narrows = {e["from"] for e in g["edges"] if e["edge"] == "narrows"}
    moves = {e["from"] for e in g["edges"] if e["edge"] == "moves"}
    out["Setting"] = [n["id"] for n in by_type("Setting") if n["id"] in narrows and n["id"] in moves]
    return out


def _slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def out_edges(g, node_id, verb=None):
    return [e for e in g["edges"] if e["from"] == node_id and (verb is None or e["edge"] == verb)]


def in_edges(g, node_id, verb=None):
    return [e for e in g["edges"] if e["to"] == node_id and (verb is None or e["edge"] == verb)]
