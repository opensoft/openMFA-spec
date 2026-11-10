# Tasks: 001-challenge-receipt-core

Status: draft implementation; new contract not ratified

- [x] T001 [S] Capture commissioned scope, draft origin and governance; files: openspec/changes/add-challenge-receipt-core/**, specs/001-challenge-receipt-core/**; verify: source and boundaries named before code.
- [x] T002 [O] Define exact-field draft wire contracts in the spec leg and structural checks; files: contracts/*-v0.schema.json, tests/runtime_contracts/**; verify: schema positives and negatives.
- [x] T003 [O] Implement real receipt math and durable state transitions; files: openmfa_runtime/**, tests/challenge_service/**; verify: substantive positive, tamper, expiry, revocation, race and restart cases pass.
- [x] T004 [S] Run declared leg gates and reconcile evidence; files: specs/001-challenge-receipt-core/evidence.md, .github/workflows/**; verify: report source/CI/limitations separately.
- [ ] T005 [S] Publish paired draft PRs and request Codex review; files: PR descriptions and exact-head review requests; verify: source heads and review receipt status recorded.
- [ ] T006 [O] Obtain owner acceptance, land reviewed legs, advance the root in lockstep and qualify accepted adapter/custody/compatibility evidence. This owner/landing gate remains pending; no product release or live acceptance is claimed.

No other executable task list is created in the OpenSpec packet. No parallel-agent execution is required. Archive only after assembly advancement and actual acceptance.
