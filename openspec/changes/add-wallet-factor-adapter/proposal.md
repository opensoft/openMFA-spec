---
Status: commissioned implementation; isolated reference qualification
code_surface: openmfa_runtime wallet factor adapter, adapter tests and assembly compatibility qualification
target_release: unallocated; no production service or product release
---

## Why

The ratified receipt core deliberately refuses without a real factor backend.
The pilot needs an adapter that verifies an actual openWallet signature
against a current trusted registry and separate signer custody, plus gates
that verify complete assembly inputs and observed cleanup.

## What Changes

- Add a required-config wallet verifier bridge: resolve by trusted challenge
  subject, verify through the owning wallet implementation, bind returned
  facts to the current registry/challenge and recheck on consumption.
- Keep the neutral core independent of a wallet checkout. Trusted composition
  supplies the owning wallet verifier and registry; no request flag or inline
  client public key can enable verification.
- Add isolated end-to-end qualification with actual wallet proof math, mutual
  TLS custody/registry calls, signed receipts, replay/refusal/restart cases and
  disposable-resource cleanup readback.
- Add assembly compatibility checks for exact roots, leg commits/digests and
  installed package provenance. Missing or mismatched inputs refuse.

## Capabilities

### New Capabilities
- `wallet-factor-adapter`: current trusted wallet possession verification for the existing challenge/receipt profile.
- `runtime-assembly-compatibility`: exact-source isolated cross-product qualification with cleanup evidence.

### Modified Capabilities
None. Possession does not become MFA, human approval, workload attestation or
domain permission. Existing proof/challenge/receipt wire bytes remain fixed.

## Impact

Brett Heap directly commissioned this work and selected portable reference
services qualified in isolation. The paired wallet feature owns its registry,
custody and transport. This feature owns factor mapping and cross-product
qualification. A development qualification is not an accepted consumer pin or
production deployment. The sole executable list is
[feature 002](../../../specs/002-wallet-factor-adapter/tasks.md).
Feedback remains deferred and neither previously blocked write is replayed.
