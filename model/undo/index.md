# The undo class

> Three classes of reversibility, the ordering on every rendering this site produces, and the one column that is not fully context free.

*Source: <https://abp.sgit.ai/model/undo/index.html> · site v0.4.3 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [The model](../../model/index.md) / The undo class

# The undo class

**A capability that cannot be undone is a different kind of thing from one that can.** That is the whole of it, and it is the ordering on every document this site produces.

| Class | What it means |
|---|---|
| `yes` | undone by the same actor with no loss |
| `with-effort` | recoverable from a backup, a history or a revert, at a cost |
| `no` | cannot be undone |

## Why it is the ordering

An ABP that lists prohibitions alphabetically has buried the only ones that matter. **Irreversible and unbounded is the first row of every document this site produces.**

> **This is not a severity ranking and it is not a score.** Reversibility is a property of the action rather than of the context, and stating it as the reason is what keeps the ordering descriptive. The risk product reorders by consequence, because it knows the consequence. This site does not.

## The one column that is not fully context free

**Whether deleting a file is reversible depends on backups, snapshots and retention, which are the deployment's and not the product's.** So `undo: no` here is a claim about the product's published behaviour, and the deployment can change it. Saying so is the difference between a document that holds no contextual judgements and one that has smuggled one in.

[The undo classes as JSON](../../data/undo-classes.json)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/model/undo/index.html)*
