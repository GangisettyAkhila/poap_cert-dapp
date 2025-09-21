import logging
import algokit_utils
from smart_contracts.poap_contract.config import CREATOR_ADDRESS, CREATOR_MNEMONIC
from smart_contracts.poap_contract.algopy_contract import PoapCert  # Algopy contract class

logger = logging.getLogger(__name__)

def deploy() -> None:
    """
    Deploy the PoAP certificate smart contract to Algorand testnet
    """
    # Setup Algorand client using deployer credentials from config.py
    algod_client = algokit_utils.get_algod_client()
    deployer = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Compile the Algopy contract (generates TEAL files)
    app = PoapCert()
    app.compile("poap_cert.teal")

    # Deploy the contract using Algokit utils
    app_client = algokit_utils.deploy_app(
        algod_client=algod_client,
        creator=deployer,
        approval_file="poap_cert.teal",
        clear_file="poap_cert.teal",  # You can split if you have separate clear program
    )

    # Fund the contract with 1 ALGO after deployment (optional)
    if app_client.app_id == 0:
        algod_client.send.payment(
            algokit_utils.PaymentParams(
                amount=algokit_utils.AlgoAmount(algo=1),
                sender=deployer.address,
                receiver=app_client.app_address,
            )
        )

    logger.info(
        f"Deployed PoAP contract: {app_client.app_name} (ID: {app_client.app_id})"
    )

if __name__ == "__main__":
    deploy()
