# Research and decisions

Status: draft

Use the fixed Ed25519 profile disclosed by the parent pilot. RFC 8785 provides explicit canonical serialization rather than Python dict ordering. Canonical unpadded base64url and domain separation prevent ambiguous or cross-protocol signature reuse. Current key metadata is supplied by a trusted resolver, never selected by a client proof.

SQLite keeps the first state transition and durable outcome within one small transaction. It deliberately does not promise atomicity with an external relying party effect. A default-deny FactorVerifier interface permits later accepted adapters without inventing verified claims now.

Primary references: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html), [Ed25519 API](https://cryptography.io/en/50.0.1/hazmat/primitives/asymmetric/ed25519/), [rfc8785 0.1.4](https://pypi.org/project/rfc8785/0.1.4/).
