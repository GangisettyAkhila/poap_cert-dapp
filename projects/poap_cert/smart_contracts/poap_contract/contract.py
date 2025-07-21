from beaker import *
from pyteal import *

class POAPCertificateApp(Application):

    @external
    def create_certificate(self, receiver: abi.Address, event_name: abi.String):
        return Seq(
            App.localPut(receiver.get(), Bytes("event_name"), event_name.get()),
            Approve()
        )

app = POAPCertificateApp()

app_spec = ApplicationSpec(
    app=app,
    schema=ApplicationStateSchema(
        local_ints=0,
        local_bytes=1,
        global_ints=0,
        global_bytes=0
    )
)
