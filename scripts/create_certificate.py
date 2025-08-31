from poap_contract.poap import app
from algokit_utils import client

def create_certificate(recipient_address: str, event_name: str):
    # Connect to Algorand client
    algod_client = client.get_algod_client()
    
    # Call issue_cert method
    cert_id = app.issue_cert(
        recipient=recipient_address,
        event=event_name,
        client=algod_client
    )
    
    print(f"Certificate issued! ID: {cert_id}")

# Example usage
if __name__ == "__main__":
    create_certificate("RECIPIENT_ADDRESS_HERE", "My First Event")
