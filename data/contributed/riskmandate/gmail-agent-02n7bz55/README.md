# One mailbox, three identities

A record of how `riskmandate.ai` was attached to an existing Google Workspace
account as a free user alias domain, authenticated with SPF/DKIM/DMARC, and
given a disclosed agent sending identity — and of what the agent standing on
that identity can actually reach.

Written to be re-run: the next domain should take twenty minutes.

## What is in this vault

### The record

| File | What it is |
|---|---|
| `index.html` | The app. Self-contained: inlined CSS, inlined JS, inlined fallback copy of the content. Opens automatically in App Mode. |
| `content.json` | Every word of the narrative record, as structured data. **Edit this, not the HTML.** |
| `RUNBOOK.md` | A plain-markdown twin of the same content, generated from `content.json`. For agents, for pasting, and for publishing. |
| `.vault/app.json` | The manifest that boots the vault into App Mode. |
| `build.py` | Regenerates `RUNBOOK.md` and re-injects the fallback data into `index.html`. |
| `versions/` | `index.json` plus one file per version. Required by the sgit.ai guidance; every entry names the vault commit it was built from. |

### The behaviour policy

Four objects for one agent in one deployment, in the vocabulary pinned at
[abp.sgit.ai](https://abp.sgit.ai/). These are the agent-readable artifacts;
the narrative versions of the same material live in `content.json` sections
`reach`, `mandate` and `barriers`.

| File | Object | State |
|---|---|---|
| `GRANT.md` | **Reach** — what the agent can actually do | Measured 2026-09-19. Not yet in the 23-primitive grammar. |
| `MANDATE.md` | **Mandate** — what the business authorised | **Inferred, not elicited.** Ten open questions. |
| `DELTA.md` | **Gap** — reach minus mandate | **Not derivable** while the mandate is inferred. The file says why. |
| `AGENTS.md` | **Barriers** — rules of engagement the agent follows | Draft. Every barrier tagged `[HARD]` or `[SOFT]`. |

`notes/session-2026-09-19.md` is the raw session debrief these were built from.
It is a working record, not one of the four objects.

## Editing it

1. Edit `content.json`.
2. Run `python3 build.py` — this re-injects the inlined fallback into
   `index.html` and regenerates `RUNBOOK.md`.
3. Add a `versions/vX.Y.Z.json` entry and bump `version.current` in `content.json`.
4. `sgit commit "..."` then `sgit push --token <token>`.
5. Write the resulting commit id into the version file and commit again — a
   version file cannot know its own commit in one pass, and a version that does
   not name the commit it was built from cannot be verified later.

Steps 2, 3 and 5 are not optional. Step 2 leaves the two copies of the content
disagreeing if skipped. Steps 3 and 5 are the requirement from
[the vault guidance](https://sgit.ai/docs/guidance/index.html), which both
agents who have worked on this vault missed on their first pass.

## The authoring contract

`index.html` follows the SG/Vault authoring contract and any edit must keep to it:

- No `<link rel="stylesheet">`, `<script src>` or `<img src>` against vault paths.
- No external resources at all — no CDNs, no web fonts, no analytics. Inline SVG
  is the graphics format.
- Vault data is read with `sg.vfs.readText()`. Plain `fetch()` of a vault path
  does not work; it is present only as a static-hosting fallback.
- `{type:'sg-app-ready'}` is posted to the parent on both the success and the
  error path, or the host shows its loading overlay forever.
- No query strings in internal links.

Reference: https://sgit.ai/docs/vault/vault-apps.html

## Validating before you push

```
python3 build.py
node --check <extracted script body>
grep '<link .*href=|<script .*src=|<img .*src=' index.html    # want zero
python3 -c "import json;json.load(open('content.json'))"
```
