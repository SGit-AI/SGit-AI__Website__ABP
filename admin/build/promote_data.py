#!/usr/bin/env python3
"""Promote the game's data pack into the ABP's published schema. Run: python3 admin/build/promote_data.py

The ontology this site needs already exists. It is published at what-can-it-do.games.sgit.ai
as a data pack the game reads, and the first job of this site is NOT to author an ontology but
to promote that one out of a game's internals and into a published schema with a stable address
that the rest of the network can cite.

So this module does exactly one thing: it reads the source bytes under `data/upstream/`, which
are the pack as fetched, verbatim, and writes the ABP vocabulary beside them. The rules it
follows are the ones the pack imposes on anybody who consumes it.

  · NOTHING IS RENAMED. A capability id, a barrier id, an undo class and a profile id are the
    published ones. Promoting an ontology means giving it an address, not a new vocabulary.
  · NOTHING IS ADDED to the facts. The two fields this site puts on a barrier -- `is_control`
    and the enforcer test behind it -- are a reading of the published wording, and they are
    marked as this site's reading rather than as the pack's data.
  · EVERY FILE CARRIES ITS PROVENANCE: the source URL it came from, the timestamp it was
    retrieved at, and the content hash of the pack it was cut from. A row without those three
    is an assertion, and this site publishes capability claims about named commercial products.
  · THE UPSTREAM BYTES STAY. `data/upstream/` is served as published. Anything rendered stays
    one click from its source bytes, and a consumer can recompute the hash for itself.

The delta is not here, and that is deliberate. A delta is computed from a grant and a mandate
every time it is needed and never stored, because a stored delta is a stale claim about
somebody's environment.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UP = ROOT / "data/upstream"
OUT = ROOT / "data"

# When the pack was fetched, and from where. Recorded by hand at the moment of the fetch,
# because a build that re-fetches is a build whose output nobody can reproduce.
RETRIEVED = "2026-09-11T13:00:37Z"
SOURCE = "https://what-can-it-do.games.sgit.ai/data/"

# This site's reading of the four published barriers. The wording on the left is the pack's;
# `is_control` is the enforcer test applied to it, and it is the whole argument of the ABP:
# a control bounds a grant only if it is enforced by something the grant does not include.
IS_CONTROL = {
    "none": (False, "Nothing is in the way."),
    "expectation": (False, "A rule in prose is inside the boundary the agent operates in. "
                           "All four major model providers stated in their own 2026 words that "
                           "an instruction at this layer can be bypassed."),
    "setting": (False, "The grant includes the ability to remove the bound."),
    "boundary": (True, "Enforced by something the grant does not include. The only row that "
                       "bounds anything."),
}
GLYPH = {"none": "filled circle", "expectation": "double circle",
         "setting": "half filled circle", "boundary": "empty circle", "absent": "dot"}

# The pack's evidence vocabulary is seven tiers deep; the published headline collapses it to
# measured against derived. `observed` is the tier that headline counts, and saying so here is
# cheaper than repeating a number somebody else computed.
MEASURED_TIERS = ("observed", "measured")

LICENCE = "CC BY 4.0"


def _read(rel):
    return json.loads((UP / rel).read_text())


def _hash_upstream():
    """The pack's own hash, recomputed from the bytes on disk in the pack's own order, so the
    site can state the hash it actually holds rather than the one it was handed."""
    files = sorted(
        (p.relative_to(UP).as_posix() for p in UP.rglob("*.json")
         if p.name not in ("pack.json", "packs.json", "proposals.json")),
        key=lambda s: s.split("/"))
    h = hashlib.sha256()
    for f in files:
        h.update(f.encode())
        h.update((UP / f).read_bytes())
    return "sha256:" + h.hexdigest(), len(files)


def _provenance(pack, content_hash, note):
    return {
        "source": SOURCE,
        "source_page": "https://what-can-it-do.games.sgit.ai/map/index.html",
        "retrieved": RETRIEVED,
        "pack_version": pack["version"],
        "content_hash": content_hash,
        "verbatim_bytes": "upstream/",
        "note": note,
        "licence": LICENCE,
    }


def build():
    pack = _read("pack.json")
    content_hash, hashed = _hash_upstream()
    if content_hash != pack["content_hash"]:
        raise SystemExit(f"data/upstream does not hash to what pack.json says: {content_hash} "
                         f"vs {pack['content_hash']} -- the bytes were edited after the fetch")

    prim = _read("primitives.json")
    voc = _read("vocabulary.json")
    prov = lambda note: _provenance(pack, content_hash, note)

    # --- capabilities --------------------------------------------------------
    caps = []
    for c in prim["capabilities"]:
        caps.append({
            "id": c["id"], "verb": c["verb"], "object": c["object"], "reach": c["reach"],
            "family": c["family"], "undo": c["reversible"], "gloss": c["label"],
        })
    capabilities = {
        "type": "abp/capabilities/v1",
        "_what_this_is": "The capability grammar of the Agent Behaviour Policy: verb.object.reach, "
                         "23 primitives, each with the undo class of its effect. Promoted from the "
                         "published capability map without renaming anything. A specific path, host "
                         "or mailbox is an INSTANCE of a primitive, never a new one.",
        "grammar": "verb.object.reach",
        "verbs": prim["verbs"], "object_classes": prim["object_classes"],
        "reaches": prim["reaches"], "families": prim["families"],
        "rules": prim["rules"],
        "count": len(caps),
        "capabilities": caps,
        "provenance": prov("Promoted from primitives.json. Field names changed "
                           "(reversible -> undo, label -> gloss); no id, value or gloss changed."),
    }

    # --- barriers ------------------------------------------------------------
    barriers = {
        "type": "abp/barriers/v1",
        "_what_this_is": "The four barriers, weakest first: what stands between the agent and a "
                         "capability. Every prohibition rendered anywhere on this site carries one. "
                         "A prohibition shown without its barrier is a claim the site cannot support.",
        "enforcer_test": "A control bounds a grant only if it is enforced by something the grant "
                         "does not include.",
        "order": [k for k in voc["control_tiers"] if not k.startswith("_")],
        "barriers": [
            {"id": k, "published_meaning": v, "glyph": GLYPH[k],
             "is_control": IS_CONTROL[k][0], "why": IS_CONTROL[k][1]}
            for k, v in voc["control_tiers"].items() if not k.startswith("_")
        ],
        "absent": {"id": "absent", "glyph": GLYPH["absent"],
                   "published_meaning": "not in this grant"},
        "provenance": prov("The four ids and their published meanings are the pack's "
                           "control_tiers, unchanged. is_control and why are this site's reading "
                           "of them, stated as such, and are not in the pack."),
    }

    # --- undo classes --------------------------------------------------------
    undo = {
        "type": "abp/undo-classes/v1",
        "_what_this_is": "The undo class of a capability's effect, as published by the product. It "
                         "is the ordering on every rendering this site produces, because "
                         "reversibility is a property of the ACTION rather than a severity. It is "
                         "not a score, and it is the one column that is not fully context free: "
                         "whether a deletion is reversible depends on backups the deployment owns.",
        "order": ["no", "with-effort", "yes"],
        "ordering_note": "Irreversible first on every rendering. Stated as a property of the "
                         "action, never as severity.",
        "classes": [{"id": k, "published_meaning": v} for k, v in voc["reversible"].items()],
        "provenance": prov("The pack's `reversible` vocabulary, unchanged, under the name this "
                           "site uses for it."),
    }

    # --- evidence tiers ------------------------------------------------------
    evidence = {
        "type": "abp/evidence-tiers/v1",
        "_what_this_is": "How a capability row is known, weakest first. The published headline "
                         "collapses these to measured against derived; this site keeps all seven "
                         "and states which of them it counts as measured.",
        "order": [k for k in voc["evidence_tiers"] if not k.startswith("_")],
        "counted_as_measured": list(MEASURED_TIERS),
        "tiers": [{"id": k, "published_meaning": v}
                  for k, v in voc["evidence_tiers"].items() if not k.startswith("_")],
        "provenance": prov("The pack's evidence_tiers, unchanged."),
    }

    # --- profiles ------------------------------------------------------------
    pidx = _read("profiles/index.json")
    profiles, index_rows = [], []
    for e in pidx["profiles"]:
        src = _read(f"profiles/{e['id']}.json")
        rows, measured, total = {}, 0, 0
        for tool in src.get("tools", []):
            for r in tool.get("grant", []):
                total += 1
                tier = r.get("tier") or "derived"
                if tier in MEASURED_TIERS:
                    measured += 1
                cap = r["capability"]
                # A capability reached by two tools keeps the WEAKEST barrier, because the agent
                # only has to take the easier path. That is a derivation this site makes and the
                # note says so on the row.
                keep = rows.get(cap)
                bt = r.get("control_tier") or "none"
                if keep is None or barrier_rank(bt) < barrier_rank(keep["barrier"]):
                    rows[cap] = {"capability": cap, "barrier": bt, "evidence": tier,
                                 "via": [tool["tool"]], "control": r.get("control"),
                                 "note": r.get("note")}
                else:
                    keep["via"].append(tool["tool"])
        cap_undo = {c["id"]: c["undo"] for c in caps}
        grant = sorted(rows.values(), key=lambda r: (
            ["no", "with-effort", "yes"].index(cap_undo[r["capability"]]),
            barrier_rank(r["barrier"]), r["capability"]))
        for r in grant:
            r["undo"] = cap_undo[r["capability"]]
            r["is_bounded"] = IS_CONTROL[r["barrier"]][0]
        prof = {
            "type": "abp/profile/v1",
            "id": e["id"], "vendor": e["vendor"], "product": e["product"],
            "variant": e["variant"], "surface": e["surface"],
            "profile_version": e["version"],
            "description": src["description"],
            "reach_names": src.get("reach_names", {}),
            "not_reachable": src.get("not_reachable", []),
            "tools": [t["tool"] for t in src.get("tools", [])],
            "grant": grant,
            "grant_size": len(grant),
            "irreversible": [r["capability"] for r in grant if r["undo"] == "no"],
            "unbounded": [r["capability"] for r in grant if not r["is_bounded"]],
            "widest_reach": widest([r["capability"] for r in grant], caps),
            "rows": {"total": total, "measured": measured, "derived": total - measured},
            "sources": src.get("sources", []),
            "not_an_assessment": "This describes a published deployment shape. It is not an "
                                 "assessment, an audit, a certification or a security review of "
                                 "any named product, and it carries no adjective and no score.",
            "provenance": prov(f"Promoted from profiles/{e['id']}.json. The grant is the union of "
                               f"its tool rows; where two tools reach the same capability the "
                               f"WEAKEST barrier is kept, because the agent takes the easier path."),
        }
        profiles.append(prof)
        index_rows.append({k: prof[k] for k in (
            "id", "vendor", "product", "variant", "surface", "profile_version",
            "grant_size", "widest_reach", "rows")} | {"file": f"profiles/{e['id']}.json"})

    # --- mandates ------------------------------------------------------------
    midx = _read("mandates/index.json")
    mandates, midx_rows = [], []
    for e in midx["mandates"]:
        src = _read(f"mandates/{e['file']}")
        m = {
            "type": "abp/mandate/v1",
            "id": src["id"], "label": src["label"], "surface": src["surface"],
            "applies_to": src["applies_to"],
            "status": src.get("status", "starting-point"),
            "authored": src.get("authored"), "authored_by": src.get("authored_by"),
            "description": src["description"],
            "want": src.get("want", []), "do_not_want": src.get("do_not_want", []),
            "unstated": sorted(c["id"] for c in caps
                               if c["id"] not in src.get("want", [])
                               and c["id"] not in src.get("do_not_want", [])),
            "notes": src.get("notes", {}),
            "provenance": prov(f"Promoted from mandates/{e['file']}. `unstated` is computed here "
                               f"as the primitives the mandate names neither way; the pack leaves "
                               f"it implicit. A mandate is elicited, not measured: these are first "
                               f"drafts written to be argued with."),
        }
        mandates.append(m)
        midx_rows.append({"id": m["id"], "label": m["label"], "surface": m["surface"],
                          "applies_to": m["applies_to"], "want": len(m["want"]),
                          "do_not_want": len(m["do_not_want"]),
                          "file": f"mandates/{m['id']}.json"})

    # --- totals --------------------------------------------------------------
    total_rows = sum(p["rows"]["total"] for p in profiles)
    total_measured = sum(p["rows"]["measured"] for p in profiles)
    provenance = {
        "type": "abp/provenance/v1",
        "_what_this_is": "Where every capability row on this site came from, and how much of it "
                         "was measured. The published map states the ratio and this site does not "
                         "get to be less careful than the game it took the data from.",
        "source": SOURCE,
        "source_page": "https://what-can-it-do.games.sgit.ai/map/index.html",
        "retrieved": RETRIEVED,
        "pack_version": pack["version"],
        "content_hash": content_hash,
        "files_hashed": hashed,
        "verify": "Recompute: sha256 over each .json under upstream/ in path order, hashing the "
                  "path then the bytes, skipping pack.json. admin/build/promote_data.py does it "
                  "on every build and refuses to write if it disagrees.",
        "rows": {"total": total_rows, "measured": total_measured,
                 "derived": total_rows - total_measured},
        "measured_means": "A row at the `observed` tier: seen directly, on the thing itself. No "
                          "row in this pack is at the `measured` tier, which the pack defines as a "
                          "dated probe with an evidence file. The published headline of 21 of 99 "
                          "counts the `observed` rows, and so does this site.",
        "by_tier": tier_counts(profiles),
        "never_tested": "No row here was obtained by probing anybody's system. A row is measured "
                        "only from a system we are entitled to run, or from the vendor's own "
                        "published documentation.",
        "licence": LICENCE,
    }

    # --- write ---------------------------------------------------------------
    w = lambda rel, obj: (OUT / rel).parent.mkdir(parents=True, exist_ok=True) or \
        (OUT / rel).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    w("capabilities.json", capabilities)
    w("barriers.json", barriers)
    w("undo-classes.json", undo)
    w("evidence-tiers.json", evidence)
    w("provenance.json", provenance)
    for p in profiles:
        w(f"profiles/{p['id']}.json", p)
    w("profiles/index.json", {
        "type": "abp/profiles-index/v1",
        "_what_this_is": "The deployment shapes this site holds a grant for. A shape is a product "
                         "in a setting, not a product: two entries here are the same product with "
                         "one setting different.",
        "count": len(profiles), "profiles": index_rows,
        "provenance": prov("Generated from the profile files.")})
    for m in mandates:
        w(f"mandates/{m['id']}.json", m)
    w("mandates/index.json", {
        "type": "abp/mandates-index/v1",
        "_what_this_is": "Starting mandates, one per surface. A mandate is what a reasonable person "
                         "WANTED, stated per capability. None was measured or surveyed: each is a "
                         "first draft written to be argued with.",
        "count": len(mandates), "mandates": midx_rows,
        "provenance": prov("Generated from the mandate files.")})
    return {"capabilities": capabilities, "barriers": barriers, "undo": undo,
            "evidence": evidence, "profiles": profiles, "mandates": mandates,
            "provenance": provenance, "pack": pack, "content_hash": content_hash}


def barrier_rank(b):
    """Weakest first: nothing is the easiest path, a boundary the hardest."""
    return ["none", "expectation", "setting", "boundary"].index(b)


def widest(cap_ids, caps):
    order = ["self", "project", "host", "tenant", "world"]
    by_id = {c["id"]: c for c in caps}
    reach = [by_id[c]["reach"] for c in cap_ids if c in by_id]
    return max(reach, key=order.index) if reach else None


def tier_counts(profiles):
    out = {}
    for p in profiles:
        for r in p["grant"]:
            out[r["evidence"]] = out.get(r["evidence"], 0) + 1
    return out


def manifest(built, version):
    """The one address a consumer starts from. A consumer pins a version: anything that computes
    from these files states which version it computed against, because a clone that floats
    against the latest has no reproducible output."""
    return {
        "type": "abp/pack/v1",
        "id": "abp-published-vocabulary",
        "name": "The Agent Behaviour Policy published vocabulary",
        "_what_this_is": "The capabilities, barriers, undo classes and deployment shapes an ABP is "
                         "written in, at a stable address with cross origin access. Promoted from "
                         "the published capability map rather than authored here.",
        "version": version,
        "site": "https://abp.sgit.ai/",
        "base": "https://abp.sgit.ai/data/",
        "licence": LICENCE,
        "pin_a_version": "State the version you computed against. A consumer that floats against "
                         "the latest has no reproducible output.",
        "files": {
            "capabilities": "capabilities.json",
            "barriers": "barriers.json",
            "undo_classes": "undo-classes.json",
            "evidence_tiers": "evidence-tiers.json",
            "profiles": "profiles/index.json",
            "mandates": "mandates/index.json",
            "provenance": "provenance.json",
            "upstream": "upstream/pack.json",
        },
        "counts": {
            "capabilities": built["capabilities"]["count"],
            "barriers": len(built["barriers"]["barriers"]),
            "undo_classes": len(built["undo"]["classes"]),
            "profiles": len(built["profiles"]),
            "mandates": len(built["mandates"]),
            "rows": built["provenance"]["rows"],
        },
        "not_here": {
            "delta": "A delta is computed from a grant and a mandate every time it is needed and "
                     "never stored. A stored delta is a stale claim about somebody's environment.",
            "score": "There is no score, rating, traffic light, risk level or severity in this "
                     "pack or anywhere on this site. A score is a verdict and the ABP describes "
                     "without judging.",
        },
        "provenance": built["provenance"],
    }


def main():
    version = (ROOT / "admin/build/version.txt").read_text().strip()
    built = build()
    (OUT / "index.json").write_text(
        json.dumps(manifest(built, version), indent=2, ensure_ascii=False) + "\n")
    print(f"promote_data: {built['capabilities']['count']} capabilities, "
          f"{len(built['profiles'])} profiles, {len(built['mandates'])} mandates, "
          f"{built['provenance']['rows']['measured']} of {built['provenance']['rows']['total']} "
          f"rows measured, {built['content_hash'][:19]}")


if __name__ == "__main__":
    main()
