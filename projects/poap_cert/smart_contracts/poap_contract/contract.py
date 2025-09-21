import os
from dotenv import load_dotenv
from algopy import *

# Load environment variables
load_dotenv()
CREATOR_ADDRESS = os.getenv("CREATOR_ADDRESS")

# ---------------------------
# Algopy POAP Certificate Contract
# ---------------------------
class PoapCert(App):
    # Global state
    cert_counter = GlobalStateValue(key="cert_counter", value_type=int)
    # Mappings (as global state dicts)
    cert_recipient = GlobalStateMap(key_type=Address, value_type=Bytes)
    cert_event = GlobalStateMap(key_type=Address, value_type=Bytes)
    cert_valid = GlobalStateMap(key_type=Address, value_type=int)

    # ---------------------------
    # App creation
    # ---------------------------
    @create
    def create(self):
        self.cert_counter.set(0)

    # ---------------------------
    # Issue certificate
    # ---------------------------
    @call
    def issue_cert(self, recipient: Address, event: str) -> int:
        cert_id = self.cert_counter.get()
        self.cert_counter.set(cert_id + 1)
        self.cert_recipient[cert_id] = recipient
        self.cert_event[cert_id] = event
        self.cert_valid[cert_id] = 1
        return cert_id

    # ---------------------------
    # Verify certificate
    # ---------------------------
    @call
    def verify_cert(self, cert_id: int) -> str:
        if self.cert_valid.get(cert_id, 0) == 1:
            return self.cert_event[cert_id]
        return "Invalid or Revoked"

    # ---------------------------
    # Revoke certificate
    # ---------------------------
    @call
    def revoke_cert(self, cert_id: int):
        if Txn.sender() != CREATOR_ADDRESS:
            raise Exception("Only creator can revoke")
        self.cert_valid[cert_id] = 0

    # ---------------------------
    # Get last certificate of recipient
    # ---------------------------
    @call
    def get_certificate(self, recipient: Address) -> str:
        # simplified: returns last cert issued to this recipient
        for cert_id in range(self.cert_counter.get()):
            if self.cert_recipient.get(cert_id) == recipient:
                return self.cert_event[cert_id]
        return "No certificate found"

    # ---------------------------
    # Check if recipient has certificate
    # ---------------------------
    @call
    def has_certificate(self, recipient: Address) -> bool:
        for cert_id in range(self.cert_counter.get()):
            if self.cert_recipient.get(cert_id) == recipient and self.cert_valid.get(cert_id, 0) == 1:
                return True
        return False

    # ---------------------------
    # Delete certificate
    # ---------------------------
    @call
    def delete_certificate(self, cert_id: int):
        self.cert_valid[cert_id] = 0

# ---------------------------
# Compile contract
# ---------------------------
if __name__ == "__main__":
    app = PoapCert()
    app.compile("poap_cert.teal")
    print("✅ Algopy POAP Certificate contract compiled successfully!")
