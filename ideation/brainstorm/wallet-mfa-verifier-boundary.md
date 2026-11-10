# openMFA Verification and Custody Boundary — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Propose an independent verifier that reports bound evidence with explicit custody and factor independence.
Topics: wallet-mfa, openmfa, authenticators, custody, assurance
Repository context: opensoft/openMFA-spec with cross-product integration references
Captured: 2026-11-10

## Possible feats

- Implement a verification service behind an OIDC broker adapter.
- Add a separately scoped external-provider TOTP code adapter.

## Product scope

openMFA verifies human authenticators, approved upstream authentication, and configured workload evidence. It challenges the subject/session, validates enrolled credential bindings, enforces freshness/replay rules, and returns a signed verification receipt. The broker maps evidence into application tokens. The domain decides action permission and approval.

Enrollment and recovery require authorized actors, subject binding, credential proof, and audit. They have separately scoped administrative interfaces.

## Custody and factor independence

A human authenticator, signing device, or distinct custodian can supply per-use evidence outside an agent context. Freely invocable software credentials share that context's compromise boundary. Receipts report the observed facts and preserve wallet custody ceilings.

A native TOTP verifier checks and consumes a response under replay policy. An external-provider adapter generates an enrolled account's code and lets the external provider verify it. The native-verification and code-generation interfaces have different semantics.

## Integration and private configuration

Keycloak is the first proposed broker adapter. Custody backend, initial authenticators, and deployment trust roots remain implementation choices. Public code and contracts use synthetic examples. Enrollment secrets, production identifiers, issuer allowlists, clinical payloads, and key/seed material remain in deployment custody.

## Human approval

openMFA verifies the human's authentication. The domain separately checks eligible standing and distinctness, captures exact-operation consent, and consumes the approval.

## Relationships and decisions

[Service records](wallet-mfa-service-records.md) defines the candidate seam. [Synthesis](wallet-mfa-synthesis-verification-service.md) places it in the ecosystem. [Shared boundaries](https://github.com/opensoft/openxFactory/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-boundaries.md) assigns owners. Entra eligibility must be verified before any external QA adapter is activated.
