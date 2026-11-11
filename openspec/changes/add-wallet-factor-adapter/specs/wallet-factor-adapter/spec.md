## Purpose

Translate real verified wallet possession over a fresh bound challenge into
the existing openMFA factor interface without introducing stronger assurance.

## ADDED Requirements

### Requirement: Trusted current wallet verification
The adapter SHALL require an explicitly configured owning-wallet verifier and
registry, resolve by trusted challenge subject, verify the expected digest,
and validate returned facts against the current exact binding. Client keys
or self-asserted verified facts SHALL NOT select trust inputs.

#### Scenario: Forgery or unavailable registry
- **WHEN** a forged proof, wrong binding or unavailable registry is presented
- **THEN** verification refuses and no receipt is minted.

### Requirement: Fresh current binding and bounded meaning
The adapter SHALL recheck current revision, reference, revocation and validity
before fresh use and bound factor validity by binding/challenge lifetime.
It SHALL retain possession-only assurance and point-in-time remote semantics.

#### Scenario: Revocation after verification
- **WHEN** the registry revokes or rotates the factor binding before consumption
- **THEN** fresh consumption refuses.
