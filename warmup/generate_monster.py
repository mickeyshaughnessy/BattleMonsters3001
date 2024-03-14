from prompts import generate_monster, make_seeds

import requests
import json

from utils import execute_completion

if __name__ == "__main__":
    _text = execute_completion(make_seeds % 100)
    with open("generated_seeds.txt", 'w') as f:
        f.write(_text)

    print(_text)

    with open("generated_monsters.txt", 'w') as f:
        lines = _text.split("\n")
        for line in lines:
            monster = execute_completion(generate_monster % line)
            monster.replace("\n", "")
            print(monster)
            try:
                f.write(monster)
                json.loads(monster)
            except:
                print("failed json loads")
            f.write("\n")
