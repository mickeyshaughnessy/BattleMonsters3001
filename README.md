# BattleMonsters3001

_This is a collectible Monster Egg hatching game_ 

The `warmup` directory contains a few warmup scripts.

The `build.sh` builds the entire token economy and private game assets.

`contracts/` directory contains Solidity smart contracts.

The game is organized around a game server. 

The game server runs game worker processes, and exposes an API for game clients. 

# Eggs (MEGG)
![image](https://github.com/mickeyshaughnessy/BattleMonsters3001/assets/1209295/9fb9dac7-53fb-4732-a31d-b1a57465f600)
Eggs hatch into Monsters - this is represented by an Egg token generating a new Monster token and then being burned.

New players begin the game with 4 Eggs and one Monster.

Eggs can be traded on the Lakewood Egg Exchange for MBUCK$$$.

# Monsters (MONST)
Monster tokens hatch from Eggs and can be used to:
 * fight in Battles or 
 * occupy one of the 4 stalls in the player's Breeding Pen

Monsters can not be traded, they can be upgraded. 
![image](https://github.com/mickeyshaughnessy/BattleMonsters3001/assets/1209295/5ca75b16-de81-4a63-a416-7614b7454e8b)

## Battles
![image](https://github.com/mickeyshaughnessy/BattleMonsters3001/assets/1209295/86b16072-3ce8-4df0-a2ec-bacb9b4e3d7a)

Monsters can be deployed to and removed from Battles. 
In battle, monsters can both lose hit points and extract resources (MonsterBucks).
When a monster's hit point become zero or less, the monster is removed from the battle and the monster dies. 


## Breeding Pen
![image](https://github.com/mickeyshaughnessy/BattleMonsters3001/assets/1209295/464b6725-9c1f-4d55-ade7-901cfc3c8b3e)
Up to 4 monsters can occupy a player's Breeding Pen.
When 2 or more monsters are in a breeding pen, a new Egg may be generated. 
Each Egg has an egg_id as well as the monster_ids of the parents.

# MonsterBucks (MBUCK$$$)
![image](https://github.com/mickeyshaughnessy/BattleMonsters3001/assets/1209295/c266733a-90bb-4b43-aca6-dabce6ca34d9)
