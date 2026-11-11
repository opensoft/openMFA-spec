# Candidate design

Status: possession-only wire profile ratified; runtime acceptance pending

Owner ratification binds the baseline and scope in
[review/ratification-2026-11-10.md](review/ratification-2026-11-10.md).
This records no real custody, factor-adapter, human or live qualification.

## Context and scope

A file-backed, caller-bound challenge/receipt core with real issuer signatures, default-deny factor verification, cancellation, expiry, binding revocation and idempotent one-use consumption.

The public product owns neutral proof/evidence behavior. A relying party owns permission and explicit human consent. An authenticated adapter constructs caller context. A trusted factor backend verifies the response and resolves current binding state. Neither is supplied by untrusted JSON. The store is operator-controlled and dedicated to one issuer. No network adapter is enabled.

## Protocol choices

Use Ed25519 via cryptography 50.0.1 and RFC 8785 canonical bytes via rfc8785 0.1.4. These are candidate choices within the commissioned Ed25519/canonical-digest design, subject to review here. References: [Ed25519 API](https://cryptography.io/en/50.0.1/hazmat/primitives/asymmetric/ed25519/), [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html), [canonicalizer 0.1.4](https://pypi.org/project/rfc8785/0.1.4/).

Challenges last at most 120 seconds. Digest is `sha256:` plus SHA-256 of JCS of the complete challenge record. Receipts last at most 60 seconds and never beyond challenge, factor or issuer-key validity. Signature input is ASCII `openMFA.receipt.v0`, NUL, then JCS of all unsigned receipt fields. Encoding is strict unpadded base64url of 64 signature bytes. Times use trusted integer service seconds, zero skew and half-open validity. Cross-field time and trust rules are runtime checks beyond structural JSON Schema. Verified methods are exactly the single possession method; higher assurance refuses.

## State and trust

SQLite `BEGIN IMMEDIATE` serializes transitions and uniqueness constraints bind idempotency keys to caller namespace. A failed signer/verifier rolls back. Raw factor responses are not persisted, only a digest. Identical verification retries retrieve the unchanged historical receipt, including after expiry; this never refreshes authority. Fresh consumption checks current receipt validity, current binding and an exact non-null operation digest. Identical consumed retries retrieve a stable acknowledgement without making a new decision. Cancellation prevents pending/fresh use. Local binding revocation is a persistent store-wide tombstone. A remote current-binding response is only point-in-time evidence; no distributed fencing is claimed. Receipt consumption does not commit an external domain effect. Backend callbacks must be bounded; authenticated transport, availability controls and audit retention belong to the future service adapter.

## Limits and acceptance

- New schemas default to spec leg; legacy wallet Q7 does not automatically cover them.
- Bindings and caller contexts are trusted adapter inputs, never a client key or client verified flag.
- Only possession is implemented; requests for MFA or human assurance refuse.
- Remote custody, composition attestor, WebAuthn/OIDC adapters and provider discovery remain dependencies.
- Remote current-binding observation is point-in-time; no distributed revocation or external-domain atomicity claim.
- Receipt retries retrieve unchanged historical evidence; fresh consumption rechecks validity and current binding.
- All repository tests and leg CI must run after merge; in-memory preparation is not source/CI/live acceptance.
- Root pins stay fixed until reviewed leg PRs merge; development package version is not an allocated release.

## Migration and rollback

Additive candidate only. Existing released files and machine keys stay fixed. Disable/remove the candidate before an assembly release if rejected; do not rewrite ratification history. No product tag, root pin or consumer dependency is advanced by the leg PRs. Future remote custody, provider discovery, workload attestation and human verification require their own governed acceptance.
