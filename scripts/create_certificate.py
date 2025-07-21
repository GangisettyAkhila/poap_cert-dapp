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
        "create_certificate",
        receiver=acct.address,
        event_name="Hack Series 2025"
    )
    print("Certificate created:", result.confirmed_round)

if __name__ == "__main__":
    main()
