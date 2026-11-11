"""Structural wire checks only; cryptographic verification lives in the code leg."""
import json
from pathlib import Path
import pytest
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[2]
DIGEST="sha256:"+"1"*64

def read(name):
    schema=json.loads((ROOT/"contracts"/name).read_text())
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)

def rejects(validator,value):
    assert list(validator.iter_errors(value)), "negative structural fixture unexpectedly accepted"

def challenge():
    return dict(profile="openmfa.challenge.v0",id="challenge:fixture",issuer="issuer:fixture",
                caller_ref="caller:fixture",tenant="tenant:fixture",audience="audience:fixture",
                subject_ref="subject:fixture",request_digest=DIGEST,nonce="A"*43,
                method="wallet-ed25519-possession.v0",issued_at=1000,expires_at=1120)

def receipt():
    value=challenge()
    for field in ["nonce","method","issued_at"]:
        del value[field]
    value.update(profile="openmfa.verification-receipt.v0",alg="Ed25519",
                 id="receipt:fixture",key_ref="issuer-key:fixture",challenge_digest=DIGEST,
                 verified_methods=["wallet-ed25519-possession.v0"],verified_at=1000,
                 expires_at=1060,binding_ref="binding:fixture",binding_revision=3,signature="A"*86)
    return value

@pytest.mark.parametrize("name,example",[
    ("challenge-v0.schema.json",challenge),("verification-receipt-v0.schema.json",receipt)
])
def test_exact_fields_and_no_assurance_escalation(name,example):
    validator=read(name)
    value=example()
    validator.validate(value)
    for field in value:
        altered=dict(value);del altered[field]
        rejects(validator,altered)
    rejects(validator,dict(value,mfa=True))
    rejects(validator,dict(value,profile="unknown"))

def test_receipt_forbids_method_upgrade_and_client_key():
    validator=read("verification-receipt-v0.schema.json")
    for altered in [dict(receipt(),verified_methods=["mfa"]),dict(receipt(),public_key="client"),
                    dict(receipt(),signature="A"*85+"B")]:
        rejects(validator,altered)

@pytest.mark.parametrize("name,example,field",[
    ("challenge-v0.schema.json",challenge,"nonce"),
    ("challenge-v0.schema.json",challenge,"request_digest"),
    ("verification-receipt-v0.schema.json",receipt,"signature"),
    ("verification-receipt-v0.schema.json",receipt,"challenge_digest"),
    ("verification-receipt-v0.schema.json",receipt,"request_digest"),
])
@pytest.mark.parametrize("suffix",["\n","\r\n"])
def test_fixed_width_fields_reject_trailing_newlines(name,example,field,suffix):
    value=example()
    value[field]+=suffix
    rejects(read(name),value)
