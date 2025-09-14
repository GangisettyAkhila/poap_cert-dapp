from smart_contracts.poap_contract.config import CREATOR_MNEMONIC
import algokit_utils
from smart_contracts.artifacts.poap_contract.client import PoapCertClient

def get_certificate(cert_id: int):
    # Setup Algorand client
    algod_client = algokit_utils.get_algod_client()
    creator_account = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Create typed app client
    app_client = PoapCertClient(
        algod_client=algod_client,
        creator=creator_account,
    )

    # Verify certificate
    result = app_client.verify_cert(cert_id=cert_id)
    print(f"Certificate details: {result.return_value}")

# Example usage
if __name__ == "__main__":
    get_certificate(0)  # Replace 0 with real cert ID
