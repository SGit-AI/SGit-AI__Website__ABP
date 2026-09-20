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

THE DELTA IS HERE, and as of 11 September 2026 that is a correction rather than an oversight.
The first published wording said a delta was computed and never stored. The corrected rule is
that THE DELTA IS DERIVED AND NEVER AUTHORED: it is stored, with the version of each input and
the time and code version that produced it, because the history of grants, mandates and deltas
is what turns a business case into a subtraction read rather than constructed, and because an
underwriter or an auditor asking whether a control held throughout a period is asking about a
series, which a recomputed present cannot answer.

So `deltas/` is written by `write_deltas()` below, from `abp.delta()`, on every build. No field
in any of those records is writable by a person, and the release gate recomputes every one of
them and fails on a single row of disagreement.
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
        # THIS SITE'S OWN, and marked as such: not in the pack. Proposed by riskmandate.ai in
        # its Lab 03 (request 1) because reach answers how far and not whose. A property on a
        # granted row, never a fourth element of the grammar, because a fourth element
        # multiplies the primitives and the vocabulary has to stay readable by address.
        "material": {
            "_what_this_is": "Whose material a capability reaches, stated on a granted row in a "
                             "deployment shape. This site's own property, proposed by "
                             "riskmandate.ai on 12 September 2026 and adopted at v0.4.3; it is "
                             "not in the pack this grammar was promoted from.",
            "values": {"own": "the deployer's own material",
                       "organisation": "the deployer's organisation's material",
                       "third_party": "other people's material",
                       "mixed": "other people's material mixed with the deployer's, and no "
                                "setting the vendor documents makes it otherwise"},
            "placement": "On the granted row, because it is a property of a capability in a "
                         "context: a mailbox connector reaches mixed material wherever it is "
                         "connected. A mandate may override it for one deployment. The nine "
                         "shapes promoted from the map do not state it, and the value is null "
                         "on their rows rather than guessed.",
            "why": "A grant you hold over other people's material is not a grant you may pass "
                   "on. Reach does not answer whose; this does.",
        },
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
                                 "note": r.get("note"), "material": r.get("material")}
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


def manifest(built, version, n_deltas):
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
            "deltas": "deltas/index.json",
            "facts": "facts/index.json",
            "graph": "graph/index.json",
            "lexicon": "lexicon/index.json",
            "bridges": "bridges/index.json",
            "universes": "universes/index.json",
            "provenance": "provenance.json",
            "upstream": "upstream/pack.json",
        },
        "counts": {
            "capabilities": built["capabilities"]["count"],
            "barriers": len(built["barriers"]["barriers"]),
            "undo_classes": len(built["undo"]["classes"]),
            "profiles": len(built["profiles"]),
            "mandates": len(built["mandates"]),
            "deltas": n_deltas,
            "universes": 13,
            "rows": built["provenance"]["rows"],
        },
        "the_delta": "Derived and never authored. Stored under deltas/, each record pinning the "
                     "version of both inputs and the time and code version that produced it. No "
                     "field in one is writable by a person: change a grant or a mandate and "
                     "recompute. Corrected from `computed and never stored` on 11 September "
                     "2026; the brief is in /docs/briefs/.",
        "not_here": {
            "consequence": "A delta crossing a threshold is a record. What follows from it is a "
                           "policy somebody set in advance, and it is not in this pack.",
            "score": "There is no score, rating, traffic light, risk level or severity in this "
                     "pack or anywhere on this site. A score is a verdict and the ABP describes "
                     "without judging.",
        },
        "provenance": built["provenance"],
    }


