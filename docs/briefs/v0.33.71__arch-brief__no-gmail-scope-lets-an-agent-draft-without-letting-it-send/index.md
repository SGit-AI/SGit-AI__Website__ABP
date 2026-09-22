# No Gmail Scope Lets An Agent Draft Without Letting It Send: The Drafts Have To Leave The Mailbox, And The Trifecta Is Broken By Credential Rather Than By Classifier

> version v0.33.71 date 20 September 2026 from Human (project lead) to Architecture, the Agent Behaviour Policy team, whoever builds the inbound pipeline for the published address, and legal

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__no-gmail-scope-lets-an-agent-draft-without-letting-it-send/index.html> · site v0.8.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / No Gmail Scope Lets An Agent Draft Without Letting It Send: The Drafts Have To Leave The Mailbox, And The Trifecta Is Broken By Credential Rather Than By Classifier

# No Gmail Scope Lets An Agent Draft Without Letting It Send: The Drafts Have To Leave The Mailbox, And The Trifecta Is Broken By Credential Rather Than By Classifier

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.71__arch-brief__no-gmail-scope-lets-an-agent-draft-without-letting-it-send.md`](../../../docs/briefs/v0.33.71__arch-brief__no-gmail-scope-lets-an-agent-draft-without-letting-it-send.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.71 **date** 20 September 2026 **from** Human (project lead) **to** Architecture, the Agent Behaviour Policy team, whoever builds the inbound pipeline for the published address, and legal

**type** Architecture brief

*Written from a memo asking two things: what the field currently considers best practice for operating a mailbox that is exposed to the outside world and therefore a prime target for injection, and how to split that work across several agents with several mandates so that the agent reading hostile mail is not the agent able to act on it. The memo proposes four or five stages and correctly anticipates that the current assistant environment may not let one account hold several permission profiles. Research was carried out on 20 September 2026 across the primary literature, vendor guidance, model cards and the platform's own interface reference, and one platform fact was checked directly because the whole architecture turns on it. Limitations: pages were read through fetch tooling and two figures are flagged in the text as reported rather than primary; the pipeline below has not been built or measured; the legal section is an engineering summary of where the obligations fall and is not legal advice, and a qualified adviser should see it before anything processes third party mail; no vendor has been approached; and the memo's suggestion of running a local model has been costed by model size rather than by benchmark on real mail.*

## What This Is

The state of the art, and the one platform fact that rewrites the memo's design: **the memo proposes splitting mailbox work across four or five agents so that the one reading untrusted mail cannot act, the one deciding cannot write, the one writing cannot send, and a last one sends or defers to a human, with a monitor over all of it; the field agrees with that instinct and has formalised it, since the governing formulation is that an agent is exposed when it combines access to private data, exposure to untrusted content and the ability to communicate externally, and the published defence is to prevent those three from meeting rather than to detect the attack, with a family of six named design patterns and one system, built on control and data flow separation with capabilities enforced at the tool call, demonstrating provable resistance at a measured cost of roughly three times the tokens and seven percentage points of task success; the evidence that detection alone is not a control is unusually strong, running from a production classifier being bypassed as step one of a zero click exploit against a mail assistant with a CVE attached, through benchmark work reporting detection rates on indirect injections falling to between seven and thirty seven per cent under realistic distribution shift, to both major vendors stating in their own words that model layer protection will never be fully effective and cannot stand alone; the platform fact that changes the memo's plan is that creating a draft and sending a draft require exactly the same three scopes, so there is no grant in the catalogue that lets an agent compose without also letting it send, which means the memo's third agent cannot be bounded by any scope and the separation has to be achieved by taking the mailbox credential away from it entirely; the correction that follows is that drafts belong in the vault rather than in the mailbox, which removes the credential from the drafting stage, gives every draft a history and a reviewable form, and leaves a final stage holding one narrow send scope and no read access at all, so that stage is outside the trifecta by construction because it never sees untrusted content; the memo's suspicion about profiles is correct and the remedy is not profiles but credentials, since connectors attach to an account rather than to a conversation and the only reliable isolation is a different credential per stage, which the estate's own vault keys and append lane already provide as a transport; a classifier tier that runs on ordinary hardware exists and is small, with the relevant models in the twenty two million to two hundred million parameter range and published recall figures, but it belongs at the expectation layer and must be described that way; routing inbound mail through a third party inference router puts the operator in the position of a controller handling other people's correspondence, which is answerable but only with retention disabled, provider routing constrained and an agreement in place; and there is a well evidenced list of companies that already fund open work in this exact area, several of which were acquired in the last eighteen months.** New contributions: **the draft and send scope identity, checked and stated as the architectural constraint; drafts relocated to the vault with the reasons; the final stage placed outside the trifecta by removing its read access; credentials rather than profiles as the separation mechanism, with the estate's existing keys and lane as the substrate; each stage mapped onto a published design pattern so the architecture is citable rather than invented; the honest cost stated from the literature; the routing question answered with the specific settings that make it defensible; and a sponsorship list drawn from organisations with a public record of funding this work.**

## What The Field Actually Agrees On

**There is more consensus here than the memo expects, and it is not the consensus a vendor would prefer.**

**The governing formulation is the lethal trifecta**, published by Simon Willison on 16 June 2025: an agent is exposed when it has access to private data, exposure to untrusted content, and the ability to communicate externally. A mailbox agent has all three by definition, which is why the published address is the hardest case the estate has taken on rather than a convenient demonstration. **The recommended mitigation is architectural avoidance, meaning the three conditions must not meet in one agent, and explicitly not a better filter.**

**The mechanism has a lineage.** The dual pattern, in which a privileged component holds the tools and a quarantined component handles untrusted content and returns only symbolic references, was described in April 2023. It was formalised in March 2025 by a team at Google DeepMind and ETH Zurich in a system that extracts control and data flow from the trusted query so that untrusted data can never affect the program flow, tags every value with a capability, and enforces policy at the tool call. On the standard agent benchmark it solved 77 per cent of tasks with provable security against an undefended baseline of 84 per cent, at a median cost of 2.82 times the input tokens and 2.73 times the output tokens.

**Six design patterns were then named in June 2025 and the memo's pipeline is three of them stacked.**

| Pattern | What it does | Where it appears below |
|---|---|---|
| Action-Selector | The model picks from a fixed menu and outputs never re-enter its context | The send stage |
| Plan-Then-Execute | The plan is fixed before untrusted output is seen | The decide stage |
| LLM Map-Reduce | Each untrusted document is processed by an isolated call and results aggregated | The classify stage, one message at a time |
| Dual LLM | Privileged holds tools, quarantined handles untrusted content and returns references | The split between classify and decide |
| Code-Then-Execute | A program rather than a plan runs over the untrusted data | Not used in version one |
| Context-Minimisation | Unnecessary context, including the original instruction, is stripped once no longer needed | Between every stage |

**So the memo is not proposing something novel and that is the good news.** It is proposing a specific arrangement of patterns with names, papers and measured costs, which means the architecture can be cited rather than defended from first principles.

## Detection Is Not A Control, And The Evidence Is Unusually Strong

**The estate's own enforcer test already says a filter the agent's own stack contains is not a barrier. The field's evidence says the same thing empirically, and it is worth having the citations to hand because somebody will propose buying a classifier instead of building the pipeline.**

**A production classifier was bypassed as step one of a real exploit.** The vulnerability known as EchoLeak, carrying CVE-2025-32711, was a zero click chain against a mail assistant in which a single crafted email was ingested by the retrieval pipeline without the user opening it. The first step evaded the vendor's own cross prompt injection classifier; the remaining steps defeated link redaction, triggered an outbound request through automatic image fetching, and exfiltrated through a domain already on the content security policy allowlist. **The severity figure circulating for it comes from a third party writeup rather than the vendor advisory and should be treated as reported.**

**Benchmark work says detection generalises badly in exactly the case that matters.** An evaluation under leave one dataset out conditions reports that standard protocols overstate performance by more than eight points of area under the curve, that detection rates on indirect injections, described there as the primary threat vector for autonomous agents, fall to between seven and thirty seven per cent, and that two widely deployed guard models cannot evaluate tool level injection at all for architectural reasons. **The authorship of that paper could not be confirmed to a citable standard and the numbers should be quoted as reported rather than established.**

**And both major vendors say it themselves.** One states that protection in the model layer will never be fully effective and is why it cannot stand alone, and that containment works by supervising what an agent is able to do rather than what it does. The other describes a five layer strategy in which classifiers are the first of five and deterministic confirmation and sanitisation are separate layers. **Neither claims the problem is solved, and one says so in those words.**

**The operational conclusion for this estate is a single sentence to put on the page: a classifier changes the odds and a credential changes what is possible.**

## The Finding That Rewrites The Memo

**The memo's third stage writes drafts and must not be able to send them. That separation cannot be expressed in the platform's permission catalogue, and this was checked directly.**

**Creating a draft requires one of three scopes: the full mailbox scope, the modify scope, or the compose scope. Sending a draft requires exactly the same three.** The compose scope is described by the platform as managing drafts and sending emails. There is no draft only scope, no send inhibit flag, and no way to hold the first capability without the second.

**So an agent that can write a draft into the mailbox can send it, and nothing in the grant prevents that.** Under the four barrier model, an instruction telling the drafting agent not to send is an expectation, and an expectation at the top of the stack is the weakest thing in the architecture. This is the third time in two days that a control the estate wanted turned out to be unexpressible in this platform's scopes, after the absence of any bound by label, correspondent or topic, and the identity between filing a message and clearing somebody's task list.

**The fix is not to find a better scope. It is to take the mailbox away from the drafting stage.**

## The Corrected Pipeline

**Five stages, and the change from the memo is that only two of them hold a mailbox credential at all.**

| Stage | What it does | Mailbox credential | Sees untrusted content | Can communicate outward |
|---|---|---|---|---|
| 0 Fetch | Pulls new messages, writes each to the vault unmodified with its hash | Read only | Yes, as bytes, and does not interpret them | No |
| 1 Classify | One message at a time, in isolation: extract structure, classify intent, flag injection | **None** | Yes | **No** |
| 2 Decide | Plans actions from classification, metadata and references, not from bodies | **None** | Only through references | No |
| 3 Draft | Writes proposed replies and actions into the vault as a reviewable plan | **None** | Only what stage 2 passed | No |
| 4 Send | Sends an approved artefact from the vault, or routes it to a human | Send only | **No** | Yes |
| 5 Monitor | Reports over the vault: counts, flags, what was sent, what was refused | Read only, or none | Only summaries | No |

**Three properties of that table are the whole design.**

**Stage 1 is the quarantined component and it must have no way out.** It reads one hostile message and returns structured data. No mailbox credential, no vault write beyond its own output path, and no network egress except to whatever model serves it. One message per call, never a batch, because processing several in one context lets one message speak about another. **This is the map step, and its isolation is the reason the map pattern works.**

**Stage 4 is outside the trifecta by construction, because it has no read access.** It holds the send scope, which is in the platform's middle sensitivity tier rather than its widest, and it never sees inbound mail. **An agent that cannot read attacker text cannot be instructed by it.** That single property is worth more than every classifier in the pipeline, and it only becomes available once drafts have left the mailbox.

**And the drafts live in the vault, which was forced by the scope finding and is better on four other counts.** Every draft has a history and an author. A draft is reviewable in a form a person can read before anything is sent. The vault's own permission model gives each stage a key rather than a promise. And a draft in the vault is the plan object argued for yesterday, so the human approves a document rather than a sequence of prompts.

**Two lanes come out of stage 4 and they are not the same.** Mail sent as the published address is sent by the agent from an approved artefact. Mail to be sent as the project lead personally is never sent by any agent; it is delivered to him as a draft he sends himself, and no component in the pipeline holds a credential that could do otherwise.

## Separation Needs Credentials, Not Profiles

**The memo suspects the current assistant environment cannot give one account several permission profiles, and that suspicion is the right one to act on.** Connectors attach to an account rather than to a conversation, so two conversations in one account reach the same tools, and an instruction that one of them must not use a tool it can reach is an expectation.

**The remedy is one credential per stage, and the estate already has the substrate.**

**Different mailbox identities for different stages.** The fetching stage authorises with a read scope. The sending stage authorises separately with a send scope. They are different authorisations even where they concern the same mailbox, and neither holds the other's capability.

**Vault keys as the isolation between stages.** Each stage gets a key that can write only its own output path and read only its input path. This is the same declared mount discipline the vault platform already enforces, and it means the boundary between stages is enforced by the host rather than by the agents' good behaviour.

**And the append lane as the transport.** A message from one stage to the next is one flat put outside the commit tree, gated by a published key, which is what the lane was built for. **The pipeline's inter stage bus already ships.**

**What the estate should still test, because the memo asks and it matters, is whether any of the available environments can survive compromise of one stage.** The relevant published claims describe ephemeral containers, sandboxed execution with a human in the loop, and sealed virtual machines as three different isolation postures. **Which of those the pipeline can actually obtain, for which stage, is an experiment rather than a reading exercise, and it should be run before the address takes real traffic.**

## The Classifier Tier That Runs On Ordinary Hardware

**The memo asks whether a local model could do the first pass. It can, the models are small, and the honest framing is that this tier improves the odds and bounds nothing.**

| Model | Size | Licence | Published figure |
|---|---|---|---|
| Prompt-Guard-2, small | 22M | Community licence | Recall 88.7 per cent at 1 per cent false positives, about 19 milliseconds per inference on a datacentre card |
| Prompt-Guard-2, large | 86M | Community licence | Recall 97.5 per cent at 1 per cent false positives |
| A DeBERTa based injection classifier | About 200M | Apache 2.0 | 95.25 per cent accuracy on a held out set, English only, and its own card warns against using it on system prompts because of false positives |
| A guard model tuned against over defence | About 200M | MIT | Claims a large improvement over prior work on a benchmark built for false positive resistance |
| A small edge safety model | 1B, quantised variant available | Community licence | Built for laptop and mobile deployment |

**Two of the toolkits the memo might otherwise reach for are archived and should not be built on**, one since May 2025 and the other since July 2026. The actively maintained open framework in this area bundles a classifier with a reasoning trace auditor and a static analysis component.

**The rule for the estate is the one it already applies everywhere else.** A local classifier in stage 1 is an expectation barrier. It is worth having because most inbound harm is opportunistic rather than adaptive, it costs almost nothing, and it runs without sending anything anywhere. **It must never appear in a published artefact as a control, and the pipeline must be correct with the classifier removed.**

## Routing Other People's Mail Through A Third Party

**The memo raises this itself and is right to. The moment inbound mail is sent to an external model, the operator is processing correspondence written by people who never agreed to it, and the position is answerable but only with the settings set correctly.**

**The obligations fall in a specific place.** The operator decides why and how the mail is processed, so the operator carries the controller's duties for third party personal data arriving unsolicited. An inference router and the models behind it act on the operator's instructions, so they are processors and sub processors, which requires an agreement, a known list of who the data reaches, a lawful basis, a retention position and a transfer position.

**The router the memo names does support the necessary posture and the specifics matter.** Zero retention can be set account wide, per model group, per key or per request. Provider routing can be constrained with an allowlist, a denylist, and a flag that excludes providers who may retain data for training. The company states it does not itself train on inputs, while warning that some downstream providers may. Retention exemption applies to inference routing only and explicitly not to plugins and tools such as web search. A named sub processor list exists behind the trust portal, and a signed agreement is described in their own help material as available to enterprise tier customers, with self serve customers able to view it for information only.

**So the defensible configuration is narrow and should be written down as a requirement rather than a preference:** retention off at the account level and asserted again per request, an explicit provider allowlist, the training exclusion flag set, no plugins or tools enabled on those calls, and the agreement in place before the address is advertised. **If the agreement is genuinely unavailable at the tier the estate is on, the honest options are to self host the classifier, which the previous section shows is feasible, or to say publicly that inbound mail is processed by a named third party.**

**Two further duties are easy to forget and cheap to meet.** People writing to a published address should be told what happens to their message, which is a line on the page the address appears on. And the vault copy of inbound mail is a retention decision: it needs a period, and somebody has to be able to delete a message on request.

## Who Already Funds This Work

**The memo asks about sponsorship, and there is a better list than guesswork: the organisations that already pay to support open work on exactly this problem.** The sponsor roster of the main open community in this field includes, at its upper tiers, the acquirers of three of the four best known startups in this space, alongside several independent companies.

**The consolidation is worth knowing before approaching anybody.** Four acquisitions are confirmed across the last two years: one classifier company acquired in September 2025 for a figure reported around three hundred million, one runtime firewall acquired in August 2025 for a figure reported around two hundred and fifty million, one agent guardrail company acquired in June 2025, and one earlier acquisition completed in 2024. A fifth company, whose open source projects are the two archived toolkits mentioned above, was acquired in 2025 and its open work has gone quiet since, which is a pattern worth noting in any conversation about sponsoring the estate's own open material.

**Several significant companies in this space remain independent and recently funded**, with raises in 2026 of a hundred million, a hundred and twenty five million and fifty eight million respectively among them.

**The approach that fits the estate's position is not a request for money for a product.** It is an offer of a published, permissively licensed, vendor neutral description of what a mailbox agent's grant actually contains, which is a gap none of these companies fills because each sells a layer rather than a record. **The one genuinely under served niche the research surfaced is mailbox specific guarding as a category of its own**, currently addressed either as a feature bolted onto an existing mail security suite or generically by agent security platforms for which mail is one connector among many.

## What This Does Not Try To Be

**It is not an implementation.** Five stages, their credentials and their transport are specified. No code was written and nothing was measured.

**It is not legal advice.** Where the obligations fall and which settings make the routing question answerable are stated as an engineering summary. A qualified adviser should see it before the address processes anybody else's mail.

**It is not a benchmark of the classifiers.** Published figures are reproduced with their sources. None was run against real mail, and the false positive behaviour on ordinary business correspondence is the number that will actually decide whether the tier is usable.

**It is not a vendor evaluation.** Companies are named because they fund open work in this area, not because their products were assessed.

**And it does not claim the pipeline resists a determined adversary.** It claims the pipeline removes the conditions under which a successful injection can do anything, which is a different and smaller claim.

## Honest Tensions

**The architecture costs about three times the tokens and some task success, on the only published measurement of a comparable design.** For a mailbox handling tens of messages a day that is irrelevant. It becomes relevant at exactly the point the estate would want to point at the pipeline as a product, and the figure should be quoted rather than discovered.

**Moving drafts out of the mailbox is correct and it breaks the thing users expect.** People look in their drafts folder. A draft in a vault is safer, reviewable and versioned, and it is somewhere nobody thinks to look. The monitoring stage exists partly to solve this and monitoring is not the same as habit.

**Stage 2 is supposed to plan from references rather than bodies, and sooner or later it will need the body.** The moment a planner reads attacker text to decide what to do, the dual pattern has been broken quietly and nothing will announce it. The discipline is that the body goes to a human, not to the planner, and it will be inconvenient in precisely the cases that matter most.

**The local classifier is cheap enough that it will be trusted more than it should be.** Small models with headline recall figures near 90 per cent read as reliable. Under distribution shift on indirect injections the field's reported numbers are far worse, and the pipeline's correctness must not depend on the classifier being right.

**And the sponsorship path has a shape the estate should notice.** Of the best known open projects in this space, the two most widely used were archived after their owner was acquired. Taking money from an acquirer is not the same as taking money from a company whose survival depends on the open thing continuing, and the estate's material is the kind that has to outlive a funding round.

## Open Questions

**Can two separate mailbox authorisations for the same account be held cleanly, one read and one send, in the environments the estate actually runs?** The architecture assumes yes. This is a one hour test and everything depends on it.

**Does any available environment survive compromise of one stage?** The vendors describe three isolation postures. Which are obtainable here, for which stage, is unmeasured.

**What is the false positive rate of the small classifiers on ordinary business mail?** Published figures come from attack benchmarks. A classifier that flags one legitimate message in twenty is unusable no matter what its recall is.

**Does the router's agreement become available at the estate's tier, and if not, does the pipeline self host the classifier or disclose the third party?** This is a decision, not a question, and it should be made before the address is advertised.

**What is the retention period for inbound mail held in the vault, and who can action a deletion request?** Both are unanswered and both are obligations.

**And should the pipeline be published as the estate's own worked example?** It is a mailbox exposed on purpose, with a described grant at every stage and named gaps, which is the estate's method applied to itself in the hardest available case. The argument against is that publishing the architecture of a live target tells an attacker exactly which stage to aim at.

## Relationship To Previous Briefs

| Date | Document | Relationship |
|---|---|---|
| 12 Sep | The correction that a guardrail is a property of one deployment rather than of the model | The classifier tier is placed at the expectation layer on exactly this reasoning |
| 19 Sep | The brief on the consent dialog | Supplies the scope catalogue, the sensitivity tiers and the enforcer test used to place each stage |
| 19 Sep | The brief on the inbox persona | Supplies plan level consent, which the vault held draft now implements as an object |
| 20 Sep | The brief on the behaviour policy as a fractal | The ladder of enforcers predicted this result: the only boundaries are next to the platform, and here the platform offers none for drafting |
| 20 Sep | The brief on users and the missing free rung | The pipeline is the estate's own dogfooding case, and its monitor is the report that brief asks the project lead to hold |

## Key Claims

| # | Claim |
|---|---|
| 1 | Creating a draft and sending a draft require the same three scopes, so no grant permits composing without permitting sending |
| 2 | The drafting stage therefore cannot be bounded by any scope, and the separation must be achieved by removing its mailbox credential entirely |
| 3 | Drafts belong in the vault, which removes the credential, gives each draft a history and a reviewable form, and makes the draft the plan object |
| 4 | The sending stage holds a send scope and no read access, so it never sees untrusted content and is outside the trifecta by construction |
| 5 | The governing formulation in the field is that private data, untrusted content and external communication must not meet in one agent |
| 6 | The memo's pipeline is three published design patterns stacked, so the architecture can be cited rather than defended from first principles |
| 7 | The only published measurement of a comparable design reports about 2.8 times the input tokens and seven points of task success as the cost |
| 8 | Detection is not a control: a production classifier was bypassed as step one of a zero click exploit against a mail assistant with a CVE attached |
| 9 | Both major vendors state in their own words that model layer protection cannot stand alone, and neither claims the problem is solved |
| 10 | Connectors attach to an account rather than a conversation, so separation needs one credential per stage and the vault keys and append lane already provide the substrate |
| 11 | Injection classifiers small enough to self host exist at 22M to 200M parameters, and two widely used open toolkits in this area are now archived |
| 12 | Routing inbound mail to a third party makes the operator a controller of other people's correspondence, and is defensible only with retention off, provider routing constrained, no tools enabled and an agreement in place |

## Sources

- The platform's draft creation and draft sending references, read 20 September 2026 for the identical scope lists that make the drafting stage unboundable. https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/create
- The platform's scope catalogue, for the three sensitivity tiers and the description of the compose scope as managing drafts and sending emails. https://developers.google.com/workspace/gmail/api/auth/scopes
- Simon Willison, "The lethal trifecta for AI agents: private data, untrusted content, and external communication", 16 June 2025. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Simon Willison, "The Dual LLM pattern for building AI assistants that can resist prompt injection", 25 April 2023. https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
- Debenedetti, Shumailov, Fan, Hayes, Carlini, Fabian, Kern, Shi, Terzis and Tramer, "Defeating Prompt Injections by Design", for control and data flow separation, the capability model, the benchmark result and the token overhead. https://arxiv.org/abs/2503.18813
- Beurer-Kellner and others, "Design Patterns for Securing LLM Agents against Prompt Injections", for the six named patterns used in the stage mapping. https://arxiv.org/abs/2506.08837
- Reddy and Gujral, "EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System", for the four step chain beginning with classifier evasion. https://arxiv.org/abs/2509.10540
- Anthropic engineering, "How we contain Claude across products", for the statement that model layer protection can never be fully effective and for the three isolation postures. https://www.anthropic.com/engineering/how-we-contain-claude
- Anthropic, "Mitigating the risk of prompt injections in browser use", 24 November 2025, for the residual attack success rate and the statement that the problem is not claimed solved. https://www.anthropic.com/news/prompt-injection-defenses
- Google security blog, "Mitigating prompt injection attacks with a layered defense strategy", 13 June 2025, for the five layers. https://blog.google/security/mitigating-prompt-injection-attacks/
- The OWASP Top 10 for LLM applications, prompt injection entry, for the seven mitigation strategies. https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- NIST AI 100-2e2025, for the separation of direct prompting attacks from indirect prompt injection executed through resource control. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- Model cards for the small injection classifiers, for sizes, licences and published recall figures. https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
- The inference router's data policy, retention guide and provider routing documentation, for the retention controls, the routing constraints, the statement on downstream training and the agreement availability. https://openrouter.ai/docs/guides/features/zdr
- The open community's public sponsor roster, for the organisations with a record of funding work in this area. https://genai.owasp.org/supporters/
- The project lead's voice memo of 20 September 2026, for the five stage proposal, the profile limitation, the local model question, and the routing and legality questions

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__no-gmail-scope-lets-an-agent-draft-without-letting-it-send/index.html)*
