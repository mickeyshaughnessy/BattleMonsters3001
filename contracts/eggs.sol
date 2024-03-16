// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IMonsters {
    function mint(address to, string memory uri) external;
}

contract Eggs is ERC721URIStorage, Ownable, ReentrancyGuard {
    uint public nextTokenId;
    address public monstersAddress;
    address public monsterBucksAddress;

    struct Order {
        bool isBuyOrder;
        uint tokenId;
        uint monsterBucksAmount;
        address maker;
    }

    mapping(uint => Order) public orders;
    uint public nextOrderId;

    event Minted(address to, uint tokenId, string uri);
    event Hatched(uint tokenId, address owner, string newMonsterURI);
    event OrderPlaced(uint orderId, bool isBuyOrder, uint tokenId, uint monsterBucksAmount, address maker);
    event OrderCancelled(uint orderId);

    constructor() ERC721("Eggs", "EGG") {}

    function mint(address to, string memory uri) public onlyOwner {
        uint tokenId = nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        emit Minted(to, tokenId, uri);
    }

    function hatch(uint tokenId, string memory newMonsterURI) public onlyOwner nonReentrant {
        require(_exists(tokenId), "Egg does not exist.");
        address owner = ownerOf(tokenId);
        _burn(tokenId);
        IMonsters(monstersAddress).mint(owner, newMonsterURI);
        emit Hatched(tokenId, owner, newMonsterURI);
    }

    function placeLimitOrder(bool isBuyOrder, uint tokenId, uint monsterBucksAmount) public nonReentrant {
        require(_exists(tokenId), "Egg does not exist.");
        if (isBuyOrder) {
            require(IERC20(monsterBucksAddress).transferFrom(msg.sender, address(this), monsterBucksAmount), "MonsterBucks transfer failed.");
        } else {
            require(ownerOf(tokenId) == msg.sender, "You are not the owner of this Egg.");
        }
        orders[nextOrderId] = Order(isBuyOrder, tokenId, monsterBucksAmount, msg.sender);
        emit OrderPlaced(nextOrderId, isBuyOrder, tokenId, monsterBucksAmount, msg.sender);
        nextOrderId++;
    }

    function cancelOrder(uint orderId) public nonReentrant {
        require(orders[orderId].maker == msg.sender, "You are not the maker of this order.");
        if (orders[orderId].isBuyOrder) {
            IERC20(monsterBucksAddress).transfer(msg.sender, orders[orderId].monsterBucksAmount);
        }
        delete orders[orderId];
        emit OrderCancelled(orderId);
    }
}
