from prompts import p_generate_abilities
from utils import execute_completion
import json

with open("generated_monsters.json") as monsters_in:
    for line in monsters_in:
        line = line.rstrip()
        abilities = execute_completion(p_generate_abilities % line) 
        print(line)
        print(abilities)
        #input() 

        #with open('generated_abilities.txt', 'w') as fout:
        #    fout.write(abilities)
        #try:
        #    monster = json.loads(line)
        #    ab = json.loads(abilities)
        #    with open('generated_monsters_abilities.json', 'a') as fout:
        #        fout.write(json.dumps(monster.update(ab)))
        #        print('loading json and dumping full monster')
        #except:
        #    print("failed to load json")
