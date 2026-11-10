# Data model

Status: draft

Entities: CallerContext, immutable Challenge, VerifiedFactor, IssuerKey, receipt and persisted consumption outcome.

Challenge holds unpredictable nonce, issuer, authenticated caller/tenant/audience, subject, method, integer lifetime and optional immutable request digest. Receipt adds issuer key, verified method/time, factor binding/revision and signature. Persisted rows store state, response digest, idempotency keys and stable results. Response bodies and private keys are not persisted. Caller namespace is a digest of canonical trusted caller context. Historical retrieval is distinct from fresh online consumption.

Exact field schemas live under `contracts/` in this spec leg. Runtime cross-field, trusted-resolution, signature and current-state checks remain mandatory beyond schema structure.
