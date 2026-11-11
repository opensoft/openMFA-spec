## Purpose

Qualify actual cross-product runtime behavior against exact assembly source
bindings and isolated custody while preserving separate operational acceptance.

## ADDED Requirements

### Requirement: Exact complete assembly inputs
The gate SHALL require explicit complete assembly roots, exact commit/tree
identities, lockstep leg pins/digests and installed-package provenance. Missing,
dirty or mismatched inputs SHALL refuse before qualification.

#### Scenario: Wrong leg or package
- **WHEN** an assembly gitlink, declared digest or installed source differs
- **THEN** the gate fails without substituting a sibling or cached package.

### Requirement: Actual integration and observed cleanup
The isolated gate SHALL exercise actual wallet signatures, authenticated
custody/registry transport, signed receipts, one-use/retry/restart and negative
cases, then verify absence of its run-owned resources. Missing cleanup readback
SHALL fail qualification. It SHALL distinguish source conformance from live acceptance.

#### Scenario: Failed integration or finalization
- **WHEN** integration fails or resource absence cannot be observed
- **THEN** the result is failure and no accepted-runtime or live claim is made.
