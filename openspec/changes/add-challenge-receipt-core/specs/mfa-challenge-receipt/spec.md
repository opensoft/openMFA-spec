## ADDED Requirements

### Requirement: Bound challenges and default refusal
openMFA SHALL bind each unpredictable nonce challenge to issuer, caller, tenant, audience, subject, method and optional request digest. It SHALL refuse unsupported assurance and absent trusted factor backends. This candidate supports possession only.

#### Scenario: Missing backend
- WHEN a client submits self-asserted verified facts without a configured verifier
- THEN no receipt is minted.

### Requirement: Signed and current receipt
openMFA SHALL issue Ed25519 receipts only after trusted factor verification and current-binding checks. Receipt validity SHALL be bounded by 60 seconds, challenge expiry, factor validity and issuer-key expiry. Stateless verification SHALL NOT prove one-use or current domain authority.

#### Scenario: Tampering or expiry
- WHEN receipt fields, expected caller context or signature differ, or validity has expired
- THEN fresh use refuses.

### Requirement: Durable one-use and retry
openMFA SHALL persist issued, verified, consumed and cancelled state in SQLite transactions. Identical authorized retries SHALL return the previously stored result without extending validity or creating another consumption. Conflicting keys or operation digests SHALL refuse. Fresh consumption SHALL recheck expiry and revocation and require an exact non-null request digest.

#### Scenario: Concurrent consumers
- WHEN two callers race with the same bound idempotency key
- THEN they observe one durable outcome; a changed operation cannot consume again.

### Requirement: Authentication evidence boundary
openMFA SHALL keep human authentication, exact-request consent and domain permission separate. A possession receipt SHALL NOT assert MFA or human approval. A core consumption acknowledgement SHALL NOT claim atomicity with an external domain effect.

#### Scenario: Higher assurance requested
- WHEN MFA or human assurance is requested of this possession-only core
- THEN it refuses.
