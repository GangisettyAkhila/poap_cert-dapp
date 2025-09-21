import os
from dotenv import load_dotenv
import algokit_utils
from smart_contracts.poap_contract.config import CREATOR_MNEMONIC
from smart_contracts.poap_contract.algopy_contract import PoapCert  # Algopy contract class

load_dotenv()

def revoke_certificate(cert_id: int):
    """
    Revoke a POAP certificate by its ID
    """
    # Setup Algorand client
    algod_client = algokit_utils.get_algod_client()
    creator_account = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Load the Algopy contract
    app = PoapCert()
    app.compile("poap_cert.teal")  # Ensure contract is compiled

    # Deploy or connect to existing contract
    app_client = algokit_utils.deploy_app(
        algod_client=algod_client,
        creator=creator_account,
        approval_file="poap_cert.teal",
        clear_file="poap_cert.teal"
    )

    # Revoke the certificate
    app.revoke_cert(cert_id)
    print(f"Certificate {cert_id} revoked!")

# Example usage
if __name__ == "__main__":
    revoke_certificate(0)  # Replace 0 with real certificate ID
