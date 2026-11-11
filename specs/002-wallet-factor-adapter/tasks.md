# Tasks: 002-wallet-factor-adapter

- [x] T001 [O] Capture commissioned scope and paired feature governance; files: `openspec/changes/add-wallet-factor-adapter/**, specs/002-wallet-factor-adapter/**`; verify from spec leg: `python3 scripts/validate-openspec-cli-pin.py --all --tarball tools/openspec-cli-pin/fission-ai-openspec-1.12.0-c844543999f673cdd72445879b86a4abea4c07ef.tgz`.
- [x] T002 [O] Implement required-config real wallet verifier bridge and refusal tests; files: `openmfa_runtime/wallet_factor.py, tests/wallet_factor/**`; verify: `python -m pytest tests/wallet_factor -q`. The actual owning-wallet implementation is exercised under T004, separately from bridge unit doubles.
- [x] T003 [O] Implement exact assembly/package gate and isolated qualification driver; files: `openmfa_runtime/assembly_gate.py, qualification/**, tests/assembly_gate/**, tests/qualification/**, pyproject.toml, .github/workflows/pytest-suite.yml`; verify: `python -m pytest tests/assembly_gate tests/qualification -q`. Full code-leg suite: 83 passed; 17 deliberately broken complete-assembly/package inputs refuse.
- [x] T004 [O] Run actual isolated cross-product tests and cleanup success/failure/cancellation readback; files: `qualification/**, specs/002-wallet-factor-adapter/evidence.md, specs/002-wallet-factor-adapter/evidence/*.json, specs/002-wallet-factor-adapter/quickstart.md`; verify in the configured code-leg qualification environment: `python qualification/run_isolated.py --wallet-root "$WALLET_ROOT" --mfa-root "$MFA_ROOT" --expected "$QUAL_EXPECTED" --evidence "$QUAL_SUCCESS_EVIDENCE"`. Actual success, injected failure and SIGTERM runs passed their expected gates with run-owned resource absence; artifacts and reproduction are recorded in the feature.
- [x] T005 [O] Reconcile evidence, publish paired PRs and verify CI/Codex; files: `docs/wallet-factor.md, PR metadata, feature evidence`; verify: `python -m pytest tests/ -q and current-head CI/review readback`.

T001 → T002 → T003 → T004 → T005. No parallel-agent execution is required.
The user's direct implementation/isolation instruction commissions these
source tasks; it is not a release, archive or live operational acceptance.

T005 local review is accepted under Brett Heap's explicit 2026-11-10
instruction. [local-review.md](local-review.md) records the specialist passes,
two qualification corrections and focused re-reviews. Exact-head CI and
protected landing will be recorded in commit-bound PR reviews. Usage-limit
responses and older receipts are not clean final-head GitHub bot reviews.
