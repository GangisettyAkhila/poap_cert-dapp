import pytest
from beaker import sandbox
from smart_contracts.poap_contract.contract import POAPCertificateApp

@pytest.fixture(scope="module")
def app_client():
    app = POAPCertificateApp()
    return app.build().client(sandbox.get_algod_client())

def test_deploy(app_client):
    app_client.create()
    assert app_client.app_id != 0

def test_create_and_get_certificate(app_client):
    user = app_client.app_creator

    # Call create_certificate method
    app_client.call(
        "create_certificate",
        receiver=user.address,
        event_name="Hack Series 2025"
    )

    # Call get_certificate to fetch it
    result = app_client.call(
        "get_certificate",
        receiver=user.address
    )

    assert result.return_value == "Hack Series 2025"

