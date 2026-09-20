#!/usr/bin/env python3
"""The article figures: diagrams of the mechanisms, and one chart of the releases.

TWO KINDS AND ONE RULE EACH.

A DIAGRAM here shows a mechanism rather than decorating a paragraph: boxes for the nodes,
named edges between them, and where a path is the point, the sentence the path reads as,
written under it. If a figure would only repeat a sentence already on the page, it is not
here. Every one is inline SVG in the page's own stylesheet, so it prints, it scales, and it
carries no request to anybody else's server.

The CHART is small multiples, one series per panel, because the four measures have different
scales and a second y axis would be a lie about both. Its two colours are the only ones in
this repository chosen by a validator rather than by eye: teal and the house amber pass the
lightness band, the chroma floor, colour-vision separation, the normal-vision floor and
contrast against both surfaces. Text never wears them; identity comes from the mark beside it.

EVERY FIGURE HAS A MARKDOWN EQUIVALENT rather than being dropped from the twin. A `both`
block carries the SVG for the page and a bracketed description for the twin, in the same
form the grant-against-mandate figure has used since v0.1.0. A reader of the markdown gets
the figure's content in words; nothing is gated behind the picture.

NO SCORE IN ANY OF THEM. No severity axis, no ranking, no size standing in for consequence.
The one ordering that appears is irreversible first, which is a property of the action.
"""

W = 960


def _svg(body, h, cls="fig"):
    return (f'<svg class="{cls}" viewBox="0 0 {W} {h}" role="img" '
            f'preserveAspectRatio="xMidYMid meet">{body}</svg>')


def fig(svg, caption, md):
    """A figure block: the SVG for the page, a described equivalent for the markdown twin."""
    return ("both",
            f'<figure class="fig">{svg}<figcaption>{caption}</figcaption></figure>',
            f"*[{md}]*")


def _box(x, y, w, h, label, sub=None, cls="box", mono=False, r=9):
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="{cls}"/>'
    lc = "fm" if mono else "fb"
    ly = y + (h / 2 + 4 if not sub else h / 2 - 4)
    t += f'<text x="{x + w / 2}" y="{ly}" text-anchor="middle" class="{lc}">{label}</text>'
    if sub:
        t += (f'<text x="{x + w / 2}" y="{y + h / 2 + 12}" text-anchor="middle" '
              f'class="fd">{sub}</text>')
    return t


def _arrow(x1, y1, x2, y2, label=None, cls="edge", dy=-6, curve=0):
    if curve:
        d = f"M {x1} {y1} C {x1 + curve} {y1}, {x2 - curve} {y2}, {x2} {y2}"
    else:
        d = f"M {x1} {y1} L {x2} {y2}"
    t = f'<path d="{d}" class="{cls}" marker-end="url(#ah{"a" if cls.endswith("-a") else ""})"/>'
    if label:
        if x1 == x2:
            # A VERTICAL EDGE CARRIES ITS LABEL BESIDE IT, never across it. Centred on the
            # arrow, the text lands under the box the arrow points at, and SVG paints the box
            # last, so the label disappears behind it. That happened, and this is the fix.
            t += (f'<text x="{x1 + 10}" y="{(y1 + y2) / 2 + 4}" class="fmd">{label}</text>')
        else:
            t += (f'<text x="{(x1 + x2) / 2}" y="{(y1 + y2) / 2 + dy}" text-anchor="middle" '
                  f'class="fmd">{label}</text>')
    return t


DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        'markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#d5d0c2"/></marker>'
        '<marker id="aha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        'markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#0b8f80"/></marker></defs>')


# ---------------------------------------------------------------------------
# the chart: four measures across eight releases, as small multiples
# ---------------------------------------------------------------------------

RELEASES = ["v0.1.0", "v0.2.0", "v0.3.0", "v0.4.0", "v0.4.1", "v0.4.2", "v0.4.3", "v0.4.4"]

PANELS = [
    ("Pages", [52, 55, 93, 95, 111, 112, 113, 114], None,
     "every one generated, every one with a markdown twin"),
    ("Nodes in the graph", [None, None, 170, 170, 170, 170, 216, 369], 2,
     "no graph before v0.3.0: the words were substrings"),
    ("Edges in the graph", [None, None, 488, 488, 488, 488, 658, 993], 2,
     "each one a verb with a distinct inverse"),
    ("Checks in the release gate", [10, 10, 11, 11, 12, 13, 13, 13], None,
     "a failure means no tag and no publish"),
]


