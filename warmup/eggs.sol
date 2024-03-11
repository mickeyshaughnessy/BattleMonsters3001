// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Eggs is ERC721URIStorage, Ownable {
    uint public nextTokenId;
    address public monstersAddress;

    constructor() ERC721("Eggs", "EGG") {}

    function mint(address to, string memory uri) public onlyOwner {
        uint tokenId = nextTokenId++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    // Placeholder for hatching functionality
    // function hatch(uint tokenId) public {
    //     require(ownerOf(tokenId) == msg.sender, "You must own the egg to hatch it.");
    //     // Logic to "burn" the egg and create a Monster will go here
    //     // _burn(tokenId);
    //     // Monsters(monstersAddress).mint(msg.sender, newMonsterURI);
    // }

    function setMonstersAddress(address _monstersAddress) public onlyOwner {
        monstersAddress = _monstersAddress;
    }
}
