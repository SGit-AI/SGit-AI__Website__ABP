#!/usr/bin/env python3
"""The ABP model: the four objects, the label, and the delta that is derived and never authored.

An ABP is not a document. It is four objects, of which the document is a rendering:

    the MANDATE    elicited, in minutes, because the deployer already knows it
    the GRANT      measured, from the deployment shape and the credentials
    the DELTA      DERIVED, recomputed whenever either input changes, stored with the versions
                   of both, and NEVER EDITED BY HAND
    the BARRIER    recorded per capability, from one of four kinds

CORRECTED ON 11 SEPTEMBER 2026, and the correction is recorded rather than quietly applied.
The first published wording was that the delta is computed and NEVER STORED. Half of that was
right. The delta is computed; it is also stored, and storing it is most of what makes it
useful, because the history of grants, mandates and deltas is what turns a business case into
a subtraction that is read rather than constructed.

    THE DELTA IS DERIVED AND NEVER AUTHORED. Nobody writes a delta. It is only ever the
    output of a computation over the grant and the mandate, and it is stored along with the
    versions of both inputs and the time it was computed.

Everything the old ruling was protecting survives, and one thing is protected better:

    a stale claim         a stored delta carries its inputs and the time it was computed, so
                          its staleness is a fact rather than a surprise
    a hand edited delta   NEVER AUTHORED is a harder rule than never stored, because it
                          forbids the ACT rather than the artefact
    a delta treated as    it reacts. A recompute is cheap because the inputs are graphs
    authoritative after
    the inputs move

The word for this already exists: it is a MATERIALISED VIEW. Stored for use, refreshed from
its inputs, never edited directly, carrying its own staleness. Writing to one is a category
error rather than a permission question, and it is the fourth instance of a pattern already in
force across this estate, alongside indexes generated from the data they index, prose derived
from the graph, and a bill of materials generated from the dependency files.

TWO THINGS THIS MODULE WILL NOT COMPUTE, and both are refusals rather than omissions.

    A SCORE. No rating, no traffic light, no risk level, no severity. The same ABP is
    dangerous in one deployment and harmless in the next and nothing about it changed. A
    policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the
    assets, the consequences and the date, and this module holds only the first.

    A CONSEQUENCE. A delta crossing a threshold is a RECORD. What follows from it is a
    policy somebody set in advance, not a judgement this code makes. That is what keeps the
    automation real and the ABP consequence agnostic at the same time, and it means any
    suspension is traceable to a threshold a person chose and a computation anybody can rerun.

    AN ORDERING BY CONSEQUENCE. The one ordering here is irreversible first, and it is
    descriptive: reversibility is a property of the ACTION. The risk product reorders by
    consequence because it knows the consequence. This module does not know it.

The path a reader follows through these objects has to read as a sentence, which is the fifth
graph rule and the acceptance test for the model:

    agent `claude-code-cli-confirmations-disabled` is-granted capability `execute.process.host`
    bounded-by barrier `a-rule-somebody-wrote-down` which-exceeds mandate `ship-a-feature`
    and-is undo `no`
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

# The version of THIS computation. A stored delta records which version of the code produced
# it, because the code changes and a record that does not say what computed it cannot be
# compared with one produced later. Bump it whenever `delta()` changes what it returns.
COMPUTED_BY = "abp.delta/v1"

UNDO_ORDER = ["no", "with-effort", "yes"]
BARRIER_ORDER = ["none", "expectation", "setting", "boundary"]
REACH_ORDER = ["self", "project", "host", "tenant", "world"]


def load():
    """Everything the model is written in, read from the published files rather than typed."""
    J = lambda p: json.loads((DATA / p).read_text())
    caps = J("capabilities.json")
    d = {
        "capabilities": caps,
        "by_id": {c["id"]: c for c in caps["capabilities"]},
        "barriers": J("barriers.json"),
        "undo": J("undo-classes.json"),
        "evidence": J("evidence-tiers.json"),
        "provenance": J("provenance.json"),
        "profiles_index": J("profiles/index.json"),
        "mandates_index": J("mandates/index.json"),
        "reductions": json.loads((DATA / "upstream/reductions.json").read_text())["reductions"],
    }
    d["profiles"] = {e["id"]: J(e["file"]) for e in d["profiles_index"]["profiles"]}
    d["mandates"] = {e["id"]: J(e["file"]) for e in d["mandates_index"]["mandates"]}
    d["is_control"] = {b["id"]: b["is_control"] for b in d["barriers"]["barriers"]}
    d["barrier_meaning"] = {b["id"]: b["published_meaning"] for b in d["barriers"]["barriers"]}
    d["glyph"] = {b["id"]: b["glyph"] for b in d["barriers"]["barriers"]}
    return d


# ---------------------------------------------------------------------------
# the delta: derived, stored, never authored
# ---------------------------------------------------------------------------

def delta(profile, mandate, D, computed_at=None):
    """The difference between what it can do and what it was authorised to do.

    DERIVED AND NEVER AUTHORED. The return value is the stored record's content: it pins the
    version of each input and the time and code version that produced it, so a consumer can
    recompute it and compare rather than take it on trust. A delta that carries no inputs is
    exactly the claim the older `never stored' wording was afraid of; one that carries them is
    checkable. What must never happen is that somebody edits it, because a hand edited delta is
    a fiction about an environment and nothing downstream could tell. `admin/build/validate.js'
    recomputes every stored record on every build for that reason.

    EXCESS is the published definition: in the grant and not in the mandate. That is a wider
    set than the capabilities the mandate explicitly refused, and it is the right one, because
    a mandate that never mentioned a capability did not authorise it. The split is reported
    underneath rather than hidden, because a reader is entitled to know which excess was
    refused outright and which was never considered.

    UNBOUNDED EXCESS is the excess whose barrier is not a control -- nothing, a rule somebody
    wrote down, or a setting the agent's own account could change. It is the only number on
    the label a buyer can move, and every control bought moves one capability into the fourth
    row and takes the number down by one.
    """
    grant = {r["capability"]: r for r in profile["grant"]}
    want = set(mandate["want"])
    refused = set(mandate["do_not_want"])

    excess = [grant[c] for c in grant if c not in want]
    unbounded = [r for r in excess if not D["is_control"][r["barrier"]]]
    shortfall = sorted(want - set(grant))
    return {
        "type": "abp/delta/v1",
        "profile": profile["id"],
        "mandate": mandate["id"],
        # The inputs, pinned. Without these the record is not checkable.
        "grant_version": profile["profile_version"],
        "mandate_version": mandate.get("authored"),
        "pack_version": D["provenance"]["pack_version"],
        "computed_at": computed_at,
        "computed_by": COMPUTED_BY,
        "excess": order(excess, D),
        "excess_refused": order([r for r in excess if r["capability"] in refused], D),
        "excess_unstated": order([r for r in excess
                                  if r["capability"] not in refused], D),
        "unbounded_excess": order(unbounded, D),
        "shortfall": shortfall,
        "aligned": order([grant[c] for c in grant if c in want], D),
        "derived_never_authored":
            "No field in this record is writable by a person. The way to change a delta is to "
            "change a grant or a mandate, and then recompute.",
    }


def order(rows, D):
    """Irreversible first, then weakest barrier first, then by id. The default order on every
    rendering this site produces. Alphabetical would bury the only rows that matter."""
    return sorted(rows, key=lambda r: (
        UNDO_ORDER.index(D["by_id"][r["capability"]]["undo"]),
        BARRIER_ORDER.index(r["barrier"]),
        r["capability"]))


# ---------------------------------------------------------------------------
# the label: one line, on the outside, for anybody
# ---------------------------------------------------------------------------

def label(profile, mandate, dlt, D, as_at):
    """Nine fields and no score. Two of them are the headline: excess answers the buyer's
    question, and unbounded excess is the only one a control purchase moves."""
    rows = profile["rows"]
    return [
        ("Shape", profile["product"] + (f", {profile['variant']}" if profile["variant"] else ""),
         "The named deployment, in the product's published words"),
        ("Grant", f"{profile['grant_size']} of {D['capabilities']['count']} primitives",
         "Everything the agent can do"),
        ("Mandate", f"{len(mandate['want'])} primitives",
         "What the deployer authorised and expected"),
        ("Excess", str(len(dlt["excess"])),
         "In the grant, not in the mandate. The finding"),
        ("Unbounded excess", str(len(dlt["unbounded_excess"])),
         "Excess whose barrier is not a control. The only number a control purchase moves"),
        ("Irreversible", str(len(profile["irreversible"])),
         "Granted capabilities with undo: no, as published"),
        ("Widest reach", profile["widest_reach"] or "none",
         "The furthest reach class in the grant"),
        ("Measured", f"{rows['measured']} of {rows['total']} rows",
         "Rows seen directly against rows derived"),
        ("As at", f"{as_at}, pack {D['provenance']['pack_version']}",
         "The date and the source version"),
    ]


VALIDITY = ("This describes the deployment shape as at {as_at}, from a twin last synchronised "
            "at {synced}. It is not an expiry and it does not mean stale: if the risk changed, "
            "the deployment changed, not this document.")

# Three clocks, and only the first is ours. An ABP is exactly as fresh as the twin, and the
# twin is exactly as fresh as its connection to somebody else's systems. That is a parameter
# rather than a defect to hide, and the gap between the second and the third belongs to the
# risk layer, because how much it matters depends on the assets.
CLOCKS = [
    ("The ABP's clock", "When the grant was last measured or calibrated",
     "Us, and it can run on events"),
    ("The twin's clock", "When the twin last synchronised with the real environment",
     "The customer's integration"),
    ("Reality's clock", "Never stops", "Nobody"),
]

NOT_AN_ASSESSMENT = (
    "**This is not an assessment.** Nothing here is an audit, a certification, a compliance "
    "assessment or a security review of any named product. It is an illustration of a method, "
    "using a published configuration, and every row carries its source, its date and whether it "
    "was measured or derived. No adjective is attached to any of it, and there is no score.")


# ---------------------------------------------------------------------------
# prohibitions: the enforceable projection of the delta
# ---------------------------------------------------------------------------

def prohibitions(dlt, D):
    """The subset of the delta a control can bound, each carrying the layer it would be
    enforced at and whether it is enforced TODAY.

    Every prohibition rendered anywhere on this site carries its barrier. A prohibition shown
    without one manufactures assurance: at the first three barriers it is a sentence, not a
    control, and the whole argument of the ABP is that most of them are sentences today.
    """
    out = []
    for r in dlt["excess"]:
        c = D["by_id"][r["capability"]]
        red = D["reductions"].get(r["capability"])
        out.append({
            "capability": r["capability"],
            "sentence": f"The agent must not {c['gloss'][0].lower() + c['gloss'][1:]}.",
            "barrier_today": r["barrier"],
            "enforced_today": D["is_control"][r["barrier"]],
            # A published reduction can name a layer WEAKER than where this deployment already
            # sits: the reductions are written for the general case. Showing one against a
            # prohibition that is already enforced above the grant would read as advice to
            # weaken it, so the column says where it already is instead.
            "layer_if_enforced": (None if D["is_control"][r["barrier"]]
                                  else (red or {}).get("tier_after")),
            "how": (red or {}).get("setting"),
            "costs": (red or {}).get("costs"),
            "undo": c["undo"],
        })
    return out


def counts(dlt, D):
    p = prohibitions(dlt, D)
    return {"prohibitions": len(p),
            "enforced_today": sum(1 for x in p if x["enforced_today"]),
            "sentences_today": sum(1 for x in p if not x["enforced_today"])}
