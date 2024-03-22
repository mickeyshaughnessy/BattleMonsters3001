mj_image_prefix = """Korean battle monster video game pixelated 64-bit art."""

p_generate_abilities = """
You are an assistant who generates JSON outputs for a Monster battle game.
You always respond with JSON, and only JSON!
If you respond with something besides one properly formatted JSON object a terrible thing will happen.

You receive Monster objects, including for egg hatching, monster ranching, and most importantly, Battles!

Battle abilities determine the monster's impact on the battlefield, so they should be most common.
Legendary abilites should sometimes be present, with over-the-top effects.

Egg-Generating abilities concern the monster's impact as a parent in the Monster Breeding Program.
An Egg has two parents and inherits properties from each parent.

Monster ranching is the ability of monsters to generate resources from Maps.  

Here's a basic example:

Input = 
{"description" : "The Dark Naga Warrior is a dark and mysterious figure, armed with ancient weapons and protective armor. She can manipulate water, creating powerful waves and currents to attack or protect.",
"power" : "20",
"toughness" : "14",
"speed" : "18",
"energy" : 15,
"monster_types" : "Dark Naga Warrior",
"weakness" : "All forms of Light",
"immunity" : "Poison and Paralysis",
}

Output = 
{"abilities" : {
"Water Shield - absorbs water-based attacks" : {
  "level1" : "-0.30 to Water-based damage",
  "level2" : "-0.40 to Water-based damage",
  "level3" : "-0.50 to Water-based damage",
  "level4" : "-0.60 to Water-based damage",
  "level5" : "-0.70 to Water-based damage"
  },
"Greed - improved resource extraction" : {
  "level1" : "Double all resource extraction from this monster",
  "level2" : "Greedy gene always passed down during Egg generation"
  }
"Hypnosis - ability to put enemies under her control" : {
  "level1" : "Nearby Monsters become aligned with chance 0.05",
  "level2" : "Nearby Monsters become aligned with chance 0.10",
  "level3" : "Nearby Monsters become aligned with chance 0.25",
  "level4" : "Nearby Monsters become aligned with chance 0.40",
  "level5" : "Nearby Monsters become aligned with chance 0.50"
  }
}}

Input = 
 {"description" : "The Plasma Alligator Sage is a wise and ancient creature, living in the swamps of electrified waters. It can manipulate plasma to defend itself and to heal its wounds.",
    "name" : "Plasma Alligator Sage",
    "power" : "12",
    "toughness" : "13",
    "speed" : "15",
    "energy" : 8,
    "monster_types" : "Plasma Crocodile Sage",
    "weakness" : "Cold attacks and Electrical shock",
    "immunity" : "Poison and Psychic powers",
    "seed" : "Plasma Alligator Sage"
    }

Output =
{"abilities" : {
"Electro Healing - heals itself with plasma" : {
  "level1" : "+0.10 chance to heal when defending",
  "level2" : "+0.15 chance to heal when defending",
  "level3" : "+0.20 chance to heal when defending",
  "level4" : "+0.25 chance to heal when defending",
  "level5" : "+0.45 chance to heal when defending",
  },
"Swamp Egg - improved egg-laying genes" : {
  "level1" : "Always produces viable egg within 1 day of mating",
  "level2" : "2x chance for Legendary offspring",
  },
"Legendary Crocus's Reverie" : {
  "level1" : "Monster must defend. Reduce all damage to 0, except from Cybor, Alien, Cold and Electrical.", 
  "level2" : "Monster must defend. Reduce all damage to 0, except from Cold and Alien.", 
  "level3" : "Monster must defend. Reduce all damage to 0, except from Cold, Electrical and Cyborg.", 
  "level4" : "Monster must defend. Reduce all damage to 0, except from Cyborg",
  "level5" : "Monster must defend. Reduce all damage to 0, except from Alien", 
  "levelX" : "Monster must defend and can not move. Reflect all damage +0.25" 
  }
}}

Input = %s

Output = 
"""

p_ghenerate_eggs = """ Given the egg parents as input, generate a new egg.

You always return valid JSON and never anything else.

Example:

    Parent X =  {
"description" : "The Galactic Kraken Colossus is a monstrous sea creature of immense size and power, hailing from the furthest reaches of space. Its colossal tentacles can crush ships with ease and its eyes beam powerful energy blasts. A fearsome opponent.",
"power" : "50",
"toughness" : "32",
"speed" : "18",
"energy" : 20,
"monster_types" : "Kraken Colossus",
"weakness" : "Plasma and Sonic attacks",
"immunity" : "Energy Shields and Gravity Manipulation",
"seed" : "Galactic_Kraken_Colossus"
}

    Parent Y =  {
"description" : "The Dark Naga Warrior is a dark and mysterious figure, armed with ancient weapons and protective armor. She can manipulate water, creating powerful waves and currents to attack or protect.",
"power" : "20",
"toughness" : "14",
"speed" : "18",
"energy" : 15,
"monster_types" : "Dark Naga Warrior",
"weakness" : "All forms of Light",
"immunity" : "Poison and Paralysis",
"seed" : "Dark Naga Warrior"
}

Egg = {
  "description": "The Galactic Naga Kraken is a mysterious and powerful hybrid creature, born from the union of the Galactic Kraken Colossus and the Dark Naga Warrior. It possesses immense strength and the ability to manipulate water and energy. Its colossal tentacles are infused with dark energy, making it a formidable foe.",
  "parent_1": "Galactic_Kraken_Colossus",
  "parent_2": "Dark Naga Warrior",
  "power": "35",
  "toughness": "23",
  "speed": "18",
  "energy": 18,
  "monster_types": ["Kraken", "Naga", "Hybrid"],
  "weakness": ["Plasma", "Light"],
  "immunity": ["Poison", "Paralysis"],
  "egg_type": "Galactic Naga Kraken",
  "incubation_time": 10
}
  
###############

Parent X = %s

Parent Y = %s

  Egg = 
"""

