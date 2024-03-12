// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Monsters is ERC721URIStorage, Ownable {
    uint public nextTokenId;

    constructor() ERC721("Monsters", "MONST") {}

    function mint(address to, string memory uri) public onlyOwner {
        uint tokenId = nextTokenId++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    // Additional functionality for Monsters can be added here
}

