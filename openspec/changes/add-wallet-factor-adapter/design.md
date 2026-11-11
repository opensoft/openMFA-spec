## Context

The challenge core accepts a trusted FactorVerifier and refuses absent
backends. The user commissioned real wallet integration and isolated services.

## Goals / Non-Goals

Use actual owning-wallet crypto with current registry facts, signed receipts
and one-use/restart/refusal tests. No human broker, workload attestation,
production deployment, factor enrollment or authority-vocabulary change.

## Decisions

Keep the adapter independent of a sibling source tree. Trusted server
composition supplies the registry and owning wallet verify_proof callable;
there is no default backend or client verified flag. Resolve by challenge
subject, verify the expected challenge digest and full trusted binding, then
validate returned facts and cap lifetime by binding/challenge validity.
Current checks resolve again and compare exact binding/revision; absence,
expiry, revocation, dependency exceptions and malformed verified facts refuse.
The ordinary code-leg unit gate tests this bridge without a foreign checkout.
The explicit assembly qualification supplies the actual owning wallet package.

The compatibility gate receives complete assembly roots explicitly. Require
clean exact commit/tree identities and recomputed leg gitlinks/pin records,
plus installed-package/source binding before integration. It never silently
finds siblings, downloads source or substitutes a fixture on missing input.
Temporary source-conformance assemblies are recorded as development evidence;
passing this gate cannot grant deployment or accepted consumer-pin standing.

Run custody, verifier and agent in separate disposable containers. The
trusted test driver transports public challenge/proof/receipt JSON between
them. Custody keeps wallet keys; verifier keeps issuer keys and registry-read
credentials; the agent holds only its subject-scoped client credential.
No container has a Docker socket, host credential directory, privileged mode
or published port. Use a run-owned internal network and readonly filesystems
with explicit state volumes. Always finalize containers/network/volumes and
read back absence, including failure paths.

## Risks / Trade-offs

Remote revocation is point-in-time -> preserve explicit current checks and
avoid any distributed fencing claim. The driver is trusted test administration
and is not a product authentication broker. Source conformance and container
separation do not prove hardware custody, real workload composition or human
approval. Those remain distinct pilot gates.

## Migration Plan

Additive adapter and qualification tooling; core receipt/proof bytes unchanged.
Leg review and root lockstep pins remain the ordinary advancement mechanism.
Disable the configured backend to restore default refusal.
