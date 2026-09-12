#!/usr/bin/env node
// The pre-release gate. Run from anywhere: node admin/build/validate.js
//
// COPIED from SGit-AI/SGit-AI__Website__Game__What-Can-It-Do (admin/build/validate.js, v0.8.0),
// which inherited its first four checks from pki.sgit.ai, graphs.sgit.ai and
// wardley-maps.sgit.ai. The game's three site-specific checks (a vault embed carrying its
// telemetry disclosure, maturity labels from a ladder, a packs registry resolving) are gone,
// because this site mounts no vault, has no ladder and serves no registry.
//
// THE HOUSE FOUR, unchanged in intent:
//   1. version agreement -- admin/build/version.txt against every page's badge, llms.txt, the
//      markdown twins AND the version surface
//   2. internal links -- every relative href/src resolves to a file in the tree
//   3. canonical host -- every canonical and og:url is on the host in CNAME
//   4. key-leak tripwire -- nothing in the tree may look like an sgit vault key
//
// AND ONE MORE FROM THE SIBLING:
//   7. every page has its markdown twin
//
// FIVE ARE NEW HERE, and each one exists because this pack asks for it by name. The style
// guide is honest that four structural guards in the pipeline are the estate's only automated
// enforcement, one of which does not work, so these are cheap on purpose.
//   8. NO SCORE, ANYWHERE. No rating, no traffic light, no risk level, no severity, on any
//      page, in any data file. This is rule 0 made mechanical: a score is a verdict, and the
//      ABP describes without judging. Every buyer will ask for one; the answer is that it
//      lives on the risk product.
//   9. NO FORBIDDEN WORD. `agentic' (ruled out of customer facing copy on evidence),
//      `insurance' (three standing rulings; this site is rung zero), `zero knowledge' and
//      `memory' in customer facing copy, the payroll processor's mark that appeared once as a
//      slip in a memo, and `the policy' as a short form of ABP, because in this estate that
//      word already denotes the insurance instrument.
//  10. NO EM DASH AND NO EN DASH, and pure ASCII outside a declared set of published glyphs.
//      The style guide's own measurement is that this rule sits at ZERO PER CENT compliance,
//      violated 248 times across eleven documents. It is the cheapest possible check and this
//      repository is meant to be the first one that holds.
//  11. EVERY PAGE IS IN llms.txt. The sibling generates llms.txt from its page list, so it
//      cannot miss a page the generator knows about -- and nothing fails if a page exists in
//      the tree that the generator does not.
//  13. THE GRAPH HOLDS TOGETHER: every edge is a verb with a distinct inverse and a stated
//      domain and range, no generic association edge exists, every edge instance uses a
//      declared type and resolves at both ends, EXACTLY ONE BARRIER MATCHES THE [Control]
//      FORMULA when the formula is walked rather than read off a field, and every word that
//      appears in a capability id has a node, a JSON file and a page of its own.
//  12. THE DATA HOLDS TOGETHER: the promoted vocabulary resolves, the upstream bytes hash to
//      what their manifest says, every profile row names a real capability and a real barrier,
//      no mandate both wants and refuses the same thing, and EVERY STORED DELTA RECOMPUTES
//      FROM ITS OWN PINNED INPUTS. That last one was the opposite check until 11 September
//      2026, when the published rule was corrected from `computed and never stored' to
//      `derived and never authored'. Never authored is the harder rule and this is how a
//      machine holds it.
//
// Any failure exits 1: no tag, no publish.
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..', '..');
const errors = [];

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    if (['.git', '.github', 'node_modules', '.sg_vault', '__pycache__'].includes(name)) continue;
    const p = path.join(dir, name);
    fs.statSync(p).isDirectory() ? walk(p, out) : out.push(p);
  }
  return out;
}
const rel = f => path.relative(ROOT, f).split(path.sep).join('/');
const read = f => fs.readFileSync(f, 'utf8');

const files = walk(ROOT);
const htmlFiles = files.filter(f => f.endsWith('.html'));
const mdFiles = files.filter(f => f.endsWith('.md'));

