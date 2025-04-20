# Extract Ethereum data to JSON
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://ethereum:8545"))

contract_address = '0x...'  # Replace with actual
abi = [...]  # Load ABI

contract = w3.eth.contract(address=contract_address, abi=abi)
payload_hash = contract.functions.getPayloadHash().call()

data = {"hash": payload_hash}
with open("shared/data/extracted_payload.json", "w") as f:
    json.dump(data, f)
