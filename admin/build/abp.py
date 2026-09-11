#!/usr/bin/env python3
"""The ABP model: the four objects, the label, and the delta that is never stored.

An ABP is not a document. It is four objects, of which the document is a rendering:

    the MANDATE    elicited, in minutes, because the deployer already knows it
    the GRANT      measured, from the deployment shape and the credentials
    the DELTA      computed, NEVER STORED
    the BARRIER    recorded per capability, from one of four kinds

This module holds the third one. `delta()` is a function and not a file, and nothing here
writes a delta to disk: a stored delta is a stale claim about somebody's environment, and the
environment is the thing that changes. The build calls it on every page render.

TWO THINGS THIS MODULE WILL NOT COMPUTE, and both are refusals rather than omissions.

    A SCORE. No rating, no traffic light, no risk level, no severity. The same ABP is
    dangerous in one deployment and harmless in the next and nothing about it changed. A
    policy cannot be dangerous; a deployment can. Risk is a function of the ABP, the
    assets, the consequences and the date, and this module holds only the first.

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
# the delta: computed, never stored
# ---------------------------------------------------------------------------

def delta(profile, mandate, D):
    """The difference between what it can do and what it was authorised to do.

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
        "profile": profile["id"],
        "mandate": mandate["id"],
        "excess": order(excess, D),
        "excess_refused": order([r for r in excess if r["capability"] in refused], D),
        "excess_unstated": order([r for r in excess
                                  if r["capability"] not in refused], D),
        "unbounded_excess": order(unbounded, D),
        "shortfall": shortfall,
        "aligned": order([grant[c] for c in grant if c in want], D),
        "computed": "on this page, from the grant and the mandate, every time it is rendered",
        "never_stored": True,
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


VALIDITY = ("This describes the deployment shape as at {as_at}. It is not an expiry and it does "
            "not mean stale: if the risk changed, the deployment changed, not this document.")

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
