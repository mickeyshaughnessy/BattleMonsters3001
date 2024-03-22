from prompts import p_generate_eggs
from prompts import p_hatch_egg
from utils import execute_completion
import json

def generate_eggs(N=100):
    eggs = []
    with open("projenitor_monsters.json", "r") as fin:
        monsters = [json.loads(line) for line in fin]
        
    for i in range(N):
        parent_1 = random.choice(monsters)
        parent_2 = random.choice(monsters)
        
        egg_data = {
            "parent_1": parent_1,
            "parent_2": parent_2,
            "egg_id": str(uuid.uuid4())
        }
        
        egg_token = execute_completion(generate_eggs % json.dumps(egg_data))
        eggs.append(json.loads(egg_token))
    
    with open("generated_eggs.json", "w") as fout:
        for egg in eggs:
            fout.write(json.dumps(egg) + "\n")
    
    return eggs

def hatch_egg(egg_token):
    # Given an egg token as input, hatch the egg and create the Monster token.
    monster = execute_completion(hatch_egg % egg_token)
    return json.loads(monster)

if __name__ == "__main__":
    eggs = generate_eggs(N=100)
    print(f"Generated {len(eggs)} eggs.")
    
    # Hatch an egg as an example
    egg_token = json.dumps(eggs[0])
    monster = hatch_egg(egg_token)
    print("Hatched monster:")
    print(monster)
