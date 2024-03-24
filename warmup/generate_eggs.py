from prompts import p_generate_eggs
from utils import execute_completion
import json, random


def generate_eggs(N=100):
    eggs = []
    with open("generated_monsters.json", "r") as fin:
        monsters = [line.rstrip() for line in fin]
        
    for i in range(N):
        parent_1 = random.choice(monsters)
        parent_2 = random.choice(monsters)
        
        egg = execute_completion(p_generate_eggs % (parent_1, parent_2)) 
        eggs.append(egg)
        print(egg)
    
    return eggs
    

if __name__ == "__main__":
    eggs = generate_eggs(N=100)
    print("Generated %s eggs" % len(eggs))
    with open("generated_eggs.json", "w") as fout:
        for egg in eggs:
            fout.write(egg + "\n")
