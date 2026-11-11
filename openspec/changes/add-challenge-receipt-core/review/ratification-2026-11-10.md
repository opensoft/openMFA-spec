# Owner ratification — 2026-11-10

## Exact decision and approved baseline

Brett Heap was asked first-hand in this chat:

> Do you ratify the possession-only wire contracts in openWallet-spec #8
> (head `778cedb`) and openMFA-spec #2 (head `61ae1cb`)? T006 in both task
> lists explicitly says “Obtain owner acceptance”; the earlier codeXfactory
> #577 approval did not ratify these new contracts. Acceptance would cover the
> wallet proof and bound challenge/receipt profiles, while real custody,
> factor adapters, human approval and live qualification remain separate gates.

His answer was:

> Ratify both possession-only profiles

This repository's approved baseline is
[openMFA-spec #2](https://github.com/opensoft/openMFA-spec/pull/2)
at `61ae1cbe21fc5b9465b901ff57a92099e81b90b3`. The other profile is the paired owner decision;
it does not move this repository's ownership or contract boundary.
The reviewed code candidate is
[openMFA-code #2](https://github.com/opensoft/openMFA-code/pull/2)
at `1c908221b9df9515aaa1137bed31191888d9f8d8`; wire ratification does not independently accept
its operational realization.

## Exact approved schema bytes

| Baseline-relative file | SHA-256 |
| --- | --- |
| `contracts/challenge-v0.schema.json` | `764adda761fe34205f371dd6210313423e02607dcf970e992c5138be1f23d0d6` |
| `contracts/verification-receipt-v0.schema.json` | `10ceaaf660c5cda9cdadc862cfb055f590e8c0ecef0170b93ede85934d3fb091` |

The ratification-record commit changes governance standing and records the
owner's act. It changes no schema, technical requirement, algorithm, lifetime,
assurance bound, runtime code, original origin ID or commissioning field.

## Scope and remaining gates

The accepted profiles establish bounded cryptographic possession evidence.
They do not assert MFA, human presence, explicit human consent, workload
composition, delegation or domain permission. The relying party continues to
own permission and separate exact-request human consent.

Real custody, factor/registry adapters, workload composition evidence, human
approval and live qualification remain separate. Reviewed realization,
reviewed leg landings and any accepted assembly/consumer advancement must
satisfy their existing gates; no floating or unmerged leg becomes a product
pin. T006's owner decision is recorded, while its combined realization,
landing and qualification checkbox remains incomplete.

No product release, tag, OpenSpec archive, live provider/credential operation,
deployment or approval bypass is authorized by this record. Feedback remains
deferred and neither previously blocked write was replayed.