// --- 1. version agreement -------------------------------------------------
const VERSION = read(path.join(ROOT, 'admin/build/version.txt')).trim();
if (!/^v\d+\.\d+\.\d+$/.test(VERSION)) {
  errors.push(`version.txt does not carry a vX.Y.Z version: "${VERSION}"`);
}
for (const f of htmlFiles) {
  for (const m of read(f).matchAll(/class="ver"[^>]*>(v\d+\.\d+\.\d+)</g)) {
    if (m[1] !== VERSION) errors.push(`${rel(f)}: version badge ${m[1]} != ${VERSION}`);
  }
}
if (!read(path.join(ROOT, 'llms.txt')).includes(VERSION)) {
  errors.push(`llms.txt does not mention ${VERSION}`);
}
// The version SURFACE, which is the one the sibling did not have. The badge in the chrome
// reads `current` from here, so if this disagrees with version.txt the badge is lying.
(function () {
  const f = path.join(ROOT, 'versions/index.json');
  if (!fs.existsSync(f)) { errors.push('versions/index.json is missing -- run build_pages.py'); return; }
  const idx = JSON.parse(read(f));
  if (idx.current !== VERSION) {
    errors.push(`versions/index.json says current is ${idx.current}, version.txt says ${VERSION}`);
  }
  const seen = new Set();
  for (const e of idx.versions || []) {
    if (seen.has(e.version)) errors.push(`versions/index.json lists ${e.version} more than once`);
    seen.add(e.version);
    for (const p of [path.join(ROOT, 'versions', e.file), path.join(ROOT, 'versions', e.page)]) {
      if (!fs.existsSync(p)) errors.push(`versions/index.json names ${rel(p)}, which does not exist`);
    }
    const det = JSON.parse(read(path.join(ROOT, 'versions', e.file)));
    // A version without its commit cannot be verified later. The guidance says so directly.
    // A version that is not tagged YET cannot carry its own hash -- a release commit cannot
    // contain it -- so it has to say where the hash will come from instead. One of the two.
    if (!det.commit && !(det.commit_resolves_by && det.commit_note)) {
      errors.push(`versions/${e.file} records neither a commit nor how to resolve one`);
    }
    if (det.commit && !/^[0-9a-f]{40}$/.test(det.commit)) {
      errors.push(`versions/${e.file}: "${det.commit}" is not a commit hash`);
    }
    // The build must not read git: a checkout with tags and one without have to produce the
    // same bytes, or the staleness check above fails on every release.
    if (det.commit_resolves_by && det.commit_resolves_by !== `git rev-list -n 1 ${e.version}`) {
      errors.push(`versions/${e.file}: commit_resolves_by does not name this version's tag`);
    }
    if (typeof det.reconstructed !== 'boolean') {
      errors.push(`versions/${e.file} does not say whether it was reconstructed`);
    }
    // The title is a sentence, not a label: "settings move into the right hand column",
    // never "UI improvements". A three-word title is almost always the second kind.
    if (!det.title || det.title.split(/\s+/).length < 5) {
      errors.push(`versions/${e.file}: the title is a label, not a sentence: "${det.title}"`);
    }
  }
  if (!seen.has(VERSION)) errors.push(`versions/index.json has no entry for ${VERSION}`);
}());

