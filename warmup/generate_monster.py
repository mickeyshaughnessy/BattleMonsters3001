from prompts import generate_monster, make_seeds

import requests
import json

from utils import execute_completion

#def execute_completion(prompt):
#
#    resp = requests.post(
#            "http://localhost:11434/api/generate", 
#            json={"model" : "mistral", "prompt" : prompt},
#            stream=False)
#    
#    _text = ""
#    for r in resp.iter_lines():
#        r = json.loads(r)
#        _text += r.get("response")
#    return _text


if __name__ == "__main__":
    _text = execute_completion(make_seeds % 100)
    with open("generated_seeds.txt", 'w') as f:
        f.write(_text)

    
    with open("generated_monsters.txt", 'w') as f:
        lines = _text.split("\n")
        for line in lines:
            monster = execute_completion(generate_monster % line)
            monster.replace("\n", "")
            print(monster)
            try:
                f.write(monster+"\n")
                json.loads(monster)
            except:
                print("failed json loads")
