# Cross-artifact analysis

Status: local candidate analysis; owner acceptance pending

| Requirement | Task | Evidence |
| --- | --- | --- |
| FR-001 bound/default-deny challenge | T003 | Missing backend, context isolation, nonce uniqueness and unsupported assurance |
| FR-002 signed/current receipt | T003 | Real crypto, field tampering, issuer activation and signed lifetime-policy refusals |
| FR-003 durable one-use | T003 | Concurrent verification/use, restart, stable retry, changed digest conflict, cancellation, expiry and revocation |
| FR-004 evidence boundary | T002/T003 | Fixed possession method, unknown/stronger claim refusal, no domain effect in the core |

Every executable task is in this feature. There is no task duplication in the OpenSpec packet. New origin IDs are present before ratification; no ratification is invented. Source, schema, CI and live acceptance gates are recorded separately. The legacy wallet skip and empty live scan are explicit. No source gate reads a sibling checkout. No owner-act, release, upstream acceptance or archive task is marked complete by this analysis.
