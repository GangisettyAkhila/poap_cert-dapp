# 🎟️ POAP Certificate DApp on Algorand

This is a **Proof of Attendance Protocol (POAP)** smart contract DApp built on the **Algorand blockchain**. It allows organizers to issue **verifiable certificates or badges** to participants of events (workshops, hackathons, meetups, etc.) using Algorand NFTs.

---

## 🚀 Features

- ✅ Mint on-chain POAP certificates for event attendees
- ✅ Participants can claim their certificate by connecting their wallet
- ✅ Certificates are **tamper-proof**, **verifiable**, and **permanent**
- ✅ Issued using Algorand **Standard Assets (ASA)**

---

## 🧠 Use Case

Most college events and workshops issue certificates via PDF — which are easily faked, lost, or unverifiable. This DApp solves the problem by issuing a **blockchain-based proof of attendance**, visible to anyone on-chain.

---

## ⚙️ Tech Stack

- 🧠 **Smart Contracts**: PyTeal (Python for Algorand)
- 🔁 **Beaker**: Smart contract framework
- 🌐 **Frontend**: (Coming soon — React / HTML+JS)
- 🔗 **AlgoKit**: For localnet and project setup

---

## 🛠️ Project Setup

### Prerequisites

- Python 3.10+
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli)
- Poetry
- Docker (for localnet)

### Setup Steps

```bash
# Clone the repo
git clone https://github.com/GangisettyAkhila/poap_cert.git
cd poap_cert

---

## 🙋‍♀️ Author

👩‍💻 **Akhila Gangisetty**  
Member, Algorand Blockchain Club  
📫 [LinkedIn](https://www.linkedin.com/in/akhila-gangisetty-199a01320/ | [Email](mailto:akhila.gangisetty001@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).


# Start local blockchain network
algokit localnet start

# Deploy smart contracts
algokit project deploy

