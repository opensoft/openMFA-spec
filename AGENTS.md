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
