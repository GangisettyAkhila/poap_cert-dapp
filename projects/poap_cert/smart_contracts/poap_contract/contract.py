from beaker import *
from pyteal import *

class POAPCertificateApp(Application):
    @external
    def create_certificate(self, receiver: abi.Address, event_name: abi.String):
        return Approve()
