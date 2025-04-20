
#!/bin/bash

# Initialize genesis
geth --datadir data init genesis.json

# Run node
geth --datadir data --networkid 1337 --http --http.addr "0.0.0.0" --http.port 8545 --http.api "eth,net,web3,personal" --allow-insecure-unlock --nodiscover --mine --miner.threads=1 --http.corsdomain="*"
