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
        app_id=12345  # Replace with your actual app ID
    )

    result = app_client.call(
        "get_certificate",
        receiver=acct.address
    )
    print("Event Name:", result.return_value)

if __name__ == "__main__":
    main()
