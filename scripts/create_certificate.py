from smart_contracts.poap_contract.config import CREATOR_MNEMONIC
import algokit_utils
from smart_contracts.artifacts.poap_contract.client import PoapCertClient

def create_certificate(recipient_address: str, event_name: str):
    # Setup Algorand client
    algod_client = algokit_utils.get_algod_client()
    creator_account = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Create typed app client
    app_client = PoapCertClient(
        algod_client=algod_client,
        creator=creator_account,
        template_values={"UPDATABLE": 1, "DELETABLE": 1}
    )

    # Issue certificate
    result = app_client.issue_cert(
        recipient=recipient_address,
        event=event_name,
    )
    print(f"Certificate issued! ID: {result.return_value}")

# Example usage
if __name__ == "__main__":
    # Replace with a valid recipient address
    create_certificate("RECIPIENT_TESTNET_ADDRESS", "Test Event")
