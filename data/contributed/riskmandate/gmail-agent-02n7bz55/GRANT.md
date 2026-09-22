# GRANT.md — Reach

**Agent:** Claude, via the Claude.ai Gmail connector
**Deployment:** Google Workspace account `athena@thecyberboardroom.com`, sending as `agent@riskmandate.ai`
**Measured:** 2026-09-19, from the connector's own tool schemas and the live permission UI
**Vault:** 02n7bz55 · recorded at v0.3.0

Reach is what the agent can actually do in this deployment. It is measured, not asserted: every line below comes from a tool schema this agent read or a permission state observed in the settings page, not from the connector's description of itself.

**Not in the `verb.object.reach` grammar.** abp.sgit.ai pins 23 capability primitives and this file does not use them — it is in the connector's own vocabulary. That is a known gap, listed at the end.

---

## 1. Mail surface

The connector exposes **30 tools** against one mailbox: 6 read-only, 24 that write or delete.

### Unprompted — runs with no approval, 10 of 30

| Tool | Reach |
|---|---|
| `search_threads` | Any message in the account. Full Gmail operator set including `in:anywhere`, so archived, sent and trashed mail are all in scope. |
| `get_message`, `get_thread`, `get_draft`, `list_drafts`, `list_labels` | Full content of anything `search_threads` can find. |
| `create_label` | New labels, including nested. |
| `label_message`, `unlabel_message` | Any label on any message, including system labels — so `INBOX` removal and `UNREAD` clearing are both here. |
| `send_message` | **Outbound email to any address, with attachments to 25MB.** The only irreversible action in the set, and it is in this table. |

### Gated — stops at an approval prompt, 20 of 30

`create_draft`, `update_draft`, `delete_draft`, `reply`, `forward`, `update_label`, `delete_label`, `label_thread`, `unlabel_thread`, `update_message_labels`, `trash_message`, `untrash_message`, `trash_thread`, `untrash_thread`, `mark_message_spam`, `unmark_message_spam`, `mark_thread_spam`, `unmark_thread_spam`, `apply_sensitive_message_label`, `apply_sensitive_thread_label`

### Blocked — 0 of 30

Nothing is set to Blocked on this deployment.

---

## 2. Sending identity

The compose tools carry **no sender field**. `send_message`, `reply`, `create_draft` and `update_draft` were all inspected: no `from`, no `sendAs`, no `alias`. The From header is therefore whatever Gmail's default send-as entry is, and the agent cannot select or override it per message.

Current default: `agent@riskmandate.ai`, DKIM-signed as `riskmandate.ai`, confirmed aligned by a live round trip on 2026-09-19.

Consequence for reach: **the agent sends as the business, and cannot send as anything else.** It also cannot send as `athena@thecyberboardroom.com` while this default stands.

---

## 3. Beyond the mailbox

| Surface | Reach |
|---|---|
| Web | Fetch and read any public page. Used this session to read riskmandate.ai and sgit.ai. |
| Shell + filesystem | A Linux container with network egress to an allowlist including `*.sgit.ai`, `*.sgraph.ai`, `github.com`, package registries and `api.anthropic.com`. |
| sgit vaults | With a key: clone, read, write, commit and push. This vault was modified from that container. |
| Vault write scope | Any vault whose key reaches this session. Two were held today. |

This row matters and is easy to miss: **the agent's reach is not the Gmail connector.** The connector is one surface. A shell with egress and a vault key is a larger one, and a behaviour policy scoped to the mailbox alone would have understated the reach by a wide margin.

---

## 4. What is absent

Not barriers anyone chose — capabilities the connector does not expose. Recorded because they cap the blast radius, and because a future version could remove them silently.

- **No account settings.** No filters, forwarding, vacation responder, signatures, delegation, IMAP/POP. No persistence mechanism outlives a session.
- **No permanent deletion.** No hard delete, no empty-trash. A 30-day floor under every destructive mail action.
- **No second account.** One Google identity at a time.
- **No introspection.** The agent cannot read back its own permission state. A restriction is discovered by hitting it, and the failure is indistinguishable from a timeout.

---

## 5. Named gaps in this record

- Not expressed in abp.sgit.ai's 23 `verb.object.reach` primitives. Until it is, this reach cannot be joined to the agent rung of the fractal ladder.
- The container's egress allowlist is recorded from its declared configuration, not probed.
- Vault reach is stated as a capability, not enumerated — no list exists of which vaults a key could reach.
- Measured in one session on one day. Connector tool sets change without notice; this is a snapshot with a date on it, not a standing fact.