def write_deltas(built, computed_at):
    """The stored deltas: one record per (shape, mandate) pair the starting mandates name.

    A MATERIALISED VIEW, in the decades-old sense. It exists for use, it is refreshed from its
    inputs, its staleness is knowable because it pins their versions, and writing to it
    directly is a category error rather than a permission question.

    Imported here rather than at module scope because `abp` reads the files this module
    writes, so it cannot be loaded until they exist."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import abp  # noqa: E402

    D = abp.load()
    rows, index = [], []
    for m in built["mandates"]:
        for pid in m["applies_to"]:
            if pid not in D["profiles"]:
                continue
            rec = abp.delta(D["profiles"][pid], D["mandates"][m["id"]], D, computed_at)
            # The stored record carries the capability ids, not the whole grant row: the row
            # lives in the profile and duplicating it here would create a second place for it
            # to be wrong.
            for k in ("excess", "excess_refused", "excess_unstated", "unbounded_excess",
                      "aligned"):
                rec[k] = [r["capability"] for r in rec[k]]
            rec["counts"] = {k: len(rec[k]) for k in
                             ("excess", "unbounded_excess", "shortfall", "aligned")}
            slug = f"{pid.replace('/', '__')}__{m['id']}"
            rec["id"] = slug
            rec["provenance"] = _provenance(built["pack"], built["content_hash"],
                                            "Derived from the grant and the mandate named "
                                            "above. Never authored: no field here is writable "
                                            "by a person, and the release gate recomputes it.")
            (OUT / "deltas").mkdir(parents=True, exist_ok=True)
            (OUT / f"deltas/{slug}.json").write_text(
                json.dumps(rec, indent=2, ensure_ascii=False) + "\n")
            index.append({"id": slug, "profile": pid, "mandate": m["id"],
                          "grant_version": rec["grant_version"],
                          "mandate_version": rec["mandate_version"],
                          "computed_at": rec["computed_at"],
                          "computed_by": rec["computed_by"],
                          "counts": rec["counts"], "file": f"deltas/{slug}.json"})
            rows.append(rec)
    (OUT / "deltas/index.json").write_text(json.dumps({
        "type": "abp/deltas-index/v1",
        "_what_this_is": "Stored deltas, one per deployment shape and mandate pair. DERIVED AND "
                         "NEVER AUTHORED: each record pins the version of both inputs and the "
                         "time and code version that produced it, so it can be recomputed and "
                         "compared rather than taken on trust. A delta that carries no inputs "
                         "is the stale claim the earlier `never stored` wording was afraid of.",
        "correction": "The foundation document of 11 September 2026 says the delta is computed "
                      "and never stored. That was corrected the same day: the delta is derived "
                      "and never authored. The correction and what follows from it are in the "
                      "dev brief of 11 September in /docs/briefs/.",
        "never_authored": "No field in any of these records is writable by a person. The way to "
                          "change a delta is to change a grant or a mandate, and recompute.",
        "count": len(index), "deltas": index,
        "provenance": _provenance(built["pack"], built["content_hash"],
                                  "Generated from the profiles and the mandates."),
    }, indent=2, ensure_ascii=False) + "\n")
    return index


def write_universes(D, g, cls, prov):
    """The universes as files: an index carrying the walk of one row, and one file per
    universe carrying its owner, its status, its node types with their matched counts, its
    verbs, and the edges that leave it.

    THE MAP IS DATA SO THAT NOTHING QUOTES IT. The dev brief of 20 September 2026 draws the
    map in prose; these files are what the pages render and what the gate checks, and the
    walk in the index is rebuilt from the published profiles, mandates and deltas on every
    build, so the sentence on the page cannot drift from the rows it is made of."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import universes as U  # noqa: E402

    (OUT / "universes").mkdir(parents=True, exist_ok=True)
    recs = U.records(cls)
    cross = [e for e in U.crossings() if e["crosses"]]
    for u in recs:
        leaving = [{"edge": e["edge"], "inverse": e["inverse"], "to": e["range_universe"],
                    "status": "live"}
                   for e in cross if e["domain_universe"] == u["id"]]
        rec = {
            "type": "abp/universe/v1",
            **u,
            "junctions_live": leaving,
            "page": f"https://abp.sgit.ai/model/universes/{u['id']}/index.html",
            "brief": f"https://abp.sgit.ai/docs/briefs/{U.BRIEF}/index.html",
            "provenance": prov("The universe is authored in admin/build/universes.py; the "
                               "matched counts and the live junctions are computed from the "
                               "graph on every build."),
        }
        (OUT / f"universes/{u['id']}.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False) + "\n")

    (OUT / "universes/index.json").write_text(json.dumps({
        "type": "abp/universes/v1",
        "_what_this_is": "The ABP mapped onto Fractal Semantic Graphs. One capability row "
                         "crosses nine universes, from the source bytes to a licence "
                         "condition, and each universe keeps its own owner, node types and "
                         "verbs, sharing only the grammar. Four more are named as gaps so "
                         "that a twin, a standard, a log or an estate of agents has an "
                         "address to attach to.",
        "levels": "Levels run up and down, to the byte and to the estate of agents. "
                  "Universes run across. The four objects of an ABP are neighbours and "
                  "never a stack.",
        "altitude": "Altitude keeps its 20 August sense on this site: a rendering of the same "
                    "facts for a different reader. It lives inside u7 and is never a "
                    "different world.",
        "statuses": {"live": "its node types exist in the graph today",
                     "partial": "some of them do",
                     "one-edge": "an edge reaches into it and finds no vocabulary yet",
                     "outside": "another site owns it; this site holds the anchor nodes "
                                "its edges point at",
                     "gap": "named so the next release has an address; nothing behind it"},
        "count": len(recs),
        "universes": [{"id": u["id"], "n": u["n"], "name": u["name"], "level": u["level"],
                       "owner": u["owner"], "status": u["status"],
                       "node_types": len(u["node_types"]),
                       "node_types_today": sum(1 for t in u["node_types"] if t["exists_today"]),
                       "verbs": len(u["verbs"]),
                       "file": f"universes/{u['id']}.json"} for u in recs],
        "junctions_live": [{"edge": e["edge"], "inverse": e["inverse"],
                            "from": e["domain_universe"], "to": e["range_universe"],
                            "owner": "this site"} for e in cross],
        "walk": U.walk(D, g),
        "brief": f"https://abp.sgit.ai/docs/briefs/{U.BRIEF}/index.html",
        "definition": U.FSG_PAGE,
        "provenance": prov("Authored in admin/build/universes.py, walked on every build."),
    }, indent=2, ensure_ascii=False) + "\n")
    return recs


def write_facts(built, computed_at, examples):
    """One fact set per stored delta, and an index that names the renderings of each.

    THE DIFF RUNS OVER THE PUBLISHED PAGE. The index records, for every fact set that an
    example page renders, the markdown twin the gate parses the label, the leaflet, the
    prohibitions and the figure back out of. A fact set nothing renders is still written,
    because a consumer rendering it elsewhere needs the same leaf assertions to check against."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import abp  # noqa: E402
    import facts as F  # noqa: E402

    D = abp.load()
    rendered = {(pid, mid): slug for slug, pid, mid, *_ in examples}
    index = []
    (OUT / "facts").mkdir(parents=True, exist_ok=True)
    for m in built["mandates"]:
        for pid in m["applies_to"]:
            if pid not in D["profiles"]:
                continue
            p, md = D["profiles"][pid], D["mandates"][m["id"]]
            dlt = abp.delta(p, md, D, computed_at)
            rec = F.fact_set(p, md, dlt, D)
            slug = f"{pid.replace('/', '__')}__{m['id']}"
            rec["id"] = slug
            rec["delta"] = f"deltas/{slug}.json"
            ex = rendered.get((pid, m["id"]))
            rec["projections"] = ([
                {"kind": "label", "rendered_at": f"examples/{ex}/index.md"},
                {"kind": "leaflet", "rendered_at": f"examples/{ex}/index.md"},
                {"kind": "prohibitions", "rendered_at": f"examples/{ex}/index.md"},
                {"kind": "figure", "rendered_at": f"examples/{ex}/index.md"},
            ] if ex else [])
            rec["provenance"] = _provenance(built["pack"], built["content_hash"],
                                            "Derived from the profile and the mandate named "
                                            "above. Never authored: the gate parses every "
                                            "rendering back out of its page and diffs it.")
            (OUT / f"facts/{slug}.json").write_text(
                json.dumps(rec, indent=2, ensure_ascii=False) + "\n")
            index.append({"id": slug, "profile": pid, "mandate": m["id"], "example": ex,
                          "projections": len(rec["projections"]),
                          "assertions": len(rec["assertions"]), "file": f"facts/{slug}.json"})
    (OUT / "facts/index.json").write_text(json.dumps({
        "type": "abp/facts-index/v1",
        "_what_this_is": "One fact set per stored delta: the leaf assertions every rendering "
                         "of that ABP must agree on. Where an example page renders one, the "
                         "index names the markdown twin the release gate parses the label, the "
                         "leaflet, the prohibitions and the figure back out of, and the build "
                         "fails on a single leaf assertion that differs. That is the fact diff.",
        "the_rule": "Every projection renders the same fact set with an empty diff. The facts "
                    "are the leaf assertions; the classes a reader sees differ by altitude, "
                    "and that is correct rather than a defect.",
        "count": len(index), "facts": index,
        "provenance": _provenance(built["pack"], built["content_hash"],
                                  "Generated from the profiles and the mandates."),
    }, indent=2, ensure_ascii=False) + "\n")
    return index


def write_graph(built, computed_at):
    """The graph, the lexicon and the bridges, as files.

    EVERY WORD IN THE GRAMMAR GETS AN ADDRESS. Until v0.3.0 a verb, an object class and a reach
    class existed only as substrings of a capability id, which made them unaddressable: nothing
    could link to `host`, nothing could disagree with it, and a customer vault had nowhere to
    attach a bridge. A node with no address cannot be argued with, and being argued with is the
    point of publishing a vocabulary."""
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import abp  # noqa: E402
    import graph as G  # noqa: E402
    import universes as U  # noqa: E402

    D = abp.load()
    g = G.build(D)
    cls = G.classify(g)
    prov = lambda note: _provenance(built["pack"], built["content_hash"], note)
    write_universes(D, g, cls, prov)

    # --- the lexicon, a file per word ---------------------------------------
    KIND = {"Verb": ("verbs", "has_verb"), "ObjectClass": ("objects", "acts_on"),
            "ReachClass": ("reaches", "reaches"), "Family": ("family", "in_family")}
    KIND["Family"] = ("families", "in_family")
    lex_index = {}
    for ntype, (folder, edge_name) in KIND.items():
        rows = []
        for n in sorted((n for n in g["nodes"].values() if n and n["type"] == ntype),
                        key=lambda n: n["label"]):
            caps = sorted(e["from"].split("/", 1)[1]
                          for e in G.in_edges(g, n["id"], edge_name))
            rec = {
                "type": f"abp/lexicon-node/v1",
                "id": n["id"], "node_type": ntype, "label": n["label"],
                "gloss": n.get("gloss"),
                "_meaning": "A node carries no inherent meaning. What this node IS emerges from "
                            "the edges below, not from the gloss. The gloss is a convenience for "
                            "a reader and is never the definition.",
                "in_capabilities": caps,
                "count": len(caps),
                # A node connected to nothing is literally meaningless. Two verbs in the
                # published grammar are in that position, and saying so is more useful than
                # dropping them or pretending they carry weight.
                "unused": not caps,
                "unused_note": (None if caps else
                                "This word is in the published grammar and no capability "
                                "primitive uses it. A node connected to nothing is literally "
                                "meaningless, so this one means nothing yet. It is kept, and "
                                "marked, because the gap is a finding about the vocabulary "
                                "rather than a mistake in it: a primitive using this verb "
                                "would need a probe before it could be added."),
                "named_by": n.get("named_by"),
                "page": f"https://abp.sgit.ai/model/lexicon/{folder}/{n['label']}/index.html",
                "provenance": prov(f"Derived from the published grammar: every capability id is "
                                   f"verb.object.reach, and this node is what the id spells with."),
            }
            (OUT / f"lexicon/{folder}").mkdir(parents=True, exist_ok=True)
            (OUT / f"lexicon/{folder}/{n['label']}.json").write_text(
                json.dumps(rec, indent=2, ensure_ascii=False) + "\n")
            rows.append({"id": n["id"], "label": n["label"], "count": len(caps),
                         "file": f"lexicon/{folder}/{n['label']}.json"})
        lex_index[folder] = rows

    (OUT / "lexicon/index.json").write_text(json.dumps({
        "type": "abp/lexicon/v1",
        "_what_this_is": "Every word the capability grammar is spelled with, as a node with its "
                         "own address. `read.file.project` is not a string: it is three nodes "
                         "and three edges, and these are the nodes.",
        "grammar": "verb.object.reach",
        "counts": {k: len(v) for k, v in lex_index.items()},
        **lex_index,
        "provenance": prov("Generated from the published capability grammar."),
    }, indent=2, ensure_ascii=False) + "\n")

    # --- the graph ------------------------------------------------------------
    (OUT / "graph").mkdir(parents=True, exist_ok=True)
    (OUT / "graph/edges.json").write_text(json.dumps({
        "type": "abp/edge-vocabulary/v1",
        "_what_this_is": "Every edge this model is written in. Each is a verb with a DISTINCT, "
                         "meaningfully named inverse, a stated domain and range, and the "
                         "sentence it reads as. The inverse is not the same edge walked "
                         "backwards: it has different fan out, and that asymmetry is what stops "
                         "the graph exploding.",
        "the_banned_edge": "There is no generic association edge in this model and there will "
                           "not be one. It constrains nothing and costs fan out.",
        "extending_it": "A new edge needs a sentence, its inverse needs a DIFFERENT sentence, "
                        "and both need a stated domain and range.",
        "source": "https://graphs.sgit.ai/v1/grammar/edge-set.html",
        "count": len(G.EDGES),
        "universes": "Each edge names the universe of its domain and of its range, and "
                     "`crosses` is true when they differ: a junction edge, the property that "
                     "turns a set of graphs into a fractal rather than a pile. Computed from "
                     "the node types, never declared. See universes/index.json.",
        "edges": U.crossings(),
        "provenance": prov("Edges marked `graphs.sgit.ai edge set` are reused under their "
                           "published names. Edges marked `proposed here` are this site's, and "
                           "are marked as such rather than presented as settled."),
    }, indent=2, ensure_ascii=False) + "\n")

    (OUT / "graph/node-types.json").write_text(json.dumps({
        "type": "abp/node-types/v1",
        "_what_this_is": "A node type is a REQUIRED PATTERN OF TYPED, DIRECTED PATHS that a "
                         "node either matches or does not. It is not a label somebody applied. "
                         "The content of a node does not decide its type; its paths do.",
        "judgment": "Judgment does not disappear. Somebody still decided that a control must be "
                    "enforced from outside the grant. What changes is where that decision "
                    "lives: out of a classifier's head and into a formula that is visible, "
                    "versioned, inspectable and arguable.",
        "not_a_node": G.NOT_A_NODE.replace("**", ""),
        "count": len(G.NODE_TYPES),
        "universes": "Each type names the universe it belongs to, which is a modelling "
                     "decision made once in universes.py and checked by the gate: a type "
                     "with no universe is a node nobody owns.",
        "node_types": [{"name": n, "is": gl, "formula": f, "note": note,
                        "universe": U.universe_of_type(n),
                        "matched": len(cls.get(n, [])) if n in cls else None}
                       for n, gl, f, note in G.NODE_TYPES],
        "provenance": prov("The formulas are run against the graph on every build and the "
                           "`matched` counts are the result, not fields anybody set."),
    }, indent=2, ensure_ascii=False) + "\n")

    (OUT / "graph/nodes.json").write_text(json.dumps({
        "type": "abp/graph-nodes/v1",
        "_what_this_is": "Every node, flat, with its type. The same shape of record at every "
                         "altitude: a verb, a capability, a barrier and a deployment shape are "
                         "all nodes here. That is the GRAMMAR surviving every zoom, which is "
                         "the mechanism and not the claim: the claim is that a node opens into "
                         "a world with its own ontology, joined by a named edge, and which "
                         "universe each type belongs to is in universes/index.json. (Until "
                         "v0.4.1 this field stated the first edition's test, one format "
                         "everywhere, which scores decomposition as fractal.)",
        "count": len([n for n in g["nodes"].values() if n]),
        "by_type": {t: len([n for n in g["nodes"].values() if n and n["type"] == t])
                    for t in sorted({n["type"] for n in g["nodes"].values() if n})},
        "nodes": [n for n in g["nodes"].values() if n],
        "provenance": prov("Built from the published data on every build."),
    }, indent=2, ensure_ascii=False) + "\n")

    (OUT / "graph/index.json").write_text(json.dumps({
        "type": "abp/graph/v1",
        "_what_this_is": "The ABP as a graph. Meaning through connectivity: a node carries no "
                         "inherent meaning, and what a thing IS emerges from the edges "
                         "traceable from it.",
        "never_render_the_whole_graph": "Every page on this site renders the result of ONE "
                                        "query. There is no map of everything and there will "
                                        "not be one.",
        "files": {"nodes": "nodes.json", "edges": "edges.json",
                  "node_types": "node-types.json", "lexicon": "../lexicon/index.json",
                  "bridges": "../bridges/index.json"},
        "counts": {"nodes": len([n for n in g["nodes"].values() if n]),
                   "edges": len(g["edges"]),
                   "edge_types": len(G.EDGES), "node_types": len(G.NODE_TYPES)},
        "matched": {k: len(v) for k, v in cls.items()},
        "discipline": "https://graphs.sgit.ai/",
        "provenance": prov("Built from the published data on every build."),
    }, indent=2, ensure_ascii=False) + "\n")
    (OUT / "graph/graph.json").write_text(json.dumps({
        "type": "abp/graph-edges/v1",
        "_what_this_is": "Every edge instance, flat. Pair it with nodes.json to walk the graph.",
        "count": len(g["edges"]), "edges": g["edges"],
        "provenance": prov("Built from the published data on every build."),
    }, indent=2, ensure_ascii=False) + "\n")

    # --- the bridges ----------------------------------------------------------
    # Layer 3. It starts with one declared bridge, to the vocabulary this was promoted from,
    # because a bridge file with nothing in it teaches nobody the shape of one.
    (OUT / "bridges").mkdir(parents=True, exist_ok=True)
    (OUT / "bridges/index.json").write_text(json.dumps({
        "type": "abp/bridges/v1",
        "_what_this_is": "Declared bridges: explicit edges connecting this vocabulary to "
                         "another at specific points. Owned by whoever declared them and "
                         "revisable without renegotiating anything. The edge is `similar_to`, "
                         "it is symmetric, and it is PARTIAL ON PURPOSE.",
        "why_not_merge": "Merging two vocabularies erases the disagreement, and the "
                         "disagreement is the finding. Vocabularies are kept intact and "
                         "connected through anchor nodes. Parties can disagree about meaning "
                         "while still agreeing about facts, which is the only stable basis for "
                         "working together.",
        "not_a_conformance_claim": "A bridge is never `we are compliant with vocabulary X`. "
                                   "That is all or nothing and it is usually a lie by the "
                                   "second field.",
        "how_to_add_one": "A third party can declare a bridge without touching either node. You "
                          "do not need our permission and we do not need yours. Open a pull "
                          "request against this file with a source, a timestamp and a hash.",
        "count": 1,
        "bridges": [{
            "from": "abp.sgit.ai capability grammar",
            "edge": "similar_to",
            "to": "what-can-it-do.games.sgit.ai capability primitives",
            "relation": "identical at the time of promotion, by construction",
            "note": "This vocabulary was promoted from that one without renaming anything, so "
                    "the bridge is total rather than partial today. It is declared anyway, "
                    "because the two will diverge and the bridge is where that will be "
                    "recorded.",
            "declared_by": "abp.sgit.ai",
            "source": SOURCE,
            "retrieved": RETRIEVED,
            "content_hash": built["content_hash"],
        }],
        "provenance": prov("The bridge file. One declared bridge today."),
    }, indent=2, ensure_ascii=False) + "\n")
    return {"nodes": len([n for n in g["nodes"].values() if n]), "edges": len(g["edges"]),
            "lexicon": sum(len(v) for v in lex_index.values()), "matched": cls}


def main():
    version = (ROOT / "admin/build/version.txt").read_text().strip()
    built = build()
    deltas = write_deltas(built, RETRIEVED)
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import abp_pages  # noqa: E402
    write_facts(built, RETRIEVED, abp_pages.EXAMPLES)
    gr = write_graph(built, RETRIEVED)
    (OUT / "index.json").write_text(
        json.dumps(manifest(built, version, len(deltas)), indent=2, ensure_ascii=False) + "\n")
    print(f"promote_data: {built['capabilities']['count']} capabilities, "
          f"{len(built['profiles'])} profiles, {len(built['mandates'])} mandates, "
          f"{len(deltas)} stored deltas, {gr['nodes']} nodes and {gr['edges']} "
          f"edges, {gr['lexicon']} lexicon words, "
          f"{built['provenance']['rows']['measured']} of {built['provenance']['rows']['total']} "
          f"rows measured, {built['content_hash'][:19]}")


if __name__ == "__main__":
    main()
