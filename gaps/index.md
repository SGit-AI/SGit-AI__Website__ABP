# The gaps register

> Gaps a behaviour policy finds in providers' products, the rule each defeats, who accepts the risk and the request to close it; and gaps found in our own behaviour policies, with what was done about them.

*Source: <https://abp.sgit.ai/gaps/index.html> · site v0.12.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / The gaps register

# Gaps and requests: what a behaviour policy wants and a product cannot enforce

**9 gaps in providers' products and 3 in our own behaviour policies**, each with the rule it defeats, the barrier that is possible, the risk that leaves and who accepts it, and the request to whoever could close it. When a product cannot enforce a rule, somebody accepts the risk, usually silently and in the act of granting the connector. This register makes that a row.

> **2 of the 9 provider gaps are ones where the rule cannot even be written.** No barrier of any kind is possible: not a setting, not a rule in prose. For those the ABP has no row to refuse, and the finding is that the rule cannot be expressed, which is worth more than a behaviour policy that pretends it can.

## The register by provider

| Provider | Open | Reported | Fixed | Cannot be expressed |
|---|---|---|---|---|
| Anthropic | 2 | 0 | 0 | 1 |
| Google | 3 | 0 | 0 | 1 |
| Google and Anthropic | 3 | 0 | 0 | 0 |
| RiskMandate.ai | 3 | 0 | 0 | 1 |
| sgit.ai | 0 | 1 | 0 | 0 |

**A count is a count.** It says nothing about whether any product is acceptable for any deployment, because acceptability is not in this register. One of the providers is us.

## How the contributor's words map onto the four barriers

| The brief says | This site says | What it means |
|---|---|---|
| none | **none** | nothing can stand in the way; the rule cannot be expressed |
| policy only | **expectation** | a rule in prose, kept by a cooperative agent and by nothing else |
| admin setting | **setting** | a switch the account can flip, which is not a control because the account can flip it back |
| identity boundary | **boundary** | enforced by something the grant does not include: a key the recipient holds, a lock an administrator owns |

Both words are kept on every entry. Nothing is merged, which is the [three layers](../model/graph/layers/index.md) rule applied to a register.

## Gaps in providers' products (9)

### gap-001: Google, Google Calendar, the API and every connector built on it

