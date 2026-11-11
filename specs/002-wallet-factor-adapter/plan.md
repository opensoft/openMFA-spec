# Plan: 002-wallet-factor-adapter

Governance: [add-wallet-factor-adapter](../../openspec/changes/add-wallet-factor-adapter/proposal.md).
Current trusted wallet factor mapping and exact-assembly isolated qualification.

Python 3.12, the existing cryptography/rfc8785 pins, SQLite and standard TLS
transport. Use the declared development bench and isolated test environments.
No project constitution is present; shared protocols and root shape rules apply.
Read the governing design for authenticated identities, persistence and
qualification boundaries. Implementation follows [tasks.md](tasks.md) in
order. Code-leg tests stay self-contained; the separately invoked integration
gate receives explicit complete assembly inputs and actual owning packages.
All paths committed here stay portable. Existing shape copies/digests,
ratified schemas, origin records and unrelated work remain preserved.
