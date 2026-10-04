#!/usr/bin/env python3
"""The gaps and requests register: what a behaviour policy wants and a product cannot enforce,
or cannot express, with who accepts the risk that leaves.

WHY A REGISTER. When a product cannot enforce a rule, somebody has to accept the risk, and
the acceptance is usually silent: it happens in the act of granting the connector. The
register makes it a row. Some gaps are so basic that the rule cannot even be written, which
is a finding in its own right and the first entry is one.

TWO KINDS OF ENTRY. `provider` entries are gaps in somebody's product, with the request to
them. `own` entries are gaps found in our own behaviour policies, where an agent's reach
exceeded its mandate, with what was done about it: the mandate widened, a barrier added, or
the risk accepted and by whom. The second kind is the honest half, and it lives on the same
page on purpose.

THE VOCABULARY IS THE SITE'S, AND THE CONTRIBUTOR'S IS KEPT BESIDE IT. The brief that asked
for this register uses four words for what barrier is possible: none, policy only, admin
setting, identity boundary. They are the four barriers under other names, so each entry
carries both: `barrier_possible` in the site's words, `barrier_possible_theirs` as written.
Nothing is merged.

ENTRIES ARE FILES, ONE EACH, under data/gaps/entries/. The index and the page are generated
from the files present, so adding an entry is adding a file, by pull request or by sending
the JSON. Every entry says who reported it and on what evidence tier; a register that scored
its own entries would be a verdict, and there is no score here.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shell  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ENTRIES = ROOT / "data" / "gaps" / "entries"
OUT = ROOT / "data" / "gaps"

FIELDS = ["id", "kind", "provider", "product", "gap", "abp_impact", "barrier_possible",
          "barrier_possible_theirs", "risk_to_accept", "evidence", "evidence_tier", "status",
          "first_seen", "reported_by", "request"]
STATUSES = ("open", "reported", "fixed", "accepted")
BARRIERS = ("none", "expectation", "setting", "boundary", "boundary, if built outside the "
            "platform", "not applicable")


def load():
    out = []
    for f in sorted(ENTRIES.glob("*.json")):
        e = json.loads(f.read_text())
        missing = [k for k in FIELDS if k not in e and not (k == "request" and e["kind"] == "own")]
        if missing:
            raise SystemExit(f"{f}: missing {missing}")
        if e["status"] not in STATUSES:
            raise SystemExit(f"{f}: status {e['status']} is not one of {STATUSES}")
        if e["barrier_possible"] not in BARRIERS:
            raise SystemExit(f"{f}: barrier_possible {e['barrier_possible']!r} is not in the "
                             f"declared set")
        if e["kind"] == "own" and "what_we_did" not in e:
            raise SystemExit(f"{f}: an own entry says what we did")
        e["file"] = f"gaps/entries/{f.name}"
        out.append(e)
    return out


def write(entries):
    by_provider = {}
    for e in entries:
        d = by_provider.setdefault(e["provider"], {"open": 0, "reported": 0, "fixed": 0,
                                                    "accepted": 0, "cannot_express": 0})
        d[e["status"]] += 1
        if e["barrier_possible"] == "none":
            d["cannot_express"] += 1
    idx = {
        "type": "abp/gaps-register/v1",
        "_what_this_is": "Gaps a behaviour policy finds in a product: a rule it wants that the "
                         "product cannot enforce or cannot express, who accepts the risk that "
                         "leaves, and the request to the provider. Plus gaps found in our own "
                         "behaviour policies and what was done about them. One file per entry "
                         "under gaps/entries/; this index is generated from the files present.",
        "how_to_add": "Add one JSON file to data/gaps/entries/ with the fields listed in "
                      "`fields`, by pull request to the repository or by sending the file to "
                      "the editor. Every entry names who reported it and the evidence tier it "
                      "rests on. No field is a score.",
        "fields": FIELDS + ["what_we_did (own entries)", "related (site paths, optional)"],
        "barrier_possible_values": list(BARRIERS),
        "status_values": list(STATUSES),
        "count": len(entries),
        "by_kind": {"provider": sum(1 for e in entries if e["kind"] == "provider"),
                    "own": sum(1 for e in entries if e["kind"] == "own")},
        "by_provider": by_provider,
        "entries": entries,
        "not_a_score": "A count of open entries per provider is a count. It says nothing about "
                       "whether any provider's product is acceptable for any deployment, "
                       "because acceptability is not in this register.",
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.json").write_text(json.dumps(idx, indent=2, ensure_ascii=False) + "\n")
    return idx


def _entry_blocks(e):
    rows = [
        ["**The gap**", shell.ascii_safe(e["gap"])],
        ["**What it does to an ABP**", shell.ascii_safe(e["abp_impact"])],
        ["**Barrier possible**", f"**{e['barrier_possible']}** (the contributor's word: "
                                 f"{e['barrier_possible_theirs']})"],
        ["**The risk, and who accepts it**", shell.ascii_safe(e["risk_to_accept"])],
    ]
    if e.get("what_we_did"):
        rows.append(["**What we did**", shell.ascii_safe(e["what_we_did"])])
    if e.get("request"):
        rows.append(["**Request to the provider**", shell.ascii_safe(e["request"])])
    rows += [
        ["**Evidence**", f"{shell.ascii_safe(e['evidence'])} *(tier: {e['evidence_tier']})*"],
        ["**Status**", f"{e['status']}, first seen {e['first_seen']}"],
    ]
    if e.get("related"):
        rows.append(["**On this site**", ", ".join(
            f"[{'/'.join(r.split('/')[:-1])}]({r})" for r in e["related"])])
    return [("h3", f"{e['id']}: {shell.ascii_safe(e['provider'])}, "
                   f"{shell.ascii_safe(e['product'])}"),
            ("table", ["", ""], rows)]


def pages():
    entries = load()
    idx = write(entries)
    prov = [e for e in entries if e["kind"] == "provider"]
    own = [e for e in entries if e["kind"] == "own"]
    cannot = [e for e in prov if e["barrier_possible"] == "none"]
    table = [[p, str(d["open"]), str(d["reported"]), str(d["fixed"]), str(d["cannot_express"])]
             for p, d in sorted(idx["by_provider"].items())]
    blocks = [
        ("crumb", "[Home](index.html) / The gaps register"),
        ("h1", "Gaps and requests: what a behaviour policy wants and a product cannot enforce"),
        ("lead", f"**{len(prov)} gaps in providers' products and {len(own)} in our own "
                 f"behaviour policies**, each with the rule it defeats, the barrier that is "
                 f"possible, the risk that leaves and who accepts it, and the request to "
                 f"whoever could close it. When a product cannot enforce a rule, somebody "
                 f"accepts the risk, usually silently and in the act of granting the "
                 f"connector. This register makes that a row."),
        ("note", f"**{len(cannot)} of the {len(prov)} provider gaps are ones where the rule "
                 f"cannot even be written.** No barrier of any kind is possible: not a "
                 f"setting, not a rule in prose. For those the ABP has no row to refuse, and "
                 f"the finding is that the rule cannot be expressed, which is worth more "
                 f"than a behaviour policy that pretends it can."),
        ("h2", "The register by provider"),
        ("table", ["Provider", "Open", "Reported", "Fixed", "Cannot be expressed"], table),
        ("p", "**A count is a count.** It says nothing about whether any product is acceptable "
              "for any deployment, because acceptability is not in this register. One of the "
              "providers is us."),
        ("h2", "How the contributor's words map onto the four barriers"),
        ("table", ["The brief says", "This site says", "What it means"], [
            ["none", "**none**", "nothing can stand in the way; the rule cannot be expressed"],
            ["policy only", "**expectation**", "a rule in prose, kept by a cooperative agent "
                                               "and by nothing else"],
            ["admin setting", "**setting**", "a switch the account can flip, which is not a "
                                             "control because the account can flip it back"],
            ["identity boundary", "**boundary**", "enforced by something the grant does not "
                                                  "include: a key the recipient holds, a lock "
                                                  "an administrator owns"],
        ]),
        ("p", "Both words are kept on every entry. Nothing is merged, which is the "
              "[three layers](model/graph/layers/index.html) rule applied to a register."),
        ("h2", f"Gaps in providers' products ({len(prov)})"),
    ]
    for e in prov:
        blocks += _entry_blocks(e)
    blocks += [
        ("h2", f"Gaps in our own behaviour policies ({len(own)})"),
        ("p", "The honest half. Places where one of our own agents' reach exceeded its "
              "mandate, and what was done: the mandate widened, a barrier added, or the risk "
              "accepted and by whom."),
    ]
    for e in own:
        blocks += _entry_blocks(e)
    blocks += [
        ("h2", "How to add an entry"),
        ("p", "One JSON file under [`data/gaps/entries/`](data/gaps/index.json), by pull "
              "request or sent to the editor, with the fields the index lists. Every entry "
              "says who reported it and the evidence tier it rests on; the index and this "
              "page are generated from the files present, so there is nothing else to edit."),
        ("note", "**Nothing on this page is an assessment, an audit, a certification or a "
                 "security review of any named product**, and no adjective here attaches to "
                 "one. Each entry is a rule somebody tried to write, the product's documented "
                 "or observed behaviour against it, and a request. The evidence tier on every "
                 "entry is the reporter's; this site did not test the provider gaps and says "
                 "so."),
        ("p", "[The register as JSON](data/gaps/index.json) &#183; "
              "[The four barriers](model/barriers/index.html) &#183; "
              "[The measured Gmail deployment](gmail/measured/index.html) &#183; "
              "[The cases](cases/index.html)"),
    ]
    return {"gaps/index.html": {
        "title": "The gaps register",
        "description": "Gaps a behaviour policy finds in providers' products, the rule each "
                       "defeats, who accepts the risk and the request to close it; and gaps "
                       "found in our own behaviour policies, with what was done about them.",
        "blocks": blocks,
    }}
