image_prefix = """Korean battle monster video game pixelated 64-bit """

#generate_egg = """

hatch_egg = """ Given the egg as input, generate a new monster 
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

  Child = {
      "description":
"""

generate_monster = """
    You always respond with just JSON. Nothing more, nothing less.

    Input_prompt = Fire Monkey Librarian

    Output = {"description" : "The Fire Monkey Kung King Fu is dangerously also an ancient and powerful librarian, responsible for shelving books in the temple library at Shau Kang. He attacks with arcane knowledge and raw firepower.",
    "name" : "Kung King Fu"
    "power" : "15",
    "toughness" : "8",
    "speed" : "29",
    "energy" : 10,
    "monster_types" : "Fire Ape Monk",
    "weakness" : "All forms of Water",
    "immunity" : "Mind Control and Temptation",
    "abilities" : "Fire Eye - range distance attack enabled",
    "seed" : "Fire Monkey Librarian"
    }

    Input_prompt = %s
    
    Output = 
    """


make_seeds = """
    Generate %s MonsterBattle 3001 monster seed phrases.

    1. red fox Hunter
    2. Giga Ape Druid
    3. Elemental octopus ninja
    4. Godzilla Uberdinosaur Spirit
    5. Undead zombie warlock
    6. Blue Dragon Lumberjack
    7. Dark Elf Detective
    8. Alien Cyborg Warrior
    9. Zombie Insect
    10. Giant Elk Priestess
    11. Elder Dragon Nicol Bolas
    12. Elemental Lightning Crew
    13. Apprentice Necromancer
    14. Skeleton
    15. Goblin Warrior
    16. Mutant Escapee
    17. Circus Freak Jailer
    18.
    """
