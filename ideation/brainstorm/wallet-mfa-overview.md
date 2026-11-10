# openMFA Verification Service Overview — Brainstorm

Status: brainstorm
Kind: reference
Summary: Propose a public Apache-2.0 verification service composing with openWallet, an OIDC broker, and domain approvals.
Topics: wallet-mfa, openmfa, openwallet, codexfactory, medxfactory
Repository context: opensoft/openMFA-spec with cross-product integration references
Captured: 2026-11-10

## Possible feats

- Deliver a first verifier and broker adapter with explicit conformance tests.
- Supply verification evidence for the codeXfactory pilot.

## Motivation and intended delivery

Agents require attributable authentication. Applications require fresh, policy-evaluated evidence and independent approval where appropriate. openMFA provides a proposed common verifier interface.

The current product is a Triad scaffold and this design packet. Runtime endpoints, enrollment, tokens, and deployment remain proposed.

## Document map

- [Verification synthesis](wallet-mfa-synthesis-verification-service.md)
  - [Custody boundary](wallet-mfa-verifier-boundary.md)
  - [Service records](wallet-mfa-service-records.md)

## Triad ownership and license

[openMFA](https://github.com/opensoft/openMFA) is the assembly root pinning this spec leg and [openMFA-code](https://github.com/opensoft/openMFA-code). The spec leg holds future governance, requirements, service contracts, and acceptance. The code leg holds future implementation and tests. All three use Apache-2.0.

Future releases identify both legs through one pinned assembly commit and digests.

## Boundaries and first acceptance

openWallet presents key proofs and grant references. openMFA verifies extra evidence. The broker issues tokens. Applications decide subject resolution, domain authority, distinct-human approval, and effects.

The first pilot is one synthetic codeXfactory resource with agent authentication, separate approval, refusal tests, interruption recovery, and cleanup. Choose adapter, factors, custody, workload attestor, wire profile, and storage through implementation governance.

## Cross-system navigation

- [Shared architecture](https://github.com/opensoft/openxFactory/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-overview.md)
- [Wallet profile](https://github.com/opensoft/openWallet-spec/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-overview.md)
- [codeXfactory pilot](https://github.com/codeXfactory/codexFactory/blob/docs/wallet-mfa-design/ideation/brainstorm/wallet-mfa-overview.md)
