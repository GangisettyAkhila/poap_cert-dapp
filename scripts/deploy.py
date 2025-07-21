from beaker import client, sandbox
from smart_contracts.poap_contract.contract import POAPCertificateApp

def main():
    app = POAPCertificateApp()
    algod_client = sandbox.get_algod_client()
    acct = sandbox.get_accounts().pop()
    app_client = client.ApplicationClient(
        client=algod_client,
        app=app,
        signer=acct.signer,
    )

    app_id = app_client.create()
    print(f"Deployed app ID: {app_id}")

if __name__ == "__main__":
    main()
