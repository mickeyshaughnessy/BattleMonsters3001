image_prefix = """Korean battle monster video game pixelated 64-bit """

generate_abilities = """
You are an assistant who generates JSON outputs for a Monster battle game.
You receive Monster objects and output potential abilities, including for egg hatching, monster ranching, and most importantly, Battles!

Battle abilities determine the monster's impact on the battlefield, so they should be most common. Legendary abilites should sometimes be present, with over-the-top effects.

Here's a basic example:

Monster = 
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
{"abilities" :
"Water Shield - absorbs water-based attacks" : {
  "level1" : "-30% to Water-based damage",
  "level2" : "-40% to Water-based damage",
  "level3" : "-50% to Water-based damage",
  "level4" : "-60% to Water-based damage",
  "level5" : "-70% to Water-based damage"
  },
"Hypnosis - ability to put enemies under her control" : {
  "level1" : "Nearby Monsters become aligned with chance 5%",
  "level2" : "Nearby Monsters become aligned with chance 10%",
  "level3" : "Nearby Monsters become aligned with chance 25%",
  "level4" : "Nearby Monsters become aligned with chance 40%",
  "level5" : "Nearby Monsters become aligned with chance 50%"
  }
}

Here's a more complex example:

Monster = 
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

    "abilities" : "

    Output =
{"abilities" :
"Electro Healing - heals itself with plasma" : {
  "level1" : "+10% chance to heal when defending",
  "level2" : "+15 chance to heal when defending",
  "level3" : "+20% chance to heal when defending",
  "level4" : "+25% chance to heal when defending",
  "level5" : "+45% chance to heal when defending",
  },
"Legendary Crocus's Reverie" : {
  "level1" : "Monster must defend. Reduce all damage to 0, except from Cybor, Alien, Cold and Electrical.", 
  "level2" : "Monster must defend. Reduce all damage to 0, except from Cold and Alien.", 
  "level3" : "Monster must defend. Reduce all damage to 0, except from Cold, Electrical and Cyborg.", 
  "level4" : "Monster must defend. Reduce all damage to 0, except from Cyborg",
  "level5" : "Monster must defend. Reduce all damage to 0, except from Alien", 
  "levelX" : "Monster must defend and can not move. Reflect all damage +25%" 
  }
}

Input = %s

Output = 
"""
#generate_egg = """

hatch_egg = """ Given the egg parents as input, generate a new monster.

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
"abilities" : ["Tentacle Grab - melee attack enabling grappling and restraint",
"Energy Blast - long range energy projectile attack"]
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
"abilities" : ["Water Shield - absorbs water-based attacks", "Hypnosis - ability to put enemies under her control"],
"seed" : "Dark Naga Warrior"
}

  Child = 
"""

generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey Kung King Fu is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
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

    Input_prompt = %s
    
    Output = 
    """

make_seeds = """
    Generate %s new MonsterBattle 3001 monster seed phrases:

    1. red fox Hunter
    2. Giga Ape Druid
    3. Elemental octopus ninja
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
    18.
    """

generate_map_seeds = """
   Generate %s MonsterBattle 3001 map seed phrases.

   1. Snowy Tundra
   2. Outer Space Asteroid Habitat
   3. Jungle Fire Temple
   4. California State Insane Asylum
   5. Desert Monument
   6. Great Plains Western United States
   7. Scablands
   8. Mountain Monastery
   9. Surface of Mars
   """

