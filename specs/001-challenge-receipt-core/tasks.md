# Tasks: 001-challenge-receipt-core

Status: possession-only wire profile ratified; implementation/operational acceptance pending

- [x] T001 [S] Capture commissioned scope, draft origin and governance; files: openspec/changes/add-challenge-receipt-core/**, specs/001-challenge-receipt-core/**; verify: source and boundaries named before code.
- [x] T002 [O] Define exact-field draft wire contracts in the spec leg and structural checks; files: contracts/*-v0.schema.json, tests/runtime_contracts/**; verify: schema positives and negatives.
- [x] T003 [O] Implement real receipt math and durable state transitions; files: openmfa_runtime/**, tests/challenge_service/**; verify: substantive positive, tamper, expiry, revocation, race and restart cases pass.
- [x] T004 [S] Run declared leg gates and reconcile evidence; files: specs/001-challenge-receipt-core/evidence.md, .github/workflows/**; verify: report source/CI/limitations separately.
- [x] T005 [S] Publish paired draft PRs and request Codex review; files: PR descriptions and exact-head review requests; verify: source heads and review receipt status recorded.
- [x] T007 [O] Add independently generated challenge-digest and signed-receipt known-answer vectors without changing the candidate wire profiles; files: code-leg `tests/challenge_service/generate_vectors.cjs`, `tests/challenge_service/vectors.json`, `tests/challenge_service/test_vectors.py`, `tests/challenge_service/VECTORS.md`, spec-leg `specs/001-challenge-receipt-core/{plan,evidence,tasks}.md`; verify: `python -m pytest tests/challenge_service/test_vectors.py -q` in the code leg, plus `node tests/challenge_service/generate_vectors.cjs` independently reproduces the committed bytes. Ten cases and exact Node reproduction passed; full suite: 48 passed. Use explicit fixture factors only; do not qualify a real adapter. This is candidate preparation under Brett Heap's instruction to continue upstream runtime prerequisites, not contract ratification.
- [ ] T006 [O] Obtain owner acceptance, land reviewed legs, advance the root in lockstep and qualify accepted adapter/custody/compatibility evidence. This owner/landing gate remains pending; no product release or live acceptance is claimed.

No other executable task list is created in the OpenSpec packet. No parallel-agent execution is required. Archive only after assembly advancement and actual acceptance.

T007 precedes T006. All current verification remains offline. Brett Heap completed T006's wire-contract owner decision on 2026-11-10: "Ratify both possession-only profiles", approving `61ae1cbe21fc5b9465b901ff57a92099e81b90b3`. The governing proposal's `review/ratification-2026-11-10.md` binds the exact schema bytes and scope. T006 remains unchecked because reviewed realization/leg landings, root advancement and real adapter/custody/compatibility acceptance remain separate outstanding gates. No release or live qualification is inferred.
