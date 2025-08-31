import pytest
from poap_contract.poap import app
from algokit_utils import client

# Connect to Algorand client
algod_client = client.get_algod_client()

def test_issue_and_verify_cert():
    # Issue a certificate
    cert_id = app.issue_cert(
        recipient="TEST_RECIPIENT_ADDRESS",
        event="Test Event",
        client=algod_client
    )

    # Verify certificate
    result = app.verify_cert(cert_id=cert_id, client=algod_client)
    assert result == "Test Event"

def test_revoke_cert():
    # Issue another certificate
    cert_id = app.issue_cert(
        recipient="TEST_RECIPIENT_ADDRESS",
        event="Revocable Event",
        client=algod_client
    )

    # Revoke it
    app.revoke_cert(cert_id=cert_id, client=algod_client)

    # Verify certificate
    result = app.verify_cert(cert_id=cert_id, client=algod_client)
    assert result == "Invalid or Revoked"