// --- 2. internal links ----------------------------------------------------
for (const f of htmlFiles) {
  const dir = path.dirname(f);
  for (const m of read(f).matchAll(/(?:href|src)="([^"#]+)(?:#[^"]*)?"/g)) {
    const target = m[1];
    if (/^(https?:|mailto:|data:|\/\/)/.test(target) || target === '') continue;
    if (!fs.existsSync(path.resolve(dir, target))) {
      errors.push(`${rel(f)}: broken link -> ${target}`);
    }
  }
}

// --- 3. canonical host ----------------------------------------------------
// CNAME is WRITTEN BY THE BUILD here, not committed once, which is the third of the five
// verifications the conventions ask for. This check reads the same file the build writes.
const HOST = read(path.join(ROOT, 'CNAME')).trim();
if (!/^[a-z0-9.-]+$/.test(HOST)) errors.push(`CNAME does not carry a hostname: "${HOST}"`);
for (const f of htmlFiles) {
  const t = read(f);
  const claimed = [
    ...[...t.matchAll(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/g)].map(m => m[1]),
    ...[...t.matchAll(/<meta[^>]+property="og:url"[^>]+content="([^"]+)"/g)].map(m => m[1]),
  ];
  for (const url of claimed) {
    if (!url.startsWith(`https://${HOST}/`)) {
      errors.push(`${rel(f)}: canonical/og:url is not on ${HOST} -> ${url}`);
    }
  }
  if (!/rel="canonical"/.test(t)) errors.push(`${rel(f)}: no canonical link`);
}

// --- 4. key-leak tripwire -------------------------------------------------
// A read key is 64 hex and may be published on purpose. A VAULT key is
// `<passphrase>:<vault-id>` -- bearer read AND write, with no revocation list -- and may never
// be. The two are one character class apart to a careless eye. This site embeds no vault and
// so PUBLISHED is empty: if that changes, escrow the write key before publishing and add the
// read key here as an exact string, never as a pattern.
const PUBLISHED = [];
const KEY_SHAPES = [
  /[A-Za-z0-9_-]{20,}:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g,
  /[A-Za-z0-9_-]{16,}:[a-z0-9]{8}\b/g,
];
for (const f of files) {
  if (/\.(png|jpg|jpeg|gif|webp|ico|svg|woff2?|zip|pdf)$/.test(f)) continue;
  const t = read(f);
  for (const shape of KEY_SHAPES) {
    for (const m of t.matchAll(shape)) {
      if (PUBLISHED.includes(m[0])) continue;
      errors.push(`${rel(f)}: vault-key-shaped string "${m[0].slice(0, 14)}..." -- if this is a `
                + `read key we meant to publish, add it to PUBLISHED in validate.js; if it is `
                + `a vault key, rotate it`);
    }
  }
}

// --- 7. every page has its twin -------------------------------------------
for (const f of htmlFiles) {
  const twin = f.replace(/\.html$/, '.md');
  if (!fs.existsSync(twin)) errors.push(`${rel(f)}: no .md twin (run build_pages.py)`);
}

// WHAT COUNTS AS THIS SITE'S OWN COPY, for checks 8 and 9.
//
// The word rules and the no-score rule govern what THIS SITE SAYS. They cannot govern the
// documents it republishes: `docs/` carries the foundation document, three briefs and six pack
// documents, and the pack requires them published UNCHANGED, with their own licence footers
// intact. Editing a published document so that a linter here goes quiet would falsify it,
// which is a worse failure than an unenforced word rule -- and one of those briefs names the
// payroll processor's mark precisely in order to record that it was a slip. The same goes for
// `data/upstream/`, which is somebody else's bytes served verbatim, and for `llms-full.txt`,
// which is nothing but a concatenation of twins that were each checked on their own.
// `what-is-an-abp/` is in the set for the same reason and it is worth naming: THAT PAGE IS THE
// FOUNDATION DOCUMENT, RENDERED, not a page about it. The pack says its wording is the wording,
// so the page cannot be edited to satisfy a guard here; it names the industry's list of agentic
// application risks because that is what the list is called.
//
// So the scope is: everything this repository AUTHORS. That is the home page, the model, the
// examples, the data layer's own pages, the version surface, llms.txt and the build itself.
// The exemption is narrow, declared here, and stated on the docs index rather than hidden.
const QUARANTINED = ['docs/', 'data/upstream/', 'llms-full.txt', 'what-is-an-abp/'];
const OWN_COPY = f => !QUARANTINED.some(q => rel(f).startsWith(q));

// --- 8. no score, anywhere -------------------------------------------------
// Rule 0 made mechanical. A score is a verdict, and the same ABP is dangerous in one
// deployment and harmless in the next. The one permitted ordering is by reversibility, stated
// as a property of the action, so `irreversible' and `undo' are not on this list.
//
// The pages that ARGUE against scoring have to be able to say the word, so a line is exempt
// when it carries a negation near it. That makes the check a tripwire rather than a proof,
// which is the honest description of every check in this file.
const SCORE_WORDS = [
  /\brisk (?:score|rating|level|tier)\b/i, /\bseverity\b/i, /\btraffic light\b/i,
  /\bcriticality\b/i, /\bCVSS\b/i, /\brisk[- ]scored?\b/i, /\bscored? (?:high|medium|low)\b/i,
  /\b(?:high|medium|low|critical)[- ]risk\b/i,
];
const DENIES = /\bno\b|\bnot\b|\bnever\b|\bwithout\b|\bnothing\b|\bcarries no\b|\brefus|\bdoes not\b|\bcannot\b|\bnowhere\b|\bthere is\b|\blives on\b|\bbelongs\b/i;
for (const f of [...htmlFiles, ...mdFiles, ...files.filter(f => f.endsWith('.json') && !rel(f).startsWith('data/upstream/'))].filter(OWN_COPY)) {
  const lines = read(f).split('\n');
  lines.forEach((line, n) => {
    for (const w of SCORE_WORDS) {
      if (w.test(line) && !DENIES.test(line)) {
        errors.push(`${rel(f)}:${n + 1}: score vocabulary with nothing denying it -- `
                  + `"${line.trim().slice(0, 90)}". A score is a verdict; it lives on the risk `
                  + `product. If this line is arguing AGAINST scoring, say so in the same line.`);
      }
    }
  });
}

// --- 9. no forbidden word --------------------------------------------------
// Each of these is a standing ruling with a reason, not a preference. Scoped to this
// site's own copy, per OWN_COPY above.
const FORBIDDEN = [
  [/\bagentic\b/i, "ruled out of customer facing copy on 10 September on evidence: it reads as "
                 + "a discount to this buyer, and the grammar is wrong. Use `agent'"],
  [/\binsurance\b/i, "three standing rulings put insurance at the top rung and forbid calling "
                   + "the lower rungs by it. This site is rung zero"],
  [/\bzero[- ]knowledge\b/i, "ruled 10 September: the vocabulary is contested and the consumer "
                           + "meaning fights an encryption product. Use `end to end encrypted'"],
  [/\bA\s?D\s?P\b/, "one of the world's largest payroll processors and a registered mark. It "
                  + "appeared once as a slip in a memo and must not appear in this repository"],
  [/\bthe policy\b/i, "never shorten ABP to `the policy': in this estate that word already "
                    + "denotes the insurance instrument on the licence to operate demonstration. "
                    + "Write ABP or behaviour policy"],
];
// A line that STATES one of these rules has to be able to name the word it forbids, and the
// README and the docs index both do. The escape is an explicit marker in the line rather than
// a file exemption, so every use of it is visible in the source and greppable in one command.
const NAMES_THE_RULE = /gate:names-the-rule/;
for (const f of [...htmlFiles, ...mdFiles].filter(OWN_COPY)) {
  const lines = read(f).split('\n');
  lines.forEach((line, n) => {
    if (NAMES_THE_RULE.test(line)) return;
    for (const [w, why] of FORBIDDEN) {
      if (w.test(line)) {
        errors.push(`${rel(f)}:${n + 1}: forbidden word -- "${line.trim().slice(0, 80)}". ${why}`);
      }
    }
  });
}

// --- 10. no em dash, no en dash, and ASCII outside the published glyphs ----
// The style guide's own measurement is 248 violations across eleven documents and ZERO PER
// CENT compliance. The exempt set is declared here, as exact characters with a reason, rather
// than as a pattern: the five barrier glyphs are DATA -- the published enforcement model puts
// one on every cell so that the reading never depends on colour -- and the middot is one of
// them. `data/` is exempt in full because the promoted files carry upstream strings exactly as
// they arrived; every one of them rendered into a page is transliterated first, and the bytes
// stay one click away.
const GLYPHS = '\u25cf\u25c9\u25d0\u25cb\u00b7\u25b2\u25bc\u2713';
const ASCII_EXEMPT = f => rel(f).startsWith('data/') || /\.(svg|ico|png|woff2?)$/.test(f);
for (const f of files) {
  if (ASCII_EXEMPT(f) || /\.(png|jpg|jpeg|gif|webp|ico|svg|woff2?|zip|pdf)$/.test(f)) continue;
  const lines = read(f).split('\n');
  lines.forEach((line, n) => {
    if (line.includes('\u2014') || line.includes('\u2013')) {
      errors.push(`${rel(f)}:${n + 1}: em dash or en dash -- "${line.trim().slice(0, 70)}". `
                + `This is the rule the estate has measured at zero per cent compliance.`);
    }
    for (const ch of line) {
      if (ch.charCodeAt(0) > 126 && !GLYPHS.includes(ch)) {
        errors.push(`${rel(f)}:${n + 1}: non-ASCII "${ch}" (U+${ch.charCodeAt(0).toString(16)}) `
                  + `outside the declared glyph set -- "${line.trim().slice(0, 60)}"`);
        break;
      }
    }
  });
}

// --- 11. every page is in llms.txt ----------------------------------------
// The second of the five verifications, and the one the sibling could not fail because it
// never looked. This walks the TREE, not the generator's page list.
(function () {
  const llms = read(path.join(ROOT, 'llms.txt'));
  for (const f of htmlFiles) {
    const twin = rel(f).replace(/\.html$/, '.md');
    if (!llms.includes(twin)) {
      errors.push(`${twin} is a page in the tree and is not listed in llms.txt`);
    }
  }
  const full = path.join(ROOT, 'llms-full.txt');
  if (!fs.existsSync(full)) errors.push('llms-full.txt is missing -- run build_pages.py');
  else if (!read(full).includes(VERSION)) errors.push(`llms-full.txt does not mention ${VERSION}`);
}());

// --- 12. the data holds together ------------------------------------------
// data/ is the contribution surface: a pull request edits JSON and the pages regenerate. So
// the gate has to refuse a pull request whose data does not hold together, or the first typo
// in a capability id ships as a silent hole in a published vocabulary.
(function () {
  const D = path.join(ROOT, 'data');
  const J = f => { try { return JSON.parse(read(path.join(D, f))); }
                   catch (e) { errors.push(`data/${f}: ${e.message}`); return null; } };

  // The upstream bytes hash to what their own manifest says. This is the claim the whole
  // provenance line rests on, so it is recomputed here as well as in the build.
  const up = path.join(D, 'upstream');
  const pack = J('upstream/pack.json');
  if (pack) {
    const list = walk(up)
      .filter(x => x.endsWith('.json') && !['pack.json', 'packs.json', 'proposals.json'].includes(path.basename(x)))
      .map(x => path.relative(up, x).split(path.sep).join('/'))
      .sort((a, b) => { const pa = a.split('/'), pb = b.split('/');
        for (let i = 0; i < Math.min(pa.length, pb.length); i++) if (pa[i] !== pb[i]) return pa[i] < pb[i] ? -1 : 1;
        return pa.length - pb.length; });
    const h = crypto.createHash('sha256');
    for (const p of list) { h.update(p); h.update(fs.readFileSync(path.join(up, p))); }
    const got = 'sha256:' + h.digest('hex');
    if (got !== pack.content_hash) {
      errors.push(`data/upstream hashes to ${got.slice(0, 22)}..., its manifest says `
                + `${pack.content_hash.slice(0, 22)}... -- the source bytes were edited after `
                + `the fetch, which breaks every provenance line on the site`);
    }
  }

  const caps = J('capabilities.json');
  const bars = J('barriers.json');
  const undo = J('undo-classes.json');
  const prov = J('provenance.json');
  if (!caps || !bars || !undo || !prov) return;
  const CAP = new Set(caps.capabilities.map(c => c.id));
  const BAR = new Set(bars.barriers.map(b => b.id));
  const UNDO = new Set(undo.classes.map(c => c.id));
  if (caps.count !== caps.capabilities.length) errors.push('data/capabilities.json: count disagrees with the list');
  // Exactly one barrier bounds anything. If that stops being true the enforcer test has
  // changed, and every page on this site is written against it.
  const controls = bars.barriers.filter(b => b.is_control);
  if (controls.length !== 1 || controls[0].id !== 'boundary') {
    errors.push(`data/barriers.json: ${controls.length} barriers claim to be controls. Exactly `
              + `one bounds anything: a boundary enforced above the grant`);
  }

  const pidx = J('profiles/index.json');
  if (pidx) for (const e of pidx.profiles) {
    const p = J(e.file); if (!p) continue;
    if (p.id !== e.id) errors.push(`data/${e.file}: id "${p.id}" does not match the index`);
    let measured = 0;
    for (const r of p.grant || []) {
      if (!CAP.has(r.capability)) errors.push(`data/${e.file}: unknown capability "${r.capability}"`);
      if (!BAR.has(r.barrier)) errors.push(`data/${e.file}: unknown barrier "${r.barrier}"`);
      if (!UNDO.has(r.undo)) errors.push(`data/${e.file}: unknown undo class "${r.undo}"`);
      // Every row carries whether anything is actually in the way. A row without it would
      // render a prohibition with no barrier, which manufactures assurance.
      if (typeof r.is_bounded !== 'boolean') errors.push(`data/${e.file}: ${r.capability} does not say whether it is bounded`);
      if (r.is_bounded !== (r.barrier === 'boundary')) {
        errors.push(`data/${e.file}: ${r.capability} says is_bounded ${r.is_bounded} at barrier "${r.barrier}"`);
      }
    }
    if ((p.grant || []).length !== p.grant_size) errors.push(`data/${e.file}: grant_size disagrees with the rows`);
    if (!p.provenance || !p.provenance.source || !p.provenance.retrieved || !p.provenance.content_hash) {
      errors.push(`data/${e.file}: a capability claim about a named commercial product with no `
                + `source URL, retrieval timestamp and content hash is an assertion`);
    }
  }

  const midx = J('mandates/index.json');
  if (midx) for (const e of midx.mandates) {
    const m = J(e.file); if (!m) continue;
    for (const k of ['want', 'do_not_want', 'unstated']) {
      for (const c of m[k] || []) if (!CAP.has(c)) errors.push(`data/${e.file}: ${k} names unknown capability "${c}"`);
    }
    for (const c of (m.want || []).filter(x => (m.do_not_want || []).includes(x))) {
      errors.push(`data/${e.file}: both wants and does not want "${c}"`);
    }
    const n = (m.want || []).length + (m.do_not_want || []).length + (m.unstated || []).length;
    if (n !== caps.count) errors.push(`data/${e.file}: covers ${n} capabilities, there are ${caps.count}`);
  }

  // THE DELTA IS DERIVED AND NEVER AUTHORED.
  //
  // This check was the opposite one until 11 September 2026, when it refused any file
  // carrying a delta at all, on a published rule that the delta is computed and never stored.
  // Half of that rule was right. The delta is computed; it is also stored, because the history
  // of grants, mandates and deltas is what lets a control project be evidenced as a
  // subtraction, and because a question about whether a control held throughout a period is a
  // question about a series that a recomputed present cannot answer.
  //
  // NEVER AUTHORED is the harder rule, and it is the one that needs a machine to hold it: it
  // forbids the ACT rather than the artefact, and a hand edited delta is a fiction about an
  // environment that nothing downstream could detect. So the gate does not take the stored
  // records on trust. It RECOMPUTES every one of them from the profile and the mandate it
  // names, and fails on a single row of disagreement. That is a few lines because the
  // computation is a set difference, which is the whole point of holding the grant and the
  // mandate as graphs with a schema rather than as prose.
  (function () {
    const didx = J('deltas/index.json');
    if (!didx) { errors.push('data/deltas/index.json is missing -- run build_pages.py'); return; }
    const eq = (a, b) => a.length === b.length && a.every((x, i) => x === b[i]);
    for (const e of didx.deltas || []) {
      const d = J(e.file); if (!d) continue;
      const prof = J(`profiles/${d.profile}.json`);
      const man = J(`mandates/${d.mandate}.json`);
      if (!prof || !man) { errors.push(`data/${e.file}: names a profile or mandate that is missing`); continue; }

      // The inputs have to be pinned, or the record is the stale claim the old rule feared.
      for (const k of ['grant_version', 'mandate_version', 'computed_at', 'computed_by']) {
        if (!d[k]) errors.push(`data/${e.file}: no ${k} -- a stored delta that does not pin its inputs cannot be checked`);
      }
      if (d.grant_version !== prof.profile_version) {
        errors.push(`data/${e.file}: pinned to grant ${d.grant_version}, the profile is now ${prof.profile_version} -- recompute`);
      }
      if (d.mandate_version !== man.authored) {
        errors.push(`data/${e.file}: pinned to mandate ${d.mandate_version}, the mandate is now ${man.authored} -- recompute`);
      }

      // The recompute. Order is irreversible first, then weakest barrier first, then by id --
      // the same ordering the site renders in, because a record whose order is not the
      // document's order would be a second thing to keep in step.
      const UNDO = ['no', 'with-effort', 'yes'];
      const BAR = ['none', 'expectation', 'setting', 'boundary'];
      const undoOf = Object.fromEntries(caps.capabilities.map(c => [c.id, c.undo]));
      const byCap = Object.fromEntries((prof.grant || []).map(r => [r.capability, r]));
      const want = new Set(man.want || []);
      const refused = new Set(man.do_not_want || []);
      const sortRows = ids => ids.slice().sort((a, b) =>
        UNDO.indexOf(undoOf[a]) - UNDO.indexOf(undoOf[b]) ||
        BAR.indexOf(byCap[a].barrier) - BAR.indexOf(byCap[b].barrier) ||
        (a < b ? -1 : a > b ? 1 : 0));
      const granted = Object.keys(byCap);
      const want_ = sortRows(granted.filter(c => want.has(c)));
      const excess = sortRows(granted.filter(c => !want.has(c)));
      const expect = {
        excess,
        excess_refused: excess.filter(c => refused.has(c)),
        excess_unstated: excess.filter(c => !refused.has(c)),
        unbounded_excess: excess.filter(c => !byCap[c].is_bounded),
        shortfall: [...want].filter(c => !(c in byCap)).sort(),
        aligned: want_,
      };
      for (const k of Object.keys(expect)) {
        if (!eq(expect[k], d[k] || [])) {
          errors.push(`data/${e.file}: ${k} does not recompute from its own inputs. `
                    + `A delta is DERIVED AND NEVER AUTHORED: expected [${expect[k].join(', ')}], `
                    + `the file says [${(d[k] || []).join(', ')}]. Either somebody edited this `
                    + `record by hand, or the build was not rerun after a grant or a mandate moved.`);
        }
      }
      for (const k of Object.keys(d.counts || {})) {
        if (d.counts[k] !== (d[k] || []).length) {
          errors.push(`data/${e.file}: counts.${k} says ${d.counts[k]}, the list has ${(d[k] || []).length}`);
        }
      }
      if (!d.provenance || !d.provenance.content_hash) {
        errors.push(`data/${e.file}: no provenance`);
      }
    }
    // A delta for a pair the mandates do not name is an orphan nothing recomputes.
    const named = new Set((didx.deltas || []).map(e => `deltas/${e.id}.json`));
    for (const f of walk(path.join(D, 'deltas')).filter(x => x.endsWith('.json') && path.basename(x) !== 'index.json')) {
      const r = 'deltas/' + path.basename(f);
      if (!named.has(r)) errors.push(`data/${r} exists but is not in deltas/index.json`);
    }
  }());

  const man = J('index.json');
  if (man && man.version !== VERSION) {
    errors.push(`data/index.json is ${man.version}, site is ${VERSION} -- run build_pages.py`);
  }
  if (prov.rows && prov.rows.measured + prov.rows.derived !== prov.rows.total) {
    errors.push('data/provenance.json: measured plus derived does not equal total');
  }
}());

// --- 13. the graph holds together -----------------------------------------
// The ontology is the product now, so it gets a gate. Three things matter and each of them is
// a claim the whole site is written against.
(function () {
  const D = path.join(ROOT, 'data');
  const J = f => { try { return JSON.parse(read(path.join(D, f))); }
                   catch (e) { errors.push(`data/${f}: ${e.message}`); return null; } };
  const ev = J('graph/edges.json');
  const nt = J('graph/node-types.json');
  const nodes = J('graph/nodes.json');
  const gr = J('graph/graph.json');
  const lex = J('lexicon/index.json');
  if (!ev || !nt || !nodes || !gr || !lex) return;

  // (a) EVERY EDGE IS A VERB WITH A DISTINCT INVERSE, AND THE GENERIC EDGE IS BANNED.
  // `connected_to` is the generic association edge under its published name. It is in the
  // network's set as symmetric, and it is exactly the edge that constrains nothing and costs
  // fan out, so this model may not use one.
  const declared = new Map();
  for (const e of ev.edges || []) {
    for (const k of ['edge', 'inverse', 'domain', 'range', 'reads_as', 'inverse_reads_as', 'from']) {
      if (!e[k]) errors.push(`data/graph/edges.json: ${e.edge || '(unnamed)'} has no ${k} -- a new edge needs a sentence, its inverse needs a DIFFERENT sentence, and both need a domain and a range`);
    }
    if (e.edge === e.inverse && e.edge !== 'similar_to') {
      errors.push(`data/graph/edges.json: ${e.edge} is its own inverse. The inverse is not the same edge walked backwards: it has different fan out, and that asymmetry is what stops the graph exploding`);
    }
    if (e.reads_as && e.reads_as === e.inverse_reads_as) {
      errors.push(`data/graph/edges.json: ${e.edge} and ${e.inverse} read as the same sentence, so one of them is not doing any work`);
    }
    if (/^(relates_to|related_to|associated_with|connected_to|links_to)$/.test(e.edge)) {
      errors.push(`data/graph/edges.json: "${e.edge}" is a generic association edge. It is banned: it constrains nothing and costs fan out`);
    }
    declared.set(e.edge, e);
  }
  // Every edge INSTANCE uses a declared edge type. An undeclared edge is a vocabulary nobody
  // agreed to, appearing in the data.
  const used = new Set((gr.edges || []).map(e => e.edge));
  for (const u of used) {
    if (!declared.has(u)) errors.push(`data/graph/graph.json uses edge "${u}", which is not in the edge vocabulary`);
  }
  // Every edge instance resolves at both ends. A dangling edge is a path that cannot be walked.
  const ids = new Set((nodes.nodes || []).map(n => n.id));
  for (const e of gr.edges || []) {
    if (!ids.has(e.from)) errors.push(`data/graph/graph.json: edge ${e.edge} starts at "${e.from}", which is not a node`);
    if (!ids.has(e.to)) errors.push(`data/graph/graph.json: edge ${e.edge} ends at "${e.to}", which is not a node`);
  }

  // (b) EXACTLY ONE BARRIER IS A CONTROL, and it is the one enforced from outside the grant.
  // This is the enforcer test, and every page on this site is written against it. It used to be
  // a boolean field; it is now a formula, so the gate walks the formula rather than reading the
  // field, which is the only version of this check worth having.
  const enforcedBy = new Map((gr.edges || []).filter(e => e.edge === 'enforced_by').map(e => [e.from, e.to]));
  const node = id => (nodes.nodes || []).find(n => n.id === id);
  const barriers = (nodes.nodes || []).filter(n => n.type === 'Barrier');
  const controls = barriers.filter(b => {
    const enf = enforcedBy.get(b.id);
    return enf && node(enf) && node(enf).inside_the_grant === false;
  });
  if (controls.length !== 1) {
    errors.push(`data/graph: ${controls.length} barriers match [Control] := a [Barrier] `
              + `-enforced_by-> an [Enforcer] the [Grant] does not include. Exactly one must. `
              + `Every page on this site is written against that.`);
  } else if (controls[0].id !== 'barrier/boundary') {
    errors.push(`data/graph: the barrier matching [Control] is ${controls[0].id}, not barrier/boundary`);
  }
  // And the formula's own declared count has to agree with walking it.
  const declaredControl = (nt.node_types || []).find(t => t.name === 'Control');
  if (declaredControl && declaredControl.matched !== controls.length) {
    errors.push(`data/graph/node-types.json says [Control] matched ${declaredControl.matched}, walking it gives ${controls.length} -- run build_pages.py`);
  }

  // (c) EVERY WORD IN THE GRAMMAR HAS AN ADDRESS. A node with no address cannot be argued with,
  // and being argued with is the point of publishing a vocabulary.
  const caps = J('capabilities.json');
  if (caps) {
    const want = {verbs: new Set(), objects: new Set(), reaches: new Set(), families: new Set()};
    for (const c of caps.capabilities) {
      want.verbs.add(c.verb); want.objects.add(c.object);
      want.reaches.add(c.reach); want.families.add(c.family);
    }
    for (const [folder, set] of Object.entries(want)) {
      const have = new Set(((lex[folder]) || []).map(r => r.label));
      for (const w of set) {
        if (!have.has(w)) errors.push(`data/lexicon: "${w}" appears in a capability id and has no node of its own`);
        const f = path.join(D, 'lexicon', folder, `${w}.json`);
        if (!fs.existsSync(f)) errors.push(`data/lexicon/${folder}/${w}.json does not exist`);
        const page = path.join(ROOT, 'model', 'lexicon', folder, w, 'index.html');
        if (!fs.existsSync(page)) errors.push(`model/lexicon/${folder}/${w}/index.html does not exist -- every word in the grammar gets a page`);
      }
      // A word with no capability under it is meaningless in this graph. That is allowed --
      // the published grammar has two -- but it has to be DECLARED, so the gap is a recorded
      // finding rather than something that crept in.
      for (const h of have) {
        if (set.has(h)) continue;
        const rec = J(`lexicon/${folder}/${h}.json`);
        if (!rec || rec.unused !== true || !rec.unused_note) {
          errors.push(`data/lexicon/${folder}/${h}.json: no capability uses "${h}", so it is `
                    + `meaningless in this graph. That is allowed, but it must be declared: set `
                    + `unused and say why, so the gap is recorded rather than accidental`);
        }
      }
    }
  }
}());

// --- report ---------------------------------------------------------------
if (errors.length) {
  console.error(`validate: ${errors.length} error(s)`);
  for (const e of errors) console.error('  x ' + e);
  process.exit(1);
}
console.log(`validate: OK -- ${VERSION} on ${HOST}, ${htmlFiles.length} pages, `
          + `${mdFiles.length} markdown files, links resolve, every page has a twin and is in `
          + `llms.txt, the version surface agrees with version.txt, no score vocabulary, no `
          + `forbidden word, no em dash outside the promoted data, the upstream bytes hash to `
          + `their manifest, every stored delta recomputes from its own inputs, and the `
          + `graph holds: every edge has a distinct inverse, exactly one barrier walks to `
          + `[Control], and every word in the grammar has an address`);
