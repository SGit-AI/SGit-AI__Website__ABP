# Five worked examples

> Five Agent Behaviour Policies, one per deployment shape, derived from published data rather than authored. Each states which of its rows were measured and which were derived, and none carries a score.

*Source: <https://abp.sgit.ai/examples/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / Examples

# Five worked examples

Five ABPs, from the smallest grant in the set to a service account that outlives the turn. **They are derived rather than authored**: the rows come from a published data pack, and the delta on each page is computed when the page is built.

> **Before you read any of them, write down a number.** For a deployment you actually run, how many of the 23 capability primitives do you think it has? Most people who have deployed an agent know what they asked it to do, and almost nobody knows what it can do. The gap between your number and the table below is the reason this document type exists.

## The five, side by side

| Deployment shape | Why this one | Grant | Mandate | Excess | Unbounded excess | Irreversible | Widest reach | Measured |
|---|---|---|---|---|---|---|---|---|
| [Chat in the browser, nothing connected](../examples/chatgpt-web-no-connectors/index.md) | *The smallest grant in the set* | 1 | 1 | **0** | **0** | 0 | project | 0 of 1 |
| [A coding agent on your own machine, confirmations on](../examples/claude-code-cli-confirmations-enabled/index.md) | *The confirmation is a barrier, and you can see which row it sits on* | 16 | 5 | **12** | **12** | 8 | world | 0 of 22 |
| [The same coding agent, confirmations off](../examples/claude-code-cli-confirmations-disabled/index.md) | *The same agent, one setting different* | 16 | 5 | **12** | **12** | 8 | world | 0 of 22 |
| [A browser extension with broad host permissions](../examples/browser-extension-broad-host-permissions/index.md) | *Other people's data, and the mandate nobody wrote down* | 3 | 1 | **2** | **2** | 3 | world | 0 of 3 |
| [A CI job on a hosted runner, under a service account](../examples/github-actions-hosted-runner/index.md) | *Persistence, and reach beyond the turn* | 8 | 5 | **4** | **3** | 3 | world | 8 of 8 |

**No column here is a score.** Excess is a count of capabilities in the grant and not in the mandate. Unbounded excess is how many of those sit at a barrier that is not a control. Neither says whether any of it is acceptable, because acceptability is not in the document.

## Read the third one first

[Claude Code with confirmations on](../examples/claude-code-cli-confirmations-enabled/index.md) and [the same thing with confirmations off](../examples/claude-code-cli-confirmations-disabled/index.md) are the same product, the same machine and the same account, with one setting different. **Reading them side by side is the argument.**

> **And the pair says something the foundation document does not.** The foundation document says that turning confirmations off moves the barrier on every capability in the delta by one row. In the published data it moves exactly one barrier, on `execute.process.host`, and that capability is inside the mandate rather than in the delta: the deployer asked for it. So the label's numbers do not move at all and the document is still materially different. That is a stronger argument for the leaflet and against a headline number, and it is recorded as a disagreement in [v0.1.0's notes](../versions/v0.1.0/index.md) rather than quietly resolved.

## What each one cost to make

Nobody knows what an ABP costs to produce, and the store has to price one. So this is instrumented rather than estimated.

| Example | Time | Questions asked of a human | Note |
|---|---|---|---|
| [chatgpt-web-no-connectors](../examples/chatgpt-web-no-connectors/index.md) | 5 min | 0 | The smallest grant. Nothing new was needed once the generator existed. |
| [claude-code-cli-confirmations-enabled](../examples/claude-code-cli-confirmations-enabled/index.md) | 5 min | 0 | The first one where the barrier column carries the argument. |
| [claude-code-cli-confirmations-disabled](../examples/claude-code-cli-confirmations-disabled/index.md) | 5 min | 0 | Built second in importance and first in value. It is the same generator call against a different profile id. |
| [browser-extension-broad-host-permissions](../examples/browser-extension-broad-host-permissions/index.md) | 5 min | 0 | Three capabilities, all three irreversible. The shortest page and not the mildest. |
| [github-actions-hosted-runner](../examples/github-actions-hosted-runner/index.md) | 5 min | 0 | A service account rather than a person. The only other shape in the set with measured rows. |

> **The honest version of this table is the sentence underneath it.** The five examples took about four hours in total, and essentially all of it went into the generator, the promoted schema and the provenance line. The marginal cost of the sixth example, for a shape already in the published map, is one line in a list and a build. **That is not the number the store needs.** The number the store needs is what it costs to produce an ABP for a shape that is NOT in the map, where the grant has to be measured rather than looked up, and this site cannot tell you that yet because it has not done one. Nought questions had to be asked of a human for these five, which is the same finding from the other side: they were derived, not elicited.

## What none of these is

> **This is not an assessment.** Nothing here is an audit, a certification, a compliance assessment or a security review of any named product. It is an illustration of a method, using a published configuration, and every row carries its source, its date and whether it was measured or derived. No adjective is attached to any of it, and there is no score.

> **Provenance.** 21 of 99 capability rows on this page were measured, meaning seen directly on the thing itself. The other 78 were derived from what the deployment architecturally is, or from the vendor's published documentation. Every row traces to [the published capability map](https://what-can-it-do.games.sgit.ai/map/index.html), retrieved 2026-09-11T13:00:37Z, content hash `sha256:d6d4ba40f1fb1f93f66`. [The source bytes](../data/upstream/pack.json).

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/examples/index.html)*
