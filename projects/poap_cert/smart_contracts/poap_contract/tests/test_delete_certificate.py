import pytest
from algosdk.v2client.algod import AlgodClient
from algokit_utils import get_localnet_default_account
from smart_contracts.artifacts.poap_contract.client import PoapCertClient

@pytest.fixture(scope="module")
def poap_client(algod_client: AlgodClient) -> PoapCertClient:
    account = get_localnet_default_account(algod_client)
    client = PoapCertClient(
        algod_client,
        creator=account,
    )
    client.deploy(
        allow_update=True,
        allow_delete=True,
    )
    return client

def test_delete_certificate(poap_client: PoapCertClient):
    # Issue a certificate
    result = poap_client.issue_cert(
        recipient=poap_client.app_creator.address,
        event="Test Event",
    )
    cert_id = result.return_value

    # Delete certificate
    poap_client.delete_certificate(cert_id=cert_id)

    # Verify certificate is invalid
    result = poap_client.verify_cert(cert_id=cert_id)
    assert result.return_value == "Invalid or Revoked"
