---
Status: ratified
Ratified: 2026-11-10 by Brett Heap for the possession-only wire profile; see review/ratification-2026-11-10.md for the approved baseline and limits.
code_surface: A file-backed, caller-bound challenge/receipt core with real issuer signatures, default-deny factor verification, cancellation, expiry, binding revocation and idempotent one-use consumption.
target_release: unallocated; no product version or release tag is reserved here.
---

# add-challenge-receipt-core

## Why

The existing design capture does not provide a cryptographic runtime. A file-backed, caller-bound challenge/receipt core with real issuer signatures, default-deny factor verification, cancellation, expiry, binding revocation and idempotent one-use consumption.

Brett Heap commissioned this upstream prerequisite after ratifying [codeXfactory PR #577](https://github.com/codeXfactory/codexFactory/pull/577), merged at `03d0fd28719ad8756dc3b533aa91f2b0ef5397e7`. That commission authorized candidate preparation. On 2026-11-10 he separately ratified this possession-only wire profile at `61ae1cbe21fc5b9465b901ff57a92099e81b90b3`; the [owner record](review/ratification-2026-11-10.md) preserves the exact response, schema digests and exclusions. Runtime realization, custody/factor acceptance, human approval and live qualification remain separate gates.

## What Changes

Add the candidate contract and a bounded Python runtime with substantive adversarial tests. The initial method is possession only. Missing factor backends and requests for MFA or human assurance refuse. A future real adapter needs separate acceptance.

## Capabilities

### New Capabilities
- `mfa-challenge-receipt`: A file-backed, caller-bound challenge/receipt core with real issuer signatures, default-deny factor verification, cancellation, expiry, binding revocation and idempotent one-use consumption.

### Modified Capabilities
None. Existing released contracts are unchanged.

## Impact

Bootstrap portable OpenSpec/Speckit feature tooling in a separate assembly-root PR. This tooling changes neither leg pin nor any shape-pinned file, and excludes host-local selectors and unfilled constitution state.

That draft tooling includes two bounded corrections found during review: honor the paired spec selector during core creation, and refuse resume when origin cannot be verified. Declare these deviations from the generated baseline, retain its provenance without a false content marker, and run isolated regression fixtures. No shared distribution or shape pin is changed.

Canonical contracts and full governance live in this spec leg. Implementation and offline tests live in the paired code leg. The assembly root and any consumer advance only after reviewed leg PRs merge, through lockstep pins. Development metadata `0.0.0.dev0` is not an allocated release. No live identity, credential, enrollment, tenant policy or deployment action is part of this change.

## Implementation Handoff

[Feature 001-challenge-receipt-core](../../../specs/001-challenge-receipt-core/plan.md) owns the sole executable task list. Do not archive before the leg reviews and assembly pin PR land.
