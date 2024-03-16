// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Monsters is ERC721, Ownable {
    uint256 public nextTokenId;

    constructor() ERC721("Monsters", "MON") {}

    function mint(address to, string memory uri) public onlyOwner {
        _safeMint(to, nextTokenId);
        _setTokenURI(nextTokenId, uri);
        nextTokenId++;
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://...";
    }

    function burnTokenByOwner(uint256 tokenId) public onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _burn(tokenId);
    }
}