def _panel(x, y, title, values, start, note):
    pw, ph = 392, 104
    px, py = x + 6, y + 34
    pts = [v for v in values if v is not None]
    top = max(pts)
    n = len(values)
    step = pw / (n - 1)
    sx = lambda i: px + i * step
    sy = lambda v: py + ph - (v / top) * (ph - 10)
    out = [f'<text x="{x}" y="{y + 12}" class="fh">{title}</text>',
           f'<text x="{x}" y="{y + 27}" class="fk">{note}</text>',
           f'<line x1="{px}" y1="{py}" x2="{px + pw}" y2="{py}" class="grid"/>',
           f'<line x1="{px}" y1="{py + ph}" x2="{px + pw}" y2="{py + ph}" class="grid"/>']
    # No label on the top gridline. It sits at the maximum, the maximum is the last value in
    # every one of these panels, and the last value is already labelled at the dot: printing
    # it twice is a number the reader has to reconcile for nothing.
    if top != values[-1]:
        out.append(f'<text x="{px + pw + 6}" y="{py + 4}" class="fd">{top:,}</text>')
    i0 = start or 0
    d = " ".join(("M" if i == i0 else "L") + f" {sx(i):.1f} {sy(values[i]):.1f}"
                 for i in range(i0, n))
    out.append(f'<path d="{d}" class="ser"/>')
    if start:
        out.append(f'<line x1="{px}" y1="{py + ph}" x2="{sx(start):.1f}" y2="{py + ph}" '
                   f'class="grid" stroke-dasharray="3 3"/>')
    out.append(f'<circle cx="{sx(n - 1):.1f}" cy="{sy(values[-1]):.1f}" r="4" class="dot"/>')
    out.append(f'<circle cx="{sx(i0):.1f}" cy="{sy(values[i0]):.1f}" r="3" class="dot"/>')
    out.append(f'<text x="{sx(n - 1):.1f}" y="{sy(values[-1]) - 10:.1f}" text-anchor="end" '
               f'class="fb">{values[-1]:,}</text>')
    out.append(f'<text x="{sx(i0):.1f}" y="{sy(values[i0]) + 16:.1f}" class="fd">'
               f'{values[i0]:,}</text>')
    for i, r in enumerate(RELEASES):
        if i in (0, 2, n - 1):
            out.append(f'<text x="{sx(i):.1f}" y="{py + ph + 15}" text-anchor="middle" '
                       f'class="fmd">{r}</text>')
        else:
            out.append(f'<line x1="{sx(i):.1f}" y1="{py + ph}" x2="{sx(i):.1f}" '
                       f'y2="{py + ph + 3}" class="grid"/>')
    return "".join(out)


