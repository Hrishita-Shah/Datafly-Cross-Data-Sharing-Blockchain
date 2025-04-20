package main

import (
	"fmt"
	"github.com/hyperledger/fabric-chaincode-go/shim"
	pb "github.com/hyperledger/fabric-protos-go/peer"
)

type DataFlyChaincode struct{}

// Init is called during chaincode instantiation to initialize any data.
func (t *DataFlyChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("Chaincode initialization successful")
	return shim.Success(nil)
}

// Invoke is called per transaction on the chaincode.
func (t *DataFlyChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	function, args := stub.GetFunctionAndParameters()
	fmt.Printf("Invoke called - Function: %s, Args: %v\n", function, args)

	switch function {
	case "storeData":
		return t.storeData(stub, args)
	case "queryData":
		return t.queryData(stub, args)
	default:
		return shim.Error("Invalid invoke function name. Expecting \"storeData\" or \"queryData\"")
	}
}

// storeData stores a key-value pair in the ledger
func (t *DataFlyChaincode) storeData(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	if len(args) != 2 {
		return shim.Error("Expecting 2 arguments: key and value")
	}

	key := args[0]
	value := args[1]

	fmt.Printf("Storing data - Key: %s, Value: %s\n", key, value)

	if err := stub.PutState(key, []byte(value)); err != nil {
		return shim.Error("Failed to store data: " + err.Error())
	}

	return shim.Success(nil)
}

// queryData retrieves the value for a given key from the ledger
func (t *DataFlyChaincode) queryData(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	if len(args) != 1 {
		return shim.Error("Expecting 1 argument: key")
	}

	key := args[0]
	fmt.Printf("Querying data - Key: %s\n", key)

	value, err := stub.GetState(key)
	if err != nil {
		return shim.Error("Failed to get data: " + err.Error())
	}
	if value == nil {
		return shim.Error("No data found for key: " + key)
	}

	return shim.Success(value)
}

func main() {
	err := shim.Start(new(DataFlyChaincode))
	if err != nil {
		fmt.Printf("Error starting DataFlyChaincode: %s\n", err)
	}
}
