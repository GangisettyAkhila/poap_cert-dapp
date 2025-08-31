from poap_contract.poap import app
from poap_contract.config import CREATOR_ADDRESS, CREATOR_MNEMONIC
import algokit_utils

# Setup Algorand client
algorand = algokit_utils.AlgorandClient.from_mnemonic(CREATOR_MNEMONIC)
deployer = algorand.account.from_private_key(CREATOR_ADDRESS)

def create_certificate(recipient_address: str, event_name: str):
    cert_id = app.issue_cert(
        recipient=recipient_address,
        event=event_name,
        client=algorand.client,
        signer=deployer.signer
    )
    print(f"Certificate issued! ID: {cert_id}")

# Example usage
if __name__ == "__main__":
    create_certificate("RECIPIENT_TESTNET_ADDRESS", "Test Event")
