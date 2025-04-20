#!/bin/bash

set -e

# Step 1: Generate crypto material
cryptogen generate --config=./crypto-config.yaml

# Step 2: Generate genesis block and channel config
export FABRIC_CFG_PATH=$PWD
mkdir -p channel-artifacts
configtxgen -profile TwoOrgsOrdererGenesis -outputBlock ./channel-artifacts/genesis.block
configtxgen -profile TwoOrgsChannel -outputCreateChannelTx ./channel-artifacts/channel.tx -channelID mychannel

# Step 3: Start Fabric network using Docker Compose
docker-compose up -d

# Step 4: Create channel and join peer
docker exec cli peer channel create -o orderer.example.com:7050 -c mychannel \
  -f ./channel-artifacts/channel.tx --outputBlock ./channel-artifacts/mychannel.block \
  --tls --cafile /opt/gopath/src/github.com/chaincode/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem

docker exec cli peer channel join -b ./channel-artifacts/mychannel.block

# Step 5: Install and instantiate chaincode
peer lifecycle chaincode package datafly_cc.tar.gz --path ./chaincode --lang golang --label datafly_cc_1

# NOTE: Package ID will be needed to approve and commit chaincode
echo "Fabric setup complete ✅"
