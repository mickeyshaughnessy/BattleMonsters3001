from utils import execute_completion

from prompts import p_generate_map_seeds

r = execute_completion(p_generate_map_seeds % 100)

with open('generated_map_seeds.txt', 'w') as f:
    f.write(r)

print(r)
