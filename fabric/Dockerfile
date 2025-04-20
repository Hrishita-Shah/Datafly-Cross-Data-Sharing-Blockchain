FROM hyperledger/fabric-tools:2.5

WORKDIR /opt/gopath/src/chaincode

# Copy go.mod and go.sum separately for better Docker cache usage
COPY go.mod go.sum ./
RUN go mod tidy

# Copy the rest of the chaincode files
COPY . .
