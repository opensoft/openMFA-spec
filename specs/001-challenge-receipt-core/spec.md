# Feature Specification: openMFA challenge-receipt-core

**Feature Branch**: `001-challenge-receipt-core`
**Created**: 2026-11-10
**Status**: Draft candidate
**Input**: Commissioned upstream prerequisite following codeXfactory PR #577; local wire contract remains under review.

## User Scenarios & Testing

### User Story 1 - Verify bounded authentication evidence (Priority: P1)

A relying party needs fresh authentication evidence bound to its authenticated context, followed by one durable consumption.

**Independent Test**: Exercise a configured test verifier and real issuer signatures in a temporary store; one consumption and stable retry succeed, while cross-caller access, replay, expiry and revocation refuse. The explicit test verifier is not factor qualification.

**Acceptance Scenarios**:
1. Given valid trusted context, when the declared method succeeds, then only bounded verified facts are returned.
2. Given altered evidence or an unavailable trust dependency, when verification is attempted, then no new evidence or use is created.
3. Given a request for stronger assurance or domain permission, when this candidate is used, then it cannot supply that claim.

### Edge Cases

Unknown/missing fields, invalid signatures, wrong algorithm/profile, expired or revoked keys, wrong subject/caller/tenant/audience, conflicting retries, and unavailable signer/backend must refuse. Race, process restart, cancellation and response loss must preserve one durable outcome.

## Requirements

- **FR-001**: openMFA SHALL bind each unpredictable nonce challenge to issuer, caller, tenant, audience, subject, method and optional request digest. It SHALL refuse unsupported assurance and absent trusted factor backends. This candidate supports possession only.
- **FR-002**: openMFA SHALL issue Ed25519 receipts only after trusted factor verification and current-binding checks. Receipt validity SHALL be bounded by 60 seconds, challenge expiry, factor validity and issuer-key expiry. Stateless verification SHALL NOT prove one-use or current domain authority.
- **FR-003**: openMFA SHALL persist issued, verified, consumed and cancelled state in SQLite transactions. Identical authorized retries SHALL return the previously stored result without extending validity or creating another consumption. Conflicting keys or operation digests SHALL refuse. Fresh consumption SHALL recheck expiry and revocation and require an exact non-null request digest.
- **FR-004**: openMFA SHALL keep human authentication, exact-request consent and domain permission separate. A possession receipt SHALL NOT assert MFA or human approval. A core consumption acknowledgement SHALL NOT claim atomicity with an external domain effect.

## Key Entities

CallerContext, immutable Challenge, VerifiedFactor, IssuerKey, receipt and persisted consumption outcome.

## Success Criteria

- Every scoped positive and adversarial case passes in the code leg's offline suite.
- Structural contracts pass their own spec-leg checks; these checks make no signature claim.
- Existing product gates retain their declared behavior and limitations.
- No receipt/proof is described as human approval, MFA, workload composition or domain permission.

## Assumptions and exclusions

Trusted service clock, caller adapter, registry, signing adapter and operator-controlled file storage are explicit trust inputs. Real remote custody, human/provider adapters, public service transport, live QA, accepted assembly pins and release qualification remain outside this first candidate.
