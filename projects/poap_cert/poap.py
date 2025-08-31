import beaker
import pyteal as pt


class PoapCert(beaker.Application):
    """
    Proof of Attendance Protocol (POAP) Certificate Contract
    """

    # 🔹 Global / Local State
    # Store certificates as mapping: cert_id -> (recipient, event_name, valid)
    cert_counter = beaker.GlobalStateValue(
        stack_type=pt.TealType.uint64, default=pt.Int(0)
    )

    # cert_id -> recipient address
    cert_recipient = beaker.Mapping(
        key_type=pt.TealType.uint64, value_type=pt.TealType.bytes
    )

    # cert_id -> event name
    cert_event = beaker.Mapping(
        key_type=pt.TealType.uint64, value_type=pt.TealType.bytes
    )

    # cert_id -> validity flag (1 = valid, 0 = revoked)
    cert_valid = beaker.Mapping(
        key_type=pt.TealType.uint64, value_type=pt.TealType.uint64
    )

    # 🔹 Issue Certificate (only creator can issue)
    @beaker.create
    def issue_cert(
        self, recipient: pt.abi.Address, event: pt.abi.String, *, output: pt.abi.Uint64
    ):
        return pt.Seq(
            (cert_id := pt.ScratchVar()).store(self.cert_counter.get()),
            # Increment cert counter
            self.cert_counter.set(self.cert_counter.get() + pt.Int(1)),
            # Store mappings
            self.cert_recipient[cert_id.load()].set(recipient.get()),
            self.cert_event[cert_id.load()].set(event.get()),
            self.cert_valid[cert_id.load()].set(pt.Int(1)),
            output.set(cert_id.load()),  # Return new cert ID
        )

    # 🔹 Verify Certificate
    @beaker.external
    def verify_cert(
        self, cert_id: pt.abi.Uint64, *, output: pt.abi.String
    ):
        return pt.Seq(
            pt.If(
                self.cert_valid[cert_id.get()] == pt.Int(1),
                output.set(self.cert_event[cert_id.get()]),
                output.set(pt.Bytes("Invalid or Revoked")),
            )
        )

    # 🔹 Revoke Certificate (optional)
    @beaker.external(authorize=beaker.Authorize.only_creator())
    def revoke_cert(self, cert_id: pt.abi.Uint64):
        return self.cert_valid[cert_id.get()].set(pt.Int(0))


app = PoapCert()
