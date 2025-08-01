@external(read_only=True)
def get_certificate(self, receiver: abi.Address, *, output: abi.String):
    return Seq(
        (event := ScratchVar()).store(App.localGet(receiver.get(), Bytes("event_name"))),
        If(event.load() == Bytes(""), 
           output.set("Certificate not found"), 
           output.set(event.load())),
        Approve()
    )
