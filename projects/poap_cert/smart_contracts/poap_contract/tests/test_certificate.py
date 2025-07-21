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
