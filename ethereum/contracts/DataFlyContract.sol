// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataFlyContract {
    string public data;

    function storeData(string memory _data) public {
        data = _data;
    }

    function retrieveData() public view returns (string memory) {
        return data;
    }
}
