import os
from dotenv import load_dotenv
from algopy import *

# Load environment variables
load_dotenv()
CREATOR_ADDRESS = os.getenv("CREATOR_ADDRESS")

# ---------------------------
# Step 1: Define POAP smart contract in Algopy
# ---------------------------
class POAP(App):
    # Define global state variables
    creator = GlobalStateValue(key="creator", value_type=Address)
    event_name = GlobalStateValue(key="event", value_type=Bytes)
    recipient_count = GlobalStateValue(key="count", value_type=int)

    # On app creation
    @create
    def create(self):
        self.creator.set(CREATOR_ADDRESS)
        self.event_name.set("My First POAP Event")
        self.recipient_count.set(0)

    # On claiming POAP
    @call
    def claim(self):
        self.recipient_count.set(self.recipient_count.get() + 1)

# ---------------------------
# Step 2: Compile Algopy contract
# ---------------------------
if __name__ == "__main__":
    poap_app = POAP()
    poap_app.compile("poap_app.teal")
    print("✅ Algopy POAP contract compiled to poap_app.teal successfully!")
