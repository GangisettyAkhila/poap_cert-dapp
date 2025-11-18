# 🎟️ POAP Certificate DApp on Algorand

This is a **Proof of Attendance Protocol (POAP)** smart contract DApp built on the **Algorand blockchain**. It allows organizers to issue **verifiable certificates or badges** to participants of events (workshops, hackathons, meetups, etc.) using **Algorand smart contracts**.

---

## 🚀 Features

- ✅ Mint on-chain POAP certificates for event attendees
- ✅ Issue, revoke, and query certificates programmatically
- ✅ Certificates are **tamper-proof**, **verifiable**, and **permanent**
- ✅ Issued using **Algorand smart contracts** (Algopy)
- ✅ Fully programmable via Python scripts (issue, revoke, verify)

---

## 🧠 Use Case

Most college events and workshops still hand out PDF certificates, which can be faked, misplaced, or impossible to verify. This DApp fixes that by issuing on-chain proof-of-attendance certificates that anyone can view, validate, and trust directly through the smart contract.

---

## ⚙️ Tech Stack

- 🧠 **Smart Contracts**: Algopy (Algorand Python)
- 🌐 **Frontend**: React / HTML+JS
- 🔗 **AlgoKit**: For localnet setup and deployment
- 🐍 **Python**: For scripts to issue, revoke, and verify certificates

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

# Start local blockchain network
algokit localnet start

# Deploy smart contracts
algokit project deploy
```
