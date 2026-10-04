# v0.11.0: the Gmail connector measured end to end by the agent that holds it, read from a vault, mapped into the grammar, and set beside the profile read from the vendors' pages

> On 19 September the agent operating a mailbox through the Gmail connector read its own thirty tool schemas, checked them against the live permission page, sent mail with no prompt, relabelled sixteen messages in nineteen unprompted writes, hit one refusal it could not explain,...

*Source: <https://abp.sgit.ai/versions/v0.11.0/index.html> · site v0.12.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Versions](../../versions/index.md) / v0.11.0

# v0.11.0: the Gmail connector measured end to end by the agent that holds it, read from a vault, mapped into the grammar, and set beside the profile read from the vendors' pages

On 19 September the agent operating a mailbox through the Gmail connector read its own thirty tool schemas, checked them against the live permission page, sent mail with no prompt, relabelled sixteen messages in nineteen unprompted writes, hit one refusal it could not explain, and wrote the four objects into an sgit vault in the connector's own vocabulary, naming the missing join to this grammar as a gap. This release is that join. The six vault files are held verbatim and hashed; a second variant of the Gmail shape is promoted from them with every row citing its line; the agent's inferred mandate is published beside the site's starting one so the ratchet the vault warns about is a number rather than a warning; and one page on the mailbox walkthrough shows what the prompts produce when somebody runs them.

| Field | Value |
|---|---|
| Version | `v0.11.0` |
| Date | 2026-09-22 |
| Commit | **`git rev-list -n 1 v0.11.0`**. The tag is the record: CI derives it from `admin/build/version.txt` and creates it on the commit whose subject carries `site v0.11.0:`. The hash is not written into [`versions/v0.11.0.json`](../../versions/v0.11.0.json), because a release commit cannot contain its own hash and reading it back from the tag made the build produce different bytes on a checkout with tags than on one without. |
| Reconstructed | no |
| Machine readable | [`versions/v0.11.0.json`](../../versions/v0.11.0.json) |

## What changed

- data/contributed/riskmandate/gmail-agent-02n7bz55/: GRANT.md, MANDATE.md, DELTA.md, AGENTS.md, the README and the version records, copied unchanged from vault 02n7bz55 at v0.4.0 and hashed in the manifest. The raw session debrief and the operator's runbook app stay in the vault and are cited by path.
- The manifest gains a vaults list beside shapes: the vault, its version and commit, the read key published on purpose, who wrote it, what was and was not copied, and the mapping module. promote_data promotes a vault entry through that module; the gate accepts a vault entry's own retrieval time, counts vault shapes, requires every named source to be among the hashed files, and requires the read key to be in PUBLISHED.
- anthropic/gmail-connector/measured-2026-09-19: five primitives, five of five rows measured, thirty tools with their permission level, five things it cannot reach with evidence, three contradictions of which one settles the earlier profile's, four open questions, and seven things the grammar has no word for. send.message.world sits at nothing, because send_message runs with no prompt; the earlier profile's create.schedule.tenant row is absent, because no filter tool exists.
- inferred-from-one-session: the agent's own mandate, marked inferred and not elicited, wanting two primitives. The site's starting mandate for the earlier variant is extended to this one, so two deltas are stored against one grant. They differ by exactly send.message.world, which is the ratchet as a number.
- A Setting node the build derives by diffing the two variants: the per tool approval on send_message, moving one barrier between setting and nothing.
- gmail/measured/: the page. The thirty tools split by permission, the grant in the grammar, what changed against the profile read from the pages, two mandates against one grant, the vault's HARD and SOFT tags mapped onto the four barriers, three things the session found that no page had said, and what stays open.
- The hub, step one and step four of the mailbox walkthrough cite the measured deployment where it bears on them.

## What it was built against

- sgit vault 02n7bz55 at v0.4.0, commit obj-cas-imm-7ded8a06b473, cloned read only on 22 September 2026 with the read key the operator supplied.
- The earlier profile for the same shape, contributed by riskmandate.ai at v0.4.4, which the vault settles one contradiction of and does not replace.
- The house pattern of two variants of one product one setting apart, in use for the coding agent since v0.1.0.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/versions/v0.11.0/index.html)*
