// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IMonsters {
    function mint(address to, string memory uri) external;
}

contract MonsterEggs is ERC721URIStorage, Ownable, ReentrancyGuard {
    uint public nextTokenId;
    address public monstersAddress;

    event Minted(address to, uint tokenId, string uri);
    event Hatched(uint tokenId, address owner, string newMonsterURI);

    constructor() ERC721("MonsterEggs", "MEGG") {}

    function mint(address to, string memory uri) public onlyOwner {
        uint tokenId = nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        emit Minted(to, tokenId, uri);
    }

    function hatch(uint tokenId, string memory newMonsterURI) public onlyOwner nonReentrant {
        require(_exists(tokenId), "MonsterEgg does not exist.");
        address owner = ownerOf(tokenId);
        _burn(tokenId);
        IMonsters(monstersAddress).mint(owner, newMonsterURI);
        emit Hatched(tokenId, owner, newMonsterURI);
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://your-base-uri/";
    }
}
