from prompts import p_generate_monster, p_make_seeds

import requests
import json

from utils import execute_completion

NSEEDS = 200

if __name__ == "__main__":
    _text = execute_completion(p_make_seeds % NSEEDS)
    with open("generated_seeds.txt", 'w') as f:
        f.write(_text)

    print(_text)

    with open("generated_monsters.txt", 'w') as f:
        with open("generated_monsters.json", 'w') as fout:
            lines = _text.split("\n")
            for line in lines:
                monster = execute_completion(p_generate_monster % line)
                m = monster.replace("\n", "")
                print(monster)
                try:
                    f.write(monster+"\n")
                    json.loads(monster)
                    fout.write(m + "\n")
                except:
                    print("failed json loads")
