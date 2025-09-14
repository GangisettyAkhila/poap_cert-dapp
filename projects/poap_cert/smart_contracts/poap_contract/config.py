import os
from dotenv import load_dotenv

load_dotenv()

CREATOR_ADDRESS = os.getenv("CREATOR_ADDRESS")
CREATOR_MNEMONIC = os.getenv("CREATOR_MNEMONIC")
