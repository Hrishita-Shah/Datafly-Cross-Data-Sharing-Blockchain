import json
import subprocess

with open('/app/shared/data/extracted_payload.json') as f:
    payload = json.load(f)

key = payload.get("tx_hash", "default_key")
value = json.dumps(payload)

# Prepare invoke command
cmd = [
    "peer", "chaincode", "invoke",
    "-o", "orderer.example.com:7050",
    "--tls", "--cafile", "/etc/hyperledger/msp/ordererCert.pem",
    "-C", "mychannel", "-n", "datafly",
    "-c", f'{{"Args":["storeData", "{key}", \'{value}\']}}'
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
