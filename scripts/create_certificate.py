import os
from dotenv import load_dotenv
import algokit_utils
from smart_contracts.poap_contract.config import CREATOR_MNEMONIC
from smart_contracts.poap_contract.algopy_contract import PoapCert  # Algopy contract class
from algopy import Address

load_dotenv()

def create_certificate(recipient_address: str, event_name: str):
    """
    Issue a POAP certificate to a recipient
    """
    # Setup Algorand client
    algod_client = algokit_utils.get_algod_client()
    creator_account = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Load the Algopy contract
    app = PoapCert()
    app.compile("poap_cert.teal")  # Ensure contract is compiled

    # Deploy app client if needed (or connect to existing)
    app_client = algokit_utils.deploy_app(
        algod_client=algod_client,
        creator=creator_account,
        approval_file="poap_cert.teal",
        clear_file="poap_cert.teal"
    )

    # Issue certificate
    cert_id = app.issue_cert(Address(recipient_address), event_name)
    print(f"Certificate issued! ID: {cert_id}")

# Example usage
if __name__ == "__main__":
    # Replace with a valid recipient address
    create_certificate("RECIPIENT_TESTNET_ADDRESS", "Test Event")
