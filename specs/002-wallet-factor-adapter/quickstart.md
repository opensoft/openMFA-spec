# Isolated reference qualification

Run in the declared development bench with Docker access and a dedicated
Python 3.12 environment. Use two complete disposable Triad checkouts whose
gitlinks, pin commits/digests and workflow references agree. Accepted product
roots and temporary source-conformance inputs are different acceptance stages.

The prototype qualification constructs private disposable source inputs with
the canonical openRepoShape bump-leg tool. It does not change or publish
the working product roots' pins. Reviewed root commits are required before
any later accepted consumer or deployment use.

Install the owning code packages selected by those inputs, including the MFA
qualification extra. The gate checks their actual module bytes against the
selected source; a different cached package or missing dependency refuses.
The driver builds new wheels from git archives, locks every wheel hash and
checks the installed container modules again.

A trusted expected-input JSON has the following structure, with real exact
Git commit/tree values supplied by the qualification operator:

```json
{
  "wallet": {"commit": "<40-hex-root-commit>", "tree": "<40-hex-root-tree>"},
  "mfa": {"commit": "<40-hex-root-commit>", "tree": "<40-hex-root-tree>"}
}
```

From the MFA code leg, with the selected roots and evidence paths supplied as
environment variables:

```sh
python qualification/check_negative_inputs.py \
  --wallet-root "$WALLET_ROOT" --mfa-root "$MFA_ROOT" \
  --expected "$QUAL_EXPECTED" --evidence "$QUAL_NEGATIVE_EVIDENCE"
python qualification/run_isolated.py \
  --wallet-root "$WALLET_ROOT" --mfa-root "$MFA_ROOT" \
  --expected "$QUAL_EXPECTED" --evidence "$QUAL_SUCCESS_EVIDENCE"
python qualification/check_cleanup.py \
  --wallet-root "$WALLET_ROOT" --mfa-root "$MFA_ROOT" \
  --expected "$QUAL_EXPECTED" --evidence "$QUAL_CLEANUP_EVIDENCE" \
  --subnet "$QUAL_CHECKED_SUBNET"
```

Normally Docker allocates the internal network automatically. Where its pools
are exhausted, pass --subnet with an operator-checked unused RFC2544 /28.
The driver checks existing Docker subnets and refuses overlap. The operator
also checks host/VPN routes first. This creates only a run-owned internal
network and never changes daemon pools or removes other networks.

The image base is immutable and must already be present. Dependency download
uses the explicit public index and exact versions; image installation is
offline and hash-locked. No credentials enter the build context or image.
Short-lived local CA/client credentials are generated after building and
copied into distinct run-owned role volumes. These credentials do not enroll
any external identity.

The custody service holds the wallet key; the verifier holds its issuer key
and registry-read credential. The agent holds only its subject-scoped client
credential. There are no host credential mounts, published ports, privileged
containers or Docker sockets. The trusted driver relays public test records
and performs local test administration; it is not a product identity broker.

The success run checks signatures, caller/digest isolation, one-use/stable
retry, real-clock expiry, service outage rollback/recovery, rotation and
persistent revocation. Cleanup checks separately inject failure and SIGTERM
after startup, require the expected failure and verify absence of all labeled
containers, networks, volumes and images. Missing absence readback fails.

Reports contain source identities, module/wheel hashes, gate outcomes and
resource labels. They exclude private keys, certificates, raw factors and
browser/session state. operational_acceptance remains false. This does not
qualify live custody, workload composition, a human authenticator, explicit
human consent, a domain effect or cleanup after host loss/SIGKILL; independent
pilot janitor and attended acceptance remain separate.
