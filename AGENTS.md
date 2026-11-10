This is the **spec leg** of openMFA (`openmfa`): requirements, decisions
and acceptance criteria.

**The project's rules are not here.** They are in the assembly root
`opensoft/openMFA`, in `AGENTS-shape.md` — read that before touching anything
that spans the legs. This leg is mounted there at `spec/`, and the other leg,
`opensoft/openMFA-code`, beside it at `../code/`, once the root is cloned with
`--recurse-submodules`.

Working here is ordinary — an ordinary repository on an ordinary branch. What
advancing this leg does NOT do is advance the project: that is ONE commit in
`opensoft/openMFA` moving the gitlink, `contracts/spec-pin.yaml` and every
workflow `@<sha>` for this leg together.

Being the spec leg confers no authority over specifications. The split is
navigation.

## Candidate runtime gates

Use the assembly root and shared OpenSpec/Speckit protocol. Governance and the
single Speckit task list live here; code and its tests live in the paired code
feature. New wire profiles remain draft until actual owner acceptance.

From this leg's root, run `python -m pytest tests/runtime_contracts -q` and
`python3 scripts/validate-openspec-cli-pin.py --all --tarball tools/openspec-cli-pin/fission-ai-openspec-1.12.0-c844543999f673cdd72445879b86a4abea4c07ef.tgz`.
Use only the pinned OpenSpec CLI. The helpers are vendored tooling; see
`docs/openspec-cli-pin.md` for source, content address and setup residual.
Do not copy historical exceptions into this product or edit vendored helpers
to clear findings. All tests validate this leg only.
