# U0: The source bytes

> The source bytes, one of the universes an ABP row crosses: owned by nobody: the bytes are what they are, with its own node types and verbs, sharing only the grammar. Status: partial.

*Source: <https://abp.sgit.ai/model/universes/u0/index.html> · site v0.4.4 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../../../index.md) / [The model](../../../model/index.md) / [The universes](../../../model/universes/index.md) / The source bytes

# U0: The source bytes

**Owner** nobody: the bytes are what they are. **Centre of gravity** the hash. **Smallest node** a byte range in a file that was fetched on a date. **Level** down. **Status** partial.

> Every promoted file carries its source, its retrieval time and its content hash, and the build refuses to run if the bytes disagree with their manifest. Per file today; per node is the change.

## Node types

A node type is a required pattern of paths, not a label. The ones marked yes are walked on every build and the count is what matched; the rest are the vocabulary this universe needs and does not have.

| Type | Formula | Exists today | Note |
|---|---|---|---|
| **SourceFile** | `a node with a -fetched_from-> [URL] and a -hashes_to-> [Digest]` | not yet |  |
| **ByteRange** | `a node -inside-> a [SourceFile] with a stated offset and length` | not yet |  |

## Verbs

Each is a verb with a distinct inverse, a stated domain and range, and the sentence it reads as. The ones marked live are in the edge vocabulary today; the rest are proposed here, or declared by the universe's owner elsewhere, and say so.

| Edge | Reads as | Inverse | Reads as | Domain | Range | From | Status |
|---|---|---|---|---|---|---|---|
| `fetched_from` | this file was fetched from this address on this date | `serves` | this address served this file | `SourceFile` | `URL` | proposed here | proposed |
| `hashes_to` | this file hashes to this digest | `digest_of` | this digest is the digest of this file | `SourceFile` | `Digest` | proposed here | proposed |
| `hashed_from` | this node was read from these bytes | `grounds` | these bytes ground this node | `Node` | `ByteRange` | proposed here; the AIUC-1 vault calls its version anchors | proposed |

## What the map adds here

Today the provenance block sits on every data file and says the same thing for every row in it. The Regulation Graph ends every chain in a hash of the retrieved bytes, per node. The per row version is what riskmandate.ai asked for in its Lab 03, request three, and it belongs here: a row's evidence is a node in U3 that is hashed_from a byte range in U0.

[All thirteen](../../../model/universes/index.md) · [U1: The grammar](../../../model/universes/u1/index.md) · [This universe as JSON](../../../data/universes/u0.json) · [The brief](../../../docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.md)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://abp.sgit.ai/model/universes/u0/index.html)*
