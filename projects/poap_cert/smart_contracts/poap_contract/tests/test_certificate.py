import pytest
from algosdk.v2client.algod import AlgodClient
from algosdk.atomic_transaction_composer import AccountTransactionSigner
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

def test_issue_and_verify_cert(poap_client: PoapCertClient):
    # Issue a certificate
    result = poap_client.issue_cert(
        recipient=poap_client.app_creator.address,
        event="Test Event",
    )
    cert_id = result.return_value

    # Verify certificate
    result = poap_client.verify_cert(cert_id=cert_id)
    assert result.return_value == "Test Event"

def test_revoke_cert(poap_client: PoapCertClient):
    # Issue another certificate
    result = poap_client.issue_cert(
        recipient=poap_client.app_creator.address,
        event="Revocable Event",
    )
    cert_id = result.return_value

    # Revoke it
    poap_client.revoke_cert(cert_id=cert_id)

    # Verify certificate
    result = poap_client.verify_cert(cert_id=cert_id)
    assert result.return_value == "Invalid or Revoked"
