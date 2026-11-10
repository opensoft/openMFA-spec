# openMFA Challenge and Receipt Service — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Propose one-time challenges and signed verification receipts with explicit replay, revocation, and error semantics.
Topics: wallet-mfa, openmfa, authentication-contracts, replay-protection
Repository context: opensoft/openMFA-spec with cross-product integration references
Captured: 2026-11-10

## Possible feats

- Define verifier schemas and adversarial vectors.
- Qualify atomic challenge consumption and binding recovery.

## Candidate operations

Operation names describe intent rather than released endpoint paths.

| Operation | Input | Result |
| --- | --- | --- |
| Create challenge | Authenticated relying party, tenant, audience, subject/session reference, requested assurance, expiry, optional operation digest | Bound nonce, ID, allowed methods, expiry |
| Verify response | Challenge, credential binding, authenticator proof | Signed receipt or fixed refusal |
| Read outcome | Authorized caller and challenge reference | Pending, verified, denied, cancelled, consumed, or expired state |
| Consume receipt | Bound caller, immutable request digest, idempotency key | One consumption or duplicate/conflict |
| Revoke binding | Authorized custodian, reference, reason | Current revocation and dependent-use invalidation |

Administrative enrollment and recovery are separate. Refuse arbitrary account enumeration and unauthorized pushes.

## Evidence semantics

Receipts bind verifier issuer, subject/actor context, audience, challenge digest, verification time, expiry, methods/custody facts, policy version, and signer. Receipt authentication grants no domain action.

The [shared envelope](https://github.com/opensoft/openxFactory/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-shared-contracts.md) is the cross-product field proposal. Define each field once under a named owner and coordinated compatibility process before publishing schemas.

## State, retries, and failure

Atomic state transitions prevent repeated consumption. An identical idempotent retry returns the prior outcome. A changed request digest conflicts. Wrong subject/audience, replay, expiry, invalid signature, revoked binding, or policy mismatch refuses explicitly.

Signer rotation uses declared verification keys and validity windows. Recovery invalidates dependent credentials/receipts under policy. Operations requiring current revocation fail closed when the check is unavailable.

## Secret handling and open decisions

Exclude responses, codes, seeds, tokens, passwords, private keys, and sensitive payloads from logs and model transcripts. Audit safe references, digests, methods, custody, times, policy, and result codes.

Choose serialization, canonicalization, algorithms, discovery, replay/introspection storage, audit failure behavior, retention, and transport. HTTP/OIDC is the application candidate. A narrow MCP facade can reuse the same authorization boundary.

## Relationships

[Custody boundary](wallet-mfa-verifier-boundary.md) supplies evidence semantics. [Synthesis](wallet-mfa-synthesis-verification-service.md) joins the API to the broker.
