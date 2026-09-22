# The Split Does Not Break The Trifecta, The Schema Does: A Closed Vocabulary At The Boundary Is The Control, And The Orchestrator Should Not Hold The Mailbox

> version v0.33.71 date 20 September 2026 from Human (project lead) to Architecture, the Agent Behaviour Policy team, whoever writes the command line tool and the vault application

*Source: <https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__the-split-does-not-break-the-trifecta-the-schema-does/index.html> · site v0.10.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [Docs](../../../docs/index.md) / [The briefs](../../../docs/index.md#briefs) / The Split Does Not Break The Trifecta, The Schema Does: A Closed Vocabulary At The Boundary Is The Control, And The Orchestrator Should Not Hold The Mailbox

# The Split Does Not Break The Trifecta, The Schema Does: A Closed Vocabulary At The Boundary Is The Control, And The Orchestrator Should Not Hold The Mailbox

> **The source bytes.** This page is generated from [`docs/briefs/v0.33.71__arch-brief__the-split-does-not-break-the-trifecta-the-schema-does.md`](../../../docs/briefs/v0.33.71__arch-brief__the-split-does-not-break-the-trifecta-the-schema-does.md), which is served unchanged. Anything rendered on this network stays one click from the file it came from.

**version** v0.33.71 **date** 20 September 2026 **from** Human (project lead) **to** Architecture, the Agent Behaviour Policy team, whoever writes the command line tool and the vault application

**type** Architecture brief

*Second of 20 September on the exposed mailbox, following the brief that established that no scope permits drafting without permitting sending. This one responds to a proposed architecture: three classes of execution environment, of which the first and the third are combined, with an orchestrating session holding the mailbox connector and a sequence of stateless model calls holding none, a state machine in the vault describing the control flow, a behaviour policy at two altitudes, every request and response written to an append only vault for provenance, a command line tool in Python living in a vault, and a second vault holding the data and a representation of the mailbox with a visual application over it. Two platform facts were checked on 20 September 2026 because the design turns on them: whether schema conformance can be enforced on a model response rather than validated after the fact, and what the calls actually cost. Limitations: nothing was built or measured; the cost figures are arithmetic over assumed token counts and are labelled as such; the claim about what the orchestrating session can be prevented from doing is reasoning from the published permission model rather than from a test, and the one hour test named in the previous brief still has not been run.*

## What This Is

A proposed architecture, one structural correction that decides whether it works, and the platform feature that makes the correction enforceable: **the memo separates three classes of execution environment, being a full session with connectors that can read, decide and act and is therefore the most exposed thing in the estate, an interface driven agent wired to tools whose outputs feed back into its own reasoning, and a single stateless call to a model with no tools at all where an injection can land in the answer but has nothing to act with, and it proposes building the mailbox workflow out of the first and the third while avoiding the second, with the stateless calls doing every piece of work that touches hostile text and the session doing only orchestration over structured results, a state machine in the vault expressing the control flow, a behaviour policy at both the individual action altitude and the whole workflow altitude, and every request and response written to an append only vault so that nothing is unexplainable after the fact; the classification is correct and the third class is genuinely different in kind, because safety there is a property of the deployment rather than of the model, which is the estate's own ruling of 12 September arriving as an architecture; but the split alone does not break the trifecta, because the moment the stateless call's output is read by the session that holds the mailbox and the ability to send, the three conditions have reassembled across the boundary rather than inside one agent, and an attacker who cannot act directly can still write the text that the acting component reads; the correction is therefore that the boundary must carry a closed vocabulary rather than free text, and the platform now enforces exactly that, since a response can be constrained by a JSON schema during decoding rather than validated afterwards, which means enumerated fields, booleans, numbers and identifiers are genuinely bounded while any open string field remains attacker influenced and must never enter the orchestrating context; the state machine is a real control only if something other than the orchestrator enforces it, so it belongs to the command line tool rather than to the session that is supposed to follow it; the same argument applied to the mailbox itself says the orchestrator should not hold the connector at all, because a session holding the union of read, draft and send with a document telling it what to do is an expectation, whereas a session that can only reach the mailbox through a tool that validates transitions is bounded by something it does not contain; the append only log delivers real provenance of the pipeline and does not deliver explanation of a decision, and it has a property nobody has named, which is that it is a store of attacker authored text that something will later read, making it both the forensic record and a re-injection surface that needs a handling rule; the representation of the mailbox in the second vault is worth more as a test harness than as a visualisation, because the whole pipeline can be exercised against it with no mailbox credential in existence; and the arithmetic says this costs on the order of two pence a message, which removes cost as a reason not to build it.** New contributions: **the three classes re-cut on the axis that actually determines exposure; the trifecta reassembling across the boundary as the failure mode the split does not address; constrained decoding identified as the enforcement mechanism and the closed against open field distinction that follows; the state machine relocated to the tool so that it becomes a boundary; the connector moved off the orchestrator with the trade stated; the two behaviour policy altitudes given their scopes; the log named as untrusted content with a handling rule; the representation reframed as the test harness; a costed model; and a build order whose first step proves the boundary before anything touches real mail.**

## The Three Environments, Re-Cut On The Axis That Matters

**The memo's three classes are real and the boundary between them is not the product. It is two independent properties.**

| Class | Holds tools | Output re-enters its own context | What an injection achieves |
|---|---|---|---|
| Session with connectors | Yes | Yes | Acts immediately, and can keep acting |
| Interface agent with tools | Yes | Yes | The same, with the tool set the builder chose |
| Single stateless call | **No** | **No** | Writes something into its own answer, and stops |

**The memo's second class is not a separate danger from the first, it is the same danger under the builder's control**, which is worth saying because a reader might conclude the interface is more dangerous than the session. It is not. It is more configurable, and the estate's whole argument is that configuration is where the barrier lives.

**The third class is genuinely different in kind and the reason is worth stating precisely.** A stateless call with no tools cannot act because there is nothing to act with, not because the model resisted anything. The model may be fully persuaded by the injection and produce exactly the output the attacker wanted. **It has nowhere to put it.** That is the 12 September ruling in architectural form: a refusal is a property of the model and a deployment with no tools is a property of the deployment, and only the second is a barrier.

## The Split Alone Does Not Break The Trifecta

**This is the correction, and it is the one thing that decides whether the architecture holds.**

**The three conditions are private data, exposure to untrusted content, and the ability to communicate externally.** In the memo's design, the stateless call has the second and neither of the others. The orchestrating session has the first and the third. **Neither agent has all three, and the system does.**

**The path is the boundary.** The stateless call reads hostile text and writes a result. The orchestrator reads that result and acts on the mailbox. So an attacker who cannot reach the tools directly can still write text that influences the output that the tool holder reads. **The trifecta has not been broken, it has been stretched across a join**, and a join is only a barrier if something constrains what crosses it.

**This is precisely the failure the dual component pattern was designed to prevent, and the way it prevents it is the part usually left out.** The privileged component is not supposed to receive the quarantined component's prose. It is supposed to receive references and symbols that stand for content it never sees. The formal version of the same idea tags every value and checks the tag at the tool call. **In both cases the protection is in what is allowed to cross, not in the fact that there are two components.**

**So the question for this architecture is not how many environments there are. It is what the schema at the boundary permits.**

## Constrained Decoding Makes The Boundary Enforceable, For Some Fields

**The platform now supplies the mechanism, and this was checked today.** A response can be constrained to a JSON schema during generation rather than parsed and validated afterwards. The documentation describes the result as guaranteed to be schema compliant, always valid, type safe, with required fields present and no retries needed for schema violations. It works with no tools attached and each request stands alone, which is exactly the third class above.

**That changes what the boundary is made of, and it does so unevenly.**

| Field kind | Constrained by the decoder? | Attacker influence | May the orchestrator read it |
|---|---|---|---|
| Enumerated value, such as a classification from a fixed list | **Yes.** The output cannot be a value outside the list | Choice among the listed values only | **Yes** |
| Boolean | **Yes** | Which of two | **Yes** |
| Number with a stated range | **Yes** | The value within the range | **Yes** |
| Identifier matching a pattern, such as a message reference | **Yes**, if the pattern is tight | Which known object | **Yes** |
| Free string, such as a summary or a proposed reply | **Shape only.** Any text at all is schema valid | **Total** | **No** |

**So the rule for the schema is short and it is the design.** The orchestrator reads only closed fields. Every open string goes to the vault and to a human, and never into the context of the thing holding the mailbox. **A drafted reply is not a value the orchestrator reads, it is an object the orchestrator moves by reference.**

**One consequence worth stating plainly.** The moment somebody adds a `reason` string to the schema so the orchestrator can log why a decision was made, the boundary is gone and nothing will announce it. That field will be proposed within a week of the pipeline working, and the answer is that the reason is written to the vault under the same identifier and is read by people, not by the orchestrator.

## The State Machine Is A Control Only If Something Else Enforces It

**The memo's control flow instinct is right and the estate's own enforcer test decides where it lives.**

**A state machine the orchestrator is told to follow is an expectation.** The orchestrator holds the tools. Nothing prevents it taking a transition the machine does not contain, and if it has been influenced it will not report that it did.

**A state machine the command line tool enforces is a boundary.** The tool validates every requested transition against the machine held in the vault, refuses anything not permitted from the current state, and writes both the request and the refusal to the log. The orchestrator asks; the tool decides.

**That makes the tool the enforcement point and gives it three jobs rather than one:** it validates transitions, it holds the credentials, and it writes the record. **The orchestrator's job shrinks to choosing which permitted transition to request next, which is the action selector pattern and is the most constrained thing in the catalogue.**

**A practical note on the machine itself.** One machine per action type, as the memo proposes, is right, and each should name its permitted transitions, its terminal states, the schema for each boundary crossing, and the behaviour policy identifier that governs it. Held in the vault, versioned, and referenced by hash in every log entry, so a run can be replayed against the exact machine that governed it.

## The Orchestrator Should Not Hold The Mailbox

**The memo identifies the crux and then accepts it: the session must hold the union of every right the workflow needs, because there is no way to give it less. That is true while the connector is attached to the session. It stops being true if the connector is not there.**

**Move the mailbox credential to the tool.** The tool holds a read authorisation and, separately, a send authorisation. The orchestrator holds neither and reaches the mailbox only by asking the tool for a transition the machine permits. **Then the union problem dissolves, because the session's grant no longer contains the mailbox at all.**

**This is the same move as yesterday's, applied one layer up.** Drafts left the mailbox because no scope could separate drafting from sending. The connector leaves the session because no setting can separate reading from acting. In both cases the platform offered no barrier and the answer was to remove the capability rather than to constrain it.

**The trade is real and the memo's preference is understandable.** Keeping the connector on the session is less work, keeps the data inside one vendor, and makes the first version possible in a day. Moving it to the tool means writing the mailbox access, handling authorisation refresh, and losing the convenience of asking in plain language. **The honest framing is that version one may keep the connector and must then describe itself as an expectation, and version two moves it and can describe itself as a boundary.** What must not happen is version one describing itself as version two.

## Two Altitudes Of Behaviour Policy, And What Each Bounds

**The memo proposes a policy per action and a policy over the whole workflow, and notes this is a good example of altitudes. It is, and the two bound different things.**

| Altitude | Subject | What it states | Enforced by |
|---|---|---|---|
| Action | One stateless call | Model, no tools, maximum tokens, the exact output schema, timeout, what is logged, what may cross the boundary | The tool, which constructs the call |
| Workflow | The whole run | Which transitions exist, which credentials the tool holds, which reaches are permitted, what requires a human, the daily volume ceiling | The tool, which validates against the machine |

**The delta between them is derivable and nobody authors it**, which keeps the 11 September ruling intact: the action policy's grant is the call's configuration, the workflow policy's grant is the tool's credentials, and the mandate at each altitude is what the machine permits.

**One thing the workflow altitude should carry that the memo does not mention: a ceiling.** A run that proposes to act on four hundred messages when the usual number is nine is the signature of something having gone wrong, whether by injection or by a bad day. A stated volume ceiling per run, enforced by the tool, is the cheapest protection in the design and it is the bulk operation rule from Friday in a different setting.

## The Log Is Untrusted Content

**Writing every request and response to an append only vault is the right decision and it creates an object nobody has named.**

**The log contains attacker authored text, on purpose.** That is what makes it useful for forensics. It also means that anything which later reads the log is reading hostile input, and the natural readers of a log are a summarising agent, a daily report generator, and an application that renders it.

**Three handling rules follow and they are cheap.**

**The log is read as data and never replayed into a context that holds tools.** A daily report over the log is produced by a stateless call with the same discipline as the pipeline itself, and its output is closed fields plus references.

**The application renders log content as inert text.** It runs in a sandboxed frame with an opaque origin, which handles a large part of this, and it should still treat every stored string as text rather than markup, and it must not fetch remote resources named in stored content. **Automatic fetching of a remote image named in attacker text is the exact mechanism of the exploit cited in yesterday's brief.**

**And the log has a retention position**, because it holds other people's correspondence. Yesterday's brief raised this for the message store and it applies with more force to a store that also captures everything a model said about it.

## What Provenance Actually Buys

**The memo claims complete provenance and complete explainability. The first is earned and the second is not, and the distinction is worth keeping because the estate sells the difference.**

**What the log gives is a complete record of the pipeline**: every input, every output, every transition requested, every transition refused, against a versioned machine, in an append only store where a correction supersedes rather than overwrites. That is genuinely strong and very few systems have it.

**What it does not give is an explanation of a decision.** Recording that a model was shown this and answered that does not say why, and a reconstruction offered later is a new model output rather than a retrieved reason. **The honest claim is that every action is attributable and reproducible, not that it is explained.** Attributable and reproducible is the stronger claim commercially anyway, because it is the one an auditor can check.

**One addition makes the record substantially more useful for almost nothing.** Record the machine's hash, the schema's hash, the behaviour policy identifiers at both altitudes, and the model identifier with every entry. **Then a run can be replayed exactly, and a change in behaviour can be attributed to a change in the machine, the schema, the behaviour policy or the model, which is four hypotheses eliminated by four fields.**

## The Representation Is The Test Harness

**The memo describes a representation of the mailbox in the data vault with an application over it, framed as visualisation. It is worth more than that.**

**With a representation, the entire pipeline can be exercised with no mailbox credential in existence.** Load it with real messages and with deliberately hostile ones, run every state machine end to end, and inspect what the orchestrator was asked to do. **Nothing can escape, because nothing is connected.**

**That makes it the place the evaluation set lives.** Every injection attempt the published address receives becomes a case in the harness, and the pipeline is re-run against the whole set whenever a schema, a machine or a model changes. This is the only mechanism in the design that will tell the estate whether a change made things worse, and it costs nothing to build because the representation is already proposed.

**It is also the demonstration.** A visitor can run the pipeline against the representation, see the log fill, and read the record, without connecting anything of their own. That is the missing free rung from this morning's brief, in the hardest case the estate has.

**On the word for it: use the data vault or the sample mailbox.** The word twin is already doing two jobs in this week's memos and this is the third.

## What It Costs

**Arithmetic, with the assumptions stated, at the current published prices for the mid tier model of two dollars per million input tokens and ten per million output.**

| Call | Input | Output | Cost |
|---|---|---|---|
| Classify and extract | 2,500 | 500 | $0.0100 |
| Injection check | 2,000 | 150 | $0.0055 |
| Propose actions | 1,800 | 400 | $0.0076 |
| **Per message** |  |  | **$0.023** |

**So one hundred messages costs about two dollars and thirty cents, and a thousand about twenty three dollars.** The asynchronous interface halves both, and the smaller model halves them again, so a thousand messages processed in batches on the cheaper model lands near six dollars. **Cost is not a reason to avoid this design, and the token overhead reported for the comparable published system, of roughly three times, is already inside these numbers because the three calls are the overhead.**

**The figure worth watching is not the total but the per message ceiling**, because a message with a large attachment or a long thread will cost many times the median and an attacker controls the length of what they send. **A maximum input size per message, enforced by the tool, belongs next to the volume ceiling.**

## Build Order

**Five steps, and the first proves the thing the architecture depends on.**

**One. The boundary, alone.** A schema with only closed fields, a stateless call constrained to it, and a fixture of twenty hostile messages. Confirm that no enumerated field ever takes a value outside its list. This is an afternoon and it either validates the design or ends it.

**Two. The tool, with no mailbox.** Python command line, the machine held in the vault, transitions validated, everything logged with the four hashes. Runs entirely against the sample mailbox.

**Three. The application over the log.** Status, the run history, refusals, the daily report. Inert rendering, no remote fetching.

**Four. Read only against the real mailbox.** The tool holds a read authorisation. Nothing is written anywhere except the vault. Run it for a week and compare what it proposed against what the project lead would have done.

**Five. The send path, narrow.** A send authorisation held by the tool, one action type permitted, a volume ceiling, and the personal lane delivering drafts to a human who sends them himself.

**The one hour test from yesterday's brief is a prerequisite for step four and has still not been run:** whether two separate mailbox authorisations, one read and one send, can be held cleanly in the environment the estate actually uses.

## What This Does Not Try To Be

**It is not an implementation.** Schemas, state machines and the tool's interface are described. None is specified to the point of being buildable without further design.

**It is not a measurement.** The cost model is arithmetic over assumed token counts and the token counts are guesses.

**It is not a test of the platform's permission model.** The claim that the orchestrator cannot be given less than the union while the connector is attached is reasoning from the published model, not from an experiment.

**It is not a security review of the vault application.** The rendering rules are stated as requirements, not verified against the current implementation.

**And it does not claim the architecture resists a determined adversary.** It claims the architecture bounds what a successful injection can reach, which is smaller and checkable.

## Honest Tensions

**The closed field rule is correct and it will be eroded by ordinary good intentions.** Every person who works on this will at some point want the orchestrator to see a summary, a reason or a subject line, and each request will be reasonable. There is no technical alarm for this, only a schema review, and schema reviews get skipped.

**Moving the connector to the tool is the right architecture and the wrong first version.** Keeping it on the session gets something working this week and produces an expectation; moving it costs real work and produces a boundary. Both are defensible and only one of them can be described as a control.

**The log makes the system auditable and also makes it a target.** A complete record of a mailbox's traffic plus every model interaction over it is a more attractive object than the mailbox alone, and it sits in a vault whose read key is a string.

**Constrained decoding guarantees the shape and not the truth.** A classification field is bounded to its list and can still be the wrong member of that list, chosen because an attacker asked for it. The schema stops an injection from expanding the space of outcomes; it does not stop it from picking one.

**And the whole design depends on the stateless calls being genuinely stateless.** The moment somebody adds caching, a conversation identifier, or a second message to the same call to save money, the third class has quietly become the second, and the saving that motivated it will be a few cents.

## Open Questions

**Does the enumerated field hold under adversarial pressure in practice?** Constrained decoding guarantees the value is in the list. Whether the chosen member is reliably correct under a message engineered to mislead is an empirical question and is step one.

**Where does the tool run when the orchestrator is a hosted session?** A command line tool held in a vault is executed by something. Whether that is the project lead's machine, a scheduled cloud job, or a session with code execution changes the credential story completely and is unresolved.

**How does the tool hold the mailbox authorisation, and where does the refresh token live?** The vault has a mechanism for holding a key, which the memo notes. Whether that is appropriate for a live authorisation with refresh has not been examined.

**What is the retention period for the log, and who can action a deletion request against it?** Unanswered, and an obligation.

**Should the daily report be produced by a stateless call or written by the tool from the closed fields?** The second needs no model at all and cannot be injected. The first reads better. The second is probably right and the first will be built.

**And does the sample mailbox get published?** As a demonstration it is the best asset in this design. As a published artefact it tells an attacker exactly which classifications the pipeline uses.

## Relationship To Previous Briefs

| Date | Document | Relationship |
|---|---|---|
| 12 Sep | The correction that a guardrail is a property of one deployment rather than of the model | The stateless class is that ruling as an architecture: safety from having no tools, not from refusing |
| 11 Sep | The ruling that the delta is derived and never authored | Preserved at both policy altitudes, where the grant is the call's configuration and the tool's credentials |
| 19 Sep | The brief on the inbox persona | Supplies the bulk operation ceiling, which reappears here as the volume ceiling per run |
| 20 Sep | The brief on the behaviour policy as a fractal | Supplies the two altitudes and the rule that the barrier kind is a property of the layer |
| 20 Sep | The brief on the mailbox pipeline, immediately prior | Established the draft and send scope identity; this brief applies the same move one layer up to the connector |

## Key Claims

| # | Claim |
|---|---|
| 1 | A stateless call with no tools is safe because it has nothing to act with, not because the model resisted, which makes it a property of the deployment |
| 2 | Splitting the work across two environments does not break the trifecta, because the three conditions reassemble across the boundary between them |
| 3 | The protection is in what is allowed to cross the boundary, not in the existence of the boundary |
| 4 | The platform can constrain a response to a schema during decoding, with no tools attached, which makes the boundary enforceable rather than merely validated |
| 5 | Constrained decoding bounds enumerated, boolean, numeric and pattern matched fields, and does nothing for free strings, which remain fully attacker influenced |
| 6 | The orchestrator must read only closed fields, and every open string goes to the vault and to a person |
| 7 | A state machine the orchestrator is told to follow is an expectation; one the tool enforces is a boundary |
| 8 | While the connector is attached to the session, the session holds the union of every right, so the connector should move to the tool |
| 9 | The log is a store of attacker authored text and is therefore both the forensic record and a re-injection surface needing a handling rule |
| 10 | The record delivers attribution and reproducibility rather than explanation, and four hashes per entry make a run replayable |
| 11 | The sample mailbox is the test harness and the demonstration, and the whole pipeline can be exercised against it with no credential in existence |
| 12 | The pipeline costs about two pence a message at current prices, halving on the asynchronous interface, so cost is not a reason not to build it |

## Sources

- The platform's structured outputs documentation, read 20 September 2026 for constrained decoding, the schema conformance guarantees, and the confirmation that it works with no tools attached and each request standing alone. https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- The platform's published pricing, read 20 September 2026 for the per million token input and output rates used in the cost model, the caching multipliers and the asynchronous discount. https://platform.claude.com/docs/en/about-claude/pricing
- Simon Willison, for the three conditions used throughout, and for the dual component pattern in which the privileged side receives references rather than content. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Debenedetti and others, "Defeating Prompt Injections by Design", for control and data flow separation, tagging values and checking at the tool call, and the reported token overhead. https://arxiv.org/abs/2503.18813
- Beurer-Kellner and others, "Design Patterns for Securing LLM Agents against Prompt Injections", for the action selector and plan then execute patterns the orchestrator is reduced to. https://arxiv.org/abs/2506.08837
- Reddy and Gujral, "EchoLeak", for the automatic remote fetch step that the rendering rule is written against. https://arxiv.org/abs/2509.10540
- The project lead's voice memo of 20 September 2026, for the three environment classes, the state machine proposal, the two policy altitudes, the vault in vault arrangement, the command line tool and the provenance claim

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/docs/briefs/v0.33.71__arch-brief__the-split-does-not-break-the-trifecta-the-schema-does/index.html)*