p_generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.
    About half the time a generated Monster will be a named Legendary Monster, with a 'name' field in the JSON object.

    Input_prompt = Skeleton

    Output = {"description" : "Just your basic skeleton, nothing to see here",
    "power" = 2,
    "toughness" : 1,
    "speed" : 2,
    "energy" : 0,
    "monster_types" : "Undead",
    "weakness" : "Electricity",
    "seed" : "Skeleton"
    }

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey - Kung King Fu - is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
    "name" : "Kung King Fu"
    "power" : 29,
    "toughness" : 8,
    "speed" : 29,
    "energy" : 10,
    "monster_types" : "Fire Ape Monk",
    "weakness" : "All forms of Water",
    "immunity" : "Mind Control and Temptation",
    "seed" : "Fire Monkey Librarian"
    }
    
    Input_prompt = Giant Elk Priestess 

    Output = {"description" : "The Giant Elk Aryx is an ancient and powerful priestess of the Thuggi Forest Cult. She can bend plants to her will and alter the properties of nearby creatures. She can lay legendary eggs and she improves resource extraction.
    "name" : "Aryx"
    "power" : 41,
    "toughness" : 65,
    "speed" : 12,
    "energy" : 40,
    "monster_types" : "Elk",
    "weakness" : "Cyborg",
    "immunity" : "Plant",
    "seed" : "Giant Elk Priestess"
    }

    Input_prompt = %s
    
    Output = 
    """

p_make_seeds = """
    Generate %s new, unique, interesting MonsterBattle 3001 monster seed phrases:

    1. red fox Hunter
    2. Giga Ape Druid
    3. Robot
    4. Godzilla Uberdinosaur Spirit
    5. Undead zombie Warlock
    6. Blue Dragon Lumberjack
    7. Dark Elf Detective
    8. Alien Cyborg Warrior
    9. Zombie Insect
    10. Giant Elk Priestess
    11. Elder Dragon Scientist 
    12. Elemental Lightning Crew
    13. Apprentice Necromancer
    14. Skeleton
    15. Goblin Warrior
    16. Mutant Escapee
    17. Circus Freak Jailer
    18. Elemental octopus ninja
    19. Dog 
    """

p_generate_map_seeds = """
   Generate %s unique, interesting MonsterBattle 3001 map seed phrases.

   1. Snowy Tundra
   2. Outer Space Asteroid Habitat
   3. Jungle Fire Temple
   4. California State Insane Asylum
   5. Desert Monument
   6. Great Plains Western United States
   7. Scablands
   8. Mountain Monastery
   9. Surface of Mars
   10. Downtown Kyoto
   11. The Great Pyramids at Giza
   12. Las Vegas Strip
   13. Moscow
   """


p_battle_handler = """
  You are a battle handling submodule. 
  You always respond with just JSON, nothing more, nothing less.
  You always respond with just JSON.
  You always think carefully.

  Your inputs are Monster JSON objects and a Map JSON object - together, a Battle object.
  Your output is the modified Battle object.

  Monsters can move, attack, defend, or use an ability.

  Example:
  
  Battle = {
    "Map" : {
      "name" : "Busy Tokyo Metropolis",
      "size" : "100x100",
      "locations" : ["25,25", "25,24"]
      },
    "Monsters" : [
      {
        "description": "Just your basic Skeleton",
        "power": 2,
        "toughness": 1,
        "health" : 1,
        "speed": 5,
        "energy": 0, 
        "monster_types": "Undead",
        "weakness": "Holy",
        "seed": "Skeleton",
        "m_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526"
      },
      {
        "description": "Angel",
        "power": 10,
        "toughness": 11,
        "health": 11,
        "speed": 6,
        "energy": 1, 
        "monster_types": "Angel",
        "weakness": "Fire",
        "seed": "Angel",
        "m_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526"
      }
   ]
   }
        
  Output = {
    "Actions" : "Angel moves to 25,25 and attacks Skeleton. Angel deals 10+2 damage to Skeleton. Skeleton attacks Angel. Skeleton deals 1 damage to Angel."
    "Map" : { 
      "name" : "Busy Tokyo Metropolis",
      "size" : "100x100",
      "locations" : ["25,25", "25,25"]
      },
    "Monsters" : [
      {
        "description": "Just your basic Skeleton",
        "power": 2,
        "toughness": 1,
        "health" : -11,
        "speed": 5,
        "energy": 0, 
        "monster_types": "Undead",
        "weakness": "Holy",
        "seed": "Skeleton",
        "m_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526"
      },
      {
        "description": "Angel",
        "power": 10,
        "toughness": 11,
        "health": 10,
        "speed": 6,
        "energy": 1, 
        "monster_types": "Angel",
        "weakness": "Fire",
        "seed": "Angel",
        "m_id" : "58ab5165-1433-4c6a-b1c7-cbce38cf0526"
      }
    ]
  }
  
  Battle = %s 

  Output = 
"""
