# DELTA.md — Gap

**Status: not derivable. This file exists to say so.**

**Vault:** 02n7bz55 · recorded at v0.3.0 · 2026-09-19

---

## Why this file is empty of numbers

The gap is reach minus mandate. `GRANT.md` holds a measured reach. `MANDATE.md` holds a mandate **inferred by this agent from one session of its own behaviour**, which is not a mandate.

Subtracting an inferred mandate from a measured reach produces a number, and the number would be wrong in a specific and predictable direction: too small. The agent reconstructed the mandate from things it was asked to do and was not stopped from doing, so every capability it exercised without objection appears on the mandate side of the subtraction. An agent computing its own gap this way will always report a narrow one, because the act of using a capability is what put it in the mandate column.

The guidance on sgit.ai says to state the gap rather than paper over it, and that a record naming what it is missing is more useful than one quietly omitting it. So this file is the gap in the gap.

---

## What is known without computing it

Three things are true regardless of where the mandate lands, because they concern capabilities nobody has claimed:

1. **Outbound email to arbitrary external recipients, unprompted.** Whatever the mandate turns out to be, it was never stated, and `send_message` sits on Always allow. Every message sent this session went to an address the operator named in the same turn — but nothing in the deployment required that.

2. **Full mailbox read, unprompted.** `search_threads` with `in:anywhere` reaches every message in the account. The mandate covers reading the inbox and isolating one stream. The reach is the entire account including trash.

3. **Vault write on any key that reaches the session.** Not in the mandate at all as a general capability — two specific vaults were named. The reach is unbounded by anything except which keys arrive.

Each is a gap item that does not depend on resolving the mandate, because in each case the mandate says nothing and the reach says everything.

---

## What would make this derivable

The ten questions in `MANDATE.md`, answered by the business rather than by the agent. The load-bearing one is whether the mandate covers unattended operation, because the answer changes the barrier set more than it changes the mandate: today the control doing the real work is a person reading each message as it is sent, and that control does not survive automation.

Until then this file should stay as it is. A gap computed by the party whose reach is being measured is not evidence, and publishing one would be worse than publishing nothing — it would look like the work had been done.
