#!/usr/bin/env python3
"""The universes: the ABP mapped onto Fractal Semantic Graphs, as data the build can walk.

ONE ROW CROSSES NINE UNIVERSES. A capability row in a deployment shape's grant is not one fact
in one vocabulary. It is a path from the bytes a primitive was promoted from, through the
grammar, into the vendor's own words about its tools and settings, into the evidence for the
row, into what enforces its barrier, into the deployer's words about what they meant, into the
derivation that records it as excess, into the renderings a reader sees, and up into the licence
and acceptance world that riskmandate.ai owns. Each of those is a UNIVERSE: a world with its own
owner, its own node types and its own verbs, joined to its neighbours by named edges and sharing
only the grammar. The map is the dev brief of 20 September 2026 in docs/briefs/; this module is
the map as data, so that the pages render it and the gate checks it rather than either of them
quoting it.

LEVELS RUN UP AND DOWN. UNIVERSES RUN ACROSS. The four objects of an ABP are not a stack: the
mandate is not above the grant. They sit side by side and each opens into a different world. A
map that stacks them is a hierarchy with the wrong shape, which is why every universe below
carries a LEVEL of down, across, up or beside rather than a rung number.

ALTITUDE KEEPS ITS 20 AUGUST SENSE on this site: a rendering of the same facts for a different
reader. That axis lives inside U7, the projections, and it is never a different world.

WHAT IS AUTHORED HERE AND WHAT IS COMPUTED. The universes, their owners, their node types and
their verbs are authored, in the same way the edge vocabulary and the node type formulas in
`graph.py` are authored: they are the model, stated once, in the file the build reads. Which
universe an existing node type belongs to is authored here too. What is COMPUTED is everything
else: which edges cross a boundary (from the universes of their domain and range types), how
many nodes each existing type matched, and the walk of one row, which is built from the
published data on every build so that the sentence on the page cannot drift from the files.

THE STATUS OF A UNIVERSE IS A CLAIM THE GATE CHECKS. `live` means its node types exist in the
graph today. `partial` means some do. `one-edge` means an edge reaches into it and finds a
world with no vocabulary yet. `outside` means another site owns it and this site holds only
the anchor nodes its edges point at. `gap` means it is named so the next release has an
address to write to, and nothing is behind the name. A universe with no owner or no status
fails the build, because a world nobody owns is a merge waiting to happen.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402
import graph  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

BRIEF = ("v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-"
         "universes-and-each-keeps-its-own-ontology")
FSG_PAGE = "https://sgit.ai/demos/fractal-graphs/index.html"
GRAPHS_LEXICON = "https://graphs.sgit.ai/v2/lexicon/index.html"
RISKMANDATE = "https://riskmandate.ai/"

STATUSES = ("live", "partial", "one-edge", "outside", "gap")
LEVELS = ("down", "across", "up", "beside")

# Which universe each node type that exists in the graph today belongs to. Authored, because
# where a type lives is a modelling decision; checked, because every type in node-types.json
# has to name a universe that exists.
NODE_TYPE_UNIVERSE = {
    "Verb": "u1", "ObjectClass": "u1", "ReachClass": "u1", "Family": "u1", "UndoClass": "u1",
    "Capability": "u1",
    "DeploymentShape": "u2", "Product": "u2", "Tool": "u2", "Setting": "u2", "Scope": "u2",
    "GrantedCapability": "u3", "EvidenceTier": "u3",
    "Barrier": "u4", "Enforcer": "u4", "Control": "u4",
    "Mandate": "u5",
    "Excess": "u6", "UnboundedExcess": "u6", "Shortfall": "u6",
    # `Node` is the domain of the two edges that may start anywhere: similar_to and supersedes.
    "Node": "any",
}

# The pages riskmandate.ai publishes for the shapes this site holds. Each reads a behaviour
# policy vault live and carries LICENCE-TO-OPERATE.md, which is the node in U8 that the edge
# licensed_under points at. Declared there, linked here by address, never held here.
RISKMANDATE_VAULT_PAGE = {
    "anthropic/claude-code-remote/ccr-container": "abp-vault-claude-code-web.html",
    "anthropic/claude-code/local-default": "abp-vault-claude-code-cli.html",
    "anthropic/claude-code/local-confirmations-off": "abp-vault-claude-code-cli-confirmations-off.html",
    "anthropic/claude-desktop/default": "abp-vault-claude-desktop.html",
    "anthropic/claude-web/connectors-on": "abp-vault-claude-web-connectors.html",
    "openai/chatgpt-web/default": "abp-vault-chatgpt-web.html",
    "generic/browser-extension/broad-host-permissions": "abp-vault-browser-extension.html",
    "github/actions-runner/ci": "abp-vault-github-actions.html",
    "generic/scheduled-job/service-account": "abp-vault-scheduled-job.html",
}

# The row the universes page walks: the shape this site is built from, the mandate that
# applies to it, and a row that is excess, bounded, and so crosses every universe including
# the one where a prohibition is enforced today.
WALK_PROFILE = "anthropic/claude-code-remote/ccr-container"
WALK_MANDATE = "coding-assistant-in-a-container"
WALK_ROW = "authenticate-as.credential.tenant"


def _v(edge, inverse, domain, range_, reads, inv_reads, src, status):
    return {"edge": edge, "inverse": inverse, "domain": domain, "range": range_,
            "reads_as": reads, "inverse_reads_as": inv_reads, "from": src, "status": status}


def _t(name, formula, exists, note=None):
    return {"name": name, "formula": formula, "exists_today": exists, "note": note}


# ---------------------------------------------------------------------------
# the universes, in the order the walk crosses them
# ---------------------------------------------------------------------------
UNIVERSES = [
    {
        "id": "u0", "n": 0, "name": "The source bytes", "level": "down",
        "owner": "nobody: the bytes are what they are",
        "centre": "the hash",
        "smallest": "a byte range in a file that was fetched on a date",
        "status": "partial",
        "status_note": "Every promoted file carries its source, its retrieval time and its "
                       "content hash, and the build refuses to run if the bytes disagree with "
                       "their manifest. Per file today; per node is the change.",
        "node_types": [
            _t("SourceFile", "a node with a -fetched_from-> [URL] and a -hashes_to-> [Digest]", False),
            _t("ByteRange", "a node -inside-> a [SourceFile] with a stated offset and length", False),
        ],
        "verbs": [
            _v("fetched_from", "serves", "SourceFile", "URL",
               "this file was fetched from this address on this date",
               "this address served this file", "proposed here", "proposed"),
            _v("hashes_to", "digest_of", "SourceFile", "Digest",
               "this file hashes to this digest", "this digest is the digest of this file",
               "proposed here", "proposed"),
            _v("hashed_from", "grounds", "Node", "ByteRange",
               "this node was read from these bytes", "these bytes ground this node",
               "proposed here; the AIUC-1 vault calls its version anchors", "proposed"),
        ],
        "adds": "Today the provenance block sits on every data file and says the same thing for "
                "every row in it. The Regulation Graph ends every chain in a hash of the "
                "retrieved bytes, per node. The per row version is what riskmandate.ai asked "
                "for in its Lab 03, request three, and it belongs here: a row's evidence is a "
                "node in U3 that is hashed_from a byte range in U0.",
    },
    {
        "id": "u1", "n": 1, "name": "The grammar", "level": "down",
        "owner": "abp.sgit.ai, promoted from what-can-it-do.games.sgit.ai and bridged back to it",
        "centre": "the primitive",
        "smallest": "the word",
        "status": "live",
        "status_note": "Complete for what it is: 10 verbs, 9 object classes, 5 reach classes, "
                       "9 families, 3 undo classes, 23 primitives, 33 word nodes with their "
                       "own addresses. Nothing is added to it by the map except one property, "
                       "material, and that is deliberate: the grammar is the shared layer that "
                       "everybody reads by address and nobody forks, so it has to stay small.",
        "node_types": [
            _t("Verb", "[Verb] := a node that is the -verb_of-> at least one [Capability]", True),
            _t("ObjectClass", "[ObjectClass] := a node that is -acted_on_by-> at least one [Capability]", True),
            _t("ReachClass", "[ReachClass] := a node that is -reachable_from-> at least one [Capability]", True),
            _t("Family", "[Family] := a node that is the -family_of-> at least one [Capability]", True),
            _t("UndoClass", "a node that is the -undo_class_of-> at least one [Capability]", True),
            _t("Capability", "[Capability] := a node with a -has_verb-> [Verb] and an -acts_on-> "
               "[ObjectClass] and a -reaches-> [ReachClass]", True,
               "Gains one property, material, with the values own, organisation, third_party "
               "and mixed: whose material a capability reaches. A property, never a fourth "
               "element of the grammar. The default lives here; the override lives on the "
               "mandate in U5."),
        ],
        "verbs": [
            _v("has_verb", "verb_of", "Capability", "Verb", "this capability has the verb read",
               "read is the verb of these capabilities", "this site", "live"),
            _v("acts_on", "acted_on_by", "Capability", "ObjectClass", "this capability acts on files",
               "files are acted on by these capabilities", "this site", "live"),
            _v("reaches", "reachable_from", "Capability", "ReachClass",
               "this capability reaches this reach class",
               "this reach class is reachable from this capability", "graphs.sgit.ai edge set", "live"),
            _v("in_family", "family_of", "Capability", "Family",
               "this capability is in the filesystem family",
               "the filesystem family is the family of these capabilities", "this site", "live"),
            _v("has_undo_class", "undo_class_of", "Capability", "UndoClass",
               "this capability has the undo class no",
               "undo class no is the undo class of these capabilities", "this site", "live"),
            _v("similar_to", "similar_to", "Node", "Node", "our node is similar to their node",
               "symmetric, and partial on purpose", "graphs.sgit.ai anchor nodes", "live"),
        ],
        "adds": "Two verbs in it, receive and revoke, have nothing under them and are kept as "
                "named absences. The grammar is the fixed point of the whole map: what every "
                "other universe attaches to by address, and what none of them may change.",
    },
    {
        "id": "u2", "n": 2, "name": "The deployment shape", "level": "across",
        "owner": "the vendor's published words, read on a date, with a hash, and never probed",
        "centre": "the setting",
        "smallest": "a scope, a flag or a line on a documentation page",
        "status": "partial",
        "status_note": "Since v0.4.3 the product, the tool a capability is reached through and "
                       "the setting that moves a barrier are nodes, all derived from data that "
                       "was already published: the tools in the vendor's words, the reductions "
                       "the map publishes per capability, and the difference between two "
                       "variants of one product. Since v0.4.4 seven shapes contributed by "
                       "riskmandate.ai are promoted here with their provenance, their scopes are "
                       "nodes in the vendor's own identifier, and material is valued on every "
                       "row they state it on. Documentation pages and contradictions are "
                       "carried as data on the profile and are not nodes yet. This is the "
                       "first universe "
                       "where the vocabulary is not this site's: a "
                       "vendor speaks in scopes, tool names, flags, consent screens and "
                       "administrator settings, and the ABP keeps them in the vendor's words "
                       "and draws an edge from each to the primitive it exposes.",
        "node_types": [
            _t("Product", "[Product] := a node that -has_variant-> at least one [DeploymentShape]", True),
            _t("DeploymentShape", "[DeploymentShape] := a node that -grants-> at least one [Capability]", True),
            _t("Tool", "[Tool] := a node that a [DeploymentShape] -runs_with-> and that -exposes-> at least one [Capability]", True,
               "One node per shape, in the vendor's words, because what shell (Bash) reaches depends on where it runs."),
            _t("Scope", "[Scope] := a node that a [DeploymentShape] is -scoped_by-> and that -permits-> at least one [Capability]", True,
               "In the vendor's word, never translated. The connector shapes contributed by "
               "riskmandate.ai at v0.4.4 reach most of their rows through one."),
            _t("Setting", "[Setting] := a node that -narrows-> at least one [Capability] and -moves-> it to at least one [Barrier]", True,
               "Two kinds, both from published data: the reduction the map publishes per "
               "capability, and the setting that distinguishes two variants of one product, "
               "derived by diffing their grants. The confirmations flag is the second kind, and "
               "it is the path the home page's pair of examples was a sentence about."),
            _t("DocumentationPage", "a [SourceFile] in U0 that a [Shape], [Tool], [Scope] or [Setting] is -documented_at->", False),
            _t("Contradiction", "a node where an -advertises-> claim and a -scoped_by-> scope on the same "
               "[Product] disagree, both quoted, both dated, published unresolved", False,
               "riskmandate.ai's Lab 01 holds four of these with verbatim quotes and URLs."),
        ],
        "verbs": [
            _v("has_variant", "variant_of", "Product", "DeploymentShape",
               "this product has this variant", "this variant is a variant of this product",
               "proposed here", "live"),
            _v("runs_with", "run_by", "DeploymentShape", "Tool",
               "this shape runs with this tool", "this tool is run by these shapes",
               "proposed here", "live"),
            _v("exposes", "exposed_by", "Tool", "Capability",
               "this tool exposes this capability", "this capability is exposed by these tools",
               "graphs.sgit.ai edge set", "live"),
            _v("scoped_by", "scopes", "DeploymentShape", "Scope",
               "this shape is scoped by this vendor scope", "this scope scopes these shapes",
               "proposed here", "live"),
            _v("permits", "permitted_by", "Scope", "Capability",
               "this scope permits this capability",
               "this capability is permitted by these scopes", "proposed here", "live"),
            _v("moves", "moved_by", "Setting", "Barrier",
               "this setting moves a capability to this barrier",
               "this barrier is where these settings move a capability to",
               "proposed here", "live"),
            _v("narrows", "narrowed_by", "Setting", "Capability",
               "this setting narrows this capability",
               "this capability is narrowed by these settings", "proposed here", "live"),
            _v("documented_at", "documents", "Shape, Tool, Scope or Setting", "DocumentationPage",
               "this tool is documented at this page, read on this date",
               "this page documents these tools", "proposed here", "proposed"),
            _v("advertises", "advertised_by", "Product", "Capability",
               "this product's page advertises this capability",
               "this capability is advertised by these products", "proposed here", "proposed"),
            _v("contradicts", "contradicted_by", "Contradiction", "Scope or Capability",
               "this advertised claim contradicts this granted scope",
               "this scope is contradicted by this claim", "proposed here", "proposed"),
            _v("grants", "granted_by", "DeploymentShape", "Capability",
               "this deployment shape grants this capability",
               "this capability is granted by this deployment shape", "graphs.sgit.ai edge set", "live"),
        ],
        "adds": "The position on a connector that is present and switched off, which is the "
                "most common state in any real estate. The enforcer test decides it: if the "
                "switch is inside the agent's grant, the capability is in the grant at barrier "
                "setting, one click away, and the label counts it; if the switch is outside "
                "the grant, the capability is not in the grant, and the estate in U9 records "
                "it as one setting away. No new barrier kind and no new label field. The "
                "seven shapes riskmandate.ai has already built are layer one facts and belong "
                "at this address, through an intake path that carries their provenance.",
    },
    {
        "id": "u3", "n": 3, "name": "The grant and its evidence", "level": "across",
        "owner": "whoever observed, or the documentation that was read",
        "centre": "the observation",
        "smallest": "one probe result on one instance on one date",
        "status": "one-edge",
        "status_note": "Every granted row carries an evidence tier and the tier is a node. "
                       "Nothing is behind the tier: no observation, no probe run, no date. "
                       "The GrantedCapability node stays what it is, the node that carries the "
                       "barrier, because the barrier is a property of a capability in a shape "
                       "and never of the capability itself.",
        "node_types": [
            _t("GrantedCapability", "[GrantedCapability] := a [Capability] with an inbound -grants-> from a "
               "[DeploymentShape], carrying a -bounded_by-> [Barrier] and a -known_by-> [EvidenceTier]", True),
            _t("EvidenceTier", "a node that -evidences-> at least one [GrantedCapability]", True),
            _t("Observation", "a node -observed_on-> an [Instance] on a date, -backed_by-> an [EvidenceFile], "
               "that -evidences-> at least one [GrantedCapability]", False),
            _t("Instance", "a running deployment of a [DeploymentShape] that somebody was entitled to run", False,
               "Named so that every observation states whose system it was and that we were "
               "entitled to run it. Never probe anybody's system."),
            _t("SelfReport", "an [Observation] made by the agent about its own grant, from inside the shape; "
               "it stays a claim until a log held outside the agent agrees", False),
            _t("EvidenceFile", "a [SourceFile] in U0", False),
            _t("Refusal", "an [Observation] that a probe was stopped before it ran, by something above the "
               "session; a barrier the grant has no row for", False),
            _t("Measured", "a [GrantedCapability] with a -measured_by-> path to an [Observation] whose "
               "[Instance] was one we were entitled to run", False,
               "Measured today is a headline, 21 of 99, counted from the observed tier. With "
               "observations as nodes it becomes a query run on every build, per row, with a "
               "date."),
        ],
        "verbs": [
            _v("known_by", "evidences", "GrantedCapability", "EvidenceTier",
               "this granted capability is known by observation",
               "observation evidences these granted capabilities", "this site", "live"),
            _v("bounded_by", "bounds", "GrantedCapability", "Barrier",
               "this granted capability is bounded by this barrier",
               "this barrier bounds these granted capabilities", "this site", "live"),
            _v("observed_on", "hosted", "Observation", "Instance",
               "this observation was made on this instance",
               "this instance hosted these observations", "graphs.sgit.ai edge set", "proposed"),
            _v("backed_by", "backs", "Observation", "EvidenceFile",
               "this observation is backed by this file", "this file backs these observations",
               "graphs.sgit.ai edge set", "proposed"),
            _v("measured_by", "measures", "GrantedCapability", "Observation",
               "this row was measured by this observation",
               "this observation measures these rows", "graphs.sgit.ai edge set", "proposed"),
            _v("contradicts", "contradicted_by", "Observation", "Observation",
               "this observation contradicts that one",
               "that observation is contradicted by this one", "proposed here", "proposed"),
            _v("stopped_by", "stopped", "Refusal", "Enforcer",
               "this probe was stopped by this enforcer", "this enforcer stopped these probes",
               "proposed here", "proposed"),
        ],
        "adds": "Lab 07's grant check, eleven of fifteen rows seen present in ordinary work and "
                "two probe batches refused by the platform's own classifier, is a SelfReport "
                "and two Refusals, and both node types are named here because that check has "
                "already happened and had nowhere to go. The calibration loop on the delta "
                "page becomes an edge somebody adds rather than a paragraph.",
    },
    {
        "id": "u4", "n": 4, "name": "The enforcement", "level": "across",
        "owner": "whoever set the control: the vendor, the platform, the deployer or nobody",
        "centre": "the enforcer",
        "smallest": "one configuration line at one layer, set by one party, on one date",
        "status": "one-edge",
        "status_note": "Four barriers, three enforcers, one Control formula that the gate "
                       "walks on every build. The formula is the most important thing on the "
                       "site and it lands in a world with three nodes. The dev brief of 11 "
                       "September on the prohibition's two lives wrote most of this universe's "
                       "vocabulary and it was never made into nodes.",
        "node_types": [
            _t("Barrier", "[Barrier] := a node that -bounds-> at least one [GrantedCapability]", True),
            _t("Enforcer", "a node that -enforces-> at least one [Barrier], -set_by-> a [Party], -at_layer-> a [Layer]", True,
               "Three today, with only inside_the_grant on each. Party and Layer are the change."),
            _t("Control", "[Control] := a [Barrier] that is -enforced_by-> an [Enforcer] the [Grant] does not include", True,
               "Does not change, and gains a second reading: with Party and removable_by as "
               "nodes and edges, does not include becomes a path, walked one universe further."),
            _t("Layer", "one of prompt, tool schema, client rule, gateway, sandbox; a node a [Layer] is -above-> or -below-> another", False),
            _t("Party", "the vendor, the platform, the deployer, the administrator, the agent's own account, or nobody", False),
            _t("EvidencedControl", "a [Control] whose [Enforcer] is -backed_by-> an [Observation] in U3", False,
               "The regulated customer's stricter formula from the three layers page, now "
               "writable beside ours without touching ours."),
            _t("CompiledRule", "a node that a [Prohibition] in U7 -compiles_to->, in a named target language, "
               "that -passes-> a shadowed permit analysis", False),
        ],
        "verbs": [
            _v("enforced_by", "enforces", "Barrier", "Enforcer",
               "this barrier is enforced by something above the grant",
               "this enforcer enforces these barriers", "this site", "live"),
            _v("set_by", "sets", "Enforcer", "Party", "this enforcer was set by this party",
               "this party sets these enforcers", "proposed here", "proposed"),
            _v("at_layer", "layer_of", "Enforcer", "Layer", "this enforcer sits at the gateway layer",
               "the gateway layer is the layer of these enforcers", "proposed here", "proposed"),
            _v("removable_by", "can_remove", "Enforcer", "Party",
               "this enforcer can be removed by this party", "this party can remove these enforcers",
               "proposed here; the enforcer test as an edge", "proposed"),
            _v("expires_on", "expiry_of", "Enforcer", "Date",
               "this enforcer is good until this date, or has no stated expiry",
               "this date is the expiry of these enforcers", "proposed here", "proposed"),
            _v("compiles_to", "compiled_from", "Prohibition", "CompiledRule",
               "this prohibition compiles to this rule", "this rule is compiled from this prohibition",
               "proposed here", "proposed"),
            _v("defeated_by", "defeats", "Barrier", "Observation",
               "this barrier was defeated in this observation", "this observation defeats this barrier",
               "graphs.sgit.ai edge set", "proposed"),
        ],
        "adds": "Lab 06 added the property the 11 September brief did not have: a barrier is "
                "perishable, and a classifier that refuses a probe today is a barrier with no "
                "row and no expiry. The five layers become nodes so that the leaflet's "
                "rightmost column, the layer a control would sit at, stops being a string.",
    },
    {
        "id": "u5", "n": 5, "name": "The deployer", "level": "across",
        "owner": "the deployer, in their own words, and the named person who will correct the draft",
        "centre": "the job",
        "smallest": "one sentence somebody said about one capability on one date",
        "status": "partial",
        "status_note": "Eight starting mandates exist, each a want list, a refuse list and an "
                       "unstated list over the 23 primitives, with a description and per "
                       "capability notes in prose. The person, the job, the purpose and whose "
                       "material are not nodes. This is the universe where customisation and "
                       "consolidation are one mechanism: a customer's mandate is written in "
                       "their vocabulary and attaches to the grammar by authorises and "
                       "withholds and to nothing else.",
        "node_types": [
            _t("Mandate", "[Mandate] := a node that -authorises-> at least one [Capability]", True),
            _t("Deployer", "an [Organisation] or [Person] that -issued-> at least one [Mandate]", False),
            _t("Owner", "a [Person] that -corrected-> or -signed-> a [Mandate]; never a team and never a function", False),
            _t("Job", "a node a [Mandate] -is_for->, in the deployer's words: draft the reply, fix the build", False),
            _t("Expectation", "one row of a [Mandate]: a [Capability] with a stance of wanted, refused or unstated, "
               "-said_by-> a [Person] on a date", False),
            _t("MaterialOverride", "a node on a [Mandate] that -overrides-> the material value of one [Capability] "
               "from U1, with its authority recorded and the default kept visible", False),
            _t("Correction", "a [Mandate] that -supersedes-> an earlier one; the sale, on riskmandate.ai's own account", False),
        ],
        "verbs": [
            _v("authorises", "authorised_by", "Mandate", "Capability",
               "this mandate authorises this capability",
               "this capability is authorised by this mandate", "this site", "live"),
            _v("withholds", "withheld_by", "Mandate", "Capability",
               "this mandate withholds this capability",
               "this capability is withheld by this mandate", "this site", "live"),
            _v("falls_short_of", "unmet_by", "Mandate", "Capability",
               "this mandate falls short of this capability it asked for",
               "this capability is unmet by this deployment shape", "this site", "live"),
            _v("is_for", "served_by", "Mandate", "Job", "this mandate is for this job",
               "this job is served by these mandates", "proposed here", "proposed"),
            _v("issued", "issued_by", "Deployer", "Mandate", "this deployer issued this mandate",
               "this mandate was issued by this deployer", "proposed here", "proposed"),
            _v("said_by", "said", "Expectation", "Person",
               "this expectation was said by this person on this date",
               "this person said these expectations", "proposed here", "proposed"),
            _v("corrected", "corrected_by", "Person", "Mandate", "this person corrected this mandate",
               "this mandate was corrected by this person", "proposed here", "proposed"),
            _v("overrides", "overridden_by", "MaterialOverride", "Capability",
               "this mandate overrides whose material this capability reaches",
               "this capability's material is overridden by this mandate", "proposed here", "proposed"),
            _v("supersedes", "superseded_by", "Node", "Node", "this claim supersedes that one",
               "that claim is superseded by this one", "graphs.sgit.ai, supersede never delete", "live"),
        ],
        "adds": "The interchange form lives here and nowhere else. The W3C rights expression "
                "vocabulary, with permission, prohibition and duty, constraints, a conflict "
                "strategy in which prohibitions win, and inheritance, is a projection of U5 "
                "and U6 written out in U7, and it is never claimed to enforce anything, "
                "because enforcement is U4. An ODRL Policy is a scoped term in this "
                "universe's lexicon; the instrument with bands, a ceiling and a premium on the "
                "licence to operate demonstration is a scoped term in U8's; the behaviour "
                "policy is the root.",
    },
    {
        "id": "u6", "n": 6, "name": "The derivation", "level": "across",
        "owner": "the computation, and never a person",
        "centre": "the pinned input",
        "smallest": "one stored record with its inputs, its time and the version of the code that produced it",
        "status": "partial",
        "status_note": "Nine stored deltas, each pinning the profile version, the mandate "
                       "version, the pack version, the time and abp.delta/v1, recomputed by "
                       "the gate on every build. What is missing is the series, the trigger "
                       "and the crossing. No field on any node here is authored: a Trigger is "
                       "received, a Crossing is computed, a Series is appended.",
        "node_types": [
            _t("Excess", "[Excess] := a [GrantedCapability] with NO -authorised_by-> path to the [Mandate] in scope", True),
            _t("UnboundedExcess", "[UnboundedExcess] := an [Excess] whose -bounded_by-> [Barrier] is not a [Control]", True),
            _t("Shortfall", "[Shortfall] := a [Capability] that a [Mandate] -authorises-> and no [DeploymentShape] in scope -grants->", True),
            _t("DeltaRecord", "a node -derived_from-> exactly one [GrantVersion] and exactly one [MandateVersion], "
               "-computed_by-> one [Computation], with an excess, an unbounded excess and a shortfall set; "
               "no field writable by a person", False,
               "Exists as a file under data/deltas/ and not yet as a node in the graph."),
            _t("Computation", "a version of the code: abp.delta/v1 today", False),
            _t("Series", "the ordered set of [DeltaRecord]s for one shape and one mandate, each -supersedes-> the last", False),
            _t("Trigger", "an event that -causes_recompute-> of a [Series]: a credential change, a token claims "
               "change, an assurance level change, a device compliance change; a new observation in U3; a "
               "corrected mandate in U5; a new pack version in U1", False),
            _t("Crossing", "a [DeltaRecord] whose count -crosses-> a [Threshold] somebody set in advance; a record, never a verdict", False),
        ],
        "verbs": [
            _v("exceeds", "exceeded_by", "GrantedCapability", "Mandate",
               "this granted capability exceeds this mandate",
               "this mandate is exceeded by these granted capabilities", "this site", "live"),
            _v("derived_from", "derived_into", "DeltaRecord", "GrantVersion or MandateVersion",
               "this record was derived from these pinned inputs",
               "these inputs were derived into this record", "proposed here", "proposed"),
            _v("computed_by", "computed", "DeltaRecord", "Computation",
               "this record was computed by this version of the code",
               "this version of the code computed these records", "proposed here", "proposed"),
            _v("causes_recompute", "recomputed_on", "Trigger", "Series",
               "this event caused this series to recompute",
               "this series was recomputed on this event", "proposed here", "proposed"),
            _v("crosses", "crossed_by", "DeltaRecord", "Threshold",
               "this record crosses this threshold", "this threshold is crossed by these records",
               "proposed here", "proposed"),
        ],
        "adds": "The gate's twelfth check, which recomputes every stored delta from its pinned "
                "inputs, extends to the series without a new idea: every record in a series "
                "recomputes, and a series with a gap in its supersedes chain fails the build. "
                "Lab 07's history folder, one entry per recompute, is the live instance of "
                "Series and it exists in riskmandate.ai's vault today.",
    },
    {
        "id": "u7", "n": 7, "name": "The projections", "level": "across",
        "owner": "the renderer, and the fact diff that has to check it",
        "centre": "the fact set",
        "smallest": "one rendered sentence that traces to one node",
        "status": "partial",
        "status_note": "The label, the leaflet and the prohibitions exist and are generated "
                       "from one call. AGENTS.md, SKILL.md and LICENCE-TO-OPERATE.md exist in "
                       "riskmandate.ai's vaults. Since v0.4.2 the fact set is a file per "
                       "stored delta under data/facts/ and the fact diff runs in the release "
                       "gate: it parses the label, the leaflet, the prohibitions and the "
                       "figure back out of each example's published twin and fails the build "
                       "on a single leaf assertion that differs. Neither is a node in the "
                       "graph yet, which is why the status stays partial. This is the "
                       "universe where altitude in the 20 August sense "
                       "lives: every projection renders the same fact set for a different "
                       "reader, and the diff over leaf assertions between any two must be empty.",
        "node_types": [
            _t("FactSet", "the leaf assertions of one [DeltaRecord]: this shape grants this capability at this "
               "barrier with this undo class; this mandate authorises these; therefore this excess. Computed, "
               "never authored", False,
               "Exists as a file per stored delta under data/facts/ since v0.4.2, and not yet as a node."),
            _t("Projection", "a node -projects-> one [FactSet], -rendered_for-> one [Audience], with every sentence "
               "-traces_to-> a node", False),
            _t("Audience", "a decision maker, an engineer, an auditor, an underwriter, an agent; the altitude axis", False),
            _t("Label", "a [Projection] with nine fields and no score", False),
            _t("Leaflet", "a [Projection] with every row", False),
            _t("Prohibition", "a [Projection] of one [Excess] row as a sentence, carrying its barrier today and the "
               "layer a control would sit at; -compiles_to-> a [CompiledRule] in U4", False),
            _t("AgentFile", "a [Projection] -rendered_for-> the agent itself: AGENTS.md, SKILL.md; honest on its own "
               "face that it is a rule in prose, the second barrier, and bounds nothing", False),
            _t("InterchangeDocument", "a [Projection] in the W3C vocabulary through the agent profile; a rule "
               "somebody wrote down until U4 compiles it", False),
            _t("FactDiff", "a node that -compares-> two [Projection]s over their [FactSet]s and is empty or names the row", False,
               "Runs as the release gate's fifteenth check since v0.4.2, over the published "
               "twin of every example, and is not yet a node."),
        ],
        "verbs": [
            _v("projects", "projected_as", "Projection", "FactSet",
               "this rendering projects this fact set", "this fact set is projected as these renderings",
               "proposed here", "proposed"),
            _v("rendered_for", "reads", "Projection", "Audience",
               "this rendering is for this reader", "this reader reads these renderings",
               "proposed here", "proposed"),
            _v("traces_to", "rendered_in", "Sentence", "Node",
               "this sentence traces to this node", "this node is rendered in these sentences",
               "proposed here", "proposed"),
            _v("compares", "compared_by", "FactDiff", "Projection",
               "this diff compares these two renderings", "these renderings are compared by this diff",
               "proposed here", "proposed"),
        ],
        "adds": "With FactSet as a node and every Projection carrying a projects edge to it, "
                "the diff is a set comparison over one node's edges, and the gate can run it "
                "on every build across the label, the leaflet, the prohibitions and the agent "
                "files. The multi audience promise on the store becomes printable the release "
                "this ships.",
    },
    {
        "id": "u8", "n": 8, "name": "The licence, the acceptance and the risk", "level": "up",
        "owner": "riskmandate.ai",
        "centre": "the named person and the date it comes back",
        "smallest": "one condition beside the thing that enforces it",
        "status": "outside",
        "status_note": "Exists on riskmandate.ai as a template file in every published vault, "
                       "unissued, and as the acceptance mechanism the Risk Graph Explorer and "
                       "the browser isolation vaults already run. This site never "
                       "holds it. It holds the anchor nodes the licence points at, and it "
                       "declares the edges that cross into it. The score has a home and this "
                       "is its address.",
        "node_types": [
            _t("LicenceToOperate", "-licensed_under-> one [Mandate] in U5 and one [DeltaRecord] in U6, -pinned_to-> a "
               "[GrantVersion] and a pack version, -issued_by-> an [Owner], -valid_until-> a date", False,
               "Owned there. The organisation is the authority, the behaviour policy is the "
               "instrument, the agent is the licensee."),
            _t("Condition", "-enforced_by-> an [Enforcer] in U4, or beside the admission that nothing enforces it", False),
            _t("Acceptance", "-accepted_by-> a named person for an interval; no deny button", False),
            _t("Risk", "-arises_from-> an [Excess] row in U6; the first node with assets in it, and the first "
               "place a score can exist", False),
            _t("Threshold", "what a [Crossing] in U6 crosses; set here, in advance, and never by the ABP", False),
        ],
        "verbs": [
            _v("licensed_under", "licenses", "LicenceToOperate", "Mandate or DeltaRecord",
               "this licence is issued under this behaviour policy",
               "this behaviour policy licenses this agent", "riskmandate.ai", "declared there"),
            _v("pinned_to", "pins", "LicenceToOperate", "GrantVersion",
               "this licence is pinned to this grant version",
               "this grant version pins these licences", "riskmandate.ai", "declared there"),
            _v("enforces_condition", "condition_of", "Enforcer", "Condition",
               "this enforcer enforces this condition of the licence",
               "this condition is enforced by this enforcer, or by nothing", "riskmandate.ai", "declared there"),
            _v("arises_from", "gives_rise_to", "Risk", "Excess",
               "this risk arises from this excess row", "this excess row gives rise to this risk",
               "graphs.sgit.ai edge set", "never drawn here"),
        ],
        "adds": "The edges are declared by riskmandate.ai in its vault, pointing at this "
                "site's addresses by version and hash, which is the three layers construction "
                "working as designed: their formulas, their bridges, our facts, and nothing "
                "merged.",
    },
    {
        "id": "u9", "n": 9, "name": "The estate and the twin", "level": "beside",
        "owner": "the customer, through twins.sgit.ai",
        "centre": "this machine, this account, this repository attached to this session",
        "smallest": "one connector present and switched off; one credential in one home directory",
        "status": "gap",
        "status_note": "The one the delta page already named: this site has no twin connected "
                       "to anything and its label says so. It resolves what host, tenant and "
                       "world mean for one instance, which is the reach class disagreement "
                       "made per estate; it holds one_setting_away for a capability whose "
                       "switch is outside the grant; it carries synchronised_at for the second "
                       "of the three clocks; and it holds a MaterialOverride when the estate "
                       "knows whose material it is.",
        "node_types": [],
        "verbs": [
            _v("instantiates", "instantiated_by", "Instance", "DeploymentShape",
               "this instance instantiates this shape", "this shape is instantiated by these instances",
               "proposed here", "gap"),
            _v("one_setting_away", "one_setting_from", "Instance", "Capability",
               "this estate is one setting away from this capability",
               "this capability is one setting from this estate", "proposed here", "gap"),
            _v("synchronised_at", "synchronised", "Instance", "Date",
               "this twin was last synchronised at this date",
               "this date is when the twin synchronised", "proposed here", "gap"),
        ],
        "adds": "Named so that a twin has an address to attach to. Nothing is behind the name.",
    },
    {
        "id": "u10", "n": 10, "name": "The obligations", "level": "beside",
        "owner": "standards.sgit.ai and the AIUC-1 conformance vault",
        "centre": "the provision",
        "smallest": "one article, one control of a standard, one line of guidance",
        "status": "gap",
        "status_note": "A bridge: the foundation document already cites the consumer guidance "
                       "of 9 March 2026, the processor rule in Article 28 and the agent "
                       "standard in prose; the change is that a citation becomes an anchor "
                       "node with a constructible URL. Never a conformance claim.",
        "node_types": [],
        "verbs": [
            _v("cites", "cited_by", "Mandate or Prohibition", "Provision",
               "this mandate cites this provision", "this provision is cited by these mandates",
               "proposed here", "gap"),
            _v("crosswalks_to", "crosswalked_from", "Control of a standard", "Capability",
               "this control crosswalks to this capability",
               "this capability is crosswalked from this control", "the AIUC-1 vault", "gap"),
        ],
        "adds": "Named so that a standard has an address to attach to.",
    },
    {
        "id": "u11", "n": 11, "name": "The runtime", "level": "beside",
        "owner": "whoever holds the logs: never this site",
        "centre": "the tool call",
        "smallest": "one call in one turn of one session",
        "status": "gap",
        "status_note": "The ABP is before the action and this universe is after it. Quantity "
                       "lives here, which is the first gap the foundation document names: "
                       "counts within an interval, sums within an interval, the licence to "
                       "operate simulation's per turn cost, and behaviour drift. The two are "
                       "joined by exactly the edges that make drift and excess different "
                       "measurements.",
        "node_types": [],
        "verbs": [
            _v("instance_of", "instanced_by", "ToolCall", "Capability",
               "this call is an instance of this capability",
               "this capability is instanced by these calls", "proposed here", "gap"),
            _v("observed_in", "observed", "ToolCall", "Session",
               "this call was observed in this session", "this session observed these calls",
               "proposed here", "gap"),
            _v("drifted_from", "drifted_by", "Session", "Mandate",
               "this session drifted from this mandate", "this mandate was drifted from by this session",
               "proposed here", "gap"),
        ],
        "adds": "Named so that a log has an address to attach to.",
    },
    {
        "id": "u12", "n": 12, "name": "The estate of agents", "level": "up",
        "owner": "the organisation",
        "centre": "one agent's output as another's input",
        "smallest": "one delegation from one agent to another",
        "status": "gap",
        "status_note": "The second gap the foundation document names, and the fractal claim "
                       "running upward: an ABP of ABPs is the same shape one level up, with "
                       "the composed grant as its grant. Nothing on the site says more than one "
                       "sentence about it today, and this is the second sentence.",
        "node_types": [],
        "verbs": [
            _v("acts_on_output_of", "output_acted_on_by", "Instance", "Instance",
               "this agent acts on the output of that agent",
               "that agent's output is acted on by this agent", "proposed here", "gap"),
            _v("delegates_to", "delegated_by", "Instance", "Instance",
               "this agent delegates to that agent", "that agent is delegated to by this agent",
               "proposed here", "gap"),
            _v("composes_into", "composed_from", "Instance", "Capability",
               "these two agents compose into this capability neither mandate authorised",
               "this capability is composed from these two agents", "proposed here", "gap"),
        ],
        "adds": "Named so that the next brief has an address to write to.",
    },
]

BY_ID = {u["id"]: u for u in UNIVERSES}


# ---------------------------------------------------------------------------
# what is computed: the crossings, the counts, the walk
# ---------------------------------------------------------------------------

def universe_of_type(t):
    """The universe a node type belongs to, or None for a type the graph does not have yet."""
    return NODE_TYPE_UNIVERSE.get(t)


def crossings():
    """Which of the live edges cross a universe boundary. COMPUTED from the universes of each
    edge's domain and range types, not declared, so the junction table on the page cannot
    disagree with the edge vocabulary."""
    out = []
    for e in graph.edge_records():
        a, b = universe_of_type(e["domain"]), universe_of_type(e["range"])
        rec = dict(e)
        rec["domain_universe"] = a
        rec["range_universe"] = b
        rec["crosses"] = (a is not None and b is not None and a != "any" and b != "any"
                          and a != b)
        out.append(rec)
    return out


def records(cls):
    """The universes as records, with the matched counts of the node types that exist."""
    out = []
    for u in UNIVERSES:
        rec = {k: v for k, v in u.items()}
        rec["node_types"] = [
            dict(t, matched=(len(cls.get(t["name"], [])) if t["name"] in cls else None))
            for t in u["node_types"]]
        out.append(rec)
    return out


def walk_row(profile, mandate, dlt, cap_id, D, g):
    """One row, nine universes. Every field comes from the published data, which is the
    only way the sentence on the page cannot drift from the files."""
    row = next(r for r in profile["grant"] if r["capability"] == cap_id)
    c = D["by_id"][cap_id]
    stance = ("wanted" if cap_id in mandate["want"] else
              "refused" if cap_id in mandate["do_not_want"] else "unstated")
    excess_ids = [r["capability"] for r in dlt["excess"]]
    unbounded_ids = [r["capability"] for r in dlt["unbounded_excess"]]
    is_excess = cap_id in excess_ids
    is_unbounded = cap_id in unbounded_ids
    enf = graph.out_edges(g, f"barrier/{row['barrier']}", "enforced_by")
    enforcer = g["nodes"][enf[0]["to"]]["label"] if enf else "nothing"
    is_control = D["is_control"][row["barrier"]]
    pro = next((p for p in abp.prohibitions(dlt, D) if p["capability"] == cap_id), None)
    prov = D["provenance"]
    rm = RISKMANDATE_VAULT_PAGE.get(profile["id"])
    via = ", ".join(row.get("via") or []) or "no tool named"
    control_note = row.get("control")

    rows = [
        ("u0", f"the row for `{cap_id}` in `data/upstream/primitives.json`, hash "
               f"`{prov['content_hash'][:22]}`, retrieved {prov['retrieved']}",
         "hashed_from, up into the grammar"),
        ("u1", f"the words `{c['verb']}`, `{c['object']}` and `{c['reach']}`, and the primitive "
               f"`{cap_id}` they spell, undo `{c['undo']}`",
         "granted_by, across into the shape"),
        ("u2", f"the shape `{profile['id']}`, variant `{profile['variant']}`, profile version "
               f"`{profile['profile_version']}`, through {via}",
         "grants, into the grant"),
        ("u3", f"the granted row, known by `{row['evidence']}`"
               + (f", with the note: {control_note}" if control_note else ""),
         "bounded_by, into the enforcement"),
        ("u4", f"the barrier `{row['barrier']}`, enforced by {enforcer}, which is "
               + ("a control" if is_control else "not a control"),
         "authorised_by or withheld_by, into the deployer's world"),
        ("u5", f"the mandate `{mandate['id']}`, authored {mandate.get('authored')}, which left "
               f"this capability **{stance}**",
         "derived_into, into the derivation"),
        ("u6", f"the stored delta computed {dlt['computed_at'] or 'at build'} by "
               f"`{dlt['computed_by']}`, pinning grant `{dlt['grant_version']}` and mandate "
               f"`{dlt['mandate_version']}`, with this row in "
               + ("**unbounded excess**" if is_unbounded else
                  "**excess** and not unbounded" if is_excess else "the **aligned** set"),
         "projected_as, into the projections"),
        ("u7", (f"the prohibition *{pro['sentence']}*, at barrier `{pro['barrier_today']}`, "
                + ("**enforced today**" if pro["enforced_today"]
                   else f"**not enforced today**, a control would sit at {pro['layer_if_enforced'] or 'a layer with no published reduction'}")
                if pro else
                "no prohibition, because the mandate asked for it; the leaflet row and the label count"),
         "licensed_under, up into the licence"),
        ("u8", ((f"a condition of `LICENCE-TO-OPERATE.md`" if is_excess else
                 f"the scope of `LICENCE-TO-OPERATE.md`")
                + f" in the behaviour policy vault riskmandate.ai publishes for this shape, "
                + ("beside the thing that enforces it, " if is_excess else "")
                + f"for an owner who has not yet signed: [{rm}]({RISKMANDATE}{rm})"
                if rm else "no published licence for this shape yet"),
         "gives_rise_to, further up into risk, which this site never draws"),
    ]

    sentence = (
        f"the words `{c['verb']}`, `{c['object']}` and `{c['reach']}` spell a primitive that the "
        f"shape `{profile['variant']}` grants through {via} as a row whose evidence tier is "
        f"{row['evidence']}, "
        f"bounded by `{row['barrier']}`, which {enforcer} enforces and which is "
        f"{'a control' if is_control else 'not a control'}, which the mandate "
        f"`{mandate['id']}` {'asked for' if stance == 'wanted' else 'left ' + stance}, "
        f"so the derivation of "
        f"{(dlt['computed_at'] or 'this build')[:10]} records it as "
        f"{'unbounded excess' if is_unbounded else 'excess and not unbounded' if is_excess else 'aligned'}"
        + (f", which the leaflet renders as a prohibition that is "
           f"{'enforced today' if pro['enforced_today'] else 'a sentence and not a control today'}"
           if pro else ", which the leaflet renders as an authorised row")
        + ((f", and which the licence in riskmandate.ai's vault for this shape carries as a "
            f"condition beside its enforcer, for an owner who has not yet signed."
            if is_excess else
            f", and which the licence in riskmandate.ai's vault for this shape carries in its "
            f"scope, for an owner who has not yet signed.")
           if rm else ", and for which no licence has been published yet."))
    return {"profile": profile["id"], "mandate": mandate["id"], "capability": cap_id,
            "rows": [{"universe": u, "node": n, "edge_leaving": e} for u, n, e in rows],
            "sentence": sentence}


def walk(D, g):
    """The walk the universes page renders: the shape this site is built from, its mandate,
    and one excess row that is bounded, so the path reaches a prohibition that is enforced."""
    p = D["profiles"][WALK_PROFILE]
    m = D["mandates"][WALK_MANDATE]
    dlt = abp.delta(p, m, D, computed_at=D["provenance"]["retrieved"])
    return walk_row(p, m, dlt, WALK_ROW, D, g)
