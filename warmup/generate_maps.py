from utils import execute_completion

from prompts import p_generate_map_seeds

r = execute_completion(p_generate_map_seeds % 10)

with open('generated_map_seeds.txt', 'w') as f:
    f.write(r)

print("Generated Seeds: %s " % r)

print('generating maps')

with open('generated_maps.txt', 'w') as fout:
    for line in r.split('. '):
        res = execute_completion(
          """
         You are a map-generating submodule in an large language model AI game.
         You always respond with JSON and never anything else.
         Give a map seed, you return subtly humorous and concise Map description JSON bodies
          
         Example 1 :
         ##################
    
         input = "Volcanic Island of Fire Giants/n 59. "
    
         output = {
         "seed" : Volcanic Island of Fire Giants,
         "description" : "Hidden in the arctic archipelago of the Fire Giants, the volcano erupts day and night. A Norse fish cannery operates on the shore and pays a hefty yearly tithe to the Fire Giant King, Magmos. Monsters may encounter Magmos, monsters may not survice Magmos. They may also encounter angry Norse fisherman. The volcano will erupt."
    
         "advantage" : ["Fire", "Magma", "Giant"],
         "map_shape" : "Island",
         "resources" : {
           "Rate" : "Legendary",
           "Types" :["Seafood", "Gems", "Geothermal Treasure"]
           }
         "size_x" : 100,
         "size_y" : 100,
         } 
         #####################
    
         input = %s
    
         output = 
         """ % line)
        fout.write(res)
        print(res)
