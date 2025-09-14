# client.py

from algosdk import account
from beaker import client, sandbox
from smart_contracts.poap_contract.contract import PoapCert

# initialize app + client
app = PoapCert()
app_client = client.ApplicationClient(
    client=sandbox.get_algod_client(),
    app=app,
    signer=sandbox.get_accounts().pop().signer,
)

# deploy the contract (if not already)
app_id, app_addr, txid = app_client.create()
print(f"Deployed App ID: {app_id}")

# call issue_cert
receiver = sandbox.get_accounts()[1].address
result = app_client.call(
    method="issue_cert",
    recipient=receiver,
    event="DevCon 2025",
)
cert_id = result.return_value
print(f"Certificate created for {receiver} with ID: {cert_id}")

# call verify_cert
result = app_client.call(
    method="verify_cert",
    cert_id=cert_id,
)
print(f"Fetched Event: {result.return_value}")
