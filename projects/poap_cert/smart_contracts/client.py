# client.py

from algosdk import account
from beaker import client, sandbox
from contract.contract import POAPCertificateApp

# initialize app + client
app = POAPCertificateApp()
app_client = client.ApplicationClient(
    client=sandbox.get_algod_client(),
    app=app,
    signer=sandbox.get_accounts().pop().signer,
)

# deploy the contract (if not already)
app_id, app_addr, txid = app_client.create()
print(f"Deployed App ID: {app_id}")

# call create_certificate
receiver = sandbox.get_accounts()[1].address
app_client.call(
    method="create_certificate",
    receiver=receiver,
    event_name="DevCon 2025",
)
print(f"Certificate created for {receiver}")

# call get_certificate
result = app_client.call(
    method="get_certificate",
    receiver=receiver,
)
print(f"Fetched Event: {result.return_value}")
