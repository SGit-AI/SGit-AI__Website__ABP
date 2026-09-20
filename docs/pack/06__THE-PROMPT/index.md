# The Prompt

> Paste this to the agent that builds the site. It is the standard prompt for a new network site, extended with what this one needs.

*Source: <https://abp.sgit.ai/docs/pack/06__THE-PROMPT/index.html> · site v0.4.2 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The pack](../../../docs/index.md#pack) / The Prompt

# The Prompt

> **The source bytes.** This page is generated from [`docs/pack/06__THE-PROMPT.md`](../../../docs/pack/06__THE-PROMPT.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**Paste this to the agent that builds the site. It is the standard prompt for a new network site, extended with what this one needs.**

Hi, can you read this brief and create the new website, just like we have the other `*.sgit.ai` websites.

As with the other sites and repos, which you have access to, can you start with the CI pipeline and auto tagging. Copy them from one named sibling repository rather than writing them, and say in your first commit message which sibling you copied from.

I have configured the repo to default to the `dev` branch and GitHub Pages is enabled. For now, please also push your branch to `dev` so that we can test the CI pipeline and see what the site looks like.

This site will go to **abp.sgit.ai**, which is already configured on this repo.

**Before you write anything, read these, in this order:**

1. `briefs/v0.33.70__foundation__agent-behaviour-policy-...md`. **It is the definition. The home page is derived from it and the what is an ABP page is it, rendered.**
2. [`00__START-HERE.md`](../../../docs/pack/00__START-HERE/index.md) in this pack. It contains one naming ruling and one finding that will change your plan.
3. `https://sgit.ai/docs/guidance/index.html`
4. `https://sgit.ai/llms.txt`
5. `https://coding.sgit.ai`
6. `https://what-can-it-do.games.sgit.ai/map/index.html`, and its `/mandates/` and `/deltas/` pages. **The ontology this site needs already exists there. Do not invent one.**
7. `https://graphs.sgit.ai` for the five graph rules, which govern the model rather than the styling.

**The name is Agent Behaviour Policy. Not Agentic. Never shortened to the policy. The reasons are in [`00__START-HERE.md`](../../../docs/pack/00__START-HERE/index.md) and they are not preferences.**

**The site owns one argument and the home page says it:** you know what you asked for, you do not know what it can do.

**The ABP is consequence agnostic. It describes and never judges, and it carries no score anywhere.** A policy cannot be dangerous; a deployment can. The score belongs on the risk product. Every page carries a label line (grant, mandate, excess, unbounded excess, irreversible, widest reach, measured, as at) and a validity statement, and no page carries a rating. [`03__THE-ABP-MODEL.md`](../../../docs/pack/03__THE-ABP-MODEL/index.md) opens with this and rule 0 of the hard rules enforces it.

**Four things this site must have that a normal site would not:**

- **A docs section** at `/docs/`, using the markdown rendering already used across the network, carrying every document in this pack and the three briefs, each one click from its source bytes.
- **A data layer** at `/data/`, promoted from the game's JSON pack into a published schema at stable addresses with cross origin access, so that the capabilities, profiles, barriers and undo classes become the network's published vocabulary rather than one game's internals.
- **Five worked examples**, derived from that data rather than authored. [`04__THE-FIRST-EXAMPLES.md`](../../../docs/pack/04__THE-FIRST-EXAMPLES/index.md) names them and says which to build first.
- **A provenance line on every page carrying capability rows**, stating how many were measured and how many derived. The map page already does this and the site must not be less careful than the game.

**Two things you must not build:** a markdown viewer, a file browser or a page layout engine, because the platform has them and the guidance forbids rebuilding them. And any checkout, price or payment link, because that is the store.

**Read [`05__THE-HARD-RULES.md`](../../../docs/pack/05__THE-HARD-RULES/index.md) before writing a single sentence about a named product.** This site publishes capability claims about nine commercial products, and rule one is the largest exposure in the repository.

**When you have the pipeline working and the first pages up, report back with:**

- Which sibling repo you copied the pipeline from, and which of the five verifications in [`02__THE-CONVENTIONS.md`](../../../docs/pack/02__THE-CONVENTIONS/index.md) that sibling failed.
- The version surface working: the version in the chrome, as a link, sourced from `versions/index.json`.
- `llms.txt` generated and listing every page.
- Which of the five examples you built and how long each took, because that number is a pricing input and nobody has it yet.

**One thing to flag rather than fix silently.** If the guidance, the style guide and this pack disagree about anything, the published source wins and the disagreement belongs in the first version's notes. The estate's method is to record the gap, not to quietly resolve it.

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/pack/06__THE-PROMPT/index.html)*
