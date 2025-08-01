@external
def delete_certificate(self, receiver: abi.Address):
    return Seq(
        App.localDel(receiver.get(), Bytes("event_name")),
        Approve()
    )

