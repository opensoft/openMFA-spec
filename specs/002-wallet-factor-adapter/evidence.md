# Isolated wallet-factor qualification — 2026-11-10

Status: implementation and isolated source qualification complete; final review pending

## Scope and immutable sources

Brett Heap commissioned the real wallet factor/registry/custody/assembly work
and chose: "Build portable reference services and qualify them in isolation".
The previously ratified possession-only wire profiles stay unchanged.

| Component | Exact tested code | PR |
| --- | --- | --- |
| openWallet registry/custody | `77f53b83567c5a1ffa10dbeb5e4b5de8f339fd92` | [openWallet-code #5](https://github.com/opensoft/openWallet-code/pull/5) |
| openMFA factor/gates/finalization | `9a1cc19276832a264ef34b0bb70d0d8e7860780f` | [openMFA-code #3](https://github.com/opensoft/openMFA-code/pull/3) |

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

- openWallet: **138 passed, one existing historical-comparison skip**, 115.15 seconds.
- openMFA: **77 passed**, 7.15 seconds, including three cleanup exception regressions.
- Focused registry/custody: **40 passed**; focused adapter/assembly/finalization: **29 passed**.
- Wallet syntax and plain/strict corpus validators passed: 21 positives, 42 negative confirmations, 11/11 requirements, zero errors/warnings.
- Pinned strict OpenSpec validation passed both owner packets; no vendored CLI/shape helper was edited.
- Current wallet [pytest CI](https://github.com/opensoft/openWallet-code/actions/runs/42938949394) and [wallet validation](https://github.com/opensoft/openWallet-code/actions/runs/42938949270) passed at `77f53b8`.
- Current MFA [pytest CI](https://github.com/opensoft/openMFA-code/actions/runs/42939892578) passed at `9a1cc19`.

## Actual isolated qualification

[Success report](evidence/isolated-success.json), case
`wmq-069fb16abf8c453e`, passed every declared gate:

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
`wmq-bba2b30bf8144fb9`, and
[SIGTERM cancellation](evidence/isolated-cleanup-cancelled.json), case
`wmq-385b170f4cfc4bfc`. Each observed its expected failure and verified absence
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

Final MFA bot review at `9a1cc19` was requested explicitly but hit the usage
limit. Earlier receipts do not cover that head. Paired spec review results are
read back on their own PRs. T005 remains pending final review acceptance;
no quota failure is represented as a clean receipt.

## Acceptance limits

These are actual cryptographic/service and container-isolation results for
portable reference software. The existing `isolated_invocable` model evidences
environment activity and confers no unsupervised authority. No production/HSM
custody, workload attestation, human authentication/consent, MFA assurance,
domain effect, accepted consumer execution pin or live QA qualification is
claimed. Host-loss/SIGKILL recovery and an independent pilot janitor remain
separate. Feedback stays deferred; neither blocked write was replayed.
