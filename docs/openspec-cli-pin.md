# OpenSpec tooling provenance

Status: candidate tooling

The two Python helpers are unchanged copies of the helpers carried by
opensoft/openWallet-spec at be34312a6ea48b2ce23d95872666960b7e816a83.
Their headers identify the original source:
opensoft/openxFactory at 44d8fbaf7d977668973dcd116040c9405416c2ea.
After their three-line vendoring header, their bytes match that source.
Defects in those helpers must be fixed upstream and re-vendored.

The OpenSpec 1.12.0 tarball is the exact content-addressed artifact already
carried by that wallet spec baseline, copied without alteration. The local
manifest records its SHA-512 and legacy SHA-1 and declares no exceptions.
It is openMFA's minimal tooling configuration, not a copy of the wallet's
historical dispositions or a product ancestry declaration.

The local workflow is openMFA's own. It checks the committed tarball before
installation and validates this leg only. No gate reads a sibling checkout.
The tarball is local; npm still resolves its dependency closure from the
registry at setup time. This is an explicit residual, not a hermetic install
claim. No branch-protection settings are changed by adding the workflow.

Run from this leg's root:

```sh
OPENSPEC_TELEMETRY=0 python3 scripts/validate-openspec-cli-pin.py --all --tarball tools/openspec-cli-pin/fission-ai-openspec-1.12.0-c844543999f673cdd72445879b86a4abea4c07ef.tgz
```

New upstream proposals require durable origin metadata before ratification.
The current challenge/receipt packet remains draft. Source/CLI validation
does not ratify it or qualify a live factor backend.
