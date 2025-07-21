from beaker import *
from pyteal import *

class CertificateApp(Application):

    @external
    def create_certificate(self, recipient: abi.Address, event_name: abi.String):
        return Approve()