def evolution():
    body = [DEFS]
    for i, (t, v, s, n) in enumerate(PANELS):
        body.append(_panel(24 + (i % 2) * 486, 16 + (i // 2) * 176, t, v, s, n))
    rows = ", ".join(f"{r} {PANELS[0][1][i]}" for i, r in enumerate(RELEASES))
    return fig(
        _svg("".join(body), 364),
        "Four measures across eight releases, as small multiples: each panel keeps its own "
        "scale, because the numbers are not comparable to each other and one axis carrying "
        "both would say something untrue about both. The dashed run on the middle two panels "
        "is the releases before the graph existed, which is an absence rather than a zero.",
        "A chart here in the page: four small line panels, one per measure, across the eight "
        f"releases. Pages: {rows}. Nodes in the graph: none before v0.3.0, then 170 at "
        "v0.3.0 through v0.4.2, 216 at v0.4.3 and 369 at v0.4.4. Edges in the graph: none "
        "before v0.3.0, then 488 through v0.4.2, 658 at v0.4.3 and 993 at v0.4.4. Checks in "
        "the release gate: 10, 10, 11, 11, 12, 13, 13, 13. Each panel keeps its own scale")


def shapes_split():
    x, y, bw = 24, 46, 640
    total, promoted, contributed = 16, 9, 7
    wA = bw * promoted / total - 1
    wB = bw * contributed / total - 1
    body = [
        f'<text x="24" y="20" class="fh">Where the 16 deployment shapes came from</text>',
        f'<text x="24" y="36" class="fk">the two sets are counted beside each other, never '
        f'folded together</text>',
        f'<rect x="{x}" y="{y}" width="{wA:.1f}" height="34" rx="4" class="barA"/>',
        f'<rect x="{x + wA + 2:.1f}" y="{y}" width="{wB:.1f}" height="34" rx="4" class="barB"/>',
        f'<rect x="24" y="{y + 54}" width="11" height="11" rx="2" class="barA"/>',
        f'<text x="41" y="{y + 64}" class="ft"><tspan class="fb">9 shapes, 62 rows</tspan> '
        f'promoted from the published capability map, retrieved 11 September</text>',
        f'<rect x="24" y="{y + 76}" width="11" height="11" rx="2" class="barB"/>',
        f'<text x="41" y="{y + 86}" class="ft"><tspan class="fb">7 shapes, 37 rows</tspan> '
        f'contributed by riskmandate.ai, fetched 20 September</text>',
    ]
    return fig(_svg("".join(body), 148),
               "One bar, two segments, separated by a 2px gap in the surface colour rather "
               "than by a border, and no text inside either fill. The count is the only thing "
               "encoded: there is no ordering here and no axis of consequence.",
               "A figure here in the page: one bar split into 9 shapes promoted from the "
               "published capability map, carrying 62 rows, and 7 shapes contributed by "
               "riskmandate.ai, carrying 37 rows. The two sets are counted beside each other "
               "and never folded together")


# ---------------------------------------------------------------------------
# the diagrams
# ---------------------------------------------------------------------------

def four_objects():
    """v0.1.0. The four objects are neighbours, and the delta is the one nobody writes."""
    y, bh, bw = 58, 62, 200
    xs = [24, 254, 484, 714]
    body = [DEFS,
            '<text x="24" y="22" class="fh">The four objects of an Agent Behaviour Policy</text>',
            '<text x="24" y="40" class="fk">side by side, not a stack: the mandate is not '
            'above the grant</text>']
    for x, (t, how, note, cls) in zip(xs, [
            ("The mandate", "elicited", "what you authorised", "box"),
            ("The grant", "measured", "what it can do", "box"),
            ("The delta", "derived", "the difference", "box-a"),
            ("The barrier", "recorded", "what is in the way", "box")]):
        body.append(_box(x, y, bw, bh, t, None, cls))
        body.append(f'<text x="{x + bw / 2}" y="{y + 30}" text-anchor="middle" class="fmd">'
                    f'{how}</text>')
        body.append(f'<text x="{x + bw / 2}" y="{y + 48}" text-anchor="middle" class="fd">'
                    f'{note}</text>')
    body += [
        f'<path d="M {xs[0] + bw / 2} {y + bh} L {xs[0] + bw / 2} {y + bh + 34} '
        f'L {xs[2] + bw / 2} {y + bh + 34} L {xs[2] + bw / 2} {y + bh + 8}" class="edge-a" '
        f'marker-end="url(#aha)"/>',
        f'<path d="M {xs[1] + bw / 2} {y + bh} L {xs[1] + bw / 2} {y + bh + 20} '
        f'L {xs[2] + bw / 2} {y + bh + 20}" class="edge-a"/>',
        f'<text x="{xs[1] + bw / 2 + 40}" y="{y + bh + 50}" class="fmd">derived from both, '
        f'and never authored</text>',
        f'<path d="M {xs[3] + bw / 2} {y + bh} L {xs[3] + bw / 2} {y + bh + 34} '
        f'L {xs[2] + bw + 14} {y + bh + 34}" class="edge"/>',
        f'<text x="{xs[3] - 6}" y="{y + bh + 68}" text-anchor="end" class="fd">one per '
        f'granted capability</text>',
        f'<text x="24" y="{y + bh + 92}" class="ft"><tspan class="fb">Three hundred and '
        f'forty things is a shrug.</tspan> Three hundred and forty things and you authorised '
        f'twelve is a finding.</text>',
    ]
    return fig(_svg("".join(body), 240),
               "The order they are produced in is the order the model page teaches them. The "
               "delta has two arrows into it and no hand: it is the output of a computation "
               "over the other two, stored with both versions pinned.",
               "A figure here in the page: the four objects of an ABP drawn side by side "
               "rather than stacked. The mandate is elicited, the grant is measured, the "
               "delta is derived from both and never authored, and the barrier is recorded "
               "once per granted capability. Arrows run from the mandate and the grant into "
               "the delta")


def barrier_ladder():
    """v0.1.0. Four barriers, one enforcer test, and the line that decides."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">Four kinds of barrier, and the one line that '
            'decides</text>',
            '<text x="24" y="40" class="fk">a control bounds a grant only if it is enforced '
            'by something the grant does not include</text>']
    rows = [("none", "nothing is in the way", "-", "no"),
            ("expectation", "a rule in prose", "the agent reading it", "no"),
            ("setting", "a switch the account can flip", "the agent's own account", "no"),
            ("boundary", "enforced above the grant", "something above the grant", "yes")]
    y0 = 62
    for i, (bid, what, enf, ctl) in enumerate(rows):
        y = y0 + i * 44
        inside = ctl == "no"
        body += [
            f'<rect x="24" y="{y}" width="330" height="34" rx="8" '
            f'class="{"box" if inside else "box-a"}"/>',
            f'<text x="40" y="{y + 15}" class="fm">{bid}</text>',
            f'<text x="40" y="{y + 28}" class="fd">{what}</text>',
            _arrow(360, y + 17, 452, y + 17, "enforced_by", dy=-5),
            f'<rect x="458" y="{y}" width="250" height="34" rx="8" '
            f'class="{"box" if inside else "box-a"}"/>',
            f'<text x="583" y="{y + 21}" text-anchor="middle" class="ft">{enf}</text>',
            f'<text x="730" y="{y + 21}" class="{"fd" if inside else "fb"}">'
            f'{"inside the grant" if inside else "outside the grant"}</text>',
        ]
    body += [
        f'<line x1="716" y1="{y0 - 10}" x2="716" y2="{y0 + 3 * 44 - 8}" class="rule" '
        f'stroke-dasharray="4 3"/>',
        f'<rect x="24" y="{y0 + 4 * 44 + 6}" width="684" height="30" rx="8" class="box-x"/>',
        f'<text x="40" y="{y0 + 4 * 44 + 26}" class="ft">Only the fourth row bounds anything, '
        f'and the site fails to build if that stops being true.</text>',
    ]
    return fig(_svg("".join(body), 290),
               "The test is not an opinion about the four rows. It is a path: follow "
               "enforced_by and ask whether the thing at the other end is inside the grant. "
               "Three of the four are, which is why three of the four bound nothing.",
               "A figure here in the page: the four barriers, each with an enforced_by edge "
               "to what enforces it. Nothing is enforced by nothing; an expectation by the "
               "agent reading it; a setting by the agent's own account; and a boundary by "
               "something above the grant. The first three enforcers are inside the grant "
               "and bound nothing. Only the boundary is outside it")


def string_vs_nodes():
    """v0.3.0. The same primitive before and after the words got addresses."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">What changed when a word got an address</text>',
            '<text x="24" y="40" class="fk">the gloss did not go away; it stopped being the '
            'definition</text>',
            '<text x="24" y="70" class="fd">Until v0.2.0</text>',
            '<text x="500" y="70" class="fd">From v0.3.0</text>']
    body += [
        _box(24, 84, 420, 56, "read.file.project", "a string, with a gloss beside it",
             "box-x", mono=True),
        f'<text x="234" y="162" text-anchor="middle" class="fk">nothing can link to `read`, '
        f'so nothing can disagree with it</text>',
    ]
    cx = 640
    body += [_box(cx - 130, 84, 260, 34, "read.file.project", None, "box-a", mono=True)]
    for i, (w, e) in enumerate([("read", "has_verb"), ("file", "acts_on"),
                                ("project", "reaches")]):
        x = 500 + i * 140
        body += [
            f'<path d="M {cx} 118 C {cx} 140, {x + 56} 130, {x + 56} 150" class="edge-a" '
            f'marker-end="url(#aha)"/>',
            f'<text x="{x + 56}" y="{144 if i != 1 else 136}" text-anchor="middle" '
            f'class="fmd">{e}</text>',
            _box(x, 152, 112, 30, w, None, "box-a", mono=True),
            f'<text x="{x + 56}" y="197" text-anchor="middle" class="fk">a node, a page, '
            f'a file</text>',
        ]
    body.append('<text x="24" y="222" class="ft"><tspan class="fb">A node carries no inherent '
                'meaning.</tspan> What a primitive is emerges from the edges traceable from '
                'it, which is why the reach pages can hold nine disagreeing definitions of '
                '`host` without averaging them.</text>')
    return fig(_svg("".join(body), 240),
               "Three nodes and three edges, each with its own address, its own JSON file and "
               "its own page. The left hand side is not wrong, it is unaddressable: a reader "
               "who disagrees with what `host` means has nothing to point at.",
               "A figure here in the page: on the left, read.file.project as one string with "
               "a gloss beside it, the shape until v0.2.0. On the right, the same primitive "
               "as a node joined by has_verb to `read`, by acts_on to `file` and by reaches "
               "to `project`, each of which is a node with a page and a file of its own")


def zoom_test():
    """v0.4.0. The corrected test, in two halves."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">The zoom test, in two halves</text>',
            '<text x="24" y="40" class="fk">what survives every zoom is the grammar; the '
            'ontology is meant to change</text>']
    left = [("document", "contains"), ("section", "contains"), ("block", "contains"),
            ("sentence", "contains"), ("word", None)]
    for i, (w, e) in enumerate(left):
        y = 70 + i * 54
        body.append(_box(60, y, 180, 32, w, None, "box", mono=True))
        if e:
            body.append(_arrow(150, y + 33, 150, y + 52, e))
    body += [
        '<text x="150" y="70" text-anchor="middle" class="fd" dy="-12">One vocabulary</text>',
        f'<text x="150" y="{70 + 5 * 54 - 12}" text-anchor="middle" class="fb">a hierarchy</text>',
        f'<text x="150" y="{70 + 5 * 54 + 6}" text-anchor="middle" class="fk">very good '
        f'addressing, and not the claim</text>',
    ]
    right = [("a capability", "its own types: verb, object, reach", "granted_by"),
             ("a deployment shape", "the vendor's words: tools, scopes, settings", "bounded_by"),
             ("a barrier", "enforcers, layers, parties", "licensed_under"),
             ("a licence condition", "authority, interval, a named owner", None)]
    for i, (w, o, e) in enumerate(right):
        y = 70 + i * 66
        body.append(_box(440, y, 420, 42, w, o, "box-a"))
        if e:
            body.append(_arrow(650, y + 43, 650, y + 66, e, cls="edge-a"))
    body += [
        '<text x="650" y="58" text-anchor="middle" class="fd">A new ontology at every '
        'step, joined by a named edge</text>',
        f'<text x="650" y="{70 + 4 * 66 - 2}" text-anchor="middle" class="fb">the claim '
        f'working</text>',
        f'<line x1="350" y1="56" x2="350" y2="{70 + 4 * 66}" class="rule" '
        f'stroke-dasharray="4 3"/>',
    ]
    return fig(_svg("".join(body), 356),
               "The first edition of the claim said one grammar and one schema everywhere, "
               "which scores the left hand side as a pass. The corrected test asks the "
               "harder question, and the left hand side is a folder tree with very good "
               "addressing.",
               "A figure here in the page: on the left, a chain from document to section to "
               "block to sentence to word, every step a contains edge in one vocabulary, "
               "which is a hierarchy. On the right, a chain from a capability to a deployment "
               "shape to a barrier to a licence condition, where each step lands in a world "
               "with its own node types and is joined by a named edge, which is the fractal "
               "claim working")


def nine_universes():
    """v0.4.0 and v0.4.1. One row, nine worlds, nine owners, one grammar."""
    U = [("0", "The source bytes", "nobody", "hashed_from"),
         ("1", "The grammar", "this site", "granted_by"),
         ("2", "The deployment shape", "the vendor's words", "grants"),
         ("3", "The grant and its evidence", "whoever observed", "bounded_by"),
         ("4", "The enforcement", "whoever set it", "authorised_by"),
         ("5", "The deployer", "the deployer", "derived_into"),
         ("6", "The derivation", "the computation", "projected_as"),
         ("7", "The projections", "the renderer", "licensed_under"),
         ("8", "The licence and the risk", "riskmandate.ai", None)]
    body = [DEFS,
            '<text x="24" y="22" class="fh">One capability row, nine universes</text>',
            '<text x="24" y="40" class="fk">each with its own owner and its own node types, '
            'sharing only the grammar</text>']
    for i, (n, name, owner, edge) in enumerate(U):
        y = 62 + i * 50
        mine = owner == "this site"
        body += [
            f'<text x="24" y="{y + 22}" class="fmd">u{n}</text>',
            f'<rect x="52" y="{y}" width="300" height="32" rx="8" '
            f'class="{"box-a" if mine else "box"}"/>',
            f'<text x="66" y="{y + 21}" class="ft">{name}</text>',
            f'<text x="368" y="{y + 21}" class="fd">owned by {owner}</text>',
        ]
        if edge:
            body += [
                f'<path d="M 202 {y + 33} L 202 {y + 48}" class="edge-a" '
                f'marker-end="url(#aha)"/>',
                f'<text x="214" y="{y + 45}" class="fmd">{edge}</text>',
            ]
    body += [
        f'<line x1="600" y1="56" x2="600" y2="{62 + 9 * 50 - 22}" class="rule" '
        f'stroke-dasharray="4 3"/>',
        '<text x="620" y="76" class="fb">What is shared</text>',
        '<text x="620" y="96" class="ft">every edge a verb with an inverse</text>',
        '<text x="620" y="114" class="ft">meaning in connectivity</text>',
        '<text x="620" y="132" class="ft">supersede, never delete</text>',
        '<text x="620" y="150" class="ft">provenance on every claim</text>',
        '<text x="620" y="186" class="fb">What is not</text>',
        '<text x="620" y="206" class="ft">the node types</text>',
        '<text x="620" y="224" class="ft">the verbs</text>',
        '<text x="620" y="242" class="ft">the taxonomy</text>',
        '<text x="620" y="260" class="ft">who decides any of it</text>',
        '<text x="620" y="296" class="fk">Nothing is merged, and</text>',
        '<text x="620" y="312" class="fk">nothing asks permission.</text>',
        '<text x="620" y="344" class="fd">Levels run up and down.</text>',
        '<text x="620" y="360" class="fd">Universes run across.</text>',
    ]
    return fig(_svg("".join(body), 508),
               "The walk on the site is built from the published data on every build, so the "
               "sentence it reads as cannot drift from the rows it is made of. Only one of "
               "the nine worlds belongs to this site.",
               "A figure here in the page: nine universes stacked in the order one capability "
               "row crosses them, from the source bytes owned by nobody, through the grammar "
               "owned by this site, the deployment shape in the vendor's words, the grant and "
               "its evidence, the enforcement, the deployer, the derivation, the projections, "
               "and up into the licence and the risk owned by riskmandate.ai. Each pair is "
               "joined by a named edge. What is shared between them is the grammar; what is "
               "not shared is the node types, the verbs, the taxonomy and who decides them")


def fact_diff():
    """v0.4.2. The diff runs over the published page, not over the generator."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">The fact diff, and why it reads the published '
            'page</text>',
            '<text x="24" y="40" class="fk">a diff that trusted the generator would be a diff '
            'over nothing</text>',
            _box(24, 64, 200, 44, "the grant", "a deployment shape", "box"),
            _box(24, 120, 200, 44, "the mandate", "what was authorised", "box"),
            _arrow(224, 86, 292, 108, None, cls="edge-a"),
            _arrow(224, 142, 292, 120, None, cls="edge-a"),
            _box(296, 90, 190, 44, "the fact set", "leaf assertions", "box-a"),
            f'<text x="300" y="152" class="fk">computed, never '
            f'authored</text>',
            _box(296, 192, 190, 44, "the label", "nine fields", "box"),
            _box(296, 248, 190, 44, "the leaflet", "every row", "box"),
            _box(296, 304, 190, 44, "the prohibitions", "one per excess row", "box"),
            _box(296, 360, 190, 44, "the figure", "three counts", "box"),
            f'<path d="M 391 134 L 391 192" class="edge-a" marker-end="url(#aha)"/>',
            f'<text x="400" y="172" class="fmd">projects</text>',
            _arrow(486, 214, 560, 214, None),
            _arrow(486, 270, 560, 258, None),
            _arrow(486, 326, 560, 300, None),
            _arrow(486, 382, 560, 344, None),
            _box(564, 190, 180, 176, "the published page", "and its markdown twin", "box"),
            _arrow(744, 278, 812, 278, None, cls="edge-a"),
            _box(816, 250, 120, 56, "the gate", "parses it back", "box-a"),
            f'<path d="M 876 250 C 876 180, 600 150, 490 118" class="edge-a" '
            f'marker-end="url(#aha)"/>',
            f'<text x="700" y="158" text-anchor="middle" class="fmd">compares, assertion by '
            f'assertion</text>',
            f'<text x="816" y="330" class="fb">One row that differs</text>',
            f'<text x="816" y="348" class="fb">fails the build.</text>',
            f'<text x="24" y="192" class="ft"><tspan class="fb">The facts are the leaf '
            f'assertions.</tspan></text>',
            f'<text x="24" y="212" class="fd">This shape grants this capability</text>',
            f'<text x="24" y="228" class="fd">at this barrier, with this undo</text>',
            f'<text x="24" y="244" class="fd">class and this evidence tier; the</text>',
            f'<text x="24" y="260" class="fd">mandate takes this stance on all</text>',
            f'<text x="24" y="276" class="fd">23 primitives; therefore this excess.</text>',
            f'<text x="24" y="308" class="fb">The classes are not.</text>',
            f'<text x="24" y="328" class="fd">How a reader groups them differs</text>',
            f'<text x="24" y="344" class="fd">by altitude, and that is correct</text>',
            f'<text x="24" y="360" class="fd">rather than a defect.</text>',
            ]
    return fig(_svg("".join(body), 420),
               "The rule has been in force since August and was named as the blocker on four "
               "consecutive days in September, because the diff did not exist. It exists now, "
               "and it reads the artefact rather than the thing that made it.",
               "A figure here in the page: the grant and the mandate feed one fact set of "
               "leaf assertions, computed and never authored. The fact set is projected as "
               "the label, the leaflet, the prohibitions and the figure, all of which render "
               "into the published page and its markdown twin. The release gate parses the "
               "page back out and compares it with the fact set assertion by assertion, both "
               "ways, and one row that differs fails the build")


def setting_path():
    """v0.4.3. The confirmations flag, as a path rather than a sentence."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">The confirmations flag, as a path the build '
            'walks</text>',
            '<text x="24" y="40" class="fk">one product, two variants, and the difference '
            'between their grants</text>',
            _box(24, 66, 260, 40, "Claude Code (the CLI)", None, "box"),
            f'<text x="154" y="120" text-anchor="middle" class="fmd">has_variant</text>',
            f'<path d="M 154 106 C 154 130, 120 130, 120 146" class="edge" '
            f'marker-end="url(#ah)"/>',
            f'<path d="M 154 106 C 154 130, 210 130, 210 146" class="edge" '
            f'marker-end="url(#ah)"/>',
            _box(24, 148, 190, 40, "local-default", None, "box", mono=True),
            _box(24, 200, 190, 40, "local-confirmations-off", None, "box", mono=True),
            _box(330, 120, 250, 56, "the setting", "that distinguishes the two", "box-a"),
            _arrow(214, 168, 326, 150, None, cls="edge-a"),
            _arrow(214, 216, 326, 168, None, cls="edge-a"),
            f'<text x="270" y="200" text-anchor="middle" class="fk">derived by diffing</text>',
            f'<text x="270" y="216" text-anchor="middle" class="fk">their grants</text>',
            _arrow(580, 134, 672, 110, "narrows", cls="edge-a", dy=-6),
            _box(676, 84, 260, 40, "execute.process.host", None, "box-a", mono=True),
            _arrow(580, 162, 672, 196, "moves", cls="edge-a", dy=14),
            _box(676, 176, 120, 40, "setting", None, "box", mono=True),
            # BOTH barriers, because the setting node carries a `moves` edge to each: what the
            # flag moves the capability BETWEEN is the pair, and drawing one would be half true.
            f'<path d="M 580 168 C 700 168, 740 150, 830 172" class="edge-a" '
            f'marker-end="url(#aha)"/>',
            _box(816, 176, 120, 40, "none", None, "box", mono=True),
            f'<text x="676" y="238" class="fd">confirmations on</text>',
            f'<text x="816" y="238" class="fd">confirmations off</text>',
            f'<rect x="24" y="266" width="912" height="56" rx="10" class="box-x"/>',
            f'<text x="40" y="288" class="ft"><tspan class="fb">The grant did not change. '
            f'The mandate did not change. The delta did not change.</tspan> One barrier '
            f'moved, and not one number on the label.</text>',
            f'<text x="40" y="308" class="fd">The home page has said that in a sentence since '
            f'v0.1.0. Since v0.4.3 it is a path: two nodes, two edges, walked on every '
            f'build.</text>',
            ]
    return fig(_svg("".join(body), 338),
               "Neither node was typed in. The product comes from the shape id, and the "
               "setting comes from diffing the grants of its two variants: whatever moved "
               "between them is what the setting moves.",
               "A figure here in the page: the product Claude Code has two variants, "
               "local-default and local-confirmations-off. The setting that distinguishes "
               "them is a node derived by diffing their grants. It narrows the capability "
               "execute.process.host and moves it between the barriers setting and none. The "
               "grant, the mandate and the delta are identical in both variants: one barrier "
               "moves and not one number on the label")


def intake_path():
    """v0.4.4. A shape somebody else measured, and the loop that closes."""
    body = [DEFS,
            '<text x="24" y="22" class="fh">How a shape somebody else measured gets an '
            'address</text>',
            '<text x="24" y="40" class="fk">layer one facts are owned by nobody, so they '
            'belong where every consumer reads</text>']
    steps = [("riskmandate.ai", "reads the vendor's pages, or measures an instance it is "
              "entitled to run", "box"),
             ("the bytes, fetched", "held unchanged, with a hash per file and a hash over "
              "all of them", "box-b"),
             ("promoted", "into a profile and a mandate, nothing renamed, every id inside "
              "the grammar", "box-a"),
             ("published here", "at the address every consumer reads, counted beside the "
              "map's rows", "box-a")]
    for i, (t, sub, cls) in enumerate(steps):
        y = 64 + i * 74
        body += [
            f'<rect x="24" y="{y}" width="600" height="52" rx="9" class="{cls}"/>',
            f'<text x="42" y="{y + 22}" class="fb">{t}</text>',
            f'<text x="42" y="{y + 40}" class="fd">{sub}</text>',
        ]
        if i < 3:
            body.append(f'<path d="M 324 {y + 52} L 324 {y + 74}" class="edge-a" '
                        f'marker-end="url(#aha)"/>')
    body += [
        f'<path d="M 624 {64 + 3 * 74 + 26} C 720 {64 + 3 * 74 + 26}, 720 90, 624 90" '
        f'class="edge-a" marker-end="url(#aha)"/>',
        f'<text x="740" y="{64 + 74 + 20}" class="fb">and the loop closes</text>',
        f'<text x="740" y="{64 + 74 + 40}" class="ft">their vault pins this</text>',
        f'<text x="740" y="{64 + 74 + 56}" class="ft">site\'s version of the</text>',
        f'<text x="740" y="{64 + 74 + 72}" class="ft">shape, rather than</text>',
        f'<text x="740" y="{64 + 74 + 88}" class="ft">holding its own copy</text>',
        f'<rect x="24" y="{64 + 4 * 74}" width="912" height="54" rx="10" class="box-x"/>',
        f'<text x="40" y="{64 + 4 * 74 + 22}" class="ft"><tspan class="fb">The tier is the '
        f'contributor\'s, and this site did not raise it.</tspan> 11 of the 37 rows are at '
        f'the contributor\'s measured tier.</text>',
        f'<text x="40" y="{64 + 4 * 74 + 42}" class="fd">Nothing was probed here. The rows '
        f'are counted beside the map\'s 21 of 99 rather than folded into them, because the '
        f'two were obtained differently.</text>',
    ]
    return fig(_svg("".join(body), 432),
               "The bytes are never edited, and the build and the gate both recompute their "
               "hashes. A profile promoted from them pins the hash of the one file it came "
               "from, so a byte that moves after the fetch fails the build in three places.",
               "A figure here in the page: riskmandate.ai reads a vendor's pages or measures "
               "an instance it is entitled to run; the bytes are fetched and held unchanged "
               "with a hash per file and a hash over all of them; they are promoted into a "
               "profile and a mandate with nothing renamed and every id inside the grammar; "
               "and they are published at the address every consumer reads. The loop closes "
               "when the contributor's vault pins this site's version of the shape rather "
               "than holding its own copy")
