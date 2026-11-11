# Isolated wallet-factor qualification — 2026-11-10

Status: implementation and isolated source qualification complete; local review complete; protected landing requires current-head CI

## Scope and immutable sources

Brett Heap commissioned the real wallet factor/registry/custody/assembly work
and chose: "Build portable reference services and qualify them in isolation".
The previously ratified possession-only wire profiles stay unchanged.

| Component | Exact tested code | PR |
| --- | --- | --- |
| openWallet registry/custody | `32c9254feffe6a856b9cc823af561fdfc45dc673` | [openWallet-code #5](https://github.com/opensoft/openWallet-code/pull/5) |
| openMFA factor/gates/finalization | `ddd59d573ef35390c9bbe70439db07ca62b58283` | [openMFA-code #3](https://github.com/opensoft/openMFA-code/pull/3) |

The complete temporary source inputs are bound in
[evidence/source-inputs.json](evidence/source-inputs.json). They were constructed
in private disposable clones using the canonical openRepoShape bump-leg tool.
Both roots passed naming/manifest/lockstep/shape gates. They bind wallet spec
`f71d8e09f963a12d9c46a461b96fd2d0ac659e66` and MFA spec
`ac3b5335a1b14da1a2d100e9604c49fa28857a19`, with the exact ratified schema
hashes checked again. These local source-conformance commits were never
published as accepted product or consumer pins. Working assembly pins and
all existing shape-copy digests remain unchanged.

## Local source and CI gates

- openWallet: **141 passed, one existing historical-comparison skip**, 139.16 seconds.
- openMFA: **83 passed**, 7.49 seconds, including three cleanup exception regressions.
- Focused registry/custody: **43 passed**; focused adapter/assembly/finalization: **35 passed**.
- Wallet syntax and plain/strict corpus validators passed: 21 positives, 42 negative confirmations, 11/11 requirements, zero errors/warnings.
- Pinned strict OpenSpec validation passed both owner packets; no vendored CLI/shape helper was edited.
- Current wallet [pytest CI](https://github.com/opensoft/openWallet-code/actions/runs/42943230683) and [wallet validation](https://github.com/opensoft/openWallet-code/actions/runs/42943230816) passed at `32c9254`.
- Current MFA [pytest CI](https://github.com/opensoft/openMFA-code/actions/runs/42943259692) passed at `ddd59d5`.

## Actual isolated qualification

[Success report](evidence/isolated-success.json), case
`wmq-ebb57bf3c09a468f`, passed every declared gate:

- Distinct custody, verifier and agent containers; read-only root filesystems, non-root users, dropped capabilities, bounded CPU/memory/PIDs and one internal network.
- Separate role credential/state volumes; no host credential mount, Docker socket, privileged mode or published port.
- Source-bound hash-locked wheels and byte-for-byte checks of installed container modules.
- Actual service-held wallet signing over mutual TLS, current registry resolution, real wallet signature verification and signed MFA receipts.
- Wrong signature/digest/caller, export and registry-only signing refusals checked against their exact expected refusal codes.
- Durable one-use, unchanged retry and verifier restart.
- Real-clock expiry, registry outage rollback/recovery, actual key rotation rejecting old evidence, current revocation and custody restart.

[Negative input report](evidence/isolated-negative-gates.json) passed **17**
refusal probes across disposable complete-assembly clones: wrong root commit/
tree, dirty roots, gitlink/pin mismatch, leg digest mismatch, empty shape pin,
shape-copy drift, wrong workflow reference and wrong installed-package source.
Input identities come from the accompanying source-input record; the negative
driver itself and installed modules were bound to the selected source.

[Cleanup summary](evidence/isolated-cleanup.json) independently exercised
[injected failure](evidence/isolated-cleanup-injected-failure.json), case
`wmq-0a7e21689a564ade`, and
[SIGTERM cancellation](evidence/isolated-cleanup-cancelled.json), case
`wmq-ded91d4b262344fe`. Each observed its expected failure and verified absence
of all run-labeled containers, networks, volumes and images. Private temporary
credential state was cleaned. Missing readback or cleanup exceptions force failure.

The first network allocation attempt correctly failed because the daemon's
automatic address pools were exhausted; its owned resources were cleaned.
The successful runs used operator-checked unused RFC2544 /28 subnets, guarded
against Docker overlap, without changing daemon pools or active networks.
See [quickstart.md](quickstart.md) for reproduction and acceptance boundaries.

## Review dispositions

Codex found that public-key bytes could acquire another subject under a fresh
key reference. Three regressions failed before the fix; registration now checks
persistent historical public-byte/subject/custody ownership and refuses
conflicting historical prototype state on open. Four new cases pass.
The wallet's exact-head `77f53b8356` bot receipt reports no major issues and
the original thread is resolved.

Codex also found that one Docker cleanup timeout could abort finalization.
The final MFA head catches subprocess/OS exceptions per listing/removal/readback,
continues all resource categories, cleans private state and returns failure
evidence. Three targeted tests pass. The finding thread is resolved with the
fix recorded; full actual success/failure/SIGTERM qualification was rerun.

Final bot review requests hit the usage limit. Brett Heap explicitly
authorized local review of all four PRs. [local-review.md](local-review.md)
records the full specialist passes and independent correction re-reviews.
No quota failure or older receipt is claimed as a clean final-head bot review.
Current-head CI and actual landing will be recorded in commit-bound PR reviews.

## Final local review corrections

The authorized local review corrected two qualification false greens.
Canonical signing probes and real second-subject bindings now detect
accidental permission grants (three mutation regressions). The cleanup
checker invalidates prior evidence, requires fresh reports and exit 1, and
binds cancellation to its observed current case (six regressions).
Independent contract/reliability re-reviews confirmed both fixes.
[local-review.md](local-review.md) also records the independently confirmed
SonarCloud S8707 false-positive disposition and explicit local acceptance.

Actual qualification was repeated at the final code heads above. The fresh
reports and case IDs in this document supersede the earlier qualification
snapshot. The paired MFA raw artifacts bind source, modules and wheels;
all run-owned resources were absent at final readback.

## Acceptance limits

These are actual cryptographic/service and container-isolation results for
portable reference software. The existing `isolated_invocable` model evidences
environment activity and confers no unsupervised authority. No production/HSM
custody, workload attestation, human authentication/consent, MFA assurance,
domain effect, accepted consumer execution pin or live QA qualification is
claimed. Host-loss/SIGKILL recovery and an independent pilot janitor remain
separate. Feedback stays deferred; neither blocked write was replayed.
