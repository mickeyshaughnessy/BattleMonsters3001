# This script takes a Map JSON plus Monsters JSON objects and generates and update JSON output
import random, json
from prompts import p_update_battle
from utils import execute_completion

monsters, maps, battles = [], [], []
with open("generated_monsters.txt", 'r') as m_in:
    for line in m_in:
        monsters.append(line.rstrip())
with open("generated_map_seeds.txt", 'r') as m_in:
    for line in m_in:
        maps.append(line.rstrip())

for _map in maps:
    n_monsters = random.choice([2,3])
    chosen = [random.choice(monsters) for i in range(n_monsters)]
    battles.append({"map" : _map, "monsters" : str(chosen)}) 

for b in battles:
    res = execute_completion(p_update_battle % (b))
    # store result, update monsters, battle, players, etc
    print("battle", b)
    print("########## BATTLE UPDATE #########")
    print(res)
    try:
        json.loads(res)
    except:
        print("failed to load")
