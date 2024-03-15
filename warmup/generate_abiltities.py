from prompts import p_generate_abilities
from utils import execute_completion
import json

with open("generated_monsters.json") as monsters_in:
    with open('monsters_abilities.json', 'w') as fout:
        for line in monsters_in:
            line = line.rstrip()
            abilities = execute_completion(p_generate_abilities % line) 
            a = abilities.replace("\n","")
            try:
                m = json.loads(line)
            except Exception as e:
                print("failed to json loads monster", e)
                continue
            try:
                a = json.loads(a)
            except Exception as e:
                print("failed to json loads abilities", e)
                continue
            try:
                m.update(a)
                fout.write(json.dumps(m)+"\n")
            except Exception as e:
                print('failed with writing or update')

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
