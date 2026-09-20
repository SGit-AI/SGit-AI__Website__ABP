#!/usr/bin/env python3
"""abp.sgit.ai - every page, as content. Run: python3 admin/build/build_pages.py

THE SITE OWNS ONE ARGUMENT and the home page says it:

    You know what you asked for. You do not know what it can do.

Everything here serves that sentence. The site publishes the free public library: the
argument, the model, the examples and the data. Buying an ABP happens on the store, so there
is no checkout, no price and no payment link anywhere in this repository.

FOUR RULES GOVERN EVERY PAGE and each of them is a build decision rather than a preference.

  · NO SCORE. Not a rating, not a traffic light, not a risk level, not a severity ranking, on
    any page, in any data file, in any figure. A score is a verdict and the ABP describes
    without judging. The one permitted ordering is irreversible first, and it is stated as a
    property of the action.
  · EVERY PAGE WITH CAPABILITY ROWS CARRIES ITS PROVENANCE: how many measured, how many
    derived, and when.
  · EVERY PROHIBITION CARRIES ITS BARRIER, because one shown without it manufactures assurance.
  · NO ADJECTIVE ABOUT A NAMED THIRD PARTY PRODUCT. This site publishes capability claims about
    nine named commercial products. A sentence saying a named product can read every page you
    visit, sourced and dated, is a record. The same sentence with `dangerously' in it is a
    verdict about somebody else's product, published by a company that sells an assessment of
    it. `admin/build/validate.js' fails the build on a list of them.

THE NAME IS AGENT BEHAVIOUR POLICY. Never Agentic: an Agentic Behaviour Policy would be a
policy about a style of behaviour, which is a category, and an Agent Behaviour Policy is the
behaviour policy for THIS AGENT IN THIS ENVIRONMENT, which is an instance. Never shortened to
`the policy', because in this estate that word already denotes the insurance instrument on the
published licence to operate demonstration. One spelling of behaviour, kept.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402
import abp_pages  # noqa: E402
import docs_pages  # noqa: E402
import graph  # noqa: E402
import lexicon_pages  # noqa: E402
import universe_pages  # noqa: E402
import promote_data  # noqa: E402
import shell  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()

MAP = "https://what-can-it-do.games.sgit.ai/map/index.html"
GRAPHS = "https://graphs.sgit.ai/"
TWINS = "https://twins.sgit.ai/"
RISKS = "https://risks.sgit.ai/"
CODING = "https://coding.sgit.ai/"
STORE = "https://store.sgit.ai/"
LTO = "https://sgit.ai/demos/vaults/licence-to-operate/index.html"
FOUNDATION_PAGE = ("docs/briefs/" + docs_pages.FOUNDATION + "/index.html")

SITE = {
    "host": "abp.sgit.ai",
    "brand": ("abp", ".sgit.ai"),
    "stage": "the free library",
    "github": "https://github.com/SGit-AI/SGit-AI__Website__ABP",
    "parent": "https://sgit.ai",
    "parent_label": "sgit.ai",
    "parent_title": "sgit.ai - the network this site is part of",
    "tagline": "The Agent Behaviour Policy: what your agent can do, what you authorised it to "
               "do, the gap between them, and what actually stands in the way.",
    "blurb": 'The <b>Agent Behaviour Policy</b>: one document, for one agent in one deployment, '
             'that puts the grant and the mandate on the same page. It describes and it does '
             'not judge, so it carries no score. '
             '<a href="{up}what-is-an-abp/index.html" style="display:inline;padding:0">'
             'The definition</a>.',
    "netline": ('<a href="' + MAP + '">&#8599; what-can-it-do.games.sgit.ai</a> - the capability '
                'map this site\'s data was promoted from &#183; '
                '<a href="' + GRAPHS + '">&#8599; graphs.sgit.ai</a> - the five graph rules &#183; '
                '<a href="' + TWINS + '">&#8599; twins.sgit.ai</a> - the interface to the real '
                'environment &#183; '
                '<a href="' + RISKS + '">&#8599; risks.sgit.ai</a> - where a score lives, and a '
                'named person signs'),
    "telemetry_note": 'This site is static. It sets no cookie, runs no analytics script and '
                      'sends nothing anywhere. '
                      '<a href="{up}data/index.html" style="display:inline;padding:0">'
                      'The data it publishes</a> is served with cross origin access on purpose.',
}

NAV = [
    ("Home", "index.html", [], ()),
    ("What is an ABP", "what-is-an-abp/index.html", [], ("what-is-an-abp/",)),
    ("The model", "model/index.html", [
        ("The four objects", "model/index.html"),
        ("The capability grammar", "model/capabilities/index.html"),
        ("The lexicon", "model/lexicon/index.html"),
        ("The barrier", "model/barriers/index.html"),
        ("The undo class", "model/undo/index.html"),
        ("The graph", "model/graph/index.html"),
        ("The edge vocabulary", "model/graph/edges/index.html"),
        ("The node type formulas", "model/graph/formulas/index.html"),
        ("The three layers", "model/graph/layers/index.html"),
        ("The universes", "model/universes/index.html"),
        ("The schema", "model/schema/index.html"),
    ], ("model/",)),
    ("Examples", "examples/index.html", [
        ("All five", "examples/index.html"),
        ("Chat, nothing connected", "examples/chatgpt-web-no-connectors/index.html"),
        ("A CLI agent, confirmations on",
         "examples/claude-code-cli-confirmations-enabled/index.html"),
        ("The same, confirmations off",
         "examples/claude-code-cli-confirmations-disabled/index.html"),
        ("A browser extension", "examples/browser-extension-broad-host-permissions/index.html"),
        ("A hosted CI runner", "examples/github-actions-hosted-runner/index.html"),
    ], ("examples/",)),
    ("Data", "data/index.html", [], ("data/",)),
    ("Docs", "docs/index.html", [
        ("Everything, rendered", "docs/index.html"),
        ("The foundation document", FOUNDATION_PAGE),
        ("How this site is built", "versions/index.html"),
    ], ("docs/", "versions/")),
]

FOOTER = [
    ("The argument", [
        ("&#8594; What is an ABP", "what-is-an-abp/index.html"),
        ("The four objects", "model/index.html"),
        ("The barrier", "model/barriers/index.html"),
        ("Five worked examples", "examples/index.html"),
    ]),
    ("The data", [
        ("The published vocabulary", "data/index.html"),
        ("The schema", "model/schema/index.html"),
        ("The source bytes", "data/upstream/pack.json"),
        ("Where it came from", MAP),
    ]),
    ("The documents", [
        ("Docs", "docs/index.html"),
        ("The foundation document", FOUNDATION_PAGE),
        ("The hard rules", "docs/pack/05__THE-HARD-RULES/index.html"),
        ("Release history", "versions/index.html"),
    ]),
    ("Across the network", [
        ("The capability map", MAP),
        ("The graph rules", GRAPHS),
        ("The style rules", CODING),
        ("llms.txt", "llms.txt"),
    ]),
]

# Every entry carries a title that is a SENTENCE rather than a label, the commit it was built
# from, and whether it was reconstructed after the fact. `basis' is what the release was built
# against; `changes' is what actually moved.
VERSION_LOG = [
    ("v0.4.2", "2026-09-20",
     "the fact set is data, the fact diff runs over every published page, and every example "
     "ends by crossing nine universes",
     {
       "summary":
         "The projections universe, one release after the map named it. Every projection "
         "renders the same fact set and the diff must be empty: a rule in force since August "
         "that blocked a promise on four consecutive days in September because the diff did "
         "not exist. It exists now, in the only form worth having. A fact set is written for "
         "every stored delta under data/facts/, the leaf assertions every rendering must "
         "agree on, computed and never authored. The release gate then parses the label, the "
         "leaflet, the prohibitions and the figure back out of each example's own published "
         "markdown twin, as text, and fails the build on a single leaf assertion that differs. "
         "The label and the leaflet are now two renderings of one fact set that are checked "
         "to carry the same facts rather than asserted to. And every example page ends with "
         "its lead row walked across nine universes, built from its own data.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "data/facts/index.json and one file per stored delta: what the shape grants at what "
         "barrier with what undo class and evidence, the mandate's stance on all 23 "
         "primitives, and the excess, unbounded excess, aligned set and shortfall that follow, "
         "pinning the same inputs as the delta. Where an example page renders the fact set, "
         "the index names the twin the gate parses.",
         "The gate's fifteenth check, the fact diff. It runs over the published page and not "
         "over the generator: the label's seven numbers, every leaflet row's capability, undo "
         "class, barrier, control status, evidence and stance, every prohibition's capability, "
         "barrier and enforcement, and the figure's three counts are read back out of the "
         "markdown twin and compared with the fact set, both ways. A diff that trusted the "
         "generator would be a diff over nothing, because the label and the leaflet come from "
         "one call.",
         "Every example page ends with its lead row crossed through nine universes as one "
         "sentence, built from the page's own profile, mandate and delta, beside the single "
         "vocabulary path it already carried, and names the fact set every number on the page "
         "is a leaf assertion in.",
         "The projections universe's status stays partial and says why: the fact set and the "
         "diff exist as files and as a gate check, and neither is a node in the graph yet.",
         "The multi format promise that the store could describe and not print is now "
         "printable for the five examples, because the guarantee behind it is a build that "
         "fails when it is false.",
       ],
       "basis": [
         "The pack's model document, for the specification the diff is built from: the facts "
         "are the leaf assertions, identical in every rendering; the classes are how a reader "
         "groups them, different by altitude, and the diff is over the former.",
         "The dev brief of 11 September on the behaviour policy as a graph, for the rule that "
         "every projection renders the same fact set with an empty diff, and for the record "
         "that the diff had not been built.",
         "The v0.4.0 brief, for the projections universe this release fills, and the build "
         "order it set out.",
       ],
     }),
    ("v0.4.1", "2026-09-20",
     "the universes become data with a page each, the walk of one row is built on every build, "
     "and the gate checks that every node type is owned",
     {
       "summary":
         "The map of v0.4.0 becomes files the build reads, pages that render one query, and a "
         "gate check. Thirteen universes are authored in admin/build/universes.py, each with "
         "its owner, its centre of gravity, its smallest node, its status, its node types and "
         "its verbs; the build writes one file per universe under data/universes/ and an index "
         "that carries the walk of one capability row through nine of them, rebuilt from the "
         "published profile, mandate and delta on every build so the sentence on the page "
         "cannot drift from the rows it is made of. Every node type now names its universe, "
         "every edge names the universes of its domain and range, and a junction is computed "
         "from those rather than declared. The gate's fourteenth check holds all of it. The "
         "release also adds a research note under /docs/research/ on the prior work the "
         "fractal claim sits beside, with every reference resolved on the day.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "data/universes/index.json and thirteen files u0.json to u12.json. The index carries "
         "the walk: nine rows, one per universe, each naming the node the walk is standing on "
         "and the edge that leaves it, over authenticate-as.credential.tenant in the shape this "
         "site is built from, and the walk as one sentence.",
         "A page at /model/universes/ that renders that one query and lists the thirteen "
         "universes with their status, and a page per universe at /model/universes/uN/ "
         "rendering its ontology: node types with the counts of the ones that exist, verbs "
         "with inverses, domains and ranges, and the edges that cross its boundary today. "
         "There is no map of everything and there will not be one.",
         "data/graph/node-types.json: every type names its universe. data/graph/edges.json: "
         "every edge names the universe of its domain and of its range and whether it crosses. "
         "Six live edges cross a boundary today: grants, bounded_by, authorises, withholds, "
         "exceeds and falls_short_of.",
         "The gate's fourteenth check: every universe has an owner and a status from the "
         "declared set, every node type names a universe that exists, every junction is "
         "computed from the edge vocabulary and listed with an owner, a live status means "
         "every declared type is in the graph, a gap declares none, and the walk crosses nine "
         "universes over a row the shape actually grants.",
         "Two corrections to the v0.4.0 brief, recorded in the brief rather than applied "
         "quietly. The walk it drew stood on send.endpoint.world, which the shape it walked "
         "does not grant; the data walks authenticate-as.credential.tenant, which is excess "
         "and bounded, and the brief now says so above the table it corrects. And two "
         "statuses moved from live to partial when the status became a gate check: the source "
         "bytes are per file rather than per node, and the derivation's records are files "
         "rather than nodes.",
         "A research note at /docs/research/: an external review of the Fractal Semantic "
         "Graphs claim against distributed description logics, E-connections, distributed "
         "first order logic, named graphs, ontology alignment, federated query, OSLC, data "
         "mesh, OSCAL, PROV-O and provenance semirings, published as received with the "
         "citation markers that did not survive the paste removed, followed by this site's "
         "reading of it: every reference resolved on 20 September 2026 with its status, what "
         "the note changes on this site, and what it does not.",
       ],
       "basis": [
         "The v0.4.0 brief, for the universes, their ontologies and the build order it set "
         "out, of which this is the first release.",
         "graphs.sgit.ai v0.6.22, for the corrected fractal claim that the status field is "
         "written against: a live universe is one whose ontology exists, not one whose "
         "format is uniform.",
         "riskmandate.ai v1.26.2, for the vault pages the eighth universe's edges point at, "
         "linked here by address and never held.",
       ],
     }),
    ("v0.4.0", "2026-09-20",
     "the ABP is mapped onto Fractal Semantic Graphs: one row crosses nine universes and each "
     "keeps its own ontology",
     {
       "summary":
         "A map, and nothing built from it yet. By the zoom test as graphs.sgit.ai now states "
         "it, the graph this site holds at v0.3.0 decomposes one vocabulary very well and "
         "crosses into another in exactly two places, the reach class disagreement and the "
         "bridge to the game. An ABP is a junction object: its four objects are owned by four "
         "different parties speaking four vocabularies, which is the case Fractal Semantic "
         "Graphs exists for. So this release publishes the map: the nine universes one "
         "capability row crosses from the source bytes to a licence condition, the ontology "
         "each keeps, the twenty two edges that cross a boundary with their owners, the "
         "lexicon as scopes, the positions on riskmandate.ai's three open requests, and the "
         "site changes in build order, one universe per release. It also corrects the fractal "
         "test this site quoted, which was the first edition's wording and scored "
         "decomposition as fractal.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "A dev brief in /docs/briefs/ carrying the map: the zoom test applied to v0.3.0 zoom "
         "by zoom, the ruling that altitude keeps its 20 August sense and universe is the word "
         "for a world with its own ontology, the walk of send.endpoint.world through nine "
         "universes as one sentence, each universe with its owner, node types, verbs, formulas "
         "and status, the junction edge set, the scoped lexicon, and the build order. It "
         "appears in the docs index, in llms.txt and in the sitemap with no second edit.",
         "The fractal test is corrected in two places it was quoted: the graph module's "
         "docstring and the three layers page. Both said that a system needing a new format "
         "or a special case is hierarchical rather than fractal, which is the first edition's "
         "wording and scores decomposition as a pass. The corrected statement is that the "
         "grammar survives every zoom and the ontology does not have to. The old sentence is "
         "recorded beside the new one rather than overwritten.",
         "The graph page links the map beside the lexicon, the edges, the formulas and the "
         "three layers, so it is reachable from the model and not only from the docs index.",
         "Nothing in the data moved. The universes, their files, their pages, the gate check "
         "over junction edges and the fact diff are the releases after this one, in the order "
         "the brief states.",
       ],
       "basis": [
         "The Fractal Semantic Graphs page at sgit.ai/demos/fractal-graphs/, read 20 September "
         "2026: every node opens into a semantic graph with its own ontology, joined by named "
         "edges; only the grammar is shared; and this site is the rung where the graph meets a "
         "real permission set, a vocabulary and not yet a join.",
         "graphs.sgit.ai v0.6.22, read 20 September 2026, for the corrected fractal claim, the "
         "zoom test in two halves, and the lexicon held as scopes with overrides recorded.",
         "riskmandate.ai v1.26.2, read 20 September 2026, for the sixteen published behaviour "
         "policy vaults, the three open requests against this site in its Lab 03, and the "
         "delivered vault in its Lab 07.",
         "store.sgit.ai v0.3.24, read 20 September 2026, for the boundary between the three "
         "sites.",
       ],
     }),
    ("v0.3.0", "2026-09-12",
     "read, file and project become nodes with their own addresses, and a node type stops being "
     "a label and becomes a formula",
     {
       "summary":
         "The model pages were a projection of nothing. A capability was an identifier with a "
         "gloss beside it, which is a self-describing node, which is schema-first thinking "
         "dressed in graph syntax: the meaning was attached to the node rather than derived "
         "from its edges. This release makes the ontology real. Every word the grammar is "
         "spelled with is now a node with an address, a JSON file and a page, "
         "`read.file.project` is three nodes joined by three edges, a node type is a formula "
         "over paths rather than a label somebody applied, and the three layer construction "
         "that lets a customer vault disagree with this vocabulary without merging anything is "
         "written down.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "A lexicon at /model/lexicon/ with a page and a JSON file per word: 10 verbs, 9 object "
         "classes, 5 reach classes and 9 families, 33 nodes that previously existed only as "
         "substrings of a capability id. A node with no address cannot be argued with, and "
         "being argued with is the point of publishing a vocabulary.",
         "The reach class pages carry the disagreement rather than resolving it: `host` means "
         "the machine you are sitting at in one deployment shape and an ephemeral container in "
         "another, and both rows are published, each owned by the shape that said it. Merging "
         "them would erase the finding, which is the ABP's own argument in one column.",
         "An edge vocabulary at /model/graph/edges/ with 15 edges, each a verb with a distinct "
         "and meaningfully named inverse, a stated domain and a stated range. Four are reused "
         "from the network's published edge set under their published names; eleven are "
         "proposed here and say so, in the same way that set marks nine of its own inverses as "
         "proposed there. There is no generic association edge in this model.",
         "Node type formulas at /model/graph/formulas/, run against the graph on every build. "
         "`is_control: true` on a barrier is gone: [Control] is now a barrier that is "
         "enforced_by an enforcer the grant does not include, walked rather than asserted, and "
         "exactly one of the four barriers matches. The release gate fails if that stops being "
         "true.",
         "The three layers at /model/graph/layers/: shared facts owned by nobody, per-party "
         "formulas, and declared bridges through anchor nodes. This is the page a customer "
         "vault needs, because it says how their vocabulary attaches to this one without "
         "either side asking permission and without anything being merged.",
         "data/graph/ carries the nodes, the edges, the edge vocabulary and the node type "
         "formulas; data/lexicon/ carries a file per word; data/bridges/ carries the declared "
         "bridges, starting with the one back to the vocabulary this was promoted from.",
       ],
       "basis": [
         "graphs.sgit.ai, read 12 September 2026: meaning through connectivity, a node carries "
         "no inherent meaning, classification is a query rather than a judgment, and "
         "vocabularies are bridged through anchor nodes rather than merged because merging "
         "erases the disagreement.",
         "The published edge set at graphs.sgit.ai/v1/grammar/edge-set.html, for the four edges "
         "reused unchanged and for the rule that extending the set needs a sentence, a "
         "different inverse sentence, a domain and a range.",
         "graphs.sgit.ai/v1/depth/, for the three layer construction and for node types as "
         "required path patterns rather than labels.",
       ],
     }),
    ("v0.2.0", "2026-09-11",
     "the delta is derived and never authored, so it is stored with its inputs pinned and the "
     "gate recomputes it",
     {
       "summary":
         "A correction to a rule this site published nine hours earlier, applied in the open. "
         "The foundation document says, twice, that the delta is computed and never stored. The "
         "first half is right and the second half is wrong: the delta is stored, and storing it "
         "is most of what makes it useful, because a question about whether a control held "
         "throughout a period is a question about a series that a recomputed present cannot "
         "answer. The corrected rule is that the delta is DERIVED AND NEVER AUTHORED, which is "
         "the harder rule, because it forbids the act rather than the artefact. The release "
         "gate's check is inverted to match: it refused any stored delta and now recomputes "
         "every one of them.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "data/deltas/ carries 9 stored deltas, one per deployment shape and mandate pair. Each "
         "record pins the version of both inputs, the published vocabulary it was computed "
         "against, the time it was computed and the version of the computation that produced "
         "it, so it can be recomputed and compared rather than taken on trust. No field in one "
         "is writable by a person.",
         "The release gate's twelfth check is inverted. It refused any file carrying a delta; "
         "it now recomputes every stored delta from the profile and the mandate it names and "
         "fails on a single row of disagreement, including the ordering. That check is a few "
         "lines because the computation is a set difference, and it is a set difference because "
         "the grant and the mandate are held as graphs with a schema rather than as prose.",
         "A new page at /model/delta/ carries the correction with both passages quoted and both "
         "replacements given, what the old rule was protecting and why all of it survives, the "
         "materialised view the pattern already had a name for, reality as the third input and "
         "the calibration loop it creates, the recompute trigger mapped onto an existing event "
         "standard, the rule that a threshold crossing is a record and the consequence is a "
         "policy somebody set in advance, the history as a business case read rather than "
         "constructed, the three clocks, and the distinction from behaviour drift.",
         "The validity statement on every example gains the second clock: as at this date, from "
         "a twin last synchronised at this date. This site has no twin connected to anything "
         "and the label says so rather than leaving the field out.",
         "The dev brief that makes the correction is published in /docs/briefs/ and appears in "
         "the index, in llms.txt and in the sitemap without a second edit, because the index is "
         "generated from the files present.",
         "The foundation document is NOT rewritten. Both corrected passages stand as published, "
         "with a correction notice above them pointing at the brief and at /model/delta/. "
         "Everything else in that document stands.",
       ],
       "basis": [
         "The dev brief of 11 September 2026, the delta is derived and never authored, which is "
         "the fifth document of that day and the first written to correct one already pushed.",
         "The foundation document of 11 September 2026, which the brief corrects in two "
         "passages and leaves standing in every other.",
         "The site building guidance, for the rule that indexes are generated from the data "
         "they index, which the brief records this as the fourth instance of.",
       ],
     }),
    ("v0.1.0", "2026-09-11",
     "the ontology is promoted out of a game and the five examples are derived rather than "
     "written",
     {
       "summary":
         "The first version of abp.sgit.ai. The capability ontology the ABP needs already "
         "existed, published, as the data pack a game reads, so this release promotes it into a "
         "schema with a stable address rather than authoring a second one, and derives five "
         "worked ABPs from it. Nothing on a generated page is typed in: every number, glyph and "
         "row is computed from data/ at build time, which is what makes the provenance line "
         "worth reading. The pipeline, the tagging and the page shell are the sibling game "
         "site's, with four changes, each of which is one of the five verifications the "
         "conventions ask for and the sibling did not have.",
       "commit": None,
       "vault": None,
       "reconstructed": False,
       "changes": [
         "The pipeline, the release gate and the page shell are copied from "
         "SGit-AI/SGit-AI__Website__Game__What-Can-It-Do at its v0.8.0: validate, then tag, "
         "then publish, with the tag derived from admin/build/version.txt and checked against "
         "the release commit's subject.",
         "data/ carries the published vocabulary: 23 capability primitives in verb.object.reach "
         "form, the four barriers, three undo classes, seven evidence tiers, nine deployment "
         "shapes and eight starting mandates, at stable addresses with cross origin access. "
         "Nothing is renamed; the source bytes are served unchanged under data/upstream/ and "
         "the build recomputes their hash on every run and refuses to write if it disagrees.",
         "Each example carries one grant-against-mandate figure that is not a table: the "
         "mandate in one column, the grant in the other, and a line joining every capability "
         "in both, so a mark with no line reaching it is excess. Colour is never the only "
         "channel, every mark carries its published barrier glyph and its full id, and the "
         "markdown twin states the same facts in prose.",
         "Five worked examples, derived from that data rather than authored, each with a label "
         "of nine fields, the grant ordered irreversible first, the mandate, the delta computed "
         "on the page, the prohibitions each carrying the barrier they sit at today, the "
         "measured-against-derived line, and the statement that none of it is an assessment.",
         "The docs section renders the foundation document, the three briefs and the six pack "
         "documents through the same block vocabulary as every other page, with the source "
         "bytes of each one click away and an index generated from the files present.",
         "The version surface the guidance asks for: versions/index.json with a file and a page "
         "per version, the badge in the chrome reading `current' from it and linking to that "
         "version's own details rather than to a generic changelog.",
         "llms.txt and llms-full.txt are generated from the site, and the gate fails the build "
         "if a page in the tree is missing from llms.txt.",
         "The version surface stops reading git. Recording the commit by resolving the tag at "
         "build time made the build non-deterministic -- it produced hashes on a checkout with "
         "tags and nulls on one without -- and the pipeline's own staleness check caught it on "
         "this release's first push. The file now records HOW TO RESOLVE the commit, `git "
         "rev-list -n 1 vX.Y.Z`, which is stable for anybody forever, and the gate checks that "
         "the resolution names this version's own tag. The guidance asks for a version to be "
         "verifiable later; a published resolution method is verifiable in a way a hash only "
         "half the world's checkouts can produce is not.",
         "Five structural guards beyond the house four: every page in llms.txt, no em dash or "
         "en dash anywhere outside the promoted data, no score vocabulary anywhere, no "
         "forbidden word, and the version surface agreeing with version.txt.",
       ],
       "basis": [
         "The foundation document of 11 September 2026, which is the definition and wins where "
         "it and the pack disagree.",
         "The build pack of 11 September 2026: what to build, the conventions, the model, the "
         "first examples, the hard rules and the prompt.",
         "The published capability map at what-can-it-do.games.sgit.ai, data pack v0.8.0, "
         "retrieved 2026-09-11, content hash sha256:d6d4ba40f1fb1f93.",
         "The vault and site building guidance at sgit.ai/docs/guidance/, read 11 September 2026.",
         "The five graph rules at graphs.sgit.ai, read 11 September 2026.",
         "The style guide at coding.sgit.ai, read 11 September 2026.",
       ],
     }),
]

# The five verifications the conventions ask for against the sibling the pipeline was copied
# from. The method is to RECORD THE GAP rather than quietly fix it and move on, so each one
# says what the sibling does and what this repository does instead.
VERIFICATIONS = [
    ("The tag is derived from the version file, not typed by hand",
     "**holds**",
     "`admin/build/version.txt` owns the version. CI reads it, refuses to tag if the newest "
     "release commit's subject disagrees, refuses if the tag already exists on an earlier "
     "commit, and refuses if the bump is not the next minor or a deliberate major. Copied "
     "unchanged."),
    ("The build fails when `llms.txt` does not list every page",
     "**did not hold**",
     "The sibling generates `llms.txt` from its page list, so it cannot miss a page the "
     "generator knows about, and nothing fails if a page exists in the tree that the generator "
     "does not. Check 11 here walks the tree and fails on any `.html` page missing from "
     "`llms.txt`."),
    ("The custom domain survives a rebuild",
     "**did not hold**",
     "The sibling commits `CNAME` once. Here the build writes it from `SITE['host']`, and the "
     "canonical check reads the same file, so a domain change is one edit in one place."),
    ("The markdown twin of every page is produced by the build",
     "**holds**",
     "`shell.write_site` emits the `.html` and the `.md` from the same block list, and gate "
     "check 7 fails on a page without a twin. Copied unchanged, and it is the reason the twins "
     "cannot drift."),
    ("The version in the chrome comes from `versions/index.json`",
     "**did not hold**",
     "The sibling has no `versions/index.json` at all: the badge reads `version.txt` and links "
     "to a hand-maintained history page. Here the build generates `versions/index.json`, a file "
     "and a page per version, from the same string the tag is derived from, and the badge links "
     "to that version's own details. The published pipeline still owns the tag, so the two "
     "cannot disagree."),
]

# Where this pack, the guidance and the published sources disagree. The published source wins
# and the disagreement is recorded rather than quietly resolved.
DISAGREEMENTS = [
    ("SETTLED IN v0.2.0. The foundation document and the project lead, on whether a delta is "
     "stored",
     "v0.1.0 built to the foundation document's rule that the delta is computed and NEVER "
     "STORED, and put a check in the release gate refusing any file that carried one. The "
     "project lead's correction, issued the same day, is that the second half was an error: "
     "the delta belongs in a vault along with the history of the grants and mandates that "
     "produced it.",
     "v0.2.0 stores the deltas with their inputs pinned and inverts the check, so the gate now "
     "recomputes every one of them. **Never authored** is the rule that replaced it, and it is "
     "harder than the one it replaced. See [the delta](model/delta/index.html)."),
    ("The foundation document and the published data, on what changes when confirmations go off",
     "The foundation document says that turning confirmations off moves the barrier on **every "
     "capability in the delta** by one row. In the published pack it moves exactly one barrier, "
     "on `execute.process.host`, and that capability is **inside the mandate**: the deployer "
     "asked for it. So the label's numbers do not move at all and the two documents still "
     "differ materially.",
     "The data wins on the fact and the foundation document wins on the wording, so both "
     "example pages state what actually changes. It makes the pair a **better** argument, not a "
     "worse one: identical headline numbers, a materially different document, which is the case "
     "for the leaflet and against any single number."),
    ("The pack and the sibling, on where the version lives",
     "The conventions ask for `versions/index.json` as the home of the version. The sibling's "
     "working pipeline derives the tag from `admin/build/version.txt` and has no "
     "`versions/index.json`.",
     "Both. `version.txt` still owns the tag, because that is the published pipeline and it "
     "wins; `versions/index.json` is generated from the same string, so the surface the "
     "guidance asks for exists and cannot drift from the tag. The gate checks the agreement."),
    ("The pack and the published data, on whether the smallest grant has an empty delta",
     "The pack says the smallest shape in the set is where a reader who does not believe an "
     "agent can do much *finds the delta is still not empty*. In the published data that "
     "shape's grant is one capability and the starting mandate asks for exactly it, so **the "
     "delta is empty**.",
     "The example says so, plainly, and says why an empty delta is a result rather than a "
     "failure: a method that could never report nothing would be a sales document, and the "
     "other four examples would be worth less for it. Changing the mandate to manufacture a "
     "delta would have been the dishonest fix."),
    ("The published headline and the pack's own vocabulary, on what `measured' means",
     "The map's headline says 21 of 99 rows were measured. The pack's vocabulary defines "
     "`measured` as a dated probe with an evidence file, and **no row in the pack is at that "
     "tier**: the 21 are at `observed`, which is seen directly on the thing itself.",
     "The site counts `observed` as measured, which reproduces the published figure, and says "
     "so in `data/provenance.json` and on the data page. Reproducing the number without the "
     "note would have been less careful than the map."),
    ("The hard rules and the published data, on em dashes and pure ASCII",
     "Every document in this repository is to be pure ASCII, with zero em dashes and zero en "
     "dashes. The data promoted from the capability map carries all three, because it was "
     "written elsewhere and this site does not get to edit somebody else's bytes.",
     "Both. The JSON keeps the upstream strings exactly as they arrived and `data/` is exempt "
     "from the guard for that reason; every upstream string rendered into a page is "
     "transliterated at render time; and the bytes are one click away under `/data/upstream/`. "
     "The guard is in the pipeline and fails the build everywhere else."),
    ("The guidance and the docs section, on rebuilding the markdown renderer",
     "The guidance forbids rebuilding markdown viewing, file trees and page layouts, because "
     "the platform provides them. The docs section has to turn eleven markdown documents into "
     "pages.",
     "`admin/build/docs_pages.py` translates a markdown document into the same small block "
     "vocabulary every other page here is written in, at build time. No viewer is shipped to a "
     "browser, no file tree and no layout engine, and the source bytes are served beside every "
     "rendered document. It is a judgement call and it is recorded as one rather than assumed."),
]


# ---------------------------------------------------------------------------
# the home page: the argument, in one screen, derived from the foundation document
# ---------------------------------------------------------------------------

def home(D):
    caps = D["capabilities"]["count"]
    prov = D["provenance"]
    pair = []
    for slug in ("claude-code-cli-confirmations-enabled",
                 "claude-code-cli-confirmations-disabled"):
        e = next(x for x in abp_pages.EXAMPLES if x[0] == slug)
        p, m = D["profiles"][e[1]], D["mandates"][e[2]]
        pair.append((slug, p, m, abp.delta(p, m, D)))
    (_, p_on, m_on, d_on), (_, p_off, _, d_off) = pair
    moved = [r for r in p_off["grant"]
             if next(x["barrier"] for x in p_on["grant"]
                     if x["capability"] == r["capability"]) != r["barrier"]]

    return {
        "title": "Agent Behaviour Policy",
        "description": "You know what you asked for. You do not know what it can do. The Agent "
                       "Behaviour Policy is the document that puts the two on the same page: "
                       "the grant, the mandate, the delta and the barrier, for one agent in one "
                       "deployment, with no score.",
        "blocks": [
            ("h1", "You know what you asked for. You do not know what it can do."),
            ("lead", "An **Agent Behaviour Policy** is a written description, for one agent in "
                     "one deployment, of everything it can do, what it was authorised to do, the "
                     "difference between the two, and what actually stands in the way. It is "
                     "derived from the deployment rather than copied from a template. **It "
                     "describes and it does not judge, so it carries no score.**"),

            ("h2", "The gap"),
            ("p", "**You know what you asked for.** Draft the reply, fix the build, summarise "
                  "the ticket, book the travel. That is the mandate, and it is usually clear, "
                  "whether or not anybody wrote it down."),
            ("p", "**You do not know what it can do.** The agent runs with an account, on a "
                  "machine, inside a container or on a desktop, with credentials and network "
                  "access and a set of tools. Everything those permit is the grant. It is almost "
                  "never enumerated, and when it is, it is larger than the person who deployed "
                  "the agent expected."),
            ("note", f"**Before you scroll.** For a deployment you actually run, write down how "
                     f"many of {caps} capability primitives you think it has, and how many of "
                     f"those you asked for. Then read [the five worked "
                     f"examples](examples/index.html). The gap between your two numbers is the "
                     f"reason this document type exists."),

            ("h2", "The four objects"),
            ("p", "An ABP is not a single list. It is four objects, and the order they are "
                  "produced in matters."),
            ("table", ["Object", "What it is", "How it is obtained"], [
                ["**The mandate**", "What the agent is authorised and expected to do",
                 "**Elicited.** In minutes, because the deployer already knows it"],
                ["**The grant**", "Everything the agent can do",
                 "**Measured.** From the deployment shape, the account and the credentials"],
                ["**The delta**", "Excess where it can and you did not ask; shortfall where you "
                                  "asked and it cannot",
                 "**Derived.** Recomputed whenever the grant or the mandate changes, "
                 "stored with the versions of both, and never edited by hand"],
                ["**The barrier**", "What stands between the agent and each capability",
                 "**Recorded**, per capability, from one of four kinds"],
            ]),
            ("note", "**The delta is derived and never authored.** Nobody writes one: it is "
                     "only ever the output of a computation over the grant and the mandate, and "
                     "it is stored with the versions of both inputs and the time it was "
                     "computed. This site said the opposite this morning, and **the correction "
                     "is published rather than applied quietly**: "
                     "[what changed and what follows from it](model/delta/index.html)."),
            ("p", "**A grant on its own is an inventory, and nobody acts on an inventory.** "
                  "*Your agent can do three hundred and forty things* is a shrug. *Your agent "
                  "can do three hundred and forty things and you authorised twelve* is a "
                  "finding. [The model, in full](model/index.html)."),

            ("h2", "Only one kind of thing is actually in the way"),
            abp_pages.barrier_legend(),
            ("note", f"**{D['barriers']['enforcer_test']}** Read the third and fourth rows "
                     f"together and the test falls out of them. A setting the agent's own "
                     f"account could change is not a control, because the grant includes the "
                     f"ability to remove the bound. [The barrier](model/barriers/index.html)."),

            ("h2", "One setting, two documents"),
            ("p", f"The clearest way to see what an ABP does is to change one setting and watch "
                  f"the document change. A coding agent on a developer's own machine, profiled "
                  f"twice: once with confirmations enabled, once with them disabled. Same "
                  f"product, same machine, same account."),
            ("table", ["", "Confirmations on", "Confirmations off"], [
                ["Grant", str(p_on["grant_size"]), str(p_off["grant_size"])],
                ["Mandate", str(len(m_on["want"])), str(len(m_on["want"]))],
                ["Excess", str(len(d_on["excess"])), str(len(d_off["excess"]))],
                ["Unbounded excess", str(len(d_on["unbounded_excess"])),
                 str(len(d_off["unbounded_excess"]))],
                ["Barrier on `execute.process.host`",
                 next(r["barrier"] for r in p_on["grant"]
                      if r["capability"] == "execute.process.host") + " (not a control)",
                 next(r["barrier"] for r in p_off["grant"]
                      if r["capability"] == "execute.process.host") + " (not a control)"],
            ]),
            ("p", f"**{len(moved)} barrier moved and not one number did.** The confirmation "
                  f"prompt was the only thing standing between an authorised capability and the "
                  f"whole of the machine, and it was a setting the agent's own account could "
                  f"change, which is the third row and not the fourth. **The ABP is about the "
                  f"deployment, not the product**, and the pair says it in a way no paragraph "
                  f"can: [confirmations "
                  f"on](examples/claude-code-cli-confirmations-enabled/index.html) and "
                  f"[confirmations "
                  f"off](examples/claude-code-cli-confirmations-disabled/index.html)."),

            ("h2", "It describes and it does not judge"),
            ("p", "**The same ABP is dangerous in one deployment and harmless in another, and "
                  "nothing about the document changed.** The most permissive grant imaginable, "
                  "running where there are no assets and nothing reachable, is a low risk. The "
                  "same grant with a production database attached tomorrow is a high one. Risk "
                  "is a function of the ABP, the assets, the consequences and the date, and "
                  "**the ABP is the one input that does not move.**"),
            ("note", "**A policy cannot be dangerous. A deployment can.** So there is no rating "
                     f"on an ABP, no traffic light and no risk level, anywhere on this site or "
                     f"in its data. Every reader asks for one. **The score has a home and it is "
                     f"[the risk work above this]({RISKS})**, where the assets are known and a "
                     f"named person signs. The people who sell do not sign, which is why the "
                     f"two are separate products and not two sections of one."),

            ("h2", "What is here"),
            ("cards", [
                {"title": "[What an ABP is](what-is-an-abp/index.html)",
                 "sub": "The foundation document: the definition, the four objects, the barrier, "
                        "one worked example with published numbers, and the questions we would "
                        "like answered.",
                 "foot": "This is the document, rendered. Not a summary of it."},
                {"title": "[The delta](model/delta/index.html)",
                 "sub": "Derived and never authored. Stored with its inputs pinned, recomputed "
                        "when either moves, and the history is the business case.",
                 "foot": "Corrected on 11 September, in the open."},
                {"title": "[The model](model/index.html)",
                 "sub": f"The {caps} capability primitives, the four barriers, the three undo "
                        f"classes, the graph rules and the schema.",
                 "foot": "Promoted from a published map, not invented here."},
                {"title": "[Five worked examples](examples/index.html)",
                 "sub": "From the smallest grant in the set to a service account that outlives "
                        "the turn. Derived from the data, with the delta computed on the page.",
                 "foot": "Each states how many rows were measured."},
                {"title": "[The data](data/index.html)",
                 "sub": "The published vocabulary as JSON, at stable addresses with cross origin "
                        "access, with the source bytes it was promoted from.",
                 "foot": f"{prov['rows']['measured']} of {prov['rows']['total']} rows measured."},
                {"title": "[The docs](docs/index.html)",
                 "sub": "Every reference document behind this site, rendered, each one click "
                        "from its source bytes.",
                 "foot": "The index is generated from the files present."},
                {"title": f"[Where a score lives]({RISKS})",
                 "sub": "The ABP is the input. The risk work above it knows the assets and the "
                        "consequences, and a named professional signs.",
                 "foot": "Not here, and that is the point."},
            ]),

            ("h2", "What an ABP is not"),
            ("ul", [
                "**Not an acceptable use policy.** That governs a person's use of a system. An "
                "ABP governs what an agent can and may do.",
                "**Not a risk assessment.** It has no assets in it and no consequences. It is "
                "the input to one.",
                "**Not a compliance assessment, a certification, an audit or a security "
                "review** of anything or anybody.",
                "**Not a guardrail.** It is what guardrails are compiled from. The barrier "
                "column says which prohibitions are guardrails already and which are sentences.",
                "**Not a claim about any product.** The capability rows come from published "
                "documentation and published measurement, with the source, the date and the "
                "measured ratio stated, and no adjective attached to any of them.",
                "**Not a template.** It is derived from one deployment, and a template cannot "
                "know what your agent can do.",
            ]),

            ("h2", "This site is the library. It is free, and it stays free"),
            ("p", "The argument, the model, the examples and the data are published here. "
                  "**There is no checkout on this site and there will not be one.** The data "
                  "files are the shared facts and they live in the repository so that people can "
                  "propose changes to them, with evidence attached."),
            ("p", f"[Propose a change](data/index.html) · [The repository]({SITE['github']}) "
                  f"· [Everything on this site, in one file](llms-full.txt)"),
            abp_pages.provenance_block(prov["rows"]),
            ("note", "**Validity.** " + abp.VALIDITY.format(as_at=abp_pages.AS_AT, synced=abp_pages.SYNCED)),
        ]}


# ---------------------------------------------------------------------------
# what is an ABP: the foundation document, rendered, with its terms linked
# ---------------------------------------------------------------------------

# Each term, the node it belongs to. The first mention of a term in the document becomes a
# link; the rest are left alone, because a page where every third word is blue is a page
# nobody reads. This is the memo's wish that every word be hyperlinked, met the way the third
# graph rule allows: every word CAN be a node, and no page renders the graph.
TERMS = [
    ("the grant", "model/index.html"),
    ("the mandate", "model/index.html"),
    ("the delta", "model/index.html"),
    ("the barrier", "model/barriers/index.html"),
    ("capability primitives", "model/capabilities/index.html"),
    ("undo class", "model/undo/index.html"),
    ("unbounded excess", "model/barriers/index.html"),
    ("validity statement", "model/index.html"),
    ("deployment shape", "data/index.html"),
]


# The two passages the dev brief of 11 September corrects, and the replacement wording it
# gives verbatim. The foundation document is NOT rewritten: the pack requires it published as
# written, the brief itself says everything else in it stands, and a document corrected by
# silently editing it is a document nobody can trust. So the correction is rendered ABOVE each
# passage, where a reader meets it before the sentence it corrects, and the source bytes under
# /docs/ stay exactly as published.
CORRECTIONS = [
    ("Never stored, because the deployment changes",
     "**Corrected the same day.** The replacement wording is: **The delta. Derived.** "
     "Recomputed whenever the grant or the mandate changes, stored with the versions of both, "
     "and never edited by hand. "
     "[What changed and what follows from it](model/delta/index.html)."),
    ("The delta is computed and never stored",
     "**Corrected the same day.** The replacement wording is: **The delta is derived and never "
     "authored.** Nobody writes a delta. It is only ever the output of a computation over the "
     "grant and the mandate, and it is stored along with the versions of both inputs and the "
     "time it was computed. That is what makes it checkable rather than stale. **What must "
     "never happen is that somebody edits a delta**, because a hand edited delta is a fiction "
     "about an environment, and nothing downstream could tell. "
     "[What changed and what follows from it](model/delta/index.html)."),
    ("the delta is computed and never stored, and the barrier is recorded per capability",
     "**Corrected the same day.** Claim 3 reads, in the corrected wording: the mandate is "
     "elicited, the grant is measured, **the delta is derived and never authored**, and the "
     "barrier is recorded per capability. "
     "[What changed and what follows from it](model/delta/index.html)."),
]


def what_is_an_abp(D):
    src = ROOT / "docs/briefs" / (docs_pages.FOUNDATION + ".md")
    href = "docs/briefs/" + docs_pages.FOUNDATION + ".md"
    title, blocks = docs_pages.to_blocks(src.read_text(), href,
                                         "docs/briefs/" + docs_pages.FOUNDATION + ".md")
    seen, corrected = set(), set()
    linked = []
    for kind, *args in blocks:
        # A corrected passage gets its correction rendered immediately BEFORE it, so a reader
        # cannot meet the superseded sentence without the replacement.
        if isinstance(args[0], str):
            for i, (needle, note) in enumerate(CORRECTIONS):
                if i not in corrected and needle in args[0]:
                    linked.append(("note", note))
                    corrected.add(i)
        elif kind == "table":
            flat = " ".join(c for r in args[1] for c in r)
            for i, (needle, note) in enumerate(CORRECTIONS):
                if i not in corrected and needle in flat:
                    linked.append(("note", note))
                    corrected.add(i)
        if kind in ("p", "lead") and isinstance(args[0], str):
            linked.append((kind, _link_terms(args[0], seen)))
        else:
            linked.append((kind, *args))
    if len(corrected) != len(CORRECTIONS):
        raise SystemExit(f"what_is_an_abp: {len(CORRECTIONS) - len(corrected)} correction(s) "
                         f"found no passage to attach to. The foundation document changed, or "
                         f"the needle did. A correction that silently fails to render is worse "
                         f"than no correction.")
    return {
        "title": "What is an Agent Behaviour Policy",
        "description": "The foundation document: the definition of the Agent Behaviour Policy, "
                       "the four objects, the barrier as the test of whether anything is in the "
                       "way, the rule that it never judges, and the questions we are asking.",
        "blocks": [
            ("crumb", "[Home](index.html) / What is an ABP"),
            ("h1", shell.ascii_safe(title)),
            ("note", "**Two passages in this document were corrected on the day it was "
                     "published, and this page does not rewrite them.** Both stand exactly as "
                     "written, each with its correction rendered immediately above it, because "
                     "a document corrected by silently editing it is a document nobody can "
                     "trust. The correction is that **the delta is derived and never "
                     "authored**, not computed and never stored. [The brief that makes it]"
                     "(docs/briefs/" + abp_pages._DELTA_BRIEF + "/index.html) and [what follows "
                     "from it](model/delta/index.html). Everything else in this document "
                     "stands."),
            ("note", "**This is the foundation document itself, rendered, not a summary of it.** "
                     "It is the definition the rest of this site stands on, and it is the "
                     "document being put in front of the community for feedback, so its wording "
                     "is the wording. Where it and anything else on this site disagree, it wins, "
                     "and the disagreements are recorded in "
                     "[v0.1.0's notes](versions/v0.1.0/index.html) rather than resolved quietly. "
                     "The first mention of each term below links to its node in "
                     "[the model](model/index.html)."),
        ] + linked,
    }


def _link_terms(s, seen):
    for term, href in TERMS:
        if term in seen:
            continue
        # Never inside an existing link or a code span: the shell's inline pass would nest them.
        i = s.find(term)
        if i < 0 or "](" in s[max(0, i - 40):i] or "`" in s[max(0, i - 3):i + len(term) + 3]:
            continue
        s = s[:i] + f"[{term}]({href})" + s[i + len(term):]
        seen.add(term)
    return s


# ---------------------------------------------------------------------------
# the version surface, as pages
# ---------------------------------------------------------------------------

def version_pages():
    pages = {}
    rows = []
    for v, date, title, entry in VERSION_LOG:
        rel = f"versions/{v}/index.html"
        rows.append([f"[{v}]({rel})", date, title])
        blocks = [
            ("crumb", f"[Home](index.html) / [Versions](versions/index.html) / {v}"),
            ("h1", f"{v}: {title}"),
            ("lead", entry["summary"]),
            ("table", ["Field", "Value"], [
                ["Version", f"`{v}`"], ["Date", date],
                ["Commit", f"**`git rev-list -n 1 {v}`**. The tag is the record: CI "
                           f"derives it from `admin/build/version.txt` and creates it on the "
                           f"commit whose subject carries `site {v}:`. The hash is not written "
                           f"into [`versions/{v}.json`](versions/{v}.json), because a release "
                           f"commit cannot contain its own hash and reading it back from the "
                           f"tag made the build produce different bytes on a checkout with "
                           f"tags than on one without."],
                ["Reconstructed", "yes" if entry["reconstructed"] else "no"],
                ["Machine readable", f"[`versions/{v}.json`](versions/{v}.json)"],
            ]),
            ("h2", "What changed"),
            ("ul", entry["changes"]),
            ("h2", "What it was built against"),
            ("ul", entry["basis"]),
        ]
        if v == VERSION_LOG[0][0]:
            blocks += [
                ("h2", "The five verifications against the sibling"),
                ("p", "The pipeline, the release gate and the page shell were copied from "
                      "[SGit-AI__Website__Game__What-Can-It-Do](https://github.com/SGit-AI/"
                      "SGit-AI__Website__Game__What-Can-It-Do) at its v0.8.0. The conventions "
                      "ask for five things to be verified rather than assumed, and **an absent "
                      "one is a finding that belongs in the first version's notes** rather than "
                      "a thing to fix quietly."),
                ("table", ["Verification", "The sibling", "What this repository does"],
                 [[a, b, c] for a, b, c in VERIFICATIONS]),
                ("p", "**Two of the three that did not hold are one-line fixes and the third is "
                      "a surface that did not exist.** None of them is a criticism of a site "
                      "that has been publishing for weeks: they are the cost of a pipeline "
                      "growing by copy, which is exactly what the five verifications are for."),
                ("h2", "Where the sources disagree"),
                ("p", "The published source wins and the disagreement is recorded. **The "
                      "estate's method is to record the gap, not to quietly resolve it.**"),
                ("table", ["The disagreement", "What each says", "What this site did"],
                 [[a, b, c] for a, b, c in DISAGREEMENTS]),
                ("h2", "What is not built yet, stated plainly"),
                ("ul", [
                    "**No view across the nine shapes.** Each example carries a "
                    "grant-against-mandate figure, and there is no figure that puts one "
                    "capability across every deployment shape at once. The third graph rule "
                    "says render the result of a query rather than the whole graph, so that "
                    "would be another query rather than a map.",
                    "**No ABP for a shape outside the published map**, which means the cost of "
                    "producing one where the grant has to be measured rather than looked up is "
                    "still unknown, and that is the number the store needs.",
                    "**No interchange form emitted.** The W3C vocabulary is described on [the "
                    "graph page](model/graph/index.html) and nothing on this site serialises to "
                    "it yet.",
                    "**Quantity and agent-to-agent interaction are not modelled**, as the model "
                    "page says. They are gaps in the ontology rather than in this site.",
                ]),
            ]
        pages[rel] = {
            "title": f"{v}: {title}",
            "description": entry["summary"][:280].rsplit(" ", 1)[0] + "...",
            "blocks": blocks,
        }

    pages["versions/index.html"] = {
        "title": "Versions",
        "description": "Every release of this site, with the commit it was built from and what "
                       "it was built against. The version in the chrome links here.",
        "blocks": [
            ("crumb", "[Home](index.html) / Versions"),
            ("h1", "Versions"),
            ("lead", "Every release of this site. **The badge in the top bar reads `current` "
                     "from [`versions/index.json`](versions/index.json) and links to that "
                     "version's own details**, rather than to a generic changelog, which is what "
                     "the guidance asks for."),
            ("table", ["Version", "Date", "What changed"], rows),
            ("h2", "How the version cannot drift"),
            ("p", "`admin/build/version.txt` owns the version. The tag is derived from it by "
                  "CI, which refuses to tag unless the newest release commit's subject carries "
                  "the same string and the bump is the next one. The build generates "
                  "[`versions/index.json`](versions/index.json) and a file per version from that "
                  "same string, and the release gate fails if the badge, `llms.txt`, the twins "
                  "or the version surface disagree with it."),
            ("p", "**Each entry records the commit**, because a version without one cannot be "
                  "verified later, and **says when it was reconstructed**, because history "
                  "assembled after the fact has to be labelled."),
            ("p", "[The machine readable index](versions/index.json) · "
                  f"[The repository]({SITE['github']})"),
        ]}
    return pages


# ---------------------------------------------------------------------------

def main():
    promote_data.main()
    D = abp.load()
    g = graph.build(D)
    cls = graph.classify(g)
    pages = {"index.html": home(D), "what-is-an-abp/index.html": what_is_an_abp(D)}
    for source in (abp_pages.pages(D), lexicon_pages.pages(D, g, cls),
                   universe_pages.pages(D, g, cls), docs_pages.pages(),
                   version_pages()):
        clash = set(source) & set(pages)
        if clash:
            raise SystemExit(f"pages collide: {sorted(clash)}")
        pages.update(source)
    summary = shell.write_site(ROOT, SITE, NAV, FOOTER, pages, VERSION, VERSION_LOG)
    prov = D["provenance"]
    print(f"build_pages: {VERSION} - {summary}; {len(abp_pages.EXAMPLES)} examples and "
          f"{D['capabilities']['count']} capabilities from the pack, "
          f"{prov['rows']['measured']} of {prov['rows']['total']} rows measured")


if __name__ == "__main__":
    main()
