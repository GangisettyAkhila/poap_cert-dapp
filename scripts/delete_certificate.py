from poap_contract.poap import app
from poap_contract.config import CREATOR_ADDRESS, CREATOR_MNEMONIC
import algokit_utils

# Setup Algorand client
algorand = algokit_utils.AlgorandClient.from_mnemonic(CREATOR_MNEMONIC)
deployer = algorand.account.from_private_key(CREATOR_ADDRESS)

def revoke_certificate(cert_id: int):
    app.revoke_cert(cert_id=cert_id, client=algorand.client, signer=deployer.signer)
    print(f"Certificate {cert_id} revoked!")

# Example usage
if __name__ == "__main__":
    revoke_certificate(0)  # Replace 0 with real cert ID
