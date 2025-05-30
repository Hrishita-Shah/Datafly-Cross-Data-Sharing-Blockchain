from web3 import Web3
from solcx import compile_source, install_solc
import json

install_solc("0.8.0")

with open("DataFlyContract.sol", "r") as file:
    contract_source = file.read()

compiled_sol = compile_source(contract_source, solc_version="0.8.0")
contract_id, contract_interface = compiled_sol.popitem()

# Connect to Ganache or Geth (adjust as needed)
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
w3.eth.default_account = w3.eth.accounts[0]

DataFly = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Deploy contract
tx_hash = DataFly.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract deployed at:", tx_receipt.contractAddress)
