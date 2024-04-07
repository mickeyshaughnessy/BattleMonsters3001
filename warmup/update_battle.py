# This script takes a Map JSON plus Monsters JSON objects and generates and update JSON output

from prompt import p_update_battle


monsters, maps, battles = [], [], []
with open("generated_monsters.txt", 'r') as m_in:
    for line in m_in:
        monsters.append(line.rstrip())
with open("generated_maps.txt", 'r') as m_in:
    for line in m_in:
        maps.append(line.rstrip())

for _map in maps:
    n_monsters = random.choice([2,3,4,5,6])
    chosen = [random.choice(monsters) for i in range(n_monsters)]
    battles.append({"map" : _map, "monsters" : chosen}) 


for b in battles:
    _map = b.get('map')
    monsters = b.get('monsters')
    monsters = str(monsters) 
    
    res = execute_completion(p_update_battle % (_map, monsters))
    # store result, update monsters, battle, players, etc
    print("############### BATTLE #########")
    print(_map)
    print(monsters)
    print(res)