|  |  |
|---|---|
| **The gap** | Creating an event with guests sends the invitations at that moment: there is no draft, no preview and no edit before send, and the API's sendUpdates parameter only chooses who is notified. |
| **What it does to an ABP** | The rule draft only, a person sends cannot be expressed for calendar invitations at all. send.message.world through an invitation has no row a mandate can refuse while still granting the calendar. |
| **Barrier possible** | **none** (the contributor's word: none) |
| **The risk, and who accepts it** | That the agent can invite anyone, immediately, with no step between composing and sending. Accepted by whoever grants a calendar to an agent, in the act of granting it. |
| **Request to the provider** | A draft or hold state for invitations, so that an event with guests can exist before anybody is notified. |
| **Evidence** | The Calendar API reference for events.insert and its sendUpdates parameter; the contributor's own agents, which hold Calendar. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [cases/beta-001/chatgpt-calendar](../cases/beta-001/chatgpt-calendar/index.md), [gmail/what-a-prompt-cannot-do](../gmail/what-a-prompt-cannot-do/index.md) |

### gap-002: Google, Gmail, through the connector

|  |  |
|---|---|
| **The gap** | Discarding a draft is irreversible and leaves no log the agent can read: a discarded draft cannot be recovered or audited through the connector. |
| **What it does to an ABP** | A mistaken discard is invisible to the deployer and to the agent's own end of turn report. Drafts are outside the grammar, so the loss cannot even be named as a row. |
| **Barrier possible** | **expectation** (the contributor's word: policy only) |
| **The risk, and who accepts it** | That drafted work disappears without trace. Accepted by the deployer who lets the agent manage drafts. |
| **Request to the provider** | A recoverable trash for drafts, and an audit event when one is discarded. |
| **Evidence** | The connector's delete_draft tool, which the measured Gmail profile on this site lists on Needs approval; no untrash_draft exists among the thirty. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [gmail/measured](../gmail/measured/index.md) |

### gap-003: Google and Anthropic, Gmail, through the Claude connector

|  |  |
|---|---|
| **The gap** | Image tags are stripped from drafts, so images can only go as attachments and inline images are impossible. |
| **What it does to an ABP** | None on the four objects. Recorded because it shapes what an agent can send, and a register that only lists what fails a policy would misstate what shapes one. |
| **Barrier possible** | **not applicable** (the contributor's word: not applicable) |
| **The risk, and who accepts it** | None. A capability absent rather than a rule unenforceable. |
| **Request to the provider** | Inline images in HTML drafts, or a documented statement that they are stripped. |
| **Evidence** | The contributor's drafts, as received. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |

### gap-004: Google and Anthropic, Gmail, through the Claude connector

|  |  |
|---|---|
| **The gap** | There is no raw MIME capture: an agent can read a message's content but cannot store the raw bytes, with full headers, DKIM signature and exact HTML. |
| **What it does to an ABP** | The provenance of stored mail is weaker than it should be. A record kept by the agent is a rendering, not the bytes, and cannot be re-verified against the sender's signature later. |
| **Barrier possible** | **not applicable** (the contributor's word: not applicable) |
| **The risk, and who accepts it** | That a dispute over what a message said cannot be settled from the agent's copy. Accepted by whoever relies on that copy. |
| **Request to the provider** | A raw export the agent can write straight to storage. |
| **Evidence** | The thirty connector tools as measured on this site; none returns raw MIME. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [gmail/measured](../gmail/measured/index.md) |

### gap-005: Google and Anthropic, Gmail, through the Claude connector

|  |  |
|---|---|
| **The gap** | Plain text drafts reach recipients with links rewritten through a google.com redirect, so the recipient sees a redirect URL rather than the address the agent wrote. |
| **What it does to an ABP** | None on the four objects. A fidelity and trust issue: a disclosed agent identity that sends links which look rewritten undercuts the disclosure. |
| **Barrier possible** | **not applicable** (the contributor's word: not applicable) |
| **The risk, and who accepts it** | None. Workaround in use: an HTML body with explicit anchors. |
| **Request to the provider** | Plain text links delivered as written, or the rewrite documented. |
| **Evidence** | The contributor's sent mail, as received. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |

### gap-006: Google, Gmail, personal accounts and most Workspace editions

|  |  |
|---|---|
| **The gap** | Personal Gmail has no native message encryption: only TLS in transit and Confidential Mode, which is not encryption. Hosted S/MIME and client side encryption exist on some Workspace editions only, and client side encryption leaves headers in clear. |
| **What it does to an ABP** | The rule only the recipient can read it cannot be enforced for most people. A hallucination, a bug or a wrong address leaks the whole message; nothing in the grant or the platform bounds send.message.world by who can open what was sent. |
| **Barrier possible** | **boundary, if built outside the platform** (the contributor's word: identity boundary) |
| **The risk, and who accepts it** | That anything the agent sends can be read by whoever receives it, intended or not. Accepted by the deployer, until a key held by the recipient becomes the boundary. |
| **Request to the provider** | None of the provider. The contributor's answer is a browser extension that encrypts to a recipient's published key, which is a boundary the platform does not have to supply. |
| **Evidence** | Google's own documentation of Confidential Mode, S/MIME and client side encryption and the editions each is available on; the contributor's edition. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |

### gap-007: Anthropic, Claude Cowork, and the account's connectors

|  |  |
|---|---|
| **The gap** | A session's tools cannot be narrowed per agent. If the account holds Gmail write tools, every session on the account gets send and draft. |
| **What it does to an ABP** | The rule this agent may not send is an expectation with no barrier: the grant is the account's and the mandate is the agent's, and nothing in between can hold a difference. |
| **Barrier possible** | **expectation** (the contributor's word: policy only) |
| **The risk, and who accepts it** | That every agent on the account can do whatever the widest one was given. Accepted by the account holder, in the act of enabling the connector. |
| **Request to the provider** | Per agent or per session tool permissions, or an account level way to publish a narrower grant to a named agent. |
| **Evidence** | The contributor's own sessions. This site's estate case for three surfaces of one product records the same property as its first open question. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [cases/estate-002](../cases/estate-002/index.md), [gmail/what-a-prompt-cannot-do](../gmail/what-a-prompt-cannot-do/index.md) |

### gap-008: Anthropic, Claude, the connectors directory

|  |  |
|---|---|
| **The gap** | Grants grow mid session. A newly added connector's tools appeared in a running session without anyone in the session asking for them. |
| **What it does to an ABP** | The reach changed while the mandate did not, and the grant the behaviour policy was written against is not the grant the session finished with. No object on this site has a row for a grant that moves during a session. |
| **Barrier possible** | **none** (the contributor's word: none) |
| **The risk, and who accepts it** | That a session acquires capabilities nobody in it granted. Accepted by the account holder, who may not be in the session. |
| **Request to the provider** | A session pins its tool set at start, or is told, in the transcript, when the set changes. |
| **Evidence** | The contributor's session, in which a Zapier connector's tools arrived mid session. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [gmail](../gmail/index.md), [model/universes/u11](../model/universes/u11/index.md) |

### gap-009: sgit.ai, The sgit command line, versions 0.16.0 and 0.17.0

|  |  |
|---|---|
| **The gap** | pull silently discards uncommitted edits to tracked files. |
| **What it does to an ABP** | An agent that writes to a vault and pulls before committing loses the write with no error. A record kept in a vault is only as durable as the agent's commit discipline. |
| **Barrier possible** | **not applicable** (the contributor's word: not applicable) |
| **The risk, and who accepts it** | Lost edits. Workaround: commit before pull. Accepted by nobody; this one is a defect in our own estate and is reported. |
| **Request to the provider** | pull refuses, stashes, or merges when tracked files have uncommitted edits; a regression test. |
| **Evidence** | Reproduced by the contributor in a throwaway vault; report and script on request. This site's own session on 22 September cloned a vault with 0.16.0 and did not exercise pull. *(tier: self-reported)* |
| **Status** | reported, first seen 2026-10-04 |

## Gaps in our own behaviour policies (3)

The honest half. Places where one of our own agents' reach exceeded its mandate, and what was done: the mandate widened, a barrier added, or the risk accepted and by whom.

### own-001: RiskMandate.ai, Every RiskMandate agent behaviour policy that grants Google Calendar

|  |  |
|---|---|
| **The gap** | The calendar invitation gap (gap-001) is a gap in each of them: every one assumes a person releases outbound, and for invitations nothing can. |
| **What it does to an ABP** | send.message.world through an invitation sits on the wanted side wherever Calendar is granted, with no draft step to point a clause at. |
| **Barrier possible** | **none** (the contributor's word: none) |
| **The risk, and who accepts it** | That an agent holding Calendar can invite anyone immediately. |
| **What we did** | Recorded it here. The risk is accepted by the operator for every policy that grants Calendar, until a hold state exists or Calendar is withdrawn from the agents. |
| **Request to the provider** | see gap-001 |
| **Evidence** | gap-001, and the contributor's own policies. *(tier: self-reported)* |
| **Status** | open, first seen 2026-10-04 |
| **On this site** | [cases/beta-001/chatgpt-calendar](../cases/beta-001/chatgpt-calendar/index.md) |

### own-002: RiskMandate.ai, The Gmail connector on the agent's mailbox, as measured on 19 September 2026

|  |  |
|---|---|
| **The gap** | send_message was on Always allow: the one irreversible action in the reach sat at nothing, while trashing a message needed approval. |
| **What it does to an ABP** | send.message.world at barrier none against a mandate that had never been elicited. The reach exceeded anything the business had said. |
| **Barrier possible** | **setting** (the contributor's word: admin setting) |
| **The risk, and who accepts it** | That the agent sends to anyone with no prompt, and that a message which talks it into replying has a way out. |
| **What we did** | The agent recommended moving send_message to Needs approval and leaving create_draft open. On the day the vault was written the change had not been made, so the risk was accepted by the operator, by reading each message as it was sent. |
| **Evidence** | GRANT.md and AGENTS.md in vault 02n7bz55, held verbatim on this site. *(tier: measured)* |
| **Status** | open, first seen 2026-09-19 |
| **On this site** | [gmail/measured](../gmail/measured/index.md) |

### own-003: RiskMandate.ai, The same mailbox, the same session

|  |  |
|---|---|
| **The gap** | Asked to move sixteen messages to a folder, the agent removed three from the inbox, since a move in Gmail is a label plus an INBOX removal. Nobody objected, and the agent's own reconstructed mandate then listed un-inboxing as authorised. |
| **What it does to an ABP** | A mandate line the business never granted, produced by an ambiguous instruction, a reasonable interpretation and no objection. The vault names it as the ratchet happening inside one session. |
| **Barrier possible** | **expectation** (the contributor's word: policy only) |
| **The risk, and who accepts it** | That the inferred mandate drifts toward the reach with every action nobody objects to. |
| **What we did** | Kept the mandate marked inferred, declined to compute a gap from it, and published the site's own starting mandate beside it on this site so the difference is a number. The business has not yet elicited the real one. |
| **Evidence** | MANDATE.md and DELTA.md in vault 02n7bz55; the two deltas on this site. *(tier: measured)* |
| **Status** | open, first seen 2026-09-19 |
| **On this site** | [gmail/measured](../gmail/measured/index.md) |

## How to add an entry

One JSON file under [`data/gaps/entries/`](../data/gaps/index.json), by pull request or sent to the editor, with the fields the index lists. Every entry says who reported it and the evidence tier it rests on; the index and this page are generated from the files present, so there is nothing else to edit.

> **Nothing on this page is an assessment, an audit, a certification or a security review of any named product**, and no adjective here attaches to one. Each entry is a rule somebody tried to write, the product's documented or observed behaviour against it, and a request. The evidence tier on every entry is the reporter's; this site did not test the provider gaps and says so.

[The register as JSON](../data/gaps/index.json) &#183; [The four barriers](../model/barriers/index.md) &#183; [The measured Gmail deployment](../gmail/measured/index.md) &#183; [The cases](../cases/index.md)

---

*[Site index for agents](../llms.txt) · [HTML version](https://abp.sgit.ai/gaps/index.html)*
