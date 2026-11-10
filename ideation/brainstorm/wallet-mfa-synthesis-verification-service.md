# Synthesis: A Reusable Verification Service — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Combine protected authenticator custody and bound receipts across independent wallet-enabled applications.
Topics: wallet-mfa, openmfa, identity-brokering, synthesis
Repository context: opensoft/openMFA-spec with cross-product integration references
Captured: 2026-11-10

## Possible feats

- Qualify one broker adapter across two synthetic relying parties.
- Demonstrate refusal of cross-application receipt replay.

## Members and joints

[Verifier boundary](wallet-mfa-verifier-boundary.md) and [service records](wallet-mfa-service-records.md) connect relying-party authentication to factor verification and receipt issuance.

The broker requests a subject/session-bound challenge. openMFA verifies the response using configured custody. The broker validates the receipt and issues an audience-scoped token. The application evaluates current domain permission and grants.

## Separate consent and operations

The human approver uses a distinct authenticated session. Exact-operation consent is captured by the domain. A changed target or request invalidates approval. Authentication, consent, and execution retain separate outcomes.

Enrollment, replacement, key rotation, recovery, challenge cancellation, replay, and revocation each require observable state and audit. Healthy infrastructure does not establish successful authentication.

## Tradeoffs and decisions

Central verification supports consistent evidence and adds an availability dependency. Select custody isolation, storage, issuer trust, broker support, and revocation behavior during governance.

[Service overview](wallet-mfa-overview.md) maps the product. [Shared synthesis](https://github.com/opensoft/openxFactory/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-synthesis-authentication.md) owns the cross-factory composition.
