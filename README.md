# Datafly-Protocol-Cross-Data-Sharing-Blockchain

DataFly is a cross-chain data migration protocol enabling secure, confidential transfer of data from Ethereum to Hyperledger Fabric using IPFS and a Flask-based messaging service. It follows an ETL (Extract, Transfer, Load) pipeline that abstracts the heterogeneity between public and permissioned blockchains.

---

## 🚀 Architecture Overview

```
Ethereum → Extract → IPFS + Messaging → Load → Fabric
```

🟢 Ethereum (Ganache) →  
📆 extract_eth.py (Python) →  
⮍ IPFS (Data payload) + Messaging Service (Signals & Metadata) →  
📆 load_fabric.py (Python) →  
🪠 Hyperledger Fabric (Chaincode)

---

## 📁 Project Structure

datafly-protocol/
├── ethereum/  
│   ├── Dockerfile  
│   ├── genesis.json  
│   ├── geth_setup.sh  
│   └── contracts/  
│       ├── DataFlyContract.sol  
│       └── deploy_contract.py  
├── fabric/  
│   ├── Dockerfile  
│   ├── configtx.yaml  
│   ├── crypto-config.yaml  
│   └── chaincode/  
│       ├── datafly_cc.go  
│       ├── install_chaincode.sh  
│       └── start_fabrics.sh  
├── shared/  
│   ├── ipfs/  
│   │   └── docker-compose.yml  
│   ├── messaging/  
│   │   ├── app.py  
│   │   └── Dockerfile  
│   └── data/  
│       └── extracted_payload.json  
├── extract/  
│   └── extract_eth.py  
├── transfer/  
│   ├── transfer.py  
│   └── Dockerfile  
├── load/  
│   └── Dockerfile  
├── load_fabric.py  
├── docker-compose.yml  
└── README.md

---

## 🔧 Prerequisites

- Docker & Docker Compose
- Git

Optional (for development):
- Python 3.10+
- Node.js & Truffle (for contract development)
- Go (for chaincode)

---

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/datafly-protocol.git
cd datafly-protocol
```

2. Build and run all services:

```bash
docker-compose up --build
```

3. This will spin up:

- Ethereum node (Ganache)
- Hyperledger Fabric network
- IPFS node
- Flask messaging server
- Extract, Transfer, and Load ETL stages

---

## 🪩 Components

### 1️⃣ Ethereum (Ganache) — ./ethereum

- Smart contract: DataFlyContract.sol
- Deployment: deploy_contract.py
- Genesis config: genesis.json
- Setup: geth_setup.sh

### 2️⃣ Fabric — ./fabric

- Chaincode: datafly_cc.go
- Configuration: configtx.yaml, crypto-config.yaml
- Fabric launcher: start_fabrics.sh
- Chaincode installer: install_chaincode.sh

### 3️⃣ IPFS — ./shared/ipfs

- Lightweight node using go-ipfs image
- Used to store extracted JSON payloads from Ethereum

### 4️⃣ Messaging — ./shared/messaging

- Flask server (app.py)
- Used to signal metadata and transaction info between Extract & Load stages

### 5️⃣ Extract — ./extract/extract_eth.py

- Connects to Ethereum node via Web3
- Fetches and processes smart contract events
- Stores output in shared/data/extracted_payload.json

### 6️⃣ Transfer — ./transfer/transfer.py

- Publishes extracted data to IPFS
- Sends IPFS hash to messaging server

### 7️⃣ Load — ./load/load_fabric.py

- Consumes IPFS hash and metadata
- Writes validated payload into Fabric ledger via chaincode

---

## 📦 Example Workflow

1. Contract on Ethereum logs an event  
2. extract_eth.py fetches event and writes to JSON  
3. transfer.py uploads to IPFS, sends hash to messaging  
4. load_fabric.py fetches from IPFS and invokes Fabric chaincode

---

## 📸 Sample Output

- extract_eth.py → shared/data/extracted_payload.json:

```json
{
  "txHash": "0xabc123...",
  "data": {
    "field1": "value",
    "timestamp": "2025-04-20T12:00:00"
  }
}
```

---

## 🧚‍♂️ Testing & Debugging

- To test individual services, you can run them standalone via:

```bash
docker-compose run extract
docker-compose run transfer
docker-compose run load
```

- Logs for Flask:

```bash
docker logs datafly-protocol-messaging-1
```

---

## 🧱 Technologies Used

- Ethereum (Ganache, Solidity)
- Hyperledger Fabric (Go Chaincode)
- Python (Web3, Flask, IPFS Client)
- Docker & Docker Compose
- IPFS

---

## 📚 References

- Ethereum Smart Contracts: https://soliditylang.org  
- Hyperledger Fabric Docs: https://hyperledger-fabric.readthedocs.io  
- IPFS API: https://docs.ipfs.io/reference/http/api/  
- Docker Compose: https://docs.docker.com/compose/

---

## 🤝 Contributors

- Hrishita Shah – @yourusername  
- Project Mentors – Prasun, Lalithya, Hari, Swamy

---

## 🚲 License

MIT License. See LICENSE file for details.

