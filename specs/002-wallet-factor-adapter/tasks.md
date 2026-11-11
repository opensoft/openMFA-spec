# Tasks: 002-wallet-factor-adapter

- [x] T001 [O] Capture commissioned scope and paired feature governance; files: `openspec/changes/add-wallet-factor-adapter/**, specs/002-wallet-factor-adapter/**`; verify from spec leg: `python3 scripts/validate-openspec-cli-pin.py --all --tarball tools/openspec-cli-pin/fission-ai-openspec-1.12.0-c844543999f673cdd72445879b86a4abea4c07ef.tgz`.
- [x] T002 [O] Implement required-config real wallet verifier bridge and refusal tests; files: `openmfa_runtime/wallet_factor.py, tests/wallet_factor/**`; verify: `python -m pytest tests/wallet_factor -q`. The actual owning-wallet implementation is exercised under T004, separately from bridge unit doubles.
- [x] T003 [O] Implement exact assembly/package gate and isolated qualification driver; files: `openmfa_runtime/assembly_gate.py, qualification/**, tests/assembly_gate/**, tests/qualification/**, pyproject.toml, .github/workflows/pytest-suite.yml`; verify: `python -m pytest tests/assembly_gate tests/qualification -q`. Full code-leg suite: 77 passed; 17 deliberately broken complete-assembly/package inputs refuse.
- [x] T004 [O] Run actual isolated cross-product tests and cleanup success/failure/cancellation readback; files: `qualification/**, specs/002-wallet-factor-adapter/evidence.md, specs/002-wallet-factor-adapter/evidence/*.json, specs/002-wallet-factor-adapter/quickstart.md`; verify in the configured code-leg qualification environment: `python qualification/run_isolated.py --wallet-root "$WALLET_ROOT" --mfa-root "$MFA_ROOT" --expected "$QUAL_EXPECTED" --evidence "$QUAL_SUCCESS_EVIDENCE"`. Actual success, injected failure and SIGTERM runs passed their expected gates with run-owned resource absence; artifacts and reproduction are recorded in the feature.
- [ ] T005 [O] Reconcile evidence, publish paired PRs and verify CI/Codex; files: `docs/wallet-factor.md, PR metadata, feature evidence`; verify: `python -m pytest tests/ -q and current-head CI/review readback`.

T001 → T002 → T003 → T004 → T005. No parallel-agent execution is required.
The user's direct implementation/isolation instruction commissions these
source tasks; it is not a release, archive or live operational acceptance.

T005 remains pending final review acceptance. Both source PRs are published
as drafts with current-head CI; GitHub Codex review of final MFA code head
9a1cc19276832a264ef34b0bb70d0d8e7860780f hit the usage limit. Its earlier
cleanup finding is fixed with focused regression and exact-source isolated
success/failure/SIGTERM qualification. No fresh clean bot receipt is claimed.
