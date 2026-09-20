#!/usr/bin/env python3
"""The docs section: every reference and guidance document, rendered, one click from its bytes.

THIS IS NOT A MARKDOWN VIEWER, AND THE DISTINCTION MATTERS because the guidance is explicit
that markdown viewing, file trees and page layouts are platform provided and must not be
rebuilt. What this module does is a build-time translation from a markdown document into the
SAME small block vocabulary every other page on this site is written in -- headings,
paragraphs, lists, tables, block quotes, rules -- so that a document in `docs/` renders through
one shell rather than through a second one. There is no viewer shipped to a browser, no file
tree component and no layout engine. The constrained subset is the point: it is exactly the
constructs `shell.py` already emits, and a document that needs something outside it is a
document that wants rewriting.

The source bytes stay. Every rendered document carries a link to the `.md` it came from, in the
repository and served from this site, because anything rendered must stay one click from its
source bytes.

THE INDEX IS GENERATED FROM THE FILES PRESENT, never maintained by hand. An index that can
disagree with its source is a defect, so adding a document to `docs/briefs/` puts it in the
index, in `llms.txt` and in the sitemap with no second edit.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shell  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

# The sections, in reading order. The foundation document comes first everywhere it appears:
# it is the definition, the home page is derived from it, and where it and the pack disagree
# it wins.
SECTIONS = [
    ("briefs", "The briefs", "The foundation document first, then the three briefs behind it. "
                             "Published as written, with their own licence footers intact."),
    ("pack", "The pack", "The six numbered documents that settled what this site is, what it "
                         "must not invent, and the rules it is built under."),
    ("research", "The research", "External readings of the ideas this site is built on, "
                                 "published as received and followed by this site's reading of "
                                 "each: what the reading changes here, what it does not, and "
                                 "every reference resolved on the day."),
]
FOUNDATION = "v0.33.70__foundation__agent-behaviour-policy-you-know-what-you-asked-for-and-you-do-not-know-what-it-can-do"

GUIDANCE = [
    ("The vault and site building guidance", "https://sgit.ai/docs/guidance/index.html",
     "11 September 2026",
     "Pick your surface first. Do not build what the platform already has. Publish a read key, "
     "never a vault key. Version everything and show the version. Anything rendered must stay "
     "one click from the source bytes."),
    ("What the platform site is, for agents", "https://sgit.ai/llms.txt", "11 September 2026",
     "How the network is organised, and the index every site in it publishes."),
    ("The style guide, with measured compliance", "https://coding.sgit.ai/", "11 September 2026",
     "Thirty one rules, and honest about its own enforcement: no linters, and four structural "
     "guards in the pipeline are the only automated enforcement."),
    ("The five graph rules", "https://graphs.sgit.ai/", "11 September 2026",
     "They govern the model rather than the styling. This site's reading of them is on "
     "[the graph page](model/graph/index.html)."),
    ("The capability map this site's data came from",
     "https://what-can-it-do.games.sgit.ai/map/index.html", "11 September 2026",
     "Twenty three primitives, nine profiles, the barrier glyph and the undo class. The "
     "ontology this site promoted rather than invented."),
]


# ---------------------------------------------------------------------------
# markdown -> the block vocabulary
# ---------------------------------------------------------------------------

def to_blocks(text, source_href, source_label):
    """A markdown document as shell blocks. Deliberately small: what is not handled here is
    passed through as a paragraph rather than silently dropped."""
    lines = text.replace("\r\n", "\n").split("\n")
    blocks, i, title = [], 0, None
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        # The document's own h1 becomes the page title rather than a second heading.
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            i += 1
            continue
        if line.startswith("### "):
            blocks.append(("h3", _inline(line[4:].strip())))
            i += 1
        elif line.startswith("## "):
            blocks.append(("h2", _inline(line[3:].strip())))
            i += 1
        elif line.startswith("# "):
            blocks.append(("h2", _inline(line[2:].strip())))
            i += 1
        elif line.startswith("```"):
            buf, i = [], i + 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            blocks.append(("pre", "\n".join(buf)))
        elif line.lstrip().startswith("|") and i + 1 < len(lines) and _is_rule(lines[i + 1]):
            head = _cells(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([_inline(c) for c in _cells(lines[i])])
                i += 1
            width = len(head)
            rows = [(r + [""] * width)[:width] for r in rows]
            blocks.append(("table", [_inline(h) for h in head], rows))
        elif line.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            blocks.append(("note", _inline(" ".join(x for x in buf if x))))
        elif re.match(r"^\s*[-*]\s+", line):
            buf = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append(_inline(re.sub(r"^\s*[-*]\s+", "", lines[i])))
                i += 1
            blocks.append(("ul", buf))
        elif re.match(r"^\s*\d+\.\s+", line):
            buf = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append(_inline(re.sub(r"^\s*\d+\.\s+", "", lines[i])))
                i += 1
            blocks.append(("ol", buf))
        elif set(line.strip()) == {"-"} and len(line.strip()) >= 3:
            i += 1  # a horizontal rule is structure the shell expresses with headings
        else:
            # A line that LOOKS like a block start but matched none of the branches above --
            # a lone table row separated from its header, most often. Take it as a paragraph
            # rather than dropping it, and always consume at least one line: a branch that can
            # decline to advance is a branch that can hang the build, and this one did.
            buf = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not _starts_block(lines[i]):
                buf.append(lines[i].strip())
                i += 1
            blocks.append(("p", _inline(" ".join(buf))))
    src = ("note", f"**The source bytes.** This page is generated from "
                   f"[`{source_label}`]({source_href}), which is served unchanged. Anything "
                   f"rendered on this network stays one click from the file it came from.")
    return title, [src] + blocks


def _starts_block(line):
    return (line.startswith(("#", ">", "```")) or line.lstrip().startswith("|")
            or re.match(r"^\s*([-*]\s+|\d+\.\s+)", line)
            or (set(line.strip()) == {"-"} and len(line.strip()) >= 3))


def _is_rule(line):
    s = line.strip()
    return s.startswith("|") and set(s) <= set("|-: ")


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


# A markdown link to a sibling document becomes a link to that document's PAGE, so the docs
# section is navigable rather than a pile of downloads.
_DOCLINK = re.compile(r"`(\d\d__[A-Z-]+)\.md`")


def _inline(s):
    s = shell.ascii_safe(s)
    s = _DOCLINK.sub(lambda m: f"[`{m.group(1)}.md`](docs/pack/{m.group(1)}/index.html)", s)
    # A table cell cannot carry a pipe, and the shell's table renderer splits on nothing, so
    # this is about the markdown twin rather than the HTML.
    return s.replace("|", "&#124;") if False else s


# ---------------------------------------------------------------------------
# the pages
# ---------------------------------------------------------------------------

def _slug(p):
    return p.stem


def _found(section):
    """The files present, which is what the index is generated from."""
    d = DOCS / section
    if not d.exists():
        return []
    files = sorted(d.glob("*.md"))
    if section == "briefs":
        files.sort(key=lambda p: (p.stem != FOUNDATION, p.stem))
    return files


def pages():
    out, listing = {}, {}
    for section, heading, blurb in SECTIONS:
        rows = []
        for f in _found(section):
            slug = _slug(f)
            rel = f"docs/{section}/{slug}/index.html"
            href = f"docs/{section}/{slug}.md"
            title, blocks = to_blocks(f.read_text(), href, f"docs/{section}/{f.name}")
            summary = _summary(blocks)
            out[rel] = {
                "title": shell.ascii_safe(title or slug),
                "description": summary,
                "blocks": [("crumb", f"[Home](index.html) / [Docs](docs/index.html) / "
                                     f"[{heading}](docs/index.html#{section}) / "
                                     f"{shell.ascii_safe(title or slug)}"),
                           ("h1", shell.ascii_safe(title or slug))] + blocks,
            }
            rows.append((rel, shell.ascii_safe(title or slug), summary, href,
                         f.stat().st_size))
        listing[section] = rows

    cards = []
    for section, heading, blurb in SECTIONS:
        for rel, title, summary, href, size in listing[section]:
            cards.append({"title": f"[{title}]({rel})", "sub": summary,
                          "foot": f"[the source bytes]({href}) · {size // 1024 or 1} KB"})

    out["docs/index.html"] = {
        "title": "Docs",
        "description": "Every reference and guidance document behind this site, rendered, with "
                       "a link to the source bytes of each. The index is generated from the "
                       "files present.",
        "blocks": [
            ("crumb", "[Home](index.html) / Docs"),
            ("h1", "Docs"),
            ("lead", "Everything this site was built from, published rather than summarised. "
                     "**The foundation document is first**: it is the definition of the Agent "
                     "Behaviour Policy, the home page is derived from it, and where it and "
                     "anything else here disagree, it wins."),
            ("note", "**This index is generated from the files present in `docs/`, not "
                     "maintained beside them.** An index that can disagree with its source is a "
                     "defect. Adding a document to the repository puts it here, in `llms.txt` "
                     "and in the sitemap with no second edit."),
        ] + _section_blocks(listing) + [
            ("h2", "Inherited guidance"),
            ("p", "**Link, do not copy.** These are the published sources this site is built "
                  "under. Where a rule is quoted on a page it is quoted with its source; "
                  "nothing here is a copy of somebody else's document kept in this repository "
                  "to go stale."),
            ("table", ["Source", "Read", "What it governs"],
             [[f"[{t}]({u})", d, b] for t, u, d, b in GUIDANCE]),
            ("h2", "One document is quoted and never copied"),
            ("note", "**The international management standards are not reproduced here, in any "
                     "form.** Their titles may be named. Adapting, translating or quoting them "
                     "at length is prohibited, and so is feeding them to a model. Where a "
                     "mapping is wanted, the European regulation is expressly reusable for "
                     "commercial purposes including adaptation, and it is the clean source."),
            ("p", "[Everything on this site, in one file](llms-full.txt) · "
                  "[The index for agents](llms.txt)"),
        ]}
    return out


def _section_blocks(listing):
    blocks = []
    for section, heading, blurb in SECTIONS:
        rows = listing.get(section, [])
        blocks += [("h2", heading), ("p", blurb),
                   ("cards", [{"title": f"[{t}]({rel})", "sub": s,
                               "foot": f"[the source bytes]({h})"}
                              for rel, t, s, h, _ in rows])]
    return blocks


def _summary(blocks):
    """The document's own first paragraph, trimmed. Generated rather than written, so it cannot
    describe a document that has since changed."""
    for kind, *args in blocks:
        if kind == "p" and isinstance(args[0], str) and len(args[0]) > 60:
            s = shell.strip(args[0])
            return (s[:240].rsplit(" ", 1)[0] + "...") if len(s) > 240 else s
    return "A reference document behind this site."
