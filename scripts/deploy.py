from algokit_utils import get_localnet_default_account, get_algod_client
from smart_contracts.artifacts.poap_contract.client import PoapCertClient

def main():
    # Setup Algorand client and account
    algod_client = get_algod_client()
    account = get_localnet_default_account(algod_client)

    # Create typed app client
    app_client = PoapCertClient(
        algod_client,
        creator=account,
    )

    # Deploy the contract
    app_client.deploy(
        allow_update=True,
        allow_delete=True,
    )
    print(f"Deployed app ID: {app_client.app_id}")

if __name__ == "__main__":
    main()
