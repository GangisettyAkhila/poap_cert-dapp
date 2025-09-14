import logging
import algokit_utils
from smart_contracts.poap_contract.config import CREATOR_ADDRESS, CREATOR_MNEMONIC

logger = logging.getLogger(__name__)

def deploy() -> None:
    """
    Deploy the PoAP certificate smart contract to Algorand testnet
    """
    # Import the compiled contract factory
    from smart_contracts.artifacts.poap_contract.client import PoapCertClient

    # Setup Algorand client using deployer credentials from config.py
    algorand = algokit_utils.get_algod_client()
    deployer = algokit_utils.get_account_from_mnemonic(CREATOR_MNEMONIC)

    # Create typed app factory
    app_client = PoapCertClient(
        algod_client=algorand,
        creator=deployer,
    )

    # Deploy the contract
    app_client.deploy(
        on_update=algokit_utils.OnUpdate.AppendApp,
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
    )

    # Fund the contract with 1 ALGO after deployment
    if app_client.app_id == 0:
        algorand.send.payment(
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

