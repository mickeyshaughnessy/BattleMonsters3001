// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Monsters is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;

    constructor() ERC721("Monsters", "MON") Ownable(msg.sender) {}

    function mint(address to, string memory uri) public onlyOwner {
        _safeMint(to, nextTokenId);
        _setTokenURI(nextTokenId, uri);
        nextTokenId++;
    }

    function burnTokenByOwner(uint256 tokenId) public onlyOwner {
        // ownerOf will revert if the token does not exist, so no need for _exists
        _burn(tokenId);
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://...";
    }
}

