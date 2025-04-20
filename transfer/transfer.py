import json
import requests

with open('../shared/data/extracted_payload.json') as f:
    payload = json.load(f)

# Upload to IPFS (if needed)
ipfs_res = requests.post(
    "http://localhost:5001/api/v0/add",
    files={"file": json.dumps(payload)}
)
print("Uploaded to IPFS:", ipfs_res.text)
