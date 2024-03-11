// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract Maps is Ownable {
    // Map id to Monster ids present on that Map
    mapping(uint => uint[]) private mapToMonsters;
    // Monster id to its current Map id
    mapping(uint => uint) private monsterToMap;
    // Map links
    mapping(uint => uint[]) private mapLinks;
    // Reference to the Monsters contract
    IERC721 public monstersContract;

    constructor(address _monstersContractAddress) {
        monstersContract = IERC721(_monstersContractAddress);
    }

    function addMonsterToMap(uint monsterId, uint mapId) public {
        require(monstersContract.ownerOf(monsterId) == msg.sender, "You must own the monster to move it.");
        require(monsterToMap[monsterId] != mapId, "Monster is already on this map.");
        // Remove from the current Map if it's on one
        if (monsterToMap[monsterId] != 0) {
            removeMonsterFromMap(monsterId, monsterToMap[monsterId]);
        }
        mapToMonsters[mapId].push(monsterId);
        monsterToMap[monsterId] = mapId;
    }

    function removeMonsterFromMap(uint monsterId, uint mapId) public {
        require(monstersContract.ownerOf(monsterId) == msg.sender, "You must own the monster to move it.");
        require(monsterToMap[monsterId] == mapId, "Monster is not on this map.");
        int index = _findMonsterIndexInMap(monsterId, mapId);
        if (index >= 0) {
            _removeAtIndex(mapToMonsters[mapId], uint(index));
            monsterToMap[monsterId] = 0; // Indicate the monster is not on any map
        }
    }

    function linkMaps(uint fromMapId, uint toMapId) public onlyOwner {
        mapLinks[fromMapId].push(toMapId);
    }

    function unlinkMaps(uint fromMapId, uint toMapId) public onlyOwner {
        int index = _findMapIndexInLinks(toMapId, fromMapId);
        if (index >= 0) {
            _removeAtIndex(mapLinks[fromMapId], uint(index));
        }
    }

    function _findMonsterIndexInMap(uint monsterId, uint mapId) private view returns (int) {
        for (uint i = 0; i < mapToMonsters[mapId].length; i++) {
            if (mapToMonsters[mapId][i] == monsterId) {
                return int(i);
            }
        }
        return -1; // Not found
    }

    function _findMapIndexInLinks(uint toMapId, uint fromMapId) private view returns (int) {
        for (uint i = 0; i < mapLinks[fromMapId].length; i++) {
            if (mapLinks[fromMapId][i] == toMapId) {
                return int(i);
            }
        }
        return -1; // Not found
    }

    function _removeAtIndex(uint[] storage array, uint index) private {
        require(index < array.length, "Index out of bounds.");
        array[index] = array[array.length - 1];
        array.pop();
    }

    // Additional functionalities to support monster movements between linked maps
    // could be implemented here, taking into account mapLinks for allowed movements.
}

