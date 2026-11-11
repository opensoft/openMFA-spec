# Candidate evidence — 2026-11-10

Status: possession-only wire contract ratified; runtime acceptance pending

## Current owner standing

Brett Heap answered "Ratify both possession-only profiles" on 2026-11-10,
accepting spec baseline `61ae1cbe21fc5b9465b901ff57a92099e81b90b3`.
The governing proposal's [owner record](../../openspec/changes/add-challenge-receipt-core/review/ratification-2026-11-10.md)
preserves the question/response, exact schema digests and exclusions. Historical
draft/pending-ratification statements below describe earlier preparation.
Current code candidate remains `1c908221b9df9515aaa1137bed31191888d9f8d8`; real custody,
factor adapters, human approval, live qualification and assembly acceptance
remain separate gates. No technical contract or runtime byte changed to
record this owner decision.

## Commission and source

Parent [codeXfactory #577](https://github.com/codeXfactory/codexFactory/pull/577) merged at `03d0fd28719ad8756dc3b533aa91f2b0ef5397e7` after the corrected required check passed. The owner accepted that proposal's specific origin-ID correction through its recorded disposition. That history does not ratify this new contract.

Code candidate: [PR](https://github.com/opensoft/openMFA-code/pull/2), source `1c908221b9df9515aaa1137bed31191888d9f8d8`. This adds independent known-answer tests to the previous runtime implementation; runtime behavior and wire contracts are unchanged. Governance and new wire contracts remain draft in this spec leg. No assembly pin, product release or consumer execution pin was advanced.

## Local verification

- Code-leg full pytest: **48 passed**, 39.55 seconds. State tests explicitly use a synthetic factor backend while issuer receipt signatures are real. Existing tests generate keys in memory; known-answer vectors use deliberately public test seeds.
- Spec-leg structural pytest after review corrections: **13 passed**, in a fresh isolated environment installed solely from the eleven local hash-locked wheels. Structural fixtures, including zero-byte-shaped signature strings, do not assert cryptographic validity.
- Pinned OpenSpec CLI 1.12.0: **1 targets passed, 0 failed**, strict clean. Tarball SHA-512/SHA-1 verified before installation. npm dependency setup still resolves from the registry.
- Scoped strict origin validation from the parent's pinned proposal helper at `93d13d6c8e14008c0b66adea65756d106fef6227`: no origin errors.
- Vendored CLI helpers and tarball compare byte-for-byte with the declared wallet spec baseline. The minimal local tooling pin grants no historical exceptions.
- Both assembly roots passed naming, manifest and lockstep pin/shape validation with original leg pins unchanged.

An isolated development cross-product check also exercised actual wallet math into a signed receipt and one-use retry, refusing cross-challenge replay and later revocation. Its temporary adapter is not shipped as an accepted production factor backend and does not create a dependency pin.

## Execution tracking

The pinned CLI's generic `instructions apply` diagnostic reports no embedded OpenSpec checklist. This is the shared workflow's deliberate Speckit handoff: [tasks.md](tasks.md) is the sole executable list. Planning/validation success does not archive the proposal or imply completed realization.

## CI, review and remaining acceptance

Review corrections: the structural gate now installs a complete SHA-256-locked wheel closure locally with index/version checks disabled. Exact field lengths reject terminal LF/CRLF in digests, signatures and nonce; the new fixtures cover both endings. This introduces no offline-gate exception and changes no runtime proof behavior.

CI hardening: the structural-test workflow now permits binary dependencies only. This fixes Sonar rule `githubactions:S8541` found on wallet spec PR #8; the same scoped workflow change is applied here. A no-install resolution check confirmed wheel availability for the declared Python 3.12 dependency closure. No gate, rule or exception is weakened.

Published draft spec: [openMFA-spec #2](https://github.com/opensoft/openMFA-spec/pull/2). Separate assembly tooling [openMFA #2](https://github.com/opensoft/openMFA/pull/2) merged normally at `c0873fde1c10274f395522179704351fb74e0c45`, preserving original leg pins. A fresh exact `@codex review` request produced a `chatgpt-codex-connector[bot]` receipt explicitly naming current code commit `1c908221b9` with no major issues. This is review evidence for that code head, not contract ratification or live acceptance.

Code CI passed on the exact current source head recorded above: [pytest run](https://github.com/opensoft/openMFA-code/actions/runs/42926807457). The source workflow uses read-only repository permissions. Current spec CI and review are read back on that PR after its evidence update.

The source CI workflows and exact `@codex review` request are published on the code PR. A request is not a review receipt. Current PR results and later heads must be checked separately; local evidence above is not a CI claim.

## Independent compatibility prerequisite

T007 is complete at the code head above. Two fixed vectors independently
generated with Node 24.21.0/OpenSSL 3.5.8 cover null/bound request digests,
Unicode and the maximum safe binding revision. Python cryptography used
OpenSSL 4.0.2 for verification. Ten cases passed in 3.34 seconds; the Node
generator reproduced the complete corpus exactly. Vector SHA-256:
`9df0b5501d36d735f0563f32b79b0999ec2267be57af191933b4b9c99421ee55`.
The code-leg `tests/challenge_service/VECTORS.md` documents provenance,
reproduction and limits. All fixed seeds are deliberately public test material.

Actual service issuance matches the independent challenge record/digest and
receipt signature. Wrong-domain/changed-byte messages, wrong caller, expiry
and issuer revocation refuse. The service test uses an explicit fixture
factor and test-only nonce/ID replacements. This closes candidate known-answer
preparation, not real factor or accepted assembly interoperability qualification.

Owner review/ratification of the new wire profile, accepted assembly compatibility, real factor/registry/custody acceptance, workload composition evidence, provider and human adapters, reviewed leg merges and assembly pins remain pending. Possession evidence confers no MFA, human approval or domain permission. No live tenant, enrollment, identity-provider or deployment operation was performed. No OpenSpec archive or product tag is authorized by this evidence.
