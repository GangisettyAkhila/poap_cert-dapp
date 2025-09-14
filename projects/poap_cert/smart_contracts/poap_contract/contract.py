
from beaker import Application, external, create, Authorize
from pyteal import *

class PoapCert(Application):
    """
    Proof of Attendance Protocol (POAP) Certificate Contract
    """

    # Global State
    cert_counter = ApplicationStateValue(
        stack_type=TealType.uint64, default=Int(0)
    )

    # Mappings
    cert_recipient = Mapping(TealType.uint64, TealType.bytes)
    cert_event = Mapping(TealType.uint64, TealType.bytes)
    cert_valid = Mapping(TealType.uint64, TealType.uint64)

    @create
    def create(self):
        return self.initialize_application_state()

    @external(authorize=Authorize.only_creator())
    def issue_cert(
        self, recipient: abi.Address, event: abi.String, *, output: abi.Uint64
    ):
        return Seq(
            (cert_id := ScratchVar()).store(self.cert_counter.get()),
            self.cert_counter.set(self.cert_counter + Int(1)),
            self.cert_recipient[cert_id.load()].set(recipient.get()),
            self.cert_event[cert_id.load()].set(event.get()),
            self.cert_valid[cert_id.load()].set(Int(1)),
            output.set(cert_id.load()),
        )

    @external(read_only=True)
    def verify_cert(self, cert_id: abi.Uint64, *, output: abi.String):
        return If(
            self.cert_valid[cert_id.get()] == Int(1),
            output.set(self.cert_event[cert_id.get()]),
            output.set(Bytes("Invalid or Revoked")),
        )

    @external(authorize=Authorize.only_creator())
    def revoke_cert(self, cert_id: abi.Uint64):
        return self.cert_valid[cert_id.get()].set(Int(0))

    @external(read_only=True)
    def get_certificate(self, recipient: abi.Address, *, output: abi.String):
        # This is a simplified implementation. A real-world app would need a more robust way
        # to look up certificates by recipient, as a recipient could have multiple certificates.
        # This implementation will only find the last certificate issued to a recipient.
        return output.set(self.cert_event[self.get_cert_id_by_recipient(recipient.get())])

    @external(read_only=True)
    def has_certificate(self, recipient: abi.Address, *, output: abi.Bool):
        return output.set(
            self.get_cert_id_by_recipient(recipient.get()) != Int(0)
        )
    
    @external
    def delete_certificate(self, cert_id: abi.Uint64):
        return self.cert_valid[cert_id.get()].set(Int(0))

    # Internal method to find a certificate ID by recipient address.
    # Note: This is a simplified and inefficient way to do this.
    # A more robust solution would involve a different data structure.
    @internal(TealType.uint64)
    def get_cert_id_by_recipient(self, recipient: TealType.bytes):
        i = ScratchVar(TealType.uint64)
        return For(
            i.store(Int(0)),
            i.load() < self.cert_counter,
            i.store(i.load() + Int(1)),
        ).Do(
            If(
                self.cert_recipient[i.load()] == recipient,
                Return(i.load()),
            )
        )
        Return(Int(0))

app = PoapCert()
