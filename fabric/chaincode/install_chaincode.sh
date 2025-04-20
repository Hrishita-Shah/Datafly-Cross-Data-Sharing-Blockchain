#!/bin/sh
echo Installing chaincode...

#!/bin/bash

export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_ADDRESS=peer0.org1.example.com:7051
export CORE_PEER_MSPCONFIGPATH=/etc/hyperledger/msp/users/Admin@org1.example.com/msp
export CORE_PEER_TLS_ROOTCERT_FILE=/etc/hyperledger/msp/tlsca.org1.example.com-cert.pem

peer lifecycle chaincode package datafly.tar.gz --path /opt/gopath/src/chaincode --lang golang --label datafly_1
peer lifecycle chaincode install datafly.tar.gz

peer lifecycle chaincode approveformyorg --channelID mychannel --name datafly \
  --version 1.0 --package-id <PACKAGE_ID> --sequence 1 --init-required \
  --orderer orderer.example.com:7050 --tls --cafile /etc/hyperledger/msp/ordererCert.pem

peer lifecycle chaincode commit -o orderer.example.com:7050 --channelID mychannel --name datafly \
  --version 1.0 --sequence 1 --init-required \
  --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /etc/hyperledger/msp/tlsca.org1.example.com-cert.pem

peer chaincode invoke -o orderer.example.com:7050 --isInit -C mychannel -n datafly \
  -c '{"Args":["Init"]}' --tls --cafile /etc/hyperledger/msp/ordererCert.pem
