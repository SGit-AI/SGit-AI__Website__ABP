# Case estate-002: One person, three surfaces of one product, one account holding every past conversation

> A deployer who runs one assistant in the browser, as a coding agent and as a desktop work product, over one account that holds every past conversation. The mandates elicited around one rule: reading the past is on demand.

*Source: <https://abp.sgit.ai/cases/estate-002/index.html> · site v0.10.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../index.md) / [Cases](../../cases/index.md) / estate-002

# One person, three surfaces of one product, one account holding every past conversation

**A deployer who runs the same assistant in the browser, as a coding agent and as a desktop work product, and who knows the past conversations contain secrets.** Three surfaces, one account, and a record of past conversations that the deployer treats as a credential store. Everything below was elicited on 2026-09-22; nothing was measured.

> **Where the words on this page came from.** One voice memo by the deployer on 22 September 2026, transcribed automatically; every quoted fragment was checked against it. **Nothing here is measured except the coding agent's shape**, which was measured by the thing being profiled on 5 September. The browser shape is derived, the desktop product has no shape, and the deployer has not yet corrected the draft.

## The estate

*[A figure here in the page: one person at the top, connected to three surfaces of the same product: in the browser with connectors possibly on, the coding agent in a measured container, and the desktop work product with no published shape. All three sit over one account with the vendor, which holds the record of every past conversation on every surface plus the connectors. The browser and desktop arrows are labelled reads with a question mark; the coding agent's is labelled reads its own. The union runs in time as well as across surfaces: everything ever pasted is in the record]*

| Deployment | Consent | Nearest published shape | The mandate | Delta |
|---|---|---|---|---|
| [Claude in the browser, with connectors possibly still on](../../cases/estate-002/claude-web/index.md) | unknown: "I might still have some connectors enabled" | [`anthropic/claude-web/connectors-on`](../../examples/index.md) | 1 wanted, 2 refused, 20 unstated | 4 excess, 0 unbounded (provisional) |
| [Claude Code, in a container with a repository attached](../../cases/estate-002/claude-code/index.md) | the harness's permission mode | [`anthropic/claude-code-remote/ccr-container`](../../examples/index.md) | 3 wanted, 2 refused, 18 unstated | 12 excess, 9 unbounded (provisional) |
| [Claude Cowork, on the desktop](../../cases/estate-002/claude-cowork/index.md) | unknown | **none published** | 0 wanted, 2 refused, 21 unstated | no shape to compute against |

## The account is the junction, and this time it holds the record

Three surfaces run over **one account with the vendor**. The account holds the conversation record and the connectors. Whatever any surface can reach of the record, the account's exposure is the union across the three, and across every conversation that ever happened on any of them.

The first case had four grants over one Google account and the finding was that the account's exposure is their union. Here the union runs in time as well as across surfaces: **everything ever pasted into any conversation is in the record, and turning reading off today does not take it out.** A mandate over this estate has to say what to do about what is already there, not only what to do next.

## What matters, and what does not

The deployer named the concept this case turns on: what is being given to the agent is context on what is important and what is not. **A mandate is that list before it is a list of prohibitions.** So the clauses on every page below open with it.

|  | What the deployer said, or what follows from it |
|---|---|
| **Matters most** | the record of past conversations, because it contains secrets; the repository, because it is the work |
| **Matters, unknown** | whichever connectors are still enabled; nobody has listed them |
| **Does not matter** | the container's own files, which are disposable; the session's own earlier tool outputs, which are not a past conversation |
| **Must never be reused** | a key, token, password or credential found anywhere in the record |

## What they told us

- **The record contains secrets.** "past messages, which I think actually contain quite a number of secrets. It contains quite a lot of data." Things get pasted into a chat that would never be committed to a repository, and the chat keeps them.
- **Reading the past should be on demand.** "that should always be an on-demand thing." Not never: on demand, named, in the conversation that needs it. The grammar has a primitive for reading a retained record and no word for when.
- **Some connectors may still be on.** "I might still have some connectors enabled." Which is the first open question, and each one is a deployment of its own.
- **The question is blast radius, then policy.** "I want to understand the blast radius, and then I want to start to see what policies can I put in place... especially taking into account the exposure." The exposure is what is already in the record; the blast radius is what each surface can do with it.
- **What is being given is context on what matters.** "we're giving agent context on what's important, what's not important, and I think that's an important concept." The mandate as an importance list before it is a list of prohibitions.

## Open questions the deployer can answer

Each of these changes a mandate or a barrier on one of the pages below, and none of them can be answered from here.

1. **Which surfaces can read past conversations, and is it on by default?** The deployer believes one or all of the three can. The measured coding agent shape says its container holds only the session's own tool outputs; the other two are not measured. Prompt A asks each surface directly.
2. **Which connectors are enabled on the account today?** Each one is a deployment with its own grant, and the browser shape's five rows are placeholders until they are named.
3. **Does Claude Code here mean the web container, the CLI on a machine, or both?** The web container is measured and its host is the container. The CLI's host is the machine, with the deployer's own credentials in the home directory, and it is a different case.
4. **What does the desktop work product expose?** Local files, applications, connectors, the record: nothing this site has read describes it, and its page holds no shape.
5. **Are past conversations shared across the three surfaces?** If they are, the record is one credential store with three readers; if not, the exposure is per surface. The answer decides whether the estate has one junction or three.
6. **Can the secrets already in the record be found and removed?** A purge is itself a read of the record by something, and that something needs a mandate of its own.

## The first prompt, for all three surfaces

Paste it into the browser, into the coding agent and into the desktop product, separately. Three answers over one account, and the differences are the estate.

**Prompt A: The record, from the inside.** Run it on each surface. It asks about the past, the connectors and what has already been read.

```
Four questions about this surface, and answer for this surface only.

  1. Can you read our past conversations? Which ones: only this surface's, or the whole
     account's? Is that on by default, or only when I ask? If you cannot tell, say so.
  2. Have you read anything from a past conversation in this session? Name it.
  3. Which connectors are enabled on my account right now, and which of them can you use
     from here? For each, does it ask me first?
  4. If a past conversation contained a password or a key, what would you do with it if
     you came across it?

Answer with what you can actually see. Mark INFERRED on anything you are guessing.
```

## The 3 deployments

**[Claude in the browser, with connectors possibly still on](../../cases/estate-002/claude-web/index.md)**: the derived shape for the web assistant with connectors switched on, 0 of 5 rows measured. Which connectors is the deployer's to name and they have not named them yet, so the shape may be wider or narrower than this deployment by every connector row.
2 said, 1 inferred, 20 unstated

**[Claude Code, in a container with a repository attached](../../cases/estate-002/claude-code/index.md)**: the shape this site is maintained from, measured by the thing being profiled, 13 of 20 rows seen on the container itself. If the deployer also runs the CLI on their own machine, that is a second deployment with a different reach for host, and it is an open question.
4 said, 1 inferred, 18 unstated

**[Claude Cowork, on the desktop](../../cases/estate-002/claude-cowork/index.md)**: no published shape, and nothing this site has read documents what the product exposes: which local files, which applications, whether it reads past conversations, and on what approval. The gap is declared.
1 said, 1 inferred, 21 unstated

## Out of scope

- Whichever connectors turn out to be enabled. Each is a deployment of its own once named, with the mailbox walkthrough's prompts ready for it.
- The CLI on the deployer's own machine, if they run it. It is a different shape with a different host, and the site holds a derived profile for it.

> **Nothing on this site is an assessment, an audit, a certification or a security review of any named product**, and no adjective on this page attaches to one. A case describes one person's deployments in their own words and against published shapes with their sources and dates.

[The case as JSON](../../data/cases/estate-002/case.json) &#183; [The walkthroughs the prompts come from](../../gmail/index.md) &#183; [The estate universe](../../model/universes/u9/index.md)

---

*[Site index for agents](../../llms.txt) · [HTML version](https://abp.sgit.ai/cases/estate-002/index.html)*
