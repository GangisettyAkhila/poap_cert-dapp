import pytest
from beaker.client import ApplicationClient
from beaker import localnet
from smart_contracts.poap_contract.contract import POAPCertificateApp

@pytest.fixture(scope="module")
def app_client():
    app = POAPCertificateApp()
    client = ApplicationClient(
        client=localnet.get_algod_client(),
        app=app,
        signer=localnet.get_accounts().pop(),
    )
    client.create()
    return client

def test_delete_certificate(app_client):
    receiver = app_client.signer.address
    event_name = "AlgoCon2025"

    # Create certificate
    app_client.call("create_certificate", receiver=receiver, event_name=event_name)

    # Delete certificate
    app_client.call("delete_certificate", receiver=receiver)

    # Try to read the deleted value
    result = app_client.get_local_state(receiver)
    assert "event_name" not in result
