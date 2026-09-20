#!/usr/bin/env python3
"""The fact set: the leaf assertions every rendering of one ABP must agree on.

EVERY PROJECTION RENDERS THE SAME FACT SET, AND THE DIFF MUST BE EMPTY. That rule has been in
force since August and it blocked a promise on four consecutive days in September, because the
diff did not exist. The pack's specification was precise about what it is over: the FACTS are
the leaf assertions, this shape grants this capability at this barrier with this undo class,
this mandate takes this stance on it, therefore this excess; the CLASSES are how those facts
are grouped for a reader, an executive's by consequence, an engineer's by reach and barrier,
different at different altitudes and correct rather than a defect. So the diff is over leaf
assertions, not over structure, and this module is the leaf assertions as data.

COMPUTED, NEVER AUTHORED, like the delta it is built from. A fact set is written under
data/facts/ for every stored delta, pinning the same inputs. The release gate then reads each
example page's own markdown twin, parses the label, the leaflet, the prohibitions and the
figure out of the rendered text, and fails the build on a single leaf assertion that differs
from the fact set. That is the fact diff: it runs over the published artefact rather than over
the generator's intermediate, because a diff that trusts the generator is a diff over nothing.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import abp  # noqa: E402


def fact_set(profile, mandate, dlt, D):
    """The leaf assertions of one delta record, in the order the renderings use."""
    want, refused = set(mandate["want"]), set(mandate["do_not_want"])
    grant = abp.order(profile["grant"], D)
    assertions = []
    for r in grant:
        c = D["by_id"][r["capability"]]
        assertions.append({"kind": "grants", "capability": r["capability"],
                           "barrier": r["barrier"], "undo": c["undo"],
                           "evidence": r["evidence"],
                           "is_control": D["is_control"][r["barrier"]]})
    for cid in sorted(D["by_id"]):
        assertions.append({"kind": "stance", "capability": cid,
                           "stance": ("wanted" if cid in want else
                                      "refused" if cid in refused else "unstated")})
    for kind in ("excess", "unbounded_excess", "aligned"):
        for r in dlt[kind]:
            assertions.append({"kind": kind, "capability": r["capability"]})
    for cid in dlt["shortfall"]:
        assertions.append({"kind": "shortfall", "capability": cid})
    return {
        "type": "abp/facts/v1",
        "_what_this_is": "The leaf assertions every rendering of this ABP must agree on: what "
                         "the shape grants, at what barrier, with what undo class and evidence; "
                         "what stance the mandate takes on every primitive; and the excess, the "
                         "unbounded excess, the aligned set and the shortfall that follow. The "
                         "classes a reader sees are not here, because they differ by altitude "
                         "and the facts do not.",
        "computed_never_authored": "No field here is writable by a person. It is derived from "
                                   "the profile and the mandate it pins, and the release gate "
                                   "parses every rendering of it back out of the published "
                                   "page and fails on a single leaf assertion that differs.",
        "profile": profile["id"],
        "mandate": mandate["id"],
        "pinned": {"grant_version": dlt["grant_version"],
                   "mandate_version": dlt["mandate_version"],
                   "pack_version": dlt["pack_version"],
                   "computed_by": dlt["computed_by"]},
        "counts": {
            "primitives": D["capabilities"]["count"],
            "grant": profile["grant_size"],
            "mandate": len(mandate["want"]),
            "excess": len(dlt["excess"]),
            "unbounded_excess": len(dlt["unbounded_excess"]),
            "shortfall": len(dlt["shortfall"]),
            "irreversible": len(profile["irreversible"]),
            "widest_reach": profile["widest_reach"] or "none",
            "measured": profile["rows"]["measured"],
            "rows": profile["rows"]["total"],
        },
        "assertions": assertions,
    }
