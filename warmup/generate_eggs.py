
from prompts import generate_eggs
from prompts import hatch_egg

from utils import execute_completion

def generate_eggs(N=100):
    with open("projenitor_monsters.json", "r") as fin:
        for line in fin.lines():
            print(line)
    # Create N new egg tokens from Monster parents (Mx, My).
     


def hatch_egg(parent_1_json, parent_2_json):
    # Given an egg token as input, hatch the egg and create the Monster token.
    execute_completion(hatch_egg % Egg)
if __name__ == "__main__":

